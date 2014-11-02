#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      User
#
# Created:     24.09.2013
# Copyright:   (c) User 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import Excercises

COUNT_OF_EXCERCISES = Excercises.COUNT_OF_EXCERCISES
EXCERCISE_TITLE     = Excercises.EXCERCISE_TITLE

global COMPLETED_EX
COMPLETED_EX = [False] * COUNT_OF_EXCERCISES

global CURRENT_EXCERCISE
CURRENT_EXCERCISE = 0

from PyQt4 import QtCore, QtGui, uic
import sys

app = QtGui.QApplication(sys.argv)
window      = uic.loadUi("./Forms/Main_Window.ui")
helpDialog  = uic.loadUi("./Forms/Help_Dialog.ui")
aboutDialog = uic.loadUi("./Forms/About_Dialog.ui")
HelpMenu = window.mainMenuBar.addMenu('Справка')
HelpMenu.addAction("Справка по Pascal", helpDialog.show)
HelpMenu.addAction("О программе", aboutDialog.show)
window.groupBox.setTitle(EXCERCISE_TITLE % (CURRENT_EXCERCISE + 1))
okPixmap = QtGui.QPixmap(Excercises.IMG_OK_x20)
noPixmap = QtGui.QPixmap(Excercises.IMG_NO_x20)
qPixmap = QtGui.QPixmap(Excercises.IMG_Q_x20)

icon1 = QtGui.QIcon()
icon1.addPixmap(QtGui.QPixmap(Excercises.IMG_Q), QtGui.QIcon.Normal, QtGui.QIcon.Off)
window.setWindowIcon(icon1)

# 760x420
# Осуществляем переход к другому заданию
def gotoExcercise(exNum):
    def callback():
        global CURRENT_EXCERCISE
        global widget


        if COMPLETED_EX[exNum]:
            print("Already Completed!")
            return
        if CURRENT_EXCERCISE == exNum:
            print("NO WAY!!!")
            return


        CURRENT_EXCERCISE = exNum

        print('Try load %i module' % exNum)

        widget.wnd.setParent(None)
        widget = Excercises.loadExcercise(window, weCanRunAway, CURRENT_EXCERCISE)

        if widget == None:
            print("No module loaded :(")
            return

        window.mainQuestLayout.addWidget(widget.wnd)
        window.connect(window.groupBox_2.children()[0], QtCore.SIGNAL("clicked()"), widget.check)
        window.groupBox.setTitle(EXCERCISE_TITLE % (CURRENT_EXCERCISE + 1))

    return callback
#=#=#=#=#= gotoExcercise(exNum) =#=#=#=#=#


def weCanRunAway():
    #Мы можем продолжать, задание завершено успешно
    global widget
    global CURRENT_EXCERCISE

    exButtons[CURRENT_EXCERCISE].setIcon(okIcon)
    COMPLETED_EX[CURRENT_EXCERCISE] = True

    if not (False in COMPLETED_EX):
        CURRENT_EXCERCISE = COUNT_OF_EXCERCISES
        window.groupBox.setTitle("")

    elif CURRENT_EXCERCISE == COUNT_OF_EXCERCISES - 1:
        CURRENT_EXCERCISE = COMPLETED_EX.index(False)
        window.groupBox.setTitle(EXCERCISE_TITLE % (CURRENT_EXCERCISE + 1))

    elif COMPLETED_EX[CURRENT_EXCERCISE + 1] != True:
        CURRENT_EXCERCISE += 1
        window.groupBox.setTitle(EXCERCISE_TITLE % (CURRENT_EXCERCISE + 1))
    else:
        CURRENT_EXCERCISE = COMPLETED_EX.index(False)
        window.groupBox.setTitle(EXCERCISE_TITLE % (CURRENT_EXCERCISE + 1))

    widget.wnd.setParent(None)

    widget = Excercises.loadExcercise(window, weCanRunAway, CURRENT_EXCERCISE)
    if widget == None:
        print("No module loaded :(")
        return

    window.mainQuestLayout.addWidget(widget.wnd)
    window.connect(window.groupBox_2.children()[0], QtCore.SIGNAL("clicked()"), widget.check)

#=#=#=#=#= weCanRunAway() =#=#=#=#=#


widget = Excercises.loadExcercise(window, weCanRunAway, CURRENT_EXCERCISE)
window.mainQuestLayout.addWidget(widget.wnd)
window.connect(window.groupBox_2.children()[0], QtCore.SIGNAL("clicked()"), widget.check)

qIcon = QtGui.QIcon()
qIcon.addPixmap(QtGui.QPixmap(Excercises.IMG_Q_x20), QtGui.QIcon.Normal, QtGui.QIcon.Off)
okIcon = QtGui.QIcon()
okIcon.addPixmap(QtGui.QPixmap(Excercises.IMG_OK_x20), QtGui.QIcon.Normal, QtGui.QIcon.Off)

exButtons = window.groupBox_2.children()[1].children()[1:]
for nameID in range(len(Excercises.ExNames)):
    exButtons[nameID].setToolTip(Excercises.ExNames[nameID])
    exButtons[nameID].setIcon(qIcon)
    window.connect(exButtons[nameID], QtCore.SIGNAL("clicked()"), gotoExcercise(nameID))

for nameID in range(len(Excercises.ExNames), len(exButtons)):
    exButtons[nameID].hide()


window.show()
sys.exit(app.exec_())
