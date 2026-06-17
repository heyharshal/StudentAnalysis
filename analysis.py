import pandas as pd

df = pd.read_csv("student.csv")

print("Student Data:")
print(df)

print("\nAverage Marks:")
print(df[["Maths", "Science", "English"]].mean())

df["Total"] = df["Maths"] + df["Science"] + df["English"]

print("\nTopper:")
print(df.loc[df["Total"].idxmax()])
import matplotlib.pyplot as plt

avg_marks = df[["Maths", "Science", "English"]].mean()

avg_marks.plot(kind="bar")

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()