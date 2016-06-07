from pyeda.inter import *
def R1(VarName, Terminal, NumOfTerminal, minX, minY, minZ, maxX, maxY, maxZ, sn) :
  print('Enter RConstraints.R1\n')
  print('input Terminal is',Terminal,'\n')
  print('There are ',NumOfTerminal,' edges here')
  global indexOfExt
  [x_base,y_base,z_base,t_base,m_base]=[0,0,0,0,0]
  [count,countT,countExt,indexOfExt] = [0,0,1,0]
  [maskZero,maskFirst,maskSecond,maskThird] = [2,2,0,0]
  Ext = And(0,1)
  repeat = 0
  inTorExt = 0 ;
  
  while count < NumOfTerminal :
    if repeat == 0:
      [x_base,y_base,z_base,t_base] = [Terminal[4*count+0], Terminal[4*count+1], Terminal[4*count+2], Terminal[4*count+3]]

    if z_base == 0 : m_base = maskZero
    elif z_base == 1 : m_base = maskFirst
    elif z_base == 2 : m_base = maskSecond
    elif z_base == 3 : m_base = maskThird
    print('[x_base,y_base,z_base,t_base] = [', x_base, ', ', y_base, ', ', z_base, ', ', t_base, ']')    
    
    if x_base <= maxX and y_base < maxY and x_base >= minX and y_base >= minY and (repeat == 1 or (repeat == 0 and t_base != 0)) :
      inTorExt = 0
      #check if the node is in floating terminal
      while countT <= (NumOfTerminal)*4-1 and inTorExt == 0 :
        print('0[', x_base, ', ', y_base, ', ', z_base, ', 0]', 'in Terminal?')
        if [x_base,y_base,z_base,0] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2], Terminal[countT+3]] : inTorExt = 1
        countT+=4
      countT = 0
      #check if the node is already got into external edges
      while countExt <= indexOfExt and inTorExt == 0 :
        print('0[', x_base, ', ', y_base, ', ', z_base, '0, ', m_base, ', ' , sn, ']', 'in Ext?')
        if VarName[x_base,y_base,z_base,0,m_base,sn] == Ext[countExt] : inTorExt = 1
        countExt+=1
      countExt = 1
      #if the node is not in Ext and Terminal, add it into Ext
      if inTorExt == 0 and z_base != 0 :
        print('0[', x_base, ', ', y_base, ', ', z_base , ', ' , 0, ', ',m_base, ',' , sn, ']', ' -> Ext')
        Ext += VarName[x_base, y_base, z_base, 0, m_base, sn]
        #print('0',Ext[indexOfExt], '-> Ext')
        indexOfExt+=1
    
    if x_base < maxX and y_base <= maxY and x_base >= minX and y_base >= minY and (repeat == 1 or (repeat == 0 and t_base != 1)) :
      inTorExt = 0
      #check if the node is in floating terminal
      while countT <= (NumOfTerminal)*4-1 and inTorExt == 0 :
        print('1[', x_base, ', ', y_base, ', ', z_base, ', 1]', 'in Terminal?')
        #print('current node in Terminal is ' , Terminal[countT], '  ' , Terminal[countT+1], '  ', Terminal[countT+2], '  ', Terminal[countT+3])
        if [x_base,y_base,z_base,1] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2], Terminal[countT+3]] : inTorExt = 1
        countT+=4
      countT = 0
      #check if the node is already got into external edges
      while countExt <= indexOfExt and inTorExt == 0 :
        print('1[', x_base, ', ', y_base, ', ', z_base, '1, ', m_base, ', ' , sn, ']', 'in Ext?')
        if VarName[x_base,y_base,z_base,1,m_base,sn] == Ext[countExt] : inTorExt = 1
        countExt+=1
      countExt = 1
      #if the node is not in Ext and Terminal, add it into Ext
      if inTorExt == 0 and z_base != 0 :
        print('1[', x_base, ', ', y_base, ', ', z_base, ', ' , 1, ', ' , m_base, ',' , sn, ']', ' -> Ext')
        Ext += VarName[x_base, y_base, z_base, 1, m_base, sn]
        #print('1',Ext[indexOfExt], '-> Ext')
        indexOfExt+=1
    
    if z_base < maxZ and y_base <= maxY and x_base <= maxX and x_base >= minX and y_base >= minY and (repeat == 1 or (repeat == 0 and t_base != 2)) :
      inTorExt = 0
      #check if the node is in floating terminal
      while countT <= (NumOfTerminal)*4-1 and inTorExt == 0 :
        print('2[', x_base, ', ', y_base, ', ', z_base, ', 2]', 'in Terminal?')
        if [x_base,y_base,z_base,2] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2], Terminal[countT+3]] : inTorExt = 1
        countT+=4
      countT = 0
      #check if the node is already got into external edges
      while countExt <= indexOfExt and inTorExt == 0 :
        print('2[', x_base, ', ', y_base, ', ', z_base, '2, ', m_base, ', ' , sn, ']', 'in Ext?')
        if VarName[x_base,y_base,z_base,2,m_base,sn] == Ext[countExt] : inTorExt = 1
        countExt+=1
      countExt = 1
      #if the node is not in Ext and Terminal, add it into Ext
      if inTorExt == 0 :
        print('2[', x_base, ', ', y_base, ', ' , z_base , ', ' , 2, ', ' , m_base, ', ', sn, ']', ' -> Ext')
        Ext += VarName[x_base, y_base, z_base, 2, m_base, sn]
        #print('2',Ext[indexOfExt], '-> Ext')
        indexOfExt+=1
        
    if x_base > minX and x_base <= maxX and y_base >= minY and y_base <= minY and (repeat == 0 or (repeat == 1 and t_base != 1)) :
      inTorExt = 0
      #check if the node is in floating terminal
      while countT <= (NumOfTerminal)*4-1 and inTorExt == 0  :
        print('3[', x_base-1, ', ', y_base, ', ', z_base, ', 1]', 'in Terminal?')
        if [x_base-1,y_base,z_base,1] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2], Terminal[countT+3]] : inTorExt = 1
        countT+=4
      countT = 0
      #check if the node is already got into external edges
      while countExt <= indexOfExt and inTorExt == 0 :
        print('3[', x_base-1, ', ', y_base, ', ', z_base, '1, ', m_base, ', ' , sn, ']', 'in Ext?')
        if VarName[x_base-1,y_base,z_base,1,m_base,sn] == Ext[countExt] : inTorExt = 1
        countExt += 1
      countExt = 1
      #if the node is not in Ext and Terminal, add it into Ext
      if inTorExt == 0 and z_base != 0 :
        print('3[', x_base-1, ', ', y_base, ', ', z_base, ', ' , 1, ', ' , m_base,  ', ', sn, ']', ' -> Ext')
        Ext += VarName[x_base-1,y_base,z_base,1,m_base,sn]
        #print('3',Ext[indexOfExt], '-> Ext')
        indexOfExt+=1
    
    if y_base > minY and y_base <= maxY and x_base >= minX and x_base <= maxX and (repeat == 0 or (repeat == 1 and t_base != 0)) :
      inTorExt = 0
      #check if the node is in floating terminal
      while countT <= (NumOfTerminal)*4-1 and inTorExt == 0  :
        print('4[', x_base, ', ', y_base-1, ', ', z_base, ', 0]', 'in Terminal?')
        if [x_base,y_base-1,z_base,0] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2], Terminal[countT+3]] : inTorExt = 1
        countT+=4
      countT = 0
      #check if the node is already got into external edges
      while countExt <= indexOfExt and inTorExt == 0 :
        print('4[', x_base, ', ', y_base-1, ', ', z_base, '0, ', m_base, ', ' , sn, ']', 'in Ext?')
        if VarName[x_base,y_base-1,z_base,0,m_base,sn] == Ext[countExt] : inTorExt = 1
        countExt += 1
      countExt = 1
      #if the node is not in Ext and Terminal, add it into Ext
      if inTorExt == 0 and z_base != 0 :
        print('4[', x_base, ', ', y_base-1, ', ' , z_base , ', ' , 0,  ', ' , m_base, ', ', sn, ']', ' -> Ext')
        Ext += VarName[x_base,y_base-1,z_base,0,m_base,sn]
        #print('4',Ext[indexOfExt], '-> Ext')
        indexOfExt+=1
        
    if z_base > minZ and x_base >= minX and x_base <= maxX and y_base >= minY and y_base <= maxY and (repeat == 0 or (repeat == 1 and t_base != 2)) :
      inTorExt = 0
      #check if the node is in floating terminal
      while countT <= (NumOfTerminal)*4-1 and inTorExt == 0  :
        print('5[', x_base, ', ', y_base, ', ', z_base-1, ', ', t_base, ']', 'in Terminal?')
        if [x_base,y_base,z_base-1,2] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2], Terminal[countT+3]] : inTorExt = 1
        countT+=4
      countT = 0
      #check if the node is already got into external edges
      while countExt <= indexOfExt and inTorExt == 0 :
        print('5[', x_base, ', ', y_base, ', ', z_base-1, '2, ', m_base, ', ' , sn, ']', 'in Ext?')
        if VarName[x_base,y_base,z_base-1,2,m_base,sn] == Ext[countExt] : inTorExt = 1
        countExt += 1
      countExt = 1
      #if the node is not in Ext and Terminal, add it into Ext
      if inTorExt == 0 :
        print('5[', x_base, ', ', y_base, ', ', z_base-1, ', ' , 2 ,  ', ' , m_base, ', ', sn, ']', ' -> Ext')
        Ext += VarName[x_base,y_base,z_base-1,2,m_base,sn]
        #print('5',Ext[indexOfExt], '-> Ext')
        indexOfExt+=1
        
    if repeat == 0 :
      if t_base == 0 :
        y_base += 1
      elif t_base == 1 :
        x_base += 1
      elif t_base == 2 :
        z_base += 1
      repeat += 1
      if x_base >= maxX or y_base >= maxY or z_base >= maxZ :
        repeat = 0
        count += 1
    elif repeat == 1 :
      count += 1
      repeat = 0
  
  #print('All external edges.')  
  return And(OneHot(*[Ext[index] for index in range(1,indexOfExt+1)]))
  

      

