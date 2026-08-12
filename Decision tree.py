from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder

# Data: Age, Income, Existing Loan, Approval
data = [
    ["Young","Low","No","No"],
    ["Young","High","No","Yes"],
    ["Middle","Low","Yes","Yes"],
    ["Middle","High","Yes","Yes"],
    ["Old","Low","Yes","Yes"],
    ["Old","High","No","No"]
]

X = []
y = []

enc = [LabelEncoder() for i in range(3)]

for i in range(3):
    enc[i].fit([r[i] for r in data])

for r in data:
    X.append([enc[i].transform([r[i]])[0] for i in range(3)])
    y.append(r[3])

model = DecisionTreeClassifier(criterion="entropy", max_depth=3)
model.fit(X, y)

print("DECISION TREE")
print(export_text(model,
      feature_names=["Age","Income","Existing_Loan"]))

# Prediction
new = [["Middle","High","No"]]
new = [[enc[i].transform([new[0][i]])[0] for i in range(3)]]

print("Loan Decision:", model.predict(new)[0])