# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 13:08:09 2017
zip archive creation for file list
@author: lorete01
"""

import zipfile


def zipThese(paths, archive='C:\\NewZip.zip'):
    """
    Creates zip archive containing all files in list
    
    Parameters
    __________
    paths: list
        list of aboslute paths to all files to be included in archive
    archive: string
        zip archive name
    Returns
    ________
    None
    
    Example:
    ________
    > zipThese(['c:\\temp\\ls.txt'],archive="c:\\temp\\TrialZip.zip")
    
    Note that, if passed aboslute paths in paths list, the zip archive
    will preserve the folder structure of the original files for easy
    restore

    @author: lorete01
    """

    zip = zipfile.ZipFile(archive, 'w')
    for p in paths:
        zip.write(p)
    zip.close()
    return None
    # This presevers folder structure.  yay!
