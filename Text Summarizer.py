#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -U spacy')
get_ipython().system('python -m spacy download en_core_web_sm')


# In[11]:


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from nltk.corpus import stopwords
from heapq import nlargest


# In[12]:


text= """
I enjoyed hearing you speak at the Martian Writers' Conference last month. Not many New York-based agents take the time to come to Mars to meet the local writers; we really appreciate the ones who do. Since you so ably represented BLUE-EYED VENUSIAN, I hope you will be interested in my book, MY HEART GOES ON TO MARS, a romantic thriller that will appeal to workers in the interstellar travel industry because it is the first novel to portray their difficult-but- glamorous job accurately. Stella Artois (157) is a flight attendant on the brand-new starcruiser Titanic, the largest passenger starcraft ever built. Hardly has she strapped in the wealthy passengers on its monumentally-costly maiden voyage, however, when she hears turmoil from below deck. "That's funny," she thinks, climbing below. "As on the ship for which my vessel is named, there is no economy class on this trip." Taken hostage by a rollicking horde of Edwardian stereotypes, can Stella escape, warn the captain about that space iceberg, and find true love before it's time to serve the warm peanuts to first class? I am uniquely qualified to tell this story, due to my many years as a supervisor for Intergalactic Flights, Inc., my Ph.D. in astrophysics from the University of Guam, and a childhood spent locked in a closet, watching the films of James Cameron on an endless loop. My writing has been published in Martian Mother's Day, Good Cryptkeeping, and Ms. Thank you for your time in reviewing this, and I hope that the enclosed synopsis will pique your interest. I may be reached at the address and phone number above, as well as via e- mail at aspiring@pickme.net. I enclose a SASE for your convenience, and I look forward to hearing from you soon. 
"""


# In[13]:


stopwords = stopwords.words("English")


# In[14]:


stopwords 


# In[15]:


nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
doc 


# In[16]:


tokens = [token.text for token in doc] 
print(tokens)


# In[17]:


punctuation = punctuation + "\n"
punctuation   


# In[18]:


word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords: 
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

print(word_frequencies)


# In[19]:


max_frequency = max(word_frequencies.values())
max_frequency 


# In[20]:


for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency
    
print(word_frequencies) 


# In[21]:


sentence_tokens = [sent for sent in doc.sents]
print(sentence_tokens) 


# In[22]:


sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]
                
sentence_scores  


# In[23]:


select_length = int(len(sentence_tokens)*0.5)
select_length  


# In[24]:


summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
summary


# In[25]:


final_summary = [word.text for word in summary]
final_summary


# In[26]:


summary = " ".join(final_summary)
summary


# In[27]:


print(text)


# In[28]:


print(summary)


# In[ ]:




