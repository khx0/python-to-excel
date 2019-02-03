#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: nikolas.schnellbaecher@bioquant.uni-heidelberg.de
# date: 2019-02-03
# file: columnwriter.py
##########################################################################################

import datetime
import os
import numpy as np

def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

now = datetime.datetime.now()
now = "%s-%s-%s" %(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')

if __name__ == '__main__':
    
    # create dummy data columns of different length
    n1 = 10
    c1 = np.linspace(0.0, 1.0, n1)
    
    n2 = 5
    c2 = np.linspace(0.0, 10.0, n2)
    
    n3 = 20
    c3 = np.linspace(0.0, 5.0, n3)
    
    n4 = 2
    c4 = np.linspace(0.0, 2.0, n4)
    
    import xlsxwriter
    wb = xlsxwriter.Workbook('myExcelWorkbook.xlsx')
    worksheet = wb.add_worksheet()
    
    '''
    the write_column(ROW, COL, DATACOLUMN) method write a column DATACOLUMN into 
    a row which starts in the worksheet cell at (ROW, COL)
    '''
    worksheet.write_column(0, 0, c1)    
    worksheet.write_column(0, 1, c2)
    worksheet.write_column(0, 2, c3)
    worksheet.write_column(0, 3, c4)
    
    wb.close()
