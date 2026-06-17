import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Player": ["Virat", "Rohit", "Dhoni", "Gill", "KL Rahul"],
    "Runs": [741, 635, 520, 890, 610]
}

df = pd.DataFrame(data)

print(df)

plt.bar(df["Player"], df["Runs"])
plt.title("IPL Runs Analysis")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.show()