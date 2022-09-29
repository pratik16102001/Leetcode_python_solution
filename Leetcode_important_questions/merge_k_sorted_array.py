# Python3 program to merge k sorted arrays of size n each.

# This function takes an array of arrays as an argument
# and
# All arrays are assumed to be sorted. It merges them
# together and prints the final sorted output.


def mergeKArrays(arr, a, output):
	c = 0

	# traverse the matrix
	for i in range(a):
		for j in range(4):
			output = arr[i][j]
			c += 1

	# sort the array
	output.sort()

# A utility function to print array elements


def printArray(arr, size):
	for i in range(size):
		print(arr[i], end=" ")


# Driver's code
if __name__ == '__main__':
	arr = [[2, 6, 12, 34], [1, 9, 20, 1000], [23, 34, 90, 2000]]
	K = 4
	N = 3
	output = [0 for i in range(N * K)]

	# Function call
	mergeKArrays(arr, N, output)

	print("Merged array is ")
	printArray(output, N * K)

# This code is contributed by umadevi9616
