import numpy as np

# BROADCASTING


#REVIEW OF ARITHMETIC OPERATIONS WITH NUMPY ARRAYS OF SAME SHAPE:
#example 1 # 1 to 9 with samesize and random int
AA  = np.random.randint(1,10,size= 5)
AA1 = np.random.randint(1,50,size = 5)
print('AA \n',AA)
print('AA1\n', AA1)

AA2 = AA + AA1
print('addition\n', AA2)
AA3 = AA -AA1
print("Subtraction \n ",AA3 )
# OUTPUT
#AA 
# [9 3 4 7 5]     
#AA1
# [13 21 19 20 21]
#addition
# [22 24 23 27 26]
#Subtraction
#  [ -4 -18 -15 -13 -16]





# example 2  # adding a scalar value a to a numpy 1D array

AA5 = np.random.randint(1,10,size=5)
print('AA5\n ', AA5)
a =2
print('a=',a)
AA6 = AA5 * a
print('AA6\n',AA6)
# output
#AA5
#  [4 6 2 7 6]    
#a= 2
#AA6
# [ 8 12  4 14 12]





# example 3 # 
#      ARITHMETIC OF 2-DIMENSIONAL ARRAY WITH A SCALAR 

A7 = np.array([[1,2,3],[4,5,6]])
print('AA7\n', A7)
b=3
print("b=", b)
AA8 = AA7 *b
print('AA8\n',AA8)
# output
#AA7
# [[1 2 3]   
# [4 5 6]]   
#b= 3        
#AA8
# [[ 3  6  9]
# [12 15 18]]






#ARITHMETIC OF 1-DIMENSIONAL ARRAY WITH A 2-DIMENSIONAL ARRAY
# example # 4 
# #Consider adding a 2-D array (3x4) to a 1-D array with 4 values

AA9 = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])
print('AA9\n',AA9)
AA10 = np.array([2,4,6,8])
print('AA10\n',AA10)
AA11 = AA9 + AA10
print('AA11\n ', AA11)
# out put
#AA9
# [[1 2 3 4]
# [2 3 4 5] 
# [3 4 5 6]]
#AA10      
# [2 4 6 8] 
#AA11
#  [[ 3  6  9 12]
# [ 4  7 10 13]
# [ 5  8 11 14]]








# Example no 5 
#  CONSIDER ADDING A 2-D ARRAY (4X2) TO A 1-D ARRAY WITH 2 VALUES
AA12 = np.array([[1,2],[3,4],[5,6],[7,8]])
print('AA12\n',AA12)
AA13 = np.array([4,4])
print('AA13\n',AA13)
addition13 = AA12 + AA13
print('Addition\n',addition13)
# output
#AA12
# [[1 2]
# [3 4] 
# [5 6] 
# [7 8]]
#AA13   
# [4 4] 
#Addition
# [[ 5  6]
# [ 7  8]
# [ 9 10]
# [11 12]]




# ARITHMETIC OF TWO 2-DIMENSIONAL ARRAYS
# example no 6 
# Consider adding elements of a 2-D array (2x3) with another 2-D array  (3x1)

AA14 = np.array([[3,4,5],[4,2,1],[1,1,1]])
print('AA14\n',AA14)
AA15 = np.array([[1],[2],[3]])
print('AA15\n',AA15)
ADDITION = AA14 + AA15
print('ADDITION\n',ADDITION)
#output
#AA14
# [[3 4 5]
## [4 2 1] 
# [1 1 1]]
#AA15     
# [[1]    
# [2]     
### [3]]
#ADDITION
# [[4 5 6]
# [6 4 3]
# [4 4 4]] 


#ERROR
# (2,3), (1,2) IS ERROR
#(2,3),(1,3) IS NOT ERROR 


