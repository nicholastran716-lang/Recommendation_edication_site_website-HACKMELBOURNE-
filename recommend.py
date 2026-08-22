import streamlit as st

from recommendation_engine import recommend_websites
from website_data import WEBSITES


st.set_page_config(
    page_title="Education Website Recommender",
    page_icon="🎓",
    layout="centered",
)

st.title("🎓 Education Website Recommender")
st.write(
    "Tell us what you want to learn and how you prefer to learn it. "
    "We'll recommend websites that may suit you best."
)

st.header("1. What would you like to learn?")
subject = st.selectbox(
    "Choose a subject",
    [
        "Maths", "Science", "Computer Science", "Programming",
        "Web Development", "Data Science", "Business", "Engineering",
        "Languages", "English", "History", "Geography", "Psychology",
        "Economics",
    ],
)
level = st.selectbox(
    "How experienced are you with this subject?",
    ["Beginner", "Intermediate", "Advanced"],
)

st.header("2. How do you like learning?")
learning_style = st.multiselect(
    "Choose one or more learning styles",
    [
        "Videos", "Reading", "Interactive exercises", "Projects",
        "Coding exercises", "Visual explanations", "Games and quizzes",
    ],
)
guidance = st.selectbox(
    "How much guidance would you like?",
    [
        "A lot of guidance",
        "Some guidance",
        "I prefer learning independently",
    ],
)

st.header("3. Budget")
budget = st.selectbox(
    "How much are you willing to spend?",
    ["Free only", "Up to $20", "Up to $50", "Up to $100", "Price is not important"],
)
payment_preference = st.selectbox(
    "What type of payment are you comfortable with?",
    [
        "Free resources only",
        "I prefer paying once",
        "A membership or subscription is okay",
        "No preference",
    ],
)

st.header("4. Technology preferences")
digital_confidence = st.selectbox(
    "How comfortable are you using websites and apps?",
    ["Not very comfortable", "Somewhat comfortable", "Very comfortable"],
)
device = st.selectbox("What device will you mainly use?", ["Computer", "Phone", "Tablet"])
if digital_confidence == "Not very comfortable":
    st.info("We'll give extra preference to websites with simpler navigation.")

st.header("5. How much time do you have?")
weekly_time = st.selectbox(
    "How much time can you spend learning each week?",
    ["Less than 1 hour", "1–3 hours", "3–6 hours", "More than 6 hours"],
)
course_length = st.selectbox(
    "What type of learning material would you prefer?",
    ["Quick lessons", "Medium-sized course", "Long complete course", "No preference"],
)

st.header("6. Tell us anything else")
user_prompt = st.text_area(
    "Describe what you're looking for in your own words",
    placeholder=(
        "Example: I have never programmed before. I want to learn Python "
        "with simple videos and projects."
    ),
)

if st.button("🔎 Find learning resources", type="primary"):
    recommendations = recommend_websites(
        WEBSITES,
        subject,
        level,
        learning_style,
        guidance,
        budget,
        payment_preference,
        digital_confidence,
        device,
        course_length,
        user_prompt,
    )

    st.header("🏆 Your best matches")
    for position, recommendation in enumerate(recommendations[:5], start=1):
        website = recommendation["website"]
        st.subheader(f"{position}. {website['name']}")
        st.write("💰 **Price:** Free" if website["price"] == "free" else "💰 **Price:** Free and/or paid options")

        if website["membership_required"]:
            st.write("👤 An account or membership may be required.")

        reasons = list(dict.fromkeys(recommendation["reasons"]))
        if reasons:
            st.write("**Why this may suit you:**")
            for reason in reasons[:5]:
                st.write(f"✓ {reason}")

        st.link_button(f"Visit {website['name']}", website["url"])
        st.divider()
