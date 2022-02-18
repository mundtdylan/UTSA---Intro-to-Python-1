def main():
    #directory and file names
    dirString = ''
    fileString1 = '9-3-file1.txt'
    fileString2 = '9-3-file2.txt'
    
    #opening files and closing.
    f = open(dirString + fileString1 + fileString2, 'r')
    f.close()
    
    #splitting the files.
    fileString1 = fileString1.split()
    fileString2 = fileString2.split()
    
    #setting files to formatting argument.
    fileSet1 = set(wordFormat(fileString1))
    fileSet2 = set(wordFormat(fileString2))
    
    #print statements and results of the words in files.
    print('These are the unique words that are contained in both files: ')
    print(' '.join(fileSet1.union(fileSet2)))
    print('These are the words that appear both files: ')
    print(' '.join(fileSet1.intersection(fileSet2)))
    print('These are the words that appear in the first file but do not appear in the second file: ')
    print(' '.join(fileSet1.difference(fileSet2)))
    print('These are the words that appear in the second file but do not appear in the first file: ')
    print(' '.join(fileSet2.difference(fileSet1)))
    print('These are the words that appear in the first file or the second file but do not appear in both files: ')
    print(' '.join(fileSet2.symmetric_difference(fileSet1)))
    
#formatting argument to use in print statements.
def wordFormat(word_list):
    words = []
    for word in word_list:
        word = word.replace(',', '')
        word = word.replace('.', '')
        word = word.lower()
        words.append(word)
    return words
    
#closing main program.
main()