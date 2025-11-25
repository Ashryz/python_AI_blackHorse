import numpy as np 
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1, arr2), axis=1)
# arraxi = np.stack((arr1, arr2), axis=0)

# print(arr)
# print(arraxi)

# harr = np.hstack((arr1,arr2))
# print(harr)

# varr = np.vstack((arr1,arr2))
# print(varr)

# darr = np.dstack((arr1, arr2))
# print(darr)

# arr = np.array([1,2,3,4,5,6])
# newarr = np.array_split(arr, 4)
# print(newarr)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.hsplit(arr, 3)
# print(newarr)

# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))

# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# print(arr[x])

############### pandas ########################
import pandas as pd

# print(pd.__version__)

# mydataset = {
#     "cars" : ["BMW", "Volvo", "Ford",["j","l"]],
#     "passings": [3,7,2,[9,8]]
# }
# x = pd.DataFrame(mydataset)
# print(x)

df = pd.read_csv('data.csv')
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.isnull().sum())
df.dropna(inplace=True)
print(df.to_string())
df.fillna(130,inplace=True)
print(df.to_string())
