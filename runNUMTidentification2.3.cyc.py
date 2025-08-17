### Reorganize the previous runNUMTidentification.py
### runNUMTidentification2.3.cyc.py
### v2 2024/03/11
### swarmGenomics version
### v1 2023/12/04
### print shell script
### @author:Chen Yu Chi

import os,sys
import csv
import pandas as pd
import re

dir_work = '/vol/storage/'
file_mito = '/vol/storage/MitoAvian/4NUMTS/Acanthisitta_chloris.fasta'
file_genome = '/vol/storage/MitoAvian/4NUMTS/genomes/Acanthisitta_chloris.fna'
file_bedR = '/vol/storage/software/get_bed2.R'
species = 'Acanthisitta_chloris'

os.system('makeblastdb -in ' + file_mito + ' -parse_seqids -dbtype nucl')
os.system('makeblastdb -in ' + file_genome + ' -parse_seqids -dbtype nucl')

os.system('blastn -db '+ file_genome + ' -query '+ file_mito +' -outfmt 7 -word_size 20 -num_threads 1 -out ' + dir_work + species +'.blast.out')
os.system("grep -v '#' " + dir_work + species +".blast.out | cut -d '\t' -f2,3,4,9,10 > " + dir_work + species + ".blast.clean.out")

os.system('ls -1 ' + dir_work + species + '.blast.clean.out > ' + dir_work + 'files_list.txt')
os.system('cp ' + file_bedR + ' ' + dir_work)
os.system('Rscript get_bed2.R')
os.system('rm get_bed2.R')

os.system('bedtools getfasta -fi '+ file_genome +' -bed ' + dir_work + species + '.blast.clean.out_AllFrags.bed -fo ' + dir_work + species + '.sep.fa')

	