import matplotlib.pyplot as plt

# Load the data
with open('/Users/vaibhavreddy/Documents/Scripts/Conversational_Analysis/human_text.txt', 'r') as file:
    human_text = file.readlines()[1:]

with open('/Users/vaibhavreddy/Documents/Scripts/Conversational_Analysis/robot_text.txt', 'r') as file:
    robot_text = file.readlines()[1:]

# Calculate message lengths
human_lengths = [len(message.split()) for message in human_text]
robot_lengths = [len(message.split()) for message in robot_text]

# Plotting the histogram of message lengths
plt.hist(human_lengths, bins=30, alpha=0.5, label='Human')
plt.hist(robot_lengths, bins=30, alpha=0.5, label='Robot')
plt.xlabel('Message Length (Number of Words)')
plt.ylabel('Frequency')
plt.title('Distribution of Message Lengths')
plt.legend()
plt.show()
