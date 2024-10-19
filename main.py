from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout

app = QApplication([])

window = QWidget()
window.setWindowTitle("Розумні замітки")

main_layout = QHBoxLayout()

note_text = QTextEdit()
main_layout.addWidget(note_text)

right_layout = QVBoxLayout()

notes_list = QListWidget()
right_layout.addWidget(QLabel("Список заміток"))
right_layout.addWidget(notes_list)

buttons_layout = QHBoxLayout()

create_note_btn = QPushButton("Створити замітку")
buttons_layout.addWidget(create_note_btn)

delete_note_btn = QPushButton("Видалити замітку")
buttons_layout.addWidget(delete_note_btn)

right_layout.addLayout(buttons_layout)

save_note_btn = QPushButton("Зберегти замітку")
right_layout.addWidget(save_note_btn)

tags_list = QListWidget()
right_layout.addWidget(QLabel("Список тегів"))
right_layout.addWidget(tags_list)

tag_input = QLineEdit()
right_layout.addWidget(QLabel("Введіть тег"))
right_layout.addWidget(tag_input)

tag_buttons_layout = QHBoxLayout()

add_tag_btn = QPushButton("Додати до замітки")
tag_buttons_layout.addWidget(add_tag_btn)

remove_tag_btn = QPushButton("Відкріпити від замітки")
tag_buttons_layout.addWidget(remove_tag_btn)

right_layout.addLayout(tag_buttons_layout)

search_tag_btn = QPushButton("Шукати замітки по тегу")
right_layout.addWidget(search_tag_btn)

main_layout.addLayout(right_layout)

window.setLayout(main_layout)

window.show()

app.exec_()
