import time, random, math, string

class WordList():

    def __init__(self, filename):
        # create dictionary
        self.wordList = list()
        with open(filename, "r") as infile:
            for line in infile:
                self.wordList.append(line.strip())

    def pickWord(self, minLen=0):
        # randomly choose a word
        while True:
            theHidden = random.choice(self.wordList)
            if len(theHidden) >= minLen:
                break
        # create a list of the same length as the word
        # but contains dashes '-'
        theGameWord = ['-'] * len(theHidden)
        return (theHidden, theGameWord)

# the main program
if __name__ == "__main__":
    wordlist = WordList("dict_ZHANG.txt")

    print(wordlist.pickWord())  # pick a random word

