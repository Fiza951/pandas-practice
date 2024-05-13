# read csv file
import pandas as pd  
df_titanic= pd.read_csv("titanic3.csv")
print(df_titanic)
IMBDS = pd.read_csv("imdb.csv")
print(IMBDS)
PEOPLE = pd.read_csv("people.csv")
print(PEOPLE)


# python dictionary  VS pandas  data frame

# dictionary 
people = {
    "name"        :["fiza","zaib","sameer","alishba","saad"],
     "age"        :[21,20,22,19,20],
    "address"     : ['Lahore', 'karachi ', 'Islamabad','okara','Multan'],
    "blood group" :['A', 'AB', 'O','B','AB']
}
print (people) 

# creating datafran for dictionary 
df_dictionary = pd.DataFrame(people)
print(df_dictionary)

# accessind elements from dictionaries and dataframeworks

#Dictionary
#1
c= people.get("name")
print(c)
 #2
w= people["age"]
print(w)

# pandas data framework
t =  PEOPLE['name']
print(t)
y=IMBDS['actors_list']
print(y)
u=df_titanic['name']
print(u)

#creating a dataframe from 2D array and naming rows and columns of data set
# import libraries
import numpy as np
#Creating array
arr = np.random.randint(10,100,size=(5,5))
print('array', arr)
# converting to dataframe
df=pd.DataFrame(arr)
print(df)
# naming rows and columns 
print ('labled data framework')
row_lables =['row1','row2','row3','row4','row5']
col_lables=['col1','col2','col3','col4','col5']
df_labled= pd.DataFrame(data=arr , index=row_lables, columns =col_lables)
print(df_labled)