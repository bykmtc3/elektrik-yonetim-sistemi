import sys
from PyQt6 import QtWidgets, QtCore

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QtWidgets.QVBoxLayout()

        self.username_label = QtWidgets.QLabel('Username:')
        self.layout.addWidget(self.username_label)

        self.username_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.username_input)

        self.password_label = QtWidgets.QLabel('Password:')
        self.layout.addWidget(self.password_label)

        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QtWidgets.QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

    def login(self):
        # Placeholder for login logic
        print('Logging in...')
        self.main_dashboard = MainDashboard()
        self.main_dashboard.show()
        self.close()

class MainDashboard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Dashboard')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QtWidgets.QVBoxLayout()

        self.dashboard_label = QtWidgets.QLabel('Welcome to the Dashboard!')
        self.layout.addWidget(self.dashboard_label)

        self.module_access_button = QtWidgets.QPushButton('Access Module')
        self.module_access_button.clicked.connect(self.access_module)
        self.layout.addWidget(self.module_access_button)

        self.setLayout(self.layout)

    def access_module(self):
        # Placeholder for module access logic
        print('Accessing module...')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())