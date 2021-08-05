# import necessary libraries
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join


# get list of files in location and construct list of files through which to loop
mypath = ''
file_list = pd.Series(data=[f for f in listdir(mypath) if isfile(join(mypath, f))])
files = pd.DataFrame.from_records(data = file_list.str.split('.'), columns = ['name', 'extension'])
files['full_name'] = files.name + '.' + files.extension

print('list of all files...')
print(files)
print('\n')

loop_files = files[files.extension == 'tsv'].full_name

print('all files through which to loop...')
print(loop_files)

# Instantiate master_df, then loop through loop_files, adding to the master_df and including organism field
master_df = pd.DataFrame()

for f in loop_files:
    organism_name = f.split('_')[0]
    print('reading in {}...'.format(f))
    df = pd.read_csv(f, sep='\t')
    df['organism'] = organism_name
    print('shape of resulting DataFrame for {} is {}'.format(f, df.shape))
    master_df = master_df.append(df)

print('\nfinal shape of master DataFrame is {}'.format(master_df.shape))


#read in excel file containing gene to enzyme mapping
temp_df = pd.read_excel('wanted_enzymes_project.xlsx')

for c in temp_df.columns:
    temp_df[c] = temp_df[c].str.lower()

gene_to_enzyme = temp_df.set_index('prod_or_gene').to_dict()['enzyme']


#map columns to enzymes
master_df['product_enzyme'] = [gene_to_enzyme.get(prod) for prod in master_df['product']]
master_df['gene_enzyme'] = [gene_to_enzyme.get(gene) for gene in master_df['gene']]

#find good way to combine
#create final enzyme column
master_df['final_enzyme'] = master_df.product_enzyme


#export final enzyme counts for each organism to csv
enzyme_counts = master_df[['organism', 'final_enzyme']].pivot_table(index='organism', columns = 'final_enzyme', aggfunc=len)

enzyme_counts.to_csv('enzyme_counts_to_culture.csv')
master_df.to_csv('master_output.csv')