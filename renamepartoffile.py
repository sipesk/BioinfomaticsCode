import os
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('csv',
                    help = 'comma separated value with two columns: part of old file name and string to use to replace')
args = parser.parse_args()

replace_csv = args.csv
current_folder = os.getcwd()

with open(replace_csv, mode='r') as infile:
    reader = csv.reader(infile)
    replace_dict = {rows[0]:rows[1] for rows in reader}

for file in os.listdir(current_folder):
    full_path = (os.path.join(current_folder, file))
    file_name, file_extension = os.path.splitext(file)
    for key, value in replace_dict.items():
        if not key in file_name:
            continue
        new_name = file_name.replace(key, value)
        new_file = (os.path.join(new_name + file_extension))
        os.rename(full_path, new_file)
