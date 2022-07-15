# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:18:09 2021

@author: duronelly2p331
"""

def print_text(text):
    """
    Prints text to the console.
    
    Parameters
    ----------
    text: string
        The text to print.
    """
    print(text)
   
    
def print_anything(any_input):
    """
    Prints input to the console. 
    Checks whether the input is string. If not, is casts it as string, then 
    prints it to the console. 
    
    Parameters
    ----------
    text: any type
        The text to print.
    """
    
    if not isinstance(any_input, str):
        any_input = str(any_input)
        
    print(any_input)
    
    
    