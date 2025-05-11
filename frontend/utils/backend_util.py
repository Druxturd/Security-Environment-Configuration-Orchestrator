from PyQt5.QtWidgets import QMainWindow, QProgressDialog, QMessageBox
from PyQt5.QtCore import Qt
from views.report_window_view import ReportWindow
from models.detail_report_model import DetailReportModel, PlaybookModel
from pydantic import BaseModel
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
        f"Host - IP Address: {x['host']} - {x['ip']}\nPlaybook: {y['name']}\nStatus: {y['status']}\nrc: {y['rc']}\nOutput: {y['stdout']}" for x in result['task_results'] for y in x['playbook_results']
    )
    # targetList = [
    #     {
    #         "host": x['host'],
    #         "ip": x['ip'],
    #         "playbooks": [
    #             {
    #                 "name": y['playbook'],
    #                 "status": y['status'],
    #                 "rc": y['rc'],
    #                 "stdout": y['stdout'],
    #                 "ok": y['events']['ok'],
    #                 "failed": y['events']['failed'],
    #                 "unreachable": y['events']['unreachable'],
    #                 "skipped": y['events']['skipped']
    #             }
    #         ]
    #     } for x in result['task_results'] for y in x['playbook_results']
    # ]
        
    #     targetList.append(target)
    #     print("")
    # for x in targetList:
    #     print(x.host)
    #     for y in x.playbooks:
    #         print(y['name'])
    # for x in result['task_results']:
    #     print(f"host - ip: {x['host']}")
    #     print("---------")
    #     for playbook_result in x['playbook_results']:
    #         events = playbook_result['events']
    #         playbook_start = playbook_result['playbook_start'][0]
    #         recap = playbook_result['recap'][0]
    #         print(playbook_start['stdout']+"\n\n")
    #         for y in events["all"]:
    #             print(y['event_data']['task'])
    #             print(y['stdout'])
    #             print("")
    #         print(recap['stdout']+"\n")
    targetList: list[testModel] = []
    for x in result['task_results']:
        targetList.append(testModel(host=x['host'], ip=x['ip'], playbook_results=x['playbook_results']))

    reportWindow = ReportWindow(report, targetList)
    reportWindow.exec()


class pbModel(BaseModel):
    name: str
    status: str
    rc: int
    playbook_start: list
    events: dict[str, list]
    recap: list
    stdout: str

    def __getitem__(self, key):
        return getattr(self, key)

class testModel(BaseModel):
    host: str
    ip: str
    playbook_results: list[pbModel]

    def __getitem__(self, key):
        return getattr(self, key)