import argparse
import netCDF4
import numpy as np
import os
import hashlib
import glob 
import datetime 
from datetime import timedelta


def search_year(file_path, word):
    with open(file_path, 'r') as fp:
        # read all content of a file
        lines = fp.readlines()
        for line in lines:
          if line.find(word) != -1:
            return(line[25:29]) 
def search_alt(file_path, word):
    with open(file_path, 'r') as fp:
        # read all content of a file
        lines = fp.readlines()
        for line in lines:
          if line.find(word) != -1:
            return(line[25:27])


exp_dir = '/scratch1/NCEPDEV/stmp2/Andrew.Tangborn/RUNDIRS/lagged/'


files = glob.glob(exp_dir+'/fcst.*/model_configure') 

for f in files:
  year = int(search_year(f,'start_year'))
  month = int(search_alt(f,'start_month'))
  day = int(search_alt(f,'start_day'))
  hour = int(search_alt(f,'start_hour'))
  d =datetime.date(year,month,day) 
  print('file = ', f)
  print(year,month,day,hour)


