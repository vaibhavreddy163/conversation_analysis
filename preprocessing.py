import re
from langdetect import detect

# Function to clean texts
def clean_text(text):
    text = text.lower()  # Convert text to lowercase
    text = re.sub(r"[^a-zA-Z\s']", '', text)  # Remove special characters except apostrophes
    return text

# Function to check if a text is in English
def is_english(text):
    try:
        language = detect(text)
    except:
        return False  # In case the language detection fails
    return language == 'en'

# Load the data
with open('/Users/vaibhavreddy/Documents/Scripts/Conversational_Analysis/human_text.txt', 'r') as file:
    human_text = file.readlines()[1:]

with open('/Users/vaibhavreddy/Documents/Scripts/Conversational_Analysis/robot_text.txt', 'r') as file:
    robot_text = file.readlines()[1:]

# Applying cleaning and language filtering
english_human_text = [clean_text(text) for text in human_text if is_english(text)]
english_robot_text = [clean_text(text) for text in robot_text if is_english(text)]

# Saving the cleaned and filtered texts to new files
with open('/Users/vaibhavreddy/Documents/Scripts/Conversational_Analysis/cleaned_data/cleaned_human_text.txt', 'w') as file:
    file.writelines(english_human_text)

with open('/Users/vaibhavreddy/Documents/Scripts/Conversational_Analysis/cleaned_data/cleaned_robot_text.txt', 'w') as file:
    file.writelines(english_robot_text)
