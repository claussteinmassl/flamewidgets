from typing import Union, List, Dict, Optional, Callable
from PySide6 import QtWidgets
from PySide6 import QtCore


class FlameListWidget(QtWidgets.QListWidget):
    """
    Custom Qt Flame List Widget

    FlameListWidget([min_width=200, max_width=2000, min_height=250, max_height=2000])

    Example:
        list_widget = FlameListWidget()
    """

    def __init__(
        self,
        min_width: Optional[int] = 200,
        max_width: Optional[int] = 2000,
        min_height: Optional[int] = 250,
        max_height: Optional[int] = 2000,
    ):
        super(FlameListWidget, self).__init__()

        # Check argument types

        if not isinstance(min_width, int):
            raise TypeError("FlameListWidget: min_width must be integer.")
        if not isinstance(max_width, int):
            raise TypeError("FlameListWidget: max_width must be integer.")
        if not isinstance(min_height, int):
            raise TypeError("FlameListWidget: min_height must be integer.")
        if not isinstance(max_height, int):
            raise TypeError("FlameListWidget: max_height must be integer.")

        # Build list widget

        self.setMinimumWidth(min_width)
        self.setMaximumWidth(max_width)
        self.setMinimumHeight(min_height)
        self.setMaximumHeight(max_height)
        self.spacing()
        self.setUniformItemSizes(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setAlternatingRowColors(True)
        self.setStyleSheet(
            'QListWidget {color: rgb(154, 154, 154); background-color: rgb(30, 30, 30); alternate-background-color: rgb(36, 36, 36); outline: 3px rgb(0, 0, 0); font: 14px "Artifakt Element"}'
            "QListWidget::item:selected {color: rgb(217, 217, 217); background-color: rgb(102, 102, 102); border: 1px solid rgb(102, 102, 102)}"
            "QScrollBar {background: rgb(61, 61, 61)}"
            "QScrollBar::handle {background: rgb(31, 31, 31)}"
            "QScrollBar::add-line:vertical {border: none; background: none; width: 0px; height: 0px}"
            "QScrollBar::sub-line:vertical {border: none; background: none; width: 0px; height: 0px}"
            "QScrollBar {background: rgb(61, 61, 61)}"
            "QScrollBar::handle {background: rgb(31, 31, 31)}"
            "QScrollBar::add-line:horizontal {border: none; background: none; width: 0px; height: 0px}"
            "QScrollBar::sub-line:horizontal {border: none; background: none; width: 0px; height: 0px}"
            "QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}"
        )
