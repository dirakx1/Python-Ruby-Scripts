#!/bin/python

import math
import os
import random
import re
import sys

n = int(raw_input().strip())

if n in range(1,100): # initial range 
    if n % 2 != 0:
        print "Weird"
    
    if n in range (2, 5):
        if n % 2 == 0:
            print "Not Weird" 
    
    if  n in range (6, 20):
        if n % 2 == 0:
            print "Weird"

    if n > 20:
        if n % 2 == 0:
            print "Not Weird" 

    
