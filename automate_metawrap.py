clearimport os
import gzip
import shutil
import gzip
import argparse

# This code is to automate metawrap when you cannot unzip all the files in order to batch assemble. It takes .gz zipped paired files from the input directory and
## unips the pair and puts them through metawrap. Finally it removes the unziped file to save storage space.
### Your data and results folder should be this architecture, this script goes in the Parent_dir and one input to run the code is data_dir
# Parent_dir/data_dir
#Parent_dir/results_dir
#example terminal line input:$ python3 automate_metawrap.py data_dir/ 20 10
#the first number is how many characters do you want to use to match files on
#the second number is how many characters do you want to use for the unique output dir


def find_matches(file_list, char_match):
    sorted_list = []
    print(file_list)
    while len(file_list) != 0:
        current_file = file_list.pop()
        for index, f in enumerate(file_list):
            match_flag = current_file[:char_match] == f[:char_match]    #want to compare the first n characters to match in the filename
            print("The current file {}, the f file {}".format(current_file, f))    #for debugging
            print(match_flag)  #for debugging, when uncommented it should return a True if there is a match and False if not
            if match_flag:      #if true, Ju Lee, do the thing
                # print("File: {} is matched with {}".format(current_file, f))   #for debugging, when uncommented this will show you the pairs.
                sorted_list.append(current_file)
                sorted_list.append(f)
                file_list.remove(f)
                break
    return(sorted_list)

def unzip(f):
    """ unzip .gz files and temporairily make an unzipped file for later use"""
    unzipped_f = os.path.join(f[:-3])
    input = gzip.GzipFile(f, 'rb')
    s = input.read()
    input.close()
    output = open(unzipped_f, 'wb')
    output.write(s)
    output.close()
    print("Done unzipping {}".format(f))
    return unzipped_f

def process_pairs(file_path, sorted_list):
    while len(sorted_list) != 0:
        sorted_fwd = os.path.join(file_path, sorted_list.pop())
        sorted_rev = os.path.join(file_path, sorted_list.pop())
        paired_reads = (sorted_fwd, sorted_rev)
        #unzip_fwd = unzip(sorted_fwd)
        #unzip_rev = unzip(sorted_rev)
        print("This is the pair {}".format(paired_reads))
        #print(os.path.basename(unzip_fwd)[:5])
        # input_string = 'metawrap read_qc -1 {} -2 {} -t 20 -o metawrap_read_qc/{} --skip-bmtagger'.format(unzip_fwd, unzip_rev, os.path.basename(unzip_fwd)[:args.out_dir_chars])
        # print("\nFile 1: {} File 2: {}".format(unzip_fwd, unzip_rev))
        # print("Checking file order")
        if unzip_fwd.endswith(_1.fastq):
            continue
        elif:

        # print("Starting")
        # output = os.system(input_string)
        # print(output)
        # print("Done with metawrap, moving on to next pair. :) \n")
        # os.remove(unzip_fwd)
        # os.remove(unzip_rev)
def main(args):
    file_path = os.getcwd() + '/' + args.data_dir
    file_list = sorted(os.listdir(file_path))
    sorted_list = find_matches(file_list, args.char_match)
    process_pairs(file_path, sorted_list)


parser = argparse.ArgumentParser()
parser.add_argument('data_dir',
                    help = 'top dir of the data and results dirs')
parser.add_argument('char_match', type = int,
                    help = 'how many characters in the file name are going to match; this must be the same # for every file')
#parser.add_argument('out_dir_chars', type = int,
#                    help = 'how many characters in the file name should be used for the file outdir')
args = parser.parse_args()
main(args)