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
        self.layout = QVBoxLayout()  # Make layout an instance variable

        # User 1
        self.label_username_1 = QLabel("Player 1:")
        self.user_name_1_edit = QLineEdit()
        self.user_name_1_edit.setPlaceholderText("Enter your name")

        # Set width to 50% of window width
        window_width = 600  # from setGeometry
        self.user_name_1_edit.setFixedWidth(int(window_width * 0.5))

        # "Enter" button for confirming name
        self.enter_button = QPushButton("Enter")
        self.enter_button.setFixedSize(100, 30)
        self.enter_button.clicked.connect(self.confirm_name)

        # Add elements to layout
        self.layout.addWidget(self.label_username_1)
        self.layout.addWidget(self.user_name_1_edit)
        self.layout.addWidget(self.enter_button)

        # count label
        self.total_score_label = QLabel(f"Total score: {self.total_score}")
        self.total_score_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.layout.addWidget(self.total_score_label)

        # current_count
        self.current_count_label = QLabel(f"Current score: {self.current_count}")
        self.current_count_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.layout.addWidget(self.current_count_label)

        # Save count button
        self.save_button = QPushButton("Save")
        self.save_button.setFixedSize(100, 40)
        self.save_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.save_button.clicked.connect(self.save_score)
        self.layout.addWidget(self.save_button)

        self.set_dices()

        # Add ROLL button
        self.roll_button = QPushButton("ROLL DICE")
        self.roll_button.setFixedSize(200, 50)
        self.roll_button.setFont(QFont("Arial", 14, QFont.Bold))
        # self.roll_button.clicked.connect(self.roll_dice)
        self.layout.addWidget(self.roll_button, alignment=Qt.AlignHCenter | Qt.AlignTop)
        self.layout.addStretch(1)

        # Add stretch to push everything to the top
        self.layout.addStretch(1)

        # Connect the return pressed event to confirm name
        self.user_name_1_edit.returnPressed.connect(self.confirm_name)
        self.user_name_1_edit.textChanged.connect(self.update_label)

        self.setLayout(self.layout)
        self.setWindowTitle("1000 Poker Dice")
        self.setGeometry(200, 100, 700, 600)

    def set_dices(self, count=5):
        self.dice_labels = []
        dice_layout = QHBoxLayout()
        for _ in range(count):  # Assuming 5 dice
            dice_label = QLabel("0")
            dice_label.setFont(QFont("Arial", 24, QFont.Bold))
            dice_label.setAlignment(Qt.AlignCenter)
            dice_label.setFixedSize(50, 50)
            dice_layout.addWidget(dice_label)
            self.dice_labels.append(dice_label)
        self.layout.addLayout(dice_layout)

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
        self.label_username_1.setText(f"Player: {self.player_name}")
        self.label_username_1.setFont(QFont("Arial", 14, QFont.Bold))

        # Add START button
        self.start_button = QPushButton("START GAME")
        self.start_button.setFixedSize(200, 50)
        self.start_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.start_button.clicked.connect(self.start_game)

        # Add stretch to push the start button to the middle and top
        self.layout.addStretch(1)
        self.layout.addWidget(
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
