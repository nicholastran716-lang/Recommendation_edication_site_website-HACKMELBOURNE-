"""Educational website data and localisation metadata.

This module stores the website database used by the recommender.
Recommendation scoring belongs in Recommender.py.
"""

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


def language_label(code):
    return LANGUAGE_NAMES.get(code, code.upper() if code else "Unknown")


def region_label(code):
    return REGION_NAMES.get(code, code if code else "Unknown")
