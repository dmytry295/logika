from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
#--------------------
# Вікно програми
#--------------------
app = QApplication([])
window = QWidget()
window.setWindowTitle("Smart Notes")
window.resize(800,600)
window.move(0,0)
window.setStyleSheet("background-color : rgb(234,255,205); font-size: 15px; font-family: Font") # створюємо фон

#--------------------
# створюємо інтерфейс
#--------------------
text_editor = QTextEdit() # поле для тексту замітки
text_editor.setPlaceholderText("Введіть текст замітки:")

list_widget_1 = QListWidget()
list_widget_2 = QListWidget()

text_searcher = QLineEdit()
text_searcher.setPlaceholderText("Введіть текст:") # пошук по тексту

tag_seacher = QLineEdit()
tag_seacher.setPlaceholderText("Введіть тег:") #  пошук по тегу
#--------------------
# ставимо кнопки
#--------------------
make_note = QPushButton()
make_note.setText("Створити замітку") # створюєм

delet_note = QPushButton()
delet_note.setText("Видалити замітку") # видаляєм

save_note = QPushButton()
save_note.setText("Зберигти замітку") # Зберігаємо

seacher_for_text = QPushButton()
seacher_for_text.setText("Шукати за текстом")

seacher_for_tag = QPushButton()
seacher_for_tag.setText("Шукати за тегом")

add_to_note = QPushButton()
add_to_note.setText("Додати тег до замітки")

unpin_to_note = QPushButton()
unpin_to_note.setText("Відкрипити тег до замітки")

convert_to_txt = QPushButton()
convert_to_txt.setText("Конвертувати до txt формату")

action_theme_btn = QPushButton()
action_theme_btn.setText("Змінити тему")

#--------------------
# макет
#--------------------
row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delet_note)

row2 = QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)


col1 = QVBoxLayout()
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список заміток:"))
col2.addWidget(list_widget_1)
col2.addLayout(row1)
col2.addWidget(save_note)
col2.addWidget(QLabel("Список тегів:"))
col2.addWidget(list_widget_2)
col2.addWidget(QLabel("Пошук даних:"))
col2.addWidget(text_searcher)
col2.addWidget(tag_seacher)
col2.addLayout(row2)

col2.addWidget(seacher_for_tag)
col2.addWidget(seacher_for_text)
col2.addWidget(convert_to_txt)
col2.addWidget(action_theme_btn)
#--------------------
# Злиття
#--------------------
layout_note =  QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)

window.setLayout(layout_note)









window.show()
app.exec_()