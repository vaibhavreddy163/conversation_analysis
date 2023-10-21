# Conversational Analysis of Human-Robot Interactions

## Project Description

This project aims to analyze conversations between humans and robots to extract meaningful insights. The dataset comprises two text files, one representing human interactions and the other representing robot responses in a conversational setting. The analysis involves various stages, including data preprocessing, exploratory data analysis, and modeling for more advanced analysis like chatbot creation.

## Structure

- `human_text.txt`: Text file containing human messages.
- `robot_text.txt`: Text file containing robot messages.
- `preprocessing.py`: Python script used for data cleaning and preprocessing.

## How to Run

### 1. **Data Preprocessing**

   Run `preprocessing.py` to clean and filter the text data. This script removes non-English conversations and special characters, making the data ready for analysis.
   
   ```bash
   python preprocessing.py
   ```

### 2. **Exploratory Data Analysis**

   Additional scripts for exploratory data analysis can be added to this repository, including word frequency analysis, bigram analysis, and more.

### 3. **Advanced Analysis**

   Further analysis like modeling for chatbot creation can be performed using additional scripts and resources added to this project.

## Dependencies

- Python 3.x
- `langdetect` library for language detection

   Install it using pip:
   ```bash
   pip install langdetect
   ```

## Author
Vaibhav Reddy Kotha
