#Cube Class
class Cube:
    def __init__(self, startingSet):
        print('init: cube created')
        global newState
        self.newState = startingSet

        print("init: cube start state is ",self.newState)
    
    @property
    def checknewState(self):
        return self.newState

    def checkColorAT(self,index):
        return self.newState[index]

    def rotateDown(self, position):
        print("rotate: down ", position)
        originalState = self.newState
        newState = self.newState

        if(position == 1):
            newState[1] = originalState[37]
            newState[4] = originalState[40]
            newState[7] = originalState[43]
            newState[46] = originalState[1]
            newState[49] = originalState[4]
            newState[52] = originalState[7]
            newState[43] = originalState[21]
            newState[40] = originalState[24]
            newState[37] = originalState[27]
            newState[21] = originalState[52]
            newState[24] = originalState[49]
            newState[27] = originalState[46]
            newState[30] = originalState[28]
            newState[33] = originalState[29]
            newState[30] = originalState[28]
            newState[31] = originalState[35]
            newState[33] = originalState[29]
            newState[34] = originalState[36]
            newState[35] = originalState[33]
            newState[36] = originalState[30]

        if(position == 3):
            newState[3] = originalState[39]
            newState[6] = originalState[42]
            newState[9] = originalState[45]
            newState[48] = originalState[3]
            newState[51] = originalState[6]
            newState[54] = originalState[9]
            newState[19] = originalState[54]
            newState[22] = originalState[51]
            newState[25] = originalState[48]
            newState[39] = originalState[25]
            newState[42] = originalState[22]
            newState[45] = originalState[19]
            newState[10] = originalState[12]
            newState[11] = originalState[15]
            newState[12] = originalState[18]
            newState[13] = originalState[11]
            newState[15] = originalState[17]
            newState[16] = originalState[10]
            newState[17] = originalState[13]
            newState[18] = originalState[16]

    def rotateRight(self, position):
        print("rotate: left ", position)
        originalState = self.newState
        newState = self.newState


        if(position == 1):
                newState[1] = originalState[37]
                newState[4] = originalState[40]
                newState[7] = originalState[43]
                newState[46] = originalState[1]
                newState[49] = originalState[4]
                newState[52] = originalState[7]
                newState[43] = originalState[21]
                newState[40] = originalState[24]
                newState[37] = originalState[27]
                newState[21] = originalState[52]
                newState[24] = originalState[49]
                newState[27] = originalState[46]
                newState[30] = originalState[28]
                newState[33] = originalState[29]
                newState[30] = originalState[28]
                newState[31] = originalState[35]
                newState[33] = originalState[29]
                newState[34] = originalState[36]
                newState[35] = originalState[33]
                newState[36] = originalState[30]
        if(position == 3):
                newState[3] = originalState[39]
                newState[6] = originalState[42]
                newState[9] = originalState[45]
                newState[48] = originalState[3]
                newState[51] = originalState[6]
                newState[54] = originalState[9]
                newState[19] = originalState[54]
                newState[22] = originalState[51]
                newState[25] = originalState[48]
                newState[39] = originalState[25]
                newState[42] = originalState[22]
                newState[45] = originalState[19]
                newState[10] = originalState[12]
                newState[11] = originalState[15]
                newState[12] = originalState[18]
                newState[13] = originalState[11]
                newState[15] = originalState[17]
                newState[16] = originalState[10]
                newState[17] = originalState[13]
                newState[18] = originalState[16]


