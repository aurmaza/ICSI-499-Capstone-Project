import pandas as pd

data = pd.read_csv("query.csv")

user_data = {}
# Creates a Dictionary with
# Key: Nexclap Username, Value: Dictionary with
# Key: Column name, Value: Value of given column


for index, row in data.iterrows():
    # Create dictionary for value of user data key
    user_dict = {}
    # for all non-marking columns
    for col_name in data.columns[1:]:
        # Add that column name and its value to the user dictionary
        user_dict[col_name] = row[col_name]
    # extract the username
    username = row['nexclapURL'].replace("https://nexclap.com/", "")
    # Add that users dictionary to the dictionary for user data
    # Key = username, Value = dictionary of user's information
    user_data[username] = user_dict
print(user_data['RushilRoy14247']['dailyposts'])
