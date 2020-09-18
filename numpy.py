#Create a Null vector (all zeros) of size 10 and set in variable 'Z'

Z = np.zeros(10)

#Create a 1D array of numbers from 0 to 9 and set it in a var called "arr"

arr = np.arange(10)

#Create a 3*3*3 array with random values and set it in variable called "arr"

arr = np.random((3,3,3))

#10*10 array with random values called 'arr4'.Find it min and max value 
arr4 = np.random.random((10,10))
min_val = arr4.min()
max_val = arr4.max()


#First create a 1D array with numbers from 1 to 9 and then convert it into a 3x3 grid. Store the final answer in the variable called “grid”.
grid = np.arange(1,10).reshape((3,3))

#Replace the max value in given vector  "arr6" with -1
arr6 = np.arange(10)
arr6[arr6.argmax()] = -1

#Reverse teh rows of 2D array arr7
arr7= np.arange(9).reshape(3,3)
arr7

#Subtract the mean row of 2D array 'arr8' and rename it to transformed_arr8
arr8 = np.random(3,10)
transformed_arr8 = arr8 - arr8.mean(axis=1,keepdims=True)
