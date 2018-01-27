from sklearn import tree
from sklearn import svm
from sklearn import gaussian_process
from sklearn import ensemble
from sklearn import neural_network

#[height, weight, shoe size]
X = [[181,80,40], [177,70,43], [160,60,38], [154,54,37], 
     [166,65,40], [190,90,47], [175,64,39], [177,70,40], 
     [159,55,37], [171,75,42], [181,85,43]]
    
Y = ['male', 'female', 'female', 'female', 'male', 'male', 
     'male', 'female', 'male', 'female', 'male']

names = [
    "Decision Tree",
    "Linear SVM",
    "Gaussian Process",
    "Random Forest",
    "Neural Net",
]

classifiers = [
    tree.DecisionTreeClassifier(),
    svm.SVC(kernel="linear", C=0.025),
    gaussian_process.GaussianProcessClassifier(1.0 * gaussian_process.kernels.RBF(1.0)),
    ensemble.RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    neural_network.MLPClassifier(alpha=1),
]

for name, clf in zip(names, classifiers):
    clf.fit(X,Y)
    prediction = clf.predict([[190,70,43],[170,55,41]])
    print(name,':',prediction)

