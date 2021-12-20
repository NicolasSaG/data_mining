import pandas as pd
from math import floor
from random import randrange
from sklearn.model_selection import train_test_split

file = pd.read_csv("tabla_hechos.csv",  encoding="utf-8")
df = pd.DataFrame(file)
# print(df.head(30))

n = len(df)

# p_train = ((n - 50) * 0.8)/n
# p_test = ((n - 50) * 0.2)/n
# p_validation = 50/n
# print("train {}, test {}, validation {}".format(p_train, p_test, p_validation))
p_train = 0.76
p_test = .19
p_validation = 0.05

train, test = train_test_split(
    df, test_size=0.19, random_state=randrange(999999))

# print(train.head(10))
# print(test.head(10))
p_validation = 50/len(train)
real_train, validation = train_test_split(
    train, test_size=p_validation, random_state=randrange(999999))

# print(validation.head(10))

real_train.to_csv("dataset_training.csv")
test.to_csv("dataset_testing.csv")
validation.to_csv("dataset_validation.csv")
