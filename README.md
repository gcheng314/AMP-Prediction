# AMP-Prediction

This project will aid in predicting novel antimicrobial peptide (AMP) families using command line blastp and hmmsearch

Requires:
Python 2.7 + 
Linux command line
amp_pred.py in Linux computer

Instructions
[On preferred O.S.]
1.
Choose a proteome from Uniprot.org, for example {d_rerio_proteome.fasta}

2.
Run trim_fasta.py with {d_rerio_proteome.fasta} and the name of your desired output file, {d_rerio_prot_trim.fasta} as parameters

3. 
Input the trimmed .fasta file {d_rerio_prot_trim.fasta} to https://www.dveltri.com/ascan/v2/index.html, a prediction tool using deep learning

4.
From extracting the resulting .zip file downloaded from https://www.dveltri.com/ascan/v2/index.html, convert the MS Excel file to a tab-delimited .txt file {d_rerio_dl_prediction.txt}

5.
Run rank_by_prob.py with {d_rerio_dl_prediction.txt}, name of output file {d_rerio_dl_ranked.txt}, and probability threshold {0.95} as parameters


[On Linux command line]
6.  
Run amp_pred.py with {d_rerio_dl_ranked.txt} as the parameter

7.
################################  BLASTP DIRECTORIES

U
