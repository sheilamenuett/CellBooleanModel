from pyeda.inter import *
import RConstraints
import time
import setOut
startTime = time.time()
# ===> Instruction(Create)  2D Routing Style p(e) <===
# ===> Edges[X, Y, Z, Trends, Masks]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge = exprvars('edge', 18, 36, 4, 3, 3)

# ===> Instruction(Create)  2D Routing Style p(e,n) <===
# ===> Edge_Net[X, Y, Z, Trends, Masks, Nets]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge_Net = exprvars('edge_net', 18, 36, 4, 3, 3, 2)

# ===> Instruction(Create)  2D Routing Style p(e,n,s) <===
# ===> Edge_Net_Subnet_NetID[X, Y, Z, Trends, Masks, Subnets]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal

outLayout=[[[[0 for trend in range(3)] for z in range(4)] for y in range(36)] for x in range(18)]

subnetRec=[[[[0 for trend in range(3)] for z in range(4)] for y in range(36)] for x in range(18)]

MaxX = 17
MaxY = 35
MaxZ = 3
#Net = 2
#cellName = TIEH_DFINH_combined
#Initialize poly
Edge[0,0,0,0,0] = expr(1)
Edge[0,1,0,0,0] = expr(1)
Edge[0,2,0,0,0] = expr(1)
Edge[0,3,0,0,0] = expr(1)
Edge[0,4,0,0,0] = expr(1)
Edge[0,5,0,0,0] = expr(1)
Edge[0,6,0,0,0] = expr(1)
Edge[0,7,0,0,0] = expr(1)
Edge[0,8,0,0,0] = expr(1)
Edge[0,9,0,0,0] = expr(1)
Edge[0,10,0,0,0] = expr(1)
Edge[0,11,0,0,0] = expr(1)
Edge[0,12,0,0,0] = expr(1)
Edge[0,13,0,0,0] = expr(1)
Edge[0,14,0,0,0] = expr(1)
Edge[0,15,0,0,0] = expr(1)
Edge[0,16,0,0,0] = expr(1)
Edge[0,17,0,0,0] = expr(1)
Edge[0,18,0,0,0] = expr(1)
Edge[0,19,0,0,0] = expr(1)
Edge[0,20,0,0,0] = expr(1)
Edge[0,21,0,0,0] = expr(1)
Edge[0,22,0,0,0] = expr(1)
Edge[0,23,0,0,0] = expr(1)
Edge[0,24,0,0,0] = expr(1)
Edge[0,25,0,0,0] = expr(1)
Edge[0,26,0,0,0] = expr(1)
Edge[0,27,0,0,0] = expr(1)
Edge[0,28,0,0,0] = expr(1)
Edge[0,29,0,0,0] = expr(1)
Edge[0,30,0,0,0] = expr(1)
Edge[0,31,0,0,0] = expr(1)
Edge[0,32,0,0,0] = expr(1)
Edge[0,33,0,0,0] = expr(1)
Edge[0,34,0,0,0] = expr(1)
Edge[0,35,0,0,0] = expr(1)
Edge_Net[0,0,0,0,0,0:] = exprzeros(2)
Edge_Net[0,1,0,0,0,0:] = exprzeros(2)
Edge_Net[0,2,0,0,0,0:] = exprzeros(2)
Edge_Net[0,3,0,0,0,0:] = exprzeros(2)
Edge_Net[0,4,0,0,0,0:] = exprzeros(2)
Edge_Net[0,5,0,0,0,0:] = exprzeros(2)
Edge_Net[0,6,0,0,0,0:] = exprzeros(2)
Edge_Net[0,7,0,0,0,0:] = exprzeros(2)
Edge_Net[0,8,0,0,0,0:] = exprzeros(2)
Edge_Net[0,9,0,0,0,0:] = exprzeros(2)
Edge_Net[0,10,0,0,0,0:] = exprzeros(2)
Edge_Net[0,11,0,0,0,0:] = exprzeros(2)
Edge_Net[0,12,0,0,0,0:] = exprzeros(2)
Edge_Net[0,13,0,0,0,0:] = exprzeros(2)
Edge_Net[0,14,0,0,0,0:] = exprzeros(2)
Edge_Net[0,15,0,0,0,0:] = exprzeros(2)
Edge_Net[0,16,0,0,0,0:] = exprzeros(2)
Edge_Net[0,17,0,0,0,0:] = exprzeros(2)
Edge_Net[0,18,0,0,0,0:] = exprzeros(2)
Edge_Net[0,19,0,0,0,0:] = exprzeros(2)
Edge_Net[0,20,0,0,0,0:] = exprzeros(2)
Edge_Net[0,21,0,0,0,0:] = exprzeros(2)
Edge_Net[0,22,0,0,0,0:] = exprzeros(2)
Edge_Net[0,23,0,0,0,0:] = exprzeros(2)
Edge_Net[0,24,0,0,0,0:] = exprzeros(2)
Edge_Net[0,25,0,0,0,0:] = exprzeros(2)
Edge_Net[0,26,0,0,0,0:] = exprzeros(2)
Edge_Net[0,27,0,0,0,0:] = exprzeros(2)
Edge_Net[0,28,0,0,0,0:] = exprzeros(2)
Edge_Net[0,29,0,0,0,0:] = exprzeros(2)
Edge_Net[0,30,0,0,0,0:] = exprzeros(2)
Edge_Net[0,31,0,0,0,0:] = exprzeros(2)
Edge_Net[0,32,0,0,0,0:] = exprzeros(2)
Edge_Net[0,33,0,0,0,0:] = exprzeros(2)
Edge_Net[0,34,0,0,0,0:] = exprzeros(2)
Edge_Net[0,35,0,0,0,0:] = exprzeros(2)
Edge[4,0,0,0,0] = expr(1)
Edge[4,1,0,0,0] = expr(1)
Edge[4,2,0,0,0] = expr(1)
Edge[4,3,0,0,0] = expr(1)
Edge[4,4,0,0,0] = expr(1)
Edge[4,5,0,0,0] = expr(1)
Edge[4,6,0,0,0] = expr(1)
Edge[4,7,0,0,0] = expr(1)
Edge[4,8,0,0,0] = expr(1)
Edge[4,9,0,0,0] = expr(1)
Edge[4,10,0,0,0] = expr(1)
Edge[4,11,0,0,0] = expr(1)
Edge[4,12,0,0,0] = expr(1)
Edge[4,13,0,0,0] = expr(1)
Edge[4,14,0,0,0] = expr(1)
Edge[4,15,0,0,0] = expr(1)
Edge[4,16,0,0,0] = expr(1)
Edge[4,17,0,0,0] = expr(1)
Edge[4,18,0,0,0] = expr(1)
Edge[4,19,0,0,0] = expr(1)
Edge[4,20,0,0,0] = expr(1)
Edge[4,21,0,0,0] = expr(1)
Edge[4,22,0,0,0] = expr(1)
Edge[4,23,0,0,0] = expr(1)
Edge[4,24,0,0,0] = expr(1)
Edge[4,25,0,0,0] = expr(1)
Edge[4,26,0,0,0] = expr(1)
Edge[4,27,0,0,0] = expr(1)
Edge[4,28,0,0,0] = expr(1)
Edge[4,29,0,0,0] = expr(1)
Edge[4,30,0,0,0] = expr(1)
Edge[4,31,0,0,0] = expr(1)
Edge[4,32,0,0,0] = expr(1)
Edge[4,33,0,0,0] = expr(1)
Edge[4,34,0,0,0] = expr(1)
Edge[4,35,0,0,0] = expr(1)
Edge_Net[4,0,0,0,0,0:] = exprzeros(2)
Edge_Net[4,1,0,0,0,0:] = exprzeros(2)
Edge_Net[4,2,0,0,0,0:] = exprzeros(2)
Edge_Net[4,3,0,0,0,0:] = exprzeros(2)
Edge_Net[4,4,0,0,0,0:] = exprzeros(2)
Edge_Net[4,5,0,0,0,0:] = exprzeros(2)
Edge_Net[4,6,0,0,0,0:] = exprzeros(2)
Edge_Net[4,7,0,0,0,0:] = exprzeros(2)
Edge_Net[4,8,0,0,0,0:] = exprzeros(2)
Edge_Net[4,9,0,0,0,0:] = exprzeros(2)
Edge_Net[4,10,0,0,0,0:] = exprzeros(2)
Edge_Net[4,11,0,0,0,0:] = exprzeros(2)
Edge_Net[4,12,0,0,0,0:] = exprzeros(2)
Edge_Net[4,13,0,0,0,0:] = exprzeros(2)
Edge_Net[4,14,0,0,0,0:] = exprzeros(2)
Edge_Net[4,15,0,0,0,0:] = exprzeros(2)
Edge_Net[4,16,0,0,0,0:] = exprzeros(2)
Edge_Net[4,17,0,0,0,0:] = exprzeros(2)
Edge_Net[4,18,0,0,0,0:] = exprzeros(2)
Edge_Net[4,19,0,0,0,0:] = exprzeros(2)
Edge_Net[4,20,0,0,0,0:] = exprzeros(2)
Edge_Net[4,21,0,0,0,0:] = exprzeros(2)
Edge_Net[4,22,0,0,0,0:] = exprzeros(2)
Edge_Net[4,23,0,0,0,0:] = exprzeros(2)
Edge_Net[4,24,0,0,0,0:] = exprzeros(2)
Edge_Net[4,25,0,0,0,0:] = exprzeros(2)
Edge_Net[4,26,0,0,0,0:] = exprzeros(2)
Edge_Net[4,27,0,0,0,0:] = exprzeros(2)
Edge_Net[4,28,0,0,0,0:] = exprzeros(2)
Edge_Net[4,29,0,0,0,0:] = exprzeros(2)
Edge_Net[4,30,0,0,0,0:] = exprzeros(2)
Edge_Net[4,31,0,0,0,0:] = exprzeros(2)
Edge_Net[4,32,0,0,0,0:] = exprzeros(2)
Edge_Net[4,33,0,0,0,0:] = exprzeros(2)
Edge_Net[4,34,0,0,0,0:] = exprzeros(2)
Edge_Net[4,35,0,0,0,0:] = exprzeros(2)
Edge[8,0,0,0,0] = expr(1)
Edge[8,1,0,0,0] = expr(1)
Edge[8,2,0,0,0] = expr(1)
Edge[8,3,0,0,0] = expr(1)
Edge[8,4,0,0,0] = expr(1)
Edge[8,5,0,0,0] = expr(1)
Edge[8,6,0,0,0] = expr(1)
Edge[8,7,0,0,0] = expr(1)
Edge[8,8,0,0,0] = expr(1)
Edge[8,9,0,0,0] = expr(1)
Edge[8,10,0,0,0] = expr(1)
Edge[8,11,0,0,0] = expr(1)
Edge[8,12,0,0,0] = expr(1)
Edge[8,13,0,0,0] = expr(1)
Edge[8,14,0,0,0] = expr(1)
Edge[8,15,0,0,0] = expr(1)
Edge[8,16,0,0,0] = expr(1)
Edge[8,17,0,0,0] = expr(1)
Edge[8,18,0,0,0] = expr(1)
Edge[8,19,0,0,0] = expr(1)
Edge[8,20,0,0,0] = expr(1)
Edge[8,21,0,0,0] = expr(1)
Edge[8,22,0,0,0] = expr(1)
Edge[8,23,0,0,0] = expr(1)
Edge[8,24,0,0,0] = expr(1)
Edge[8,25,0,0,0] = expr(1)
Edge[8,26,0,0,0] = expr(1)
Edge[8,27,0,0,0] = expr(1)
Edge[8,28,0,0,0] = expr(1)
Edge[8,29,0,0,0] = expr(1)
Edge[8,30,0,0,0] = expr(1)
Edge[8,31,0,0,0] = expr(1)
Edge[8,32,0,0,0] = expr(1)
Edge[8,33,0,0,0] = expr(1)
Edge[8,34,0,0,0] = expr(1)
Edge[8,35,0,0,0] = expr(1)
Edge_Net[8,0,0,0,0,0:] = exprzeros(2)
Edge_Net[8,1,0,0,0,0:] = exprzeros(2)
Edge_Net[8,2,0,0,0,0:] = exprzeros(2)
Edge_Net[8,3,0,0,0,0:] = exprzeros(2)
Edge_Net[8,4,0,0,0,0:] = exprzeros(2)
Edge_Net[8,5,0,0,0,0:] = exprzeros(2)
Edge_Net[8,6,0,0,0,0:] = exprzeros(2)
Edge_Net[8,7,0,0,0,0:] = exprzeros(2)
Edge_Net[8,8,0,0,0,0:] = exprzeros(2)
Edge_Net[8,9,0,0,0,0:] = exprzeros(2)
Edge_Net[8,10,0,0,0,0:] = exprzeros(2)
Edge_Net[8,11,0,0,0,0:] = exprzeros(2)
Edge_Net[8,12,0,0,0,0:] = exprzeros(2)
Edge_Net[8,13,0,0,0,0:] = exprzeros(2)
Edge_Net[8,14,0,0,0,0:] = exprzeros(2)
Edge_Net[8,15,0,0,0,0:] = exprzeros(2)
Edge_Net[8,16,0,0,0,0:] = exprzeros(2)
Edge_Net[8,17,0,0,0,0:] = exprzeros(2)
Edge_Net[8,18,0,0,0,0:] = exprzeros(2)
Edge_Net[8,19,0,0,0,0:] = exprzeros(2)
Edge_Net[8,20,0,0,0,0:] = exprzeros(2)
Edge_Net[8,21,0,0,0,0:] = exprzeros(2)
Edge_Net[8,22,0,0,0,0:] = exprzeros(2)
Edge_Net[8,23,0,0,0,0:] = exprzeros(2)
Edge_Net[8,24,0,0,0,0:] = exprzeros(2)
Edge_Net[8,25,0,0,0,0:] = exprzeros(2)
Edge_Net[8,26,0,0,0,0:] = exprzeros(2)
Edge_Net[8,27,0,0,0,0:] = exprzeros(2)
Edge_Net[8,28,0,0,0,0:] = exprzeros(2)
Edge_Net[8,29,0,0,0,0:] = exprzeros(2)
Edge_Net[8,30,0,0,0,0:] = exprzeros(2)
Edge_Net[8,31,0,0,0,0:] = exprzeros(2)
Edge_Net[8,32,0,0,0,0:] = exprzeros(2)
Edge_Net[8,33,0,0,0,0:] = exprzeros(2)
Edge_Net[8,34,0,0,0,0:] = exprzeros(2)
Edge_Net[8,35,0,0,0,0:] = exprzeros(2)