# RESHAPPING ARRAY
#np.reshape
# EXAMPLE 1
ARS = np.arange(24)
print('ARS\n',ARS)
print('Dimension\n',ARS.ndim)
print('Shapr\n',ARS.shape)
#2D
NARS =np.reshape(ARS,(6,4))
print('reshape\n',NARS)
print('dimension\n',NARS.ndim)
print('size\n',NARS.size)
# 3D 
nARS = np.reshape(ARS,(2,4,3))
print('nARS\n',nARS)
print('dimension\n',nARS.ndim)
print('Size\n',nARS.size)
# output
#ARS
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
#Dimension
# 1
#Shapr
# (24,)
#reshape
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]
# [12 13 14 15]
# [16 17 18 19]
# [20 21 22 23]]
#dimension  
#2
#size
# 24
#nARS
 #[[[ 0  1  2]
 # [ 3  4  5]
 # [ 6  7  8]
#  [ 9 10 11]]

 #[[12 13 14]
 # [15 16 17]
 # [18 19 20]
 # [21 22 23]]]
#imension
 #3
#size
# 24

# example 2
#RESHAPING FROM 1-D NUMPY ARRAYS TO 2-D NUMPY ARRAYS
A1 = np.array([1,3,5,7])
print('1D Array\n',A1)
print('dimensions\n',A1.ndim)
print('size\n',A1.size)

A2= np.reshape(A1,(2,2))
print('2D array\n',A2)
print('dimension\n', A2.ndim)
print('size\n',A2.size)
# output
#1D Array
# [1 3 5 7]
##dimensions
 #1        
#size      
 #4        
#2D array  
# [[1 3]   
# [5 7]]   
## 2        
#size      
# 4        


# Example 3
#RESHAPING FROM 1-D NUMPY ARRAYS TO 3-D NUMPY ARRAYS

A1D = np.array([1,2,3,4,5,6])
print('A1D\n',A1D)
print('dimension\n',A1D.ndim)
print('size\n',A1D.size)

A2D = np.resize(A1D,(2,2,3))
print('A2D\n',A2D)
print('dimension\n',A2D.ndim)
print('Size\n',A2D.size)
# output
#A1D
# [1 2 3 4 5 6]
#dimension     
# 1
#size
# 6
#A2D
# [[[1 2 3]    
#  [4 5 6]]    
#
# [[1 2 3]     
#  [4 5 6]]]   
#dimension     
# 3
#Size
# 12



#example 4
#FLATTENING ARRAYS. YOU CAN CONVERT AN ARRAY OF AN UNKNOWN 
 # DIMENSION TO A 1D ARRAY USING NP.RESHAPE(-1)
 
 
AA1 = np.array([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]])
print('AA1\n',AA1)
print('dim\n',AA1.ndim)
print('size\n',AA1.size)

AA2 = np.reshape(AA1,(-1))
print('AA1\n',AA2)
print('dim\n',AA2.ndim)
print('size\n',AA2.size)
# output
#AA1
# [[1 2 3 4 5]
# [2 3 4 5 6]
# [3 4 5 6 7]]
#dim
# 2
#size
# 15
#AA1
# [1 2 3 4 5 2 3 4 5 6 3 4 5 6 7]
#dim
# 1
#size
# 15




#4example 5
# again go back to its orignal shape
AA3 = np.resize(AA2,(2,3,5))
print('AA3\n',AA3)
print('AA3\n',AA3)
print('dim\n',AA3.ndim)
print('size\n',AA3.size)
#output
#AA3
# [[[1 2 3 4 5]
#  [2 3 4 5 6]
#  [3 4 5 6 7]]

# [[1 2 3 4 5]
#  [2 3 4 5 6]
#  [3 4 5 6 7]]]
#dim
# 3
#size
# 30


# np.resize()
#CHANGE IN NEW ARRAY DOESN’T REFLECT IN ORIGINAL ARRAY
# same as reshape


# np.transpose()
 # 2D array
A= np.array([[1,2],[3,4],[5,6]])
print('A\n',A)
AT = np.transpose(A)
print('AT\n',AT)

#output
#A
# [[1 2]  
# [3 4]   
# [5 6]]  
#AT       
# [[1 3 5]
# [2 4 6]]

