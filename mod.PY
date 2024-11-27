# mood_responses.py

def mood_response(mood):
    """
    Takes the user's mood as input and returns a corresponding response and suggestion.
    :param mood: str - The mood entered by the user
    :return: str - A custom response
    """
    mood = mood.lower()  # Normalize input to lowercase for consistent matching

    # Mapping moods and their synonyms to responses and suggestions
    mood_data = {
        "happy": {
            "synonyms": ["joyful", "content", "cheerful", "elated"],
            "response": "That's great to hear! Keep spreading positivity! 😊",
            "suggestion": "Why not share your happiness with someone you care about?"
        },
        "sad": {
            "synonyms": ["down", "upset", "blue", "unhappy"],
            "response": "I'm sorry you're feeling that way. Remember, tough times don't last. 💙",
            "suggestion": "Try listening to some uplifting music or talking to a friend."
        },
        "excited": {
            "synonyms": ["thrilled", "ecstatic", "overjoyed"],
            "response": "Woohoo! What's got you so pumped up? 🎉",
            "suggestion": "Channel that energy into something creative or fun!"
        },
        "angry": {
            "synonyms": ["mad", "frustrated", "annoyed"],
            "response": "Take a deep breath. Let's try to calm down together. 🧘",
            "suggestion": "Try some breathing exercises or take a walk to cool off."
        },
        "tired": {
            "synonyms": ["exhausted", "weary", "sleepy"],
            "response": "You should rest up. A good nap might work wonders! 😴",
            "suggestion": "Make sure you're hydrated and consider a short power nap."
        },
        "confused": {
            "synonyms": ["perplexed", "uncertain", "lost"],
            "response": "It's okay to feel this way. Try breaking things down step by step. 🤔",
            "suggestion": "Write down what’s confusing you and tackle it one piece at a time."
        },
    }

    # Match mood or its synonyms
    for key, value in mood_data.items():
        if mood == key or mood in value["synonyms"]:
            return f"{value['response']}\nSuggestion: {value['suggestion']}"

    # Default response for unrecognized moods
    return "That's an interesting mood! I hope you have a good day. 🌟"

def log_mood(mood):
    """
    Logs the user's mood to a text file.
    :param mood: str - The mood entered by the user
    """
    with open("mood_log.txt", "a") as file:
        file.write(f"{mood}\n")
