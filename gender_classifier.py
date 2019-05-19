from sklearn import tree

# [height,weight, shoe size]
X = [[180,90,44], [140,50,37],[150,60,39],[180,90,46],[130,40,35],[140,60,40],[170,85,42],[130,50,34],[160,75,39],[190,110,48]]

Y = ['male', 'female', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

prediction = clf.predict([[190,80,48]])
print(prediction)

