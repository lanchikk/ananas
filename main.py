from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox, QMessageBox
)
from random import shuffle,choice


class Question:
    def init(self, question_text, correct_answer, wrong_answers):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.wrong_answers = wrong_answers

    def get_shuffled_answers(self):
        answers = [self.correct_answer] + self.wrong_answers
        shuffle(answers[1:])
        return answers


class MemoryCard(QWidget):
    def init(self):
        super().init()
        self.card_width, self.card_height = 600, 500
        self.setWindowTitle('Memory Card')
        self.resize(self.card_width, self.card_height)
        self.move(300, 300)

        self.initUI()

        self.questions = [
            Question("В якому році Україна стала незалежною?", "1991", ["1919", "1488", "1999"]),
            Question("Скільки років тривала війна в Афганістані?", "Десять", ["П'ять", "Вісім", "Шість"]),
            Question("Який результат 2+2?", "Чотири", ["Три", "П'ять", "Шість"]),
        ]
        self.current_question = None
        self.ask_question()

    def initUI(self):
        self.btn_Sleep = QPushButton('Відпочити')
        self.box_Minutes = QSpinBox()
        self.box_Minutes.setValue(30)

        self.btn_menu = QPushButton('Меню')
        self.btn_rest = QPushButton('Відпочити')
        self.btn_next = QPushButton('Відповісти')

        self.btn_next.clicked.connect(self.check_answer)

        layout_controls = QHBoxLayout()
        layout_controls.addWidget(self.btn_menu, alignment=Qt.AlignLeft)
        layout_controls.addWidget(self.btn_Sleep, alignment=Qt.AlignRight)
        layout_controls.addWidget(self.box_Minutes, alignment=Qt.AlignRight)

        self.RadioGroupBox = QGroupBox('Варіанти відповідей')
        self.RadioGroup = QButtonGroup()

        self.rbtn_ans1 = QRadioButton()
        self.rbtn_ans2 = QRadioButton()
        self.rbtn_ans3 = QRadioButton()
        self.rbtn_ans4 = QRadioButton()

        self.RadioGroup.addButton(self.rbtn_ans1)
        self.RadioGroup.addButton(self.rbtn_ans2)
        self.RadioGroup.addButton(self.rbtn_ans3)
        self.RadioGroup.addButton(self.rbtn_ans4)

        layout_ans = QVBoxLayout()
        layout_ans1 = QHBoxLayout()
        layout_ans2 = QVBoxLayout()
        layout_ans3 = QVBoxLayout()

        layout_ans2.addWidget(self.rbtn_ans1)
        layout_ans2.addWidget(self.rbtn_ans2)
        layout_ans3.addWidget(self.rbtn_ans3)
        layout_ans3.addWidget(self.rbtn_ans4)

        layout_ans1.addLayout(layout_ans2)
        layout_ans1.addLayout(layout_ans3)
        self.RadioGroupBox.setLayout(layout_ans1)

        self.question = QLabel("Питання?")

        layout_ans.addLayout(layout_controls)
        layout_ans.addWidget(self.question, alignment=Qt.AlignHCenter)
        layout_ans.addWidget(self.RadioGroupBox)
        layout_ans.addWidget(self.btn_next, stretch=2)

        self.setLayout(layout_ans)

    def ask_question(self):
        self.current_question = choice(self.questions)
        self.question.setText(self.current_question.question_text)

        shuffled_answers = self.current_question.get_shuffled_answers()
        self.rbtn_ans1.setText(shuffled_answers[0])
        self.rbtn_ans2.setText(shuffled_answers[1])
        self.rbtn_ans3.setText(shuffled_answers[2])
        self.rbtn_ans4.setText(shuffled_answers[3])

        self.btn_next.setText("Відповісти")
        self.RadioGroupBox.setTitle('Варіанти відповідей')
        self.btn_next.clicked.disconnect()
        self.btn_next.clicked.connect(self.check_answer)

    def check_answer(self):
        selected_button = self.RadioGroup.checkedButton()
        if selected_button is None:
            QMessageBox.warning(self, "Увага", "Виберіть варіант відповіді!")
            return
if selected_button.text() == self.current_question.correct_answer:
            self.RadioGroupBox.setTitle("Правильно!")
            self.btn_next.setText("Наступне питання")
            self.btn_next.clicked.disconnect()
            self.btn_next.clicked.connect(self.next_question)
        else:
            self.RadioGroupBox.setTitle("Неправильно, спробуйте ще раз!")
            self.btn_next.setText("Відповісти")

    def next_question(self):
        self.ask_question()


if name == 'main':
    app = QApplication([])
    win_card = MemoryCard()
    win_card.show()
    app.exec_()