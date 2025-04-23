from PyQt5.QtWidgets import QMainWindow, QProgressDialog, QMessageBox
from PyQt5.QtCore import Qt
from views.utils_view import ReportWindow
import httpx

async def executeHarden(main_window:QMainWindow, URL:str, payload):
    progressDialog = QProgressDialog("Running playbooks...", None, 0, 0, main_window, Qt.WindowType.FramelessWindowHint)
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
        QMessageBox.critical(main_window, "Error", result['error'])
    else:
        _outputReport(result)

def _outputReport(result):
    
    report = "\n\n".join(
        f"IPAddress: {x['host']}\nPlaybook: {y['playbook']}\nStatus: {y['Status']}\nrc: {y['rc']}\nOutput: {y['stdout']}" for x in result['results'] for y in x['results']
    )
    reportWindow = ReportWindow(report)
    reportWindow.exec()