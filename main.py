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
st.subheader(":red[Big 5 personality test]")
st.write("Welcome to the Personality Prediction App! Discover your personality traits and gain insights into your character based on the Big 5 Personality Test.")
st.write("The Big 5 Personality Test, also known as the Five Factor Model, assesses five key dimensions of personality: Openness to Experience, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Each trait offers a unique perspective on your personality, helping you better understand yourself.")

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
    st.subheader(
        ":blue[Answer the following questions to predict your personality]")
    i = 1
    for key, question in questions.items():
        user_response = st.radio(
            f"{i} .  {question}", list(options_mapping.keys()))
        i += 1
        st.divider()
        numerical_response = options_mapping[user_response]
        user_responses[key] = numerical_response

    submitted = st.form_submit_button("Submit", use_container_width=True)
    if submitted:
        df = pd.DataFrame([user_responses])

        st.balloons()
        st.divider()

        # Make predictions using the loaded model
        user_personality = loaded_model.predict(df)
        user_personality = int(user_personality)

        # Define a mapping of cluster numbers to personality types
        personality_types = {
            0: ["Extraversion (Outgoing/Energetic)", "You have a strong sense of curiosity and imagination. You love exploring new ideas and experiences, making you open-minded and creative. You appreciate art, beauty, and different cultures, and you're always eager to try something new."],
            1: ["Neuroticism (Sensitive/Nervous)", "You tend to be emotionally stable and resilient. Stress and worry don't easily get the better of you. You maintain a steady mood and have good control over your emotions, which allows you to navigate life's challenges with composure."],
            2: ["Agreeableness (Friendly/Compassionate)", "Your compassion and cooperative spirit define your personality. You're naturally nurturing and kind, always willing to help and considerate of others. You value harmonious relationships and believe in the power of teamwork and compromise."],
            3: ["Conscientiousness (Efficient/Organized)", "You are highly organized and responsible. Your diligence and reliability shine through in your daily life. You set and achieve goals effectively, and others can always count on you to keep your commitments."],
            4: ["Openness to Experience (Inventive/Curious", "You have a strong sense of curiosity and imagination. You love exploring new ideas and experiences, making you open-minded and creative. You appreciate art, beauty, and different cultures, and you're always eager to try something new."]
        }

        st.markdown("<span style='color:red; font-size:30px;'>Your Personality Type:</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: grey; font-size: 24px;'>{personality_types[user_personality][0]}</span>", unsafe_allow_html=True)
        st.markdown(f"**{personality_types[user_personality][1]}**")

        personality_traits_highs_n_lows = {
            0: {
                "Highs": [
                    "Sociability",
                    "Assertiveness",
                    "Outgoing",
                    "Enthusiasm in social settings."
                ],
                "Lows": [
                    "Introversion",
                    "Shyness",
                    "Reticence in social situations",
                    "Quiet demeanor."
                ]
            },
            1: {
                "Highs": [
                    "Anxiety",
                    "Moodiness",
                    "Emotional reactivity",
                    "Sensitivity to stress."
                ],
                "Lows": [
                    "Emotional stability",
                    "Resilience",
                    "Calmness under pressure",
                    "Even-temperedness."
                ]
            },
            2: {
                "Highs": [
                    "Compassion",
                    "Cooperation",
                    "Politeness",
                    "Empathy",
                    "Nurturing nature."
                ],
                "Lows": [
                    "Competitiveness",
                    "Assertiveness",
                    "Lack of consideration for others",
                    "Conflict-prone."
                ]
            },
            3: {
                "Highs": [
                    "Organization",
                    "Responsibility",
                    "Diligence",
                    "Reliability",
                    "Goal-oriented."
                ],
                "Lows": [
                    "Disorganization",
                    "Lack of responsibility",
                    "Impulsiveness",
                    "Unreliability."
                ]
            },
            4: {
                "Highs": [
                    "Curiosity",
                    "Creativity",
                    "Open-mindedness",
                    "Appreciation of art and novelty."
                ],
                "Lows": [
                    "Resistance to change",
                    "Preference for routine",
                    "Reluctance to explore new ideas."
                ]
            }
        }

        col1, col2 = st.columns(2)

        image_dict={
            0:"extraversion.jpeg",
            1:"neutoticism.jpeg",
            2:"agreeableness.jpeg",
            3:"conscientiousness.jpeg",
            4:"openness.jpeg",
        }

        with col1:
            image=image_dict[user_personality]
            st.image(image, use_column_width=True)


        with col2:
            st.markdown("<p style='font-size:20px;'>Your Highs and Lows : </p>", unsafe_allow_html=True)
            html_table = """
            <table>
            <tr>
                <th>Highs</th>
                <th>Lows</th>
            </tr>
            """

            item=personality_traits_highs_n_lows[user_personality]
            highs=item["Highs"]
            lows=item["Lows"]
            for highs,lows in zip(highs,lows):
                html_table += f"""
            <tr>
                <td>{highs}</td>
                <td>{lows}</td>
            </tr>
            """

            html_table += "</table>"

            st.write(html_table, unsafe_allow_html=True)


        with st.container():
            st.write("Visit https://en.wikipedia.org/wiki/Big_Five_personality_traits to know more!")