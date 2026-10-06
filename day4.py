import numpy as np
# percentile
# qaunatile
# 82%-->100-82=18->better 100 -> 55% ->poor below
# quantile ->eqqual dividing


# day4
# dtype->datatype
# what is meantby
# to perform and to check which datatype
# type conversion
# astype
# a=np.array([10,20,30,40]) #thiskelluarray dtype int64
# print(a.dtype)
# b=a.astype(float)
# print(b.dtype)

# out
# a=np.array([10,20,30]) #array creat
# result=a*2  #mathematical operation variable"result""
# print(result) 


# with out parameter  
#  empty function 
# a=np.array([10,20,30]) 
# result=np.empty(3) -#->arbitary array creation memory save save when the orignal values replace arbitary values
# np.multiply(a,2,out=result) 
# print(result) 

# the out parameter allows us to store th operation results(mathematical operations) 
# already existing array this can reduce unecessary temporary array 


# flipkart
# day1=sales,sum=,min=,max=  one product 
# day2=sales sum=,min,max  salay a b 
# day3=sales sum,min ,max,count


# a=np.array([])
# res=np.min(a,initial=10)
# print(res)

# # linspace
# where
# arange
# empty identity axis

# axis?
# axis=0 down coloumn
# axis=1 row horizontal

# dtype is nothing datatype->int64,float,int8
# a=np.array([10,20,30],dtype=float)  #-> float to int converted
# print(a.astype(int))


# initial
# 500 records day1 ->sales price,profit,quantity,person->3,10
# 250 records day2 ->sales person->4,8
# day 3? minimum ennin orders person orders flipkart 
# initial 
# like parameter..
# init=np.array([70,90,400])
# print(np.min(init))
# print(np.min(init,initial=50))
# print(init)

# linspace->enpoint,retstep
# nums=np.linspace(0,100,5,retstep=True)
# print(nums)
# endpoint=False 100 0->start,100->stop,5->equal parts divided
# print(np.linspace(0,100,5,endpoint=False,retstep=True))
# retstep=differnce between the elements
# endpoint=no endpoint by default it is true if we need False

# keepdims=True
# is nothing but the after some mathematical
# operations also we are keeping the same dimension
# a=np.array([[10,20,30],  #2d 
#             [40,50,60]])
# print(a.mean(axis=1)) [20,50] #2d->1D ml model-> algorithm 2d
# print(a.mean(axis=1,keepdims=True)) 

# broadcasting?
# must be one row or coloumn same in both 2d or 3d array
# and the broadcasting will check the compatible.->is they are work together
# salary=np.array([20000,45000,50000,65000])
# b = salary + 5000
# print(b)
# a=(2,3)
# b=(1,4)
# a=np.array([[10,20,30],
#             [40,50,60]]) #2d array
# b=np.array([[1,2,5],
#             [2,5,6,]]) #1d array
# print(a+b) equal coloumns,arows 


# transpose
# a=np.array([[10,20,30],
#            [40,50,60]])
# print(np.transpose(a)) #rows to coloumns and coloums to rows

# concatenate
# a=np.array([[10,20,30],
#             [40,50,60]])
# b=np.array([[1,2,5],
#             [2,5,6,]])
# c=np.concatenate((a,b)) #vertical adding two arrays 
# print(np.hstack((a,b))) #hstack side by side x-axis
# print(np.vstack((a,b))) #y-axis

# otp
# spli
# random
# broadcasting vs vectorization
# pamdas introduction
































































































































