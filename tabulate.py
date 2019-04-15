'''
This script will produce a table of novel AMP candidates from the output file of
rank.py with the following categories: AMP probabily, Protein Length, 
Number of Matches (via Diamond BLAST up to 25 matches), mean length of the 
matches, and the e-value (via hmmsearch if found) 

Requires:
file is not empty

'''

import subprocess
import re

def mean(L):
    if L == []:
        return 'n/a'

    else:
        return sum(L)//len(L)
    
class Properties:
    '''
    Fields
    prob: Str
    query_len: Str
    match_lst: listof Nat
    e_val: Str
    
    '''
    def __init__(self, prob, query_len, match_lst, e_val):
        self.prob = prob
        self.query_len = query_len
        self.match_lst = match_lst
        self.e_val = e_val        
        
    def __repr__(self):
        return "{0} {1} {2} {3}".format(self.prob, self.query_len, self.match_lst, self.e_val)

    def __eq__(self, other):
        return (isinstance(other, Properties)) and \
            self.prob == other.prob and \
            self.query_len == other.query_len and \
            self.match_lst == other.match_lst and \
            self.e_val == other.e_val

predicted = open('predicted.txt', 'w')
raw_input = open('example.txt', 'r') # <====== replace example.txt with name of
                                     # output file from rank.py

entry = raw_input.readline() #ignores first line
entry = raw_input.readline()
    
dict_table = {}

while entry != '':
    probability = entry.split('\t')[1]
    accession = entry[:entry.index('\t')]
    sequence = entry.split('\t')[3]
    length = entry.split('\t')[2]
    dict_table[accession] = Properties(probability, length, [], 'n/a')
    query = ">" + accession + "\n" + sequence + "\n"
    predicted.write(query)
    entry = raw_input.readline()

raw_input.close()
predicted.close()

diamond = 'diamond blastp -d uniref90.dmnd -q predicted.fasta -o matches.txt'
diamond_cmd = subprocess.Popen(diamond.split(' '), stdout = subprocess.PIPE)
diamond_cmd_out = diamond_cmd.communicate()

match_file = open('matches.txt', 'r')
match_query = match_file.readline()

#Getting values for output
while match_query != '':
    lst_match = match_query.split('\t')

    if lst_match[0] not in lst_match[1]:
        dict_table[lst_match[0]].match_lst.append(int(lst_match[9]))

    match_query = match_file.readline()

match_file.close()
rm_0 = 'rm matches.txt'
rm_0_cmd = subprocess.Popen(rm_0.split(' '), stdout = subprocess.PIPE)

print('Starting hmmsearch')
hmm_search = 'hmmsearch --tblout tbl.txt -E 0.1 /home/grant/HMMs/AMPs.hmm predicted.fasta'
hmm_cmd = subprocess.Popen(hmm_search.split(' '), stdout = subprocess.PIPE)
hmm_out = hmm_cmd.communicate()
table = open('tbl.txt', 'r')
line = table.readline()

#extracting e-values from hmmsearch and appending to output
while line != '':
    if not(line.startswith('#')):
        acc = line[:line.find(' ')]
        find_ind = line.find('-')
        first_sub = line[find_ind+1:]
        second_ind = first_sub.find(' - ')
        second_sub = first_sub[second_ind+1:]
        e_beginning = second_sub[re.search('\d', second_sub).start():]
        end_ind = e_beginning.find(' ')
        e_value = e_beginning[:end_ind]
        dict_table[acc].e_val = e_value

    line = table.readline()

f_out = open(input_txt[:input_txt.index('.')] + '_table.txt', 'w')

f_out.write('Accession No.\tAMP Probability\tQuery Length\tNumber of Matches\tMean Length of Matches\tE-value\n')

for key in dict_table:
    f_out.write(key + '\t' + '\t'.join([dict_table[key].prob,
                                    dict_table[key].query_len,
                                    str(len(dict_table[key].match_lst)),
                                    str(mean(dict_table[key].match_lst)),
                                    dict_table[key].e_val]) + '\n')

#Removes temporrary files created by this script
rm_1 = 'rm predicted.fasta'
rm_1_cmd = subprocess.Popen(rm_1.split(' '), stdout = subprocess.PIPE)

rm_2 = 'rm tbl.txt'
rm_2_cmd = subprocess.Popen(rm_2.split(' '), stdout = subprocess.PIPE)

f_out.close()
print('Done')
