import numpy

# shuffle is a method to randomize the array (marieses ) 
arr = numpy.random.randint(0,10,(4,4))
numpy.random.shuffle(arr)

print(arr)
