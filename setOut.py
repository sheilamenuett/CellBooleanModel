from pyeda.inter import *
def setUpLayoutViaFromResult(result, layout, subnetRec, NumberOfNets, ):
        numOfVar = 0
        for netIndex in range(NumberOfNets):
                tempNetID = netIndex+1
                for v, val in sorted(result.items()):
                    numOfVar = numOfVar + 1
                    if v.name == 'edge_net_subnet{}'.format(tempNetID):
                        if val == 1:
                                tempS = str(v)
                                subIndex = tempS.find("subnet")+6
                                preIndex = tempS.find('[')+1
                                endIndex = tempS.find(']')
                                NetID = int(tempS[subIndex:preIndex-1])
                                tempSplit = tempS[preIndex:endIndex]
                                spS = tempSplit.split(',')
                                x = int(spS[0])
                                y = int(spS[1])
                                z = int(spS[2])
                                trend = int(spS[3])
                                mask = int(spS[4])
                                subNet = spS[5]
                                if (z == 0 and mask == 2) or (z == 1 and mask == 2) or (z == 2 and mask == 0) or (z == 3 and mask == 0):
                                    layout[x][y][z][trend] = NetID
                                    subnetRec[x][y][z][trend] = int(subNet)
        print("#Var = ", numOfVar)

def ResultToText_V2(layout, maxX, maxY, maxZ):
    [x,y,z]=[0,0,0]
    [round,trend]=[0,2]
    for z in range(maxZ+1) :
        print('\nLayer', z)
        for y in range(maxY+1) :
            print(y, end = '\t')
            for x in range(maxX+1):
                for round in range(1+1) :
                    # set trend by round
                    if round == 0 : trend = 2
                    elif round == 1 : trend = 1
                    if layout[x][y][z][trend] > 0 :
                        if trend == 2 : print('*', end = '')
                        elif trend == 1 : print(layout[x][y][z][trend], end = '')
                    if layout[x][y][z][trend] == 0 :
                        if trend == 2 : print('.',end = '')
                        else: print('─', end = '')
            print('\n', end='\t')
            for x in range(maxX+1):
                #print('[',x, ',',y,']', end = '')
                [round,trend] = [4,0]
                if layout[x][y][z][trend] > 0 :
                    print(layout[x][y][z][trend], end = ' ')
                else:  print('|', end = ' ')
            print('\n', end='')


#setUpLayoutViaFromResult(AND2_X1_DFINH_0525.FORMULA.satisfy_one(), AND2_X1_DFINH_0525.outLayout, AND2_X1_DFINH_0525.subnetRec, 4)
#ResultToText_V2(AND2_X1_DFINH_0525.outLayout, 26-1, 36-1, 4-1)


def ResultToText_Specfied(layout, subnetRec, maxX, maxY, maxZ, NetID, SubnetID):
    [x,y,z]=[0,0,0]
    [round,trend]=[0,2]
    for z in range(maxZ+1) :
        print('\nLayer', z)
        for y in range(maxY+1) :
            print(y, end = '\t')
            for x in range(maxX+1):
                for round in range(1+1) :
                    # set trend by round
                    if round == 0 : trend = 2
                    elif round == 1 : trend = 1
                    #===Test Region start
                    #if layout[x][y][z][trend] == NetID and subnetRec[x][y][z][trend] == SubnetID : print('+', end = '')
                    #else : print(subnetRec[x][y][z][trend], end = '')
                    #===Test Region end
                    if layout[x][y][z][trend] == NetID and  subnetRec[x][y][z][trend] == SubnetID :
                        if trend == 2 : print('*', end = '')
                        elif trend == 1 : print(layout[x][y][z][trend], end = '')
                    else :
                        if trend == 2 : print('.',end = '')
                        else: print('─', end = '')
            print('\n', end='\t')
            for x in range(maxX+1):
                #print('[',x, ',',y,']', end = '')
                [round,trend] = [4,0]
                if layout[x][y][z][trend] == NetID and  subnetRec[x][y][z][trend] == SubnetID :
                    print(layout[x][y][z][trend], end = ' ')
                else:  print('|', end = ' ')
            print('\n', end='')


#ResultToText_Specfied(AND2_X1_DFINH_0524.outLayout, AND2_X1_DFINH_0524.subnetRec, 26-1, 36-1, 4-1, 1,2)




