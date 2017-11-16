# Studienarbeit

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset 1
import csv

with open('europarl-v78.txt', 'r', encoding=('utf-8')) as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('europarl-v78.csv', 'w', encoding=('utf-8')) as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)
        
Dataset1 = pd.read_csv('europarl-v78.csv', sep= "\t", header= None)

# dataset= pandas.read_csv('./input/dists.txt', sep= "delimiter", header= none)
#dataset2 = pd.read_table("C:\\Users\\User\\Desktop\\desktop\\StudienArbeit\\parallel corpura\\europarl-v78.txt")

# Importing the dataset 2
with open('europarl-v7.txt', 'r', encoding=('utf-8')) as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('europarl-v7.csv', 'w', encoding=('utf-8')) as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)
        
Dataset2 = pd.read_csv('europarl-v7.csv',sep="delimiter", header= None, engine='python')

#Merging Dataset1 and Dataset2
Dataset3 = pd.concat([Dataset1,Dataset2], axis=1)
# Tokenise the text
import re
from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
tokenizer.tokenize()

