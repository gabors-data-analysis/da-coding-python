# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:44:45 2021

@author: duronelly2p331
"""

def add_two_numbers(a, b):
    """
    Adds up two numbers.
    
    Parameters
    ----------
    a: int or float
    b: int or float
        The numbers to add up. 
    
    Returns
    ----------
    result: int or float
        The sum of 'a' and 'b'. 
    """
    
    result = a + b
    
    return result

def devide_two_numbers(a, b):
    """
    Divides input 'a' with input 'b'. 
    
    In case of inadequate inputs prints an error message. 
    
    Parameters
    ----------
    a: int or float
        numerator
    b: int or float
        denominator
    
    Returns
    ----------
    result: int or float
        Input 'a' divided by input 'b'.
    """
    
    try:
        result = a / b
    except:
        print('Inadequate inputs for division.')
    else:
        return result
    
    