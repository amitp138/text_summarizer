import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from nltk.corpus import stopwords
from heapq import nlargest

def summarize_text(text, max_sentences=2):
    # Load the spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Define the punctuation characters for text processing
    local_punctuation = punctuation + "\n"

    # Get the list of English stopwords
    stop_words = set(stopwords.words("english"))

    # Create a spaCy document
    doc = nlp(text)

    # Initialize word frequency
    word_frequencies = {}
    
    for word in doc:
        if word.text.lower() not in stop_words:
            if word.text.lower() not in local_punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    # Get the maximum frequency
    max_frequency = max(word_frequencies.values())

    # Normalize word frequencies
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency

    # Tokenize the sentences
    sentence_tokens = [sent for sent in doc.sents]

    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    select_length = int(len(sentence_tokens) * max_sentences)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    final_summary = [word.text for word in summary]
    summary = " ".join(final_summary)

    return summary
