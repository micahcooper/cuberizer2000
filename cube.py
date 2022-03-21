#Cube Class
class Cube:
    def __init__(self, startingSet):
        print('init: cube created')
        global cubeState
        self.cubeState = startingSet

        print("init: cube start state is ",self.cubeState)
    
    @property
    def checkCubeState(self):
        return self.cubeState

    def checkColorAT(self,index):
        return self.cubeState[index]

    def rotateDown(self, position):
        print("rotate: down ", position)
        temporaryState = self.cubeState

        if(position == 1):
            cubeState[1] = temporaryState[37]
            cubeState[4] = temporaryState[40]
            cubeState[7] = temporaryState[43]
            cubeState[46] = temporaryState[1]
            cubeState[49] = temporaryState[4]
            cubeState[52] = temporaryState[7]
            cubeState[43] = temporaryState[21]
            cubeState[40] = temporaryState[24]
            cubeState[37] = temporaryState[27]
            cubeState[21] = temporaryState[52]
            cubeState[24] = temporaryState[49]
            cubeState[27] = temporaryState[46]
            cubeState[30] = temporaryState[28]
            cubeState[33] = temporaryState[29]
            cubeState[30] = temporaryState[28]
            cubeState[31] = temporaryState[35]
            cubeState[33] = temporaryState[29]
            cubeState[34] = temporaryState[36]
            cubeState[35] = temporaryState[33]
            cubeState[36] = temporaryState[30]

        if(position == 3):
            cubeState[3] = temporaryState[39]
            cubeState[6] = temporaryState[42]
            cubeState[9] = temporaryState[45]
            cubeState[48] = temporaryState[3]
            cubeState[51] = temporaryState[6]
            cubeState[54] = temporaryState[9]
            cubeState[19] = temporaryState[54]
            cubeState[22] = temporaryState[51]
            cubeState[25] = temporaryState[48]
            cubeState[39] = temporaryState[25]
            cubeState[42] = temporaryState[22]
            cubeState[45] = temporaryState[19]
            cubeState[10] = temporaryState[12]
            cubeState[11] = temporaryState[15]
            cubeState[12] = temporaryState[18]
            cubeState[13] = temporaryState[11]
            cubeState[15] = temporaryState[17]
            cubeState[16] = temporaryState[10]
            cubeState[17] = temporaryState[13]
            cubeState[18] = temporaryState[16]

    def rotateRight(self, position):
        print("rotate: left ", position)
        temporaryState = cubeState

        if(position == 1):
                cubeState[1] = temporaryState[37]
                cubeState[4] = temporaryState[40]
                cubeState[7] = temporaryState[43]
                cubeState[46] = temporaryState[1]
                cubeState[49] = temporaryState[4]
                cubeState[52] = temporaryState[7]
                cubeState[43] = temporaryState[21]
                cubeState[40] = temporaryState[24]
                cubeState[37] = temporaryState[27]
                cubeState[21] = temporaryState[52]
                cubeState[24] = temporaryState[49]
                cubeState[27] = temporaryState[46]
                cubeState[30] = temporaryState[28]
                cubeState[33] = temporaryState[29]
                cubeState[30] = temporaryState[28]
                cubeState[31] = temporaryState[35]
                cubeState[33] = temporaryState[29]
                cubeState[34] = temporaryState[36]
                cubeState[35] = temporaryState[33]
                cubeState[36] = temporaryState[30]
        if(position == 3):
                cubeState[3] = temporaryState[39]
                cubeState[6] = temporaryState[42]
                cubeState[9] = temporaryState[45]
                cubeState[48] = temporaryState[3]
                cubeState[51] = temporaryState[6]
                cubeState[54] = temporaryState[9]
                cubeState[19] = temporaryState[54]
                cubeState[22] = temporaryState[51]
                cubeState[25] = temporaryState[48]
                cubeState[39] = temporaryState[25]
                cubeState[42] = temporaryState[22]
                cubeState[45] = temporaryState[19]
                cubeState[10] = temporaryState[12]
                cubeState[11] = temporaryState[15]
                cubeState[12] = temporaryState[18]
                cubeState[13] = temporaryState[11]
                cubeState[15] = temporaryState[17]
                cubeState[16] = temporaryState[10]
                cubeState[17] = temporaryState[13]
                cubeState[18] = temporaryState[16]


