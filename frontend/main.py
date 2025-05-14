from PySide6.QtCore import QObject, QEvent, Qt
from PySide6.QtWidgets import QPushButton, QApplication
from qasync import QEventLoop
from app_manager import AppManager

import sys
import asyncio

if __name__ == "__main__":
    class FocusFilter(QObject):
        def eventFilter(self, obj, event):
            if isinstance(obj, QPushButton) and event.type() == QEvent.Type.Show:
                obj.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            return super().eventFilter(obj, event)

    app = QApplication(sys.argv)
    app.setApplicationName("Security Environment Configuration Orchestrator")

    focus_filter = FocusFilter()
    app.installEventFilter(focus_filter)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    manager = AppManager()
    manager.main_window.show()

    async def clean_up():
        print("Cleaning up...")
    
    with loop:
        try:
            loop.run_forever()
        finally:
            loop.run_until_complete(clean_up())