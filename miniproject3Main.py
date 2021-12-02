import csv

import gensim.downloader as api
import pandas as pd
writeToFile=open("testing.txt","+w") # tet file for us nothing important
global row
# model = api.load("word2vec-google-news-300") # opens up the model for googlenews300

dataSet = pd.read_csv("synonyms.csv")

with open("synonyms.csv") as f :
    reader = csv.reader(f)
    for i in range(81):
        for row in reader:
            print(row[i],row[i+1],row[i+2],row[i+3],row[i+4],row[i+5])




# writeToFile.write(f"{model.most_similar(positive=['enormous'], topn=10)}")



