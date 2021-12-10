import numpy

arr = numpy.arange(10)

# to convert the array or matrix to another formate 
# array.resahpe(sizex, sizey)
# the array size must equal  sizex * sizey
shape = arr.reshape(5,2)
print(shape)
