import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Course Recommender",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 Course Recommendation System")
st.write(
    "Select your interests and preferences to receive personalised "
    "course recommendations."
)

# Example course database
courses = [
    {
        "name": "Python Fundamentals",
        "interests": {"Programming", "Data Science"},
        "level": "Beginner",
        "hours": 4,
        "description": "Learn Python syntax, functions, loops, and data structures.",
    },
    {
        "name": "Web Development",
        "interests": {"Programming", "Web Development"},
        "level": "Beginner",
        "hours": 6,
        "description": "Build interactive websites and web applications.",
    },
    {
        "name": "Data Visualisation",
        "interests": {"Data Science", "Design"},
        "level": "Intermediate",
        "hours": 5,
        "description": "Communicate information through meaningful charts.",
    },
    {
        "name": "Machine Learning",
        "interests": {"Programming", "Data Science", "Artificial Intelligence"},
        "level": "Intermediate",
        "hours": 8,
        "description": "Create models that identify patterns and make predictions.",
    },
    {
        "name": "Embedded Systems",
        "interests": {"Programming", "Electronics", "Engineering"},
        "level": "Intermediate",
        "hours": 7,
        "description": "Program microcontrollers and connect software to hardware.",
    },
    {
        "name": "Circuit Analysis",
        "interests": {"Electronics", "Engineering"},
        "level": "Beginner",
        "hours": 5,
        "description": "Learn voltage, current, KCL, KVL, and network analysis.",
    },
]

# Sidebar inputs
st.sidebar.header("Your preferences")

name = st.sidebar.text_input("Your name")

selected_interests = st.sidebar.multiselect(
    "What are you interested in?",
    [
        "Programming",
        "Data Science",
        "Web Development",
        "Artificial Intelligence",
        "Electronics",
        "Engineering",
        "Design",
    ],
)

selected_level = st.sidebar.selectbox(
    "Current level",
    ["Beginner", "Intermediate"],
)

available_hours = st.sidebar.slider(
    "Available study hours per week",
    min_value=1,
    max_value=15,
    value=6,
)

# Forms prevent immediate reruns after every input change.
with st.form("recommendation_form"):
    goal = st.text_area(
        "What would you like to learn or build?",
        placeholder="For example: I want to build an engineering dashboard.",
    )

    submitted = st.form_submit_button("Find courses")

if submitted:
    if not selected_interests:
        st.warning("Please select at least one interest.")
    else:
        recommendations = []

        for course in courses:
            matching_interests = len(
                course["interests"].intersection(selected_interests)
            )

            score = matching_interests * 3

            if course["level"] == selected_level:
                score += 2

            if course["hours"] <= available_hours:
                score += 1

            if score > 0:
                recommendations.append(
                    {
                        **course,
                        "score": score,
                        "matches": matching_interests,
                    }
                )

        recommendations.sort(
            key=lambda course: course["score"],
            reverse=True,
        )

        if name:
            st.success(f"Here are your recommendations, {name}!")
        else:
            st.success("Here are your recommendations!")

        top_courses = recommendations[:3]

        columns = st.columns(len(top_courses))

        for column, course in zip(columns, top_courses):
            with column:
                st.subheader(course["name"])
                st.write(course["description"])
                st.write(f"**Level:** {course['level']}")
                st.write(f"**Weekly workload:** {course['hours']} hours")
                st.metric("Recommendation score", course["score"])

        st.divider()

        chart_data = pd.DataFrame(
            {
                "Course": [course["name"] for course in recommendations],
                "Score": [course["score"] for course in recommendations],
            }
        ).set_index("Course")

        st.subheader("Recommendation comparison")
        st.bar_chart(chart_data)

        if goal:
            st.subheader("Your stated goal")
            st.info(goal)

st.divider()

# File uploader demonstration
st.header("Upload existing course data")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"],
)

if uploaded_file is not None:
    uploaded_data = pd.read_csv(uploaded_file)

    st.subheader("Uploaded data")
    st.dataframe(uploaded_data, use_container_width=True)

    st.write(f"Number of records: {len(uploaded_data)}")

# Session state demonstration
st.divider()
st.header("Session-state demonstration")

if "visits" not in st.session_state:
    st.session_state.visits = 0

if st.button("Increase counter"):
    st.session_state.visits += 1

st.write(f"Counter: {st.session_state.visits}")