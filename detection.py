import pandas as pd
import joblib

# Load the trained KMeans model from the file
loaded_model = joblib.load("personality_kmeans_model.pkl")

# Load the test data from the CSV file
test_data = pd.read_csv("testdata.csv")

#The html form responce should produce a csv file like testdata.csv
#1st row is the question tags
#2nd row is the user input range 1-5

#uncomment to see the test data
#print(test_data)

# Make predictions using the loaded model
my_personality = loaded_model.predict(test_data[0:50])

# Define a mapping of cluster numbers to personality types
personality_types = {
    0: "Extraversion (Outgoing/Energetic)",
    1: "Neuroticism (Sensitive/Nervous)",
    2: "Agreeableness (Friendly/Compassionate)",
    3: "Conscientiousness (Efficient/Organized)",
    4: "Openness to Experience (Inventive/Curious)"
}

print("My Personality Cluster: ", my_personality)
print("My Personality Type: ", personality_types[int(my_personality)])