#np.swapaxes ()
#EXAMPLE 1: SWAPPING AXES OF A 2-D ARRAY
SA = np.arange(8).reshape(2,4)
print('SA\n',SA)
S2D =np.swapaxes(SA,0,1)
print('S2D\n',S2D)
# output
#SA
 #[[0 1 2 3]
 #[4 5 6 7]]
#S2D        
 #[[0 4]    
 #[1 5]     
 #[2 6]     
 #[3 7]] 
 
 
# Example 2:EXAMPLE 1: SWAPPING AXES OF A 3-D ARRAY
SA2 = np.arange(8).reshape(2,2,2)
S3D = np.swapaxes(SA2,1,2)
print('S3D\n',S3D)
#S3D
#[[[0 2] 
#  [1 3]] 

# [[4 6]  
 # [5 7]]]


#np.flatten()  flatten in row major order  = C, column flatten = F
Aa = np.arange(8).reshape(2,4)
print('Aa\n',Aa)
# Row major
FAr = Aa.flatten(order='C')
print('FAr\n',FAr)
# row major
FAc = Aa.flatten(order="F")
print('FAc\n',FAc)

#Aa
# [[0 1 2 3]       
# [4 5 6 7]]       
#FAr
# [0 1 2 3 4 5 6 7]
#FAc
# [0 4 1 5 2 6 3 7]



# MANUPULATING
#1. UPDATING EXISTING VALUES OF NUMPY ARRAY ELEMENTS
#a. 1-D Arrays
D1 = np.array([2,4,6,8])
print('orignal array\n',D1)
D1 [1]=1
D1 [3]=3
print('U1D\n',D1)
# output
#orignal array
# [2 4 6 8]
#U1D       
# [2 1 6 3]

#b. 2-D Arrays
D2=np.array([[4,8,12,16],[20,24,28,32]])
print('orignal\n',D2)
D2 [0][2]=1
D2[1][2]=2
print('updated array\n',D2)

#OUTPUT
#orignal
 #[[ 4  8 12 16]
 #[20 24 28 32]]
#updated array  
# [[ 4  8  1 16]
# [20 24  2 32]]


#2 APPENDING        np.append(arr, values, axis=None)
#2. APPEND NEW ELEMENTS TO NUMPY ARRAYS

#a. Appending Elements in 1-D Array
AD1 = np.array([1,1,1,1,1,1])
UAD1=np.append(AD1,[2,2,2,2],axis=None)
print('orignal\n',AD1)
print('appended\n',UAD1) 
# output
#orignal
# [1 1 1 1 1 1]        
#appended
# [1 1 1 1 1 1 2 2 2 2]

#b. Appending Elements in 2-D Arrays
#In case of 2-D Arrays if axis is not mentioned both arr and values are 
#flattened before use
# EAXIX AT END(0,0,Axis)
AD3 = np.array([[1,1,1,1,1,1],[2,2,2,2,2,2]])
UAD3=np.append(AD3,[[3,3,3,3,3,3]])
print('orignal\n',AD3)
print('appended\n',UAD3) 
# output
#orignal
# [[1 1 1 1 1 1]
# [2 2 2 2 2 2]]
#appended       
#  [1 1 1 1 1 1 2 2 2 2 2 2 3 3 3 3 3 3]




#Example: Appending a Row to a 2-D array (axis=0)
DA4= np.array([[2,3,4,4],[1,2,3,4]])
print('2D array\n',DA4)
UDA4=np.append(DA4,[[1,1,1,1]],axis = 0)
print('appended\n',UDA4)
# output
#2D array
 #[[2 3 4 4]
 #[1 2 3 4]]
#appended   
 #[[2 3 4 4]
 #[1 2 3 4] 
 #[1 1 1 1]]
 
 
#Example: Appending a Column to a 2-D array (axis=1)
DA5= np.array([[2,3,4,4],[1,2,3,4]])
print('2D array\n',DA5)
UDA5=np.append(DA5,[[1],[1]],axis = 1)
print('appended\n',UDA5)
# output
#2D array
 #[[2 3 4 4]
 #[1 2 3 4]]
#appended   
 # [[2 3 4 4 1]
 #[1 2 3 4 1]]






