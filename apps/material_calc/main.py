import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QComboBox,
)


class ThermalCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # Данные по регионам (СП 50.13330.2012)
        self.regions = {
            "Москва и МО": {"Стена": 3.15, "Крыша": 4.95, "Пол": 2.5, "Тнаруж": -22},
            "Санкт-Петербург": {"Стена": 3.05, "Крыша": 4.8, "Пол": 2.4, "Тнаруж": -20},
            "Новосибирск": {"Стена": 3.7, "Крыша": 5.5, "Пол": 3.0, "Тнаруж": -35},
            "Красноярск": {"Стена": 4.2, "Крыша": 6.0, "Пол": 3.5, "Тнаруж": -38},
            "Якутск": {"Стена": 5.2, "Крыша": 7.0, "Пол": 4.5, "Тнаруж": -50},
            "Свой вариант": None,  # Позволяет ввести вручную
        }

        # Данные по материалам
        self.materials = {
            "Пенополистирол (0.035 Вт/м·К)": 0.035,
            "Минеральная вата (0.040 Вт/м·К)": 0.040,
            "Пенополиуретан (0.025 Вт/м·К)": 0.025,
            "Керамзит (0.120 Вт/м·К)": 0.120,
            "Газобетон (0.120 Вт/м·К)": 0.120,
            "Свой вариант": None,
        }

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Выбор региона
        self.label_region = QLabel("Выберите регион:")
        self.combo_region = QComboBox()
        self.combo_region.addItems(self.regions.keys())
        self.combo_region.currentIndexChanged.connect(self.update_R)

        # Выбор конструкции
        self.label_structure = QLabel("Выберите конструкцию:")
        self.combo_structure = QComboBox()
        self.combo_structure.addItems(["Стена", "Крыша", "Пол"])
        self.combo_structure.currentIndexChanged.connect(self.update_R)

        # Поля для температур
        self.label_T_inside = QLabel("Температура внутри (°C):")
        self.entry_T_inside = QLineEdit("20")  # По умолчанию +20°C
        self.entry_T_inside.textChanged.connect(self.update_R)

        self.label_T_outside = QLabel("Температура снаружи (°C):")
        self.entry_T_outside = QLineEdit()
        self.entry_T_outside.setPlaceholderText("Авто или введите вручную")
        self.entry_T_outside.setReadOnly(True)

        # Поле для R
        self.label_R = QLabel("Требуемое термическое сопротивление (м²·К/Вт):")
        self.entry_R = QLineEdit()
        self.entry_R.setPlaceholderText("Авто или введите вручную")
        self.entry_R.setReadOnly(True)

        # Выбор утеплителя
        self.label_material = QLabel("Выберите утеплитель:")
        self.combo_material = QComboBox()
        self.combo_material.addItems(self.materials.keys())
        self.combo_material.currentIndexChanged.connect(self.update_lambda)

        # Поле для коэффициента теплопроводности
        self.label_lambda = QLabel("Коэффициент теплопроводности (Вт/м·К):")
        self.entry_lambda = QLineEdit()
        self.entry_lambda.setPlaceholderText("Авто или введите вручную")
        self.entry_lambda.setReadOnly(True)

        # Кнопка расчёта
        self.calc_button = QPushButton("Рассчитать")
        self.calc_button.clicked.connect(self.calculate)

        # Метка вывода результата
        self.result_label = QLabel("Рекомендуемая толщина: - см")

        # Добавляем элементы на форму
        layout.addWidget(self.label_region)
        layout.addWidget(self.combo_region)
        layout.addWidget(self.label_structure)
        layout.addWidget(self.combo_structure)
        layout.addWidget(self.label_T_inside)
        layout.addWidget(self.entry_T_inside)
        layout.addWidget(self.label_T_outside)
        layout.addWidget(self.entry_T_outside)
        layout.addWidget(self.label_R)
        layout.addWidget(self.entry_R)
        layout.addWidget(self.label_material)
        layout.addWidget(self.combo_material)
        layout.addWidget(self.label_lambda)
        layout.addWidget(self.entry_lambda)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle("Калькулятор теплоизоляции")
        self.setGeometry(100, 100, 400, 450)

    def update_R(self):
        """Автозаполняет термическое сопротивление и температуру снаружи"""
        selected_region = self.combo_region.currentText()
        selected_structure = self.combo_structure.currentText()

        if selected_region != "Свой вариант":
            R_value = self.regions[selected_region][selected_structure]
            T_outside = self.regions[selected_region]["Тнаруж"]
            self.entry_R.setText(str(R_value))
            self.entry_R.setReadOnly(True)
            self.entry_T_outside.setText(str(T_outside))
            self.entry_T_outside.setReadOnly(True)
        else:
            self.entry_R.clear()
            self.entry_R.setReadOnly(False)
            self.entry_T_outside.clear()
            self.entry_T_outside.setReadOnly(False)

    def update_lambda(self):
        """Автозаполняет коэффициент теплопроводности при выборе материала"""
        selected_material = self.combo_material.currentText()
        lambda_value = self.materials[selected_material]

        if lambda_value is not None:
            self.entry_lambda.setText(str(lambda_value))
            self.entry_lambda.setReadOnly(True)
        else:
            self.entry_lambda.clear()
            self.entry_lambda.setReadOnly(False)

    def calculate(self):
        try:
            R_required = float(self.entry_R.text())
            lambda_material = float(self.entry_lambda.text())

            thickness = R_required * lambda_material
            self.result_label.setText(
                f"Рекомендуемая толщина: {thickness * 100:.2f} см"
            )

        except ValueError:
            QMessageBox.critical(
                self, "Ошибка", "Введите корректные числовые значения!"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThermalCalculator()
    window.show()
    sys.exit(app.exec_())
