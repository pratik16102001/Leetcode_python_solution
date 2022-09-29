# Function to merge two sorted arrays
from heapq import merge

def mergeArray(arr1,arr2):
	return list(merge(arr1, arr2))

# Driver function
if __name__ == "__main__":
	arr1 = [1,3,4,5]
	arr2 = [2,4,6,8]
	print (mergeArray(arr1, arr2))
