import json

# In[422]:

# function for reading files
def readFile(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    dataset = json.loads(data)
    return dataset