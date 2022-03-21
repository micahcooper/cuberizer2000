# rubrik cube solver class
import cube

def _init_(self, incomingCube):
    global cube
    cube = incomingCube

def myLogic():
    #rotate cube example
    cube.rotateDown(1)
    cube.rotateRight(3)
    return cube