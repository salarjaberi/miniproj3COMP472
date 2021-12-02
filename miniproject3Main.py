import csv
import gensim.downloader as api
import pandas as pd
import pandas as pd
dataSet = pd.read_csv("synonyms.csv")
model = api.load("word2vec-google-news-300") # opens up the mode
global numCorrectLabel,withoutGuessing,accuracy,wrongGuesses
numCorrectLabel = 0
withoutGuessing = 0
accuracy = 0
wrongGuesses=0

count = 0
for i in dataSet.index:
    guess="" # empty intialize
    label="" # labels if it is a correct , guess or wrong

    # labels question and answer
    question = dataSet["question"][i]
    answer = dataSet["answer"][i]
    try:
        # option words from the synonym.cvs file
        w0 =dataSet["0"][i]
        w1 =dataSet["1"][i]
        w2 = dataSet["2"][i]
        w3 = dataSet["3"][i]

        # calculates the similarities from word2vec
        sim0= model.similarity(question,w0)
        sim1 = model.similarity(question, w1)
        sim2 = model.similarity(question, w2)
        sim3 = model.similarity(question, w3)

        # taking the max sim prob between all sim0->sim3
        max_sim_prob = max(sim0,sim1,sim2,sim3)

        #sorting the max sim and assinging the guess word to the highest number
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

        if guess==answer:
            numCorrectLabel=numCorrectLabel+1

        # this knows if the guess based on probabilities is right or wrong
        if guess!=answer:
            wrongGuesses=wrongGuesses+1
            label="wrong"


    # if we get a keyerror - not found - it will print as "guess" for label.
    except KeyError:
            guess="N/A"
            label="guess"

    withoutGuessing=(numCorrectLabel+wrongGuesses)
    accuracy=(numCorrectLabel/withoutGuessing) * 100

    header = ['Question', 'Answer', 'Guess', 'Label']
    data = [question, answer, guess, label]
    with open('Word2vec-google-news-300-details.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        if count == 0: # write the header count to 0 simply to get the titles once
            writer.writerow(header)
            count = 1
        writer.writerow(data) # write the data

    modelName="Word2vec-google-news-300"
    sizeofVocab=len(model)


    header2 = ['Model Name','Size Of Vocab','Num. Correct Labels','Without Guessing','Accuracy']
    data2 = [modelName, sizeofVocab, numCorrectLabel,withoutGuessing,accuracy]
    with open('analysis.csv', '+w', encoding='UTF8', newline='') as f2:
        writer = csv.writer(f2)

        writer.writerow(header2)

        writer.writerow(data2)  # write the data


    count = count + 1