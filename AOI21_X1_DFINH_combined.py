from pyeda.inter import *
import RConstraints
import time
import setOut
startTime = time.time()
# ===> Instruction(Create)  2D Routing Style p(e) <===
# ===> Edges[X, Y, Z, Trends, Masks]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge = exprvars('edge', 26, 36, 4, 3, 3)

# ===> Instruction(Create)  2D Routing Style p(e,n) <===
# ===> Edge_Net[X, Y, Z, Trends, Masks, Nets]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge_Net = exprvars('edge_net', 26, 36, 4, 3, 3, 5)

# ===> Instruction(Create)  2D Routing Style p(e,n,s) <===
# ===> Edge_Net_Subnet_NetID[X, Y, Z, Trends, Masks, Subnets]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge_Net_Subnet2 = exprvars('edge_net_subnet2', 26, 36, 4, 3, 3, 1)
Edge_Net_Subnet3 = exprvars('edge_net_subnet3', 26, 36, 4, 3, 3, 1)

outLayout=[[[[0 for trend in range(3)] for z in range(4)] for y in range(36)] for x in range(26)]

subnetRec=[[[[0 for trend in range(3)] for z in range(4)] for y in range(36)] for x in range(26)]

MaxX = 25
MaxY = 35
MaxZ = 3
#Net = 5
#cellName = AOI21_X1_DFINH_combined
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
Edge_Net[0,0,0,0,0,0:] = exprzeros(5)
Edge_Net[0,1,0,0,0,0:] = exprzeros(5)
Edge_Net[0,2,0,0,0,0:] = exprzeros(5)
Edge_Net[0,3,0,0,0,0:] = exprzeros(5)
Edge_Net[0,4,0,0,0,0:] = exprzeros(5)
Edge_Net[0,5,0,0,0,0:] = exprzeros(5)
Edge_Net[0,6,0,0,0,0:] = exprzeros(5)
Edge_Net[0,7,0,0,0,0:] = exprzeros(5)
Edge_Net[0,8,0,0,0,0:] = exprzeros(5)
Edge_Net[0,9,0,0,0,0:] = exprzeros(5)
Edge_Net[0,10,0,0,0,0:] = exprzeros(5)
Edge_Net[0,11,0,0,0,0:] = exprzeros(5)
Edge_Net[0,12,0,0,0,0:] = exprzeros(5)
Edge_Net[0,13,0,0,0,0:] = exprzeros(5)
Edge_Net[0,14,0,0,0,0:] = exprzeros(5)
Edge_Net[0,15,0,0,0,0:] = exprzeros(5)
Edge_Net[0,16,0,0,0,0:] = exprzeros(5)
Edge_Net[0,17,0,0,0,0:] = exprzeros(5)
Edge_Net[0,18,0,0,0,0:] = exprzeros(5)
Edge_Net[0,19,0,0,0,0:] = exprzeros(5)
Edge_Net[0,20,0,0,0,0:] = exprzeros(5)
Edge_Net[0,21,0,0,0,0:] = exprzeros(5)
Edge_Net[0,22,0,0,0,0:] = exprzeros(5)
Edge_Net[0,23,0,0,0,0:] = exprzeros(5)
Edge_Net[0,24,0,0,0,0:] = exprzeros(5)
Edge_Net[0,25,0,0,0,0:] = exprzeros(5)
Edge_Net[0,26,0,0,0,0:] = exprzeros(5)
Edge_Net[0,27,0,0,0,0:] = exprzeros(5)
Edge_Net[0,28,0,0,0,0:] = exprzeros(5)
Edge_Net[0,29,0,0,0,0:] = exprzeros(5)
Edge_Net[0,30,0,0,0,0:] = exprzeros(5)
Edge_Net[0,31,0,0,0,0:] = exprzeros(5)
Edge_Net[0,32,0,0,0,0:] = exprzeros(5)
Edge_Net[0,33,0,0,0,0:] = exprzeros(5)
Edge_Net[0,34,0,0,0,0:] = exprzeros(5)
Edge_Net[0,35,0,0,0,0:] = exprzeros(5)
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
Edge_Net[4,0,0,0,0,0:] = exprzeros(5)
Edge_Net[4,1,0,0,0,0:] = exprzeros(5)
Edge_Net[4,2,0,0,0,0:] = exprzeros(5)
Edge_Net[4,3,0,0,0,0:] = exprzeros(5)
Edge_Net[4,4,0,0,0,0:] = exprzeros(5)
Edge_Net[4,5,0,0,0,0:] = exprzeros(5)
Edge_Net[4,6,0,0,0,0:] = exprzeros(5)
Edge_Net[4,7,0,0,0,0:] = exprzeros(5)
Edge_Net[4,8,0,0,0,0:] = exprzeros(5)
Edge_Net[4,9,0,0,0,0:] = exprzeros(5)
Edge_Net[4,10,0,0,0,0:] = exprzeros(5)
Edge_Net[4,11,0,0,0,0:] = exprzeros(5)
Edge_Net[4,12,0,0,0,0:] = exprzeros(5)
Edge_Net[4,13,0,0,0,0:] = exprzeros(5)
Edge_Net[4,14,0,0,0,0:] = exprzeros(5)
Edge_Net[4,15,0,0,0,0:] = exprzeros(5)
Edge_Net[4,16,0,0,0,0:] = exprzeros(5)
Edge_Net[4,17,0,0,0,0:] = exprzeros(5)
Edge_Net[4,18,0,0,0,0:] = exprzeros(5)
Edge_Net[4,19,0,0,0,0:] = exprzeros(5)
Edge_Net[4,20,0,0,0,0:] = exprzeros(5)
Edge_Net[4,21,0,0,0,0:] = exprzeros(5)
Edge_Net[4,22,0,0,0,0:] = exprzeros(5)
Edge_Net[4,23,0,0,0,0:] = exprzeros(5)
Edge_Net[4,24,0,0,0,0:] = exprzeros(5)
Edge_Net[4,25,0,0,0,0:] = exprzeros(5)
Edge_Net[4,26,0,0,0,0:] = exprzeros(5)
Edge_Net[4,27,0,0,0,0:] = exprzeros(5)
Edge_Net[4,28,0,0,0,0:] = exprzeros(5)
Edge_Net[4,29,0,0,0,0:] = exprzeros(5)
Edge_Net[4,30,0,0,0,0:] = exprzeros(5)
Edge_Net[4,31,0,0,0,0:] = exprzeros(5)
Edge_Net[4,32,0,0,0,0:] = exprzeros(5)
Edge_Net[4,33,0,0,0,0:] = exprzeros(5)
Edge_Net[4,34,0,0,0,0:] = exprzeros(5)
Edge_Net[4,35,0,0,0,0:] = exprzeros(5)
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
Edge_Net[8,0,0,0,0,0:] = exprzeros(5)
Edge_Net[8,1,0,0,0,0:] = exprzeros(5)
Edge_Net[8,2,0,0,0,0:] = exprzeros(5)
Edge_Net[8,3,0,0,0,0:] = exprzeros(5)
Edge_Net[8,4,0,0,0,0:] = exprzeros(5)
Edge_Net[8,5,0,0,0,0:] = exprzeros(5)
Edge_Net[8,6,0,0,0,0:] = exprzeros(5)
Edge_Net[8,7,0,0,0,0:] = exprzeros(5)
Edge_Net[8,8,0,0,0,0:] = exprzeros(5)
Edge_Net[8,9,0,0,0,0:] = exprzeros(5)
Edge_Net[8,10,0,0,0,0:] = exprzeros(5)
Edge_Net[8,11,0,0,0,0:] = exprzeros(5)
Edge_Net[8,12,0,0,0,0:] = exprzeros(5)
Edge_Net[8,13,0,0,0,0:] = exprzeros(5)
Edge_Net[8,14,0,0,0,0:] = exprzeros(5)
Edge_Net[8,15,0,0,0,0:] = exprzeros(5)
Edge_Net[8,16,0,0,0,0:] = exprzeros(5)
Edge_Net[8,17,0,0,0,0:] = exprzeros(5)
Edge_Net[8,18,0,0,0,0:] = exprzeros(5)
Edge_Net[8,19,0,0,0,0:] = exprzeros(5)
Edge_Net[8,20,0,0,0,0:] = exprzeros(5)
Edge_Net[8,21,0,0,0,0:] = exprzeros(5)
Edge_Net[8,22,0,0,0,0:] = exprzeros(5)
Edge_Net[8,23,0,0,0,0:] = exprzeros(5)
Edge_Net[8,24,0,0,0,0:] = exprzeros(5)
Edge_Net[8,25,0,0,0,0:] = exprzeros(5)
Edge_Net[8,26,0,0,0,0:] = exprzeros(5)
Edge_Net[8,27,0,0,0,0:] = exprzeros(5)
Edge_Net[8,28,0,0,0,0:] = exprzeros(5)
Edge_Net[8,29,0,0,0,0:] = exprzeros(5)
Edge_Net[8,30,0,0,0,0:] = exprzeros(5)
Edge_Net[8,31,0,0,0,0:] = exprzeros(5)
Edge_Net[8,32,0,0,0,0:] = exprzeros(5)
Edge_Net[8,33,0,0,0,0:] = exprzeros(5)
Edge_Net[8,34,0,0,0,0:] = exprzeros(5)
Edge_Net[8,35,0,0,0,0:] = exprzeros(5)
Edge[12,0,0,0,0] = expr(1)
Edge[12,1,0,0,0] = expr(1)
Edge[12,2,0,0,0] = expr(1)
Edge[12,3,0,0,0] = expr(1)
Edge[12,4,0,0,0] = expr(1)
Edge[12,5,0,0,0] = expr(1)
Edge[12,6,0,0,0] = expr(1)
Edge[12,7,0,0,0] = expr(1)
Edge[12,8,0,0,0] = expr(1)
Edge[12,9,0,0,0] = expr(1)
Edge[12,10,0,0,0] = expr(1)
Edge[12,11,0,0,0] = expr(1)
Edge[12,12,0,0,0] = expr(1)
Edge[12,13,0,0,0] = expr(1)
Edge[12,14,0,0,0] = expr(1)
Edge[12,15,0,0,0] = expr(1)
Edge[12,16,0,0,0] = expr(1)
Edge[12,17,0,0,0] = expr(1)
Edge[12,18,0,0,0] = expr(1)
Edge[12,19,0,0,0] = expr(1)
Edge[12,20,0,0,0] = expr(1)
Edge[12,21,0,0,0] = expr(1)
Edge[12,22,0,0,0] = expr(1)
Edge[12,23,0,0,0] = expr(1)
Edge[12,24,0,0,0] = expr(1)
Edge[12,25,0,0,0] = expr(1)
Edge[12,26,0,0,0] = expr(1)
Edge[12,27,0,0,0] = expr(1)
Edge[12,28,0,0,0] = expr(1)
Edge[12,29,0,0,0] = expr(1)
Edge[12,30,0,0,0] = expr(1)
Edge[12,31,0,0,0] = expr(1)
Edge[12,32,0,0,0] = expr(1)
Edge[12,33,0,0,0] = expr(1)
Edge[12,34,0,0,0] = expr(1)
Edge[12,35,0,0,0] = expr(1)
Edge_Net[12,0,0,0,0,0:] = exprzeros(5)
Edge_Net[12,1,0,0,0,0:] = exprzeros(5)
Edge_Net[12,2,0,0,0,0:] = exprzeros(5)
Edge_Net[12,3,0,0,0,0:] = exprzeros(5)
Edge_Net[12,4,0,0,0,0:] = exprzeros(5)
Edge_Net[12,5,0,0,0,0:] = exprzeros(5)
Edge_Net[12,6,0,0,0,0:] = exprzeros(5)
Edge_Net[12,7,0,0,0,0:] = exprzeros(5)
Edge_Net[12,8,0,0,0,0:] = exprzeros(5)
Edge_Net[12,9,0,0,0,0:] = exprzeros(5)
Edge_Net[12,10,0,0,0,0:] = exprzeros(5)
Edge_Net[12,11,0,0,0,0:] = exprzeros(5)
Edge_Net[12,12,0,0,0,0:] = exprzeros(5)
Edge_Net[12,13,0,0,0,0:] = exprzeros(5)
Edge_Net[12,14,0,0,0,0:] = exprzeros(5)
Edge_Net[12,15,0,0,0,0:] = exprzeros(5)
Edge_Net[12,16,0,0,0,0:] = exprzeros(5)
Edge_Net[12,17,0,0,0,0:] = exprzeros(5)
Edge_Net[12,18,0,0,0,0:] = exprzeros(5)
Edge_Net[12,19,0,0,0,0:] = exprzeros(5)
Edge_Net[12,20,0,0,0,0:] = exprzeros(5)
Edge_Net[12,21,0,0,0,0:] = exprzeros(5)
Edge_Net[12,22,0,0,0,0:] = exprzeros(5)
Edge_Net[12,23,0,0,0,0:] = exprzeros(5)
Edge_Net[12,24,0,0,0,0:] = exprzeros(5)
Edge_Net[12,25,0,0,0,0:] = exprzeros(5)
Edge_Net[12,26,0,0,0,0:] = exprzeros(5)
Edge_Net[12,27,0,0,0,0:] = exprzeros(5)
Edge_Net[12,28,0,0,0,0:] = exprzeros(5)
Edge_Net[12,29,0,0,0,0:] = exprzeros(5)
Edge_Net[12,30,0,0,0,0:] = exprzeros(5)
Edge_Net[12,31,0,0,0,0:] = exprzeros(5)
Edge_Net[12,32,0,0,0,0:] = exprzeros(5)
Edge_Net[12,33,0,0,0,0:] = exprzeros(5)
Edge_Net[12,34,0,0,0,0:] = exprzeros(5)
Edge_Net[12,35,0,0,0,0:] = exprzeros(5)
Edge[16,0,0,0,0] = expr(1)
Edge[16,1,0,0,0] = expr(1)
Edge[16,2,0,0,0] = expr(1)
Edge[16,3,0,0,0] = expr(1)
Edge[16,4,0,0,0] = expr(1)
Edge[16,5,0,0,0] = expr(1)
Edge[16,6,0,0,0] = expr(1)
Edge[16,7,0,0,0] = expr(1)
Edge[16,8,0,0,0] = expr(1)
Edge[16,9,0,0,0] = expr(1)
Edge[16,10,0,0,0] = expr(1)
Edge[16,11,0,0,0] = expr(1)
Edge[16,12,0,0,0] = expr(1)
Edge[16,13,0,0,0] = expr(1)
Edge[16,14,0,0,0] = expr(1)
Edge[16,15,0,0,0] = expr(1)
Edge[16,16,0,0,0] = expr(1)
Edge[16,17,0,0,0] = expr(1)
Edge[16,18,0,0,0] = expr(1)
Edge[16,19,0,0,0] = expr(1)
Edge[16,20,0,0,0] = expr(1)
Edge[16,21,0,0,0] = expr(1)
Edge[16,22,0,0,0] = expr(1)
Edge[16,23,0,0,0] = expr(1)
Edge[16,24,0,0,0] = expr(1)
Edge[16,25,0,0,0] = expr(1)
Edge[16,26,0,0,0] = expr(1)
Edge[16,27,0,0,0] = expr(1)
Edge[16,28,0,0,0] = expr(1)
Edge[16,29,0,0,0] = expr(1)
Edge[16,30,0,0,0] = expr(1)
Edge[16,31,0,0,0] = expr(1)
Edge[16,32,0,0,0] = expr(1)
Edge[16,33,0,0,0] = expr(1)
Edge[16,34,0,0,0] = expr(1)
Edge[16,35,0,0,0] = expr(1)
Edge_Net[16,0,0,0,0,0:] = exprzeros(5)
Edge_Net[16,1,0,0,0,0:] = exprzeros(5)
Edge_Net[16,2,0,0,0,0:] = exprzeros(5)
Edge_Net[16,3,0,0,0,0:] = exprzeros(5)
Edge_Net[16,4,0,0,0,0:] = exprzeros(5)
Edge_Net[16,5,0,0,0,0:] = exprzeros(5)
Edge_Net[16,6,0,0,0,0:] = exprzeros(5)
Edge_Net[16,7,0,0,0,0:] = exprzeros(5)
Edge_Net[16,8,0,0,0,0:] = exprzeros(5)
Edge_Net[16,9,0,0,0,0:] = exprzeros(5)
Edge_Net[16,10,0,0,0,0:] = exprzeros(5)
Edge_Net[16,11,0,0,0,0:] = exprzeros(5)
Edge_Net[16,12,0,0,0,0:] = exprzeros(5)
Edge_Net[16,13,0,0,0,0:] = exprzeros(5)
Edge_Net[16,14,0,0,0,0:] = exprzeros(5)
Edge_Net[16,15,0,0,0,0:] = exprzeros(5)
Edge_Net[16,16,0,0,0,0:] = exprzeros(5)
Edge_Net[16,17,0,0,0,0:] = exprzeros(5)
Edge_Net[16,18,0,0,0,0:] = exprzeros(5)
Edge_Net[16,19,0,0,0,0:] = exprzeros(5)
Edge_Net[16,20,0,0,0,0:] = exprzeros(5)
Edge_Net[16,21,0,0,0,0:] = exprzeros(5)
Edge_Net[16,22,0,0,0,0:] = exprzeros(5)
Edge_Net[16,23,0,0,0,0:] = exprzeros(5)
Edge_Net[16,24,0,0,0,0:] = exprzeros(5)
Edge_Net[16,25,0,0,0,0:] = exprzeros(5)
Edge_Net[16,26,0,0,0,0:] = exprzeros(5)
Edge_Net[16,27,0,0,0,0:] = exprzeros(5)
Edge_Net[16,28,0,0,0,0:] = exprzeros(5)
Edge_Net[16,29,0,0,0,0:] = exprzeros(5)
Edge_Net[16,30,0,0,0,0:] = exprzeros(5)
Edge_Net[16,31,0,0,0,0:] = exprzeros(5)
Edge_Net[16,32,0,0,0,0:] = exprzeros(5)
Edge_Net[16,33,0,0,0,0:] = exprzeros(5)
Edge_Net[16,34,0,0,0,0:] = exprzeros(5)
Edge_Net[16,35,0,0,0,0:] = exprzeros(5)

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
Edge_Net[2,1,0,0,1,0:] = exprzeros(5)
Edge_Net[2,2,0,0,1,0:] = exprzeros(5)
Edge_Net[2,3,0,0,1,0:] = exprzeros(5)
Edge_Net[2,4,0,0,1,0:] = exprzeros(5)
Edge_Net[2,5,0,0,1,0:] = exprzeros(5)
Edge_Net[2,6,0,0,1,0:] = exprzeros(5)
Edge_Net[2,7,0,0,1,0:] = exprzeros(5)
Edge_Net[2,8,0,0,1,0:] = exprzeros(5)
Edge_Net[2,9,0,0,1,0:] = exprzeros(5)
Edge_Net[2,10,0,0,1,0:] = exprzeros(5)
Edge_Net[2,11,0,0,1,0:] = exprzeros(5)
Edge_Net[2,12,0,0,1,0:] = exprzeros(5)
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
Edge_Net[6,1,0,0,1,0:] = exprzeros(5)
Edge_Net[6,2,0,0,1,0:] = exprzeros(5)
Edge_Net[6,3,0,0,1,0:] = exprzeros(5)
Edge_Net[6,4,0,0,1,0:] = exprzeros(5)
Edge_Net[6,5,0,0,1,0:] = exprzeros(5)
Edge_Net[6,6,0,0,1,0:] = exprzeros(5)
Edge_Net[6,7,0,0,1,0:] = exprzeros(5)
Edge_Net[6,8,0,0,1,0:] = exprzeros(5)
Edge_Net[6,9,0,0,1,0:] = exprzeros(5)
Edge_Net[6,10,0,0,1,0:] = exprzeros(5)
Edge_Net[6,11,0,0,1,0:] = exprzeros(5)
Edge_Net[6,12,0,0,1,0:] = exprzeros(5)
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
#store in
#(L)Initialize Edge
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
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[6,1,0,0,1,0:] = exprzeros(5)
Edge_Net[6,2,0,0,1,0:] = exprzeros(5)
Edge_Net[6,3,0,0,1,0:] = exprzeros(5)
Edge_Net[6,4,0,0,1,0:] = exprzeros(5)
Edge_Net[6,5,0,0,1,0:] = exprzeros(5)
Edge_Net[6,6,0,0,1,0:] = exprzeros(5)
Edge_Net[6,7,0,0,1,0:] = exprzeros(5)
Edge_Net[6,8,0,0,1,0:] = exprzeros(5)
Edge_Net[6,9,0,0,1,0:] = exprzeros(5)
Edge_Net[6,10,0,0,1,0:] = exprzeros(5)
Edge_Net[6,11,0,0,1,0:] = exprzeros(5)
Edge_Net[6,12,0,0,1,0:] = exprzeros(5)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[10,1,0,0,1] = expr(1)
Edge[10,2,0,0,1] = expr(1)
Edge[10,3,0,0,1] = expr(1)
Edge[10,4,0,0,1] = expr(1)
Edge[10,5,0,0,1] = expr(1)
Edge[10,6,0,0,1] = expr(1)
Edge[10,7,0,0,1] = expr(1)
Edge[10,8,0,0,1] = expr(1)
Edge[10,9,0,0,1] = expr(1)
Edge[10,10,0,0,1] = expr(1)
Edge[10,11,0,0,1] = expr(1)
Edge[10,12,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[10,1,0,0,1,0:] = exprzeros(5)
Edge_Net[10,2,0,0,1,0:] = exprzeros(5)
Edge_Net[10,3,0,0,1,0:] = exprzeros(5)
Edge_Net[10,4,0,0,1,0:] = exprzeros(5)
Edge_Net[10,5,0,0,1,0:] = exprzeros(5)
Edge_Net[10,6,0,0,1,0:] = exprzeros(5)
Edge_Net[10,7,0,0,1,0:] = exprzeros(5)
Edge_Net[10,8,0,0,1,0:] = exprzeros(5)
Edge_Net[10,9,0,0,1,0:] = exprzeros(5)
Edge_Net[10,10,0,0,1,0:] = exprzeros(5)
Edge_Net[10,11,0,0,1,0:] = exprzeros(5)
Edge_Net[10,12,0,0,1,0:] = exprzeros(5)
#(R)End initialize EdgeNet
#(L)Disable GIL
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
#(L)End disable GIL
#(R)Disable GIL
Edge[10,0,1,1,1] = expr(0)
Edge[10,1,1,1,1] = expr(0)
Edge[10,2,1,1,1] = expr(0)
Edge[10,3,1,1,1] = expr(0)
Edge[10,4,1,1,1] = expr(0)
Edge[10,5,1,1,1] = expr(0)
Edge[10,6,1,1,1] = expr(0)
Edge[10,7,1,1,1] = expr(0)
Edge[10,8,1,1,1] = expr(0)
Edge[10,9,1,1,1] = expr(0)
Edge[10,10,1,1,1] = expr(0)
Edge[10,11,1,1,1] = expr(0)
Edge[10,12,1,1,1] = expr(0)
Edge[10,13,1,1,1] = expr(0)
Edge[10,0,1,1,1] = expr(0)
Edge[10,1,1,1,1] = expr(0)
Edge[10,2,1,1,1] = expr(0)
Edge[10,3,1,1,1] = expr(0)
Edge[10,4,1,1,1] = expr(0)
Edge[10,5,1,1,1] = expr(0)
Edge[10,6,1,1,1] = expr(0)
Edge[10,7,1,1,1] = expr(0)
Edge[10,8,1,1,1] = expr(0)
Edge[10,9,1,1,1] = expr(0)
Edge[10,10,1,1,1] = expr(0)
Edge[10,11,1,1,1] = expr(0)
Edge[10,12,1,1,1] = expr(0)
Edge[10,13,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[10,1,0,0,1] = expr(1)
Edge[10,2,0,0,1] = expr(1)
Edge[10,3,0,0,1] = expr(1)
Edge[10,4,0,0,1] = expr(1)
Edge[10,5,0,0,1] = expr(1)
Edge[10,6,0,0,1] = expr(1)
Edge[10,7,0,0,1] = expr(1)
Edge[10,8,0,0,1] = expr(1)
Edge[10,9,0,0,1] = expr(1)
Edge[10,10,0,0,1] = expr(1)
Edge[10,11,0,0,1] = expr(1)
Edge[10,12,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[10,1,0,0,1,0:] = exprzeros(5)
Edge_Net[10,2,0,0,1,0:] = exprzeros(5)
Edge_Net[10,3,0,0,1,0:] = exprzeros(5)
Edge_Net[10,4,0,0,1,0:] = exprzeros(5)
Edge_Net[10,5,0,0,1,0:] = exprzeros(5)
Edge_Net[10,6,0,0,1,0:] = exprzeros(5)
Edge_Net[10,7,0,0,1,0:] = exprzeros(5)
Edge_Net[10,8,0,0,1,0:] = exprzeros(5)
Edge_Net[10,9,0,0,1,0:] = exprzeros(5)
Edge_Net[10,10,0,0,1,0:] = exprzeros(5)
Edge_Net[10,11,0,0,1,0:] = exprzeros(5)
Edge_Net[10,12,0,0,1,0:] = exprzeros(5)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[14,1,0,0,1] = expr(1)
Edge[14,2,0,0,1] = expr(1)
Edge[14,3,0,0,1] = expr(1)
Edge[14,4,0,0,1] = expr(1)
Edge[14,5,0,0,1] = expr(1)
Edge[14,6,0,0,1] = expr(1)
Edge[14,7,0,0,1] = expr(1)
Edge[14,8,0,0,1] = expr(1)
Edge[14,9,0,0,1] = expr(1)
Edge[14,10,0,0,1] = expr(1)
Edge[14,11,0,0,1] = expr(1)
Edge[14,12,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[14,1,0,0,1,0:] = exprzeros(5)
Edge_Net[14,2,0,0,1,0:] = exprzeros(5)
Edge_Net[14,3,0,0,1,0:] = exprzeros(5)
Edge_Net[14,4,0,0,1,0:] = exprzeros(5)
Edge_Net[14,5,0,0,1,0:] = exprzeros(5)
Edge_Net[14,6,0,0,1,0:] = exprzeros(5)
Edge_Net[14,7,0,0,1,0:] = exprzeros(5)
Edge_Net[14,8,0,0,1,0:] = exprzeros(5)
Edge_Net[14,9,0,0,1,0:] = exprzeros(5)
Edge_Net[14,10,0,0,1,0:] = exprzeros(5)
Edge_Net[14,11,0,0,1,0:] = exprzeros(5)
Edge_Net[14,12,0,0,1,0:] = exprzeros(5)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[10,0,1,1,1] = expr(0)
Edge[10,1,1,1,1] = expr(0)
Edge[10,2,1,1,1] = expr(0)
Edge[10,3,1,1,1] = expr(0)
Edge[10,4,1,1,1] = expr(0)
Edge[10,5,1,1,1] = expr(0)
Edge[10,6,1,1,1] = expr(0)
Edge[10,7,1,1,1] = expr(0)
Edge[10,8,1,1,1] = expr(0)
Edge[10,9,1,1,1] = expr(0)
Edge[10,10,1,1,1] = expr(0)
Edge[10,11,1,1,1] = expr(0)
Edge[10,12,1,1,1] = expr(0)
Edge[10,13,1,1,1] = expr(0)
Edge[10,0,1,1,1] = expr(0)
Edge[10,1,1,1,1] = expr(0)
Edge[10,2,1,1,1] = expr(0)
Edge[10,3,1,1,1] = expr(0)
Edge[10,4,1,1,1] = expr(0)
Edge[10,5,1,1,1] = expr(0)
Edge[10,6,1,1,1] = expr(0)
Edge[10,7,1,1,1] = expr(0)
Edge[10,8,1,1,1] = expr(0)
Edge[10,9,1,1,1] = expr(0)
Edge[10,10,1,1,1] = expr(0)
Edge[10,11,1,1,1] = expr(0)
Edge[10,12,1,1,1] = expr(0)
Edge[10,13,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[14,0,1,1,1] = expr(0)
Edge[14,1,1,1,1] = expr(0)
Edge[14,2,1,1,1] = expr(0)
Edge[14,3,1,1,1] = expr(0)
Edge[14,4,1,1,1] = expr(0)
Edge[14,5,1,1,1] = expr(0)
Edge[14,6,1,1,1] = expr(0)
Edge[14,7,1,1,1] = expr(0)
Edge[14,8,1,1,1] = expr(0)
Edge[14,9,1,1,1] = expr(0)
Edge[14,10,1,1,1] = expr(0)
Edge[14,11,1,1,1] = expr(0)
Edge[14,12,1,1,1] = expr(0)
Edge[14,13,1,1,1] = expr(0)
Edge[14,0,1,1,1] = expr(0)
Edge[14,1,1,1,1] = expr(0)
Edge[14,2,1,1,1] = expr(0)
Edge[14,3,1,1,1] = expr(0)
Edge[14,4,1,1,1] = expr(0)
Edge[14,5,1,1,1] = expr(0)
Edge[14,6,1,1,1] = expr(0)
Edge[14,7,1,1,1] = expr(0)
Edge[14,8,1,1,1] = expr(0)
Edge[14,9,1,1,1] = expr(0)
Edge[14,10,1,1,1] = expr(0)
Edge[14,11,1,1,1] = expr(0)
Edge[14,12,1,1,1] = expr(0)
Edge[14,13,1,1,1] = expr(0)
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
Edge_Net[2,22,0,0,1,0:] = exprzeros(5)
Edge_Net[2,23,0,0,1,0:] = exprzeros(5)
Edge_Net[2,24,0,0,1,0:] = exprzeros(5)
Edge_Net[2,25,0,0,1,0:] = exprzeros(5)
Edge_Net[2,26,0,0,1,0:] = exprzeros(5)
Edge_Net[2,27,0,0,1,0:] = exprzeros(5)
Edge_Net[2,28,0,0,1,0:] = exprzeros(5)
Edge_Net[2,29,0,0,1,0:] = exprzeros(5)
Edge_Net[2,30,0,0,1,0:] = exprzeros(5)
Edge_Net[2,31,0,0,1,0:] = exprzeros(5)
Edge_Net[2,32,0,0,1,0:] = exprzeros(5)
Edge_Net[2,33,0,0,1,0:] = exprzeros(5)
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
Edge_Net[6,22,0,0,1,0:] = exprzeros(5)
Edge_Net[6,23,0,0,1,0:] = exprzeros(5)
Edge_Net[6,24,0,0,1,0:] = exprzeros(5)
Edge_Net[6,25,0,0,1,0:] = exprzeros(5)
Edge_Net[6,26,0,0,1,0:] = exprzeros(5)
Edge_Net[6,27,0,0,1,0:] = exprzeros(5)
Edge_Net[6,28,0,0,1,0:] = exprzeros(5)
Edge_Net[6,29,0,0,1,0:] = exprzeros(5)
Edge_Net[6,30,0,0,1,0:] = exprzeros(5)
Edge_Net[6,31,0,0,1,0:] = exprzeros(5)
Edge_Net[6,32,0,0,1,0:] = exprzeros(5)
Edge_Net[6,33,0,0,1,0:] = exprzeros(5)
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
Edge_Net[6,22,0,0,1,0:] = exprzeros(5)
Edge_Net[6,23,0,0,1,0:] = exprzeros(5)
Edge_Net[6,24,0,0,1,0:] = exprzeros(5)
Edge_Net[6,25,0,0,1,0:] = exprzeros(5)
Edge_Net[6,26,0,0,1,0:] = exprzeros(5)
Edge_Net[6,27,0,0,1,0:] = exprzeros(5)
Edge_Net[6,28,0,0,1,0:] = exprzeros(5)
Edge_Net[6,29,0,0,1,0:] = exprzeros(5)
Edge_Net[6,30,0,0,1,0:] = exprzeros(5)
Edge_Net[6,31,0,0,1,0:] = exprzeros(5)
Edge_Net[6,32,0,0,1,0:] = exprzeros(5)
Edge_Net[6,33,0,0,1,0:] = exprzeros(5)
Edge[10,22,0,0,1] = expr(1)
Edge[10,23,0,0,1] = expr(1)
Edge[10,24,0,0,1] = expr(1)
Edge[10,25,0,0,1] = expr(1)
Edge[10,26,0,0,1] = expr(1)
Edge[10,27,0,0,1] = expr(1)
Edge[10,28,0,0,1] = expr(1)
Edge[10,29,0,0,1] = expr(1)
Edge[10,30,0,0,1] = expr(1)
Edge[10,31,0,0,1] = expr(1)
Edge[10,32,0,0,1] = expr(1)
Edge[10,33,0,0,1] = expr(1)
Edge_Net[10,22,0,0,1,0:] = exprzeros(5)
Edge_Net[10,23,0,0,1,0:] = exprzeros(5)
Edge_Net[10,24,0,0,1,0:] = exprzeros(5)
Edge_Net[10,25,0,0,1,0:] = exprzeros(5)
Edge_Net[10,26,0,0,1,0:] = exprzeros(5)
Edge_Net[10,27,0,0,1,0:] = exprzeros(5)
Edge_Net[10,28,0,0,1,0:] = exprzeros(5)
Edge_Net[10,29,0,0,1,0:] = exprzeros(5)
Edge_Net[10,30,0,0,1,0:] = exprzeros(5)
Edge_Net[10,31,0,0,1,0:] = exprzeros(5)
Edge_Net[10,32,0,0,1,0:] = exprzeros(5)
Edge_Net[10,33,0,0,1,0:] = exprzeros(5)
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
Edge[10,21,1,1,1] = expr(0)
Edge[10,22,1,1,1] = expr(0)
Edge[10,23,1,1,1] = expr(0)
Edge[10,24,1,1,1] = expr(0)
Edge[10,25,1,1,1] = expr(0)
Edge[10,26,1,1,1] = expr(0)
Edge[10,27,1,1,1] = expr(0)
Edge[10,28,1,1,1] = expr(0)
Edge[10,29,1,1,1] = expr(0)
Edge[10,30,1,1,1] = expr(0)
Edge[10,31,1,1,1] = expr(0)
Edge[10,32,1,1,1] = expr(0)
Edge[10,33,1,1,1] = expr(0)
Edge[10,34,1,1,1] = expr(0)
Edge[10,35,1,1,1] = expr(0)
Edge[10,22,0,0,1] = expr(1)
Edge[10,23,0,0,1] = expr(1)
Edge[10,24,0,0,1] = expr(1)
Edge[10,25,0,0,1] = expr(1)
Edge[10,26,0,0,1] = expr(1)
Edge[10,27,0,0,1] = expr(1)
Edge[10,28,0,0,1] = expr(1)
Edge[10,29,0,0,1] = expr(1)
Edge[10,30,0,0,1] = expr(1)
Edge[10,31,0,0,1] = expr(1)
Edge[10,32,0,0,1] = expr(1)
Edge[10,33,0,0,1] = expr(1)
Edge_Net[10,22,0,0,1,0:] = exprzeros(5)
Edge_Net[10,23,0,0,1,0:] = exprzeros(5)
Edge_Net[10,24,0,0,1,0:] = exprzeros(5)
Edge_Net[10,25,0,0,1,0:] = exprzeros(5)
Edge_Net[10,26,0,0,1,0:] = exprzeros(5)
Edge_Net[10,27,0,0,1,0:] = exprzeros(5)
Edge_Net[10,28,0,0,1,0:] = exprzeros(5)
Edge_Net[10,29,0,0,1,0:] = exprzeros(5)
Edge_Net[10,30,0,0,1,0:] = exprzeros(5)
Edge_Net[10,31,0,0,1,0:] = exprzeros(5)
Edge_Net[10,32,0,0,1,0:] = exprzeros(5)
Edge_Net[10,33,0,0,1,0:] = exprzeros(5)
Edge[14,22,0,0,1] = expr(1)
Edge[14,23,0,0,1] = expr(1)
Edge[14,24,0,0,1] = expr(1)
Edge[14,25,0,0,1] = expr(1)
Edge[14,26,0,0,1] = expr(1)
Edge[14,27,0,0,1] = expr(1)
Edge[14,28,0,0,1] = expr(1)
Edge[14,29,0,0,1] = expr(1)
Edge[14,30,0,0,1] = expr(1)
Edge[14,31,0,0,1] = expr(1)
Edge[14,32,0,0,1] = expr(1)
Edge[14,33,0,0,1] = expr(1)
Edge_Net[14,22,0,0,1,0:] = exprzeros(5)
Edge_Net[14,23,0,0,1,0:] = exprzeros(5)
Edge_Net[14,24,0,0,1,0:] = exprzeros(5)
Edge_Net[14,25,0,0,1,0:] = exprzeros(5)
Edge_Net[14,26,0,0,1,0:] = exprzeros(5)
Edge_Net[14,27,0,0,1,0:] = exprzeros(5)
Edge_Net[14,28,0,0,1,0:] = exprzeros(5)
Edge_Net[14,29,0,0,1,0:] = exprzeros(5)
Edge_Net[14,30,0,0,1,0:] = exprzeros(5)
Edge_Net[14,31,0,0,1,0:] = exprzeros(5)
Edge_Net[14,32,0,0,1,0:] = exprzeros(5)
Edge_Net[14,33,0,0,1,0:] = exprzeros(5)
Edge[10,21,1,1,1] = expr(0)
Edge[10,22,1,1,1] = expr(0)
Edge[10,23,1,1,1] = expr(0)
Edge[10,24,1,1,1] = expr(0)
Edge[10,25,1,1,1] = expr(0)
Edge[10,26,1,1,1] = expr(0)
Edge[10,27,1,1,1] = expr(0)
Edge[10,28,1,1,1] = expr(0)
Edge[10,29,1,1,1] = expr(0)
Edge[10,30,1,1,1] = expr(0)
Edge[10,31,1,1,1] = expr(0)
Edge[10,32,1,1,1] = expr(0)
Edge[10,33,1,1,1] = expr(0)
Edge[10,34,1,1,1] = expr(0)
Edge[10,35,1,1,1] = expr(0)
Edge[14,21,1,1,1] = expr(0)
Edge[14,22,1,1,1] = expr(0)
Edge[14,23,1,1,1] = expr(0)
Edge[14,24,1,1,1] = expr(0)
Edge[14,25,1,1,1] = expr(0)
Edge[14,26,1,1,1] = expr(0)
Edge[14,27,1,1,1] = expr(0)
Edge[14,28,1,1,1] = expr(0)
Edge[14,29,1,1,1] = expr(0)
Edge[14,30,1,1,1] = expr(0)
Edge[14,31,1,1,1] = expr(0)
Edge[14,32,1,1,1] = expr(0)
Edge[14,33,1,1,1] = expr(0)
Edge[14,34,1,1,1] = expr(0)
Edge[14,35,1,1,1] = expr(0)

# Net-2 subNet-0 Terminal[0] to Terminal[1]
# AIL1(6,6,1,12) ==> AIL1(14,14,1,12)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[6,1:13,0,0,1,0] = exprones(12)
Edge_Net_Subnet2[6,1:13,0,0,2,0] = exprones(12)
Edge_Net[6,1:13,0,0,1,1] = exprones(12)
for x in range(6,6+1):
  for y in range(1,12+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[14,1:13,0,0,1,0] = exprones(12)
Edge_Net_Subnet2[14,1:13,0,0,2,0] = exprones(12)
Edge_Net[14,1:13,0,0,1,1] = exprones(12)
for x in range(14,14+1):
  for y in range(1,12+1) :
    outLayout[x][y][0][0] = 2
# Net-3 subNet-0 Terminal[0] to Terminal[1]
# AIL1(10,10,1,12) ==> AIL1(6,6,22,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[10,1:13,0,0,1,0] = exprones(12)
Edge_Net_Subnet3[10,1:13,0,0,2,0] = exprones(12)
Edge_Net[10,1:13,0,0,1,2] = exprones(12)
for x in range(10,10+1):
  for y in range(1,12+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[6,22:34,0,0,1,0] = exprones(12)
Edge_Net_Subnet3[6,22:34,0,0,2,0] = exprones(12)
Edge_Net[6,22:34,0,0,1,2] = exprones(12)
for x in range(6,6+1):
  for y in range(22,33+1) :
    outLayout[x][y][0][0] = 3
# Net = 2 Subnet = 0 | Left -> Right [2,18] Top -> Bottom [0,16]
# Range R1(6,6,1,12)
# Range R2(14,14,1,12)
### Disable edges outside window
Edge_Net_Subnet2[0:2,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(2592)
Edge_Net_Subnet2[2:18,16:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(11520)
Edge_Net_Subnet2[18:25+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(10368)

### Consistency Constraints
Net2_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(2,18+1)])for y in range(0,16+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(2,18+1)])for y in range(0,16+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,0],Xor(Edge_Net_Subnet2[x,y,2,trend,1,0],Edge_Net_Subnet2[x,y,2,trend,2,0])),And(~Edge_Net_Subnet2[x,y,2,trend,0,0],~Edge_Net_Subnet2[x,y,2,trend,1,0],~Edge_Net_Subnet2[x,y,2,trend,2,0]))for x in range(2,18+1)])for y in range(0,16+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,0],Xor(Edge_Net_Subnet2[x,y,3,1,1,0],Edge_Net_Subnet2[x,y,3,1,2,0])),And(~Edge_Net_Subnet2[x,y,3,1,0,0],~Edge_Net_Subnet2[x,y,3,1,1,0],~Edge_Net_Subnet2[x,y,3,1,2,0]))for x in range(2,18+1)])for y in range(0,16+1)]).to_cnf()
Net2_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,0],Xor(Edge_Net_Subnet2[x,y,1,trend,0,0],Edge_Net_Subnet2[x,y,1,trend,1,0])),And(~Edge_Net_Subnet2[x,y,1,trend,2,0],~Edge_Net_Subnet2[x,y,1,trend,0,0],~Edge_Net_Subnet2[x,y,1,trend,1,0]))for x in range(2,18+1)])for y in range(0,16+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet0_C6 = And(
1,1
).to_cnf()
Net2_Subnet0_C = And(Net2_Subnet0_C1, Net2_Subnet0_C2,Net2_Subnet0_C3_ME1_Mask,Net2_Subnet0_C4_MINT1_Mask,Net2_Subnet0_C5_AIL2GIL_Mask,Net2_Subnet0_C6,)
### Design Rules
Net2_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(2,18+1)])for y in range(0,16+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge_Net_Subnet2[x-1,y,1,1,1,0]), And(Edge_Net_Subnet2[x+1,y,1,1,1,0], Edge_Net_Subnet2[x+2,y,1,1,1,0], Edge_Net_Subnet2[x+3,y,1,1,1,0], ))for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge_Net_Subnet2[x+1,y,1,1,1,0]), And(Edge_Net_Subnet2[x-1,y,1,1,1,0], Edge_Net_Subnet2[x-2,y,1,1,1,0], Edge_Net_Subnet2[x-3,y,1,1,1,0], ))for x in range(3,18+1)])for y in range(0,16+1)])
	).to_cnf()
