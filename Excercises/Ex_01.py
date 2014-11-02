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

NAME        = "Задание №1 : Отметить правильные переменные"

# Здесь первое задание - отметить правильные имена переменных

##variables_ = {'F'    : True,   'f'      : True,   'Ф'  : False,  'ф'    : False,  'su'   : True,   's u'  : False,  'n'   : True,\
##             'n1'   : True,   'ц1'     : False,  '.s' : False,  's_1'  : True,   's5'   : True,   '5s'   : False,  'D'   : True,\
##             'sum'  : True,   'end'    : False,  'ent': True,   'begin': False,  'write': False,  'b'    : True,   'b123': True,\
##             '12b'  : False,  'writeln': True,   'for': False,  'while': False,  'bedin': True,   'writ' : True,   '3'   : False,\
##             'until': False,  'program': False,  'var': False,  'and'  : False,  'or'   : False,  'const': False,  'real': False,\
##             'abs'  : False,  'div'    : False,  'mod': False,  'to'   : False,  'do'   : False,  'k3_'  : True,   '_s'  : True}

variables = {'F'    : 2,      'f'      : 2,      'Ф'  : False,  'ф'    : False,  'su'   : 2,      's u'  : False,  'n'   : 2,\
             'n1'   : 2,      'ц1'     : False,  '.s' : False,  's_1'  : 2,      's5'   : 2,      '5s'   : False,  'D'   : 2,\
             'sum'  : 2,      'end'    : False,  'ent': 2,      'begin': False,  'write': False,  'b'    : 2,      'b123': 2,\
             '12b'  : False,  'writeln': False,  'for': False,  'while': False,  'bedin': 2,      'writ' : 2,      '3'   : False,\
             'until': False,  'program': False,  'var': False,  'and'  : False,  'or'   : False,  'const': False,  'real': False,\
             'abs'  : False,  'div'    : False,  'mod': False,  'to'   : False,  'do'   : False,  'k3_'  : 2,      '_s'  : 2}

class ExWnd():
    def __init__(self, callback):
        #self.DESCRIPTION = ""
        self.wnd = uic.loadUi("./Excercises/Ex_01.ui")
        self.callback = callback
        #tmpVar = dict(variables)
        self.checkBoxes = self.wnd.groupBox.children()[0].children()[1:]
        self.images = self.wnd.groupBox_2.children()[0].children()[1:]
        self.okPixmap = QtGui.QPixmap(Excercises.IMG_OK)
        self.noPixmap = QtGui.QPixmap(Excercises.IMG_NO)
        self.pixMaps = {0:self.noPixmap, 1:self.okPixmap}

        newQuests = Excercises.makeRndList(list(variables))

        for chk in self.checkBoxes:
            chk.setText(newQuests.pop())


    def check(self):

        allright = False
        row0, row1, row2, row3, row4, row5 = True, True, True, True, True, True

        for chk in self.checkBoxes[0:7]:
            row0 &= (chk.checkState() == (variables[chk.text()]))
            ##print("var %s, status %i, answer %i" % (chk.text(), chk.checkState(),variables[chk.text()] ))
        for chk in self.checkBoxes[7:14]:
            row1 &= (chk.checkState() == (variables[chk.text()]))
        for chk in self.checkBoxes[14:21]:
            row2 &= (chk.checkState() == (variables[chk.text()]))
        for chk in self.checkBoxes[21:28]:
            row3 &= (chk.checkState() == (variables[chk.text()]))
        for chk in self.checkBoxes[28:35]:
            row4 &= (chk.checkState() == (variables[chk.text()]))
        for chk in self.checkBoxes[35:42]:
            row5 &= (chk.checkState() == (variables[chk.text()]))


        self.images[0].setPixmap(self.pixMaps[row0])
        self.images[1].setPixmap(self.pixMaps[row1])
        self.images[2].setPixmap(self.pixMaps[row2])
        self.images[3].setPixmap(self.pixMaps[row3])
        self.images[4].setPixmap(self.pixMaps[row4])
        self.images[5].setPixmap(self.pixMaps[row5])



        allright = row0 & row1 & row2 & row3 & row4 & row5
        if allright:
            self.callback()

