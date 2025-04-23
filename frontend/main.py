from PyQt5.QtWidgets import QApplication
from qasync import QEventLoop
from app_manager import AppManager
import sys
import asyncio

# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Security Environment Configuration Orchestrator")

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    manager = AppManager()
    manager.main_window.show()

    async def cleanup():
        print("Cleaning up...")

    with loop:
        try:
            loop.run_forever()
        finally:
            loop.run_until_complete(cleanup())
