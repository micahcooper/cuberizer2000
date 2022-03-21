#script for test cases
import cube
import solver

#test case 1
testcaseSet1 = {'rbgwy'}
cube1 = cube(testcaseSet1)
solver(cube1)

print( cube1.currentSet() )