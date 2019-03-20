# AMP-Prediction

This project will aid in predicting novel antimicrobial peptide (AMP) families using command line Diamond blast and hmmsearch

Requires:
Python 2.7.1 or higher 
Linux command line
All .hmm files downloaded from http://www.camp.bicnirrh.res.in/pattern_hmm.php?q=HMM_fam and merged 
amp_pred.py in Linux 

BEFRORE RUNNING amp.py:

change indicated directories to your cown preferred directories

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