Net2_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,18+1)])for y in range(0,16+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(2,18+1)])for y in range(0,16+1)])
	).to_cnf()
Net2_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(2,18+1)])for y in range(3,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0]), And(Edge_Net_Subnet2[x,y+1,1,0,0,0], Edge_Net_Subnet2[x,y+2,1,0,0,0], Edge_Net_Subnet2[x,y+3,1,0,0,0], ))for x in range(2,18+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge_Net_Subnet2[x,y-1,1,0,0,0]), And(Edge_Net_Subnet2[x,y+1,1,0,0,0], Edge_Net_Subnet2[x,y+2,1,0,0,0], Edge_Net_Subnet2[x,y+3,1,0,0,0], ))for x in range(2,18+1)])for y in range(0+1,16+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge_Net_Subnet2[x,y+1,1,0,0,0]), And(Edge_Net_Subnet2[x,y-1,1,0,0,0], Edge_Net_Subnet2[x,y-2,1,0,0,0], Edge_Net_Subnet2[x,y-3,1,0,0,0], ))for x in range(2,18+1)])for y in range(0+3,16+1)])
	).to_cnf()
Net2_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(2,18+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(2,18+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(2,18+1)])for y in range(0+3,16+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(2,18+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,18+1)])for y in range(0,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge_Net_Subnet2[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,0], Edge_Net_Subnet2[x+2,y,3,1,mask,0], Edge_Net_Subnet2[x+3,y,3,1,mask,0], Edge_Net_Subnet2[x+4,y,3,1,mask,0], Edge_Net_Subnet2[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge_Net_Subnet2[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,0], Edge_Net_Subnet2[x-2,y,3,1,mask,0], Edge_Net_Subnet2[x-3,y,3,1,mask,0], Edge_Net_Subnet2[x-4,y,3,1,mask,0], Edge_Net_Subnet2[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,18+1)])for y in range(0,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(3,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(0,16+1)])
	).to_cnf()
