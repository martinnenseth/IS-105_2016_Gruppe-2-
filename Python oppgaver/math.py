#!/usr/bin/env python
# -*- coding: utf-8 -*-

tall1 = raw_input("Tast inn tall 1: ")
tall2 = raw_input("Tast inn tall 2: ")

tall1 = int(tall1)
tall2 = int(tall2)

# Pluss 
def pluss() :
    result = tall1 + tall2
    print "Pluss: " 
    print result

# Minus
def minus() :
    result = tall1 - tall2
    print "Minus: " 
    print result

# Gange
def gange() :
    result = tall1 * tall2
    print "Gange: "
    print result

# Dele 
def dele() : 
    result = tall1 / tall2
    print "Dele: "
    print result

# print ut alle resultatene
def printResultat() : 
    pluss()
    minus()
    gange()
    dele()  
    
printResultat()    
