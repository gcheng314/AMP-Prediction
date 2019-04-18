def knowns(infile):
    '''
    knowns will take a fasta file downloaded from Uniprot and will output a file
    that contains all known AMPs 
    
    Requires:
    file is not empty
    file is in FASTA format
    
    Example:
    If the user sets 'd_rerio_proteome.fasta' as the input file, the function will 
    write all proteins that are known AMPs to a new file
    '''
    
    list_amps = ['Nigrocin', 'Bacteriocin', 'Brevinin', 'Beta-defensin', 
                 'Cathelicidin', 'Defensin', 'Dermaseptin', 'Latarcin', 
                 'Palustrin', 'Rugosin', 'Cecropin', 'LEAP2', 'Hainanensisin',
                 'Liver-expressed', 'Penaeidin', 'Tachystatin', 'Pleurain',
                 'Esculentin', 'Phylloseptin', 'Temporin', 'Pleurocidin',
                 'Thaumatin', 'Formaecin', 'Melittin', 'Ponericin', 'Thionin',
                 'Ascaphin', 'Odorranain', 'Caerin', 'Clavanin',  'Amolopin',
                 'Gaegurin', 'Metchnikowin', 'Pseudin', 'Aurein', 'Palustrin',
                 'Bombinin', 'Coleoptericin', 'Hepcidin', 'Moricin', 
                 'Ranateurin', 'Transferrin', 'Cupiennin', 'Histatin',
                 'family antimicrobial peptide', 'Crustin', 
                 'Myticin', 'Uperin', 'Nigroain', 'Maximins']
    
    f = open(infile, 'r')
    o = open(infile[:infile.index('.')]+'_TP.txt', 'w')
    line = f.readline()
    
    while line != '':
        if line.startswith('>') and line.split(' ')[1] in list_amps:
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
    
