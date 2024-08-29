from main_window import*
from menu_window import*

from random import choice, shuffle #виб. ранд. ел.зі списку \ перемішує елементи списку
from time import sleep             #щоб програма засинала 



# клас Питання  
class Question(): 
 
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3): 
        self.question = question             # питання 
        self.answer = answer                 # відповідь 
        self.wrong_answer1 = wrong_answer1   # непр.відп.1 
        self.wrong_answer2 = wrong_answer2 
        self.wrong_answer3 = wrong_answer3 
 
        self.actual = True  # чи актуальне питання 
        self.attempts = 0   # кільк. спроб 
        self.correct = 0    # кільк. прав.відп. 
 
    def got_right(self): 
        ''' змінює статистику, отримавши правильну відповідь''' 
        self.attempts += 1 
        self.correct += 1 
 
    def got_wrong(self): 
        ''' змінює статистику, отримавши неправильну відповідь''' 
        self.attempts += 1

# питання 
q1 = Question('хто використов є фотосинтез?', 'рослини', 'камень', 'тварини', 'клітини') 
q2 = Question('яка най тупіша тварина на землі? ', 'коала', 'шимпанзе', 'кенгуру', 'черепаха') 
q3 = Question('хто має великого підводного родича?', 'ізоподи', 'кіт', 'жираф', 'кенгуру') 
q4 = Question('яка найрозумніша тварина на землі?', 'шимпанзе', 'восьминіг ', 'дельфін', 'страус') 
q5 = Question('яка істота є безсмертною істотою на землі?', 'Turritopsis dohrnii', 'гідра', 'аксолотль', 'медуза') 
q6 = Question('найближчий родич кита?', 'бегемот', 'дельфін', 'косатка', 'крокодил') 
q7 = Question('най жорстокіша створіння на землі?', 'дельфін', 'ласка', 'лев', 'косатка') 
q8 = Question('хто з них є небезпечним?', 'качкодзьоб','скунс', 'кіт',  'кролики') 
q9 = Question('хто з них може залазити на дерево?', 'крокодил', 'собака', 'кролик', 'бегемот') 
q10 = Question('Що с цього є міфом?', 'страус ховає свою голову якщо його налякати', 'дельфіни топлять дельфінят', 'кальмари можуть відкрити банку ', 'крокодили можуть залазити на дерево') 
q11 = Question('яка з акул є сама агресивна?', 'акула бик', 'рифова акула', 'біла акула', 'тупорила акула') 
q12 = Question('кого людина приручила першим?', 'вовк', 'кота', 'собака', 'папуга') 
q13 = Question('чому гриби мають свою окрему групу?', 'виділили за їх морфологічною подібністю та особливостями живлення', 'бо вони не роблять фотосинтез', 'незнаю', 'бо цікаві')

#списки з панелі
radio_list = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
question = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13]


#                            (функція що обирає випадкове запитання зі списку та показує його на екрані) 
def new_question(): 
    global cur_question 
    cur_question = choice(question)                   #вибирає рандомне запитання 
 
    lb_Question.setText(cur_question.question)         #встановлює текст(відповіді та запитання) на віджети 
    lb_Correct.setText(cur_question.answer) 
 
    shuffle(radio_list)                                 #перемішує кнопки(щоб не на 1 шій була завжди прав.відпов.)- змінюючи позицію в списку 
     
    radio_list[0].setText(cur_question.wrong_answer1)   #розмішюємо на них знову питання 
    radio_list[1].setText(cur_question.wrong_answer2) 
    radio_list[2].setText(cur_question.wrong_answer3)   #в новому порядку 
    radio_list[3].setText(cur_question.answer)



#                                                   (функція для перевірки результату відповіді)
def check_result(): 
    for ans_btn in radio_list: 
        if ans_btn.isChecked():                         # вибраний вірних перемикач? 
            if ans_btn.text() == lb_Correct.text():     # чи збігається текст на вибр.кпонці та текст прав.відповіді? 
                cur_question.got_right()                # збільшити кільк.спроб +1 
                lb_Result.setText('Правильно!') 
                update_statistics()         
                break 
    else: 
        cur_question.got_wrong()                 #якщо не вибр.прав.відп. 
        lb_Result.setText('Неправильно! :)')     #змінити надпис на НЕПРАВИЛЬНО 
        update_statistics()



#                                               (функцію-обробник кнопки “Відпочити”)


def rest():
    main_win.hide()
    n = box_Minutes.value() * 60
    sleep(n)
    main_win.show()

def show_menu():
    main_win.hide()
    menu_win.show()

def back_menu():
    main_win.show()
    menu_win.hide()

def clear():
    txt_Question.clear()                    
    txt_Answer.clear()
    txt_Wrong1.clear()                       
    txt_Wrong2.clear()
    txt_Wrong3.clear()


def add_question():
    newq = Question(txt_Question.text(),txt_Answer.text(),txt_Wrong1.text(),txt_Wrong2.text(),txt_Wrong3.text())
    question.append(newq)
    clear()

def switch_screen():
    if btn_Ok.text() == 'Відповісти':
        check_result()
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_Ok.setText('Наступне запитання')
    else:
        new_question()
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_Ok.setText('Відповісти')

        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)








def update_statistics():
    total_attenpts = sum(q.attempts for q in question )
    total_correct = sum(q.correct for q in question)
    lbl_statistics.setText(f"Статистика:\nПравильних відповідей: {total_correct}\nЗагальна кількість спроб:")



new_question()

btn_Menu.clicked.connect(show_menu)
btn_back.clicked.connect(back_menu)
btn_clear.clicked.connect(clear)
btn_Sleep.clicked.connect(rest)
btn_Ok.clicked.connect(switch_screen)
btn_add_q.clicked.connect(add_question)


main_win.show()
app.exec_()
















