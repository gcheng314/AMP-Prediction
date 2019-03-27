def rank_results(infile, outfile, P):
    '''
    rank_results reads in a txt file, infile, that is converted from an Excel
    spreadsheet downloaded from https://www.dveltri.com/ascan/v2/index.html and
    saved as a tab-delimited .txt file.
    
    It then filters the contents by each protein's probability of being an AMP 
    greater than or equal to P and saves all the results in another file
    
    Requires:
    
    0.00 <= P <= =1.00
    
    Example:
    If the s. salar proteome is the input of dveltri's tool, and the Excel file is converted to a txt file,
    all the results are ranked from highest probability to lowest with a sequence length cutoff of 50 amino acids. 
    '''
    
    class Protein:
        '''
        Fields:
        acc: Str
        prob: Float
        lngth: Nat
        sequ: Str
        '''
        
        def __init__(self, acc, prob, lngth, sequ):
            self.acc = acc
            self.prob = prob
            self.lngth = lngth
            self.sequ = sequ
            
        def __repr__(self):
            return "{0}\t{1}\t{2}\t{3}".format(self.acc, self.prob, 
                                               self.lngth, self.sequ)
        
        def __eq__(self, other):
            return (isinstance(other, Protein)) and \
                self.acc == other.acc and \
                self.prob == other.prob and \
                self.lngth == other.lngth and \
                self.sequ == other.sequ        
    
    input_file = open(infile, 'r')
    prot_list = []

    #reading the input file
    entry = f.readline()
    entry = f.readline()
    
    while entry != '':
    
        first_split = entry.index('\t')
        
        second_split = entry[first_split+1:].index('\t') +\
            len(entry[:first_split+1])
    
        third_split = entry[second_split+1:].index('\t') +\
            len(entry[:second_split+1])
    
        accession = entry[:first_split+1].split('|')[1]

        #debugging 
        #if not(entry[second_split+1:third_split+1].startswith('0') or
               #entry[second_split+1:third_split+1].startswith('1')):
            #print(accession)
    
        probability = float(entry[second_split+1:third_split+1])
        sequence = entry[third_split+1:]
        length = len(sequence)
        
        if probability >= P:
            prot = Protein(accession, probability, length, sequence)
            prot_list.append(prot)
            
        entry = input_file.readline()
        
    input_file.close()  
    
    #sorting the proteins according to sequence length 
    for i in range(1,len(prot_list)):
        current = prot_list[i]
    
        while i>0 and prot_list[i-1].lngth > current.lngth:
            prot_list[i] = prot_list[i-1]
            i -= 1
            prot_list[i] = current
    
    #creating the output file
    output = open(infile[:infile.index('.')] + '_ranked.txt', 'w')        
    output.write('Accession No.\tProbability\tLength\tSequence\n')            
    
    for each in prot_list:
        output.write(str(each))
    
    output.close()
    
    print('Done')
