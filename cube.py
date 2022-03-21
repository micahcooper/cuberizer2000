#Cube Class

class Cube:
    def __init__(self,startingSet):
        print('initializing the cube')
        global cubeState
        cubeState = startingSet
        print("cube starting state is ",cubeState)

    def rotateDown(self, direction, position):
        print("rotate down")
        temporarySet = self.cubeState

        if(position == 1):
                cubeState[1] = temporarySet[37]
                cubeState[4] = temporarySet[40]
                cubeState[7] = temporarySet[43]
                cubeState[46] = temporarySet[1]
                cubeState[49] = temporarySet[4]
                cubeState[52] = temporarySet[7]
                cubeState[43] = temporarySet[21]
                cubeState[40] = temporarySet[24]
                cubeState[37] = temporarySet[27]
                cubeState[21] = temporarySet[52]
                cubeState[24] = temporarySet[49]
                cubeState[27] = temporarySet[46]
                cubeState[30] = temporarySet[28]
                cubeState[33] = temporarySet[29]
                cubeState[30] = temporarySet[28]
                cubeState[31] = temporarySet[35]
                cubeState[33] = temporarySet[29]
                cubeState[34] = temporarySet[36]
                cubeState[35] = temporarySet[33]
                cubeState[36] = temporarySet[30]
        if(position == 3):
                cubeState[3] = temporarySet[39]
                cubeState[6] = temporarySet[42]
                cubeState[9] = temporarySet[45]
                cubeState[48] = temporarySet[3]
                cubeState[51] = temporarySet[6]
                cubeState[54] = temporarySet[9]
                cubeState[19] = temporarySet[54]
                cubeState[22] = temporarySet[51]
                cubeState[25] = temporarySet[48]
                cubeState[39] = temporarySet[25]
                cubeState[42] = temporarySet[22]
                cubeState[45] = temporarySet[19]
                cubeState[10] = temporarySet[12]
                cubeState[11] = temporarySet[15]
                cubeState[12] = temporarySet[18]
                cubeState[13] = temporarySet[11]
                cubeState[15] = temporarySet[17]
                cubeState[16] = temporarySet[10]
                cubeState[17] = temporarySet[13]
                cubeState[18] = temporarySet[16]

    def rotateRight(position):
        print("rotate left")
        temporarySet = cubeState

        if(position == 1):
                cubeState[1] = temporarySet[37]
                cubeState[4] = temporarySet[40]
                cubeState[7] = temporarySet[43]
                cubeState[46] = temporarySet[1]
                cubeState[49] = temporarySet[4]
                cubeState[52] = temporarySet[7]
                cubeState[43] = temporarySet[21]
                cubeState[40] = temporarySet[24]
                cubeState[37] = temporarySet[27]
                cubeState[21] = temporarySet[52]
                cubeState[24] = temporarySet[49]
                cubeState[27] = temporarySet[46]
                cubeState[30] = temporarySet[28]
                cubeState[33] = temporarySet[29]
                cubeState[30] = temporarySet[28]
                cubeState[31] = temporarySet[35]
                cubeState[33] = temporarySet[29]
                cubeState[34] = temporarySet[36]
                cubeState[35] = temporarySet[33]
                cubeState[36] = temporarySet[30]
        if(position == 3):
                cubeState[3] = temporarySet[39]
                cubeState[6] = temporarySet[42]
                cubeState[9] = temporarySet[45]
                cubeState[48] = temporarySet[3]
                cubeState[51] = temporarySet[6]
                cubeState[54] = temporarySet[9]
                cubeState[19] = temporarySet[54]
                cubeState[22] = temporarySet[51]
                cubeState[25] = temporarySet[48]
                cubeState[39] = temporarySet[25]
                cubeState[42] = temporarySet[22]
                cubeState[45] = temporarySet[19]
                cubeState[10] = temporarySet[12]
                cubeState[11] = temporarySet[15]
                cubeState[12] = temporarySet[18]
                cubeState[13] = temporarySet[11]
                cubeState[15] = temporarySet[17]
                cubeState[16] = temporarySet[10]
                cubeState[17] = temporarySet[13]
                cubeState[18] = temporarySet[16]

    def currentState():
        print(cubeState)

