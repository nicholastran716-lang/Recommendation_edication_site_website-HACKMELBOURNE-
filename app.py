"""Streamlit interface for the Education Website Recommender."""

import json

import streamlit as st
import streamlit.components.v1 as components

from Recommender import recommend_websites
from websites import (
    LANGUAGE_NAMES,
    REGION_NAMES,
    language_label,
    region_label,
    websites,
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Education Website Recommender",
    page_icon="🎓",
    layout="centered"
)


# ============================================================
# BROWSER LOCALISATION HELPERS
# ============================================================

def get_browser_context():
    """Read coarse browser locale/timezone with fallbacks for older Streamlit versions."""
    locale = None
    timezone = None

    try:
        locale = getattr(st.context, "locale", None)
    except Exception:
        locale = None

    try:
        timezone = getattr(st.context, "timezone", None)
    except Exception:
        timezone = None

    # Older Streamlit versions may not expose st.context.locale.
    if not locale:
        try:
            accept_language = st.context.headers.get("Accept-Language", "")
            if accept_language:
                locale = accept_language.split(",")[0].strip()
        except Exception:
            pass

    return locale, timezone


def language_from_locale(locale):
    if not locale:
        return "en"
    return locale.replace("_", "-").split("-")[0].lower()


def region_from_locale(locale):
    if not locale:
        return None

    parts = locale.replace("_", "-").split("-")
    for part in reversed(parts[1:]):
        if len(part) == 2 and part.isalpha():
            return part.upper()
    return None


def region_from_timezone(timezone):
    """Small fallback map for common browser timezones when locale has no region."""
    if not timezone:
        return None

    exact = {
        "Europe/London": "GB",
        "Europe/Dublin": "IE",
        "Pacific/Auckland": "NZ",
        "Asia/Kolkata": "IN",
        "Asia/Tokyo": "JP",
        "Asia/Seoul": "KR",
        "Asia/Shanghai": "CN",
        "Asia/Singapore": "SG",
        "Asia/Kuala_Lumpur": "MY",
        "America/Toronto": "CA",
        "America/Vancouver": "CA",
        "America/New_York": "US",
        "America/Chicago": "US",
        "America/Denver": "US",
        "America/Los_Angeles": "US",
        "America/Mexico_City": "MX",
        "America/Sao_Paulo": "BR",
        "Europe/Paris": "FR",
        "Europe/Berlin": "DE",
        "Europe/Madrid": "ES",
        "Europe/Rome": "IT",
    }

    if timezone in exact:
        return exact[timezone]
    if timezone.startswith("Australia/"):
        return "AU"
    return None

# ============================================================
# ACCESSIBILITY HELPERS AND USER INTERFACE
# ============================================================

def apply_accessibility_css():
    """Apply large-text and high-contrast presentation settings."""
    css_rules = []

    if large_text:
        css_rules.append(
            """
            html, body, .stApp, .stApp p, .stApp li,
            .stApp label, .stApp input, .stApp textarea,
            .stApp button, .stApp [data-baseweb] {
                font-size: 1.15rem !important;
                line-height: 1.6 !important;
            }

            .stApp h1 { font-size: 2.7rem !important; line-height: 1.2 !important; }
            .stApp h2 { font-size: 2.15rem !important; line-height: 1.25 !important; }
            .stApp h3 { font-size: 1.65rem !important; line-height: 1.3 !important; }

            .stApp [data-testid="stWidgetLabel"] p,
            .stApp [data-testid="stMarkdownContainer"] p {
                font-size: 1.15rem !important;
            }
            """
        )

    if high_contrast:
        css_rules.append(
            """
            .stApp,
            [data-testid="stAppViewContainer"],
            [data-testid="stHeader"],
            [data-testid="stSidebar"] > div:first-child {
                background: #000000 !important;
                color: #FFFFFF !important;
            }

            .stApp h1, .stApp h2, .stApp h3,
            .stApp p, .stApp li, .stApp label,
            .stApp span, .stApp small,
            [data-testid="stSidebar"] * {
                color: #FFFFFF !important;
            }

            .stApp a {
                color: #FFFF00 !important;
                text-decoration: underline !important;
            }

            .stApp input,
            .stApp textarea,
            .stApp [data-baseweb="select"] > div,
            .stApp [data-baseweb="base-input"] > div {
                background: #000000 !important;
                color: #FFFFFF !important;
                border: 2px solid #FFFFFF !important;
            }

            .stApp button,
            .stApp [data-testid="stLinkButton"] a {
                border: 2px solid #FFFFFF !important;
                font-weight: 700 !important;
            }

            .stApp button:focus,
            .stApp a:focus,
            .stApp input:focus,
            .stApp textarea:focus,
            .stApp [tabindex]:focus {
                outline: 4px solid #FFFF00 !important;
                outline-offset: 3px !important;
            }

            [data-baseweb="popover"],
            [data-baseweb="menu"],
            [role="listbox"] {
                background: #000000 !important;
                color: #FFFFFF !important;
            }
            """
        )

    if css_rules:
        st.markdown(
            f"<style>{''.join(css_rules)}</style>",
            unsafe_allow_html=True,
        )


