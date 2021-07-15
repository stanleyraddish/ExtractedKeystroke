import random

def splitExamples(mainFile, trainFile, crossVFile, testFile, examples):
    x = [i for i in range(examples)]
    random.shuffle(x)
    train = x[0:50] # Indices of training data
    crossV = x[50:70] # Indices of CV data
    test = x[70:90] # Indices to split to test
    mainF = open(mainFile, "r")
    trainF = open(trainFile, "a")
    crossVF = open(crossVFile, "a")
    testF = open(testFile, "a")
    data = mainF.readlines()
    for i in train:
        trainF.write(data[3*i])
        trainF.write(data[3*i + 1])
        trainF.write("\n")
    for i in crossV:
        crossVF.write(data[3*i])
        crossVF.write(data[3*i + 1])
        crossVF.write("\n")
    for i in test:
        testF.write(data[3*i])
        testF.write(data[3*i + 1])
        testF.write("\n")
    mainF.close()
    trainF.close()
    crossVF.close()
    testF.close()

splitExamples("worddata4.txt", "wordtrain.txt", "wordCV.txt", "wordtest.txt", 90)



