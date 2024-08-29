
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import *

 

app = QApplication([]) #програма

menu_win = QWidget()                             #основне вікно
menu_win.resize(400, 300)                        # встановлюємо розмір вікна
menu_win.setWindowTitle("Меню")         # назва вікна

#лінія для меню 
txt_Question = QLineEdit('')                     #запитання
txt_Answer = QLineEdit('')                       #відповідь
txt_Wrong1 = QLineEdit('')                       #неправильно
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('') 

layout_form = QFormLayout()

layout_form.addRow('Введіть запитання:',txt_Question)
layout_form.addRow('Введіть вірну відповідь:',txt_Answer) 
layout_form.addRow('Введіть першу хибну відповідь:',txt_Wrong1)  
layout_form.addRow('Введіть другу хибну відповідь:',txt_Wrong2) 
layout_form.addRow('Введіть третю хибну відповідь:',txt_Wrong3) 

btn_back = QPushButton('Назад') 
btn_add_q = QPushButton('Додати запитання') 
btn_clear = QPushButton('Очистити') 





lbl_statistics = QLabel('Статистика:\nПравильних відповідей: 0\nЗагальна кількість спроб: 0') # надпис статистики

gorysintal_btn = QHBoxLayout()
gorysintal_btn.addWidget(btn_back)
gorysintal_btn.addWidget(btn_add_q)
gorysintal_btn.addWidget(btn_clear)
 
# макет для вікна
vline = QVBoxLayout()
vline.addLayout(layout_form)
vline.addLayout(gorysintal_btn)
vline.addWidget(lbl_statistics)
 
menu_win.setLayout(vline)
 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
