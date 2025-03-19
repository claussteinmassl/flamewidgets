from typing import Union, List, Dict, Optional, Callable
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui
from importlib.resources import files


class FlamePushButtonMenu(QtWidgets.QPushButton):
    """
    Custom Qt Flame Menu Push Button Widget

    FlamePushButtonMenu(button_name, menu_options[, menu_width=150, max_menu_width=2000, menu_action=None])

    button_name: [str] text displayed on button.
    menu_options: [list] options shown when button is pressed.
    menu_width: [int] (optional) width of widget. default is 150.
    max_menu_width: [int] (optional) set maximum width of widget. default is 2000.
    menu_action: [function] (optional) execute when button is changed.
    text_align: [str] (optional) align text left, center or right. default is center.

    To update an existing button menu:

    FlamePushButtonMenu.update_menu(button_name, menu_options[, menu_action=None])

    Examples:

        push_button_menu_options = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        menu_push_button = FlamePushButtonMenu('push_button_name', push_button_menu_options, text_align='left')

        or

        push_button_menu_options = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        menu_push_button = FlamePushButtonMenu(push_button_menu_options[0], push_button_menu_options, text_align='left')
    """

    def __init__(
            self,
            button_name: str,
            menu_options: List[str],
            menu_width: Optional[int] = 150,
            max_menu_width: Optional[int] = 2000,
            menu_action: Optional[Callable[..., None]] = None,
            text_align="center",
    ):
        super(FlamePushButtonMenu, self).__init__()
        from functools import partial

        # Check argument types

        if not isinstance(button_name, str):
            raise TypeError("FlamePushButtonMenu: button_name must be string.")
        if not isinstance(menu_options, list):
            raise TypeError("FlamePushButtonMenu: menu_options must be list.")
        if not isinstance(menu_width, int):
            raise TypeError("FlamePushButtonMenu: menu_width must be integer.")
        if not isinstance(max_menu_width, int):
            raise TypeError("FlamePushButtonMenu: max_menu_width must be integer.")
        if not text_align in ["left", "center", "right"]:
            raise ValueError(
                "FlamePushButtonMenu: align must be one of: left, center, right."
            )

        self.setProperty("text_align", text_align)

        # Store current selection
        self.current_selection = button_name

        # Build push button menu
        self.setText(button_name)
        self.setMinimumHeight(28)
        self.setMinimumWidth(menu_width)
        self.setMaximumWidth(max_menu_width)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet(
            "QPushButton {color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); border: none; text-align:"
            + text_align
            + '; padding-left: 10px; font: 14px "Artifakt Element"}'
              "QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(45, 55, 68); border: none}"
              "QPushButton:hover {border: 1px solid rgb(90, 90, 90)}"
              "QPushButton::menu-indicator {image: none}"
              "QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}"
        )

        # Load icons
        arrow_path = str(files("flamewidgets.resources").joinpath("dropdown_arrow.png"))
        self.arrow_icon = QtGui.QPixmap(arrow_path)

        # Load the current icon
        current_icon_path = str(files("flamewidgets.resources").joinpath("dropdown_current.png"))
        self.current_icon_pixmap = QtGui.QPixmap(current_icon_path)

        # Create a transparent icon of the same size to reserve icon space
        if not self.current_icon_pixmap.isNull():
            size = self.current_icon_pixmap.size()
            self.empty_pixmap = QtGui.QPixmap(size)
            self.empty_pixmap.fill(QtCore.Qt.transparent)
        else:
            print("WARNING: Could not load current selection icon")
            # Create a default empty pixmap if icon loading failed
            self.empty_pixmap = QtGui.QPixmap(16, 16)
            self.empty_pixmap.fill(QtCore.Qt.transparent)

        # Create a QMenu with proper style
        self.pushbutton_menu = QtWidgets.QMenu(self)
        self.pushbutton_menu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushbutton_menu.setMinimumWidth(menu_width)

        # Make icons visible explicitly with proper spacing
        self.pushbutton_menu.setStyleSheet(
            'QMenu {color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); border: none; font: 14px "Artifakt Element"}'
            "QMenu::item {padding: 5px 20px 5px 20px}"
            "QMenu::item:selected {color: rgb(217, 217, 217); background-color: rgb(58, 69, 81)}"
            "QMenu::icon {padding-left: 10px; margin-right: 10px}"
        )

        # Add menu items
        is_button_in_options = button_name in menu_options

        for menu in menu_options:
            action = QtGui.QAction(menu, self)
            action.triggered.connect(partial(self.create_menu, menu, menu_action))

            # Always show icons in menu
            action.setIconVisibleInMenu(True)

            # Set the current icon if this is the selected item
            if is_button_in_options and menu == button_name:
                action.setIcon(QtGui.QIcon(self.current_icon_pixmap))
            else:
                # Set empty icon to reserve space
                action.setIcon(QtGui.QIcon(self.empty_pixmap))

            self.pushbutton_menu.addAction(action)

        self.setMenu(self.pushbutton_menu)

    def create_menu(self, menu, menu_action):
        self.setText(menu)
        self.current_selection = menu

        # Update the icons for all actions
        for action in self.pushbutton_menu.actions():
            # Always ensure icon visibility
            action.setIconVisibleInMenu(True)

            if action.text() == menu:
                action.setIcon(QtGui.QIcon(self.current_icon_pixmap))
            else:
                # Set empty icon to reserve space
                action.setIcon(QtGui.QIcon(self.empty_pixmap))

        if menu_action:
            menu_action()

    def update_menu(self, button_name: str, menu_options: List[str], menu_action=None):
        from functools import partial

        self.setText(button_name)
        self.current_selection = button_name
        self.pushbutton_menu.clear()

        # Check if button_name is in menu_options
        is_button_in_options = button_name in menu_options

        for menu in menu_options:
            action = QtGui.QAction(menu, self)
            action.triggered.connect(partial(self.create_menu, menu, menu_action))

            # Always show icons in menu
            action.setIconVisibleInMenu(True)

            # Set the current icon if this is the selected item
            if is_button_in_options and menu == button_name:
                action.setIcon(QtGui.QIcon(self.current_icon_pixmap))
            else:
                # Set empty icon to reserve space
                action.setIcon(QtGui.QIcon(self.empty_pixmap))

            self.pushbutton_menu.addAction(action)

    def paintEvent(self, event):
        # Don't call super().paintEvent() to avoid double text drawing
        # Instead, draw everything ourselves

        painter = QtGui.QPainter(self)

        # Draw the button background
        option = QtWidgets.QStyleOptionButton()
        option.initFrom(self)
        option.state = QtWidgets.QStyle.State_Enabled
        if self.underMouse():
            option.state |= QtWidgets.QStyle.State_MouseOver
        if self.isDown():
            option.state |= QtWidgets.QStyle.State_Sunken

        # Draw the button without text
        self.style().drawControl(QtWidgets.QStyle.CE_PushButtonBevel, option, painter, self)

        # Draw the arrow icon
        if hasattr(self, 'arrow_icon') and not self.arrow_icon.isNull():
            icon_width = self.arrow_icon.width()
            icon_height = self.arrow_icon.height()
            # 10 pixels padding from the right edge
            x = self.width() - icon_width - 10
            y = (self.height() - icon_height) // 2
            painter.drawPixmap(x, y, self.arrow_icon)

        # Calculate text rect with proper padding
        padding = 10  # Base padding
        arrow_width = self.arrow_icon.width() if hasattr(self, 'arrow_icon') else 16
        text_rect = self.rect().adjusted(padding, 0, -(arrow_width + padding * 2), 0)

        # Get alignment
        text_align = self.property("text_align")
        if text_align == "left":
            alignment = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        elif text_align == "right":
            alignment = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
        else:  # center
            alignment = QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter

        # Draw the text with proper alignment and padding
        font = painter.font()
        font.setFamily("Artifakt Element")
        font.setPointSize(14)
        painter.setFont(font)
        painter.setPen(QtGui.QColor(154, 154, 154))
        painter.drawText(text_rect, alignment, self.text())

    # def paintEvent(self, event):
    #     super().paintEvent(event)
    #     if hasattr(self, 'arrow_icon') and not self.arrow_icon.isNull():
    #         painter = QtGui.QPainter(self)
    #         icon_width = self.arrow_icon.width()
    #         icon_height = self.arrow_icon.height()
    #         # 10 pixels padding from the right edge
    #         x = self.width() - icon_width - 10
    #         y = (self.height() - icon_height) // 2
    #         painter.drawPixmap(x, y, self.arrow_icon)