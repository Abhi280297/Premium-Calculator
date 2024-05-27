#!/usr/bin/env python
# coding: utf-8

# In[2]:


def check_premium(gender,year_of_birth,smoker):
    
    smoker_text     = 'Your annual premium is = Rs '
    non_somker_text = 'Your Discounted annual premium is = Rs '
    
    if gender == 'MALE':
        if year_of_birth > 1990 and year_of_birth <= 2000:
            if smoker == 'YES':
                print (smoker_text, 35000)
            else:
                print (non_somker_text, 35000 - (35000 * 0.1))
                
        elif year_of_birth > 1970 and year_of_birth <= 1990:
            if smoker == 'YES':
                print (smoker_text, 40000)
            else:
                print (non_somker_text, 40000 - (40000 * 0.05))      
                
    elif gender == 'FEMALE':
        if year_of_birth > 1990 and year_of_birth <= 2000:
            if smoker == 'YES':
                print (smoker_text, 30000)
            else:
                print (non_somker_text, 30000 - (30000 * 0.1))
                
        if year_of_birth > 1970 and year_of_birth <= 1990:
            if smoker == 'YES':
                print (smoker_text, 35000)
            else:
                print (non_somker_text, 35000 - (35000 * 0.05))    


# In[10]:


check_premium('FEMALE', 1990, 'NO')  # you can change the data here and check the premium.


# In[12]:


check_premium('MALE', 1989, 'YES')  # you can change the data here and check the premium.


# In[13]:


check_premium('FEMALE', 1989, 'YES')  # you can change the data here and check the premium.


# In[ ]:




