with open('Data/word_list.txt', 'r') as file:
    allText = file.read() 
    wordlist = list(map(str, allText.split()))