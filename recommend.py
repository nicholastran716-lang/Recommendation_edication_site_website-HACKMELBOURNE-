import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Education Website Recommender",
    page_icon="🎓",
    layout="centered"
)


# ============================================================
# EDUCATIONAL WEBSITE DATABASE
# ============================================================
#
# Each website contains information that the recommendation
# algorithm can compare against the user's preferences.
#
# digital_difficulty:
#   "easy"   = simple interface / easier for new technology users
#   "medium" = moderate amount of navigation or setup
#   "hard"   = potentially more complex for beginners
#
# guidance:
#   "high"   = more structured learning path
#   "medium" = some structure
#   "low"    = mostly self-directed
#
# course_length:
#   "short", "medium", "long"
#
# ============================================================

websites = [

    {
        "name": "Khan Academy",
        "subjects": ["maths", "science", "economics", "computing"],
        "levels": ["beginner", "intermediate"],
        "styles": ["video", "practice"],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "easy",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "high",
        "course_length": ["short", "medium", "long"],
        "certificate": False,
        "url": "https://www.khanacademy.org/"
    },

    {
        "name": "Coursera",
        "subjects": [
            "computer science",
            "business",
            "science",
            "data science"
        ],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["video", "reading", "projects"],
        "price": "mixed",
        "max_cost": 100,
        "payment": "subscription",
        "membership_required": True,
        "digital_difficulty": "medium",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "high",
        "course_length": ["medium", "long"],
        "certificate": True,
        "url": "https://www.coursera.org/"
    },

    {
        "name": "edX",
        "subjects": [
            "computer science",
            "engineering",
            "business",
            "science",
            "maths"
        ],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["video", "reading", "projects"],
        "price": "mixed",
        "max_cost": 100,
        "payment": "mixed",
        "membership_required": False,
        "digital_difficulty": "medium",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "high",
        "course_length": ["medium", "long"],
        "certificate": True,
        "url": "https://www.edx.org/"
    },

    {
        "name": "MIT OpenCourseWare",
        "subjects": [
            "computer science",
            "engineering",
            "maths",
            "science"
        ],
        "levels": ["intermediate", "advanced"],
        "styles": ["video", "reading", "practice"],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "medium",
        "devices": ["computer", "tablet"],
        "guidance": "low",
        "course_length": ["medium", "long"],
        "certificate": False,
        "url": "https://ocw.mit.edu/"
    },

    {
        "name": "freeCodeCamp",
        "subjects": [
            "computer science",
            "programming",
            "web development",
            "data science"
        ],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "practice", "projects", "coding"],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "medium",
        "devices": ["computer"],
        "guidance": "high",
        "course_length": ["medium", "long"],
        "certificate": True,
        "url": "https://www.freecodecamp.org/"
    },

    {
        "name": "Codecademy",
        "subjects": [
            "computer science",
            "programming",
            "web development",
            "data science"
        ],
        "levels": ["beginner", "intermediate"],
        "styles": ["practice", "projects", "reading", "interactive"],
        "price": "mixed",
        "max_cost": 50,
        "payment": "subscription",
        "membership_required": True,
        "digital_difficulty": "easy",
        "devices": ["computer", "tablet"],
        "guidance": "high",
        "course_length": ["short", "medium"],
        "certificate": True,
        "url": "https://www.codecademy.com/"
    },

    {
        "name": "Brilliant",
        "subjects": ["maths", "science", "computer science"],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["interactive", "practice", "visual"],
        "price": "mixed",
        "max_cost": 50,
        "payment": "subscription",
        "membership_required": True,
        "digital_difficulty": "easy",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "high",
        "course_length": ["short", "medium"],
        "certificate": False,
        "url": "https://brilliant.org/"
    },

    {
        "name": "W3Schools",
        "subjects": [
            "programming",
            "web development",
            "computer science"
        ],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "practice", "interactive", "coding"],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "easy",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "medium",
        "course_length": ["short", "medium"],
        "certificate": True,
        "url": "https://www.w3schools.com/"
    },

    {
        "name": "GeeksforGeeks",
        "subjects": [
            "computer science",
            "programming",
            "algorithms",
            "data structures"
        ],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["reading", "practice", "coding"],
        "price": "mixed",
        "max_cost": 50,
        "payment": "mixed",
        "membership_required": False,
        "digital_difficulty": "medium",
        "devices": ["computer", "phone"],
        "guidance": "medium",
        "course_length": ["short", "medium"],
        "certificate": True,
        "url": "https://www.geeksforgeeks.org/"
    },

    {
        "name": "LeetCode",
        "subjects": [
            "programming",
            "algorithms",
            "data structures"
        ],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["practice", "coding", "challenges"],
        "price": "mixed",
        "max_cost": 50,
        "payment": "subscription",
        "membership_required": False,
        "digital_difficulty": "medium",
        "devices": ["computer"],
        "guidance": "low",
        "course_length": ["short", "medium"],
        "certificate": False,
        "url": "https://leetcode.com/"
    },

    {
        "name": "Duolingo",
        "subjects": ["languages"],
        "levels": ["beginner", "intermediate"],
        "styles": ["interactive", "practice", "gamified"],
        "price": "mixed",
        "max_cost": 20,
        "payment": "subscription",
        "membership_required": False,
        "digital_difficulty": "easy",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "high",
        "course_length": ["short", "medium", "long"],
        "certificate": False,
        "url": "https://www.duolingo.com/"
    },

    {
        "name": "BBC Bitesize",
        "subjects": [
            "maths",
            "science",
            "english",
            "history",
            "geography"
        ],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "video", "practice"],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "easy",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "high",
        "course_length": ["short", "medium"],
        "certificate": False,
        "url": "https://www.bbc.co.uk/bitesize"
    },

    {
        "name": "TED-Ed",
        "subjects": [
            "science",
            "history",
            "psychology",
            "philosophy",
            "general knowledge"
        ],
        "levels": ["beginner", "intermediate"],
        "styles": ["video", "visual"],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "easy",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "low",
        "course_length": ["short"],
        "certificate": False,
        "url": "https://ed.ted.com/"
    },

    {
        "name": "OpenLearn",
        "subjects": [
            "science",
            "business",
            "technology",
            "psychology",
            "languages"
        ],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "video", "activities"],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "easy",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "high",
        "course_length": ["short", "medium"],
        "certificate": True,
        "url": "https://www.open.edu/openlearn/"
    },

    {
        "name": "Quizlet",
        "subjects": ["general", "languages", "science", "maths"],
        "levels": ["beginner", "intermediate", "advanced"],
        "styles": ["flashcards", "practice", "gamified"],
        "price": "mixed",
        "max_cost": 20,
        "payment": "subscription",
        "membership_required": False,
        "digital_difficulty": "easy",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "medium",
        "course_length": ["short"],
        "certificate": False,
        "url": "https://quizlet.com/"
    },

    {
        "name": "CK-12",
        "subjects": ["maths", "science"],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "practice", "interactive"],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "easy",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "high",
        "course_length": ["short", "medium"],
        "certificate": False,
        "url": "https://www.ck12.org/"
    },

    {
        "name": "Scratch",
        "subjects": ["programming", "computer science"],
        "levels": ["beginner"],
        "styles": [
            "interactive",
            "projects",
            "visual",
            "gamified"
        ],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "easy",
        "devices": ["computer", "tablet"],
        "guidance": "high",
        "course_length": ["short", "medium"],
        "certificate": False,
        "url": "https://scratch.mit.edu/"
    },

    {
        "name": "The Odin Project",
        "subjects": [
            "programming",
            "web development",
            "computer science"
        ],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "projects", "coding"],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "medium",
        "devices": ["computer"],
        "guidance": "medium",
        "course_length": ["long"],
        "certificate": False,
        "url": "https://www.theodinproject.com/"
    },

    {
        "name": "CS50",
        "subjects": ["computer science", "programming"],
        "levels": ["beginner", "intermediate"],
        "styles": ["video", "practice", "projects", "coding"],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "medium",
        "devices": ["computer"],
        "guidance": "high",
        "course_length": ["medium", "long"],
        "certificate": True,
        "url": "https://cs50.harvard.edu/"
    },

    {
        "name": "Math is Fun",
        "subjects": ["maths"],
        "levels": ["beginner", "intermediate"],
        "styles": ["visual", "reading", "practice"],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "easy",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "high",
        "course_length": ["short"],
        "certificate": False,
        "url": "https://www.mathsisfun.com/"
    }
]


