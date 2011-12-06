"""
Module: Utils.py
Severals useful utils
"""
# $Id: Utils.py,v 1.2 2011-11-20 12:28:32 ruslan Exp $

def new_id(d):
    """
    new_id - function to find the max id and return a new one
    """
    return max(d.keys()) + 1
