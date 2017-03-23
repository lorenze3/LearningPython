# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 06:13:01 2017

@author: TeamLorenzen
"""
# pipe delimited file name(with path) and date of last modification.

fileout=open('c:\\temp\\index.txt', 'w')
fileout.write('Path\\filename.ext || last mod date mm/dd/yyyy \n')
for key in tryit:
    fileout.write(key + ' || ' +tryit[key].strftime('%m/%d/%Y') + '\n')
fileout.close()