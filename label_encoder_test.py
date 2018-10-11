#Encode labels with value between 0 and n_classes-1.
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit([1, 2, 2, 6])

print(le.classes_)

print(le.transform([1, 1, 2, 6]))

print(le.inverse_transform([0, 0, 1, 2]))

le = preprocessing.LabelEncoder()
le.fit(["paris", "paris", "tokyo", "amsterdam"])

print(list(le.classes_))

print(le.transform(["tokyo", "tokyo", "paris"]))

print(list(le.inverse_transform([2, 2, 1])))