def ResultToText(layout, maxX, maxY, maxZ):
    [x,y,z]=[0,0,0]
    [round,trend]=[0,2]
    for z in range(maxZ+1) :
        print('\nLayer', z)
        for y in range(maxY+1) :
            print(y, end = '\t')
            for x in range(maxX+1):
                #print('[',x, ',',y,']', end = '')
                #if round != 4 :
                for round in range(1+1) :
                    # set trend by round
                    if round == 0 : trend = 2
                    elif round == 1 : trend = 1
                    if layout[x][y][z][trend] > 0 :
                        if trend == 2 : print('*', end = '')
                        elif trend == 1 : print(layout[x][y][z][trend], end = '')
                    if layout[x][y][z][trend] == 0 :
                        if trend == 2 : print('.',end = '')
                        else: print(' ', end = '')
            print('\n', end='\t')
            for x in range(maxX+1):
                #print('[',x, ',',y,']', end = '')
                [round,trend] = [4,0]
                if layout[x][y][z][trend] > 0 :
                    print(layout[x][y][z][trend], end = ' ')
                else:  print(' ', end = ' ')
            print('\n', end='')







def ResultToText_V3(layout, maxX, maxY, maxZ):
    [x,y,z]=[0,0,0]
    [round,trend]=[0,2]
    for z in range(maxZ+1) :
        print('\nLayer', z)
        for y in range(maxY+1) :
            print(y, end = '\t')
            for x in range(maxX+1):
                for round in range(1+1) :
                    # set trend by round
                    if round == 0 : trend = 2
                    elif round == 1 : trend = 1
                    if layout[x][y][z][trend] > 0 :
                        if trend == 2 : print('*', end = '\t')
                        elif trend == 1 : print(layout[x][y][z][trend], end = '\t')
                    if layout[x][y][z][trend] == 0 :
                        if trend == 2 : print('.',end = '\t')
                        else: print('─', end = '\t')
            print('\n', end='\t')
            for x in range(maxX+1):
                #print('[',x, ',',y,']', end = '')
                [round,trend] = [4,0]
                if layout[x][y][z][trend] > 0 :
                    print(layout[x][y][z][trend], end = '\t')
                else:  print('|', end = '\t')
            print('\n', end='')

#ResultToText_V3(outLayout, 26-1, 36-1, 4-1)

def clauseDistribution(formula):
        # index 0 => #literal=1 | index 1 => #literal=2 | index 2=> #literal=3 | index 3=> #literal>=4
        orHeader = False
        cnt = [0 for x in range(4)]
        tempOut = ""
        if formula.is_cnf() == False:
                print("Formulation: {} does not CNF!")
        else:
                #print(cnt)
                tempS = str(formula)
                tempSP = str.split(tempS, ", ")
                tempCnt = 0
                for temp in tempSP:
                        if temp.count("Or(") > 0:
                                orHeader = True
                                tempCnt = tempCnt + 1
                        elif temp.count(")") > 0:
                                tempCnt = tempCnt + 1
                                orHeader = False
                                #print ("{} => {}".format(tempCnt, temp))
                                if tempCnt >= 4:
                                        #print (temp)
                                        cnt[3] = cnt[3] + 1
                                else:
                                        #print (temp)
                                        cnt[tempCnt-1] = cnt[tempCnt-1] + 1
                                tempCnt = 0
                        else:
                                if orHeader:
                                        tempCnt = tempCnt + 1
                                else:
                                        tempCnt = 0
                                        cnt[0] = cnt[0] + 1

                total = 0
                for num in range(len(cnt)):
                        total = total + cnt[num]

                for num in range(len(cnt)):
                        if num+1 >=4:
                                print( "#literals>{} = {} , {}".format((num+1) , cnt[num], round((cnt[num]/total),3) ) )
                        else:
                                print( "#literals {} = {} , {}".format((num+1) , cnt[num], round((cnt[num]/total),3) ) )
                        tempOut = tempOut + "{}\t".format(round((cnt[num]/total),3))
                print( "#Clauses = {}".format(total) )
                tempOut = tempOut + "{}\t".format( total )
                return tempOut



def ResultToTxt(Result, fileName):
        f = open(fileName + "_outLayout.txt", 'w' )
        for zSize in range(len(Result[0][0])):
                for xSize in range(len(Result)):
                        for ySize in range(len(Result[0])):
                                for tSize in range(len(Result[0][0][0])):
                                        if Result[xSize][ySize][zSize][tSize]  >  0 :
                                                #f.write("outLayout[" + str(xSize) + "][" + str(ySize) + "][" + str(zSize) + "][" + str(tSize) + "]=" + str(Result[xSize][ySize][zSize][tSize]), 'w', newLine = "\n")
                                                f.write("outLayout[{}][{}][{}][{}]={}\n".format(xSize,ySize,zSize,tSize,Result[xSize][ySize][zSize][tSize]))



