#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      User
#
# Created:     25.09.2013
# Copyright:   (c) User 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from PyQt4 import QtCore, QtGui, uic
import sys

import Excercises
NAME        = "Задание №3 : Выбрать подходящий вариант описания фрагмента программы."
#generateRndVarName = Excercises.generateRndVarName()

INTEGER = "описание переменной целого типа"
REAL    = "описание переменной вещественного типа"
WRITELN = "вывод на экран значения переменной"
READLN  = "ввод значения переменной"
ABS     = "вычисление модуля числа"
FRAC    = "получение дробной части числа"
MOD     = "вычисление остатка после деления"
DIV     = "целочисленное деление"
SQRT    = "извлечение квадратного корня"
SQR     = "возведение в квадрат"
TRUNK   = "получение целой части числа"
ROUND   = "округление числа"
SUM     = "сумма двух чисел"
SUB     = "разность двух чисел"
MUL     = "умножение двух чисел"
DIV_    = "деление одного числа на другое"
MOV     = "присвоение значения переменной"

answers = [INTEGER, REAL, WRITELN, READLN, ABS, FRAC, MOD, DIV, SQRT, SQR, SUM, SUB, MUL, DIV_, MOV, ROUND, TRUNK]

##variables = [chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)] + ["_"]


# Здесь второе задание - вписать необходимые для описания величин типы (только integer и real)
quests = {"var %s:integer;" : INTEGER,
          "readln(%s);"     : READLN,
          "writeln(%s)"     : WRITELN,
          "var %s:real;"    : REAL,
          "abs(%s);"        : ABS,
          "frac(%s);"       : FRAC,
          "%s mod %s"       : MOD,
          "%s div %s"       : DIV,
          "sqrt(%s);"       : SQRT,
          "sqr(%s);"        : SQR,
          "%s + %s"         : SUM,
          "%s - %s"         : SUB,
          "%s * %s"         : MUL,
          "%s / %s"         : DIV_,
          "%s := %s"        : MOV,
          "trunk(%s);"      : TRUNK,
          "round(%s);"      : ROUND
        }



class ExWnd():
    def __init__(self, callback):

        self.wnd = uic.loadUi("./Excercises/Ex_03.ui")
        self.callback = callback
        self.okPixmap = QtGui.QPixmap(Excercises.IMG_OK)
        self.noPixmap = QtGui.QPixmap(Excercises.IMG_NO)
        self.pixMaps = {0:self.noPixmap, 1:self.okPixmap}

        self.newQuests = {}
        for item in quests:
            try:
                self.newQuests[item % Excercises.generateRndVarName()] = quests[item]
            except:
                self.newQuests[item % (Excercises.generateRndVarName(), Excercises.generateRndVarName())] = quests[item]

        self.images = self.wnd.groupBox_2.children()[0].children()[1:]
        self.labels = self.wnd.groupBox.children()[0].children()[1::2]
        self.comboboxes = self.wnd.groupBox.children()[0].children()[2::2]

        Q = Excercises.makeRndList(list(self.newQuests))

        for label in self.labels:
            label.setText(Q.pop())

        items = list(answers)
        for combo in self.comboboxes:
            combo.addItems(items)
            #combo.setCurrentIndex(-1)




    def check(self):

        rows = [False] * 6

        for rowId in range(6):
            rows[rowId] = answers[self.comboboxes[rowId].currentIndex()] == self.newQuests[self.labels[rowId].text()]
            self.images[rowId].setPixmap(self.pixMaps[rows[rowId]])


        allright = rows[0] & rows[1] & rows[2] & rows[3] & rows[4] & rows[5]

        if allright:
            self.callback()

