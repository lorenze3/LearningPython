# -*- coding: utf-8 -*-

import datetime
import os


def fileList(folder='c:\\', 
             date=datetime.date.today()+datetime.timedelta(-30)):
    """
    Generates list of files from a folder (and subfolders) modified after date
    
    Parameters
    __________
    folder: string
        a path name to be used as root of the search
    date: date
        only files modified on or after this date will be kept in the list
        default is 30 days before today()
    Returns 
    ________
    filesList: dictionary
    
    Example
    _______

    > fileList(folder="c:\\temp", date=datetime.date(2017,3,21))
    ["<first file>",
    . . .          ,
     "<last file>"]
    
    Test on a directory with few subfolders
     a dictionary where each filename by absolute path
    is the key to the date modified value.
    
        
    @author: lorete01
    """
    filesList = []
    filesDate = dict()
    for root, dir, fn in os.walk(folder):
        for file in fn:
            # print(root + '\\' + file)
            # not sure why I need the double slash at
            # home and not in the office
            # add files to filesList (which is a list)
            filesList += [root + '\\' + file]
            for ff in filesList:
                # for each file add it to filesDate (a dict) iff getmtime>=date
                if datetime.date.fromtimestamp(os.path.getmtime(ff)) >= date:
                    filesDate[ff] = \
                        datetime.date.fromtimestamp(os.path.getmtime(ff))
    return filesDate
    # return filesList
