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
1- download the desired corpus using the following code: model = api.load(" your model name")".
2- pass to the Main function the following parameters using the following code: 
mainFunction("model, "The name of your model", <model name>-details.csv, analysis.csv)"