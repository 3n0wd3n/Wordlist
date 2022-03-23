import csv
import re

file = open("btc_word_list.csv")

csv = csv.reader(file)

def all_regex():
  arr = []
  for row in csv:
    a = re.search("^al", row[0])
    if a:
      arr.append(row[0])
    aa = re.search("^an", row[0])
    if aa:
      arr.append(row[0])
    c = re.search("^co", row[0])
    if c:
      arr.append(row[0])
    cc = re.search("^cr", row[0])
    if cc:
      arr.append(row[0])
    d = re.search("^da", row[0])
    if d:
      arr.append(row[0])
    e = re.search("^ex", row[0])
    if e:
      arr.append(row[0])
    g = re.search("^gl", row[0])
    if g:
      arr.append(row[0])
    l = re.search("^le", row[0])
    if l:
      arr.append(row[0])
    m = re.search("^mu", row[0])
    if m:
      arr.append(row[0])
    p = re.search("^ph", row[0])
    if p:
      arr.append(row[0])
    s = re.search("^sk", row[0])
    if s:
      arr.append(row[0])
    t = re.search("^th", row[0])
    if t:
      arr.append(row[0])
  return arr

words = all_regex()

print("Word that we choose: ", words)

print("Total len of choosen words: ", len(words))

indexes = [130, 22, 107, 3, 176, 181, 161, 78, 190, 167, 138, 44]

print(len(indexes))

for i in range(12):

  tmp = indexes[i]
  
  print(i + 1, words[tmp])

file.close()
