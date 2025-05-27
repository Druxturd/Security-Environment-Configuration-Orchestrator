import httpx

from frontend.models.report_model import (
    ReportModel,
    SelectedHardenReportModel,
)
from frontend.views.report_window_view import ReportWindowView
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox, QProgressDialog


async def execute_harden(main_window: QMainWindow, URL: str, payload):
    progressDialog = QProgressDialog(
        "Running playbooks...",
        "Cancel",
        0,
        0,
        main_window,
        Qt.WindowType.FramelessWindowHint,
    )
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
        QMessageBox.critical(main_window, "Error", result["error"])
    else:
        _output_report(result)


async def execute_patch(main_window: QMainWindow, URL: str, payload):
    progressDialog = QProgressDialog(
        "Running playbooks...",
        "Cancel",
        0,
        0,
        main_window,
        Qt.WindowType.FramelessWindowHint,
    )
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
        QMessageBox.critical(main_window, "Error", result["error"])
    else:
        _output_report(result)


def _output_report(result):
    if "task_results" in result:
        report = "\n\n".join(
            f"Host - IP Address: {x['host']} - {x['ip']}\nPlaybook: {y['name']}\nStatus: {y['status']}\nrc: {y['rc']}\nOutput: {y['stdout']}"
            for x in result["task_results"]
            for y in x["playbook_results"]
        )

        target_list: list[ReportModel] = []
        for x in result["task_results"]:
            target_list.append(
                ReportModel(
                    host=x["host"], ip=x["ip"], playbook_results=x["playbook_results"]
                )
            )
        report_window = ReportWindowView(report, target_list)
        report_window.exec()

    elif "auto_harden_results" in result:
        auto_target_list: list[ReportModel] = []
        for res in result["auto_harden_results"]:
            for x in res:
                auto_target_list.append(
                    ReportModel(
                        host=x["host"],
                        ip=x["ip"],
                        playbook_results=x["playbook_results"],
                    )
                )

        report = "\n\n".join(
            f"Host - IP Address: {x.host} - {x.ip}\nPlaybook: {y.name}\nStatus: {y.status}\nrc: {y.rc}\nOutput: {y.stdout}"
            for x in auto_target_list
            for y in x.playbook_results
        )
        report_window = ReportWindowView(report, auto_target_list)
        report_window.exec()

    elif "selected_harden_results" in result or "semi_auto_harden_results" in result:
        selected_target_list: list[SelectedHardenReportModel] = []
        if "selected_harden_results" in result:
            for res in result["selected_harden_results"]:
                for x in res:
                    selected_target_list.append(
                        SelectedHardenReportModel(
                            host=x["host"],
                            ip=x["ip"],
                            playbook_results=x["playbook_results"],
                        )
                    )
        elif "semi_auto_harden_results" in result:
            for res in result["semi_auto_harden_results"]:
                for x in res:
                    selected_target_list.append(
                        SelectedHardenReportModel(
                            host=x["host"],
                            ip=x["ip"],
                            playbook_results=x["playbook_results"],
                        )
                    )
        report = "\n\n".join(
            f"Host - IP Address: {x.host} - {x.ip}\nPlaybook: {y.name}\nStatus: {y.status}\nrc: {y.rc}\nOutput: {y.stdout}"
            for x in selected_target_list
            for y in x.playbook_results
        )
        report_window = ReportWindowView(report, selected_target_list)
        report_window.exec()
