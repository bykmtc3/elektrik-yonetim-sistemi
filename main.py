import sys
from PyQt6.QtWidgets import QApplication
from ui_advanced import MainWindow
from config import Config
from security import SecurityManager
from logger import Logger

logger = Logger()

def main():
    try:
        # Initialize security
        security = SecurityManager()
        
        # Check authentication
        if not security.verify_admin():
            logger.log("SECURITY", "Unauthorized access attempt")
            return
        
        # Start application
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
        
    except Exception as e:
        logger.log("ERROR", f"Application failed: {str(e)}")
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()