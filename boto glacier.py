# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:46:10 2017

stole this whole hog from https://www.withoutthesarcasm.com/using-amazon-glacier-for-personal-backups/
"""

from boto.glacier.layer1 import Layer1
from boto.glacier.vault import Vault
from boto.glacier.concurrent import ConcurrentUploader
import sys
import os.path

access_key_id = ""
secret_key = ""
target_vault_name = 'LorenzenBackup'
fname = "c:\\temp\\index.txt"

if(os.path.isfile(fname) == False):
    print("Can't find the file to upload!");
    sys.exit(-1);

glacier_layer1 = Layer1(aws_access_key_id=access_key_id, aws_secret_access_key=secret_key)

uploader = ConcurrentUploader(glacier_layer1, target_vault_name, 32*1024*1024)

print("operation starting...");

archive_id = uploader.upload(fname, fname)

print("Success! archive id: '%s'"%(archive_id))


