def mood_response(mood):
    mood = mood.lower()
    responses = {
        "happy": "Glad to hear you're happy! Stay Happy!", 
        "sad": "Sorry to hear you're feeling sad, hope things get better soon.",
        "excited": "Awesome! It is great to feel excited!"}
    return responses.get(mood, "Thank you for sharing how you are feeling today.")