Net2_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(2,18+1)])for y in range(2,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,18+1)])for y in range(0,16+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(2,18+1)])for y in range(0,16+1)])
	).to_cnf()
Net2_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge_Net_Subnet2[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,0], Edge_Net_Subnet2[x+2,y,2,1,mask,0], Edge_Net_Subnet2[x+3,y,2,1,mask,0], Edge_Net_Subnet2[x+4,y,2,1,mask,0], Edge_Net_Subnet2[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge_Net_Subnet2[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,0], Edge_Net_Subnet2[x-2,y,2,1,mask,0], Edge_Net_Subnet2[x-3,y,2,1,mask,0], Edge_Net_Subnet2[x-4,y,2,1,mask,0], Edge_Net_Subnet2[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(Edge_Net_Subnet2[x-1,y,2,1,mask,0], Edge_Net_Subnet2[x-2,y,2,1,mask,0], Edge_Net_Subnet2[x-3,y,2,1,mask,0], Edge_Net_Subnet2[x-4,y,2,1,mask,0], Edge_Net_Subnet2[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(2,2+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(Edge_Net_Subnet2[x+1,y,2,1,mask,0], Edge_Net_Subnet2[x+2,y,2,1,mask,0], Edge_Net_Subnet2[x+3,y,2,1,mask,0], Edge_Net_Subnet2[x+4,y,2,1,mask,0], Edge_Net_Subnet2[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(18-1,2)])for y in range(0,16+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge_Net_Subnet2[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,0], Edge_Net_Subnet2[x,y+2,2,0,mask,0], Edge_Net_Subnet2[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(0+1,16+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge_Net_Subnet2[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,0], Edge_Net_Subnet2[x,y-2,2,0,mask,0], Edge_Net_Subnet2[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(0+3,16+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,0], And(Edge_Net_Subnet2[x,y+1,2,0,mask,0], Edge_Net_Subnet2[x,y+2,2,0,mask,0], Edge_Net_Subnet2[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,0], And(Edge_Net_Subnet2[x,y-1,2,0,mask,0], Edge_Net_Subnet2[x,y-2,2,0,mask,0], Edge_Net_Subnet2[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(16,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,18+1)])for y in range(0,16+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(2,18+1)])for y in range(0,16+1)])
	).to_cnf()
Net2_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(0,16+1)])
	).to_cnf()
Net2_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(2,18+1)])for y in range(2,16+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(2,18+1)])for y in range(0,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(4,16+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(0,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(2,18+1)])for y in range(3,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(4,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,18+1)])for y in range(0,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,18+1)])for y in range(0,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(2,18+1)])for y in range(0,16+1)])
	).to_cnf()
