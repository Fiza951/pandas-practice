# read csv file by name 
import pandas as pd  
df_titanic= pd.read_csv("titanic3.csv")
print(df_titanic)
IMBDS = pd.read_csv("imdb.csv")
print(IMBDS)
PEOPLE = pd.read_csv("people.csv")
print(PEOPLE)  # output main data set + 234 rowx *  24 columns deta haindata set ki

# read csv file bt copy path
imdb1 = pd.read_csv(r'C:\Users\pc\pandas\pand prac\imdb.csv')
print(imdb1)

People1= pd.read_csv(r'C:\Users\pc\pandas\pand prac\people.csv')
print(People1)

titanic1= pd.read_csv(r'C:\Users\pc\pandas\pand prac\titanic3.csv')
print(titanic1)  # same output as above

 
# python dictionary  VS pandas  data frame

# dictionary 
people = {
    "name"        :["fiza","zaib","sameer","alishba","saad"],
     "age"        :[21,20,22,19,20],
    "address"     : ['Lahore', 'karachi ', 'Islamabad','okara','Multan'],
    "blood group" :['A', 'AB', 'O','B','AB']
}
print (people)  # output sath sath ek line mai aaye gi , se saperate hogi


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
print(u)  # same tareeqa se access kr sakty hain or dictionary out put el line mai aajaye gi 
# or csv ki output mai index asscess wala column or mrrchay uska name or data type aaye gi

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


#Direct creating a numpy array and labling the row and column index
# remember numpy means only numbers

arr =np.random.randint(10,100,size=(5,6))
print('Array\n',arr)

df_arr= pd.DataFrame(data=arr)
print('df_arr\n',df_arr)

col_lables=['col1','col2','col3','col4','col5','col6']
row_lables=['row1','row2','row3','row4','ror5']
Df_arr=pd.DataFrame(data = arr,index = row_lables, columns=col_lables)
print("Df_arr\n", Df_arr)
#v output
#Array
# [[99 38 99 60 38 72]
# [31 96 96 78 69 41] 
# [43 32 57 88 79 79] 
## [23 35 68 59 17 49] 
 #[41 46 41 15 54 75]]
#df_arr
#     0   1   2   3   4   5
#0  99  38  99  60  38  72 
#1  31  96  96  78  69  41 
#2  43  32  57  88  79  79 
#3  23  35  68  59  17  49
#4  41  46  41  15  54  75
#Df_arr
#       col1  col2  col3  col4  col5  col6
#row1    99    38    99    60    38    72
#ow2    31    96    96    78    69    41
#row3    43    32    57    88    79    79
#row4    23    35    68    59    17    49
#ror5    41    46    41    15    54    75



# creating a simple series it starts with capital Series

# without index 

list = [1,2,3,4,5,6]
serr= pd.Series(data = list)
print(serr)
# out put 0 se 5 index automatically aaye ga or data ki type bhi  last mai 
#dtype: int64

# with index 

list1 = [2,4,6,8,10,12,14,16]
indices = ['R1','R2','R3','R4','R5','R6','R7','R8']
Ser1=pd.Series(data=list1 , index=indices)
print(Ser1)

# type of a series 
print(type(serr))
#<class 'pandas.core.series.Series'>
print(type(Ser1))
# same for all Series


# Accessing elements
q = Ser1['R2']
print(q)
p = Ser1['R3']
print(p)


# Series having empty element in list
list2 =['sameer','fiza','rauf', 'irfan', 'hamza','maaz']
indices = ['P1','P2','P3','P4','P5','P6']
Ser2= pd.Series(data=list2, index= indices)
print(Ser2)

# Serie havin missing index and list elements
list3 =[' ','','rauf', 'irfan', 'hamza','maaz']
indices = ['P1','P2',' ','P4','  ','P6']
Ser3= pd.Series(data=list3, index= indices)
print(Ser3)
# in output missing vales are not given
# elements may missing from list or maybe from index


