def unknowns(infile):
    '''
    unknowns will take a fasta file downloaded from Uniprot and will output a 
    file that contains all uncharacterized proteins from the original file
    
    Requires:
    file is not empty
    file is in FASTA format
    
    Example:
    If the user sets 'd_rerio_proteome.fasta' as the input, the function will
    write all uncharacterized proteins to a new file.
    
    '''
    
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
    
