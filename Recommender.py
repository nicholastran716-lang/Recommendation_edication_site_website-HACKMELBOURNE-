"""Matching and filtering logic for the Education Website Recommender."""

from websites import language_label, region_label


def recommend_websites(
    websites,
    subject,
    level,
    learning_style,
    guidance,
    budget,
    payment_preference,
    digital_confidence,
    device,
    course_length,
    certificate_preference,
    user_prompt="",
    localisation_mode=True,
    selected_language="en",
    selected_region=None,
    language_filter_mode="Prioritise my language",
    region_filter_mode="Prioritise local resources",
):
    """Score and sort educational websites using the user's preferences.

    Returns:
        list[dict]: Each result contains the website, its score, and reasons.
    """
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

    return recommendations
