# Fake News Prediction using Machine Learning and Natural Language Processing

This repository contains the code for a machine learning project that predicts whether a news article is real or fake based on its content. The project uses Natural Language Processing (NLP) techniques to preprocess the data, and a machine learning algorithm to train a model to make the prediction.

## Dataset

The dataset used in this project is the [Fake and Real News Dataset](https://www.kaggle.com/competitions/fake-news/data) from Kaggle. 
## Data Preprocessing

Before training the machine learning model, the data goes through a preprocessing stage, which includes the following steps:

1. *Data Cleaning*: Remove any unnecessary characters and symbols from the news articles, such as punctuation marks and special characters.

2. *Tokenization*: Split the news articles into individual words.

3. *Stop Word Removal*: Remove commonly used words that don't add much meaning to the news articles, such as "the", "and", and "is".

4. *Stemming*: Reduce words to their root form, so that words like "running" and "ran" are treated as the same word.

5. *Vectorization*: Convert the words into numerical vectors that can be fed into the machine learning algorithm.

## Model Training and Evaluation

Models Used: Logistic Regression, Naive Bayes.

## Getting Started

To get started with this project, you can follow these steps:

1. Clone this repository to your local machine.

2. Install the required packages.

3. Open the `fake_news_prediction.ipynb` notebook and run the cells.

## Conclusion

This project demonstrates how machine learning and natural language processing techniques can be used to predict whether a news article is real or fake. With a maximum accuracy of 98.73%.
