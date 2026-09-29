import numpy as np
# empty memory allocate for the array but does not intialize the zero or other values
# result=np.empty(5) #image processing,ml preprocessing,scientific computoing
# print(result)
# for i in range(5):
#     result[i] = i * 2
# print(result)
# full
# 3X3 ==31
# a=np.full((3,3),31)
# print(a) #full((number of rows,number of coloumnns),which element we need to fill)
# i=np.identity(3)
# print(i)
# Vectorization->mean sperforming an operation on many values at once
# for loop->using a loop to process each value one by one
# salary=np.array([10000,35000,28000,52000,31000])
# new value=original X (1+percentage/100)
# new value = original X (1+10/100)-> 1+0.10
# new_salary=salary * 1.10
# print(new_salary)
# salary=np.array([10000,35000,28000,52000,31000])
# new_salary=[]
# for s in salary:
#     new_salary.append(s * 1.10)
# print(new_salary)

# day_3
# arethematic-> means the mathematicl performances
# +,-,*,%

# a=np.array([[10,20],        
#             [30,40]])   

# b=np.array([[1,2],
#            [3,4]])
# c=a+b
# # print(c) #axis=0 coloumn always
# print(np.sum(c,axis=1))



# axis****->it tells numpy whic direction to perfor, the operation on a single or multidimemsional.. x,y
# x->horizontal=1
# y->vertical=0
# u=np.array([[1,2,3],
#            [4,5,6]])
# print(np.sum(u,axis=1))

# aggregate functions
# min,max.mean,median,sum,std,var
# stats=mean,median, mean=10,20,30,40 mean =20 variance,std devi,
# # 25%,50%,75% quartile 25%,50%,75%,100% -
# a=np.array([10,20,30,40,50])
# print(np.mean(a))
# print(np.var(a))
# print(np.std(a))
# # print(np.percentile(a,50))
# # print(np.quantile(a,1))

# sorting         0     1     2     3     4  
# salary=np.array([10000,35000,28000,52000,31000])
# print(np.sort(salary))
# print(np.argsort(salary))  
  
# :->all rows             0   1   2
# employees=np.array([   [101,25,45000], 
#                         [102,29,55000], 
#                         [103,24,48000],
#                         [104,32,70000]]) 
# print(employees[:,0])  #:-> consider, 0 coloukmn (2,3) 2 rows 3 coloumns
# print(employees[:,2])
# print(employees[employees[:,2]>50000] & employees[employees[:,1]>25])


























