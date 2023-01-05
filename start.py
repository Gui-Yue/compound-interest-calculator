# -*- coding = utf-8 -*-
# Creat_Time : 2023/01/05 11:19
# Author : Yuemeng_Gui
# File : start.py
# Software : PyCharm

import math

# i:收益率，n：期数

def Final(i,n):
    f = math.pow(1+i, n)
    return f

def Now(i,n):
    f = 1/Final(i, n)
    return f

def AnnuelFinal(i,n):
    f1 = Final(i, n) - 1
    f = f1/i
    return f

def AnnuelNow(i,n):
    f1 = 1/i
    f2 = i*Final(i, n)
    f = f1 - 1/f2
    return f

def caculate():
    while True:
        i = str((input("输入收益率(输入q退出):")))
        if i == "q":
            print("退出！")
            break
        i = float(i)
        n = int(input("输入期数(正整数):"))
        FP = Final(i, n)
        PF = Now(i, n)
        FA = AnnuelFinal(i, n)
        AF = 1/FA
        PA = AnnuelNow(i, n)
        AP = 1/PA
        print("F/P:%f\nP/F:%f\nF/A:%f\nA/F:%f\nP/A:%f\nA/P:%f" % (FP, PF, FA, AF, PA, AP))

def main():
    try:
        caculate()
    except ValueError:
        print("输入有误，请重新输入!")
        main()

main()