Net2_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(2,18+1)])for y in range(0,16+1)])
	).to_cnf()
Net2_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(2,18+1)])for y in range(2,16+1)]),
	).to_cnf()
Net2_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(2,18+1)])for y in range(0,16+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(2,18+1)])for y in range(2,16+1)]),
	).to_cnf()
Net2_Subnet0_DR = And(Net2_Subnet0_DR_Trend, Net2_Subnet0_DR_GIL_HorMinWidth,Net2_Subnet0_DR_GIL_HorMinSpacing,Net2_Subnet0_DR_GIL_VerMinSpacing,Net2_Subnet0_DR_AIL2_VerMinWidth,Net2_Subnet0_DR_AIL2_VerMinSpacing,Net2_Subnet0_DR_VerAIL2_HorMinSpacing,Net2_Subnet0_DR_MINT1AB_HorMinWidth,Net2_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet0_DR_M1AB_MinWidth,Net2_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet0_DR_V0_HorMinSpacing,Net2_Subnet0_DR_V1_HorMinSpacing,Net2_Subnet0_DR_V0_VerMinSpacing,Net2_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[6,1,0,0, 6,2,0,0, 6,3,0,0, 6,4,0,0, 6,5,0,0, 6,6,0,0, 6,7,0,0, 6,8,0,0, 6,9,0,0, 6,10,0,0, 6,11,0,0, 6,12,0,0, ],12,2,0,1,18,16,3,0),
	RConstraints.R1(Edge_Net_Subnet2,[14,1,0,0, 14,2,0,0, 14,3,0,0, 14,4,0,0, 14,5,0,0, 14,6,0,0, 14,7,0,0, 14,8,0,0, 14,9,0,0, 14,10,0,0, 14,11,0,0, 14,12,0,0, ],12,2,0,1,18,16,3,0),
	).to_cnf()