# ============================================================
# PAGE HEADER
# ============================================================

st.title("🎓 Education Website Recommender")

st.write(
    """
    Tell us what you want to learn and how you prefer to learn it.

    We'll compare your preferences with different educational websites
    and recommend the ones that may suit you best.
    """
)


# ============================================================
# SECTION 1 — SUBJECT AND EXPERIENCE
# ============================================================

st.header("1. What would you like to learn?")


subject = st.selectbox(
    "Choose a subject",
    [
        "Maths",
        "Science",
        "Computer Science",
        "Programming",
        "Web Development",
        "Data Science",
        "Business",
        "Engineering",
        "Languages",
        "English",
        "History",
        "Geography",
        "Psychology",
        "Economics"
    ],
    help="Choose the subject closest to what you want to learn."
)


level = st.selectbox(
    "How experienced are you with this subject?",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ],
    help=(
        "Beginner = new to the subject. "
        "Intermediate = you know some basics. "
        "Advanced = you already have strong knowledge."
    )
)


# ============================================================
# SECTION 2 — LEARNING STYLE
# ============================================================

st.header("2. How do you like learning?")


learning_style = st.multiselect(
    "Choose one or more learning styles",
    [
        "Videos",
        "Reading",
        "Interactive exercises",
        "Projects",
        "Coding exercises",
        "Visual explanations",
        "Games and quizzes"
    ],
    help="You can choose more than one."
)


