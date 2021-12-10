import numpy
# retrieve an randome values array
# all of vlaues less or equal 1 
# rand(size) , rand(sizex, sizey)
rand = numpy.random.rand(2,3)

print(rand)

# retrieve an randome value or array of randome int num bers
# all of values  is int  
# randint(min, max, numberOfElements(size))
randint = numpy.random.randint(0, 100,(2,5))
print(randint)