# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:04:31 2020

@author: home
"""


import os
import shutil

try:
 os.mkdir('Images1')
 print(os.listdir())
except:
    pass

for file in os.listdir():
    if '.png' in file:
        
        curr_path = os.path.join(os.getcwd(),file)
        print(curr_path)
        
        
        dest_path = os.path.join(os.getcwd(),'Images1')
        print(dest_path)
        shutil.move(curr_path,dest_path)
        