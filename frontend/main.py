import asyncio
import os
import platform
import signal
import subprocess
import sys

from dotenv import load_dotenv
from qasync import QEventLoop

from frontend.app_manager import AppManager
from PySide6.QtCore import QEvent, QObject, Qt
from PySide6.QtGui import QFontMetrics
from PySide6.QtWidgets import QApplication, QLabel, QPushButton

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))


class GlobalEventFilter(QObject):
    def eventFilter(self, obj, event):
        if isinstance(obj, QPushButton) and event.type() == QEvent.Type.Show:
            obj.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        if isinstance(obj, QLabel) and event.type() == QEvent.Type.Resize:
            obj.setWordWrap(True)
            metrics = QFontMetrics(obj.font())
            full_width = metrics.horizontalAdvance(obj.text())
            if full_width > obj.width():
                obj.setToolTip(obj.text())
            else:
                obj.setToolTip("")

        return super().eventFilter(obj, event)


def start_backend():
    backend_dir = os.path.join(os.path.dirname(__file__), "..", "backend")
    backend_script = os.path.join(backend_dir, "main.py")
    return subprocess.Popen([sys.executable, backend_script])


def terminate_process(proc):
    if proc.poll() is not None:
        return
    system = platform.system()
    if system == "Windows":
        proc.terminate()
    else:
        proc.send_signal(signal.SIGINT)
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()


async def clean_up():
    print("Cleaning up...")


if __name__ == "__main__":
    backend_proc = start_backend()

    app = QApplication(sys.argv)
    app.setApplicationName("Security Environment Configuration Orchestrator")

    global_filter = GlobalEventFilter()
    app.installEventFilter(global_filter)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    manager = AppManager()
    manager.main_window.show()

    app.aboutToQuit.connect(lambda: terminate_process(backend_proc))

    with loop:
        try:
            loop.run_forever()
        finally:
            loop.run_until_complete(clean_up())
            loop.close()
            terminate_process(backend_proc)
