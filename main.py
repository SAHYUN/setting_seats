__author__ = "[ jongh1118@gmail.com ]"

import random
import sys
import asyncio
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

form_class = uic.loadUiType("main.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.fst = None
        self.lst = None

        self.firstline_set.clicked.connect(self.setup_first)
        self.lastline_set.clicked.connect(self.setup_last)
        self.start.clicked.connect(self.change_line)

    def change_line(self):

        fl = [0, 0, 0, 0, 0]
        ll = [0, 0, 0, 0]

        all_student = [x for x in range(1, 30)]
        random.shuffle(all_student)

        array = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0]]


        try:
            for i in self.fst.split(","):
                fl.append(i)
                all_student.remove(int(i))
                fl.remove(0)
            
            if len(fl) > len(self.fst.split(",")):
                for j in range(len(fl) - len(self.fst.split(","))):
                    fl.append(all_student.pop(random.randint(0, len(all_student) - 1)))
                    fl.remove(0)
        except:
            fl = None

        
        try:
            for i in self.lst.split(","):
                ll.append(i)
                all_student.remove(int(i))
                ll.remove(0)
            
            if len(ll) > len(self.lst.split(",")):
                for j in range(len(ll) - len(self.lst.split(","))):
                    ll.append(all_student.pop(random.randint(0, len(all_student) - 1)))
                    ll.remove(0)
        except:
            ll = None


        if fl == None and ll == None:
            for k in range(5):
                for l in range(5):
                    array[k][l] = all_student.pop(random.randint(0, len(all_student) - 1))
            
            for q in range(4):
                array[5][q] = all_student.pop(random.randint(0, len(all_student) - 1))

        
        elif fl == None:
            random.shuffle(ll)
            for k in range(5):
                for l in range(5):
                    array[k][l] = all_student.pop(random.randint(0, len(all_student) - 1))
            
            for q in range(4):
                array[5][q] = ll.pop(random.randint(0, len(ll) - 1))
                

        elif ll == None:
            random.shuffle(fl)

            for k in range(1, 5):
                for l in range(5):
                    array[k][l] = all_student.pop(random.randint(0, len(all_student) - 1))

            for q in range(5):
                array[0][q] = fl.pop(random.randint(0, len(fl) - 1))
            
            for m in range(4):
                array[5][m] = all_student.pop(random.randint(0, len(all_student) - 1))
            
        
        else:
            random.shuffle(fl)
            random.shuffle(ll)

            for k in range(1, 5):
                for l in range(5):
                    array[k][l] = all_student.pop(random.randint(0, len(all_student) - 1))
            
            for q in range(5):
                array[0][q] = fl.pop(random.randint(0, len(fl) - 1))
            
            for m in range(4):
                array[5][m] = ll.pop(random.randint(0, len(ll) - 1))
        
        a = 0
        k = 0

        number = [[self.set_1, self.set_2, self.set_3, self.set_4, self.set_5],
                [self.set_6, self.set_7, self.set_8, self.set_9, self.set_10],
                [self.set_11, self.set_12, self.set_13, self.set_14, self.set_15],
                [self.set_16, self.set_17, self.set_18, self.set_19, self.set_20],
                [self.set_21, self.set_22, self.set_23, self.set_24, self.set_25],
                [self.set_26, self.set_27, self.set_28, self.set_29]]

        for i in array:
            for j in i:
                number[k][a].setText(str(j))
                a += 1
            k += 1
            a = 0

    

    def setup_first(self):
        text, ok = QInputDialog.getText(self, "앞줄", "앞줄에 있어야 하는 학생의 번호를 작성해주세요.(최대 5명)\n띄어쓰기 없이 , 로 구분해주세요.\nex) 1,2,3")
        if ok:
            self.fst = text
    
    def setup_last(self):
        text, ok = QInputDialog.getText(self, "뒷줄", "뒷줄에 있어야 하는 학생의 번호를 작성해주세요.(최대 4명)\n띄어쓰기 없이 , 로 구분해주세요.\nex) 1,2,3")
        if ok:
            self.lst = text



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()