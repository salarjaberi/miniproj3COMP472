# miniproj3COMP472
the git hub url: https://github.com/salarjaberi/miniproj3COMP472
In this submission, you will be able to obtain 6 deliverables:
5 <model name>-details.csv which contains the question word, the answer, the system's guess and the label(correct,wrong,guess)
We used the following models: 
1- word2vec-google-news-300 
2-glove-wiki-gigaword-300
3-fasttext-wiki-news-subwords-300
4-glove-twitter-25
5-glove-twitter-50
1 analysis.csv which contains the performance parameters of each model such as model name, size of the corpus
,the number of correct labels, the number of questions that the model answered without guessing(correct+wrong labels) and the accuracy.

Steps to run the code:
**1** - There is nothing special to run our code - Simply run the code. Keep in mind that the api.load for the models will take time to run 
**2** - Output results are shown in the output folder, if you wish to run it again it will output in the project directory 