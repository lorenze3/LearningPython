# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:44:29 2017

@author: lorete01
"""
idxfn='c:\\temp\\index.txt'
import sendArchiveMsg, FileList2, zipThese

Files = fileList(folder="c:\\temp\\test", date=datetime.date(2017, 1, 1))
zipThis(Files.keys(),archive="c:\\temp\\TestZip.zip")
# create attachment
fileout=open(idxfn, 'w')
fileout.write('Path\\filename.ext || last mod date mm/dd/yyyy \n')
for key in Files:
    fileout.write(key + ' || ' +Files[key].strftime('%m/%d/%Y') + '\n')
fileout.close()
## todo add in call to boto3 to actually archive the things
FailedSend=sendArchMsg(attachment=idxfn)