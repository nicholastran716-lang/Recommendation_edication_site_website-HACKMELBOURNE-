import streamlit as st


websites = [
    {
        "name": "Khan Academy",
        "subjects": ["maths", "science"],
        "levels": ["beginner", "intermediate"],
        "styles": ["video", "practice"],
        "price": "free"
    },

    {
        "name": "Coursera",
        "subjects": ["computer science", "business", "science"],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["video", "reading", "projects"],
        "price": "mixed"
    }
]



subject = st.selectbox(
    "What do you want to learn?",
    ["Maths", "Science", "Computer Science", "Languages"]
)

level = st.radio(
    "What level are you?",
    ["Beginner", "Intermediate", "Advanced"]
)

learning_style = st.multiselect(
    "How do you like learning?",
    ["Videos", "Reading", "Interactive exercises", "Projects"]
)

recommendations = []
score = 0

if subject in websites["subjects"]:
    score += 4

if level in websites["levels"]:
    score += 3

for style in learning_style:
    if style in websites["styles"]:
        score += 2



recommendations.sort(
    key=lambda x: x["score"],
    reverse=True
)

