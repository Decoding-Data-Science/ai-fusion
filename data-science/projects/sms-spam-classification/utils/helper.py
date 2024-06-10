import os, sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)

import nltk, re
from nltk import word_tokenize

def remove_url(text):
    pattern = re.compile(r'https?: ?//\S+|www\.\S+')
    return pattern.sub(r'', text)

def remove_html_tags(text):
    pattern = re.compile('<.*?>')
    return pattern.sub(r'', text)

def remove_special_char(text):
    text = nltk.word_tokenize(text) 
    text = [i for i in text if i.isalnum()]
    return ' '.join(text)

lemma = nltk.wordnet.WordNetLemmatizer()

def lemmatizer(text):
    text = ' '.join(lemma.lemmatize(word) for word in text.split(' '))
    return text

def transform_text(text):
    '''
    Transform the original text by:
        Lowercase,
        Remove URL and HTML tags,
        Remove all Special Characters and Punctuation,
        Remove Newlines,
        Remove the words containing numbers,
        Lemmatize the text
    '''
    text = str(text).lower()
    text = remove_url(text)
    text = remove_html_tags(text)
    text = remove_special_char(text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = lemmatizer(text)
    return text

def remove_custom_stopwords(text):
    stop_words = ['a', 'the']
    text = str(text).lower()
    text = word_tokenize(text)
    return ' '.join([str(i) for i in text if i not in stop_words])

def preprocess_text(text):
    text = transform_text(text)
    text = remove_custom_stopwords(text)
    return text