#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox
from random import shuffle, randint

class Question():
    def __init__(self, qst, right_answer, wrong1, wrong2, wrong3):
        self.qst = qst
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400,300)

question = QLabel('Какой национальности не существует')
btn_OK = QPushButton('Ответить')
main_layout = QVBoxLayout()

ansBox = QGroupBox('Варианты ответа')
btn1 = QRadioButton('Энцы')
btn2 = QRadioButton('Чулымцы')
btn3 = QRadioButton('Смурфы')
btn4 = QRadioButton('Алеуты')

layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()

layout1.addWidget(btn1)
layout1.addWidget(btn2)
layout2.addWidget(btn3)
layout2.addWidget(btn4)

layout.addLayout(layout1)
layout.addLayout(layout2)

ansBox.setLayout(layout)

resBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
right_ans = QLabel('Правильный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(right_ans, alignment=Qt.AlignCenter)
resBox.setLayout(layout_res)

layout_box = QHBoxLayout()
layout_box.addWidget(ansBox)
layout_box.addWidget(resBox)
resBox.hide()

main_layout.addWidget(question, stretch=1)
main_layout.addLayout(layout_box, stretch=2)
main_layout.addWidget(btn_OK, stretch=2)

main_win.setLayout(main_layout)

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

def show_result():
    ansBox.hide()
    resBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    resBox.hide()
    ansBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [btn1, btn2, btn3, btn4]
#в начало кода добавить from random import shuffle
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.qst)
    right_ans.setText(q.right_answer)
    show_question()

q = Question('Вопрос ?', "Ответ1", "Ответ2", "Ответ3", "Ответ4")
ask(q)


def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно!')
    
question_list = []
question_list.append(Question('Вопрос ?', "Ответ1", "Ответ2", "Ответ3", "Ответ4"))
question_list.append(Question('Вопрос1 ?', "Ответ565", "Ответ4", "Ответ3", "Ответ4"))
question_list.append(Question('Вопрос2 ?', "Ответ8", "Ответ2", "Отfff", "Ответ4"))

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question == len(question_list):
        main_win.cur_question = 0    
    q = question_list[main_win.cur_question]
    ask(q)

main_win.cur_question = -1

def click_ok():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()

main_win.total = 0
main_win.score = 0
btn_OK.clicked.connect(click_ok)
next_question()

main_win.show()
app.exec_()