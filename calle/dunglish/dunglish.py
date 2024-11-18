n = int(input())

sentence = input().split()

m = int(input())

dictionary = {}

for _ in range(m): 
    word, translation, correct = input().split()
    if not dictionary.get(word): 
        dictionary[word] = [(translation, correct)]
    else: 
        dictionary[word].append((translation, correct))

count_correct = 1
count_incorrect = 1


for val in sentence: 
    count_correct *= len([word[0] for word in dictionary[val] if word[1]== 'correct'])
    count_incorrect *= len(dictionary[val])

count_incorrect -= count_correct

if count_correct == 1 and not count_incorrect: 
    for i, word in enumerate(sentence): 
        print(dictionary[word][0][0], end = '')
        if i != len(sentence)-1: 
            print(" ", end = '') 
    print()
    print("correct")
elif count_incorrect == 1 and not count_correct: 
    for i, word in enumerate(sentence): 
        print(dictionary[word][0][0], end = ' ')
        if i != len(sentence)-1: 
            print(" ", end = '') 
    print()
    print("incorrect")
else: 
    print(count_correct, "correct")
    print(count_incorrect, "incorrect")

