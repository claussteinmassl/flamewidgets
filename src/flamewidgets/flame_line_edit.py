from typing import Union, List, Dict, Optional, Callable
from PySide6 import QtWidgets
from PySide6 import QtCore


class FlameLineEdit(QtWidgets.QLineEdit):
    """
    Custom Qt Flame Line Edit Widget

    FlameLineEdit(text[, width=150, max_width=2000, text_changed=some_function])

    text: [str] text shown in line edit
    width: [int] (optional) width of widget. default is 150.
    max_width: [int] (optional) maximum width of widget. default is 2000.
    text_changed: [function] (optional) function to call when text is changed.
    return_pressed: [function] (optional) function to call when return is pressed.

    Example:
        line_edit = FlameLineEdit('Some text here')
    """

    def __init__(
        self,
        text: str,
        width: Optional[int] = 150,
        max_width: Optional[int] = 2000,
        text_changed: Optional[Callable] = None,
        placeholder_text: Optional[str] = None,
        return_pressed: Optional[Callable] = None,
    ):
        super(FlameLineEdit, self).__init__()

        # Check argument types
        if not isinstance(text, str) and not isinstance(text, int):
            raise TypeError("FlameLineEdit: text must be string or int.")
        if not isinstance(width, int):
            raise TypeError("FlameLineEdit: width must be integer.")
        if not isinstance(max_width, int):
            raise TypeError("FlameLineEdit: max_width must be integer.")

        text = str(text)

        # Build line edit
        self.setText(text)
        self.setMinimumHeight(28)
        self.setMinimumWidth(width)
        self.setMaximumWidth(max_width)
        # self.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textChanged.connect(text_changed)
        self.setPlaceholderText(placeholder_text)
        self.setStyleSheet(
            'QLineEdit {color: rgb(154, 154, 154); background-color: rgb(55, 65, 75); selection-color: rgb(38, 38, 38); selection-background-color: rgb(184, 177, 167); border: 1px solid rgb(55, 65, 75); padding-left: 5px; font: 14px "Artifakt Element"}'
            "QLineEdit:focus {background-color: rgb(73, 86, 99)}"
            "QLineEdit:hover {border: 1px solid rgb(90, 90, 90)}"
            "QLineEdit:disabled {color: rgb(106, 106, 106); background-color: rgb(55, 55, 55); border: 1px solid rgb(55, 55, 55)}"
            "QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: none}"
        )

        if return_pressed:
            self.returnPressed.connect(return_pressed)
