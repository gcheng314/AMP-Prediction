def trim(infile):
    '''
    reads infile (in FASTA format), finds the header of 
    each protein, and replaces it with a number in order from 1 to the total
    number of proteins in the file. 
    This script also changes any illegal aminoo acid characters to 'X'.
    to prepare for the file being the input of 
    https://www.dveltri.com/ascan/v2/index.html
    The script writes the changed fasta file to a new file
    
    Requires:
    The file is not empty
    The file is in the same directory as this script
    
    Examples:
    If the user uses the zebrafish proteome downloaded from Uniprot as the 
    input, the script writes the same file with the changes to a new file
    
    '''
    original_fasta = open(infile, 'r') #initializing files for reading 
    modded_fasta = open(infile[:infile.index('.')] + 
                        '_trim.txt', 'w')  #and writing, respectively

    legal_letters = ['A','C','D','E','F','G','H','I','K','L','M','N',
                     'P','Q','R','S','T','V','W','X','Y','\n']
    for line in original_fasta:     
    
        if line.startswith(">"): #trims each header
            modded_fasta.write(line[:line.index(' ')] + '\n')
            
        else: #finds any illegal letters and changes them to 'X'
            lst_line = list(line)
            
            for char in lst_line:
                if char not in legal_letters:
                    lst_line[lst_line.index(char)] = 'X'
            
            modded_fasta.write(''.join(lst_line))
     
    original_fasta.close()
    modded_fasta.close()
    print('Done')