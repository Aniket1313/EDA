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
