from PyQt5.QtWidgets import QApplication
from qasync import QEventLoop
from views.main_window_view import MainWindow
import sys
import asyncio

# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Security Environment Configuration Orchestrator")

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    async def cleanup():
        print("Cleaning up...")

    with loop:
        try:
            loop.run_forever()
        finally:
            loop.run_until_complete(cleanup())
