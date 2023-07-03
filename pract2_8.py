from __future__ import with_statement
import re

words = []
testword = []
ans = []

print("MENU")
print("------------------------")
print("1. Hash tag segmentation")
print("2. URL segmentation")
print("Enter the input choice for performing word segmentaion >>> ")

choice = int(input())
if choice == 1:
    text = "#whatismyname"
    print("input with hashtag", text)
    pattern = re.compile("[^\w']")
    a = pattern.sub('', text)
elif choice == 2:
    text = "www.whatismyname.com"
    print("input with URL", text)
    a = re.split('\s|(?<!\d)[,.](?!\d)', text)
    splitwords = ["www", "com", "in"]
    a = "".join([each for each in a if each not in splitwords])
else:
    print("Wrong Choice..try again")
print(a)

for each in a:
    testword.append(each)
test_lenth = len(testword)

with open('word.txt', 'r') as f:
    lines = f.readlines()
    words = [(e.strip()) for e in lines]


def seg(a, lenth):
    ans = []
    for k in range(0, lenth+1):
        if a[0:k] in words:
            print(a[0:k], "-appears in the corpus")
            ans.append(a[0:k])
        if ans != []:
            g = max(ans, key=len)
            return g


test_tot_itr = 0
answer = []
Score = 0
N = 37
M = 0
C = 0

while test_tot_itr < test_lenth:
    answer_words = seg(a, test_lenth)
    if answer_words != 0:
        test_itr = len(answer_words)
        answer.append(answer_words)
        a = a[test_itr:test_lenth]
        test_tot_itr += test_itr
Aft_seg = " ".join([each for each in answer])
print("output")
print("------------------------")
print(Aft_seg)
C = len(answer)
score = C * N/N
print("Score ", score)