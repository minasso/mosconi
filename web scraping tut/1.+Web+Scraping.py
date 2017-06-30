# In[4]:

from datetime import datetime

from lxml import html
import requests

import numpy as np
import pandas as pd
import matplotlib.pylab as plt

pd.options.display.max_columns=50

def print_element(element):
    print(( "<%s %s>%s ..." % (element.tag, element.attrib, element.text_content()[:200].replace("\n", " "))))


# In[6]:

page = requests.get('http://en.wikipedia.org/wiki/List_of_Nobel_laureates')
tree = html.fromstring(page.text)
print_element(tree)


# ## Locate The table

# ### First we find all tables

# In[7]:

tables = tree.xpath('//table')
for table in tables:
    print_element(table)


# **When locating the table watchout for client side javascript alteration to the HTML code**

# In[8]:

table = tree.xpath('//table[@class="wikitable sortable"]')[0]
print_element(table)


# ## Extract the Subjects & Years

# In[9]:

subjects = [subject[0].text_content().replace("\n"," ") for subject in table.xpath('tr')[0][1:]]
subjects


# In[10]:

years = [item[0].text for item in table.xpath('tr')[1:-1]]


# ## Extract Winners Data

# ### Testing for a sigle years

# In[11]:

for index, item in enumerate(table.xpath('tr')[1][1:]):
    subject = subjects[index]
    print("%s:" % subject)
    for winner in item.xpath('span[@class="vcard"]/span/a'):
        winner_name = winner.attrib["title"]
        winner_url = winner.attrib["href"]
        print(" - %s" % winner_name)


# ### Extract The complete table

# In[9]:

year_list = []
subject_list = []
name_list = []
url_list = []
for y_index, year in enumerate(years):
    #print year
    for index, item in enumerate(table.xpath('tr')[y_index + 1][1:]):
        subject = subjects[index]
        #print "%s:" % subject
        for winner in item.xpath('span[@class="vcard"]/span/a'):
            winner_name = winner.attrib["title"]
            winner_url = winner.attrib["href"]
            #print " - %s" % winner_name
            year_list.append(year)
            subject_list.append(subject)
            name_list.append(winner_name)
            url_list.append(winner_url)


# # Post Processing in Pandas

# In[10]:

data_set = pd.DataFrame(name_list, columns=["winner_name"])
data_set["subject"] = subject_list
data_set["year"] = year_list
data_set["year"] = data_set["year"].astype(np.int32)
data_set["url"] = url_list
data_set.head(5)


# ## Looking at the data

# In[11]:

years_df = data_set["year"].value_counts().sort_index()
years_df


# ## Number of Prizes per Year

# In[12]:

plt.figure(figsize=(15,5))
plt.plot(years_df.index, years_df.values, linewidth=2, alpha=.6)
plt.grid()
plt.xlabel("Year")
plt.ylabel("Number of Prizes")
plt.show();
print("Total Prizes: %s" % len(data_set))


# In[13]:

years_df.value_counts()
plt.bar(years_df.value_counts().index, years_df.value_counts())
plt.box(on="off")
plt.grid()
plt.xlabel("Number of Nober Prizes/Year")
plt.xlabel("")
plt.show();


# ## By Subject

# In[14]:

plt.figure(figsize=(13,5))

for subject in subjects:
    df = data_set[data_set["subject"]==subject]["year"].value_counts().sort_index().cumsum()
    plt.plot(df.index, df, label=subject, linewidth=2, alpha=.6)


plt.grid()
plt.legend(loc="best")
plt.xlabel("Year")
plt.ylabel("Cumulative Sum of Given Nobel Prizes")
plt.xticks(np.arange(1900, 2020, 10))

plt.show();


# # The effects of WW I and WW II

# In[15]:

plt.figure(figsize=(13,5))

for subject in subjects:
    df = data_set[(data_set["subject"]==subject) &
                  (data_set["year"].astype(np.int32)<1950)]["year"].value_counts().sort_index().cumsum()
    plt.plot(df.index, df, label=subject, linewidth=2, alpha=.6)

plt.grid()
plt.legend(loc="best")
plt.xlabel("Year")
plt.ylabel("Cumulative Sum of Given Nobel Prizes")
plt.xticks(np.arange(1900, 1950, 5))

gca = plt.gca()

gca.add_patch(plt.Rectangle((1914,0), 4, 60, alpha=.3, color="orange"))
gca.add_patch(plt.Rectangle((1939,0), (45-39), 60, alpha=.3, color="orange"))

plt.annotate(s="WW I", xy=(1915,55))
plt.annotate(s="WW II", xy=(1941,55))
plt.show();

