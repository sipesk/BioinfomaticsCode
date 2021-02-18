## Supplemental Bioinfomatics Programs
Some python scripts that I've needed to use to manipulate data while working with bioinformatics

## File renamer
This script was made to deal with the terrible names that are given when you download genome sets from JGI (Joint Genome Institue). This script is inteneded to be in the same directory as the donloaded and unzipped JGI folders. It will rename each subdir to the name that is after the '>' in the .faa file. 
That file will come with the genome cart download. To run: In termininal, after putting the script file in the same directory as all of the downloaded files from JGI: $python3 filerenamer.py


## ChangeNames_csv
This script is intended to batch change the names of file names to whatever you desire. It takes a csvfile with two columns; oldnames and newnames. 
The user must provide a csv file with these headers and copy the file names (no extention needed) into the oldnames col and provide what the newnames should be.
To run: in the directory with the file names to change, python3 changenamescsv.py


## Process_data
This script is intented to compile the outputs from Bowtie2. Bowtie2 finishes with txt files that the user used in Bowtie2 as bins/MAGS and also the sorted CSV file of the metagenome/whole sample that was used. Briefly, Bowtie2 will present the number of mapped reads to the whole sample. See more in /sipesk/NEWBowtie.
The user must create a .txt file called *Toal_reads_ALL_samples.txt*. This file should have the name of the Samples in column one, the total number of reads in that sample in col 2 and the product of col2/1 million in column 3. The final output will be a .txt file with each bin in the first column and the subsequent colums will be the total summation of the maps of that bin to each sample. It will also create an intermediate file with the master list of all the final mapped calulations. (Reads per kilobase per million mapped reads = "mapped reads"/[(length of gene/1000) x reads in sample/1,000,000)]. 
In the directiory with all the bowtie outputs and the 'total reads all sample.txt', the script should be ran as: python3 process_data.py --data-dir /path/to/bowtie2/outputs.


## Automate metawrap
This script is intended to automate the matching of forward and reverse fastq.gz files, interate over the file by only unzipping the pair and then applying the pair in the correct order to metawrap's (see https://github.com/bxlab/metaWRAP/blob/master/Usage_tutorial.md) assembly process. This is a great way to limit the cpu burden and also allow the process to run autonomously. To run this, in the directory will all the .fastq.gz files that you want to assemble into trimmed, processed reads, run: python3 automat_metawrap.py.



