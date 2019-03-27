def knowns(infile):
    list_amps = ['Bacteriocin', 'Brevinin', 'Beta-defensin', 'Cathelicidin', 
                 'Defensin', 'Dermaseptin', 'Latarcin', 'Palustrin', 'Rugosin', 
                 'Cecropin', 'LEAP2', 'Liver-expressed', 'Penaeidin', 
                 'Tachystatin', 'Esculentin', 'Maximin', 'Phylloseptin', 
                 'Temporin', 'Pleurocidin', 'Thaumatin', 'Formaecin', 
                 'Melittin', 'Ponericin', 'Thionin', 'Ascaphin', 'Caerin', 
                 'Clavanin', 'Gaegurin', 'Metchnikowin', 'Pseudin', 'Aurein', 
                 'Bombinin', 'Coleoptericin', 'Hepcidin', 'Moricin', 
                 'Ranateurin', 'Transferrin', 'Cupiennin', 'Histatin',
                 'Myticin', 'Uperin']
    q = 0
    f = open(infile, 'r')
    o = open(infile[:infile.index('.')]+'_TP.txt', 'w')
    line = f.readline()
    
    while line != '':
        if line.startswith('>') and line.split(' ')[1] in list_amps:
            q += 1
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