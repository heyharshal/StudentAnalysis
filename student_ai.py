from sklearn.tree import DecisionTreeClassifier

# Training Data
marks = [[95], [85], [75], [65], [55], [45], [35]]
result = ["Pass", "Pass", "Pass", "Pass", "Pass", "Fail", "Fail"]

# AI Model Banana
model = DecisionTreeClassifier()

# Model Ko Sikhana (Training)
model.fit(marks, result)

# User Se Input Lena
new_marks = int(input("Enter Marks: "))

# Prediction Karna
prediction = model.predict([[new_marks]])

print("Prediction:", prediction[0])