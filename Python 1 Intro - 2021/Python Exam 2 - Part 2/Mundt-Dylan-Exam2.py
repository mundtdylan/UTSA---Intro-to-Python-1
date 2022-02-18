#Dylan-Mundt-onf721-11/4/21 Exam 2-Part 2

def main():
  # Opens and reads the three different files into lists: 
  # nouns, verbs, and prepositions.
    try:
        listNoun = open('noun-phrases.txt', 'r')
        listVerb = open('verbs.txt', 'r')
        listPrep = open('prepositions.txt', 'r')
        sentences = open('my_sentences.txt', 'w')
    #error exceptions.
    except IOError:
        print("The file could not be found.")
    except IndexError:
        print("There was an indexing error.")
    except:
        print("There was an error.")
      # Reads the lists into strings.
    listNoun = listNoun.readlines()
    listVerb = listVerb.readlines()
    listPrep = listPrep.readlines()
      # Removes the newline characters from the strings.
    for i in range(len(listNoun)):
        listNoun[i] = listNoun[i].rstrip('\n')
    for i in range(len(listVerb)):
        listVerb[i] = listVerb[i].rstrip('\n')
    for i in range(len(listPrep)):
        listPrep[i] = listPrep[i].rstrip('\n')
    
      # call sentenceBuilder() 25 times and write the sentences to the file, numbered 1-25.
    for i in range(25):
        sentences.write(str(i+1) + ". " + sentenceBuilder(listNoun, listVerb) + "\n")
        
# Function verbPhrase() that takes in list of verb, nouns and prepositions. and returns a random verb phrase.
def verbPhrase(listNoun, listVerb, listPrep):
    import random
    return (random.choice(listVerb) + random.choice(listNoun) + listPrep)

# Function prepPhrase() that takes in list of nouns and prepositions. and returns a random prepositional phrase.
def prepPhrase(listNoun, listPrep):
    import random
    return (random.choice(listPrep) + random.choice(listNoun))
# SentenceBuilder() that takes in nounPhrase and verbPhrase and returns a complete sentence. Use rndom to select a noun randomly from the list, strip spaces, add a period and capitalize the first letter.
def sentenceBuilder(listNoun, listVerb):
    import random
    return (random.choice(listVerb).strip()[0].upper() + random.choice(listNoun).strip()[1:].lower() +  " " + ".")
        
main()