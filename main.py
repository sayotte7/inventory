import os, json, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

version = '1.00.000'

storage_file = 'storage.json'

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle(f"FXC Inventory Management Solution (FIMs) v{version}")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #333333; color: #ffffff")

        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        layout = QVBoxLayout()

        button_group = QVBoxLayout()
        self.button_inventory = QPushButton("Inventory")
        self.button_inventory.installEventFilter(self)
        self.button_inventory.setStyleSheet("""
                QPushButton {
                    background-color: #007bff;
                    color: #ffffff;
                    font-size: 25px;
                    padding: 8px 16px;
                    border-radius: 15px;
                }
                QPushButton:hover {
                    background-color: #0056b3;
                }
            """)
        self.button_checkout = QPushButton("Check Out")
        self.button_checkout.installEventFilter(self)
        self.button_checkout.setStyleSheet("""
                QPushButton {
                    background-color: #007bff;
                    color: #ffffff;
                    font-size: 25px;
                    padding: 8px 16px;
                    border-radius: 15px;
                }
                QPushButton:hover {
                    background-color: #0056b3;
                }
            """)
        button_group.addWidget(self.button_inventory)
        button_group.addWidget(self.button_checkout)

        layout.addLayout(button_group)
        widget_central.setLayout(layout)

        self.window_inventory = QVBoxLayout()
        self.label_window_inventory = QLabel("Inventory")
        self.label_window_inventory.setAlignment(Qt.AlignCenter)
        self.button_add_window_inventory = QPushButton("Add Inventory")
        self.button_add_window_inventory.installEventFilter(self)
        self.button_add_window_inventory.setStyleSheet("""
                QPushButton {
                    background-color: #007bff;
                    color: #ffffff;
                    font-size: 25px;
                    padding: 8px 16px;
                    border-radius: 15px;
                }
                QPushButton:hover {
                    background-color: #0056b3;
                }
            """)
        list_window_inventory = QListWidget()

    def toggle_window_inventory(self):
        if self.window_inventory.isHidden():
            

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.RightButton:
                return True
            elif event.button() == Qt.LeftButton:
                return True
        return False

def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()