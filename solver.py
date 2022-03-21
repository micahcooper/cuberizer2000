# rubrik cube solver class
import cube

class Solver:
    def __init__(self, incomingCube):
        global cube
        cube = incomingCube

    def myLogic():
        #rotate cube example
        cube.rotateDown(1)
        cube.rotateRight(3)
        return cube