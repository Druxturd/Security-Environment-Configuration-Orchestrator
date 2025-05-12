from PySide6.QtWidgets import QApplication
from qasync import QEventLoop
from app_manager import AppManager

import sys
import asyncio

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Security Environment Configuration Orchestrator")

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