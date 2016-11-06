#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
markdown tools, used to assist creation of markdown elements from
python objects

@author: Jev Kuznetsov
"""

def htmlTable(rows, header=None):
    """ create html table from list containing row data """
    
    s = "<table>\n"
    # header
    if header is not None:
        s+="<tr>\n"
        for h in header:
           s+= "<th>" + str(h) + "</th>" 
        
        
        s+="<\tr>\n"
    
    # row data
    for row in rows:
        s+="<tr>\n"
        for col in row:
            s+= "<td>" + str(col) + "</td>"

        s+="</tr>\n"
    s +="</table>\n"
    
    return s