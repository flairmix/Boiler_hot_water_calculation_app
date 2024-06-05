from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QWidget,
    QTextEdit
)


class PredefinedTextWidget(QWidget):
    def __init__(self, parent=None, text="Ваш заранее написанный текст"):
        super(PredefinedTextWidget, self).__init__(parent)
        self.text_label = QLabel(text, self)
        
        # Создаем сетку для размещения виджета
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.text_label)
        
        # Применяем сетку к виджетам
        self.setLayout(grid_layout)


class DescriptionField(QWidget):
    def __init__(self, parent=None):
        super(DescriptionField, self).__init__(parent)
        self.description_label = QLabel("Description:", self)
        self.description_text = QTextEdit(self)
        self.description_text.setFixedHeight(25)
        
        # Создаем сетку для размещения виджетов
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.description_label, 0, 0)
        grid_layout.addWidget(self.description_text, 0, 1)
        
        # Применяем сетку к виджетам
        self.setLayout(grid_layout)