#!/usr/bin/env python
# coding: utf-8
#get_ipython().system('pip install beautifulsoup4')
#get_ipython().system('pip install requests')
#get_ipython().system('pip install spacy')
#get_ipython().system('pip install trafilatura')
from bs4 import BeautifulSoup
import json
import numpy as np
import requests
from requests.models import MissingSchema
import spacy
import trafilatura
import pandas as pd
df=pd.read_csv(r'C:\Users\sgc\Desktop\TextExtraction\Input.xlsx - Sheet1.csv')
df.head()
url=[]
for i in range(len(df)):
    url.append(df.loc[i,'URL'])
print(url)
import textstat
#get_ipython().system('pip install vaderSentiment')
import re
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sid_obj= SentimentIntensityAnalyzer()
for i in range(5,7):
    downloaded=trafilatura.fetch_url(df['URL'][i])
    text=trafilatura.extract(downloaded)
   # print(text)
    df['count'][i]=len(text)
    df['sentences'][i]=textstat.sentence_count(text)
    df['Syllable'][i]=textstat.syllable_count(text)
    df['fog_index'][i]=textstat.gunning_fog(text)
    df['Complex_word'][i]=textstat.difficult_words(text)
    df['Complex_word_percent'][i]=(textstat.difficult_words(text)/len(text))*100
    sentences = text.split(".") #split the text into a list of sentences.
    words = text.split(" ")
    #words1=sentences.split(" ")
    average = sum(len(word) for word in words) / len(words)
    #split the input text into a list of separate words
    if(sentences[len(sentences)-1]==""): #if the last value in sentences is an empty string
          average_sentence_length = len(words) / len(sentences)-1
    else:
          average_sentence_length = len(words) / len(sentences)
    df['average_sentence_length'][i]=average_sentence_length
    df['average_word_length'][i]=average
    pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
    pronouns = pronounRegex.findall(text)
    df['Personal_Pronouns'][i]=pronouns
    df['Polarity'][i]=TextBlob(text).sentiment.polarity
    df['Subjectivity'][i]=TextBlob(text).sentiment.subjectivity
    res=sid_obj.polarity_scores(text)
    df['Positive_scores'][i]=res['pos']
    df['Negative_scores'][i]=res['neg']
len(df)
import requests
import nltk
from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
import random
from wordcloud import WordCloud
import os
import spacy
nlp = spacy.load('en_core_web_sm')
from textblob import TextBlob
#from pattern.en import sentiment
import spacy
nlp = spacy.load('en_core_web_sm')
import trafilatura
import textstat
#get_ipython().system('pip install Textstat')
for i in range(len(df)):
       try:
           text=" "
           downloaded = trafilatura.fetch_url(df['URL'][i])
           text=trafilatura.extract(downloaded)
           #clean_text= text.replace("n", " ")
           #clean_text= clean_text.replace("/", " ")       
           #clean_text= ''.join([c for c in clean_text if c != "'"])
           #sentence=[]
           #tokens = nlp(text)
           #for sent in tokens.sents:
           #    sentence.append((sent.text.strip()))
           df['sentences'][i]=textstat.sentence_count(text)
           df['Syllable'][i]=textstat.syllable_count(text)
           df['fog_index'][i]=textstat.gunning_fog(text)
           df['Complex_word'][i]=textstat.difficult_words(text)
           df['Complex_word_percent'][i]=(textstat.difficult_words(text)/len(text))*100
           sentences = text.split(".") #split the text into a list of sentences.
           words = text.split(" ")
    #words1=sentences.split(" ")
           average = sum(len(word) for word in words) / len(words)
    #split the input text into a list of separate words
           if(sentences[len(sentences)-1]==""): #if the last value in sentences is an empty string
                    average_sentence_length = len(words) / len(sentences)-1
           else:
                    average_sentence_length = len(words) / len(sentences)
           df['average_sentence_length'][i]=average_sentence_length
           df['average_word_length'][i]=average
           pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
           pronouns = pronounRegex.findall(text)
           df['Personal_Pronouns'][i]=pronouns
           df['Polarity'][i]=TextBlob(text).sentiment.polarity
           df['Subjectivity'][i]=TextBlob(text).sentiment.subjectivity
           res=sid_obj.polarity_scores(text)
           df['Positive_scores'][i]=res['pos']
           df['Negative_scores'][i]=res['neg']
           #df['count'][i]=len(text)
           #print(text)
       except:
           print("404 error file")
df.head(20)
df.to_csv("Output_expected.csv")





