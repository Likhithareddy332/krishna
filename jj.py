from textblob import TextBlob

def correct_spelling(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()
    return str(corrected_text)

# Test the spell corrector
misspelled_text = "I havv a speling errror."
corrected_text = correct_spelling(misspelled_text)
print(f"Corrected: '{corrected_text}'")
