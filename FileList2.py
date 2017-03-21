# -*- coding: utf-8 -*-

import datetime
import os


def fileList(folder='c:\\', date=datetime.date.today()):
    """
    Generates list of files from a folder modified after date
    
    Parameters
    __________
    folder: string
        a path name to be used as root of the search
    date: date
        only files modified on or after this date will be kept in the list
        default is today
    Returns 
    ________
    filesList: dictionary
     a dictionary where each filename by absolute path
    is the key to the date modified value.
    
    Example
    _______
    > fileList(folder="c:\\temp", date=datetime.date(2017,3,21))
    ["<first file>",
    . . .          ,
     "<last file>"]
    
    Test on a directory with few subfolders
    
    @author: lorete01
    """
    filesList = []
    for root, dir, fn in os.walk(folder):
        for file in fn:
            # print(root + file)
            filesList += [root+file]
    return filesList