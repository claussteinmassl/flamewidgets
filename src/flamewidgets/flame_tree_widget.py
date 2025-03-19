from typing import Union, List, Dict, Optional, Callable
from PySide6 import QtWidgets
from PySide6 import QtCore


class FlameTreeWidget(QtWidgets.QTreeWidget):
    """
    Custom Qt Flame Tree Widget

    FlameTreeWidget(tree_headers[, connect=None, tree_min_width=100, tree_min_height=100])

    tree_headers: list of names to be used for column names in tree [list]
    connect: execute when item in tree is clicked on [function]
    tree_min_width = set tree width [int]
    tree_min_height = set tree height [int]

    Exmaple:

        tree_headers = ['Header1', 'Header2', 'Header3', 'Header4']
        tree = FlameTreeWidget(tree_headers)
    """

    def __init__(
        self,
        tree_headers: List[str],
        connect: Optional[Callable[..., None]] = None,
        tree_min_width: Optional[int] = 100,
        tree_min_height: Optional[int] = 100,
    ):
        super(FlameTreeWidget, self).__init__()

        # Check argument types

        if not isinstance(tree_headers, list):
            raise TypeError("FlameTreeWidget: tree_headers must be a list")
        if not isinstance(tree_min_width, int):
            raise TypeError("FlameTreeWidget: tree_min_width must be an integer")
        if not isinstance(tree_min_height, int):
            raise TypeError("FlameTreeWidget: tree_min_height must be an integer")

        # Build tree widget

        self.setMinimumWidth(tree_min_width)
        self.setMinimumHeight(tree_min_height)
        self.setSortingEnabled(True)
        self.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.setAlternatingRowColors(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clicked.connect(connect)
        self.setStyleSheet(
            'QTreeWidget {color: rgb(154, 154, 154); background-color: rgb(30, 30, 30); alternate-background-color: rgb(36, 36, 36); border: none; font: 14px "Artifakt Element"}'
            'QHeaderView::section {color: rgb(154, 154, 154); background-color: rgb(57, 57, 57); border: none; padding-left: 10px; font: 14px "Artifakt Element"}'
            'QTreeWidget:item:selected {color: rgb(217, 217, 217); background-color: rgb(71, 71, 71); selection-background-color: rgb(153, 153, 153); border: 1px solid rgb(17, 17, 17); font: 14px "Artifakt Element"}'
            'QTreeWidget:item:selected:active {color: rgb(153, 153, 153); border: none; font: 14px "Artifakt Element"}'
            'QTreeWidget:disabled {color: rgb(101, 101, 101); background-color: rgb(34, 34, 34); font: 14px "Artifakt Element"}'
            'QMenu {color: rgb(154, 154, 154); background-color: rgb(36, 48, 61); font: 14px "Artifakt Element"}'
            'QMenu::item:selected {color: rgb(217, 217, 217); background-color: rgb(58, 69, 81); font: 14px "Artifakt Element"}'
            "QScrollBar {color: rgb(17, 17, 17); background: rgb(49, 49, 49)}"
            "QScrollBar::handle {color: rgb(17, 17, 17)}"
            "QScrollBar::add-line:vertical {border: none; background: none; width: 0px; height: 0px}"
            "QScrollBar::sub-line:vertical {border: none; background: none; width: 0px; height: 0px}"
            "QScrollBar {color: rgb(17, 17, 17); background: rgb(49, 49, 49)}"
            "QScrollBar::handle {color: rgb(17, 17, 17)}"
            "QScrollBar::add-line:horizontal {border: none; background: none; width: 0px; height: 0px}"
            "QScrollBar::sub-line:horizontal {border: none; background: none; width: 0px; height: 0px}"
        )

        self.setHeaderLabels(tree_headers)
