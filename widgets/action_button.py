
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QGridLayout,
    QWidget,
    QPushButton
)


class ActionButton(QWidget):
    def __init__(self, parent=None, labelButton="Calculate"):
        super(ActionButton, self).__init__(parent)
        self.action_button = QPushButton(labelButton, self)
        self.action_button.setFixedWidth(200)

        # Создаем сетку для размещения виджетов
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.action_button)
        
        # Применяем сетку к виджетам
        self.setLayout(grid_layout)

 