import os
import csv
import argparse
import sys
import pathlib

data_path = path = "/Users/ksipes/Documents/UTK/Svalbard/Data/NovaSeq/3-Data/refined_50_10_bins/"
csv_guide = "filenamestokeep.csv"
csv_path = os.path.join(data_path, csv_guide)
with open(csv_path, 'r') as csvfile:
    good_files = []
    for n in csv.reader(csvfile):
        if len(n) > 0: good_files.append(n[0])
    print(good_files)
    all_files = os.listdir(data_path)
    for filename in all_files:
        if filename.endswith(".fa") and filename not in good_files:
            print(filename)
            full_file_path = os.path.join(data_path, filename)
            print("File to delete: {} ".format(filename))
            os.remove(full_file_path)
        else:
           print(f"Ignored -- {filename}")