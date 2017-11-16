# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 23:31:14 2017

@author: SurfacePro4
"""

import cv2
import matplotlib.pyplot as plt
import random

num = 100;
wide = 300;
height = 300;
index = 0

#training set
for i in range (0,int(0.8*num),1):
    original = cv2.imread(r'C:\Users\SurfacePro4\Desktop\Senior proj\dataset\original\person1\test1.jpg')

    rx = random.randrange(1, wide)
    ry = random.randrange(1, height)
    rw = random.randrange(int(0.25*wide), int(0.75*wide))
    rh = random.randrange(int(0.25*height), int(0.65*height))

    gen = cv2.rectangle(original,(rx-rw//3,ry-rh//3),(rx+2*rw//3,ry+2*rh//3),(0,0,0),-1)
    index=index+1
    cv2.imwrite(r"C:\Users\SurfacePro4\Desktop\Senior proj\dataset\generated\training_set\person1\gen"+str(i)+".jpg",gen)
    
#test set
for i in range (0,int(0.2*num),1):
    original = cv2.imread(r'C:\Users\SurfacePro4\Desktop\Senior proj\dataset\original\person1\test1.jpg')

    rx = random.randrange(1, wide)
    ry = random.randrange(1, height)
    rw = random.randrange(int(0.25*wide), int(0.75*wide))
    rh = random.randrange(int(0.25*height), int(0.65*height))

    gen = cv2.rectangle(original,(rx-rw//3,ry-rh//3),(rx+2*rw//3,ry+2*rh//3),(0,0,0),-1)
    index=index+1
    cv2.imwrite(r"C:\Users\SurfacePro4\Desktop\Senior proj\dataset\generated\test_set\person1\gen"+str(i)+".jpg",gen)
    
