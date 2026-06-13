"""Task 7: Data Cleaning Mini Project

Questions
Remove extra spaces.
Convert names to title case.
Find missing emails.
Replace missing emails with "Not Provided".

Concepts: String Cleaning, Missing Values"""

import pandas as pd

data = {
    "Name": ["John ", " ALICE", "bob", "Emma"],
    "Email": ["john@gmail.com", "alice@gmail.com", None, "emma@gmail.com"]
}

df=pd.DataFrame(data)

print(df)

df["Name"]=df["Name"].str.strip()

df["Name"]=df["Name"].str.title()

print(df[df["Email"].isna()])

df["Email"]=df["Email"].fillna("Not Provided")

print(df)

