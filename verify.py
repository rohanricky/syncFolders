import os

dir_path = os.path.dirname(os.path.realpath(__file__))

DIRECTORY_TO_WATCH = dir_path+"/DroidA"
SECOND = dir_path+"/DroidB"

files = []
second = []
for x in os.listdir(DIRECTORY_TO_WATCH):
    files.append(x)

for y in os.listdir(SECOND):
    second.append(y)

def cmp(a, b):
    return (a > b) - (a < b)

print(cmp(files,second))
