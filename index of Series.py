import pandas as pd 
import numpy as np
# index
list = [4,8,12,16,20,24,28]
SER = pd.Series(data=list)
print(SER)
print(SER.index)
# output
#0     4
#1     8
#2    12
#3    16
#4    20
#5    24
#6    28
#dtype: int64
#RangeIndex(start =0 ,stop=7,step=1)

#  Changing index of a series object
# series
list10=['maaz','irfan','sohail','rayyan','ahmed']
Ser10 = pd.Series(data=list10)
print(Ser10)
print(Ser10.index)

# first method to change index 
arr1 = np.random.randint(100,200,size=5)
Ser10.index = arr1
print(Ser10)
print(Ser10.index)


#output
#0      maaz  
#1     irfan  
#2    sohail  
#3    rayyan  
#4     ahmed  
#dtype: object
#RangeIndex(start=0, stop=5, step=1)


# output
#150      maaz
#193     irfan
#151    sohail
#121    rayyan
#115     ahmed
#dtype: object
#Index([150, 193, 151, 121, 115], dtype='int32')

# Second Method of changing index with floats
new_index =[1,4,6.0,7,4]
Ser10.index = new_index
print(Ser10)
print(Ser10.index)

#output
#1.0      maaz
#4.0     irfan
#6.0    sohail
#7.0    rayyan
#4.0     ahmed
#dtype: object
#Index([1.0, 4.0, 6.0, 7.0, 4.0], dtype='float64')


#with integers
new_index1 =[1,4,6,7,4]
Ser10.index = new_index1
print(Ser10)
print(Ser10.index)
# out put
#1      maaz
#4     irfan
#6    sohail
#7    rayyan
#4     ahmed
#dtype: object
#Index([1, 4, 6, 7, 4], dtype='int64')


 # use of indexing 
 # IDENTIFICATIOM
 
 # getting values from +ve &-ve positions
LIST = ['fiza','alishba','zoya','shazma','raheel','Sameer']
indecies=[1,4,8,12,16,20]
SER21 = pd.Series(data= LIST , index = indecies)
print(SER21)


#0utput
#1        fiza
#4     alishba
#8        zoya
#12     shazma
#16     raheel
#20     Sameer
#dtype: object


# getting values from +ve &-ve positions of index
# 0 positin se value aajati hai
print(SER21.iloc[0])
print(SER21.iloc[2])
print(SER21.iloc[-2])
print(SER21.iloc[-1])

#out put 

#fiza
#zoya
#raheel
#Sameer

# getting values byusing index
print(SER21[4])
print(SER21[8])
print(SER21[16])
# output
#alishba
#zoya
#raheel

#by using s.loc method
print(SER21.loc[4])
print(SER21.loc[8])
print(SER21.loc[16])

# output
#alishba
#zoya
#raheel


# error foe 0 in both because 0 index does not exist
#print(SER21.loc[0])
#print(SER21[0])


# Fancing getting multiple elementbusing list
# from positions
 #Same with zeros
print(SER21[[1,4,8]])
#1       fiza
#4    alishba
#8       zoya
#dtype: object
print(SER21.loc[[1,8,12]])
#1       fiza
#8       zoya
#12    shazma
#dtype: object



# from index
print(SER21.iloc[[0,1,2]])
#1       fiza
#4    alishba
#8       zoya
#dtype: object

# 2nd use og index 
#SELECTION/FILTERING/SUBSETTING OF SERIES OBJECT 
# HAVING INTEGER INDICES

print(SER21[1:12])

#output
####4     alishba
#8        zoya
#12     shazma
#16     raheel
#20     Sameer
#dtype: object
print(SER21.loc[4:16])
#output
##4     alishba
#8        zoya
#12     shazma
#16     raheel
#dtype: object
print(SER21.iloc[0:5])
#output
###1        fiza#
#4     alishba
#8        zoya
#12     shazma
#16     raheel
#dtype: object

#3rd use of index 
# ALIGNMENT
#basic arithmetic operations like addition, subtraction,
#multiplication, division, etc., on two Series objects, to produce a new Series

#EXAMPLE 1:    ADDING TWO SERIES OBJECT WITH 
##                 SAME INTEGER INDICES

LTS1= [1,2,34,5,5]
ind1 = [ 0,1,2,3,4]
SERL1 = pd.Series(data=LTS1 , index = ind1)
print(SERL1)
print(SERL1.index)


LTS2 = [2,4,6,8,10]
ind2 =[0,1,2,3,4]
SERL2 =pd.Series(data=LTS2 , index = ind2)
print(SERL2)
print(SERL2.index)

SERL3 = SERL1 + SERL2
print(SERL3)
print(SERL3.index)
# output
#0     1
#1     2
#2    34
#3     5
##4     5
#dtype: int64
#Index([0, 1, 2, 3, 4], dtype='int64')
#0     2
#1     4
#2     6
#3     8
#4    10
#dtype: int64
#Index([0, 1, 2, 3, 4], dtype='int64')
#0     3
#1     6
#2    40
#3    13
#4    15
#dtype: int64
#Index([0, 1, 2, 3, 4], dtype='int64')



#EXAMPLE 2:      ADDING TWO SERIES OBJECT HAVING 
#                   DIFFERENT INTEGER INDICES


LST1 = [2,4,6,8]
indx1 =[0,2,3,4]
SerL1 = pd.Series(data= LST1 , index = indx1)
print(SerL1)
print(SerL1.index)


LST2 = [1,3,5,7]
indx2 =[0,1,2,3]
SerL2 = pd.Series(data = LST2, index = indx2)
print(SerL2)
print(SerL2.index)

SerL3 = SerL1 +SerL2
print(SerL3)
print(SerL3.index)

#output 
#0    2
#2    4
#3    6
#4    8
#dtype: int64
#Index([0, 2, 3, 4], dtype='int64')
#0    1
#1    3
#2    5
#3    7
#dtype: int64
#Index([0, 1, 2, 3], dtype='int64')
#0     3.0
#1     NaN
#2     9.0
#3    13.0
#4     NaN
#dtype: float64
#Index([0, 1, 2, 3, 4], dtype='int64')




# Now getting the replacement of NaN values
#putting missing values we use
SerL4 = SerL1.add(SerL2,fill_value = 5)
print(SerL4)

#0     3.0
#1     8.0
#2     9.0
#3    13.0
#4    13.0
#dtype: float64