from typing import Union, List, Dict, Optional, Callable
from PySide6 import QtWidgets
from PySide6 import QtCore


class FlameButton(QtWidgets.QPushButton):
    """
    Custom Qt Flame Button Widget

    FlameButton(button_name, connect[, button_color='normal', button_width=150, button_max_width=150])

    button_name: button text [str]
    connect: execute when clicked [function]
    button_color: (optional) normal, blue, red [str]
    button_width: (optional) default is 150 [int]
    button_max_width: (optional) default is 150 [int]

    Example:

        button = FlameButton('Button Name', do_something_magical_when_pressed, button_color='blue')
    """

    def __init__(
        self,
        button_name: str,
        connect: Callable[..., None],
        button_color: Optional[str] = "normal",
        button_width: Optional[int] = 150,
        button_max_width: Optional[int] = 150,
        tooltip: Optional[str] = None,
    ) -> None:

        super(FlameButton, self).__init__()

        # Check argument types

        if not isinstance(button_name, str):
            raise TypeError("FlameButton: button_name must be a string")
        elif button_color not in ["normal", "blue", "red"]:
            raise ValueError(
                "FlameButton: button_color must be one of: normal(grey), blue, or red"
            )
        elif not isinstance(button_width, int):
            raise TypeError("FlameButton: button_width must be an integer")
        elif not isinstance(button_max_width, int):
            raise TypeError("FlameButton: button_max_width must be an integer")

        # Build button

        self.setText(button_name)
        self.setMinimumSize(QtCore.QSize(button_width, 28))
        self.setMaximumSize(QtCore.QSize(button_max_width, 28))
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clicked.connect(connect)

        self.setToolTip(tooltip)
        if button_color == "normal":
            self.setStyleSheet(
                'QPushButton {color: rgb(154, 154, 154); background-color: rgb(58, 58, 58); border: none; font: 14px "Artifakt Element"}'
                "QPushButton:hover {border: 1px solid rgb(90, 90, 90)}"
                "QPushButton:pressed {color: rgb(159, 159, 159); background-color: rgb(66, 66, 66); border: 1px solid rgb(90, 90, 90)}"
                "QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(58, 58, 58); border: none}"
                "QPushButton::menu-indicator {subcontrol-origin: padding; subcontrol-position: center right}"
                "QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}"
            )
        elif button_color == "blue":
            self.setStyleSheet(
                'QPushButton {color: rgb(190, 190, 190); background-color: rgb(58, 108, 173); border: none; font: 14px "Artifakt Element"}'
                "QPushButton:hover {border: 2px solid rgb(90, 90, 90)}"
                "QPushButton:pressed {color: rgb(159, 159, 159); border: 1px solid rgb(90, 90, 90)"
                "QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(58, 58, 58); border: none}"
                "QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}"
            )
        elif button_color == "red":
            self.setStyleSheet(
                'QPushButton {color: rgb(190, 190, 190); background-color: rgb(200, 29, 29); border: none; font: 14px "Artifakt Element"}'
                "QPushButton:hover {border: 1px solid rgb(90, 90, 90)}"
                "QPushButton:pressed {color: rgb(159, 159, 159); border: 1px solid rgb(90, 90, 90)"
                "QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(58, 58, 58); border: none}"
                "QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}"
            )
