import streamlit as st


websites = [
    {
        "name": "Khan Academy",
        "subjects": ["maths", "science"],
        "levels": ["beginner", "intermediate"],
        "styles": ["video", "practice"],
        "price": "free",
        "url": "https://www.khanacademy.org/"
    },

    {
        "name": "Coursera",
        "subjects": ["computer science", "business", "science"],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["video", "reading", "projects"],
        "price": "mixed",
        "url": "https://www.coursera.org/"
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
subject = subject.lower()
level = level.lower()
style_map = {
    "Videos": "video",
    "Reading": "reading",
    "Interactive exercises": "practice",
    "Projects": "projects",
}
selected_styles = [style_map[style] for style in learning_style]

for website in websites:
    score = 0

    if subject in website["subjects"]:
        score += 4

    if level in website["levels"]:
        score += 3

    score += sum(2 for style in selected_styles if style in website["styles"])
    recommendations.append({"website": website, "score": score})

recommendations.sort(
    key=lambda x: x["score"],
    reverse=True
)

st.subheader("Recommended websites")
for recommendation in recommendations:
    website = recommendation["website"]
    st.markdown(
        f"[{website['name']}]({website['url']}) - score: {recommendation['score']}"
    )
    