def R2(VarName, Terminal, NumOfTerminal, minX, minY, minZ, maxX, maxY, maxZ, sn):
  print('Enter R2!\n\n\n\n\n\n\n\n')
  [x,y,z,mask,countT] = [minX,minY,minZ,0,0]
  inT = 0 #check whether the node is in Terminal or not
  overRange = 0 #check whether the node is in the range we wet
  Result = And(0,0) #store the constraints to be outputed
  global indexOfResult
  indexOfResult = 0
  [maskFirst,maskSecond,maskThird] = [2,0,0]
  
  while x in range(minX, maxX+1) :
    #print('pass x loop x = ', x)
    y = minY
    while y in range(minY, maxY+1) :
      #print('pass y loop y = ', y)
      #z = minZ
      z = 1
      while z in range(minZ, maxZ+1):
        #print('new node!')
        #set mask
        if z == 1 : mask = maskFirst
        elif z == 2 : mask = maskSecond
        elif z == 3 : mask = maskThird
        #print the current node
        print('current node : ', '[', x ,',',y,',',z,',',mask,']')
    
        #check over range
        print('in/over Range?')
        if x < minX or x > maxX or y < minY or y > maxY or z < minZ or z > maxZ : 
          overRange = 1
          print('  over range')
        else : 
          overRange = 0
          print('  in range')
      
        #check whether the node is in Terminal
        inT = 0 #initialization inT
        inT2 = 0 #check [x,y,z2,2,mask2,sID]
        while countT < NumOfTerminal*3-1 and inT == 0 and overRange == 0:
          print('[', x, ', ', y, ', ', z, ']', 'in Terminal?')
          if [x,y,z] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2]]: 
            inT = 1
            print('  yes')
          if inT2 == 0 and [x,y,z-1] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2]]:
            inT2 = 1
            print('[', x , ',' , y , ',' , z , '-1] in Terminal!')
          countT += 3
        countT = 0 #initialization countT
    
        #Produce Constraints!
        if inT == 0 and overRange == 0 and z != 0 :
          [x2,y2,z2] = [x-1,y-1,z-1]
          if z2 == 0 : mask2 = 2
          elif z2 == 1 : mask2 = maskFirst
          elif z2 == 2 : mask2 = maskSecond
          elif z2 == 3 : mask2 = maskThird

      
          #case0
          if x == minX and y == minY and z == minZ :
            print('0_[',x,', ',y,', ',z,'] ')
            Result += Or(
                         NHot(
                              2,
                              VarName[x,y,z,0,mask,sn],
                              VarName[x,y,z,1,mask,sn],
                              VarName[x,y,z,2,mask,sn]
                              ),
                         ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn])  
                        ).to_cnf()
            indexOfResult += 1
          #case1
          elif x == minX and y == minY:
            if z == maxZ :
              print('1.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,1,mask,sn],
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y,z2,2,mask2,sn]
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            else:
              print('1.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y,z,2,mask,sn],
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y,z,2,mask,sn],
                                VarName[x,y,z2,2,mask2,sn]
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            indexOfResult += 1
          #case2
          elif x == minX and z == minZ :
            if y == maxY:
              print('2.0_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y,z,2,mask,sn],
                                VarName[x,y2,z,0,mask,sn]
                                ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()
     
            else:
              print('2.1_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y,z,2,mask,sn],
                                VarName[x,y2,z,0,mask,sn]
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()
            indexOfResult += 1
          #case3
          elif y == minY and z == minZ :
            if x == maxX-1:
              print('3.0_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,2,mask,sn],
                                VarName[x2,y,z,1,mask,sn]
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            else:
              print('3.1_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y,z,2,mask,sn],
                                VarName[x2,y,z,1,mask,sn]
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            indexOfResult += 1
          #case4
          elif x == minX:
            if z == maxZ and y == maxY:
              print('4.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y2,z,0,mask,sn],
                                ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()
              else :
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y2,z,0,mask,sn],
                                VarName[x,y,z2,2,mask2,sn]
                                ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif z == maxZ:
              print('4.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y2,z,0,mask,sn],
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y2,z,0,mask,sn],
                                VarName[x,y,z2,2,mask2,sn]
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif y == maxY:
              print('4.2_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y,z,2,mask,sn],
                                VarName[x,y2,z,0,mask,sn],
                                ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y,z,2,mask,sn],
                                VarName[x,y2,z,0,mask,sn],
                                VarName[x,y,z2,2,mask2,sn]
                                ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            else:
              print('4.3_[',x,', ',y,', ',z,'] ')  
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn],VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn],VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn],VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn],VarName[x,y2,z,0,mask,sn]),
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn],VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn],VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y,z,1,mask,sn],VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn],VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn],VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y,z,2,mask,sn],VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()      

            indexOfResult += 1
    
          #case5
          elif y == minY :
            if x == maxX and z == maxZ :
              print('5.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x2,y,z,1,mask,sn],
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x2,y,z,1,mask,sn],
                                VarName[x,y,z2,2,mask2,sn]
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif x == maxX :
              print('5.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,2,mask,sn],
                                VarName[x2,y,z,1,mask,sn],
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,2,mask,sn],
                                VarName[x2,y,z,1,mask,sn],
                                VarName[x,y,z2,2,mask2,sn]
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif z == maxZ :
              print('5.2_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,1,mask,sn],
                                VarName[x2,y,z,1,mask,sn],
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,1,mask,sn],
                                VarName[x2,y,z,1,mask,sn],
                                VarName[x,y,z2,2,mask2,sn]
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            else :
              print('5.3_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
              else : 
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            indexOfResult += 1        
          #case6
          elif z == minZ :
            if x == maxX and y == maxY :
              print('6.0_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,2,mask,sn],
                                VarName[x,y2,z,0,mask,sn],
                                VarName[x2,y,z,1,mask,sn]
                                ),
                           ~Or(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            elif x == maxX :
              print('6.1_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y,z,2,mask,sn],
                                VarName[x,y2,z,0,mask,sn],
                                VarName[x2,y,z,1,mask,sn]
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            elif y == maxY :
              print('6.2_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y,z,2,mask,sn],
                                VarName[x,y2,z,0,mask,sn],
                                VarName[x2,y,z,1,mask,sn]
                                ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            else :
              print('6.3_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            indexOfResult += 1    
          #case7
          else:
            if [x,y,z] == [maxX, maxY, maxZ] :
              print('7.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y2,z,0,mask,sn],
                                VarName[x2,y,z,1,mask,sn],
                                ),
                           ~Or(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y2,z,0,mask,sn], 
                                VarName[x2,y,z,1,mask,sn],
                                VarName[x,y,z2,2,mask2,sn]
                                ),
                           ~Or(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif [x,y] == [maxX, maxY] :
              print('7.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,2,mask,sn],
                                VarName[x,y2,z,0,mask,sn],
                                VarName[x2,y,z,1,mask,sn],
                                ),
                           ~Or(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,2,mask,sn],
                                VarName[x,y2,z,0,mask,sn], 
                                VarName[x2,y,z,1,mask,sn],
                                VarName[x,y,z2,2,mask2,sn]
                                ),
                           ~Or(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif [x,z] == [maxX, maxZ] :
              print('7.2_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y2,z,0,mask,sn],
                                VarName[x2,y,z,1,mask,sn],
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,0,mask,sn],
                                VarName[x,y2,z,0,mask,sn], 
                                VarName[x2,y,z,1,mask,sn],
                                VarName[x,y,z2,2,mask2,sn]
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif [y,z] == [maxY, maxZ] :
              print('7.3_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y2,z,0,mask,sn],
                                VarName[x2,y,z,1,mask,sn],
                                ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           NHot(
                                2,
                                VarName[x,y,z,1,mask,sn],
                                VarName[x,y2,z,0,mask,sn], 
                                VarName[x2,y,z,1,mask,sn],
                                VarName[x,y,z2,2,mask2,sn]
                                ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif x == maxX :
              print('7.4_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]), 
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif y == maxY :
              print('7.5_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                 ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                 ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()         
            elif z == maxZ :
              print('7.6_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(

                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(

                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()          
            else : 
              print('7.7_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(

                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(

                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                  And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                  And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
              if [x,y,z] == [14,13,2] : print(indexOfResult+1, '_constraint of node[14,13,1]\n',Result[indexOfResult+1], '\nend\n')
            indexOfResult += 1
        z += 1   
      y +=1
    x += 1
  print('Prepare to return!')
  return And(And(*[Result[index] for index in range(1,indexOfResult)])) 
  #return And(And(*[Result[index] for index in range(472,472+1)]))


  
def R4(VarNameEN, VarNameE, minX, minY, minZ, maxX, maxY, maxZ, netID) :
  print('Enter RConstraints.R4\n')
  global indexOfResult
  [x_base,y_base,z_base,t_base,m_base]=[minX, minY, 1,0,0]
  indexOfResult = 0
  [maskZero,maskFirst,maskSecond,maskThird] = [2,2,0,0]
  Result = And(0,1).to_cnf()
  repeat = 0
  numCheckEdge = 0
  
  while z_base <= maxZ :
    y_base = minY
    while y_base <= maxY :
      x_base = minX
      while x_base <= maxX :
        t_base = 0
        while t_base <= 2 :
          repeat = 0
          while repeat <= 1 :
      
            # assign mask for different layer
            if z_base == 0 : m_base = maskZero
            elif z_base == 1 : m_base = maskFirst
            elif z_base == 2 : m_base = maskSecond
            elif z_base == 3 : m_base = maskThird
            print('repeat = ', repeat,' [x_base,y_base,z_base,t_base] = [', x_base, ', ', y_base, ', ', z_base, ', ', t_base, ']')
            
            if repeat == 0 : [o_x_base,o_y_base,o_z_base,o_t_base,o_m_base,numCheckEdge] = [x_base,y_base,z_base,t_base,m_base,numCheckEdge+1]

            if x_base <= maxX and y_base < maxY and x_base >= minX and y_base >= minY and (repeat == 1 or (repeat == 0 and t_base != 0)) :
             if z_base != 0 :
                print('0[', x_base, ', ', y_base, ', ', z_base , ', ' , 0, ', ',m_base, ']', ' -> Result')
                Result += Implies(
                           And(
                                 VarNameEN[o_x_base, o_y_base, o_z_base, o_t_base, o_m_base, netID],
                                 VarNameE[x_base, y_base, z_base, 0, m_base,]
                              ),
                           VarNameEN[x_base, y_base, z_base, 0, m_base, netID],
                          ).to_cnf()
                #print('0',Result[indexOfResult], '-> Result')
                indexOfResult+=1
    
            if x_base < maxX and y_base <= maxY and x_base >= minX and y_base >= minY and (repeat == 1 or (repeat == 0 and t_base != 1)) :
              if z_base != 0 :
                print('1[', x_base, ', ', y_base, ', ', z_base, ', ' , 1, ', ' , m_base, ']', ' -> Result')
                Result += Implies(
                           And(
                                 VarNameEN[o_x_base, o_y_base, o_z_base, o_t_base, o_m_base, netID],
                                 VarNameE[x_base, y_base, z_base, 1, m_base,]
                              ),
                           VarNameEN[x_base, y_base, z_base, 1, m_base, netID],
                          ).to_cnf()
                #print('1',Result[indexOfResult], '-> Result')
                indexOfResult+=1
    
            if z_base < maxZ and y_base <= maxY and x_base <= maxX and x_base >= minX and y_base >= minY and (repeat == 1 or (repeat == 0 and t_base != 2)) :
              print('2[', x_base, ', ', y_base, ', ' , z_base , ', ' , 2, ', ' , m_base, ']', ' -> Result')
              Result += Implies(
                           And(
                                 VarNameEN[o_x_base, o_y_base, o_z_base, o_t_base, o_m_base, netID],
                                 VarNameE[x_base, y_base, z_base, 2, m_base,]
                              ),
                           VarNameEN[x_base, y_base, z_base, 2, m_base, netID],
                         ).to_cnf()
              #print('2',Result[indexOfResult], '-> Result')
              indexOfResult+=1
        
            if x_base > minX and x_base <= maxX and y_base >= minY and y_base <= minY and (repeat == 0 or (repeat == 1 and t_base != 1)) :
              if z_base != 0 :
                print('3[', x_base-1, ', ', y_base, ', ', z_base, ', ' , 1, ', ' , m_base,  ']', ' -> Result')
                Result += Implies(
                           And(
                                 VarNameEN[o_x_base, o_y_base, o_z_base, o_t_base, o_m_base, netID],
                                 VarNameE[x_base-1, y_base, z_base, 1, m_base,]
                              ),
                           VarNameEN[x_base-1, y_base, z_base, 1, m_base, netID],
                          ).to_cnf()
                #print('3',Result[indexOfResult], '-> Result')
                indexOfResult+=1
    
            if y_base > minY and y_base <= maxY and x_base >= minX and x_base <= maxX and (repeat == 0 or (repeat == 1 and t_base != 0)) :
              if z_base != 0 :
                print('4[', x_base, ', ', y_base-1, ', ' , z_base , ', ' , 0,  ', ' , m_base, ']', ' -> Result')
                Result += Implies(
                           And(
                                 VarNameEN[o_x_base, o_y_base, o_z_base, o_t_base, o_m_base, netID],
                                 VarNameE[x_base, y_base-1, z_base, 0, m_base,]
                              ),
                           VarNameEN[x_base, y_base-1, z_base, 0, m_base, netID],
                          ).to_cnf()
                #print('4',Result[indexOfResult], '-> Result')
                indexOfResult+=1
        
            if z_base > minZ and x_base >= minX and x_base <= maxX and y_base >= minY and y_base <= maxY and (repeat == 0 or (repeat == 1 and t_base != 2)) :
              print('5[', x_base, ', ', y_base, ', ', z_base-1, ', ' , 2 ,  ', ' , m_base, ']', ' -> Result')
              Result += Implies(
                           And(
                                 VarNameEN[o_x_base, o_y_base, o_z_base, o_t_base, o_m_base, netID],
                                 VarNameE[x_base, y_base, z_base-1, 2, m_base,]
                              ),
                           VarNameEN[x_base, y_base, z_base-1, 2, m_base, netID],
                          ).to_cnf()
              #print('5',Result[indexOfResult], '-> Result')
              indexOfResult+=1
        
            if repeat == 0 :
              print('repeat is 0 ', end ='')
              if t_base == 0 :
                y_base += 1
                print(' y+1')
              elif t_base == 1 :
                x_base += 1
                print(' x+1')
              elif t_base == 2 :
                print(' z+1')
                z_base += 1
              repeat += 1
              if x_base > maxX or y_base > maxY or z_base > maxZ :
                print('new edge exceeds the rnage...abandon')
                repeat = 2
            elif repeat == 1 :
              repeat += 1
            if repeat > 1 :
              [x_base,y_base,z_base,t_base] =[o_x_base,o_y_base,o_z_base,o_t_base]
          
          t_base += 1
        x_base += 1
      y_base += 1
    z_base += 1
        
  print('R4 Check ' , numCheckEdge , " Edges.")
  #print('All Resulternal edges.')  
  return And(And(*[Result[index] for index in range(1,indexOfResult+1)])) 
  #return And(OneHot(*[Ext[index] for index in range(1,indexOfExt+1)]))


def R2_R4(VarName, E_VarName, Terminal, NumOfTerminal, minX, minY, minZ, maxX, maxY, maxZ, sn):
  print('Enter R2!\n\n\n\n\n\n\n\n')
  [x,y,z,mask,countT] = [minX,minY,minZ,0,0]
  inT = 0 #check whether the node is in Terminal or not
  overRange = 0 #check whether the node is in the range we wet
  Result = And(0,0) #store the constraints to be outputed
  global indexOfResult
  indexOfResult = 0
  [maskFirst,maskSecond,maskThird] = [2,0,0]
  
  while x in range(minX, maxX+1) :
    #print('pass x loop x = ', x)
    y = minY
    while y in range(minY, maxY+1) :
      #print('pass y loop y = ', y)
      #z = minZ
      z = 1
      while z in range(minZ, maxZ+1):
        #print('new node!')
        #set mask
        if z == 1 : mask = maskFirst
        elif z == 2 : mask = maskSecond
        elif z == 3 : mask = maskThird
        #print the current node
        print('current node : ', '[', x ,',',y,',',z,',',mask,']')
    
        #check over range
        print('in/over Range?')
        if x < minX or x > maxX or y < minY or y > maxY or z < minZ or z > maxZ : 
          overRange = 1
          print('  over range')
        else : 
          overRange = 0
          print('  in range')
      
        #check whether the node is in Terminal
        inT = 0 #initialization inT
        inT2 = 0 #check [x,y,z2,2,mask2,sID]
        while countT < NumOfTerminal*3-1 and inT == 0 and overRange == 0:
          print('[', x, ', ', y, ', ', z, ']', 'in Terminal?')
          if [x,y,z] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2]]: 
            inT = 1
            print('  yes')
          if inT2 == 0 and [x,y,z-1] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2]]:
            inT2 = 1
            print('[', x , ',' , y , ',' , z , '-1] in Terminal!')
          countT += 3
        countT = 0 #initialization countT
    
        #Produce Constraints!
        if inT == 0 and overRange == 0 and z != 0 :
          [x2,y2,z2] = [x-1,y-1,z-1]
          if z2 == 0 : mask2 = 2
          elif z2 == 1 : mask2 = maskFirst
          elif z2 == 2 : mask2 = maskSecond
          elif z2 == 3 : mask2 = maskThird

      
          #case0
          if x == minX and y == minY and z == minZ :
            print('0_[',x,', ',y,', ',z,'] ')
            Result += Or(
						 OneHot(And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask]),
								And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn]),
								And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn])
								),
                         ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn])  
                        ).to_cnf()
            indexOfResult += 1
          #case1
          elif x == minX and y == minY:
            if z == maxZ :
              print('1.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                             And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,1,mask,sn]),
                             ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn])
                            ).to_cnf()

              else :
                Result += Or(
                             OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
								   ),
                             ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                            ).to_cnf()
            else:
              print('1.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                             OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
                                   ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                             OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
								   ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            indexOfResult += 1
          #case2
          elif x == minX and z == minZ :
            if y == maxY:
              print('2.0_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           OneHot(
								  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask]),
								  And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn]),
								  And(~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
                                ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()
     
            else:
              print('2.1_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask]),
								  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask]),
								  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn]),
								  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask]),
								  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn]),
								  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                                ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()
            indexOfResult += 1
          #case3
          elif y == minY and z == minZ :
            if x == maxX-1:
              print('3.0_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                                  ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            else:
              print('3.1_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x2,y,z,1,mask]),
								  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x2,y,z,1,mask,sn]),
								  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x2,y,z,1,mask]),
								  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x2,y,z,1,mask,sn]),
								  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            indexOfResult += 1
          #case4
          elif x == minX:
            if z == maxZ and y == maxY:
              print('4.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                             And(VarName[x,y,z,1,mask,sn],VarName[x,y2,z,0,mask,sn]),
                             ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn])
                            ).to_cnf()
              else :
                Result += Or(
                             OneHot(
									And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,1,mask], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
								   ),
							 ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
							).to_cnf()
            elif z == maxZ:
              print('4.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y2,z,0,mask]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y2,z,0,mask,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn])
                                ),
							 ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y2,z,0,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
								   ),
							 ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
							).to_cnf()
            elif y == maxY:
              print('4.2_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask]),
									And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn]),
									And(~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
								   ),
							 ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
							).to_cnf()

              else :
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
								   ),
							 ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
							).to_cnf()
            else:
              print('4.3_[',x,', ',y,', ',z,'] ')  
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()      

            indexOfResult += 1
    
          #case5
          elif y == minY :
            if x == maxX and z == maxZ :
              print('5.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(VarName[x,y,z,0,mask,sn],VarName[x2,y,z,1,mask,sn]),
							 ~Or(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
							).to_cnf()

              else :
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn])
								   ),
							 ~Or(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
							).to_cnf()
            elif x == maxX :
              print('5.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x2,y,z,1,mask]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x2,y,z,1,mask,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                   ),
							 ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
							).to_cnf()

              else :
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,2,mask], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
								   ),
							 ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
							).to_cnf()
            elif z == maxZ :
              print('5.2_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x2,y,z,1,mask]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x2,y,z,1,mask,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn])
                                   ),
							 ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
								   ),
							 ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
							).to_cnf()
            else :
              print('5.3_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x2,y,z,1,mask]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x2,y,z,1,mask]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x2,y,z,1,mask,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x2,y,z,1,mask]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x2,y,z,1,mask,sn]),
									And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                                   ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
              else : 
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                                   ),
							 ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
							).to_cnf()
            indexOfResult += 1        
          #case6
          elif z == minZ :
            if x == maxX and y == maxY :
              print('6.0_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           OneHot(
								  And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
								  And(VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
								  And(~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                                 ),
                           ~Or(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            elif x == maxX :
              print('6.1_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask]),
								  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
								  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
								  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
								  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
								  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            elif y == maxY :
              print('6.2_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           OneHot(
								  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask]),
								  And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
								  And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
								  And(~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
								  And(~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
								  And(~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                                 ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            else :
              print('6.3_[',x,', ',y,', ',z,'] ')
              Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            indexOfResult += 1    
          #case7
          else:
            if [x,y,z] == [maxX, maxY, maxZ] :
              print('7.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(VarName[x,y2,z,0,mask,sn],VarName[x2,y,z,1,mask,sn]),
							 ~Or(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
							).to_cnf()

              else :
                Result += Or(
							 OneHot(
									And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                   ),
							 ~Or(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif [x,y] == [maxX, maxY] :
              print('7.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
									And(VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
									And(~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                   ),
							 ~Or(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                                   ),
							 ~Or(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif [x,z] == [maxX, maxZ] :
              print('7.2_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                                   ),
							 ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
							).to_cnf()

              else :
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(~E_VarName[x,y,z,0,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                                   ),
							 ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif [y,z] == [maxY, maxZ] :
              print('7.3_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
									And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
									And(~E_VarName[x,y,z,1,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
                                   ),
							 ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
							).to_cnf()

              else :
                Result += Or(
							 OneHot(
									And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,1,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
									And(~E_VarName[x,y,z,1,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
									And(~E_VarName[x,y,z,1,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                                   ),
							 ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif x == maxX :
              print('7.4_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]), 
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]), 
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]), 
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]), 
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]), 
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]), 
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]), 
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]), 
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]), 
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif y == maxY :
              print('7.5_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                                 ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
                           OneHot(
                                  And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                                 ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()         
            elif z == maxZ :
              print('7.6_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(

                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(

                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()          
            else : 
              print('7.7_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(

                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(

                           OneHot(
                                  And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(VarName[x,y,z,0,mask,sn], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,0,mask], VarName[x,y,z,1,mask,sn], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], VarName[x,y,z,2,mask,sn], ~E_VarName[x,y2,z,0,mask], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], ~E_VarName[x,y,z2,2,mask2]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], VarName[x,y2,z,0,mask,sn], ~E_VarName[x2,y,z,1,mask], VarName[x,y,z2,2,mask2,sn]),
                                  And(~E_VarName[x,y,z,0,mask], ~E_VarName[x,y,z,1,mask], ~E_VarName[x,y,z,2,mask], ~E_VarName[x,y2,z,0,mask], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                                 ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
              if [x,y,z] == [14,13,2] : print(indexOfResult+1, '_constraint of node[14,13,1]\n',Result[indexOfResult+1], '\nend\n')
            indexOfResult += 1
        z += 1   
      y +=1
    x += 1
  print('Prepare to return!')
  return And(And(*[Result[index] for index in range(1,indexOfResult)]))


def R2_R4_V2(VarName, E_VarName, Terminal, NumOfTerminal, minX, minY, minZ, maxX, maxY, maxZ, sn):
  print('Enter R2!\n\n\n\n\n\n\n\n')
  [x,y,z,mask,countT] = [minX,minY,minZ,0,0]
  inT = 0 #check whether the node is in Terminal or not
  overRange = 0 #check whether the node is in the range we wet
  Result = And(0,0) #store the constraints to be outputed
  global indexOfResult
  indexOfResult = 0
  [maskFirst,maskSecond,maskThird] = [2,0,0]
  
  while x in range(minX, maxX+1) :
    #print('pass x loop x = ', x)
    y = minY
    while y in range(minY, maxY+1) :
      #print('pass y loop y = ', y)
      #z = minZ
      z = 1
      while z in range(minZ, maxZ+1):
        #print('new node!')
        #set mask
        if z == 1 : mask = maskFirst
        elif z == 2 : mask = maskSecond
        elif z == 3 : mask = maskThird
        #print the current node
        print('current node : ', '[', x ,',',y,',',z,',',mask,']')
    
        #check over range
        print('in/over Range?')
        if x < minX or x > maxX or y < minY or y > maxY or z < minZ or z > maxZ : 
          overRange = 1
          print('  over range')
        else : 
          overRange = 0
          print('  in range')
      
        #check whether the node is in Terminal
        inT = 0 #initialization inT
        inT2 = 0 #check [x,y,z2,2,mask2,sID]
        while countT < NumOfTerminal*3-1 and inT == 0 and overRange == 0:
          print('[', x, ', ', y, ', ', z, ']', 'in Terminal?')
          if [x,y,z] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2]]: 
            inT = 1
            print('  yes')
          if inT2 == 0 and [x,y,z-1] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2]]:
            inT2 = 1
            print('[', x , ',' , y , ',' , z , '-1] in Terminal!')
          countT += 3
        countT = 0 #initialization countT
    
        #Produce Constraints!
        if inT == 0 and overRange == 0 and z != 0 :
          [x2,y2,z2] = [x-1,y-1,z-1]
          if z2 == 0 : mask2 = 2
          elif z2 == 1 : mask2 = maskFirst
          elif z2 == 2 : mask2 = maskSecond
          elif z2 == 3 : mask2 = maskThird

      
          #case0
          if x == minX and y == minY and z == minZ :
            print('0_[',x,', ',y,', ',z,'] ')
            Result += Or(
						 And(
							 NHot(
								  2,
								  VarName[x,y,z,0,mask,sn],
								  VarName[x,y,z,1,mask,sn],
								  VarName[x,y,z,2,mask,sn]
								 ),
							 
							 ~Xor(VarName[x,y,z,0,mask,sn], E_VarName[x,y,z,0,mask]),
							 ~Xor(VarName[x,y,z,1,mask,sn], E_VarName[x,y,z,1,mask]),
							 ~Xor(VarName[x,y,z,2,mask,sn], E_VarName[x,y,z,2,mask])
						 ),
                         ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn])  
                        ).to_cnf()
            indexOfResult += 1
          #case1
          elif x == minX and y == minY:
            if z == maxZ :
              print('1.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									 ),
								 ~Xor(VarName[x,y,z,0,mask,sn], E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn], E_VarName[x,y,z,1,mask])	 
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            else:
              print('1.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y,z,2,mask,sn],
									 ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y,z,2,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            indexOfResult += 1
          #case2
          elif x == minX and z == minZ :
            if y == maxY:
              print('2.0_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,1,mask,sn],
									VarName[x,y,z,2,mask,sn],
									VarName[x,y2,z,0,mask,sn]
								   ),
							   ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
							   ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
							   ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask])
							  ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()
     
            else:
              print('2.1_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,0,mask,sn],
									VarName[x,y,z,1,mask,sn],
									VarName[x,y,z,2,mask,sn],
									VarName[x,y2,z,0,mask,sn]
								   ),
							   ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
							   ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
							   ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
							   ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask])
							  ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()
            indexOfResult += 1
          #case3
          elif y == minY and z == minZ :
            if x == maxX-1:
              print('3.0_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,0,mask,sn],
									VarName[x,y,z,2,mask,sn],
									VarName[x2,y,z,1,mask,sn]
								   ),
							   ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
							   ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
							   ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
							  ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            else:
              print('3.1_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,0,mask,sn],
									VarName[x,y,z,1,mask,sn],
									VarName[x,y,z,2,mask,sn],
									VarName[x2,y,z,1,mask,sn]
                                   ),
							   ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
							   ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
							   ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
							   ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
							  ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            indexOfResult += 1
          #case4
          elif x == minX:
            if z == maxZ and y == maxY:
              print('4.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									 ),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()
              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif z == maxZ:
              print('4.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									 ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif y == maxY:
              print('4.2_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y,z,2,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									 ),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y,z,2,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            else:
              print('4.3_[',x,', ',y,', ',z,'] ')  
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn],VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn],VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn],VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn],VarName[x,y2,z,0,mask,sn]),
									   ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn],VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn],VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,1,mask,sn],VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn],VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn],VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,2,mask,sn],VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
									   ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()      

            indexOfResult += 1
    
          #case5
          elif y == minY :
            if x == maxX and z == maxZ :
              print('5.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif x == maxX :
              print('5.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,2,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								  ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								  ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								  ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,2,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								  ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								  ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								  ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask]),
								  ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif z == maxZ :
              print('5.2_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								  ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								  ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								  ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            else :
              print('5.3_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
              else : 
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
									 ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            indexOfResult += 1        
          #case6
          elif z == minZ :
            if x == maxX and y == maxY :
              print('6.0_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,2,mask,sn],
									VarName[x,y2,z,0,mask,sn],
									VarName[x2,y,z,1,mask,sn]
								   ),
							   ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
							   ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
							   ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
							  ),
                           ~Or(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            elif x == maxX :
              print('6.1_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,0,mask,sn],
									VarName[x,y,z,2,mask,sn],
									VarName[x,y2,z,0,mask,sn],
									VarName[x2,y,z,1,mask,sn]
                                   ),
							   ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
							   ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
							   ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
							   ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
							  ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            elif y == maxY :
              print('6.2_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,1,mask,sn],
									VarName[x,y,z,2,mask,sn],
									VarName[x,y2,z,0,mask,sn],
									VarName[x2,y,z,1,mask,sn]
                                   ),
							   ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
							   ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
							   ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
							   ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
							  ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            else :
              print('6.3_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   OneHot(
									   And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
									   And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
									   And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
									   And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
									   And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
									   And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
									   And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
									  ),
							   ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,mask]),
							   ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
							   ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
							   ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
							   ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
							  ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            indexOfResult += 1    
          #case7
          else:
            if [x,y,z] == [maxX, maxY, maxZ] :
              print('7.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
							     ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
								),
                           ~Or(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y2,z,0,mask,sn], 
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
							     ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif [x,y] == [maxX, maxY] :
              print('7.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,2,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
								),
                           ~Or(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,2,mask,sn],
									  VarName[x,y2,z,0,mask,sn], 
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif [x,z] == [maxX, maxZ] :
              print('7.2_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y2,z,0,mask,sn], 
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif [y,z] == [maxY, maxZ] :
              print('7.3_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y2,z,0,mask,sn], 
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif x == maxX :
              print('7.4_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]), 
										And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
									   ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2]),
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif y == maxY :
              print('7.5_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   ),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
									   ),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()         
            elif z == maxZ :
              print('7.6_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
									   ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask]),  
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()          
            else : 
              print('7.7_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]), 
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
									   ),
								 ~Xor(VarName[x,y,z,0,mask,sn],E_VarName[x,y,z,0,mask]),
								 ~Xor(VarName[x,y,z,1,mask,sn],E_VarName[x,y,z,1,mask]), 
								 ~Xor(VarName[x,y,z,2,mask,sn],E_VarName[x,y,z,2,mask]),
								 ~Xor(VarName[x,y2,z,0,mask,sn],E_VarName[x,y2,z,0,mask]),
								 ~Xor(VarName[x2,y,z,1,mask,sn],E_VarName[x2,y,z,1,mask]),
								 ~Xor(VarName[x,y,z2,2,mask2,sn],E_VarName[x,y,z2,2,mask2])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
              if [x,y,z] == [14,13,2] : print(indexOfResult+1, '_constraint of node[14,13,1]\n',Result[indexOfResult+1], '\nend\n')
            indexOfResult += 1
        z += 1   
      y +=1
    x += 1
  print('Prepare to return!')
  return And(And(*[Result[index] for index in range(1,indexOfResult)])) 
  #return And(And(*[Result[index] for index in range(472,472+1)]))

def R2_R4_V3(VarName, E_VarName, EN_VarName, Terminal, NumOfTerminal, minX, minY, minZ, maxX, maxY, maxZ, sn, n):
  print('Enter R2!\n\n\n\n\n\n\n\n')
  [x,y,z,mask,countT] = [minX,minY,minZ,0,0]
  inT = 0 #check whether the node is in Terminal or not
  overRange = 0 #check whether the node is in the range we wet
  Result = And(0,0) #store the constraints to be outputed
  global indexOfResult
  indexOfResult = 0
  [maskFirst,maskSecond,maskThird] = [2,0,0]
  
  while x in range(minX, maxX+1) :
    #print('pass x loop x = ', x)
    y = minY
    while y in range(minY, maxY+1) :
      #print('pass y loop y = ', y)
      #z = minZ
      z = 1
      while z in range(minZ, maxZ+1):
        #print('new node!')
        #set mask
        if z == 1 : mask = maskFirst
        elif z == 2 : mask = maskSecond
        elif z == 3 : mask = maskThird
        #print the current node
        print('current node : ', '[', x ,',',y,',',z,',',mask,']')
    
        #check over range
        print('in/over Range?')
        if x < minX or x > maxX or y < minY or y > maxY or z < minZ or z > maxZ : 
          overRange = 1
          print('  over range')
        else : 
          overRange = 0
          print('  in range')
      
        #check whether the node is in Terminal
        inT = 0 #initialization inT
        inT2 = 0 #check [x,y,z2,2,mask2,sID]
        while countT < NumOfTerminal*3-1 and inT == 0 and overRange == 0:
          print('[', x, ', ', y, ', ', z, ']', 'in Terminal?')
          if [x,y,z] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2]]: 
            inT = 1
            print('  yes')
          if inT2 == 0 and [x,y,z-1] == [Terminal[countT], Terminal[countT+1], Terminal[countT+2]]:
            inT2 = 1
            print('[', x , ',' , y , ',' , z , '-1] in Terminal!')
          countT += 3
        countT = 0 #initialization countT
    
        #Produce Constraints!
        if inT == 0 and overRange == 0 and z != 0 :
          [x2,y2,z2] = [x-1,y-1,z-1]
          if z2 == 0 : mask2 = 2
          elif z2 == 1 : mask2 = maskFirst
          elif z2 == 2 : mask2 = maskSecond
          elif z2 == 3 : mask2 = maskThird

      
          #case0
          if x == minX and y == minY and z == minZ :
            print('0_[',x,', ',y,', ',z,'] ')
            Result += Or(
						 And(
							 NHot(
								  2,
								  VarName[x,y,z,0,mask,sn],
								  VarName[x,y,z,1,mask,sn],
								  VarName[x,y,z,2,mask,sn]
								 ),
							 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
							 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
							 Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n])
						 ),
                         ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn])  
                        ).to_cnf()
            indexOfResult += 1
          #case1
          elif x == minX and y == minY:
            if z == maxZ :
              print('1.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									 ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n] ),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n] )	 
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2], EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            else:
              print('1.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y,z,2,mask,sn],
									 ),
								 Implies(E_VarName[x,y,z,0,mask],EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask],EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y,z,2,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2], EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            indexOfResult += 1
          #case2
          elif x == minX and z == minZ :
            if y == maxY:
              print('2.0_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,1,mask,sn],
									VarName[x,y,z,2,mask,sn],
									VarName[x,y2,z,0,mask,sn]
								   ),
							   Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
							   Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n]),
							   Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n])
							  ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()
     
            else:
              print('2.1_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,0,mask,sn],
									VarName[x,y,z,1,mask,sn],
									VarName[x,y,z,2,mask,sn],
									VarName[x,y2,z,0,mask,sn]
								   ),
							   Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n] ),
							   Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n] ),
							   Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n] ),
							   Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n] )
							  ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()
            indexOfResult += 1
          #case3
          elif y == minY and z == minZ :
            if x == maxX-1:
              print('3.0_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,0,mask,sn],
									VarName[x,y,z,2,mask,sn],
									VarName[x2,y,z,1,mask,sn]
								   ),
							   Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
							   Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n]),
							   Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n])
							  ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            else:
              print('3.1_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,0,mask,sn],
									VarName[x,y,z,1,mask,sn],
									VarName[x,y,z,2,mask,sn],
									VarName[x2,y,z,1,mask,sn]
                                   ),
							   Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
							   Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
							   Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n]),
							   Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n])
							  ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            indexOfResult += 1
          #case4
          elif x == minX:
            if z == maxZ and y == maxY:
              print('4.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									 ),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()
              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2], EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif z == maxZ:
              print('4.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									 ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2], EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif y == maxY:
              print('4.2_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y,z,2,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									 ),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y,z,2,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2], EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            else:
              print('4.3_[',x,', ',y,', ',z,'] ')  
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn],VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn],VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn],VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn],VarName[x,y2,z,0,mask,sn]),
									   ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn],VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn],VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn],VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,1,mask,sn],VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn],VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn],VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,2,mask,sn],VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
									   ),
								 Implies(E_VarName[x,y,z,0,mask],EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask],EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2],EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()      

            indexOfResult += 1
    
          #case5
          elif y == minY :
            if x == maxX and z == maxZ :
              print('5.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2], EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif x == maxX :
              print('5.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,2,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								  Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								  Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n]),
								  Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,2,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								  Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								  Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n]),
								  Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n]),
								  Implies(E_VarName[x,y,z2,2,mask2], EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif z == maxZ :
              print('5.2_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								  Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								  Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								  Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y,z,1,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2], EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            else :
              print('5.3_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
              else : 
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
									 ),
								 Implies(E_VarName[x,y,z,0,mask],EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask],EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2],EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            indexOfResult += 1        
          #case6
          elif z == minZ :
            if x == maxX and y == maxY :
              print('6.0_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,2,mask,sn],
									VarName[x,y2,z,0,mask,sn],
									VarName[x2,y,z,1,mask,sn]
								   ),
							   Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n]),
							   Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n]),
							   Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n])
							  ),
                           ~Or(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            elif x == maxX :
              print('6.1_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,0,mask,sn],
									VarName[x,y,z,2,mask,sn],
									VarName[x,y2,z,0,mask,sn],
									VarName[x2,y,z,1,mask,sn]
                                   ),
							   Implies(E_VarName[x,y,z,0,mask],EN_VarName[x,y,z,0,mask,n]),
							   Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n]),
							   Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
							   Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n])
							  ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            elif y == maxY :
              print('6.2_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   NHot(
									2,
									VarName[x,y,z,1,mask,sn],
									VarName[x,y,z,2,mask,sn],
									VarName[x,y2,z,0,mask,sn],
									VarName[x2,y,z,1,mask,sn]
                                   ),
							   Implies(E_VarName[x,y,z,1,mask],EN_VarName[x,y,z,1,mask,n]),
							   Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n]),
							   Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
							   Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n])
							  ),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            else :
              print('6.3_[',x,', ',y,', ',z,'] ')
              Result += Or(
						   And(
							   OneHot(
									   And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
									   And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
									   And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
									   And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
									   And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
									   And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
									   And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
									  ),
							   Implies(E_VarName[x,y,z,mask],EN_VarName[x,y,z,0,mask,n]),
							   Implies(E_VarName[x,y,z,1,mask],EN_VarName[x,y,z,1,mask,n]),
							   Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n]),
							   Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
							   Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n])
							  ),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()
            indexOfResult += 1    
          #case7
          else:
            if [x,y,z] == [maxX, maxY, maxZ] :
              print('7.0_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								 Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n]),
							     Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n])
								),
                           ~Or(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y2,z,0,mask,sn], 
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
							     Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2],EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif [x,y] == [maxX, maxY] :
              print('7.1_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,2,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								 Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n])
								),
                           ~Or(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,2,mask,sn],
									  VarName[x,y2,z,0,mask,sn], 
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2],EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif [x,z] == [maxX, maxZ] :
              print('7.2_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,0,mask,sn],
									  VarName[x,y2,z,0,mask,sn], 
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 Implies(E_VarName[x,y,z,0,mask],EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2],EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif [y,z] == [maxY, maxZ] :
              print('7.3_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y2,z,0,mask,sn],
									  VarName[x2,y,z,1,mask,sn],
									 ),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 NHot(
									  2,
									  VarName[x,y,z,1,mask,sn],
									  VarName[x,y2,z,0,mask,sn], 
									  VarName[x2,y,z,1,mask,sn],
									  VarName[x,y,z2,2,mask2,sn]
									 ),
								 Implies(E_VarName[x,y,z,1,mask],EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2],EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif x == maxX :
              print('7.4_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   ),
								 Implies(E_VarName[x,y,z,0,mask],EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]), 
										And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
									   ),
								 Implies(E_VarName[x,y,z,0,mask],EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2],EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
            elif y == maxY :
              print('7.5_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   ),
								 Implies(E_VarName[x,y,z,1,mask],EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
									   ),
								 Implies(E_VarName[x,y,z,1,mask],EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2],EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()         
            elif z == maxZ :
              print('7.6_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   ),
								 Implies(E_VarName[x,y,z,0,mask],EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask],EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
									   ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n]),  
								 Implies(E_VarName[x,y,z2,2,mask2], EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()          
            else : 
              print('7.7_[',x,', ',y,', ',z,'] ')
              if z2 == 0 and inT2 == 0 :
                print("z2 = 0")
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
									   ),
								 Implies(E_VarName[x,y,z,0,mask],EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask],EN_VarName[x,y,z,1,mask,n]), 
								 Implies(E_VarName[x,y,z,2,mask],EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask],EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask],EN_VarName[x2,y,z,1,mask,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn])
                          ).to_cnf()

              else :
                Result += Or(
							 And(
								 OneHot(
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y,z,2,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn]),
										And(VarName[x,y2,z,0,mask,sn], VarName[x,y,z2,2,mask2,sn]),
										And(VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn]),
									   ),
								 Implies(E_VarName[x,y,z,0,mask], EN_VarName[x,y,z,0,mask,n]),
								 Implies(E_VarName[x,y,z,1,mask], EN_VarName[x,y,z,1,mask,n]), 
								 Implies(E_VarName[x,y,z,2,mask], EN_VarName[x,y,z,2,mask,n]),
								 Implies(E_VarName[x,y2,z,0,mask], EN_VarName[x,y2,z,0,mask,n]),
								 Implies(E_VarName[x2,y,z,1,mask], EN_VarName[x2,y,z,1,mask,n]),
								 Implies(E_VarName[x,y,z2,2,mask2], EN_VarName[x,y,z2,2,mask2,n])
								),
                           ~Or(VarName[x,y,z,0,mask,sn], VarName[x,y,z,1,mask,sn], VarName[x,y,z,2,mask,sn], VarName[x,y2,z,0,mask,sn], VarName[x2,y,z,1,mask,sn], VarName[x,y,z2,2,mask2,sn])
                          ).to_cnf()
              if [x,y,z] == [14,13,2] : print(indexOfResult+1, '_constraint of node[14,13,1]\n',Result[indexOfResult+1], '\nend\n')
            indexOfResult += 1
        z += 1   
      y +=1
    x += 1
  print('Prepare to return!')
  return And(And(*[Result[index] for index in range(1,indexOfResult)])) 
