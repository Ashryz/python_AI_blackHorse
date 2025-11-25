import numpy as np 

# get version 
# print(np.__version__)

# #create an array 

# arr1 = np.array([1,2,3,4,5,6,7,8])
# arr2 = np.array([[1,2,3,4],
#                  [5,6,7,8]])
# arr3 = np.array([[[1,2],
#                   [3,4]],
#                   [[5,6],
#                    [7,8]]])

# print(np.array([1,2,3,4],ndmin=2))
# print(arr1, arr1.ndim)
# print(arr1, arr1.shape)

# print(arr2,arr2.ndim)
# print(arr2,arr2.shape)

# print(arr3,arr3.ndim)
# print(arr3,arr3.shape)


# # get 2nd element in each array

# print(arr1[1])
# print(arr2[0,1])
# print(arr3[0,0,1])

# # loop on array

# for i in np.nditer(arr3):
#     print(i)

# # join 2 arr

# array1 = np.array([1,2,3,4])
# array2 = np.array([5,6,7,8])
# print(np.concatenate((array1,array2)))

# # reshape

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12])
# print(arr.reshape(2, 3, 2))
# print(arr.reshape(3, 2, 2))
