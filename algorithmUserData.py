import pandas as pd

data = pd.read_csv("SampleFiles/query.csv")

user_data = {}
# Creates a Dictionary with
# Key: Nexclap Username, Value: Dictionary with
# Key: Column name, Value: Value of given column

weights = {"blogpost": 2,
           "dailyposts": 1,
           "code_posts": 4,
           "vedio_posts": 1,
           "likes_received": 1,
           "comments_received": 1,
           "comments_made": 1}
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
    # Compute the total score for each user by multiplying their scores in each category by the corresponding weights and summing them up

    user_dict["total_score"] = (row["blogpost"] * weights["blogpost"]) + \
        (row["dailyposts"] * weights["dailyposts"]) + \
        (row["code_posts"] * weights["code_posts"]) + \
        (row["vedio_posts"] * weights["vedio_posts"]) + \
        (row["likes_recieved"] * weights["likes_received"]) + \
        (row["comments_received"] * weights["comments_received"]) + \
        (row["comments_made"] * weights["comments_made"])
    # Key = username, Value = dictionary of user's information

    user_data[username] = user_dict


sorted_user_data = sorted(
    user_data.items(), key=lambda x: x[1]['total_score'], reverse=True)
toCsv = pd.DataFrame([user_dict for _, user_dict in sorted_user_data], index=[
                     username for username, _ in sorted_user_data])
toCsv.to_csv("SampleFiles/sorted_user_data.csv")

# Define the weights for each parameter


# Compute the total score for each user by multiplying their scores in each category by the corresponding weights and summing them up
