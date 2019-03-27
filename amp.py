import subprocess
import re

#initialize variables 
raw_input = open('om_ranked.txt', 'r')
entry = raw_input.readline()
entry = raw_input.readline()
dict_table = {}
predicted = open('predicted.fasta', 'w')

#diamond blast searches
while entry != '':
    accession = entry[:entry.index('\t')]
    sequence = entry.split('\t')[3]
    length = entry.split('\t')[2]
    
    query = ">" + accession + "\n" + sequence + "\n"
    predicted.write(query)
    
    temp = open('temp.faa', 'w')
    temp.write(query)
    temp.close()
    
    ###Change file directories as appropriate for user's use-case### 
    
    cmd1 = 'diamond blastp -d uniref90.dmnd -q temp.faa -o matches.txt'
    proc1 = subprocess.Popen(cmd1.split(' '), stdout = subprocess.PIPE)
    proc_out = proc1.communicate()    
    
    match_file = open('matches.txt', 'r')
    
    match_query = match_file.readline()
    match_query = match_file.readline()
    
    num_matches = 0
    len_list = []
    
    #Getting values for output
    while match_query != '':
        num_matches += 1
        query_length = int(match_query.split('\t')[9])
        len_list.append(query_length)
        match_query = match_file.readline()
    
    match_file.close()
    cmd2 = 'rm matches.txt'
    proc2 = subprocess.Popen(cmd2.split(' '), stdout = subprocess.PIPE)

    if num_matches == 0:
        mean_len = "n/a"

    else:
        mean_len = sum(len_list)//num_matches

    dict_table[accession] = [str(length), str(num_matches), str(mean_len)]
    entry = raw_input.readline()

predicted.close()

print('Starting hmmsearch')
cmd3 = 'hmmsearch --tblout tbl.txt -E 0.01 /home/grant/hmms/AMPs.hmm predicted.fasta'
proc3 = subprocess.Popen(cmd3.split(' '), stdout = subprocess.PIPE)
proc3_out = proc3.communicate()
table = open('tbl.txt', 'r')

line = table.readline()
i = 0

#extracting e-values from hmmsearch and appending to output
while i < len(dict_table) or line != '':

    if line.startswith('#'):
        line = table.readline()
    
    elif list(dict_table.keys())[i] not in line:
        line = table.readline()
        e_value = 'n/a'
        dict_table[list(dict_table.keys())[i]].append(e_value) 
        i += 1
            
    else:
        start_ind = len(list(dict_table.keys())[i])
        sub_str = line[start_ind:]
        e_beginning = sub_str[re.search('\d', sub_str).start():]
        end_ind = e_beginning.find(' ')
        e_value = e_beginning[:end_ind]
        dict_table[list(dict_table.keys())[i]].append(e_value) 
        line = table.readline()
        i += 1

f_out = open('om_output.txt', 'w')
f_out.write('Accession No.\tQuery Length\tNumber of Matches\tMean Length of Matches\tE-value\n')

for i in range(len(dict_table)):
    f_out.write(list(dict_table.keys())[i] + '\t' + '\t'.join(list(dict_table.keys()[i])))
                
raw_input.close()
f_out.close()
print('Done')
