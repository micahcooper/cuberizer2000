#Cube Class
def _init_(self, startingSet): 
    global myCubesState
    myCubesState = startingSet

def rotateDown(direction, position):
    temporarySet = myCubesState

    if(position == 1):
            myCubesState[1] = temporarySet[37]
            myCubesState[4] = temporarySet[40]
            myCubesState[7] = temporarySet[43]
            myCubesState[46] = temporarySet[1]
            myCubesState[49] = temporarySet[4]
            myCubesState[52] = temporarySet[7]
            myCubesState[43] = temporarySet[21]
            myCubesState[40] = temporarySet[24]
            myCubesState[37] = temporarySet[27]
            myCubesState[21] = temporarySet[52]
            myCubesState[24] = temporarySet[49]
            myCubesState[27] = temporarySet[46]
            myCubesState[30] = temporarySet[28]
            myCubesState[33] = temporarySet[29]
            myCubesState[30] = temporarySet[28]
            myCubesState[31] = temporarySet[35]
            myCubesState[33] = temporarySet[29]
            myCubesState[34] = temporarySet[36]
            myCubesState[35] = temporarySet[33]
            myCubesState[36] = temporarySet[30]
    if(position == 3):
            myCubesState[3] = temporarySet[39]
            myCubesState[6] = temporarySet[42]
            myCubesState[9] = temporarySet[45]
            myCubesState[48] = temporarySet[3]
            myCubesState[51] = temporarySet[6]
            myCubesState[54] = temporarySet[9]
            myCubesState[19] = temporarySet[54]
            myCubesState[22] = temporarySet[51]
            myCubesState[25] = temporarySet[48]
            myCubesState[39] = temporarySet[25]
            myCubesState[42] = temporarySet[22]
            myCubesState[45] = temporarySet[19]
            myCubesState[10] = temporarySet[12]
            myCubesState[11] = temporarySet[15]
            myCubesState[12] = temporarySet[18]
            myCubesState[13] = temporarySet[11]
            myCubesState[15] = temporarySet[17]
            myCubesState[16] = temporarySet[10]
            myCubesState[17] = temporarySet[13]
            myCubesState[18] = temporarySet[16]

def rotateRight(position):
    temporarySet = myCubesState

    if(position == 1):
            myCubesState[1] = temporarySet[37]
            myCubesState[4] = temporarySet[40]
            myCubesState[7] = temporarySet[43]
            myCubesState[46] = temporarySet[1]
            myCubesState[49] = temporarySet[4]
            myCubesState[52] = temporarySet[7]
            myCubesState[43] = temporarySet[21]
            myCubesState[40] = temporarySet[24]
            myCubesState[37] = temporarySet[27]
            myCubesState[21] = temporarySet[52]
            myCubesState[24] = temporarySet[49]
            myCubesState[27] = temporarySet[46]
            myCubesState[30] = temporarySet[28]
            myCubesState[33] = temporarySet[29]
            myCubesState[30] = temporarySet[28]
            myCubesState[31] = temporarySet[35]
            myCubesState[33] = temporarySet[29]
            myCubesState[34] = temporarySet[36]
            myCubesState[35] = temporarySet[33]
            myCubesState[36] = temporarySet[30]
    if(position == 3):
            myCubesState[3] = temporarySet[39]
            myCubesState[6] = temporarySet[42]
            myCubesState[9] = temporarySet[45]
            myCubesState[48] = temporarySet[3]
            myCubesState[51] = temporarySet[6]
            myCubesState[54] = temporarySet[9]
            myCubesState[19] = temporarySet[54]
            myCubesState[22] = temporarySet[51]
            myCubesState[25] = temporarySet[48]
            myCubesState[39] = temporarySet[25]
            myCubesState[42] = temporarySet[22]
            myCubesState[45] = temporarySet[19]
            myCubesState[10] = temporarySet[12]
            myCubesState[11] = temporarySet[15]
            myCubesState[12] = temporarySet[18]
            myCubesState[13] = temporarySet[11]
            myCubesState[15] = temporarySet[17]
            myCubesState[16] = temporarySet[10]
            myCubesState[17] = temporarySet[13]
            myCubesState[18] = temporarySet[16]

def checkState():
    return myCubesState

