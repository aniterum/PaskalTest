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
NAME        = "Задание №5 : Дописать недостающую часть программы"

Q   = "%(1)s=%(2)s%(3)s%(op)s%(4)s%(5)s"
opAndType  = {"-":"integer", "+":"integer", "*":"integer", "/":"real"}

Var  = "var%(1)s,%(3)s,%(5)s:%(isDivisionThenReal)s;"
Var1 = "var%(1)s,%(5)s,%(3)s:%(isDivisionThenReal)s;"
Var2 = "var%(3)s,%(1)s,%(5)s:%(isDivisionThenReal)s;"
Var3 = "var%(3)s,%(5)s,%(1)s:%(isDivisionThenReal)s;"
Var4 = "var%(5)s,%(1)s,%(3)s:%(isDivisionThenReal)s;"
Var5 = "var%(5)s,%(3)s,%(1)s:%(isDivisionThenReal)s;"

ANSWER = "%(1)s:=%(2)s*%(3)s%(op)s%(4)s*%(5)s;"

WRITELN_STR = "writeln(%(1)s);"

READLN_1 = "(%(3)s,%(5)s);"
READLN_2 = "(%(5)s,%(3)s);"

QUESTION    = "для нахождения значения выражения: " + Q

class ExWnd():
    def __init__(self, callback):

        self.wnd = uic.loadUi("./Excercises/Ex_05.ui")
        self.callback = callback
        self.okPixmap = QtGui.QPixmap(Excercises.IMG_OK)
        self.noPixmap = QtGui.QPixmap(Excercises.IMG_NO)
        self.pixMaps = {0:self.noPixmap, 1:self.okPixmap}

        import random
        # Чтобы имена перменных не повторились!
        firstVar = Excercises.generateRndVarName(False)
        secondVar = Excercises.generateRndVarName(False)
        while secondVar == firstVar:
            secondVar = Excercises.generateRndVarName(False)
        thirdVar = Excercises.generateRndVarName(False)
        while thirdVar == secondVar:
            thirdVar = Excercises.generateRndVarName(False)

        opt = random.choice(list(opAndType))

        self.mainDict = mainDict = {"1" : firstVar,
                                    "3" : secondVar,
                                    "5" : thirdVar,
                                    "2" : random.randint(5, 100),
                                    "4" : random.randint(5,100),
                                    "op": opt,
                   "isDivisionThenReal" : opAndType[opt]}


        self.varIantes = [Var  % self.mainDict,
                          Var1 % self.mainDict,
                          Var2 % self.mainDict,
                          Var3 % self.mainDict,
                          Var4 % self.mainDict,
                          Var5 % self.mainDict]

        self.readlns = [READLN_1 % self.mainDict,
                        READLN_2 % self.mainDict]


        self.questionLabel = self.wnd.groupBox.children()[0]
        self.questionLabel.setText(QUESTION % self.mainDict)
        self.images = self.wnd.groupBox_2.children()

        self.items = self.wnd.groupBox.children()[1].children()
        self.editBoxes = []
        self.editBoxes.append(self.items[2])
        self.editBoxes.append(self.items[5])
        self.editBoxes.append(self.items[6])

        self.writelnLabel = self.items[7]
        self.writelnLabel.setText(WRITELN_STR % self.mainDict)

        self.answer = ANSWER % self.mainDict

    def check(self):
        global newQuests
        rows = [False] * 3

        rows[0] = self.editBoxes[0].text().strip().lower().replace(" ", "") in self.varIantes
        rows[1] = self.editBoxes[1].text().strip().lower().replace(" ", "") in self.readlns
        #print(self.answer)
        #print(self.editBoxes[2].text().strip().lower().replace(" ", ""))
        rows[2] = self.editBoxes[2].text().strip().lower().replace(" ", "") == self.answer

        for rowId in range(len(rows)):
            self.images[rowId].setPixmap(self.pixMaps[rows[rowId]])



        ALLRIGHT = rows[0] & rows[1] & rows[2]

        if ALLRIGHT:
            self.callback()