# floats as index
list4= ['apple','mango','banana','grape']
Indfloat=[0.1, 0.2, 0.3, 0.4]
Ser4=pd.Series(data=list4 , index = Indfloat)
print(Ser4)
# output + dtype : object

# floats as list
list5=[0.1, 0.2, 0.3, 0.4]
IND=[1,2,3,4]
Ser5=pd.Series(data=list5 , index = IND)
print(Ser5)
#output + dtype : float64

# Nan values are placeholders for missing values
list6 =[45,67,89,np.nan,78]
Ser6=pd.Series(data = list6)
print(Ser6)
# output
#0    45.0     
#1    67.0     
#2    89.0     
#3     NaN     
#4    78.0     
#dtype: float64

# specify a datatype to series objects
# specify a data type name by ourself
# ager data int hai or hm data type floar define krdain to wo fliat 
#mai output aaye gi jese ex 2


# ex 1
list7 =[45,67,89,45,78]
Ser7=pd.Series(data = list7 ,dtype= np.uint8)
print(Ser7)
# output
#0    45    
#1    67     
#2    89    
#3     45     
#4    78     
#dtype: uint8

#ex 2
list8=[45,67,89,45,78]
Ser8=pd.Series(data = list8,dtype= np.float64)
print(Ser8)

# output
#0    45.0     
#1    67.0     
#2    89.0     
#3    45.0     
#4    78.0     
#dtype: float64

# naming  series
list9 = [1,2,3,4,5]
Ser9=pd.Series(data=list9 , name='range of 6')
print(Ser9)
#
#0    1
#1    2
#2    3
#3    4
#4    5
#Name: range of 6, dtype: int64


#creating series from numpy array
#ex1
s=pd.Series(data= np.arange(6) , name ='range of 6')
print(s)
# output
#0    0
#1    1
#2    2
#3    3
#4    4
#5    5
#Name: range of 6, dtype: int32

# ex2
f=pd.Series(data=np.array([22,34.5,67,78,77.8]),dtype="float64",name="points")
print(f)
#ouytput
#0    22.0
#1    34.5
#2    67.0
#3    78.0
#4    77.8
#Name: points, dtype: float


#creating series from dictionary
Dict_1 ={
    'name ':['fiza','salman','amaya','sidra','ali','arham'],
    'age':[22,21,22,24,23,21],
    'Gender':['F','M','F','F','M','M'],
    'Grade':['A','B','F','D','A','F']
}
print(Dict_1)
j=pd.Series(data = Dict_1)
print(j)
#output
#{'name ': ['fiza', 'salman', 'amaya', 'sidra', 'ali', 'arham'], 'age': [22, 21, 22, 24, 23, 21], 'Gender': ['F', 'M', 'F', 'F', 'M', 'M'], 'Grade': ['A', 'B', 'F', 'D', 'A', 'F']}
#name      [fiza, salman, amaya, sidra, ali, arham]
#age                       [22, 21, 22, 24, 23, 21]
#Gender                          [F, M, F, F, M, M]
#Grade                           [A, B, F, D, A, F]
#dtype: object



#creating series from scalar value
d=pd.Series(data= 30)
print(d)
#output
#0    30
#dtype: int64

#creating  empty series  but they must have dtype 
c=pd.Series(dtype='float64')
print(c)
#output
#Series([], dtype: float64)



# Attributes of panda series
dic={
    0 :'rauf',
    1: 'rehman',
    2 :'rashid',
    3:'hanif'
}
series=pd.Series(data=dic , name='dictionary')
print(series)
print(series.name)
print(series.shape)
print(series.ndim)
print(series.index)
print(series.empty)
print(series.size)
print(series.index)
print(series.values)

#output
#0      rauf
#1    rehman
#2    rashid
#3     hanif
#Name: dictionary, dtype: object
#dictionary
#(4,)
#1
#Index([0, 1, 2, 3], dtype='int64')
#False
#4
#Index([0, 1, 2, 3], dtype='int64')
#['rauf' 'rehman' 'rashid' 'hanif']


