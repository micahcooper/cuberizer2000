#script for test cases
import cube
import solver
#print(dir(cube))

print('')
print('=====TEST ONE=====')

######test case 1######
testcase1 = list(("r","r","g","b","w","w","b","r","g","b","w","w","b","r","g","b","w","w","b","r","g","b","w","w","b","r","g","b","w","w","b","r","g","b","w","w","b","r","g","b","w","w","b","r","g","b","w","w","b","r","g","b","w","w","b"))
cube1 = cube.Cube(testcase1)
for x in range(3):
    print('run: check position ', x, cube1.checkColorAT(x))

braniac = solver.Solver(cube1)
braniac.myLogic()


print( 'last: state ', cube1.checknewState )
print('==================')
print('')
