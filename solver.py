# rubrik cube solver class
import cube

class Solver:
    def __init__(self, incomingCube):
        global cube
        self.cube = incomingCube

    def myLogic(self):
        #rotate cube example
        print('logic:')
        self.cube.rotateDown(1)
        self.cube.rotateRight(3)
        return cube