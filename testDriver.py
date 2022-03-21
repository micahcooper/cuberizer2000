#script for test cases
import cube
import solver
#print(dir(cube))

######test case 1######
testcase1 = list(("r", "g", "w"))
cube1 = cube.Cube(testcase1)
#solver.Solver(cube1)

print( 'test case 1')
print( cube1.currentState )

"""
#####test case 2#######
testcase2 = ["bbrrrwwwgg"]
cube2 = cube.Cube(testcase2)
solver.Solver(cube2)

print( 'test case 2')
print( cube2.currentState )

#####test case 3#######
testcase3 = {'wwwww'}
cube3 = cube.Cube(testcase3)
solver.Solver(cube3)

print( 'test case 3' )
print( cube3.currentState )

#####test case 4#######
testcase4 = {'brg'}
cube4 = cube.Cube(testcase4)
solver.Solver(cube4)

print('test case 4')
print( cube4.currentState )
"""