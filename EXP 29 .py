#29.Scenario: Decision Tree for Iris Flower ClassificationYou are analyzing the famous Iris flower dataset to classify iris flowers into three species based on
#their sepal and petal dimensions. You want to use a Decision Tree classifier to accomplish this task.Write a Python program that loads the Iris dataset from scikit-learn, and allows the user to input the
#sepal length, sepal width, petal length, and petal width of a new flower. The program should then usethe Decision Tree classifier to predict the species of the new flower.

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Train Model
model = DecisionTreeClassifier()
model.fit(X, y)

# User Input
sepal_length = float(input("Enter Sepal Length: "))
sepal_width = float(input("Enter Sepal Width: "))
petal_length = float(input("Enter Petal Length: "))
petal_width = float(input("Enter Petal Width: "))

flower = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

prediction = model.predict(flower)

species = iris.target_names[prediction[0]]

print("\nPredicted Species:", species)
