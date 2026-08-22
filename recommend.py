import streamlit as st


websites = [
    {
        "name": "Khan Academy",
        "subjects": ["maths", "science", "economics", "computing"],
        "levels": ["beginner", "intermediate"],
        "styles": ["video", "practice"],
        "price": "free",
        "url": "https://www.khanacademy.org/"
    },

    {
        "name": "Coursera",
        "subjects": ["computer science", "business", "science", "data science"],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["video", "reading", "projects"],
        "price": "mixed",
        "url": "https://www.coursera.org/"
    },

    {
        "name": "edX",
        "subjects": ["computer science", "engineering", "business", "science", "maths"],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["video", "reading", "projects"],
        "price": "mixed",
        "url": "https://www.edx.org/"
    },

    {
        "name": "MIT OpenCourseWare",
        "subjects": ["computer science", "engineering", "maths", "science"],
        "levels": ["intermediate", "advanced"],
        "styles": ["video", "reading", "practice"],
        "price": "free",
        "url": "https://ocw.mit.edu/"
    },

    {
        "name": "freeCodeCamp",
        "subjects": ["computer science", "programming", "web development", "data science"],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "practice", "projects"],
        "price": "free",
        "url": "https://www.freecodecamp.org/"
    },

    {
        "name": "Codecademy",
        "subjects": ["computer science", "programming", "web development", "data science"],
        "levels": ["beginner", "intermediate"],
        "styles": ["practice", "projects", "reading"],
        "price": "mixed",
        "url": "https://www.codecademy.com/"
    },

    {
        "name": "Brilliant",
        "subjects": ["maths", "science", "computer science"],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["interactive", "practice", "visual"],
        "price": "mixed",
        "url": "https://brilliant.org/"
    },

    {
        "name": "W3Schools",
        "subjects": ["programming", "web development", "computer science"],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "practice", "interactive"],
        "price": "free",
        "url": "https://www.w3schools.com/"
    },

    {
        "name": "GeeksforGeeks",
        "subjects": ["computer science", "programming", "algorithms", "data structures"],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["reading", "practice", "coding"],
        "price": "mixed",
        "url": "https://www.geeksforgeeks.org/"
    },

    {
        "name": "LeetCode",
        "subjects": ["programming", "algorithms", "data structures"],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["practice", "coding", "challenges"],
        "price": "mixed",
        "url": "https://leetcode.com/"
    },

    {
        "name": "Duolingo",
        "subjects": ["languages"],
        "levels": ["beginner", "intermediate"],
        "styles": ["interactive", "practice", "gamified"],
        "price": "mixed",
        "url": "https://www.duolingo.com/"
    },

    {
        "name": "BBC Bitesize",
        "subjects": ["maths", "science", "english", "history", "geography"],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "video", "practice"],
        "price": "free",
        "url": "https://www.bbc.co.uk/bitesize"
    },

    {
        "name": "TED-Ed",
        "subjects": ["science", "history", "psychology", "philosophy", "general knowledge"],
        "levels": ["beginner", "intermediate"],
        "styles": ["video", "visual"],
        "price": "free",
        "url": "https://ed.ted.com/"
    },

    {
        "name": "OpenLearn",
        "subjects": ["science", "business", "technology", "psychology", "languages"],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "video", "activities"],
        "price": "free",
        "url": "https://www.open.edu/openlearn/"
    },

    {
        "name": "Quizlet",
        "subjects": ["general", "languages", "science", "maths"],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["flashcards", "practice", "gamified"],
        "price": "mixed",
        "url": "https://quizlet.com/"
    },

    {
        "name": "CK-12",
        "subjects": ["maths", "science"],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "practice", "interactive"],
        "price": "free",
        "url": "https://www.ck12.org/"
    },

    {
        "name": "Scratch",
        "subjects": ["programming", "computer science"],
        "levels": ["beginner"],
        "styles": ["interactive", "projects", "visual", "gamified"],
        "price": "free",
        "url": "https://scratch.mit.edu/"
    },

    {
        "name": "The Odin Project",
        "subjects": ["programming", "web development", "computer science"],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "projects", "coding"],
        "price": "free",
        "url": "https://www.theodinproject.com/"
    },

    {
        "name": "CS50",
        "subjects": ["computer science", "programming"],
        "levels": ["beginner", "intermediate"],
        "styles": ["video", "practice", "projects"],
        "price": "free",
        "url": "https://cs50.harvard.edu/"
    },

    {
        "name": "Math is Fun",
        "subjects": ["maths"],
        "levels": ["beginner", "intermediate"],
        "styles": ["visual", "reading", "practice"],
        "price": "free",
        "url": "https://www.mathsisfun.com/"
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