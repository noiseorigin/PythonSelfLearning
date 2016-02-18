#!/usr/bin/python  
#coding=gbk  

from xlrd import open_workbook  
import sys  
  

def print_workbook(wb):  
  for s in wb.sheets():  
    print "Sheet:", s.name  
    for r in range(s.nrows):  
      strRow = ""  
      for c in s.row(r):  
        strRow += ("\t" + c.value)  
      print "ROW[" + str(r) + "]:", strRow  
  

def row_to_str(row):  
  strRow = ""  
  for c in row:  
      strRow += ("\t" + str(c.value))  
  return strRow;  
  
 
def print_report(report):  
  for o in report:  
    if isinstance(o, list):  
      for i in o:  
        print "\t" + i  
    else:  
      print o  
  
 
def diff_sheet(sheet1, sheet2):  
  nr1 = sheet1.nrows  
  nr2 = sheet2.nrows  
  nr = max(nr1, nr2)  
  report = []  
  for r in range(nr):  
    row1 = None;  
    row2 = None;  
    if r<nr1:  
      row1 = sheet1.row(r)  
    if r<nr2:  
      row2 = sheet2.row(r)  
  
    diff = 0; # 0:equal, 1: not equal, 2: row2 is more, 3: row2 is less  
    if row1==None and row2!=None:  
      diff = 2  
      report.append("+ROW[" + str(r+1) + "]: " + row_to_str(row2))  
    if row1==None and row2==None:  
      diff = 0  
    if row1!=None and row2==None:  
      diff = 3  
      report.append("-ROW[" + str(r+1) + "]: " + row_to_str(row1))  
    if row1!=None and row2!=None:  
      # diff the two rows  
      reportRow = diff_row(row1, row2)  
      if len(reportRow)>0:  
        report.append("#ROW[" + str(r+1) + "]1: " + row_to_str(row1))  
        report.append("#ROW[" + str(r+1) + "]2: " + row_to_str(row2))  
        report.append(reportRow)  
  
  return report;  
  

def diff_row(row1, row2):  
  nc1 = len(row1)  
  nc2 = len(row2)  
  nc = max(nc1, nc2)  
  report = []  
  for c in range(nc):  
    ce1 = None;  
    ce2 = None;  
    if c<nc1:  
      ce1 = row1[c]  
    if c<nc2:  
      ce2 = row2[c]  
      
    diff = 0; # 0:equal, 1: not equal, 2: row2 is more, 3: row2 is less  
    if ce1==None and ce2!=None:  
      diff = 2  
      report.append("+CELL[" + str(c+1) + ": " + ce2.value)  
    if ce1==None and ce2==None:  
      diff = 0  
    if ce1!=None and ce2==None:  
      diff = 3  
      report.append("-CELL[" + str(c+1) + ": " + ce1.value)  
    if ce1!=None and ce2!=None:  
      if ce1.value == ce2.value:  
        diff = 0  
      else:  
        diff = 1  
        report.append("#CELL[" + chr(c+65) + "]1: " + str(ce1.value))  
        report.append("#CELL[" + chr(c+65) + "]2: " + str(ce2.value))  
  
  return report  
  
  
if __name__=='__main__':  
  if len(sys.argv)<3:  
    exit()  
  
  file1 = sys.argv[1]  
  file2 = sys.argv[2]  
  
  wb1 = open_workbook(file1)  
  wb2 = open_workbook(file2)  
  
  #print_workbook(wb1)  
  #print_workbook(wb2)  
  
 
  report = diff_sheet(wb1.sheet_by_index(0), wb2.sheet_by_index(0))  
  print file1 + "\n" + file2 + "\n#############################"  
  
  print_report(report)  