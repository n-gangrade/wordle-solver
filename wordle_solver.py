guess = ''
feedback = ''
possible_words = []

#open file with all possible wordle solutions'
with open("wordlist.txt") as f:
    for line in f:
        possible_words.append(line.strip())

print("Some good starter words are: adieu, audio, or canoe")

for guesses in range(6):
    guess = input("Enter your word: ").lower()
    print("g - green, y - yellow, w - wrong/grey")
    feedback = input("Feedback: ").lower()
    if feedback == "ggggg":
        print("Well done!")
        break
    
    possible_words_tuple = tuple(possible_words)
    for word in possible_words_tuple: #goes over every possible word 
        for i in range(5): #goes over all the letters in the word to see whether a word should be removed from the list
            if feedback[i] == "w" and guess[i] in word: #if grey letter is anywhere in the word
                possible_words.remove(word)
                break
            elif feedback[i] == "g" and guess[i] != word[i]: #if green letter is not in the same location in the word
                possible_words.remove(word)
                break
            elif feedback[i] == "y" and guess[i] not in word: #if yellow letter is not anywhere in the word
                possible_words.remove(word)
                break
            elif feedback[i] == "y" and guess[i] == word[i]: #if yellow letter is in same location in the word
                possible_words.remove(word)
                break
    
    count = 0
    for word in possible_words:
        print(word, end=", ")
        count += 1
        if count == 8:
            print("")
            count = 0