def speak_text(text_to_read):
    """Render browser text-to-speech controls using the Web Speech API."""
    text_json = json.dumps(text_to_read)

    if high_contrast:
        button_style = (
            "background:#000;color:#fff;border:2px solid #fff;"
            "padding:10px 14px;font-size:16px;font-weight:700;"
        )
    else:
        button_style = (
            "background:#fff;color:#111;border:1px solid #777;"
            "padding:10px 14px;font-size:16px;font-weight:600;"
        )

    components.html(
        f"""
        <div style="display:flex;gap:10px;align-items:center;font-family:Arial,sans-serif;">
            <button id="readButton" aria-label="Read this section aloud" style="{button_style}">
                🔊 Read aloud
            </button>
            <button id="stopButton" aria-label="Stop reading" style="{button_style}">
                ⏹ Stop
            </button>
        </div>

        <script>
            const textToRead = {text_json};
            const readButton = document.getElementById("readButton");
            const stopButton = document.getElementById("stopButton");

            readButton.addEventListener("click", () => {{
                window.speechSynthesis.cancel();
                const speech = new SpeechSynthesisUtterance(textToRead);
                speech.lang = "en-AU";
                speech.rate = 0.9;
                window.speechSynthesis.speak(speech);
            }});

            stopButton.addEventListener("click", () => {{
                window.speechSynthesis.cancel();
            }});
        </script>
        """,
        height=62,
    )


# Accessibility settings are placed first so they affect the whole page.
st.sidebar.header("♿ Accessibility")

accessibility_mode = st.sidebar.toggle(
    "Accessibility mode",
    help="Turn on display options that can make this page easier to use.",
)

if accessibility_mode:
    large_text = st.sidebar.checkbox("Larger text", value=True)
    high_contrast = st.sidebar.checkbox("Higher contrast", value=True)
else:
    large_text = False
    high_contrast = False

tts_mode = st.sidebar.toggle(
    "Text-to-speech",
    help="Shows buttons that can read important parts of the page aloud.",
)

st.sidebar.caption(
    "These settings change how the page is presented. "
    "They do not change how recommendations are scored."
)

apply_accessibility_css()


# ============================================================
# LOCALISATION CONTROLS
# ============================================================

browser_locale, browser_timezone = get_browser_context()
detected_language = language_from_locale(browser_locale)
detected_region = region_from_locale(browser_locale) or region_from_timezone(browser_timezone)

st.sidebar.divider()
st.sidebar.header("🌍 Localisation")

localisation_mode = st.sidebar.toggle(
    "Use localised recommendations",
    value=True,
    help=(
        "Uses your browser language and coarse region to rank resources. "
        "It does not request GPS location or infer gender."
    ),
)

selected_language = detected_language
selected_region = detected_region

if localisation_mode:
    detected_parts = [f"Language: {language_label(detected_language)}"]
    if detected_region:
        detected_parts.append(f"Region: {region_label(detected_region)}")
    if browser_timezone:
        detected_parts.append(f"Timezone: {browser_timezone}")

    st.sidebar.caption(
        "Detected from browser/device settings — " + " · ".join(detected_parts)
    )

    language_filter_mode = st.sidebar.selectbox(
        "Language filtering",
        [
            "Prioritise my language",
            "Only show resources supporting my language",
            "Ignore language",
        ],
        help=(
            "Prioritise adds a ranking bonus. The strict option removes resources "
            "that are not tagged as supporting the detected language. Language "
            "tags are conservative, so strict mode can hide partial translations."
        ),
    )

    region_filter_mode = st.sidebar.selectbox(
        "Regional filtering",
        [
            "Prioritise local resources",
            "Local + global resources only",
            "Ignore region",
        ],
        help=(
            "Region is inferred coarsely from browser locale/timezone. "
            "Global resources are not treated as foreign."
        ),
    )

    override_localisation = st.sidebar.checkbox(
        "Change detected language or region",
        value=False,
    )

    if override_localisation:
        available_languages = sorted(
            {language for site in websites for language in site["languages"]},
            key=language_label,
        )
        selected_language = st.sidebar.selectbox(
            "Language",
            available_languages,
            index=(
                available_languages.index(detected_language)
                if detected_language in available_languages
                else available_languages.index("en")
            ),
            format_func=language_label,
        )

        region_options = [None] + sorted(REGION_NAMES, key=region_label)
        selected_region = st.sidebar.selectbox(
            "Region",
            region_options,
            index=(
                region_options.index(detected_region)
                if detected_region in region_options
                else 0
            ),
            format_func=lambda value: "Global / unknown" if value is None else region_label(value),
        )

    st.sidebar.caption(
        "No gender is inferred. Browsers do not provide a reliable gender setting, "
        "and guessing it could create biased recommendations."
    )
