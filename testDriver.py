#script for test cases
import cube
import solver

######test case 1######
testcaseSet1 = {'rbgwy'}
cube1 = cube(testcaseSet1)
solver(cube1)

print( 'test case 1')
print( cube1.currentSet() )

#####test case 2#######
testcaseSet2 = {'bbrrrwwwgg'}
cube2 = cube(testcaseSet2)
solver(cube2)

print( 'test case 2')
print( cube2.currentSet() )

#####test case 3#######
testcaseSet3 = {'wwwww'}
cube3 = cube(testcaseSet2)
solver(cube3)

print( 'test case 3' )
print( cube3.currentSet() )

#####test case 4#######
testcaseSet4 = {'brg'}
cube4 = cube(testcaseSet2)
solver(cube4)

print('test case 4')
print( cube4.currentSet() )