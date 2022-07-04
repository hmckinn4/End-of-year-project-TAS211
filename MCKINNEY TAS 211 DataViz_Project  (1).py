#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use("fivethirtyeight")
plt.rcParams["figure.figsize"] = (8, 6)

import logging #these 2 lines suppress the pink warning messages
logging.getLogger().setLevel(logging.CRITICAL) 


# In[2]:


df = pd.read_csv("super0308.csv", parse_dates = ["FirstYear"]) #importing data set 

pd.set_option("display.max_columns", None) #displays all columns 
df.head() 


# # Who is the most intelligent character?

# In[3]:


#This pulls specific column types to to trim the data and narrow the focus.
df_looks = df[["Name", "Intelligence"]]
df_looks = df_looks.dropna(subset = ["Intelligence"]) #dropping any NaN values
df_looks["Intelligence"] = df_looks["Intelligence"].astype(int) #turns strings into integers 
df_looks[0:25] 

df_rank = df_looks.sort_values(by = "Intelligence", ascending = False) #sorts intelligence from highest to lowest number

df_rank.head(60) 


# ## What score of intelligence occurs most in the characters?

# In[4]:


df_looks["Intelligence"].value_counts().plot(kind='barh') #Creates vizual representation of occuance per intelligence level 
plt.title("Intelligence Score Ordered by Occurance", fontsize = 20) 
plt.xlabel("Occurances", fontsize = 20)
plt.ylabel("Intelligence Score ", fontsize = 20)


# ## Having "50 points" of intelligence occurs most among characters.
# 
# 
# ## Therefore, 50 is the mode. 

# ## Which teams comprise the majority of characters?

# In[5]:


df = df.dropna(subset = ["Team"]) #dropping all NaN
df["Team"]


# In[6]:


#df.loc command locates everyything within the team collumn that is not mentioned as other than or != (not equal)
df_other = df.loc[(df["Team"] != "Avengers") & (df["Team"] != "Justice League") & (df["Team"] != "X-Men") & (df["Team"] != "Guardians of the Galaxy") & (df["Team"] != "Legion of Doom") & (df["Team"] != "Freelance"), 'Team'] = "other"
team_val_counts = df["Team"].value_counts() 
team_val_counts 

team_val_counts.plot(kind = "pie", autopct = "%1.0f%%", subplots = True, fontsize = 14) #creating pie chart
plt.title("Percent of characters per team ", fontsize = 18)
plt.ylabel('')
plt.axis("equal")


# ## The avengers have the most characters by a large margin at 39%. The chart above shows the rest of the distribution of charcters.
# 
# ## After the Freelance team, all other teams hold 1% or less of the total characters.
# ## All of these teams fall into the "Other" category
# ## How many teams are in this "Other category?
# 

# In[7]:


other = df.loc[(df["Team"] != "Avengers") & (df["Team"] != "Justice League") & (df["Team"] != "X-Men") & (df["Team"] != "Guardians of the Galaxy") & (df["Team"] != "Legion of Doom") & (df["Team"] != "Freelance")]
    #df.loc creates variable "other" comprising everything within the "Team" column except for the mentioned rows 


# In[8]:


other_val_counts = other["Team"].value_counts()
df_other = df.loc[(df["Team"] != "Avengers") & (df["Team"] != "Justice League") & (df["Team"] != "X-Men") & (df["Team"] != "Guardians of the Galaxy") & (df["Team"] != "Legion of Doom") & (df["Team"] != "Freelance"), 'Team'] = "other"
team_val_counts = df["Team"].value_counts()
other_val_counts


# ## 102 teams are in the "Other Category"

# In[9]:


other_counts = df["Team"].value_counts()
other_counts


# ## What percent of characters have yellow eyes?

# In[10]:


df_other = df.loc[(df["EyeColor"] != "Yellow"), 'EyeColor'] = "other" #creating variable for all eyecolors other than yellow
eye_color_counts = df["EyeColor"].value_counts() #valuecounting new Eyecolor data set 
eye_color_counts

eye_color_counts.plot(kind = "pie", autopct = "%1.0f%%", subplots = True, fontsize = 14)
plt.title("Percent of characters per team ", fontsize = 18)
plt.ylabel('')
plt.axis("equal")


# ## 2% of characters have yellow eyes.

# In[ ]:




