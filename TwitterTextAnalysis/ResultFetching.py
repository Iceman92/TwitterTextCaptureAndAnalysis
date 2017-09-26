from collections import defaultdict
from collections import Counter

#List of files according to the question asked
FileA = "./MaximumNoOfTweets.txt"
FileB = "./MaximumNoOfTweetsEveryHour.txt"
FileC = "./MaximumNoOfFollowers.txt"
FileD = "./MaximumNoOfRetweets.txt"

#The file to be read from
ResultFile_PATH = "./USA.txt"

COUNTER = Counter()
USERNAMES = defaultdict(int)

#The number input by the user
N = int(input("Enter value of N: "))

F = open(ResultFile_PATH, 'r', encoding = "utf-8")


#Question a
for line in F:
    USERNAMES[line.split("\t|\t")[0]] += 1
COUNTER = Counter(USERNAMES)
print(COUNTER.most_common(N))
TEXT_FILE = open(FileA, "w")
TEXT_FILE.write('\n'.join(str(d) for d in COUNTER.most_common(N)))
TEXT_FILE.close()
F.close()

#Question c
F = open(ResultFile_PATH, 'r', encoding = "utf-8")
USERNAMES = defaultdict(int)
COUNTER = Counter()
for line in F:
    if len(line.split("\t|\t")) == 5:
        USERNAMES[line.split("\t|\t")[0]] += int(line.split("\t|\t")[3])
COUNTER = Counter(USERNAMES)
print(COUNTER.most_common(N))
TEXT_FILE = open(FileC, "w")
TEXT_FILE.write('\n'.join(str(d) for d in COUNTER.most_common(N)))
TEXT_FILE.close()
F.close()

#Question d
F = open(ResultFile_PATH, 'r', encoding = "utf-8")
USERNAMES = defaultdict(int)
COUNTER = Counter()
for line in F:
    if len(line.split("\t|\t")) == 5:
        USERNAMES[line.split("\t|\t")[0]] += int(line.split("\t|\t")[4])
COUNTER = Counter(USERNAMES)
print(COUNTER.most_common(N))
TEXT_FILE = open(FileD, "w")
TEXT_FILE.write('\n'.join(str(d) for d in COUNTER.most_common(N)))
TEXT_FILE.close()
F.close()
