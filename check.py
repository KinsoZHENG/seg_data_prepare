import os
from sklearn.model_selection import train_test_split

path = "./ori_image/"
files = os.listdir(path)

names = []
for file in files:
    name = os.path.splitext(file)[0]
    names.append(name)


trains, vals = train_test_split(names, test_size=0.2, random_state=0)

with open("train.txt", 'a') as f:
    for train in trains:
        info = train + "\n"
        f.write(info)

with open("val.txt", 'a') as f:
    for val in vals:
        info = val + "\n"
        f.write(info)