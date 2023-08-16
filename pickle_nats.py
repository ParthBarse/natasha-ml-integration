#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# In[2]:


def makeTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')	# make tokens after splitting by slash
    total_Tokens = []
    for i in tkns_BySlash:
        tokens = str(i).split('-')	# make tokens after splitting by dash
        tkns_ByDot = []
        for j in range(0,len(tokens)):
            temp_Tokens = str(tokens[j]).split('.')	# make tokens after splitting by dot
            tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
    total_Tokens = list(set(total_Tokens))	#remove redundant tokens
    if 'com' in total_Tokens:
        total_Tokens.remove('com')


# In[3]:


file = "pickel_model.pkl"
with open(file, 'rb') as f1:  
    logit = pickle.load(f1)
f1.close()


# In[4]:


urls = []
new_url = input("Enter a new URL: ")

# Append the new URL to the list
urls.append(new_url)


# In[5]:


file = "pickel_vector.pkl"
with open(file, 'rb') as f2:  
    vectorizer = pickle.load(f2)
f2.close()
vectorizer = vectorizer
x = vectorizer.transform(urls)
#score = lgr.score(x_test, y_test)
y_predict = logit.predict(x)


# In[6]:


print(y_predict)


# In[7]:


# if(prediction == 0):
#     print('benign')
# elif(prediction == 1):
#     print('defacement')
# elif(prediction == 2):
#     print('phishing')
# else:
#     print('malware')

