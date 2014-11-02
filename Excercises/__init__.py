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

from Excercises import Ex_01, Ex_02, Ex_03, Ex_04, Ex_05
from Excercises import Ex_FIN
import random

COUNT_OF_EXCERCISES = 5

IMG_OK = "etc/my_ok.png"
IMG_NO = "etc/my_no.png"
IMG_Q  = "etc/my_q.png"
IMG_OK_x20 = "etc/my_ok_x20.png"
IMG_NO_x20 = "etc/my_no_x20.png"
IMG_Q_x20  = "etc/my_q_x20.png"

IMG_OK_x256 = "etc/my_ok_x256.png"

modules = {0:Ex_01, 1:Ex_02, 2:Ex_03, 3:Ex_04, 4:Ex_05}
ExNames = [Ex_01.NAME, Ex_02.NAME, Ex_03.NAME, Ex_04.NAME, Ex_05.NAME]

EXCERCISE_TITLE     = "Задание №%i"

def loadExcercise(hWnd, weCanRunAway, exNum):
    if exNum == COUNT_OF_EXCERCISES:
        widget = Ex_FIN.ExWnd(weCanRunAway)
        return widget
    if not exNum in modules.keys():
        return None
    print("Loading %i excercise" % exNum)
    widget = modules[exNum].ExWnd(weCanRunAway)
    return widget


def makeRndList(someList):
    tmpList = list(someList)
    res = []
    for i in range(len(tmpList)):
        tmp = random.choice(tmpList)
        res.append(tmp)
        tmpList.remove(tmp)
    return res


VARIABLES = [chr(x) for x in range(97, 123)]

def generateRndVarName(useNumbers = True):
    res = ""
    for i in range(1):
        res += random.choice(VARIABLES)
    if useNumbers:
        res += str(random.randint(1, 10))
    return res

def makeDictWithTwoRndVars(useNumbers = True):
    d = [["1", generateRndVarName(useNumbers)], ["2", generateRndVarName()]]
    return dict(d)

def makeDictWithRndVarAndValue(useNumbers = True):
    d = [["1", generateRndVarName(useNumbers)], ["2", str(random.randint(1, 100))]]
    return dict(d)