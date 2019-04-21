# AMP-Prediction

This project will aid in predicting novel antimicrobial peptide (AMP) families using command line Diamond blast and hmmsearch

# Includes:
tabulate.py

rank.py

trim.py

find_unknowns.py

find_knowns.py


# Requires:
- Python 2.7.1 or higher
- Linux command line
- All .hmm files downloaded from http://www.camp.bicnirrh.res.in/pattern_hmm.php?q=HMM_fam and merged into amps.hmm 
- database file with diamond made. 

change indicated directories to your cown preferred directories

# Instructions

[On preferred O.S.]

1.
Choose a proteome from Uniprot.org, for example {d_rerio_proteome.fasta}

2.
Run trim.py with {d_rerio_proteome.fasta}  

        If on Windows or MacOSX, convert the end-of-line characters in the file to Unix format using dox2unix Linux command or
        via software such as Notepad++

3. 
Input the trimmed .fasta file {d_rerio_prot_trim.fasta} to https://www.dveltri.com/ascan/v2/index.html, a prediction tool using deep
learning

4.
From extracting the resulting .zip file downloaded from https://www.dveltri.com/ascan/v2/index.html, convert the MS Excel file to a tab
delimited .txt file {d_rerio_pred.txt}

5.
Run rank.py with {d_rerio_pred.txt} as the parameter and upload the output {d_rerio_pred_ranked.txt} to
Linux 

[On Linux command line]

6.  
Run tabulate.py with {d_rerio_pred_ranked.txt} as the raw_input variable. If necessary, change the source code so that the
directories/file locations used in the subprocess commands are appropriate to the user

[Additionally]

find_knowns.py filters the true positive AMPs from a raw proteome downloaded from Uniprot via known families
find_unknowns.py filters the unknowns/uncharacterized proteins from a raw proteome downloaded from Uniprot
Both these scripts will output a text file in fasta format

# Citations

Buchfink B, Xie C, Huson DH, "Fast and sensitive protein alignment using DIAMOND", Nature Methods 12, 59-60 (2015).
doi:10.1038/nmeth.3176

Daniel Veltri, Uday Kamath, and Amarda Shehu (2018) Deep Learning Improves Antimicrobial Peptide Recognition. Bioinformatics,
34(16):2740-2747. (DOI: 10.1093/bioinformatics/bty179)

The UniProt Consortium 
UniProt: a worldwide hub of protein knowledge 

Waghu, F. H., Gopi, L., Barai, R. S., Ramteke, P., Nizami, B., & Idicula-Thomas, S. (2013). CAMP: Collection of sequences and structures
of antimicrobial peptides. Nucleic acids research, 42(Database issue), D1154–D1158. doi:10.1093/nar/gkt1157
Nucleic Acids Res. 47: D506-515 (2019)