#3. INSERT    np.insert(arr, index, values, axis=None)
# #Required index in center (0,INDEX,0)
#INSERTING NEW ELEMENTS IN NUMPY ARRAYS
#a. Inserting Elements in 1-D Arrays
a1 = np.array([2,4,6,8])
print('Orignal\n',a1)
Ia1=np.insert(a1,1,[2,1])
print('inserted\n',Ia1)
#output
#Orignal
# [2 4 6 8]    
#inserted      
# [2 2 1 4 6 8]


#b. Inserting Elements in 2-D  Arrays
#Example: In case of 2-D array, if axis is not mentioned the array is flattened first
a2 =np.array([[1,2,3,4,5],[2,3,4,5,6]])
print('Orignal\n',a2)
Ia2 =np.insert(a2,4,55)
print('insert\n',Ia2)
#output
#Orignal
# [[1 2 3 4 5]
# [2 3 4 5 6]]
#insert
# [ 1  2  3  4 55  5  2  3  4  5  6]


#Example: If axis=0, value(s) are  added as a row before mentioned index
a3 = np.array([[1,2,3],[2,3,4]])
print('Orignal\n',a3)
Ia3= np.insert(a3,0,[[3,4,5]],axis=0)
print('Inserted\n',Ia3)
# output
#Orignal
# [[1 2 3]
# [2 3 4]]
#Inserted 
# [[3 4 5]
# [1 2 3] 
# [2 3 4]]


#Example: If axis=1, value(s) are added as a column at mentioned  index
#a4 = np.array([[1,2,3],[2,3,4]])
print('Orignal\n',a4)
Ia4= np.insert(a4,0,[[3],[4],[5]],axis=1)
print('Inserted\n',Ia4)
# output
#Orignal
# [[1 2 3]      
# [2 3 4]]      
#Inserted       
# [[3 4 5 1 2 3]
# [3 4 5 2 3 4]]

 #DELETED

#4. DELETING ELEMENTS OF NUMPY ARRAYS
#a. Deleting Elements from a 1-D Arrays
#   1 ELEMENT
r1=np.random.randint(1,10,size=5)
print('Orignal\n',r1)
Dr1=np.delete(r1,4)
print('Deleted\n',Dr1)
#output
#Orignal
# [6 5 9 2 3]
#Deleted     
# [6 5 9 2] 


# Or a list (list k given index waley he gaib hon gye)
r2 =np.random.randint(1,100,size=10)
print('Orignal\n',r2)
Dr2=np.delete(r2,[2,5])
print('Deleted\n',Dr2)
#output
#Orignal
# [60 80 80  5 13 57 50 76 35 80]
#Deleted
# [60 80  5 13 50 76 35 80]


#b. Deleting Elements from a 2-D Arrays
#Example: Delete a specific element from a 2-D array, don't mention the axis. The 
#resulting array is flattened before use
r3=np.random.randint(1,100,size=(3,4))
print('orignal\n',r3)
Dr3 = np.delete(r3,7)
print('deleted\n',Dr3)
# output
#orignal
# [[71 25 85 40]
# [56 94 73 29]
# [59 80 35 39]]
#deleted
# [71 25 85 40 56 94 73 59 80 35 39]




#Example: Delete a specific row from an existing 2-D array
r4=np.random.randint(1,100,size=(4,5))
print('orignal\n',r4)
Dr4 = np.delete(r4,2,axis=0)
print('deletes row\n',Dr4)

#Example: Delete a specific column from an existing 2-D array
Dr5=np.delete(r4,2,axis=1)
print('deleted column\n',Dr5)
# output
#orignal
# [[14 15 79 61  6]
# [19 15 94 35 54] 
# [27 20 17 60 48] 
# [34 86 37 70 56]]
#deletes row       
# [[14 15 79 61  6]
# [19 15 94 35 54] 
# [34 86 37 70 56]]
#deleted column
# [[14 15 61  6]
# [19 15 35 54]
# [27 20 60 48]
# [34 86 70 56]]

 
 #5. ASSIGNING VS COPING NUMPY ARRAYS
