import numpy as np
# Multiple conditions.
# salary=np.array([40000,55000,70000,80000])
# # print(salary[[0,2,3]]) 
# age=np.array([22,28,31,35])
# res=(salary>50000) & (age>=30)
# print(salary[res])
# print(res)

#Fancy Indexing
# salary=np.array([40000,55000,70000,80000])
# print(salary[[0,2,3]]) ->list is nothing but collection of elements
# when we need two or more elements to extract with helpof indexing we use list because it say collection of elements
# where
# return postions where the condition is true...

# salary=np.array([25000,30000,48000,120000,20000])
# print(np.where(salary>=30000))
# print(salary[val])



# copy vs view
# u=np.array([1,2,3]) #original 
# a=u.copy() #copy orders->higher order chck original loss chance 
# print(a)
# a[0]=31
# u[0]=24
# print(a)
# print(u)
# View

# a=np.array([9,11,5,24,31])
# b=a.view()
# b[0]=100
# print(a)
# print(b)

employees=np.array([[101,25,45000],
                     [102,30,60000]])

print(employees[0,0])
print(employees[employees[:,1]>50000])














