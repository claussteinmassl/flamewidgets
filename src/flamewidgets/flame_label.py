from typing import Union, List, Dict, Optional, Callable
from PySide6 import QtWidgets
from PySide6 import QtCore


class FlameLabel(QtWidgets.QLabel):
    """
    Custom Qt Flame Label Widget

    FlameLabel(label_name[, label_type='normal', label_width=150, align=''])

    label_name: [str] label text.
    label_type: [str] (optional) select from different styles: normal, underline, background. default is normal.
    label_width: [int] (optional) default is 150.
    align: [str] (optional) align text to left, right, or center. defaults: normal=left, underline=center, background=left.

    Example:

        label = FlameLabel('Label Name', label_type='underline', label_width=300, align='left')
    """

    def __init__(
        self,
        label_name: str,
        label_type: Optional[str] = "normal",
        label_width: Optional[int] = 150,
        align: Optional[str] = "",
    ):
        super(FlameLabel, self).__init__()

        # Check argument types

        if not isinstance(label_name, str):
            raise TypeError("FlameLabel: label_name must be a string")
        elif not isinstance(label_type, str):
            raise TypeError("FlameLabel: label_type must be a string")
        elif label_type not in ["normal", "underline", "background", "border"]:
            raise ValueError(
                "FlameLabel: label_type must be one of: normal, underline, background"
            )
        elif not isinstance(label_width, int):
            raise TypeError("FlameLabel: label_width must be an integer")

        # Build label

        self.setText(label_name)
        self.setMinimumSize(label_width, 28)
        self.setMaximumHeight(28)
        self.setFixedHeight(28)
        self.setFocusPolicy(QtCore.Qt.NoFocus)

        # Set label stylesheet based on label_type

        if align == "left":
            self.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        elif align == "right":
            self.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        elif align == "center":
            self.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        elif align == "" and label_type == "normal":
            self.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        elif align == "" and label_type == "underline":
            self.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        elif align == "" and label_type == "background":
            self.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        elif align == "" and label_type == "border":
            self.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        if label_type == "normal":
            self.setStyleSheet(
                'QLabel {color: rgb(154, 154, 154); font: 14px "Artifakt Element"}'
                "QLabel:disabled {color: rgb(106, 106, 106)}"
            )
        elif label_type == "underline":
            self.setStyleSheet(
                'QLabel {color: rgb(154, 154, 154); border-bottom: 1px inset rgb(40, 40, 40); font: 14px "Artifakt Element"}'
                "QLabel:disabled {color: rgb(106, 106, 106)}"
            )
        elif label_type == "background":
            self.setStyleSheet(
                'QLabel {color: rgb(154, 154, 154); background-color: rgb(30, 30, 30); padding-left: 5px; font: 14px "Artifakt Element"}'
                "QLabel:disabled {color: rgb(106, 106, 106)}"
            )
        if label_type == "border":
            self.setStyleSheet(
                'QLabel {color: rgb(154, 154, 154); border: 1px solid #404040; font: 14px "Artifakt Element"}'
                "QLabel:disabled {color: rgb(106, 106, 106)}"
            )
