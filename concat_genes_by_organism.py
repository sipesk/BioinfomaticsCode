import csv
import os
from operator import itemgetter

# For each folder in the directory
try:

    MasterList = []

    skipHeaderLine = False
    firstFolder = True
    for folder in os.listdir():
        # Had to ignore .idea file since MacBook adds it to the directory and I cannot remove it
        if os.path.isdir(folder) and not folder == '.idea':
            print(folder)

            id_Prokka = dict()

            # Get the file name from the same directory
            fileName = folder

            # Open the file
            fullName = os.path.join(fileName, fileName + '-gene_calls.txt')
            with open(fullName, "r") as gene_calls:
                # Create a reader object delimited by tab characters
                reader = csv.reader(gene_calls, delimiter="\t")

                # For each row add an element in the dictionary where the ID is the key and
                # the Prokka is the value
                for row in reader:
                    id_Prokka.update({row[0] : (row[5], row[8])})

            # Close the file
            gene_calls.close()

            # New File to write to UPDATE IF NEEDED
            newFile = open(os.getcwd() + "/" + folder + "/" + fileName + "-updated_gene_coverage.txt", "w")

            fullName = os.path.join(fileName, fileName + "-gene_coverages.txt")
            with open(fullName, "r") as gene_coverages:
                reader = csv.reader(gene_coverages, delimiter="\t")
                for row in reader:

                    # Skip over column headers if this isn't the first folder opened
                    if skipHeaderLine:
                        skipHeaderLine = False
                        continue

                    # Include Organism Name if after first run
                    if firstFolder:
                        firstFolder = False
                        temp = 'Organism Name;'
                    else:
                        temp = str(folder) + ';'

                    # For each row make a string, separated with ;, while adding in the Prokka based on ID
                    temp += str(row[0]) + '; ' + str(id_Prokka.get(row[0])[0])

                    for i in row[1:]:
                        if i == '0.0':
                            i = ''
                        temp += ';' + str(i)

                    # Add the AA Sequence at the end
                    temp += ';' + str(id_Prokka.get(row[0])[1])

                    # End each line with a newline character
                    temp += ';\n'

                    # Write it to the file
                    newFile.write(temp)
                    MasterList.append(temp)

            skipHeaderLine = True
            # Close the file
            gene_coverages.close()

    #print(MasterList)
    #sortedMasterList = sorted(MasterList, key=itemgetter(MasterList[1].index(' ') + 1))

    # Write all info to this file
    masterFile = open(os.getcwd() + "/Master_Gene_File_Non_Zero.txt", "w")
    for line in MasterList:
        masterFile.write(line)

except FileNotFoundError:
    print('The file name ' + fullName + ' does not exist\n Check your spelling possibly.')
