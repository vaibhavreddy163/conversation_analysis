import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')


# Load the data
with open('/Users/vaibhavreddy/Documents/Scripts/Conversational_Analysis/human_text.txt', 'r') as file:
    human_text = file.readlines()[1:]

with open('/Users/vaibhavreddy/Documents/Scripts/Conversational_Analysis/robot_text.txt', 'r') as file:
    robot_text = file.readlines()[1:]

# Define stopwords
basic_stopwords = set([
    # Add any stopwords you want to exclude here as strings separated by commas
])

# Define a function to preprocess the texts
def preprocess_texts(texts, stopwords):
    preprocessed_texts = []
    for message in texts:
        words = word_tokenize(message)
        words = [word.lower() for word in words if word.isalnum() and word.lower() not in stopwords]
        preprocessed_texts.extend(words)
    return preprocessed_texts

# Preprocess the texts
human_words = preprocess_texts(human_text, basic_stopwords)
robot_words = preprocess_texts(robot_text, basic_stopwords)

# Define a function to plot the most common bigrams
def plot_most_common_bigrams(words, title, num_bigrams=20):
    bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
    common_bigrams = Counter(bigrams).most_common(num_bigrams)
    labels, counts = zip(*common_bigrams)
    labels = [" ".join(label) for label in labels]
    plt.barh(labels, counts, color='lightgreen')
    plt.xlabel('Frequency')
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.show()

# Plot the most common bigrams for human and robot texts
plot_most_common_bigrams(human_words, 'Top Bigrams in Human Texts')
plot_most_common_bigrams(robot_words, 'Top Bigrams in Robot Texts')
