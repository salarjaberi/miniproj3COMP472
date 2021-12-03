import csv
import gensim.downloader as api
import pandas as pd

# This fucntion is used to get a list of all the models in the Gsim Model - no need to keep it in the
# functioning code - we used it to find new models for part 2
# print(list(gensim.downloader.info()['models'].keys()))


dataSet = pd.read_csv("synonyms.csv")
# tesing pls work github is not letting me push anything.
# model1 = api.load("word2vec-google-news-300")  # opens up the google-news-300 task 1 part 1
# model2 = api.load("glove-wiki-gigaword-300")   # task 2 model 1 size -300
# model3 = api.load("fasttext-wiki-news-subwords-300") # task 2 model 2  size -300
model4 = api.load("glove-twitter-25")
model5 = api.load("glove-twitter-50")



global numCorrectLabel, withoutGuessing, accuracy, wrongGuesses


def mainFunction(model, modelName, csvName):
    numCorrectLabel = 0
    withoutGuessing = 0
    accuracy = 0
    wrongGuesses = 0
    count = 0
    count_A = 0
    countx=0
    for i in dataSet.index:
        countx=countx+1
        guess = ""  # empty intialize
        label = ""  # labels if it is a correct , guess or wrong
        # labels question and answer
        question = dataSet["question"][i]
        answer = dataSet["answer"][i]

        try:
            # option words from the synonym.cvs file
            w0 = dataSet["0"][i]
            w1 = dataSet["1"][i]
            w2 = dataSet["2"][i]
            w3 = dataSet["3"][i]

            # calculates the similarities from word2vec
            sim0 = model.similarity(question, w0)
            sim1 = model.similarity(question, w1)
            sim2 = model.similarity(question, w2)
            sim3 = model.similarity(question, w3)

            # taking the max sim prob between all sim0->sim3
            max_sim_prob = max(sim0, sim1, sim2, sim3)

            # sorting the max sim and assinging the guess word to the highest number
            if max_sim_prob == sim0:
                guess = w0
                label = "correct"

            elif max_sim_prob == sim1:
                guess = w1
                label = "correct"

            elif max_sim_prob == sim2:
                guess = w2
                label = "correct"

            elif max_sim_prob == sim3:
                guess = w3
                label = "correct"

            if guess == answer:
                numCorrectLabel = numCorrectLabel + 1
            # this knows if the guess based on probabilities is right or wrong
            if guess != answer:
                wrongGuesses = wrongGuesses + 1
                label = "wrong"
        # if we get a keyerror - not found - it will print as "guess" for label.
        except KeyError:
            guess = "N/A"
            label = "guess"

        withoutGuessing = (numCorrectLabel + wrongGuesses)
        accuracy = (numCorrectLabel / withoutGuessing) * 100

        header = ['Question', 'Answer', 'Guess', 'Label']
        data = [question, answer, guess, label]

        with open(csvName, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            if count == 0:  # write the header count to 0 simply to get the titles once
                writer.writerow(header)
                count = 1

            writer.writerow(data)  # write the data

        # analyis.csv info
        sizeofVocab = len(model)
        header2 = ['Model Name', 'Size Of Vocab', 'Num. Correct Labels', 'Without Guessing', 'Accuracy']
        data2 = [modelName, sizeofVocab, numCorrectLabel, withoutGuessing, accuracy]
        with open("analysis.csv", 'a', encoding='UTF8', newline='') as f2:
            writer = csv.writer(f2)
            if count_A == 0:
                writer.writerow(header2)
                count_A=1
            if countx==80:
                writer.writerow(data2)  # write the csv file - only prints last one we need

        count = count + 1
        count_A = count_A + 1

    return model

# ----------------------------Task 1-----------------------------------------------
# modelName1 = "Word2vec-google-news-300"
# csvfileName1 = 'Word2vec-google-news-300-details.csv'
# mainFunction(model1, modelName1, csvfileName1, analysis)

# ----------------------------Task 2 Model 1 glove-wiki-gigaword-300-----------------------------------------------
# modelName2 = "glove-wiki-gigaword-300"
# csvfileName2 = 'glove-wiki-gigaword-300.csv'
# mainFunction(model2, modelName2, csvfileName2, analysis)

# ----------------------------Task 2 Model 2 fasttext-wiki-news-subwords-300-----------------------------------------------
# modelName3 = "fasttext-wiki-news-subwords-300"
# csvfileName3 = 'fasttext-wiki-news-subwords-300.csv'
# mainFunction(model3, modelName3, csvfileName3, analysis)


# ----------------------------Task 2 Model 3 glove-twitter-25----------------------------------------------
modelName4 = "glove-twitter-25"
csvfileName4 = 'glove-twitter-25.csv'
mainFunction(model4, modelName4, csvfileName4)


# ----------------------------Task 2 Model 4 glove-twitter-50----------------------------------------------
modelName5 = "glove-twitter-50"
csvfileName5 = 'glove-twitter-50.csv'
mainFunction(model5, modelName5, csvfileName5)