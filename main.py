### # 1. 
import random
list_of_words_1 = ["Hi", "Hello", "Good after noon", "I think you good"]
list_of_words_2 = ["Tell me", "About", "Something"]
list_of_words_3 = ["Yeah", "It's good", "Soo", "Yep"]

print(list_of_words_1[random.randint(0, len(list_of_words_1)-1)]+" "+list_of_words_2[random.randint(0, len(list_of_words_2)-1)]+" "+list_of_words_3[random.randint(0, len(list_of_words_3)-1)])


### # 2.1
text = open("text.txt", "r",1)
lines = ""
for line in text:
    lines = line

print("З пробілами "+ str(len(lines)))

splited_line = lines.split(" ")
without = 0
for word in splited_line:
    without += len(word)

print("Без пробілів "+str(without))

### # 2.2

print("Слів "+ str(len(splited_line)))

not_same_words = []

for word in splited_line:
    if word not in not_same_words:
        not_same_words.append(word)

print("Різних слів "+ str(len(not_same_words)))

### 3.4

text_2 = open("3.txt", "r", 1)

line = ""
for line_no in text_2:
    line = line_no

splited_on_dots_3 = line.split("...")
splited_on_dots = line.split(".")

print(len(splited_on_dots)-1-((len(splited_on_dots_3)-1)*3))
splited_on_question_mark = line.split("?")
print(len(splited_on_question_mark)-1)
splited_on_znak_okluku = line.split("!")
print(len(splited_on_znak_okluku)-1)
splited_on_dots_3 = line.split("...")
print(len(splited_on_dots_3)-1)