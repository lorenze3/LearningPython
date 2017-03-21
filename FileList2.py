# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:47:37 2017

@author: lorete01
"""
import datetime
import os

def fileList(folder='c:\\', date=datetime.date.today()):
    filesList=[]
    for root,dir,fn in os.walk(folder):
        for file in fn:
            #print(root + file)
            filesList+=[root+file]
    return filesList