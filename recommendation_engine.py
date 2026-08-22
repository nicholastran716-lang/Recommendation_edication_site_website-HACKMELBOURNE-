STYLE_MAP = {
    "Videos": ["video"],
    "Reading": ["reading"],
    "Interactive exercises": ["interactive", "practice"],
    "Projects": ["projects"],
    "Coding exercises": ["coding", "practice"],
    "Visual explanations": ["visual", "video"],
    "Games and quizzes": ["gamified", "flashcards", "challenges"],
}

GUIDANCE_MAP = {
    "A lot of guidance": "high",
    "Some guidance": "medium",
    "I prefer learning independently": "low",
}

BUDGET_MAP = {
    "Free only": 0,
    "Up to $20": 20,
    "Up to $50": 50,
    "Up to $100": 100,
    "Price is not important": None,
}

DEVICE_MAP = {"Computer": "computer", "Phone": "phone", "Tablet": "tablet"}

LENGTH_MAP = {
    "Quick lessons": "short",
    "Medium-sized course": "medium",
    "Long complete course": "long",
    "No preference": None,
}


def recommend_websites(websites, subject, level, learning_styles, guidance,
                       budget, payment_preference, digital_confidence, device,
                       course_length, user_prompt):
    selected_subject = subject.lower()
    selected_level = level.lower()
    selected_guidance = GUIDANCE_MAP[guidance]
    maximum_budget = BUDGET_MAP[budget]
    selected_device = DEVICE_MAP[device]
    selected_length = LENGTH_MAP[course_length]
    selected_styles = {
        value
        for style in learning_styles
        for value in STYLE_MAP[style]
    }
    prompt = user_prompt.lower()
    recommendations = []

    for website in websites:
        score = 0
        reasons = []

        if selected_subject in website["subjects"]:
            score += 10
            reasons.append(f"Offers {subject} learning material")
        else:
            score -= 5

        if selected_level in website["levels"]:
            score += 6
            reasons.append(f"Suitable for a {level.lower()} learner")
        else:
            score -= 3

        if any(style in website["styles"] for style in selected_styles):
            score += 3
            reasons.append("Supports your preferred learning style")

        if website["guidance"] == selected_guidance:
            score += 4
            reasons.append("Provides the amount of guidance you prefer")
        guidance_number = {"low": 1, "medium": 2, "high": 3}
        difference = abs(
            guidance_number[website["guidance"]]
            - guidance_number[selected_guidance]
        )
        if difference == 1:
            score += 1

        if maximum_budget is not None:
            if website["max_cost"] <= maximum_budget:
                score += 6
                reasons.append("Fits within your selected budget")
            else:
                score -= 8

        if payment_preference == "Free resources only":
            if website["price"] == "free":
                score += 7
                reasons.append("Completely free learning material is available")
            else:
                score -= 5
        elif payment_preference == "I prefer paying once":
            if website["payment"] != "subscription":
                score += 3
                reasons.append("Does not depend heavily on a subscription")
            else:
                score -= 2
        elif payment_preference == "A membership or subscription is okay":
            score += 1

        if digital_confidence == "Not very comfortable":
            if website["digital_difficulty"] == "easy":
                score += 8
                reasons.append("Has a relatively simple interface for new technology users")
            elif website["digital_difficulty"] == "medium":
                score += 1
            else:
                score -= 6
        elif digital_confidence == "Somewhat comfortable":
            score += {"easy": 4, "medium": 3}.get(website["digital_difficulty"], 0)
        else:
            score += 1

        if selected_device in website["devices"]:
            score += 4
            reasons.append(f"Suitable for learning on a {device.lower()}")
        else:
            score -= 4

        if selected_length is not None and selected_length in website["course_length"]:
            score += 3
            reasons.append("Has material matching your preferred course length")

        if prompt:
            score += sum(3 for value in website["subjects"] if value in prompt)
            score += sum(2 for value in website["levels"] if value in prompt)
            score += sum(2 for value in website["styles"] if value in prompt)
            if "free" in prompt and website["price"] == "free":
                score += 5
            if any(value in prompt for value in (
                "easy to use", "simple website", "bad with technology",
                "not good with technology",
            )) and website["digital_difficulty"] == "easy":
                score += 5
            if "phone" in prompt and "phone" in website["devices"]:
                score += 3

        recommendations.append({"website": website, "score": score, "reasons": reasons})

    return sorted(recommendations, key=lambda result: result["score"], reverse=True)
