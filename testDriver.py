#script for test cases
import cube
import solver
#print(dir(cube))

print('')
print('=====TEST ONE=====')

######test case 1######
testcase1 = list(("r", "g", "w"))
cube1 = cube.Cube(testcase1)
for x in range(3):
    print('run: check position ', x, cube1.checkColorAT(x))
    
solver.Solver(cube1)


print( 'last: state ', cube1.checkCubeState )
print('==================')
print('')
