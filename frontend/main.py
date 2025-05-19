from PySide6.QtCore import QObject, QEvent, Qt
from PySide6.QtWidgets import QPushButton, QLabel, QApplication
from PySide6.QtGui import QFontMetrics
from qasync import QEventLoop
from app_manager import AppManager

import sys
import asyncio

if __name__ == "__main__":
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

    app = QApplication(sys.argv)
    app.setApplicationName("Security Environment Configuration Orchestrator")

    global_filter = GlobalEventFilter()
    app.installEventFilter(global_filter)

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