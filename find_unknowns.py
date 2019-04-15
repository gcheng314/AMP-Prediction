def unknowns(infile):
    '''
    unknowns will take a fasta file downloaded from Uniprot and will output a 
    file that contains all uncharacterized proteins '''
    
    f = open(infile, 'r')
    o = open(infile[:infile.index('.')]+'_unknowns.txt', 'w')
    line = f.readline()
    
    while line != '':
        if 'ncharacterized' in line:
            acc = line
            o.write(acc)
            line = f.readline()
            
            while not(line.startswith('>')):
                o.write(line)
                line = f.readline()
                           
        else:
            line = f.readline()
    
    f.close()   
    o.close()
    print('Done')