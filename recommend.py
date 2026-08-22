import json

import streamlit as st
import streamlit.components.v1 as components


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
    },

    {
        "name": "ABC Education",
        "subjects": [
            "maths",
            "science",
            "english",
            "history",
            "geography",
            "economics",
            "engineering",
            "languages",
            "computer science"
        ],
        "levels": ["beginner", "intermediate"],
        "styles": ["reading", "video", "interactive", "visual", "practice"],
        "price": "free",
        "max_cost": 0,
        "payment": "free",
        "membership_required": False,
        "digital_difficulty": "easy",
        "devices": ["computer", "phone", "tablet"],
        "guidance": "medium",
        "course_length": ["short", "medium"],
        "certificate": False,
        "url": "https://www.abc.net.au/education"
    }
]


# ============================================================
# LOCALISATION METADATA AND DETECTION
# ============================================================
#
# Browser/device locale and timezone are used only as coarse defaults.
# The app does NOT request GPS location, use IP geolocation, or infer gender.
# Gender is not reliably exposed by browsers/devices and should not be guessed.
#
# `region_relevance` means a resource is especially aligned to that region.
# An empty list means the resource is broadly/global rather than region-specific.
#
# Language metadata is intentionally conservative: only languages we are
# reasonably confident the platform supports are listed.
# ============================================================

LANGUAGE_NAMES = {
    "ar": "Arabic",
    "az": "Azerbaijani",
    "bn": "Bengali",
    "bg": "Bulgarian",
    "cs": "Czech",
    "da": "Danish",
    "nl": "Dutch",
    "en": "English",
    "fr": "French",
    "de": "German",
    "el": "Greek",
    "hi": "Hindi",
    "hu": "Hungarian",
    "id": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "mr": "Marathi",
    "nb": "Norwegian",
    "pa": "Punjabi",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "sr": "Serbian",
    "es": "Spanish",
    "sv": "Swedish",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zh": "Chinese",
}

REGION_NAMES = {
    "AU": "Australia",
    "BR": "Brazil",
    "CA": "Canada",
    "CN": "China",
    "DE": "Germany",
    "ES": "Spain",
    "FR": "France",
    "GB": "United Kingdom",
    "IE": "Ireland",
    "IN": "India",
    "IT": "Italy",
    "JP": "Japan",
    "KR": "South Korea",
    "MX": "Mexico",
    "MY": "Malaysia",
    "NZ": "New Zealand",
    "SG": "Singapore",
    "US": "United States",
}

LOCALISATION_METADATA = {
    "Khan Academy": {
        "languages": [
            "ar", "az", "bn", "bg", "cs", "da", "nl", "en", "fr", "de",
            "hi", "hu", "id", "it", "ja", "ko", "mr", "nb", "pa", "pl",
            "pt", "ro", "ru", "sr", "es", "sv", "ta", "te", "th", "tr",
            "uk", "ur", "vi", "zh"
        ],
        "region_relevance": [],
    },
    "Scratch": {
        "languages": [
            "ar", "bg", "cs", "da", "nl", "en", "fr", "de", "el", "hi",
            "hu", "id", "it", "ja", "ko", "nb", "pl", "pt", "ro", "ru",
            "es", "sv", "tr", "uk", "zh"
        ],
        "region_relevance": [],
    },
    "Duolingo": {
        "languages": [
            "ar", "cs", "nl", "en", "fr", "de", "hi", "id", "it", "ja",
            "ko", "pl", "pt", "ru", "es", "sv", "tr", "uk", "vi", "zh"
        ],
        "region_relevance": [],
    },
    "BBC Bitesize": {
        "languages": ["en"],
        "region_relevance": ["GB"],
    },
    "OpenLearn": {
        "languages": ["en"],
        "region_relevance": [],
    },
    "CK-12": {
        "languages": ["en"],
        "region_relevance": ["US"],
    },
    "CS50": {
        "languages": ["en"],
        "region_relevance": [],
    },
    "ABC Education": {
        "languages": ["en"],
        "region_relevance": ["AU"],
    },
}

# Add conservative defaults to every database record.
for website in websites:
    metadata = LOCALISATION_METADATA.get(website["name"], {})
    website["languages"] = metadata.get("languages", ["en"])
    website["region_relevance"] = metadata.get("region_relevance", [])


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


def language_label(code):
    return LANGUAGE_NAMES.get(code, code.upper() if code else "Unknown")


def region_label(code):
    return REGION_NAMES.get(code, code if code else "Unknown")


# ============================================================
# ACCESSIBILITY HELPERS AND CONTROLS
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
# FIND COURSES BUTTON
# ============================================================

find_button = st.button(
    ("🔎 Find learning resources"),
    type="primary",
)

if find_button:

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
        # LOCALISATION FILTERS AND MATCH BONUSES
        # ====================================================

        website_languages = website.get("languages", ["en"])
        region_relevance = website.get("region_relevance", [])
        supports_selected_language = selected_language in website_languages
        matches_selected_region = (
            selected_region is not None
            and selected_region in region_relevance
        )

        # Strict language mode filters out sites that are not tagged as
        # supporting the detected/selected browser language.
        if (
            localisation_mode
            and language_filter_mode == "Only show resources supporting my language"
            and not supports_selected_language
        ):
            continue

        # A region-specific resource from a different region is filtered in
        # strict regional mode. Global resources have an empty relevance list
        # and remain eligible.
        if (
            localisation_mode
            and region_filter_mode == "Local + global resources only"
            and region_relevance
            and selected_region not in region_relevance
        ):
            continue

        if localisation_mode and language_filter_mode == "Prioritise my language":
            if supports_selected_language:
                score += 4
                if selected_language != "en" or len(website_languages) > 1:
                    reasons.append(
                        f"Supports {language_label(selected_language)}"
                    )
            else:
                score -= 2

        if localisation_mode and region_filter_mode == "Prioritise local resources":
            if matches_selected_region:
                score += 6
                reasons.append(
                    f"Especially relevant to learners in {region_label(selected_region)}"
                )
            elif not region_relevance:
                # Global resources remain useful but receive a smaller bonus
                # than genuinely local resources.
                score += 1


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

