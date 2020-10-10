# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:51:19 2020

@author: opusm
"""
while "Y":
    
    numbers = int(input("How many numbers? "))
    
    for num in range(0,numbers+1):
        print(num)
        
        #continue
    proceed = input("Do you wish to continue? Y/N ").upper()
        
    #if proceed == "Y":
     #   numbers = int(input("How many numbers? "))
      #  for num in range(0,numbers+1):
       #     print(num)
    
    if proceed == "N": 
        print("Goodbye.")
        break

        