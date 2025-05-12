from PySide6.QtWidgets import (
    QMainWindow,
    QProgressDialog
)
from PySide6.QtCore import Qt
from utils.message_box_util import *
from models.report_model import ReportModel
from views.report_window_view import ReportWindow
import httpx

async def execute_harden(main_window: QMainWindow, URL: str, payload):
    progressDialog = QProgressDialog("Running playbooks...", "Cancel", 0, 0, main_window, Qt.WindowType.FramelessWindowHint)
    progressDialog.setWindowTitle("Please wait...")
    progressDialog.setModal(True)
    progressDialog.setCancelButton(None)
    progressDialog.setEnabled(False)
    progressDialog.show()

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url=URL, json=payload, timeout=None)
            result = response.json()
    except Exception as e:
        result = {"error": str(e)}
    finally:
        progressDialog.close()

    if "error" in result:
        add_critical_msg_box(main_window, "Error", result['error'])
    else:
        _output_report(result)

def _output_report(result):
    report = "\n\n".join(
        f"Host - IP Address: {x['host']} - {x['ip']}\nPlaybook: {y['name']}\nStatus: {y['status']}\nrc: {y['rc']}\nOutput: {y['stdout']}" for x in result['task_results'] for y in x['playbook_results']
    )

    targetList: list[ReportModel] = []
    for x in result['task_results']:
        targetList.append(ReportModel(host=x['host'], ip=x['ip'], playbook_results=x['playbook_results']))

    reportWindow = ReportWindow(report, targetList)
    reportWindow.exec()