else:
    language_filter_mode = "Ignore language"
    region_filter_mode = "Ignore region"


# ============================================================
# PAGE HEADER
# ============================================================

st.title("🎓 Education Website Recommender")

intro_text = (
    "Tell us what you want to learn and how you prefer to learn it. "
    "We'll compare your preferences with different educational websites "
    "and recommend the ones that may suit you best. If localisation is enabled, "
    "your browser language and coarse region also influence the results."
)

st.write(intro_text)

if tts_mode:
    st.caption("Use these buttons to hear the introduction.")
    speak_text(intro_text)


# ============================================================
# SECTION 1 — SUBJECT AND EXPERIENCE
# ============================================================

st.header(("1. What would you like to learn?"))

subject = st.selectbox(
    ("Choose a subject"),
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
        "Economics",
    ],
    help=("Choose the subject closest to what you want to learn."),
)

level = st.selectbox(
    ("How experienced are you with this subject?"),
    ["Beginner", "Intermediate", "Advanced"],
    help=("Beginner = new to the subject. Intermediate = you know some basics. "
            "Advanced = you already have strong knowledge."),
)


# ============================================================
# SECTION 2 — LEARNING STYLE
# ============================================================

st.header(("2. How do you like learning?"))

learning_style = st.multiselect(
    ("Choose one or more learning styles"),
    [
        "Videos",
        "Reading",
        "Interactive exercises",
        "Projects",
        "Coding exercises",
        "Visual explanations",
        "Games and quizzes",
    ],
    help=("You can choose more than one."),
)

guidance = st.selectbox(
    ("How much guidance would you like?"),
    [
        "A lot of guidance",
        "Some guidance",
        "I prefer learning independently",
    ],
    help=("A lot of guidance means you prefer a clear step-by-step course."),
)


# ============================================================
# SECTION 3 — BUDGET AND MEMBERSHIP
# ============================================================

st.header(("3. Budget"))

budget = st.selectbox(
    ("How much are you willing to spend?"),
    [
        "Free only",
        "Up to $20",
        "Up to $50",
        "Up to $100",
        "Price is not important",
    ],
)

payment_preference = st.selectbox(
    ("What type of payment are you comfortable with?"),
    [
        "Free resources only",
        "I prefer paying once",
        "A membership or subscription is okay",
        "No preference",
    ],
    help=("A subscription usually means paying repeatedly, for example every month."),
)


# ============================================================
# SECTION 4 — DIGITAL COMFORT
# ============================================================

st.header(("4. Technology preferences"))

digital_confidence = st.selectbox(
    ("How comfortable are you using websites and apps?"),
    [
        "Not very comfortable",
        "Somewhat comfortable",
        "Very comfortable",
    ],
    help=("There is no wrong answer. We use this to recommend websites "
            "that may be easier for you to navigate."),
)

device = st.selectbox(
    ("What device will you mainly use?"),
    ["Computer", "Phone", "Tablet"],
)

if digital_confidence == "Not very comfortable":
    st.info(
        ("That's completely fine. We'll give extra preference to websites "
                "with simpler navigation and clearer learning paths.")
    )


# ============================================================
# SECTION 5 — TIME COMMITMENT
# ============================================================

st.header(("5. How much time do you have?"))

weekly_time = st.selectbox(
    ("How much time can you spend learning each week?"),
    [
        "Less than 1 hour",
        "1–3 hours",
        "3–6 hours",
        "More than 6 hours",
    ],
)

course_length = st.selectbox(
    ("What type of learning material would you prefer?"),
    [
        "Quick lessons",
        "Medium-sized course",
        "Long complete course",
        "No preference",
    ],
)


