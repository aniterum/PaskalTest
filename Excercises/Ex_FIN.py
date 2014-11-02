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
NAME        = ""

class ExWnd():
    def __init__(self, callback):

        self.wnd = uic.loadUi("./Excercises/Ex_FIN.ui")
        self.callback = callback
        self.okPixmap = QtGui.QPixmap(Excercises.IMG_OK_x256)

        self.wnd.groupBox.children()[0].setPixmap(self.okPixmap)


    def check(self):
        pass
