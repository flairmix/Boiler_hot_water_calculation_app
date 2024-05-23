from PySide6.QtWidgets import (
    QLineEdit,
    QGridLayout,
    QLabel,
    QWidget
)


class InputFieldsConsumption(QWidget):
    def __init__(self, parent=None):
        super(InputFieldsConsumption, self).__init__(parent)

        self.heading = QLabel("Расход по часам, м3/ч", self)
        self.heading.setFixedWidth(100)
        self.hour_0 = QLabel("00 : 00", self)
        self.hour_0_value = QLineEdit("0.487", self)




        
        # Создаем сетку для размещения виджетов
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.heading, 0, 1)
        grid_layout.addWidget(self.hour_0, 2, 0)
        grid_layout.addWidget(self.hour_0_value, 2, 1)


        # Применяем сетку к виджетам
        self.setLayout(grid_layout)
  


            
