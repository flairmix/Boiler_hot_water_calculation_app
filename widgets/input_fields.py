from PySide6.QtWidgets import (
    QLineEdit,
    QGridLayout,
    QLabel,
    QWidget
)


class InputFields(QWidget):
    def __init__(self, parent=None):
        super(InputFields, self).__init__(parent)

        self.name = QLabel("calculation_name", self)
        self.boiler_power_kW = QLabel("Мощность бойлера, кВт", self)
        self.power_recircle_kW = QLabel("Нагрузка циркуляции, кВт", self)
        self.boiler_volume_m3 = QLabel("Емкость бойлера, м3", self)
        self.hw_reserve_init = QLabel("Изначальная загрузка бойлера, м3", self)
        self.days = QLabel("Расчетное кол-во дней", self)
        # self.consumption_by_hours_24 = consumption_1
        self.tw1 = QLabel("температура В1", self)
        self.t3 = QLabel("температура Т3", self)
        self.t4 = QLabel("температура Т4", self)
        self.t3_boiler = QLabel("температура нагрева бойлера", self)

        self.name_value = QLineEdit("calculation_name", self)
        self.boiler_power_kW_value = QLineEdit("600", self)
        self.power_recircle_kW_value = QLineEdit("193", self)
        self.boiler_volume_m3_value = QLineEdit("20", self)
        self.hw_reserve_init_value = QLineEdit("20", self)
        self.days_value = QLineEdit("3", self)
        # self.consumption_by_hours_24_value = QLineEdit("", self)
        self.tw1_value = QLineEdit("5", self)
        self.t3_value = QLineEdit("65", self)
        self.t4_value = QLineEdit("55", self)
        self.t3_boiler_value = QLineEdit("65", self)
        
        # Создаем сетку для размещения виджетов
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.name, 2, 0)
        grid_layout.addWidget(self.name_value, 2, 1)
        grid_layout.addWidget(self.boiler_power_kW, 3, 0)
        grid_layout.addWidget(self.boiler_power_kW_value, 3, 1)
        grid_layout.addWidget(self.power_recircle_kW, 4, 0)
        grid_layout.addWidget(self.power_recircle_kW_value, 4, 1)
        grid_layout.addWidget(self.boiler_volume_m3, 5, 0)
        grid_layout.addWidget(self.boiler_volume_m3_value, 5, 1)
        grid_layout.addWidget(self.hw_reserve_init, 6, 0)
        grid_layout.addWidget(self.hw_reserve_init_value, 6, 1)
        grid_layout.addWidget(self.days, 7, 0)
        grid_layout.addWidget(self.days_value, 7, 1)
        grid_layout.addWidget(self.tw1, 8, 0)
        grid_layout.addWidget(self.tw1_value, 8, 1)
        grid_layout.addWidget(self.t3, 9, 0)
        grid_layout.addWidget(self.t3_value, 9, 1)
        grid_layout.addWidget(self.t4, 10, 0)
        grid_layout.addWidget(self.t4_value, 10, 1)
        grid_layout.addWidget(self.t3_boiler, 11, 0)
        grid_layout.addWidget(self.t3_boiler_value, 11, 1)

        # Применяем сетку к виджетам
        self.setLayout(grid_layout)
  


            