# a. Assigning two NumPy Arrays (Create an alias)









#Concatination ( joining ) and   Stacking 
#joining and spliting of numpy arrays

# CONCATENATION 
#Concatenate two 1-D Arrays along axis = 0 (row wise). The 1-D arrays can 
#be of any size/length.
arr1 = np.random.randint(low=1,high=100,size=5)
arr2 =np.random.randint(low=1,high=100 , size = 3)
arr3 = np.concatenate((arr1,arr2),axis=0)
print('arr1\n', arr1)
print('arr2\n',arr2)
print('arr3\n',arr3)
# output
#arr1
 #[47 65 57 11 77]
#arr2
# [31 91 51]
#arr3
# [47 65 57 11 77 31 91 51]


#Concatenate two 2-D Arrays along axis=0 (vertically/row-wise). The 
#number of columns of two arrays must match.
arr4 = np.random.randint(1,100,size=(2,3))
arr5 = np.random.randint(1,100,size=(6,3))
arr6=np.concatenate((arr4,arr5),axis=0)
print('arr4\n',arr4)
print('arr5\n',arr5)
print('arr6\n',arr6)
#output
#arr4
 #[[18 68 88]
# [31 55 62]]
#arr5
# [[96 59 36]
 #[42 24 57]
 #[60 95 25]
 #[19  4 73]
 #[54 53 77]
 #[48 95 44]]
#arr6
# [[18 68 88]
## [31 55 62]
 #[96 59 36]
# [42 24 57]
# [60 95 25]
 #[19  4 73]
# [54 53 77]
# [48 95 44]]




#Concatenate two 2-D Arrays along axis=1 (horizontally/column-wise). The 
#number of rows of two arrays must match.
arr7 = np.random.randint(1,100,size = (2,3))
arr8 = np.random.randint(1,100,size=(2,4))
arr9=np.concatenate((arr7,arr8),axis =1)
print('arr7\n',arr7)
print("arr8\n",arr8)
print("arr9\n",arr9)
#output
#arr7
# [[75  1 92]
# [28 57 66]]
#arr8
# [[91 91 87 42]
# [92  9 74  5]]
#arr9
# [[75  1 92 91 91 87 42]
# [28 57 66 92  9 74  5]]



# STACKING ( basically its a transpose type of thing)
# 1) row or column_stack
Arr1 = [1,2,3]
Arr2= [4,5,6]
StR_Arr3 =np.row_stack((Arr1,Arr2))
print('Arr1\n',Arr1)
print('Arr2\n',Arr2)
print('StR_Arr3\n',StR_Arr3)
# output
#Arr1
# [1, 2, 3]
#Arr2
# [4, 5, 6]
#StR_Arr3
 #[[1 2 3]
 #[4 5 6]]
StC_Arr3=np.column_stack((Arr1,Arr2))
print('StC_Arr3\n',StC_Arr3)
#output
#StC_Arr3
# [[1 4]
# [2 5]
# [3 6]]


#2) hstack
#Perform horizontal stacking of two 1-D Arrays, which can be of different 
# size/length

arra1= np.random.randint(1,100,size=4)
arra2=np.random.randint(1,100,size=2)
arra3=np.hstack((arra1,arra2))
print('arra1\n',arra1)
print('arra2\n',arra2)
print('Stacked Array\n',arra3)

# output
#arra1
# [35 79  2 33]
#arra2
# [ 6 46]
#Stacked Array
# [35 79  2 33  6 46]

# Perform horizontal stacking of two 2-D Arrays. The number of rows of two 
# arrays must match
a1=np.random.randint(1,100,size=(2,3))
a2 = np.random.randint(1,100,size=(2,4))
a3 = np.hstack((a1,a2))
print('a1\n',a1)
print('a2\n',a2)
print('a3\n',a3)
#output
#a1
# [[ 1 39 48]
# [91  7 86]]
#a2
# [[37 22 87 72]
# [66  6 16  2]]
#a3
# [[ 1 39 48 37 22 87 72]
# [91  7 86 66  6 16  2]]

