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

NAME        = "Задание №2 : Вписать типы переменных, необходимых для описания заданных величин."

INTEGER = "integer"
REAL    = "real"

# Здесь второе задание - вписать необходимые для описания величин типы (только integer и real)
quests = {"Количество учеников в классе" : INTEGER,
          "Масса тела человека"          : REAL,
          "Время поезда в пути"          : REAL,
          "Номер страницы в книге"       : INTEGER,
          "Число дней в месяце"          : INTEGER,
          "Скорость автомобиля"          : REAL,
          "Расстояние между городами"    : REAL,
          "Стоимость билета в автобусе"  : INTEGER,
          "Количество воды в чайнике"    : REAL,
          "Количество лепестков у цветка": INTEGER,
          "Возраст Вселенной"            : REAL,
          "Масса Земли"                  : REAL,
          "Количество тарелок на столе"  : INTEGER,
          "Величина заряда молнии"       : REAL,
          "Пробег автомобиля"            : REAL,
          "Разрешение экрана"            : INTEGER,
          "Количество океанов на Земле"  : INTEGER,
          "Плотность атомсферы"          : REAL,
          "Температура на улице"         : REAL,
          "Количество людей в стране"    : INTEGER,
          "Скорость света"               : REAL,
          "Длина экватора"               : REAL



        }


class ExWnd():
    def __init__(self, callback):

        self.wnd = uic.loadUi("./Excercises/Ex_02.ui")
        self.callback = callback
        self.okPixmap = QtGui.QPixmap(Excercises.IMG_OK)
        self.noPixmap = QtGui.QPixmap(Excercises.IMG_NO)
        self.pixMaps = {0:self.noPixmap, 1:self.okPixmap}



        self.images = self.wnd.groupBox_2.children()[0].children()[1:]
        self.editBoxes = self.wnd.groupBox.children()[0].children()[1:7]
        self.labels = self.wnd.groupBox.children()[0].children()[7:14]


        newQuests = Excercises.makeRndList(list(quests))

        for label in self.labels:
            label.setText(newQuests.pop())



    def check(self):

        rows = [False] * 6

        for rowId in range(6):
            rows[rowId] = self.editBoxes[rowId].text().strip().lower() == quests[self.labels[rowId].text()]
            self.images[rowId].setPixmap(self.pixMaps[rows[rowId]])


        allright = rows[0] & rows[1] & rows[2] & rows[3] & rows[4] & rows[5]

        if allright:
            self.callback()