#Initialize P AIL1
#store in
#(L)Initialize Edge
Edge[2,1,0,0,1] = expr(1)
Edge[2,2,0,0,1] = expr(1)
Edge[2,3,0,0,1] = expr(1)
Edge[2,4,0,0,1] = expr(1)
Edge[2,5,0,0,1] = expr(1)
Edge[2,6,0,0,1] = expr(1)
Edge[2,7,0,0,1] = expr(1)
Edge[2,8,0,0,1] = expr(1)
Edge[2,9,0,0,1] = expr(1)
Edge[2,10,0,0,1] = expr(1)
Edge[2,11,0,0,1] = expr(1)
Edge[2,12,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[2,1,0,0,1,0:] = exprzeros(2)
Edge_Net[2,2,0,0,1,0:] = exprzeros(2)
Edge_Net[2,3,0,0,1,0:] = exprzeros(2)
Edge_Net[2,4,0,0,1,0:] = exprzeros(2)
Edge_Net[2,5,0,0,1,0:] = exprzeros(2)
Edge_Net[2,6,0,0,1,0:] = exprzeros(2)
Edge_Net[2,7,0,0,1,0:] = exprzeros(2)
Edge_Net[2,8,0,0,1,0:] = exprzeros(2)
Edge_Net[2,9,0,0,1,0:] = exprzeros(2)
Edge_Net[2,10,0,0,1,0:] = exprzeros(2)
Edge_Net[2,11,0,0,1,0:] = exprzeros(2)
Edge_Net[2,12,0,0,1,0:] = exprzeros(2)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[6,1,0,0,1] = expr(1)
Edge[6,2,0,0,1] = expr(1)
Edge[6,3,0,0,1] = expr(1)
Edge[6,4,0,0,1] = expr(1)
Edge[6,5,0,0,1] = expr(1)
Edge[6,6,0,0,1] = expr(1)
Edge[6,7,0,0,1] = expr(1)
Edge[6,8,0,0,1] = expr(1)
Edge[6,9,0,0,1] = expr(1)
Edge[6,10,0,0,1] = expr(1)
Edge[6,11,0,0,1] = expr(1)
Edge[6,12,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[6,1,0,0,1,0:] = exprzeros(2)
Edge_Net[6,2,0,0,1,0:] = exprzeros(2)
Edge_Net[6,3,0,0,1,0:] = exprzeros(2)
Edge_Net[6,4,0,0,1,0:] = exprzeros(2)
Edge_Net[6,5,0,0,1,0:] = exprzeros(2)
Edge_Net[6,6,0,0,1,0:] = exprzeros(2)
Edge_Net[6,7,0,0,1,0:] = exprzeros(2)
Edge_Net[6,8,0,0,1,0:] = exprzeros(2)
Edge_Net[6,9,0,0,1,0:] = exprzeros(2)
Edge_Net[6,10,0,0,1,0:] = exprzeros(2)
Edge_Net[6,11,0,0,1,0:] = exprzeros(2)
Edge_Net[6,12,0,0,1,0:] = exprzeros(2)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[2,0,1,1,1] = expr(0)
Edge[2,1,1,1,1] = expr(0)
Edge[2,2,1,1,1] = expr(0)
Edge[2,3,1,1,1] = expr(0)
Edge[2,4,1,1,1] = expr(0)
Edge[2,5,1,1,1] = expr(0)
Edge[2,6,1,1,1] = expr(0)
Edge[2,7,1,1,1] = expr(0)
Edge[2,8,1,1,1] = expr(0)
Edge[2,9,1,1,1] = expr(0)
Edge[2,10,1,1,1] = expr(0)
Edge[2,11,1,1,1] = expr(0)
Edge[2,12,1,1,1] = expr(0)
Edge[2,13,1,1,1] = expr(0)
Edge[2,0,1,1,1] = expr(0)
Edge[2,1,1,1,1] = expr(0)
Edge[2,2,1,1,1] = expr(0)
Edge[2,3,1,1,1] = expr(0)
Edge[2,4,1,1,1] = expr(0)
Edge[2,5,1,1,1] = expr(0)
Edge[2,6,1,1,1] = expr(0)
Edge[2,7,1,1,1] = expr(0)
Edge[2,8,1,1,1] = expr(0)
Edge[2,9,1,1,1] = expr(0)
Edge[2,10,1,1,1] = expr(0)
Edge[2,11,1,1,1] = expr(0)
Edge[2,12,1,1,1] = expr(0)
Edge[2,13,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[6,0,1,1,1] = expr(0)
Edge[6,1,1,1,1] = expr(0)
Edge[6,2,1,1,1] = expr(0)
Edge[6,3,1,1,1] = expr(0)
Edge[6,4,1,1,1] = expr(0)
Edge[6,5,1,1,1] = expr(0)
Edge[6,6,1,1,1] = expr(0)
Edge[6,7,1,1,1] = expr(0)
Edge[6,8,1,1,1] = expr(0)
Edge[6,9,1,1,1] = expr(0)
Edge[6,10,1,1,1] = expr(0)
Edge[6,11,1,1,1] = expr(0)
Edge[6,12,1,1,1] = expr(0)
Edge[6,13,1,1,1] = expr(0)
Edge[6,0,1,1,1] = expr(0)
Edge[6,1,1,1,1] = expr(0)
Edge[6,2,1,1,1] = expr(0)
Edge[6,3,1,1,1] = expr(0)
Edge[6,4,1,1,1] = expr(0)
Edge[6,5,1,1,1] = expr(0)
Edge[6,6,1,1,1] = expr(0)
Edge[6,7,1,1,1] = expr(0)
Edge[6,8,1,1,1] = expr(0)
Edge[6,9,1,1,1] = expr(0)
Edge[6,10,1,1,1] = expr(0)
Edge[6,11,1,1,1] = expr(0)
Edge[6,12,1,1,1] = expr(0)
Edge[6,13,1,1,1] = expr(0)
#(R)End disable GIL

#Initialize N AIL1
Edge[2,22,0,0,1] = expr(1)
Edge[2,23,0,0,1] = expr(1)
Edge[2,24,0,0,1] = expr(1)
Edge[2,25,0,0,1] = expr(1)
Edge[2,26,0,0,1] = expr(1)
Edge[2,27,0,0,1] = expr(1)
Edge[2,28,0,0,1] = expr(1)
Edge[2,29,0,0,1] = expr(1)
Edge[2,30,0,0,1] = expr(1)
Edge[2,31,0,0,1] = expr(1)
Edge[2,32,0,0,1] = expr(1)
Edge[2,33,0,0,1] = expr(1)
Edge_Net[2,22,0,0,1,0:] = exprzeros(2)
Edge_Net[2,23,0,0,1,0:] = exprzeros(2)
Edge_Net[2,24,0,0,1,0:] = exprzeros(2)
Edge_Net[2,25,0,0,1,0:] = exprzeros(2)
Edge_Net[2,26,0,0,1,0:] = exprzeros(2)
Edge_Net[2,27,0,0,1,0:] = exprzeros(2)
Edge_Net[2,28,0,0,1,0:] = exprzeros(2)
Edge_Net[2,29,0,0,1,0:] = exprzeros(2)
Edge_Net[2,30,0,0,1,0:] = exprzeros(2)
Edge_Net[2,31,0,0,1,0:] = exprzeros(2)
Edge_Net[2,32,0,0,1,0:] = exprzeros(2)
Edge_Net[2,33,0,0,1,0:] = exprzeros(2)
Edge[6,22,0,0,1] = expr(1)
Edge[6,23,0,0,1] = expr(1)
Edge[6,24,0,0,1] = expr(1)
Edge[6,25,0,0,1] = expr(1)
Edge[6,26,0,0,1] = expr(1)
Edge[6,27,0,0,1] = expr(1)
Edge[6,28,0,0,1] = expr(1)
Edge[6,29,0,0,1] = expr(1)
Edge[6,30,0,0,1] = expr(1)
Edge[6,31,0,0,1] = expr(1)
Edge[6,32,0,0,1] = expr(1)
Edge[6,33,0,0,1] = expr(1)
Edge_Net[6,22,0,0,1,0:] = exprzeros(2)
Edge_Net[6,23,0,0,1,0:] = exprzeros(2)
Edge_Net[6,24,0,0,1,0:] = exprzeros(2)
Edge_Net[6,25,0,0,1,0:] = exprzeros(2)
Edge_Net[6,26,0,0,1,0:] = exprzeros(2)
Edge_Net[6,27,0,0,1,0:] = exprzeros(2)
Edge_Net[6,28,0,0,1,0:] = exprzeros(2)
Edge_Net[6,29,0,0,1,0:] = exprzeros(2)
Edge_Net[6,30,0,0,1,0:] = exprzeros(2)
Edge_Net[6,31,0,0,1,0:] = exprzeros(2)
Edge_Net[6,32,0,0,1,0:] = exprzeros(2)
Edge_Net[6,33,0,0,1,0:] = exprzeros(2)
Edge[2,21,1,1,1] = expr(0)
Edge[2,22,1,1,1] = expr(0)
Edge[2,23,1,1,1] = expr(0)
Edge[2,24,1,1,1] = expr(0)
Edge[2,25,1,1,1] = expr(0)
Edge[2,26,1,1,1] = expr(0)
Edge[2,27,1,1,1] = expr(0)
Edge[2,28,1,1,1] = expr(0)
Edge[2,29,1,1,1] = expr(0)
Edge[2,30,1,1,1] = expr(0)
Edge[2,31,1,1,1] = expr(0)
Edge[2,32,1,1,1] = expr(0)
Edge[2,33,1,1,1] = expr(0)
Edge[2,34,1,1,1] = expr(0)
Edge[2,35,1,1,1] = expr(0)
Edge[6,21,1,1,1] = expr(0)
Edge[6,22,1,1,1] = expr(0)
Edge[6,23,1,1,1] = expr(0)
Edge[6,24,1,1,1] = expr(0)
Edge[6,25,1,1,1] = expr(0)
Edge[6,26,1,1,1] = expr(0)
Edge[6,27,1,1,1] = expr(0)
Edge[6,28,1,1,1] = expr(0)
Edge[6,29,1,1,1] = expr(0)
Edge[6,30,1,1,1] = expr(0)
Edge[6,31,1,1,1] = expr(0)
Edge[6,32,1,1,1] = expr(0)
Edge[6,33,1,1,1] = expr(0)
Edge[6,34,1,1,1] = expr(0)
Edge[6,35,1,1,1] = expr(0)

FORMULA = And()
endTime = time.time()
print('Total Time = ', endTime-startTime)
setOut.clauseDistribution(FORMULA)
setOut.setUpLayoutViaFromResult(FORMULA.satisfy_one(),outLayout,subnetRec,2)
print('#edge = 6545')