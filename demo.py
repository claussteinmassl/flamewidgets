import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui
from importlib.resources import files
from flamewidgets import *


class DemoApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DemoApp, self).__init__(parent)

        self.setMinimumSize(QtCore.QSize(500, 500))
        self.setMaximumSize(QtCore.QSize(500, 500))
        self.setWindowTitle("Flame Widgets Demo")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setStyleSheet("background-color: #313131")

        self.button = FlameButton("This is a button", self.on_click)
        self.button2 = FlameButton("This is a button", self.on_click, button_color="blue")
        self.button3 = FlameButton("This is a button", self.on_click, button_color="red")
        self.label = FlameLabel("This is a label", "normal", 150, "left")
        self.line_edit = FlameLineEdit("This is a line edit", 150, 2000, self.on_click)
        self.line_edit_file_browse = FlameLineEditFileBrowse("This is a line edit file browse", "Python (*.py)")
        self.push_button = FlamePushButton("This is a push button", True, self.on_click, button_width=200)
        self.push_button_menu = FlamePushButtonMenu("push button menu (left)...", ["option 1", "option 2"], text_align="left")
        self.push_button_menu2 = FlamePushButtonMenu("push button menu (right)...", ["option 1", "option 2"], text_align="right")
        self.text_edit = FlameTextEdit("This is a text edit", False)
        self.token_push_button = FlameTokenPushButton("This is a token push button", {"token": "<value>"}, self.line_edit)
        self.tree_widget = FlameTreeWidget(["Column 1", "Column 2", "Column 3"])

        self.grid_layout = QtWidgets.QGridLayout()
        self.setLayout(self.grid_layout)
        self.grid_layout.addWidget(self.button)
        self.grid_layout.addWidget(self.button2)
        self.grid_layout.addWidget(self.button3)
        self.grid_layout.addWidget(self.label)
        self.grid_layout.addWidget(self.line_edit)
        self.grid_layout.addWidget(self.push_button)
        self.grid_layout.addWidget(self.push_button_menu)
        self.grid_layout.addWidget(self.push_button_menu2)
        self.grid_layout.addWidget(self.text_edit)
        self.grid_layout.addWidget(self.token_push_button)
        self.grid_layout.addWidget(self.tree_widget)

    def on_click(self):
        pass


if __name__ == "__main__":
    import sys
    import signal
    import os
    # make sure we can hit ctrl-c to exit the program
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    # create and show the gui
    app = QtWidgets.QApplication(sys.argv)
    font = str(files("flamewidgets.resources").joinpath("Artifakt Element Regular.ttf"))
    window = DemoApp()
    window.show()
    sys.exit(app.exec())


