# GenderClassifier

Based on Siraj Raval python tutorial:

https://www.youtube.com/watch?v=T5pRlIbr6gg&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU

Including my solution for the challenge.

## Dependencies

- Scikit-learn (http://scikit-learn.org/stable/install.html)
- numpy (`pip install numpy`)
- scipy (`pip install scipy`)

## Result

Output:
```
Decision Tree : ['female' 'male']
Linear SVM : ['male' 'female']
Gaussian Process : ['female' 'male']
Random Forest : ['male' 'male']
Neural Net : ['male' 'male']
```

Exspected result: `['male' 'male']`

For this small test Random Forest and Neural Net classifier are the most accurate. 
But since the data set is tiny this result is not very meaningfull.
