import os
import csv
import argparse
import sys
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('csv',
                    help = 'comma separated value with two columns: old file names and new file names')
args = parser.parse_args()

path = os.getcwd()
tmp_path = os.getcwd()

with open(args.csv,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
       oldname = os.path.join(path, row[0])
       if os.path.exists(oldname):
           newname = os.path.join(tmp_path, row[1])
           os.rename(oldname, newname)
           print("renamed {} to {}".format(os.path.basename(oldname), os.path.basename(newname)))
       else:
           print("file {} not found".format(oldname))

