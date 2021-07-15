Initial Data (Folder) 
	- word data 1, word data 2, word data 3, word data 4 (.txt Files)
		- Individual data collected from each participant from typing target word
	- sentencedata1, sentencedata2, sentencedata3, sentencedata4 (.txt Files)
		- Individual data collected from each participant from typing target sentence
		  (Data is extracted from sentence to represent timing of targt word)

Programs (Folder) 
	- KeyTime Word (Python File)
		- Program that asks client to type a target word and records time data in file
	- KeyTime Sentence Extract (Python File)
		- Program that asks cllient to type a target sentence and records extracted data
		  that corrsponds to time data of target word
	- trainCVtest split (Python File)
		- Program that reads a file containing individual data and splits data at                          random into respective training, cross-validation, and test data files

script1 (.txt File)
	- Network script used for both simulations

wordtraindata (.txt File)
	- Contains 50 instances of data from each participant, for a total of 200 training
          examples

wordCVdata (.txt File)
	- Contains 20 instances of data from each participant, for a total of 80 cross
          validation examples used to optimize learning parameters

wordtestdata (.txt File)
	- Contains 20 instances of data from each participant, for a total of 80 test examples             used to evaluate network training

sentencetestdata (.txt File)
	- Contains all 20 instances of data from each participants, for a total of 80 test
          examples. Note that this test data is time data of the target word extracted
          from typing the target sentence

Simulation Images (Folder)
	- Hidden Units CV Errors (PNG) (Included in paper)
		- picture of CV error/accuracy trained on different number of hidden units
	- Simulation 1 Test - 5 Hidden Error Curves (PNG)
		- picture of error curves on training 120 epochs with 6 hidden units
	- Simulation 1 Test - 6 Hidden (PNG) (Included in paper)
		- picture of test error/accuracy for network with 6 hidden units
	- Simulation 2 Extracted Test - 6 Hidden (PNG) (Included in paper)
		- picture of classification accuracy of keystroke data extracted from sentences