# ============================================================
# SECTION 6 — CERTIFICATES
# ============================================================

st.header(("6. Certificates"))

certificate_preference = st.selectbox(
    ("Would you like a certificate after completing the material?"),
    ["Yes", "No", "I don't mind"],
    help=("Certificates may be useful for resumes, university applications "
            "or employment."),
)


# ============================================================
# SECTION 7 — OPTIONAL DETAILED DESCRIPTION
# ============================================================

st.header(("7. Tell us anything else"))

user_prompt = st.text_area(
    ("Describe what you're looking for in your own words"),
    placeholder=("Example: I have never programmed before. I want to learn Python "
            "with simple videos and projects. I only have about 2 hours per week "
            "and would prefer something free."),
    help=("This section is optional."),
)

# ============================================================
# RUN RECOMMENDATION ENGINE
# ============================================================

find_button = st.button(
    "🔎 Find learning resources",
    type="primary",
)

if find_button:
    recommendations = recommend_websites(
        websites=websites,
        subject=subject,
        level=level,
        learning_style=learning_style,
        guidance=guidance,
        budget=budget,
        payment_preference=payment_preference,
        digital_confidence=digital_confidence,
        device=device,
        course_length=course_length,
        certificate_preference=certificate_preference,
        user_prompt=user_prompt,
        localisation_mode=localisation_mode,
        selected_language=selected_language,
        selected_region=selected_region,
        language_filter_mode=language_filter_mode,
        region_filter_mode=region_filter_mode,
    )

    # ========================================================
    # DISPLAY TOP RECOMMENDATIONS
    # ========================================================

    st.header(("🏆 Your best matches"))

    if localisation_mode:
        localisation_summary = f"Using {language_label(selected_language)}"
        if selected_region:
            localisation_summary += f" and {region_label(selected_region)}"
        st.caption(localisation_summary + " for localisation.")


    # Only display top five results

    top_recommendations = recommendations[:5]

    if not top_recommendations:
        st.warning(
            "No resources matched the current localisation filters. "
            "Try changing Language filtering or Regional filtering in the sidebar."
        )


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
            (f"**Recommendation score:** {score}")
        )

        if localisation_mode:
            supported_names = ", ".join(
                language_label(code) for code in website.get("languages", ["en"])[:6]
            )
            if len(website.get("languages", ["en"])) > 6:
                supported_names += ", …"
            st.write(f"🌐 **Languages:** {supported_names}")

            if website.get("region_relevance"):
                region_names = ", ".join(
                    region_label(code) for code in website["region_relevance"]
                )
                st.write(f"📍 **Region focus:** {region_names}")
            else:
                st.write("📍 **Region focus:** Global")


        # ----------------------------------------------------
        # Price
        # ----------------------------------------------------

        if website["price"] == "free":

            st.write(("💰 **Price:** Free"))

        else:

            st.write(
                ("💰 **Price:** Free and/or paid options")
            )


        # ----------------------------------------------------
        # Membership information
        # ----------------------------------------------------

        if website["membership_required"]:

            st.write(
                ("👤 An account or membership may be required.")
            )


        # ----------------------------------------------------
        # Certificate information
        # ----------------------------------------------------

        if website["certificate"]:

            st.write(
                ("📜 Certificate options may be available.")
            )


        # ----------------------------------------------------
        # Explain recommendation
        # ----------------------------------------------------

        if reasons:

            st.write(("**Why this may suit you:**"))

            # Remove duplicate reasons

            unique_reasons = list(dict.fromkeys(reasons))

            for reason in unique_reasons[:5]:

                st.write(f"✓ {(reason)}")


        # ----------------------------------------------------
        # Link
        # ----------------------------------------------------

        st.link_button(
            f"Visit {website['name']}",
            website["url"]
        )


        st.divider()

    if tts_mode:
        recommendation_speech = [
            ("Here are your best matches.")
        ]

        for position, recommendation in enumerate(top_recommendations, start=1):
            website = recommendation["website"]
            reasons = list(dict.fromkeys(recommendation["reasons"]))

            recommendation_speech.append(
                f"Number {position}: {website['name']}. "
                f"Match score {recommendation['score']}."
            )

            if reasons:
                spoken_reasons = ". ".join(
                    (reason) for reason in reasons[:3]
                )
                recommendation_speech.append(spoken_reasons + ".")

        st.subheader(("🔊 Listen to your recommendations"))
        speak_text(" ".join(recommendation_speech))

