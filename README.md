# AMP-Prediction

This project will aid in predicting novel antimicrobial peptide (AMP) families using command line Diamond blast and hmmsearch

Includes:
amp.py
rank.py
trim_fasta.py


Requires:
- Python 2.7.1 or higher 
- Notepad++ 
- Linux command line
- All .hmm files downloaded from http://www.camp.bicnirrh.res.in/pattern_hmm.php?q=HMM_fam and merged into amps.hmm 
- amp_pred.py in Linux machine

BEFRORE RUNNING amp.py:

change indicated directories to your cown preferred directories

Instructions
[On preferred O.S.]
1.
Choose a proteome from Uniprot.org, for example {d_rerio_proteome.fasta}

2.
Run trim_fasta.py with {d_rerio_proteome.fasta} and the name of your desired output file, {d_rerio_prot_trim.fasta} as parameters 

                  *** If on Windows or MacOSX, open {d_rerio_proteome.fasta} with Notepad++, click on Edit => EOL Conversion => Unix ***

3. 
Input the trimmed .fasta file {d_rerio_prot_trim.fasta} to https://www.dveltri.com/ascan/v2/index.html, a prediction tool using deep learning

4.
From extracting the resulting .zip file downloaded from https://www.dveltri.com/ascan/v2/index.html, convert the MS Excel file to a tab-delimited .txt file {d_rerio_pred.txt}

5.
Run rank.py with {d_rerio_pred.txt} and probility threshold {0.95} as parameters and upload the output {d_rerio_pred_ranked.txt} to Linux 

[On Linux command line]
6.  
Run amp_pred.py with {d_rerio_pred_ranked.txt} as the raw_input variable. If necessary, change the source code so that the directories/file locations used in the subprocess commands are appropriate to the user

[Additionally]
check_knowns.py filters the true positive AMPs from a raw proteome downloaded from Uniprot via known families
