from PySide6.QtWidgets import (
    QLineEdit,
    QGridLayout,
    QLabel,
    QWidget
)


class InputFields(QWidget):
    def __init__(self, parent=None):
        super(InputFields, self).__init__(parent)
        grid_layout = QGridLayout()

        self.boiler_power_kW = QLabel("Мощность бойлера, кВт", self)
        self.boiler_power_kW_value = QLineEdit("450", self)
        grid_layout.addWidget(self.boiler_power_kW, 1, 0)
        grid_layout.addWidget(self.boiler_power_kW_value, 1, 1)

        self.power_recircle_kW = QLabel("Нагрузка циркуляции, кВт", self)
        self.power_recircle_kW_value = QLineEdit("193", self)
        grid_layout.addWidget(self.power_recircle_kW, 2, 0)
        grid_layout.addWidget(self.power_recircle_kW_value, 2, 1)

        self.boiler_volume_m3 = QLabel("Емкость бойлера, м3", self)
        self.boiler_volume_m3_value = QLineEdit("20", self)
        grid_layout.addWidget(self.boiler_volume_m3, 3, 0)
        grid_layout.addWidget(self.boiler_volume_m3_value, 3, 1)

        self.days = QLabel("Расчетное кол-во дней", self)
        self.days_value = QLineEdit("3", self)
        grid_layout.addWidget(self.days, 4, 0)
        grid_layout.addWidget(self.days_value, 4, 1)

        self.tw1 = QLabel("температура В1", self)
        self.tw1_value = QLineEdit("5", self)
        grid_layout.addWidget(self.tw1, 5, 0)
        grid_layout.addWidget(self.tw1_value, 5, 1)

        self.t3 = QLabel("температура Т3", self)
        self.t3_value = QLineEdit("65", self)
        grid_layout.addWidget(self.t3, 6, 0)
        grid_layout.addWidget(self.t3_value, 6, 1)

        self.t4 = QLabel("температура Т4", self)
        self.t4_value = QLineEdit("55", self)
        grid_layout.addWidget(self.t4, 7, 0)
        grid_layout.addWidget(self.t4_value, 7, 1)

        self.t3_boiler = QLabel("температура нагрева бойлера", self)
        self.t3_boiler_value = QLineEdit("65", self)
        grid_layout.addWidget(self.t3_boiler, 8, 0)
        grid_layout.addWidget(self.t3_boiler_value, 8, 1)

        self.G_day = QLabel("Суточный расход, м3/ч", self)
        self.G_day_value = QLineEdit("36", self)
        grid_layout.addWidget(self.G_day, 9, 0)
        grid_layout.addWidget(self.G_day_value, 9, 1)

        self.hours = QLabel("Часы работы", self)
        self.hours_value = QLineEdit("24", self)
        grid_layout.addWidget(self.hours, 10, 0)
        grid_layout.addWidget(self.hours_value, 10, 1)

        self.G_mid_hour = QLabel("Среднечасовой расход, м3/ч", self)
        self.G_mid_hour_value = QLineEdit(str(float(self.G_day_value.text()) / float(self.hours_value.text())), self )
        grid_layout.addWidget(self.G_mid_hour, 11, 0)
        grid_layout.addWidget(self.G_mid_hour_value, 11, 1)

        self.G_max_hour = QLabel("Максимально-часовой расход, м3/ч", self)
        self.G_max_hour_value = QLineEdit("13.869", self )
        grid_layout.addWidget(self.G_max_hour, 12, 0)
        grid_layout.addWidget(self.G_max_hour_value, 12, 1)

        self.G_min_hour = QLabel("Минимальный часовой расход, м3/ч", self)
        self.G_min_value = QLineEdit("0.487", self )
        grid_layout.addWidget(self.G_min_hour, 13, 0)
        grid_layout.addWidget(self.G_min_value, 13, 1)


        # Применяем сетку к виджетам
        self.setLayout(grid_layout)
  


            
