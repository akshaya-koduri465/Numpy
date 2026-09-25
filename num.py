# virtualenvironment?
# how to create a virtual environment?
# py -m venv env
# py-python
# -m python module 
# venv-run the virtual environment module
# env-optional
# py -m venv env
import numpy as np
# creation of arrays?
# 1.array
# a=np.array([10,20,30]) 1d
# print(type(a))
# b=np.array([[10,20,30],[30,40,50]])
# # print(b)
# print(b.ndim)
# print(b.shape)
# print(b.size)
# print(b.dtype)
# creation of arrays
# 2.arange
# Type	Meaning	How to recognize	Example
# Property / Attribute	Tells you what the object is / has	Usually no ()	arr.shape
# Information	Details you get about the object	Usually through attributes/properties	arr.dtype, arr.ndim, arr.size
# Method	An action/function the object can perform	Has ()	arr.reshape()
# creation of arrays
# 2.arange for(start,stop,step) (1,10,1)
# uhitha=np.arange(1,10,1)
# print(uhitha)
# 3.linspace
# c=np.linspace(1,12,4)
# print(c) #(start,stop,12-2 points equal)
# 4.eye
# d=np.eye(3,4)
# print(d)
# e=np.zeros([3,3])
# print(e)
# ones
# Problem 2 — Product Sales Setup

# A company is preparing data for 8 products.

# Create these 5 NumPy arrays:

# Product IDs → numbers from 501 to 508. 
# Product_ID=np.arange(501,509,1)
# print(Product_ID)
# # Product Prices → 8 equally spaced prices from 100 to 450.
# Product_Prices=np.linspace(100,450,8)
# print(Product_Prices)
# Returns → initially every product has 0 returns.
# returns=np.zeros(8)
# print(returns)
# Availability → initially every product has a value of 1.
# availability=np.ones(8)
# print(availability)
# Categories → create an array containing:
# 10, 20, 30, 40
# Categoreies=np.array([10,20,30,40])
# print(Categoreies)

# 💼 NumPy Practice — Sales Analytics

# You are working with a company's monthly sales dataset.

# Create the following NumPy arrays:

# Month numbers → Generate 1 through 12.
# Target sales → Generate 12 equally spaced target values from 50,000 to 1,60,000.
# Actual sales initialization → Create an array of 12 zeros because actual sales haven't been entered yet.
# Performance flag → Create an array of 12 ones as the initial/default status.
# Region codes → Create an array containing the fixed codes:
# 101, 102, 103, 104
# what is numpy
# how the da is ud]sed the numpy 
# creation of numpy arrays and task linkedin post

# indexing -> numpy
# a=np.array([10,20,30,40,50])
# print(a[0])
# print(a[3])
# print(a[-5])
# slicing 
# print(a[1:4:2])
#  indexing 
# uhitha=[10,20,30]
# print(uhitha[0])
# a=np.array([[10,20,30], [40,50,60]])   
# print(a[1,1])
# a=np.arange(1,44,2) 
# print(a)
# print(a.size)
#single row
# print(a)
# [1,2,3,4]
# [5,6,7,8]
# b=a.reshape(2,11)
# b=a.reshape(43,1)
# print(b)
arr=np.array([30,50,60,25,9,21])
print(arr)
print(np.std(arr))
print(np.mode(arr))
# print(np.sum(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.size(arr))











