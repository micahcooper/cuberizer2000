#script for test cases
import cube
import solver
print(dir(cube))

######test case 1######
testcaseSet1 = {'rbgwy'}
cube1 = cube.Cube(testcaseSet1)
solver.Solver(cube1)

print( 'test case 1')
print( cube1.currentSet() )

#####test case 2#######
testcaseSet2 = {'bbrrrwwwgg'}
cube2 = cube.Cube(testcaseSet2)
solver.Solver(cube2)

print( 'test case 2')
print( cube2.currentSet() )

#####test case 3#######
testcaseSet3 = {'wwwww'}
cube3 = cube.Cube(testcaseSet2)
solver.Solver(cube3)

print( 'test case 3' )
print( cube3.currentSet() )

#####test case 4#######
testcaseSet4 = {'brg'}
cube4 = cube.Cube(testcaseSet2)
solver.Solver(cube4)

print('test case 4')
print( cube4.currentSet() )