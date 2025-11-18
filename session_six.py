import numpy as np 

print(f"version: {np.__version__}")

arr_0 = np.array(42)
print(f"Type: {type(arr_0)}")
print(arr_0)
print(f"Dimensions: {arr_0.ndim}")

arr_1 = np.array([1,2,3,4])
print(arr_1)
print(f"Dimensions: {arr_1.ndim}")


arr_2 = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
print(arr_2)
print(f"Dimensions: {arr_2.ndim}")
print(f"Shape: {arr_2.shape}")

arr_3 = np.array([[[1, 2, 3], [4, 5, 6]],
                 [[1, 2, 3], [4, 5, 6]]])
print(arr_3)
print(f"Dimensions: {arr_3.ndim}")
print(f"Shape: {arr_3.shape}")

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('4th element on 1st row: ', arr[0, 3])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z)
      
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
  

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)