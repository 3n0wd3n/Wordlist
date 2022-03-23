import csv
file = open("btc_word_list.csv")
csvreader = csv.reader(file)

words = []
less_words_bracketsless = []
less_words_brackets = []
for row in csvreader:
  words.append(row)
  if "an" in row[0] or "al" in row[0]:
    less_words_bracketsless.append(row[0])
    less_words_brackets.append(row[0])
print(less_words_bracketsless)
print()
print(less_words_brackets)

file.close()
