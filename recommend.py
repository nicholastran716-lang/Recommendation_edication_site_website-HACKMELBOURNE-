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


st.title("Education Website Recommender")


# -------------------------
# Basic preferences
# -------------------------

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


# -------------------------
# Specific prompt
# -------------------------

user_prompt = st.text_area(
    "Describe what you're looking for in more detail",
    placeholder=(
        "Example: I want a free beginner computer science course "
        "with lots of projects and videos"
    )
)


# Only generate results when user clicks
if st.button("Find courses"):

    recommendations = []

    subject = subject.lower()
    level = level.lower()
    prompt = user_prompt.lower()

    style_map = {
        "Videos": "video",
        "Reading": "reading",
        "Interactive exercises": "practice",
        "Projects": "projects",
    }

    selected_styles = [
        style_map[style]
        for style in learning_style
    ]


    # -------------------------
    # Score each website
    # -------------------------

    for website in websites:
        score = 0
        reasons = []

        # Subject matching
        if subject in website["subjects"]:
            score += 4
            reasons.append("Matches your subject")

        # Level matching
        if level in website["levels"]:
            score += 3
            reasons.append("Matches your level")

        # Learning style matching
        for style in selected_styles:
            if style in website["styles"]:
                score += 2
                reasons.append(f"Supports {style}")


        # -------------------------
        # Prompt matching
        # -------------------------

        # Subject keywords
        for website_subject in website["subjects"]:
            if website_subject in prompt:
                score += 3
                reasons.append(
                    f"Your prompt mentions {website_subject}"
                )

        # Level keywords
        for website_level in website["levels"]:
            if website_level in prompt:
                score += 2
                reasons.append(
                    f"Suitable for {website_level}"
                )

        # Learning style keywords
        for website_style in website["styles"]:
            if website_style in prompt:
                score += 2
                reasons.append(
                    f"Includes {website_style}"
                )

        # Price preference
        if website["price"] in prompt:
            score += 3
            reasons.append(
                f"Matches your {website['price']} price preference"
            )


        recommendations.append({
            "website": website,
            "score": score,
            "reasons": reasons
        })


    # Highest scores first
    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    # -------------------------
    # Display results
    # -------------------------

    st.subheader("Recommended websites")

    for recommendation in recommendations:

        website = recommendation["website"]

        st.markdown(
            f"### [{website['name']}]({website['url']})"
        )

        st.write(
            f"Match score: {recommendation['score']}"
        )

        if recommendation["reasons"]:

            st.write("Why we recommended it:")

            for reason in recommendation["reasons"]:
                st.write(f"- {reason}")

        st.divider()