guidance = st.selectbox(
    "How much guidance would you like?",
    [
        "A lot of guidance",
        "Some guidance",
        "I prefer learning independently"
    ],
    help=(
        "A lot of guidance means you prefer a clear step-by-step course."
    )
)


# ============================================================
# SECTION 3 — BUDGET AND MEMBERSHIP
# ============================================================

st.header("3. Budget")


budget = st.selectbox(
    "How much are you willing to spend?",
    [
        "Free only",
        "Up to $20",
        "Up to $50",
        "Up to $100",
        "Price is not important"
    ]
)


payment_preference = st.selectbox(
    "What type of payment are you comfortable with?",
    [
        "Free resources only",
        "I prefer paying once",
        "A membership or subscription is okay",
        "No preference"
    ],
    help=(
        "A subscription usually means paying repeatedly, "
        "for example every month."
    )
)


# ============================================================
# SECTION 4 — DIGITAL COMFORT
# ============================================================

st.header("4. Technology preferences")


digital_confidence = st.selectbox(
    "How comfortable are you using websites and apps?",
    [
        "Not very comfortable",
        "Somewhat comfortable",
        "Very comfortable"
    ],
    help=(
        "There is no wrong answer. We use this to recommend websites "
        "that may be easier for you to navigate."
    )
)


device = st.selectbox(
    "What device will you mainly use?",
    [
        "Computer",
        "Phone",
        "Tablet"
    ]
)


# Give extra reassurance to less digitally confident users

if digital_confidence == "Not very comfortable":
    st.info(
        "That's completely fine. We'll give extra preference to websites "
        "with simpler navigation and clearer learning paths."
    )


# ============================================================
# SECTION 5 — TIME COMMITMENT
# ============================================================

st.header("5. How much time do you have?")


weekly_time = st.selectbox(
    "How much time can you spend learning each week?",
    [
        "Less than 1 hour",
        "1–3 hours",
        "3–6 hours",
        "More than 6 hours"
    ]
)


course_length = st.selectbox(
    "What type of learning material would you prefer?",
    [
        "Quick lessons",
        "Medium-sized course",
        "Long complete course",
        "No preference"
    ]
)


# ============================================================
# SECTION 6 — CERTIFICATES
# ============================================================

st.header("6. Certificates")


certificate_preference = st.selectbox(
    "Would you like a certificate after completing the material?",
    [
        "Yes",
        "No",
        "I don't mind"
    ],
    help=(
        "Certificates may be useful for resumes, university applications "
        "or employment."
    )
)


# ============================================================
# SECTION 7 — OPTIONAL DETAILED DESCRIPTION
# ============================================================

st.header("7. Tell us anything else")


user_prompt = st.text_area(
    "Describe what you're looking for in your own words",
    placeholder=(
        "Example: I have never programmed before. "
        "I want to learn Python with simple videos and projects. "
        "I only have about 2 hours per week and would prefer something free."
    ),
    help="This section is optional."
)


# ============================================================
# FIND COURSES BUTTON
# ============================================================

