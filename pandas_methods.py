
import pandas as pd

df = pd.DataFrame({
    "Name":["lokesh","sravan","CBN","KCR","RR","PSPK"],
    # "Party":["TDP","YSRCP","TDP","","CONGRESS","JS"]
    "Party":["TDP","YSRCP","TDP",None,"CONGRESS","JS"]
})
print(df)

df = pd.DataFrame({
    "Name": ["geethu", "Priya", "nandhu"],
    "Age": [28, 30, 22],
    "Salary": [45000, 60000, 40000]
})

print(df)

data = {
    "Name": ["supriya","jerry","micky"],
    "Age": [25, 27, 28],
    "Salary": [50000, 100000, 80000]
}
df=pd.DataFrame(data)
print(df)

data = [
    {"Name": "hardik pandya", "Age": 32, "Salary": 95000000},
    {"Name": "sanju samsun", "Age": 31, "Salary": 18000000},
    {"Name": "tilak varma", "Age": 23, "Salary": 80000000}
]

df = pd.DataFrame(data)
print(df)

#missing keys
data = [
    {"Name": "hardik pandya", "Age": 32, "Salary": 95000000},
    {"Name": "sanju samsun", "Age": 31},
    {"Name": "tilak varma", "Salary": 80000000}
]
df=pd.DataFrame(data)
print(data)

import numpy as np
arr = np.array([
    [101, 25, 45000],
    [102, 28, 60000],
    [103, 24, 40000]
])

df = pd.DataFrame(
    arr,
    columns=["Employee_ID", "Age", "Salary"]
)

print(df)
df = pd.DataFrame(
    {
        "Name": ["x", "y", "z"],
        "Salary": [45000, 60000, 40000]
    },
    index=["E101", "E102", "E103"]
)
print(df)

a = {
    "Name": ["geethu", "Priya", "kushvi"],
    "Salary": [50000, 60000, 40000],
    "Age": [22, 24, 23]
}
df = pd.DataFrame(
    a,
    columns=["Name", "Age", "Salary"]
)
print(df)

df = pd.DataFrame(
    {
        "Name": ["geethu", "Priya", "kushvi"],
        "Age": [23, 22, 24],
        "Salary": [45000, 60000, 40000]
    },
    index=["E101", "E102", "E103"]
)
# loc()

print(df.loc["E102"])
print(df.loc["E101":"E103"])

# iloc()

print(df.iloc[0])

df["Annual_salary"] = df["Salary"]*12

df["High_salary"] = df["Salary"]>50000

df["Bonus"] = df["Annual_salary"]*0.05

df["Companies"] = "ABC Technologies"

print(df[df["High_salary"]])
df = df.drop(columns=["Companies","High_salary"])

# # Rename|

df = df.rename(
    columns={
        "Name" : "Employee_Name",
        "Salary" : "Monthly_Salary"
    }
)
print(df)



import pandas as pd
df = pd.DataFrame({
    "org_name":["Google","Oracle","Ibm","Jp morgan","Delloite"],
    "dept":["IT","HR","FINANCE","MARKETING","AUDIT"],
    "type":["product","product","service","service","service"],
    "salary":[100000,80000,60000,90000,35000]
},index=["c1","c2","c3","c4","c5"]
)

print(df)
print(df[df["type"]=="product"])

print(df[df["salary"].between(50000,100000,inclusive="left")])
print(df[df["salary"].between(50000,100000,inclusive="right")])

print(df.query("dept=='IT'"))

minimum_salary=60000
print(df.query(
    f"salary>{minimum_salary}"
))

dept = "IT"
print(df.query("dept==@dept"))

print(df.where(df["salary"]>70000,other="N/A"))

print(df.mask(df["salary"]<80000))

print(df.loc[
    df["salary"]>80000,
    ["org_name","dept","salary"]
])

print(df.loc[
    (df["dept"].isin(["IT","AUDIT"])) &
    (df["salary"].between(40000,100000,inclusive="both")),
    ["org_name","salary"]
])

mask=df["salary"]>60000
print(mask.to_numpy())
print(df.filter(like="sal"))

# comparision methods

print(df["salary"].gt(50000))   # >
print(df["salary"].ge(80000))   # >=
print(df["salary"].lt(60000))   # <
print(df["salary"].le(70000))   #<=
print(df["salary"].eq(90000))   # ==
print(df["salary"].ne(35000))   # !=

employees = pd.DataFrame({
    "EmpID": ["E101", "E102", "E103", "E104"],
    "Name": ["Geethu", "Priya", "Kushvee", "Meghana"],
    "Department": ["IT", "HR", "SALES", "FINANCE"],
    "City": ["Hyderabad", "Mumbai", "Bangalore", "Chennai"],
    "Age": [25, 24, 26, 30],
    "Salary": [65000, 55000, 88000, 20000],
    "Experience": [6, 3, 2, 4]
},index=["e1","e2","e3","e4"]
)

# Select employees from IT, HR, or Finance using isin().
print(employees[employees["Department"].isin(["IT", "HR", "FINANCE"])])

# Select employees aged between 25 and 30 using between().
print(employees[employees["Age"].between(25,30)])

# Select employees earning between ₹50,000 and ₹80,000.
print(employees[employees["Salary"].between(50000,80000)])

# print(employees[employees["City"].between(50000,80000)])

# Select employees from Hyderabad or Mumbai.
print(employees[employees["City"] == "Hyderabad"])

# Select employees who are not from IT.
print(employees[employees["Department"] != "IT"])

# Select employees from IT with more than 5 years of experience.
print(employees[(employees["Department"] == "IT") & (employees["Experience"] > 5)])

# Use loc to return only Name, Department, City, and Salary.
print(employees.loc[:, ["Name","City","Department","Salary"]])

# Rewrite one complex filter using query().
print(employees.query("Salary > 60000 and Age < 30"))

# Use where() to keep salaries above ₹60,000 and replace other values with NaN.
print(employees["Salary"].where(employees["Salary"] > 60000))

# Use mask() to replace salaries below ₹50,000 with 0.
print(employees["Salary"].mask(employees["Salary"]<50000,0))

# Use filter(like='Sal') to select salary-related columns.
print(employees.filter(like="Sal"))