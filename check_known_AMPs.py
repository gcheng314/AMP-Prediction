def knowns(infile):
    '''
    knowns reads in a fasta file, filters the queries by true positive AMPs based on the Uniprot format, 
    and writes the filtered queries to a new fasta file. Additionally, the number of true positives     
    
    Requires:
    file is downloaded from Uniprot
    
    Example:
    
    If knowns is run with the proteome of o. mykiss as its parameter, the output file contains 
    all queries from the proteome and the printed value is 8
    '''
    
    list_amps = ['Bacteriocin', 'Brevinin', 'Beta-defensin', 'Cathelicidin', 
                 'Defensin', 'Dermaseptin', 'Latarcin', 'Palustrin', 'Rugosin', 
                 'Cecropin', 'LEAP', 'LEAP2', 'Liver-expressed', 'liver-expressed', 
                 'Penaeidin', 'Tachystatin', 'Esculentin', 'Maximin', 'Phylloseptin', 
                 'Temporin', 'Pleurocidin', 'Thaumatin', 'Formaecin', 
                 'Melittin', 'Ponericin', 'Thionin', 'Ascaphin', 'Caerin', 
                 'Clavanin', 'Gaegurin', 'Metchnikowin', 'Pseudin', 'Aurein', 
                 'Bombinin', 'Coleoptericin', 'Hepcidin', 'Hepcidin-1', 'Moricin', 
                 'Ranateurin', 'Transferrin', 'Cupiennin', 'Histatin',
                 'Myticin', 'Uperin']
    num_queries = 0
    file_input = open(infile, 'r')
    file_output = open(infile[:infile.index('.')]+'_TP.txt', 'w')
    line = file_input.readline()
    
    while line != '':
       
        if line.startswith('>') and line.split(' ')[1] in list_amps:
            num_queries += 1
            accession = line
            file_output.write(accession)
            line = file_input.readline()
            
            while not(line.startswith('>')):
                file_output.write(line)
                line = file_input.readline()
                           
        else:
            line = file_input.readline()
    print(str(num_queries) + ' known AMPs are detected')
    file_input.close()   
    file_output.close()
