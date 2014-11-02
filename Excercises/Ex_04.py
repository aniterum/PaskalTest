#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      User
#
# Created:     26.09.2013
# Copyright:   (c) User 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from PyQt4 import QtCore, QtGui, uic
import sys

import Excercises
NAME        = "Задание №4 : Написать команды, которые выполняют указанные действия"

INTEGER = "описать переменную %(1)s целого типа"
REAL    = "описать переменную %(1)s вещественного типа"
WRITELN = "вывод значения переменной %(1)s"
READLN  = "ввод значения переменной %(1)s"
ABS     = "вычисление модуля %(1)s"
FRAC    = "вычисление дробной части %(1)s"
MOD     = "в %(1)s остаток от деления %(1)s на %(2)s"
DIV     = "в %(1)s результат целочисленного деления %(1)s на %(2)s"
SQRT    = "вычисление квадратного корня числа %(1)s"
SQR     = "возведение \"%(1)s\" в квадрат"
TRUNK   = "получение целой части %(1)s"
ROUND   = "округление %(1)s"
SUM     = "увеличить %(1)s на %(2)s"
SUB     = "уменьшить %(1)s на %(2)s"
MUL     = "увеличить %(1)s в %(2)s раз(а)"
DIV_    = "уменьшить %(1)s в %(2)s раз(а)"
MOV     = "присвоить %(1)s значение %(2)s"

##quests = [INTEGER, REAL, WRITELN, READLN, ABS, FRAC, MOD, DIV, SQRT, SQR, SUM, SUB, MUL, DIV_, MOV, ROUND, TRUNK]
# При сравнении ответов нужно сносить нахер все пробелы!!!
INTEGER_ANS = "var%(1)s:integer;"
REAL_ANS    = "var%(1)s:real;"
WRITELN_ANS = "writeln(%(1)s);"
READLN_ANS  = "readln(%(1)s);"
ABS_ANS     = "abs(%(1)s);"
FRAC_ANS    = "frac(%(1)s);"
MOD_ANS     = "%(1)s:=%(1)smod%(2)s;"
DIV_ANS     = "%(1)s:=%(1)sdiv%(2)s;"
SQRT_ANS    = "sqrt(%(1)s);"
SQR_ANS     = "sqr(%(1)s);"
TRUNK_ANS   = "trunk(%(1)s);"
ROUND_ANS   = "round(%(1)s);"
SUM_ANS     = "%(1)s:=%(1)s+%(2)s;"
SUB_ANS     = "%(1)s:=%(1)s-%(2)s;"
MUL_ANS     = "%(1)s:=%(1)s*%(2)s;"
DIV__ANS    = "%(1)s:=%(1)s/%(2)s;"
MOV_ANS    = "%(1)s:=%(2)s;"

quests = [[INTEGER, INTEGER_ANS], [REAL, REAL_ANS], [WRITELN,WRITELN_ANS], [READLN,READLN_ANS], [ABS,ABS_ANS], [FRAC,FRAC_ANS], \
          [MOD,MOD_ANS],          [DIV,DIV_ANS],    [SQRT,SQRT_ANS],       [SQR,SQR_ANS],       [SUM,SUM_ANS], [SUB,SUB_ANS],   \
          [MUL,MUL_ANS],          [DIV_,DIV__ANS],  [MOV,MOV_ANS],         [ROUND,ROUND_ANS],   [TRUNK,TRUNK_ANS]]

class ExWnd():
    def __init__(self, callback):

        self.wnd = uic.loadUi("./Excercises/Ex_04.ui")
        self.callback = callback
        self.okPixmap = QtGui.QPixmap(Excercises.IMG_OK)
        self.noPixmap = QtGui.QPixmap(Excercises.IMG_NO)
        self.pixMaps = {0:self.noPixmap, 1:self.okPixmap}

        newQuests = []
        for quest, answer in quests:
            rndDict = Excercises.makeDictWithRndVarAndValue(False)
            newQuests.append([quest % rndDict, answer % rndDict])
        self.newQuests = dict(newQuests)

        self.images = self.wnd.groupBox_2.children()[0].children()[1:]
        self.labels = self.wnd.groupBox.children()[0].children()[1::2]
        self.editBoxes = self.wnd.groupBox.children()[0].children()[2::2]

        rndQuests = Excercises.makeRndList(list(self.newQuests))

        for label in self.labels:
            label.setText(rndQuests.pop())



    def check(self):
        global newQuests
        rows = [False] * 6

        for rowId in range(6):
            rows[rowId] = self.editBoxes[rowId].text().strip().lower().replace(" ", "") == self.newQuests[self.labels[rowId].text()]
            self.images[rowId].setPixmap(self.pixMaps[rows[rowId]])


        allright = rows[0] & rows[1] & rows[2] & rows[3] & rows[4] & rows[5]

        if allright:
            self.callback()