if st.button("🔎 Find learning resources", type="primary"):

    recommendations = []


    # ========================================================
    # CONVERT USER ANSWERS INTO DATABASE VALUES
    # ========================================================

    selected_subject = subject.lower()
    selected_level = level.lower()
    prompt = user_prompt.lower()


    # --------------------------------------------------------
    # Learning style conversion
    # --------------------------------------------------------

    style_map = {

        "Videos": ["video"],

        "Reading": ["reading"],

        "Interactive exercises": [
            "interactive",
            "practice"
        ],

        "Projects": [
            "projects"
        ],

        "Coding exercises": [
            "coding",
            "practice"
        ],

        "Visual explanations": [
            "visual",
            "video"
        ],

        "Games and quizzes": [
            "gamified",
            "flashcards",
            "challenges"
        ]
    }


    selected_styles = []

    for style in learning_style:
        selected_styles.extend(style_map[style])


    # Remove duplicates

    selected_styles = list(set(selected_styles))


    # --------------------------------------------------------
    # Guidance conversion
    # --------------------------------------------------------

    guidance_map = {

        "A lot of guidance": "high",

        "Some guidance": "medium",

        "I prefer learning independently": "low"
    }


    selected_guidance = guidance_map[guidance]


    # --------------------------------------------------------
    # Budget conversion
    # --------------------------------------------------------

    budget_map = {

        "Free only": 0,

        "Up to $20": 20,

        "Up to $50": 50,

        "Up to $100": 100,

        "Price is not important": None
    }


    maximum_budget = budget_map[budget]


    # --------------------------------------------------------
    # Device conversion
    # --------------------------------------------------------

    device_map = {

        "Computer": "computer",

        "Phone": "phone",

        "Tablet": "tablet"
    }


    selected_device = device_map[device]


    # --------------------------------------------------------
    # Course length conversion
    # --------------------------------------------------------

    length_map = {

        "Quick lessons": "short",

        "Medium-sized course": "medium",

        "Long complete course": "long",

        "No preference": None
    }


    selected_length = length_map[course_length]


    # ========================================================
    # SCORE EVERY WEBSITE
    # ========================================================

    for website in websites:

        score = 0

        reasons = []


        # ====================================================
        # SUBJECT MATCH
        # ====================================================
        #
        # Subject is one of the most important criteria.
        #

        if selected_subject in website["subjects"]:

            score += 10

            reasons.append(
                f"Offers {subject} learning material"
            )

        else:

            score -= 5


        # ====================================================
        # EXPERIENCE LEVEL MATCH
        # ====================================================

        if selected_level in website["levels"]:

            score += 6

            reasons.append(
                f"Suitable for a {level.lower()} learner"
            )

        else:

            score -= 3


        # ====================================================
        # LEARNING STYLE MATCH
        # ====================================================

        matched_styles = []

        for style in selected_styles:

            if style in website["styles"]:

                score += 3

                matched_styles.append(style)


        if matched_styles:

            reasons.append(
                "Supports your preferred learning style"
            )


        # ====================================================
        # GUIDANCE MATCH
        # ====================================================

        if website["guidance"] == selected_guidance:

            score += 4

            reasons.append(
                "Provides the amount of guidance you prefer"
            )


        # Adjacent guidance levels are still reasonable

        guidance_number = {
            "low": 1,
            "medium": 2,
            "high": 3
        }

        guidance_difference = abs(
            guidance_number[website["guidance"]]
            -
            guidance_number[selected_guidance]
        )

        if guidance_difference == 1:
            score += 1


        # ====================================================
        # BUDGET MATCH
        # ====================================================

        if maximum_budget is not None:

            if website["max_cost"] <= maximum_budget:

                score += 6

                reasons.append(
                    "Fits within your selected budget"
                )

            else:

                score -= 8


        # ====================================================
        # PAYMENT AND MEMBERSHIP MATCH
        # ====================================================

        if payment_preference == "Free resources only":

            if website["price"] == "free":

                score += 7

                reasons.append(
                    "Completely free learning material is available"
                )

            else:

                score -= 5


        elif payment_preference == "I prefer paying once":

            if website["payment"] != "subscription":

                score += 3

                reasons.append(
                    "Does not depend heavily on a subscription"
                )

            else:

                score -= 2


        elif payment_preference == \
                "A membership or subscription is okay":

            # No penalty for subscription websites

            score += 1


        # ====================================================
        # DIGITAL CONFIDENCE MATCH
        # ====================================================

        if digital_confidence == "Not very comfortable":

            if website["digital_difficulty"] == "easy":

                score += 8

                reasons.append(
                    "Has a relatively simple interface for new technology users"
                )

            elif website["digital_difficulty"] == "medium":

                score += 1

            else:

                score -= 6


        elif digital_confidence == "Somewhat comfortable":

            if website["digital_difficulty"] == "easy":

                score += 4

            elif website["digital_difficulty"] == "medium":

                score += 3


        else:

            # Very comfortable users can reasonably use any interface

            score += 1


        # ====================================================
        # DEVICE MATCH
        # ====================================================

        if selected_device in website["devices"]:

            score += 4

            reasons.append(
                f"Suitable for learning on a {device.lower()}"
            )

        else:

            score -= 4


        # ====================================================
        # COURSE LENGTH MATCH
        # ====================================================

        if selected_length is not None:

            if selected_length in website["course_length"]:

                score += 3

                reasons.append(
                    "Has material matching your preferred course length"
                )


        # ====================================================
        # CERTIFICATE MATCH
        # ====================================================

        if certificate_preference == "Yes":

            if website["certificate"]:

                score += 5

                reasons.append(
                    "Certificate options are available"
                )

            else:

                score -= 3


        # ====================================================
        # FREE-TEXT PROMPT MATCHING
        # ====================================================
        #
        # For now this performs simple keyword matching.
        # Later this section could be replaced with an AI model.
        #

        if prompt:

            # ------------------------------------------------
            # Subject words
            # ------------------------------------------------

            for website_subject in website["subjects"]:

                if website_subject in prompt:

                    score += 3


            # ------------------------------------------------
            # Level words
            # ------------------------------------------------

            for website_level in website["levels"]:

                if website_level in prompt:

                    score += 2


            # ------------------------------------------------
            # Learning style words
            # ------------------------------------------------

            for website_style in website["styles"]:

                if website_style in prompt:

                    score += 2


            # ------------------------------------------------
            # Common natural language words
            # ------------------------------------------------

            if "free" in prompt and website["price"] == "free":

                score += 5


            if (
                "easy to use" in prompt
                or "simple website" in prompt
                or "bad with technology" in prompt
                or "not good with technology" in prompt
            ):

                if website["digital_difficulty"] == "easy":

                    score += 5


            if (
                "certificate" in prompt
                and website["certificate"]
            ):

                score += 4


            if (
                "phone" in prompt
                and "phone" in website["devices"]
            ):

                score += 3


        # ====================================================
        # SAVE WEBSITE SCORE
        # ====================================================

        recommendations.append({

            "website": website,

            "score": score,

            "reasons": reasons
        })


    # ========================================================
    # SORT FROM BEST TO WORST MATCH
    # ========================================================

    recommendations.sort(
        key=lambda result: result["score"],
        reverse=True
    )


    # ========================================================
    # DISPLAY TOP RECOMMENDATIONS
    # ========================================================

    st.header("🏆 Your best matches")


    # Only display top five results

    top_recommendations = recommendations[:5]


    for position, recommendation in enumerate(
        top_recommendations,
        start=1
    ):

        website = recommendation["website"]

        score = recommendation["score"]

        reasons = recommendation["reasons"]


        # ----------------------------------------------------
        # Website title
        # ----------------------------------------------------

        st.subheader(
            f"{position}. {website['name']}"
        )


        # ----------------------------------------------------
        # Score
        # ----------------------------------------------------

        st.write(
            f"**Recommendation score:** {score}"
        )


        # ----------------------------------------------------
        # Price
        # ----------------------------------------------------

        if website["price"] == "free":

            st.write("💰 **Price:** Free")

        else:

            st.write(
                "💰 **Price:** Free and/or paid options"
            )


        # ----------------------------------------------------
        # Membership information
        # ----------------------------------------------------

        if website["membership_required"]:

            st.write(
                "👤 An account or membership may be required."
            )


        # ----------------------------------------------------
        # Certificate information
        # ----------------------------------------------------

        if website["certificate"]:

            st.write(
                "📜 Certificate options may be available."
            )


        # ----------------------------------------------------
        # Explain recommendation
        # ----------------------------------------------------

        if reasons:

            st.write("**Why this may suit you:**")

            # Remove duplicate reasons

            unique_reasons = list(dict.fromkeys(reasons))

            for reason in unique_reasons[:5]:

                st.write(f"✓ {reason}")


        # ----------------------------------------------------
        # Link
        # ----------------------------------------------------

        st.link_button(
            f"Visit {website['name']}",
            website["url"]
        )


        st.divider()