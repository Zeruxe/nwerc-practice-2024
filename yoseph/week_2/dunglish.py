n = int(input())
sentence = input().split()
m = int(input())

correct_count = 1
incorrect_count = 1

dictionary = {}
for i in range(m):
    word, translation, correctness = input().split()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append((translation, correctness))

for word in sentence:
    correct_options = [translation for translation, c in dictionary[word] if c == "correct"]
    correct_count *= len(correct_options)
    incorrect_count *= len(dictionary[word])

incorrect_count -= correct_count

if correct_count == 1 and incorrect_count == 0:
    translation = " ".join(dictionary[word][0][0] for word in sentence)
    print(translation)
    print("correct")
elif incorrect_count == 1 and correct_count == 0:
    translation = " ".join(dictionary[word][0][0] for word in sentence)
    print(translation)
    print("incorrect")
else:
    print(f"{correct_count} correct")
    print(f"{incorrect_count} incorrect")

"""
def generate_translations(index, current_translation, is_correct):
    global correct_count 
    global incorrect_count 
    if index == n:
        translation_sentence = " ".join(current_translation)
        all_translations.append((translation_sentence, is_correct))
        if is_correct:
            correct_count += 1
        else:
            incorrect_count += 1
        return
    dutch_word = words[index]
    for translation, correctness in dictionary[dutch_word]:
        new_is_correct = is_correct and (correctness == "correct")
        generate_translations(index + 1, current_translation + [translation], new_is_correct)

generate_translations(0, [], True)

"""