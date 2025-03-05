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
    QHBoxLayout,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import random
from apps.dice1000.utils import DiceUtils


class DicePoker(QWidget):
    def __init__(self):
        super().__init__()
        self.player_name = ""
        self.total_score = 0
        self.free_dices = 5
        self.current_count = 0
        self.init_ui()

    def init_ui(self):
        
        # Основной вертикальный слой
        self.main_layout = QVBoxLayout()

        # Верхний горизонтальный слой (слева и справа)
        self.top_layout = QHBoxLayout()

        # Левый верхний блок (3 элемента)
        self.left_top_layout = QVBoxLayout()
        self.left_top_layout.setContentsMargins(0, 0, self.width() // 2, 0)
        
        # Player 1 name
        self.label_username_1 = QLabel("Player 1:")
        self.label_username_1.setFont(QFont("Arial", 16, QFont.Bold))
        self.label_username_1.setAlignment(Qt.AlignCenter)
        self.left_top_layout.addWidget(self.label_username_1)
        
        # Edit widget for player 1 name
        self.user_name_1_edit = QLineEdit()
        self.user_name_1_edit.setPlaceholderText("Enter your name")
        self.user_name_1_edit.setFixedWidth(200)
        self.left_top_layout.addWidget(self.user_name_1_edit)
        
        # "Enter" button for confirming name
        self.enter_button = QPushButton("Enter")
        self.enter_button.setFixedSize(100, 30)
        self.enter_button.clicked.connect(self.confirm_name)
        self.left_top_layout.addWidget(self.enter_button)
        
        # Total score label 1
        self.total_score_label = QLabel(f"Total score: {self.total_score}")
        self.total_score_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.left_top_layout.addWidget(self.total_score_label)
        
        # current score 1
        self.current_count_label = QLabel(f"Current score: {self.current_count}")
        self.current_count_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.left_top_layout.addWidget(self.current_count_label)
        self.left_top_layout.addStretch(1)

        # Правый верхний блок (3 элемента)
        self.right_top_layout = QVBoxLayout()
        
        # Player 2 name
        self.label_username_2 = QLabel("Player 2:")
        self.label_username_2.setFont(QFont("Arial", 16, QFont.Bold))
        self.label_username_2.setAlignment(Qt.AlignCenter)
        self.right_top_layout.addWidget(self.label_username_2)
        
        # Edit widget for player 2 name
        self.user_name_2_edit = QLineEdit()
        self.user_name_2_edit.setPlaceholderText("Enter your name")
        self.user_name_2_edit.setFixedWidth(200)
        self.right_top_layout.addWidget(self.user_name_2_edit)
        
        # "Enter" button for confirming name
        self.enter_button_2 = QPushButton("Enter")
        self.enter_button_2.setFixedSize(100, 30)
        self.enter_button_2.clicked.connect(self.confirm_name)
        self.right_top_layout.addWidget(self.enter_button_2)
        
        # Total score label 2
        self.total_score_label_2 = QLabel(f"Total score: {self.total_score}")
        self.total_score_label_2.setFont(QFont("Arial", 14, QFont.Bold))
        self.right_top_layout.addWidget(self.total_score_label_2)
        
        # current score 2
        self.current_count_label_2 = QLabel(f"Current score: {self.current_count}")
        self.current_count_label_2.setFont(QFont("Arial", 14, QFont.Bold))
        self.right_top_layout.addWidget(self.current_count_label_2)
        self.right_top_layout.addStretch(1)

        # Добавляем два верхних блока в общий горизонтальный слой
        self.top_layout.addLayout(self.left_top_layout)
        self.top_layout.addLayout(self.right_top_layout)

        # Нижний блок (3 элемента в один ряд)
        self.dices_bottom_layout = QHBoxLayout()
        self.set_dices()
        
        # self.bottom_layout.addWidget(QLabel("Нижний 1", self))
        # self.bottom_layout.addWidget(QLabel("Нижний 2", self))
        # self.bottom_layout.addWidget(QLabel("Нижний 3", self))

        # roll layout
        # Add ROLL button
        self.roll_layout = QHBoxLayout()
        self.roll_button = QPushButton("ROLL DICE")
        self.roll_button.setFixedSize(200, 50)
        self.roll_button.setFont(QFont("Arial", 14, QFont.Bold))
        # self.roll_button.clicked.connect(self.roll_dice)
        self.roll_layout.addWidget(self.roll_button, alignment=Qt.AlignHCenter | Qt.AlignTop)

        # Save count button
        self.save_button = QPushButton("Save")
        self.save_button.setFixedSize(100, 40)
        self.save_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.save_button.clicked.connect(self.save_score)
        self.roll_layout.addWidget(self.save_button, alignment=Qt.AlignHCenter | Qt.AlignTop)
        # Add stretch to push everything to the top
        # self.roll_layout.addStretch(1)

        # Добавляем все в основной слой
        self.main_layout.addLayout(self.top_layout, 1)   # Верхний блок (50%)
        self.main_layout.addLayout(self.dices_bottom_layout, 1)  # Нижний блок (50%)
        self.main_layout.addLayout(self.roll_layout, 1)  # Кнопка "ROLL DICE" (50%)

        self.setLayout(self.main_layout)
        self.setWindowTitle("1000 Poker Dice Game")
        self.resize(700, 500)  # Размер окна
        
        # Connect the return pressed event to confirm name
        self.user_name_1_edit.returnPressed.connect(self.confirm_name)
        self.user_name_1_edit.textChanged.connect(self.update_label)
        return

        
        # Set width to 50% of window width
        window_width = 600  # from setGeometry
        self.user_name_1_edit.setFixedWidth(int(window_width * 0.5))

        # Save count button
        self.save_button = QPushButton("Save")
        self.save_button.setFixedSize(100, 40)
        self.save_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.save_button.clicked.connect(self.save_score)
        self.layout.addWidget(self.save_button)

        
        # Create a horizontal layout to hold both player sections
        main_layout = QHBoxLayout()
        main_layout.addLayout(self.layout)  # Add player 1 layout to the left
        main_layout.addLayout(self.layout2)  # Add player 2 layout to the right

        # Set the main layout as the layout for the widget
        self.setLayout(main_layout)


        self.set_dices()
        
          

        # Add ROLL button
        self.roll_button = QPushButton("ROLL DICE")
        self.roll_button.setFixedSize(200, 50)
        self.roll_button.setFont(QFont("Arial", 14, QFont.Bold))
        # self.roll_button.clicked.connect(self.roll_dice)
        self.layout.addWidget(self.roll_button, alignment=Qt.AlignHCenter | Qt.AlignTop)

        # Add stretch to push everything to the top
        self.layout.addStretch(1)

        # Connect the return pressed event to confirm name
        self.user_name_1_edit.returnPressed.connect(self.confirm_name)
        self.user_name_1_edit.textChanged.connect(self.update_label)

        # self.setLayout(self.layout)
        self.setWindowTitle("1000 Poker Dice")
        self.setGeometry(300, 100, 800, 600)

    def set_dices(self, count=5):
        self.dice_labels = []
        # dice_layout = QHBoxLayout()
        for _ in range(count):  # Assuming 5 dice
            dice_label = QLabel("0")
            dice_label.setFont(QFont("Arial", 24, QFont.Bold))
            dice_label.setAlignment(Qt.AlignCenter)
            dice_label.setFixedSize(50, 50)
            self.dices_bottom_layout.addWidget(dice_label)
            self.dice_labels.append(dice_label)
        # self.layout.addLayout(dice_layout)

    def update_label(self, text):
        self.label_username_1.setText(f"Your name: {text}")

    def confirm_name(self):
        # Get the player name from the input field
        self.player_name = self.user_name_1_edit.text()

        if not self.player_name:
            QMessageBox.warning(self, "Warning", "Please enter your name!")
            return

        # Remove the input field and enter button
        self.user_name_1_edit.setParent(None)
        self.enter_button.setParent(None)

        # Update the label
        self.label_username_1.setText(f"Player 1: {self.player_name}")
        self.label_username_1.setFont(QFont("Arial", 14, QFont.Bold))

        # Add START button
        self.start_button = QPushButton("START GAME")
        self.start_button.setFixedSize(200, 50)
        self.start_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.start_button.clicked.connect(self.start_game)

        # # Add stretch to push the start button to the middle and top
        # self.bottom_layout.addStretch(1)
        self.roll_layout.addWidget(
            self.start_button, alignment=Qt.AlignHCenter | Qt.AlignTop
        )

    def start_game(self):
        self.roll_button.clicked.connect(self.roll_dice)
        self.roll_button.setStyleSheet("background-color: blue; color: white;")

        self.start_button.setParent(None)

    # def roll_dice(self):
    #     for dice_label in self.dice_labels:
    #         dice_label.setText(str(random.randint(1, 6)))
    #     self.start_button.setParent(None)
    #     result = DiceUtils(self.dice_labels).count_dice()

    #     QMessageBox.information(
    #         self,
    #         "Your turn",
    #         f"Welcome, {self.player_name}! Current count: {result[0]}",
    #     )

    def roll_dice(self):
        # Roll all dice
        for dice_label in self.dice_labels:
            dice_label.setText(str(random.randint(1, 6)))
            dice_label.setStyleSheet("")  # Reset styling
            dice_label.setEnabled(True)   # Reset enabled state
        
        # Get result from DiceUtils
        result = DiceUtils(self.dice_labels).count_dice()
        score = result[0]
        kept_dice_dict = result[1]  # Dict of dice to KEEP
        
        # Disable all dice EXCEPT those in the kept_dice_dict
        # Track the number of each value we want to keep
        to_keep = kept_dice_dict.copy()
        
        # Process each die
        for dice_label in self.dice_labels:
            value = dice_label.text()
            
            # If this die value is in our "keep" list and we still need more of this value
            if value in to_keep and to_keep[value] > 0:
                # Keep this die (leave enabled)
                to_keep[value] -= 1
            else:
                # Disable this die (it's not needed for scoring)
                dice_label.setStyleSheet("background-color: lightgray; color: gray;")
                dice_label.setEnabled(False)
        
        # Show result message
        QMessageBox.information(
            self,
            "Your turn",
            f"Welcome, {self.player_name}! Current count: {score}",
        )
        
        # Store the current score
        self.current_count = score
        self.current_count_label.setText(f"Current count: {self.current_count}")

    def save_score(self):
        # To be implemented in the next step
        self.total_score += self.current_count
        self.total_score_label.setText(f"Total score: {self.total_score}")

        # if hasattr(self, "Total_score_label"):
        #     self.total_score_label.setText(f"Total score: {self.total_score}")
        # else:
        #     self.total_score_label = QLabel(f"Total: {self.total_score}")
        #     self.total_score_label.setFont(QFont("Arial", 14, QFont.Bold))
        #     self.layout.addWidget(self.total_score_label)

    def _dice_counter(self, dice):
        count = 0
        # check if all dice are the same
        if len(set(dice)) == 1:
            if dice[0].text() == "1":
                return 1000
            return int(dice[0].text() * 30)
        # Check if 4s
        if len(set(dice)) == 2:
            if dice[0].text() == dice[1].text():
                if dice[0].text() == "1":
                    return 2000
                return int(dice[0].text()) * 200
        # count 5s
        count += sum(5 for d in dice if d.text() == "5")
        # count 10
        count += sum(10 for d in dice if d.text() == "1")
        return count
        sum(int(dice_label.text()) for dice_label in self.dice_labels)

    def _dict_dice(self):
        dice_dict = {}
        for dice in self.dice_labels:
            dice_dict[dice.text()] = dice_dict.get(dice.text(), 0) + 1
        return dice_dict


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DicePoker()
    window.show()
    sys.exit(app.exec_())
