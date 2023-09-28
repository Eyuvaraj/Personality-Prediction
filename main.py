import streamlit as st
import pandas as pd
import joblib

# Load the trained KMeans model from the file
loaded_model = joblib.load("personality_kmeans_model.pkl")

st.set_page_config(
    page_title="Personality Prediction App",
    layout="wide",
    page_icon="🌼",
    menu_items=None
)

# Add a title
st.title("Personality Prediction App")
st.markdown("#### :red[Big 5 Personality Test]")
st.divider()

questions = {
    "EXT1": "I am the life of the party.",
    "EXT2": "I don't talk a lot.",
    "EXT3": "I feel comfortable around people.",
    "EXT4": "I keep in the background.",
    "EXT5": "I start conversations.",
    "EXT6": "I have little to say.",
    "EXT7": "I talk to a lot of different people at parties.",
    "EXT8": "I don't like to draw attention to myself.",
    "EXT9": "I don't mind being the center of attention.",
    "EXT10": "I am quiet around strangers.",
    "EST1": "I get stressed out easily.",
    "EST2": "I am relaxed most of the time.",
    "EST3": "I worry about things.",
    "EST4": "I seldom feel blue.",
    "EST5": "I am easily disturbed.",
    "EST6": "I get upset easily.",
    "EST7": "I change my mood a lot.",
    "EST8": "I have frequent mood swings.",
    "EST9": "I get irritated easily.",
    "EST10": "I often feel blue.",
    "AGR1": "I feel little concern for others.",
    "AGR2": "I am interested in people.",
    "AGR3": "I insult people.",
    "AGR4": "I sympathize with others' feelings.",
    "AGR5": "I am not interested in other people's problems.",
    "AGR6": "I have a soft heart.",
    "AGR7": "I am not really interested in others.",
    "AGR8": "I take time out for others.",
    "AGR9": "I feel others' emotions.",
    "AGR10": "I make people feel at ease.",
    "CSN1": "I am always prepared.",
    "CSN2": "I leave my belongings around.",
    "CSN3": "I pay attention to details.",
    "CSN4": "I make a mess of things.",
    "CSN5": "I get chores done right away.",
    "CSN6": "I often forget to put things back in their proper place.",
    "CSN7": "I like order.",
    "CSN8": "I shirk my duties.",
    "CSN9": "I follow a schedule.",
    "CSN10": "I am exacting in my work.",
    "OPN1": "I have a rich vocabulary.",
    "OPN2": "I have difficulty understanding abstract ideas.",
    "OPN3": "I have a vivid imagination.",
    "OPN4": "I am not interested in abstract ideas.",
    "OPN5": "I have excellent ideas.",
    "OPN6": "I do not have a good imagination.",
    "OPN7": "I am quick to understand things.",
    "OPN8": "I use difficult words.",
    "OPN9": "I spend time reflecting on things.",
    "OPN10": "I am full of ideas."
}


options_mapping = {
    "Disagree": 1,
    "Slightly Disagree": 2,
    "Neutral": 3,
    "Slightly Agree": 4,
    "Agree": 5
}

# Initialize a dictionary to store user responses
user_responses = {}

# Loop through the questions and generate the form elements with radio buttons
with st.form("questions_form"):
    st.subheader(":blue[Answer the following questions to predict your personality]")
    i=1
    for key, question in questions.items():
        user_response = st.radio(f"{i}  {question}", list(options_mapping.keys()))
        i+=1
        st.divider()
        numerical_response = options_mapping[user_response]
        user_responses[key] = numerical_response
    
    submitted = st.form_submit_button("Submit", use_container_width=True)
    if submitted:
        df = pd.DataFrame([user_responses])
        
        st.text("Your response:")
        st.dataframe(df)
        
        st.balloons()
        st.write("Thank you!")

        # Make predictions using the loaded model
        user_personality = loaded_model.predict(df)

        # Define a mapping of cluster numbers to personality types
        personality_types = {
            0: "Extraversion (Outgoing/Energetic)",
            1: "Neuroticism (Sensitive/Nervous)",
            2: "Agreeableness (Friendly/Compassionate)",
            3: "Conscientiousness (Efficient/Organized)",
            4: "Openness to Experience (Inventive/Curious)"
        }

        st.markdown("### My Personality Type: ", unsafe_allow_html=True)
        st.markdown(f"#### {personality_types[int(user_personality)]}")