Net2_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[6,1,0, 6,2,0, 6,3,0, 6,4,0, 6,5,0, 6,6,0, 6,7,0, 6,8,0, 6,9,0, 6,10,0, 6,11,0, 6,12,0, 6,13,0, 14,1,0, 14,2,0, 14,3,0, 14,4,0, 14,5,0, 14,6,0, 14,7,0, 14,8,0, 14,9,0, 14,10,0, 14,11,0, 14,12,0, 14,13,0, ],26,2,0,0,18,16,3,0,1),
	)
Net2_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(2,18+1)])for y in range(0,16+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,4+1)])for x in range(2,18+1)])for y in range(0,16+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet0_R = And(Net2_Subnet0_R1,Net2_Subnet0_R2,Net2_Subnet0_R3,)
Net2_Subnet0_Formula = And(Net2_Subnet0_C,Net2_Subnet0_DR,Net2_Subnet0_R)
# Net = 3 Subnet = 0 | Left -> Right [2,14] Top -> Bottom [0,35]
# Range R1(10,10,1,12)
# Range R2(6,6,22,33)
### Disable edges outside window
Edge_Net_Subnet3[0:2,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(2592)
Edge_Net_Subnet3[14:25+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(15552)

### Consistency Constraints
Net3_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(2,14+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(2,14+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,0],Xor(Edge_Net_Subnet3[x,y,2,trend,1,0],Edge_Net_Subnet3[x,y,2,trend,2,0])),And(~Edge_Net_Subnet3[x,y,2,trend,0,0],~Edge_Net_Subnet3[x,y,2,trend,1,0],~Edge_Net_Subnet3[x,y,2,trend,2,0]))for x in range(2,14+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,0],Xor(Edge_Net_Subnet3[x,y,3,1,1,0],Edge_Net_Subnet3[x,y,3,1,2,0])),And(~Edge_Net_Subnet3[x,y,3,1,0,0],~Edge_Net_Subnet3[x,y,3,1,1,0],~Edge_Net_Subnet3[x,y,3,1,2,0]))for x in range(2,14+1)])for y in range(0,35+1)]).to_cnf()
Net3_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,0],Xor(Edge_Net_Subnet3[x,y,1,trend,0,0],Edge_Net_Subnet3[x,y,1,trend,1,0])),And(~Edge_Net_Subnet3[x,y,1,trend,2,0],~Edge_Net_Subnet3[x,y,1,trend,0,0],~Edge_Net_Subnet3[x,y,1,trend,1,0]))for x in range(2,14+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet0_C6 = And(
1,1
).to_cnf()
Net3_Subnet0_C = And(Net3_Subnet0_C1, Net3_Subnet0_C2,Net3_Subnet0_C3_ME1_Mask,Net3_Subnet0_C4_MINT1_Mask,Net3_Subnet0_C5_AIL2GIL_Mask,Net3_Subnet0_C6,)
### Design Rules
Net3_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(2,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(2,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(2,14+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge_Net_Subnet3[x-1,y,1,1,1,0]), And(Edge_Net_Subnet3[x+1,y,1,1,1,0], Edge_Net_Subnet3[x+2,y,1,1,1,0], Edge_Net_Subnet3[x+3,y,1,1,1,0], ))for x in range(2,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge_Net_Subnet3[x+1,y,1,1,1,0]), And(Edge_Net_Subnet3[x-1,y,1,1,1,0], Edge_Net_Subnet3[x-2,y,1,1,1,0], Edge_Net_Subnet3[x-3,y,1,1,1,0], ))for x in range(3,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,14+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(2,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(2,14+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(2,14+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0]), And(Edge_Net_Subnet3[x,y+1,1,0,0,0], Edge_Net_Subnet3[x,y+2,1,0,0,0], Edge_Net_Subnet3[x,y+3,1,0,0,0], ))for x in range(2,14+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0]), And(Edge_Net_Subnet3[x,y-1,1,0,0,0], Edge_Net_Subnet3[x,y-2,1,0,0,0], Edge_Net_Subnet3[x,y-3,1,0,0,0], ))for x in range(2,14+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge_Net_Subnet3[x,y-1,1,0,0,0]), And(Edge_Net_Subnet3[x,y+1,1,0,0,0], Edge_Net_Subnet3[x,y+2,1,0,0,0], Edge_Net_Subnet3[x,y+3,1,0,0,0], ))for x in range(2,14+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge_Net_Subnet3[x,y+1,1,0,0,0]), And(Edge_Net_Subnet3[x,y-1,1,0,0,0], Edge_Net_Subnet3[x,y-2,1,0,0,0], Edge_Net_Subnet3[x,y-3,1,0,0,0], ))for x in range(2,14+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net3_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(2,14+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(2,14+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(2,14+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(2,14+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(2,14+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(2,14+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net3_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(2,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge_Net_Subnet3[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,0], Edge_Net_Subnet3[x+2,y,3,1,mask,0], Edge_Net_Subnet3[x+3,y,3,1,mask,0], Edge_Net_Subnet3[x+4,y,3,1,mask,0], Edge_Net_Subnet3[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge_Net_Subnet3[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,0], Edge_Net_Subnet3[x-2,y,3,1,mask,0], Edge_Net_Subnet3[x-3,y,3,1,mask,0], Edge_Net_Subnet3[x-4,y,3,1,mask,0], Edge_Net_Subnet3[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(2,14+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(2,14+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,14+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(2,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge_Net_Subnet3[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,0], Edge_Net_Subnet3[x+2,y,2,1,mask,0], Edge_Net_Subnet3[x+3,y,2,1,mask,0], Edge_Net_Subnet3[x+4,y,2,1,mask,0], Edge_Net_Subnet3[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge_Net_Subnet3[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,0], Edge_Net_Subnet3[x-2,y,2,1,mask,0], Edge_Net_Subnet3[x-3,y,2,1,mask,0], Edge_Net_Subnet3[x-4,y,2,1,mask,0], Edge_Net_Subnet3[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(Edge_Net_Subnet3[x-1,y,2,1,mask,0], Edge_Net_Subnet3[x-2,y,2,1,mask,0], Edge_Net_Subnet3[x-3,y,2,1,mask,0], Edge_Net_Subnet3[x-4,y,2,1,mask,0], Edge_Net_Subnet3[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(2,2+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(Edge_Net_Subnet3[x+1,y,2,1,mask,0], Edge_Net_Subnet3[x+2,y,2,1,mask,0], Edge_Net_Subnet3[x+3,y,2,1,mask,0], Edge_Net_Subnet3[x+4,y,2,1,mask,0], Edge_Net_Subnet3[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(14-1,2)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge_Net_Subnet3[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,0], Edge_Net_Subnet3[x,y+2,2,0,mask,0], Edge_Net_Subnet3[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge_Net_Subnet3[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,0], Edge_Net_Subnet3[x,y-2,2,0,mask,0], Edge_Net_Subnet3[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,0], And(Edge_Net_Subnet3[x,y+1,2,0,mask,0], Edge_Net_Subnet3[x,y+2,2,0,mask,0], Edge_Net_Subnet3[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,0], And(Edge_Net_Subnet3[x,y-1,2,0,mask,0], Edge_Net_Subnet3[x,y-2,2,0,mask,0], Edge_Net_Subnet3[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,14+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(2,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(2,14+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(2,14+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net3_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net3_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(2,14+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(2,14+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(4,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(2,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(2,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(2,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(2,14+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(2,14+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(2,14+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(2,14+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet0_DR = And(Net3_Subnet0_DR_Trend, Net3_Subnet0_DR_GIL_HorMinWidth,Net3_Subnet0_DR_GIL_HorMinSpacing,Net3_Subnet0_DR_GIL_VerMinSpacing,Net3_Subnet0_DR_AIL2_VerMinWidth,Net3_Subnet0_DR_AIL2_VerMinSpacing,Net3_Subnet0_DR_VerAIL2_HorMinSpacing,Net3_Subnet0_DR_MINT1AB_HorMinWidth,Net3_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet0_DR_M1AB_MinWidth,Net3_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet0_DR_V0_HorMinSpacing,Net3_Subnet0_DR_V1_HorMinSpacing,Net3_Subnet0_DR_V0_VerMinSpacing,Net3_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[10,1,0,0, 10,2,0,0, 10,3,0,0, 10,4,0,0, 10,5,0,0, 10,6,0,0, 10,7,0,0, 10,8,0,0, 10,9,0,0, 10,10,0,0, 10,11,0,0, 10,12,0,0, ],12,2,0,1,14,35,3,0),
	RConstraints.R1(Edge_Net_Subnet3,[6,22,0,0, 6,23,0,0, 6,24,0,0, 6,25,0,0, 6,26,0,0, 6,27,0,0, 6,28,0,0, 6,29,0,0, 6,30,0,0, 6,31,0,0, 6,32,0,0, 6,33,0,0, ],12,2,0,1,14,35,3,0),
	).to_cnf()
Net3_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[10,1,0, 10,2,0, 10,3,0, 10,4,0, 10,5,0, 10,6,0, 10,7,0, 10,8,0, 10,9,0, 10,10,0, 10,11,0, 10,12,0, 10,13,0, 6,22,0, 6,23,0, 6,24,0, 6,25,0, 6,26,0, 6,27,0, 6,28,0, 6,29,0, 6,30,0, 6,31,0, 6,32,0, 6,33,0, 6,34,0, ],26,2,0,0,14,35,3,0,2),
	)
Net3_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(2,14+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,4+1)])for x in range(2,14+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet0_R = And(Net3_Subnet0_R1,Net3_Subnet0_R2,Net3_Subnet0_R3,)
Net3_Subnet0_Formula = And(Net3_Subnet0_C,Net3_Subnet0_DR,Net3_Subnet0_R)
FORMULA = And(Net2_Subnet0_Formula, Net3_Subnet0_Formula, )
endTime = time.time()
print('Total Time = ', endTime-startTime)
setOut.clauseDistribution(FORMULA)
setOut.setUpLayoutViaFromResult(FORMULA.satisfy_one(),outLayout,subnetRec,5)
print('#edge = 9625')