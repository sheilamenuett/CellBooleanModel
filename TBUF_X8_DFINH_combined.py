from pyeda.inter import *
import RConstraints
import time
import setOut
startTime = time.time()
# ===> Instruction(Create)  2D Routing Style p(e) <===
# ===> Edges[X, Y, Z, Trends, Masks]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge = exprvars('edge', 86, 36, 4, 3, 3)

# ===> Instruction(Create)  2D Routing Style p(e,n) <===
# ===> Edge_Net[X, Y, Z, Trends, Masks, Nets]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge_Net = exprvars('edge_net', 86, 36, 4, 3, 3, 6)

# ===> Instruction(Create)  2D Routing Style p(e,n,s) <===
# ===> Edge_Net_Subnet_NetID[X, Y, Z, Trends, Masks, Subnets]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge_Net_Subnet1 = exprvars('edge_net_subnet1', 86, 36, 4, 3, 3, 7)
Edge_Net_Subnet2 = exprvars('edge_net_subnet2', 86, 36, 4, 3, 3, 10)
Edge_Net_Subnet4 = exprvars('edge_net_subnet4', 86, 36, 4, 3, 3, 3)
Edge_Net_Subnet5 = exprvars('edge_net_subnet5', 86, 36, 4, 3, 3, 3)
Edge_Net_Subnet3 = exprvars('edge_net_subnet3', 86, 36, 4, 3, 3, 10)
Edge_Net_Subnet8 = exprvars('edge_net_subnet8', 86, 36, 4, 3, 3, 5)

outLayout=[[[[0 for trend in range(3)] for z in range(4)] for y in range(36)] for x in range(86)]

subnetRec=[[[[0 for trend in range(3)] for z in range(4)] for y in range(36)] for x in range(86)]

MaxX = 85
MaxY = 35
MaxZ = 3
#Net = 6
#cellName = TBUF_X8_DFINH_combined
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
Edge_Net[0,0,0,0,0,0:] = exprzeros(6)
Edge_Net[0,1,0,0,0,0:] = exprzeros(6)
Edge_Net[0,2,0,0,0,0:] = exprzeros(6)
Edge_Net[0,3,0,0,0,0:] = exprzeros(6)
Edge_Net[0,4,0,0,0,0:] = exprzeros(6)
Edge_Net[0,5,0,0,0,0:] = exprzeros(6)
Edge_Net[0,6,0,0,0,0:] = exprzeros(6)
Edge_Net[0,7,0,0,0,0:] = exprzeros(6)
Edge_Net[0,8,0,0,0,0:] = exprzeros(6)
Edge_Net[0,9,0,0,0,0:] = exprzeros(6)
Edge_Net[0,10,0,0,0,0:] = exprzeros(6)
Edge_Net[0,11,0,0,0,0:] = exprzeros(6)
Edge_Net[0,12,0,0,0,0:] = exprzeros(6)
Edge_Net[0,13,0,0,0,0:] = exprzeros(6)
Edge_Net[0,14,0,0,0,0:] = exprzeros(6)
Edge_Net[0,15,0,0,0,0:] = exprzeros(6)
Edge_Net[0,16,0,0,0,0:] = exprzeros(6)
Edge_Net[0,17,0,0,0,0:] = exprzeros(6)
Edge_Net[0,18,0,0,0,0:] = exprzeros(6)
Edge_Net[0,19,0,0,0,0:] = exprzeros(6)
Edge_Net[0,20,0,0,0,0:] = exprzeros(6)
Edge_Net[0,21,0,0,0,0:] = exprzeros(6)
Edge_Net[0,22,0,0,0,0:] = exprzeros(6)
Edge_Net[0,23,0,0,0,0:] = exprzeros(6)
Edge_Net[0,24,0,0,0,0:] = exprzeros(6)
Edge_Net[0,25,0,0,0,0:] = exprzeros(6)
Edge_Net[0,26,0,0,0,0:] = exprzeros(6)
Edge_Net[0,27,0,0,0,0:] = exprzeros(6)
Edge_Net[0,28,0,0,0,0:] = exprzeros(6)
Edge_Net[0,29,0,0,0,0:] = exprzeros(6)
Edge_Net[0,30,0,0,0,0:] = exprzeros(6)
Edge_Net[0,31,0,0,0,0:] = exprzeros(6)
Edge_Net[0,32,0,0,0,0:] = exprzeros(6)
Edge_Net[0,33,0,0,0,0:] = exprzeros(6)
Edge_Net[0,34,0,0,0,0:] = exprzeros(6)
Edge_Net[0,35,0,0,0,0:] = exprzeros(6)
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
Edge_Net[4,0,0,0,0,0:] = exprzeros(6)
Edge_Net[4,1,0,0,0,0:] = exprzeros(6)
Edge_Net[4,2,0,0,0,0:] = exprzeros(6)
Edge_Net[4,3,0,0,0,0:] = exprzeros(6)
Edge_Net[4,4,0,0,0,0:] = exprzeros(6)
Edge_Net[4,5,0,0,0,0:] = exprzeros(6)
Edge_Net[4,6,0,0,0,0:] = exprzeros(6)
Edge_Net[4,7,0,0,0,0:] = exprzeros(6)
Edge_Net[4,8,0,0,0,0:] = exprzeros(6)
Edge_Net[4,9,0,0,0,0:] = exprzeros(6)
Edge_Net[4,10,0,0,0,0:] = exprzeros(6)
Edge_Net[4,11,0,0,0,0:] = exprzeros(6)
Edge_Net[4,12,0,0,0,0:] = exprzeros(6)
Edge_Net[4,13,0,0,0,0:] = exprzeros(6)
Edge_Net[4,14,0,0,0,0:] = exprzeros(6)
Edge_Net[4,15,0,0,0,0:] = exprzeros(6)
Edge_Net[4,16,0,0,0,0:] = exprzeros(6)
Edge_Net[4,17,0,0,0,0:] = exprzeros(6)
Edge_Net[4,18,0,0,0,0:] = exprzeros(6)
Edge_Net[4,19,0,0,0,0:] = exprzeros(6)
Edge_Net[4,20,0,0,0,0:] = exprzeros(6)
Edge_Net[4,21,0,0,0,0:] = exprzeros(6)
Edge_Net[4,22,0,0,0,0:] = exprzeros(6)
Edge_Net[4,23,0,0,0,0:] = exprzeros(6)
Edge_Net[4,24,0,0,0,0:] = exprzeros(6)
Edge_Net[4,25,0,0,0,0:] = exprzeros(6)
Edge_Net[4,26,0,0,0,0:] = exprzeros(6)
Edge_Net[4,27,0,0,0,0:] = exprzeros(6)
Edge_Net[4,28,0,0,0,0:] = exprzeros(6)
Edge_Net[4,29,0,0,0,0:] = exprzeros(6)
Edge_Net[4,30,0,0,0,0:] = exprzeros(6)
Edge_Net[4,31,0,0,0,0:] = exprzeros(6)
Edge_Net[4,32,0,0,0,0:] = exprzeros(6)
Edge_Net[4,33,0,0,0,0:] = exprzeros(6)
Edge_Net[4,34,0,0,0,0:] = exprzeros(6)
Edge_Net[4,35,0,0,0,0:] = exprzeros(6)
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
Edge_Net[8,0,0,0,0,0:] = exprzeros(6)
Edge_Net[8,1,0,0,0,0:] = exprzeros(6)
Edge_Net[8,2,0,0,0,0:] = exprzeros(6)
Edge_Net[8,3,0,0,0,0:] = exprzeros(6)
Edge_Net[8,4,0,0,0,0:] = exprzeros(6)
Edge_Net[8,5,0,0,0,0:] = exprzeros(6)
Edge_Net[8,6,0,0,0,0:] = exprzeros(6)
Edge_Net[8,7,0,0,0,0:] = exprzeros(6)
Edge_Net[8,8,0,0,0,0:] = exprzeros(6)
Edge_Net[8,9,0,0,0,0:] = exprzeros(6)
Edge_Net[8,10,0,0,0,0:] = exprzeros(6)
Edge_Net[8,11,0,0,0,0:] = exprzeros(6)
Edge_Net[8,12,0,0,0,0:] = exprzeros(6)
Edge_Net[8,13,0,0,0,0:] = exprzeros(6)
Edge_Net[8,14,0,0,0,0:] = exprzeros(6)
Edge_Net[8,15,0,0,0,0:] = exprzeros(6)
Edge_Net[8,16,0,0,0,0:] = exprzeros(6)
Edge_Net[8,17,0,0,0,0:] = exprzeros(6)
Edge_Net[8,18,0,0,0,0:] = exprzeros(6)
Edge_Net[8,19,0,0,0,0:] = exprzeros(6)
Edge_Net[8,20,0,0,0,0:] = exprzeros(6)
Edge_Net[8,21,0,0,0,0:] = exprzeros(6)
Edge_Net[8,22,0,0,0,0:] = exprzeros(6)
Edge_Net[8,23,0,0,0,0:] = exprzeros(6)
Edge_Net[8,24,0,0,0,0:] = exprzeros(6)
Edge_Net[8,25,0,0,0,0:] = exprzeros(6)
Edge_Net[8,26,0,0,0,0:] = exprzeros(6)
Edge_Net[8,27,0,0,0,0:] = exprzeros(6)
Edge_Net[8,28,0,0,0,0:] = exprzeros(6)
Edge_Net[8,29,0,0,0,0:] = exprzeros(6)
Edge_Net[8,30,0,0,0,0:] = exprzeros(6)
Edge_Net[8,31,0,0,0,0:] = exprzeros(6)
Edge_Net[8,32,0,0,0,0:] = exprzeros(6)
Edge_Net[8,33,0,0,0,0:] = exprzeros(6)
Edge_Net[8,34,0,0,0,0:] = exprzeros(6)
Edge_Net[8,35,0,0,0,0:] = exprzeros(6)
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
Edge_Net[12,0,0,0,0,0:] = exprzeros(6)
Edge_Net[12,1,0,0,0,0:] = exprzeros(6)
Edge_Net[12,2,0,0,0,0:] = exprzeros(6)
Edge_Net[12,3,0,0,0,0:] = exprzeros(6)
Edge_Net[12,4,0,0,0,0:] = exprzeros(6)
Edge_Net[12,5,0,0,0,0:] = exprzeros(6)
Edge_Net[12,6,0,0,0,0:] = exprzeros(6)
Edge_Net[12,7,0,0,0,0:] = exprzeros(6)
Edge_Net[12,8,0,0,0,0:] = exprzeros(6)
Edge_Net[12,9,0,0,0,0:] = exprzeros(6)
Edge_Net[12,10,0,0,0,0:] = exprzeros(6)
Edge_Net[12,11,0,0,0,0:] = exprzeros(6)
Edge_Net[12,12,0,0,0,0:] = exprzeros(6)
Edge_Net[12,13,0,0,0,0:] = exprzeros(6)
Edge_Net[12,14,0,0,0,0:] = exprzeros(6)
Edge_Net[12,15,0,0,0,0:] = exprzeros(6)
Edge_Net[12,16,0,0,0,0:] = exprzeros(6)
Edge_Net[12,17,0,0,0,0:] = exprzeros(6)
Edge_Net[12,18,0,0,0,0:] = exprzeros(6)
Edge_Net[12,19,0,0,0,0:] = exprzeros(6)
Edge_Net[12,20,0,0,0,0:] = exprzeros(6)
Edge_Net[12,21,0,0,0,0:] = exprzeros(6)
Edge_Net[12,22,0,0,0,0:] = exprzeros(6)
Edge_Net[12,23,0,0,0,0:] = exprzeros(6)
Edge_Net[12,24,0,0,0,0:] = exprzeros(6)
Edge_Net[12,25,0,0,0,0:] = exprzeros(6)
Edge_Net[12,26,0,0,0,0:] = exprzeros(6)
Edge_Net[12,27,0,0,0,0:] = exprzeros(6)
Edge_Net[12,28,0,0,0,0:] = exprzeros(6)
Edge_Net[12,29,0,0,0,0:] = exprzeros(6)
Edge_Net[12,30,0,0,0,0:] = exprzeros(6)
Edge_Net[12,31,0,0,0,0:] = exprzeros(6)
Edge_Net[12,32,0,0,0,0:] = exprzeros(6)
Edge_Net[12,33,0,0,0,0:] = exprzeros(6)
Edge_Net[12,34,0,0,0,0:] = exprzeros(6)
Edge_Net[12,35,0,0,0,0:] = exprzeros(6)
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
Edge_Net[16,0,0,0,0,0:] = exprzeros(6)
Edge_Net[16,1,0,0,0,0:] = exprzeros(6)
Edge_Net[16,2,0,0,0,0:] = exprzeros(6)
Edge_Net[16,3,0,0,0,0:] = exprzeros(6)
Edge_Net[16,4,0,0,0,0:] = exprzeros(6)
Edge_Net[16,5,0,0,0,0:] = exprzeros(6)
Edge_Net[16,6,0,0,0,0:] = exprzeros(6)
Edge_Net[16,7,0,0,0,0:] = exprzeros(6)
Edge_Net[16,8,0,0,0,0:] = exprzeros(6)
Edge_Net[16,9,0,0,0,0:] = exprzeros(6)
Edge_Net[16,10,0,0,0,0:] = exprzeros(6)
Edge_Net[16,11,0,0,0,0:] = exprzeros(6)
Edge_Net[16,12,0,0,0,0:] = exprzeros(6)
Edge_Net[16,13,0,0,0,0:] = exprzeros(6)
Edge_Net[16,14,0,0,0,0:] = exprzeros(6)
Edge_Net[16,15,0,0,0,0:] = exprzeros(6)
Edge_Net[16,16,0,0,0,0:] = exprzeros(6)
Edge_Net[16,17,0,0,0,0:] = exprzeros(6)
Edge_Net[16,18,0,0,0,0:] = exprzeros(6)
Edge_Net[16,19,0,0,0,0:] = exprzeros(6)
Edge_Net[16,20,0,0,0,0:] = exprzeros(6)
Edge_Net[16,21,0,0,0,0:] = exprzeros(6)
Edge_Net[16,22,0,0,0,0:] = exprzeros(6)
Edge_Net[16,23,0,0,0,0:] = exprzeros(6)
Edge_Net[16,24,0,0,0,0:] = exprzeros(6)
Edge_Net[16,25,0,0,0,0:] = exprzeros(6)
Edge_Net[16,26,0,0,0,0:] = exprzeros(6)
Edge_Net[16,27,0,0,0,0:] = exprzeros(6)
Edge_Net[16,28,0,0,0,0:] = exprzeros(6)
Edge_Net[16,29,0,0,0,0:] = exprzeros(6)
Edge_Net[16,30,0,0,0,0:] = exprzeros(6)
Edge_Net[16,31,0,0,0,0:] = exprzeros(6)
Edge_Net[16,32,0,0,0,0:] = exprzeros(6)
Edge_Net[16,33,0,0,0,0:] = exprzeros(6)
Edge_Net[16,34,0,0,0,0:] = exprzeros(6)
Edge_Net[16,35,0,0,0,0:] = exprzeros(6)
Edge[20,0,0,0,0] = expr(1)
Edge[20,1,0,0,0] = expr(1)
Edge[20,2,0,0,0] = expr(1)
Edge[20,3,0,0,0] = expr(1)
Edge[20,4,0,0,0] = expr(1)
Edge[20,5,0,0,0] = expr(1)
Edge[20,6,0,0,0] = expr(1)
Edge[20,7,0,0,0] = expr(1)
Edge[20,8,0,0,0] = expr(1)
Edge[20,9,0,0,0] = expr(1)
Edge[20,10,0,0,0] = expr(1)
Edge[20,11,0,0,0] = expr(1)
Edge[20,12,0,0,0] = expr(1)
Edge[20,13,0,0,0] = expr(1)
Edge[20,14,0,0,0] = expr(1)
Edge[20,15,0,0,0] = expr(1)
Edge[20,16,0,0,0] = expr(1)
Edge[20,17,0,0,0] = expr(1)
Edge[20,18,0,0,0] = expr(1)
Edge[20,19,0,0,0] = expr(1)
Edge[20,20,0,0,0] = expr(1)
Edge[20,21,0,0,0] = expr(1)
Edge[20,22,0,0,0] = expr(1)
Edge[20,23,0,0,0] = expr(1)
Edge[20,24,0,0,0] = expr(1)
Edge[20,25,0,0,0] = expr(1)
Edge[20,26,0,0,0] = expr(1)
Edge[20,27,0,0,0] = expr(1)
Edge[20,28,0,0,0] = expr(1)
Edge[20,29,0,0,0] = expr(1)
Edge[20,30,0,0,0] = expr(1)
Edge[20,31,0,0,0] = expr(1)
Edge[20,32,0,0,0] = expr(1)
Edge[20,33,0,0,0] = expr(1)
Edge[20,34,0,0,0] = expr(1)
Edge[20,35,0,0,0] = expr(1)
Edge_Net[20,0,0,0,0,0:] = exprzeros(6)
Edge_Net[20,1,0,0,0,0:] = exprzeros(6)
Edge_Net[20,2,0,0,0,0:] = exprzeros(6)
Edge_Net[20,3,0,0,0,0:] = exprzeros(6)
Edge_Net[20,4,0,0,0,0:] = exprzeros(6)
Edge_Net[20,5,0,0,0,0:] = exprzeros(6)
Edge_Net[20,6,0,0,0,0:] = exprzeros(6)
Edge_Net[20,7,0,0,0,0:] = exprzeros(6)
Edge_Net[20,8,0,0,0,0:] = exprzeros(6)
Edge_Net[20,9,0,0,0,0:] = exprzeros(6)
Edge_Net[20,10,0,0,0,0:] = exprzeros(6)
Edge_Net[20,11,0,0,0,0:] = exprzeros(6)
Edge_Net[20,12,0,0,0,0:] = exprzeros(6)
Edge_Net[20,13,0,0,0,0:] = exprzeros(6)
Edge_Net[20,14,0,0,0,0:] = exprzeros(6)
Edge_Net[20,15,0,0,0,0:] = exprzeros(6)
Edge_Net[20,16,0,0,0,0:] = exprzeros(6)
Edge_Net[20,17,0,0,0,0:] = exprzeros(6)
Edge_Net[20,18,0,0,0,0:] = exprzeros(6)
Edge_Net[20,19,0,0,0,0:] = exprzeros(6)
Edge_Net[20,20,0,0,0,0:] = exprzeros(6)
Edge_Net[20,21,0,0,0,0:] = exprzeros(6)
Edge_Net[20,22,0,0,0,0:] = exprzeros(6)
Edge_Net[20,23,0,0,0,0:] = exprzeros(6)
Edge_Net[20,24,0,0,0,0:] = exprzeros(6)
Edge_Net[20,25,0,0,0,0:] = exprzeros(6)
Edge_Net[20,26,0,0,0,0:] = exprzeros(6)
Edge_Net[20,27,0,0,0,0:] = exprzeros(6)
Edge_Net[20,28,0,0,0,0:] = exprzeros(6)
Edge_Net[20,29,0,0,0,0:] = exprzeros(6)
Edge_Net[20,30,0,0,0,0:] = exprzeros(6)
Edge_Net[20,31,0,0,0,0:] = exprzeros(6)
Edge_Net[20,32,0,0,0,0:] = exprzeros(6)
Edge_Net[20,33,0,0,0,0:] = exprzeros(6)
Edge_Net[20,34,0,0,0,0:] = exprzeros(6)
Edge_Net[20,35,0,0,0,0:] = exprzeros(6)
Edge[24,0,0,0,0] = expr(1)
Edge[24,1,0,0,0] = expr(1)
Edge[24,2,0,0,0] = expr(1)
Edge[24,3,0,0,0] = expr(1)
Edge[24,4,0,0,0] = expr(1)
Edge[24,5,0,0,0] = expr(1)
Edge[24,6,0,0,0] = expr(1)
Edge[24,7,0,0,0] = expr(1)
Edge[24,8,0,0,0] = expr(1)
Edge[24,9,0,0,0] = expr(1)
Edge[24,10,0,0,0] = expr(1)
Edge[24,11,0,0,0] = expr(1)
Edge[24,12,0,0,0] = expr(1)
Edge[24,13,0,0,0] = expr(1)
Edge[24,14,0,0,0] = expr(1)
Edge[24,15,0,0,0] = expr(1)
Edge[24,16,0,0,0] = expr(1)
Edge[24,17,0,0,0] = expr(1)
Edge[24,18,0,0,0] = expr(1)
Edge[24,19,0,0,0] = expr(1)
Edge[24,20,0,0,0] = expr(1)
Edge[24,21,0,0,0] = expr(1)
Edge[24,22,0,0,0] = expr(1)
Edge[24,23,0,0,0] = expr(1)
Edge[24,24,0,0,0] = expr(1)
Edge[24,25,0,0,0] = expr(1)
Edge[24,26,0,0,0] = expr(1)
Edge[24,27,0,0,0] = expr(1)
Edge[24,28,0,0,0] = expr(1)
Edge[24,29,0,0,0] = expr(1)
Edge[24,30,0,0,0] = expr(1)
Edge[24,31,0,0,0] = expr(1)
Edge[24,32,0,0,0] = expr(1)
Edge[24,33,0,0,0] = expr(1)
Edge[24,34,0,0,0] = expr(1)
Edge[24,35,0,0,0] = expr(1)
Edge_Net[24,0,0,0,0,0:] = exprzeros(6)
Edge_Net[24,1,0,0,0,0:] = exprzeros(6)
Edge_Net[24,2,0,0,0,0:] = exprzeros(6)
Edge_Net[24,3,0,0,0,0:] = exprzeros(6)
Edge_Net[24,4,0,0,0,0:] = exprzeros(6)
Edge_Net[24,5,0,0,0,0:] = exprzeros(6)
Edge_Net[24,6,0,0,0,0:] = exprzeros(6)
Edge_Net[24,7,0,0,0,0:] = exprzeros(6)
Edge_Net[24,8,0,0,0,0:] = exprzeros(6)
Edge_Net[24,9,0,0,0,0:] = exprzeros(6)
Edge_Net[24,10,0,0,0,0:] = exprzeros(6)
Edge_Net[24,11,0,0,0,0:] = exprzeros(6)
Edge_Net[24,12,0,0,0,0:] = exprzeros(6)
Edge_Net[24,13,0,0,0,0:] = exprzeros(6)
Edge_Net[24,14,0,0,0,0:] = exprzeros(6)
Edge_Net[24,15,0,0,0,0:] = exprzeros(6)
Edge_Net[24,16,0,0,0,0:] = exprzeros(6)
Edge_Net[24,17,0,0,0,0:] = exprzeros(6)
Edge_Net[24,18,0,0,0,0:] = exprzeros(6)
Edge_Net[24,19,0,0,0,0:] = exprzeros(6)
Edge_Net[24,20,0,0,0,0:] = exprzeros(6)
Edge_Net[24,21,0,0,0,0:] = exprzeros(6)
Edge_Net[24,22,0,0,0,0:] = exprzeros(6)
Edge_Net[24,23,0,0,0,0:] = exprzeros(6)
Edge_Net[24,24,0,0,0,0:] = exprzeros(6)
Edge_Net[24,25,0,0,0,0:] = exprzeros(6)
Edge_Net[24,26,0,0,0,0:] = exprzeros(6)
Edge_Net[24,27,0,0,0,0:] = exprzeros(6)
Edge_Net[24,28,0,0,0,0:] = exprzeros(6)
Edge_Net[24,29,0,0,0,0:] = exprzeros(6)
Edge_Net[24,30,0,0,0,0:] = exprzeros(6)
Edge_Net[24,31,0,0,0,0:] = exprzeros(6)
Edge_Net[24,32,0,0,0,0:] = exprzeros(6)
Edge_Net[24,33,0,0,0,0:] = exprzeros(6)
Edge_Net[24,34,0,0,0,0:] = exprzeros(6)
Edge_Net[24,35,0,0,0,0:] = exprzeros(6)
Edge[28,0,0,0,0] = expr(1)
Edge[28,1,0,0,0] = expr(1)
Edge[28,2,0,0,0] = expr(1)
Edge[28,3,0,0,0] = expr(1)
Edge[28,4,0,0,0] = expr(1)
Edge[28,5,0,0,0] = expr(1)
Edge[28,6,0,0,0] = expr(1)
Edge[28,7,0,0,0] = expr(1)
Edge[28,8,0,0,0] = expr(1)
Edge[28,9,0,0,0] = expr(1)
Edge[28,10,0,0,0] = expr(1)
Edge[28,11,0,0,0] = expr(1)
Edge[28,12,0,0,0] = expr(1)
Edge[28,13,0,0,0] = expr(1)
Edge[28,14,0,0,0] = expr(1)
Edge[28,15,0,0,0] = expr(1)
Edge[28,16,0,0,0] = expr(1)
Edge[28,17,0,0,0] = expr(1)
Edge[28,18,0,0,0] = expr(1)
Edge[28,19,0,0,0] = expr(1)
Edge[28,20,0,0,0] = expr(1)
Edge[28,21,0,0,0] = expr(1)
Edge[28,22,0,0,0] = expr(1)
Edge[28,23,0,0,0] = expr(1)
Edge[28,24,0,0,0] = expr(1)
Edge[28,25,0,0,0] = expr(1)
Edge[28,26,0,0,0] = expr(1)
Edge[28,27,0,0,0] = expr(1)
Edge[28,28,0,0,0] = expr(1)
Edge[28,29,0,0,0] = expr(1)
Edge[28,30,0,0,0] = expr(1)
Edge[28,31,0,0,0] = expr(1)
Edge[28,32,0,0,0] = expr(1)
Edge[28,33,0,0,0] = expr(1)
Edge[28,34,0,0,0] = expr(1)
Edge[28,35,0,0,0] = expr(1)
Edge_Net[28,0,0,0,0,0:] = exprzeros(6)
Edge_Net[28,1,0,0,0,0:] = exprzeros(6)
Edge_Net[28,2,0,0,0,0:] = exprzeros(6)
Edge_Net[28,3,0,0,0,0:] = exprzeros(6)
Edge_Net[28,4,0,0,0,0:] = exprzeros(6)
Edge_Net[28,5,0,0,0,0:] = exprzeros(6)
Edge_Net[28,6,0,0,0,0:] = exprzeros(6)
Edge_Net[28,7,0,0,0,0:] = exprzeros(6)
Edge_Net[28,8,0,0,0,0:] = exprzeros(6)
Edge_Net[28,9,0,0,0,0:] = exprzeros(6)
Edge_Net[28,10,0,0,0,0:] = exprzeros(6)
Edge_Net[28,11,0,0,0,0:] = exprzeros(6)
Edge_Net[28,12,0,0,0,0:] = exprzeros(6)
Edge_Net[28,13,0,0,0,0:] = exprzeros(6)
Edge_Net[28,14,0,0,0,0:] = exprzeros(6)
Edge_Net[28,15,0,0,0,0:] = exprzeros(6)
Edge_Net[28,16,0,0,0,0:] = exprzeros(6)
Edge_Net[28,17,0,0,0,0:] = exprzeros(6)
Edge_Net[28,18,0,0,0,0:] = exprzeros(6)
Edge_Net[28,19,0,0,0,0:] = exprzeros(6)
Edge_Net[28,20,0,0,0,0:] = exprzeros(6)
Edge_Net[28,21,0,0,0,0:] = exprzeros(6)
Edge_Net[28,22,0,0,0,0:] = exprzeros(6)
Edge_Net[28,23,0,0,0,0:] = exprzeros(6)
Edge_Net[28,24,0,0,0,0:] = exprzeros(6)
Edge_Net[28,25,0,0,0,0:] = exprzeros(6)
Edge_Net[28,26,0,0,0,0:] = exprzeros(6)
Edge_Net[28,27,0,0,0,0:] = exprzeros(6)
Edge_Net[28,28,0,0,0,0:] = exprzeros(6)
Edge_Net[28,29,0,0,0,0:] = exprzeros(6)
Edge_Net[28,30,0,0,0,0:] = exprzeros(6)
Edge_Net[28,31,0,0,0,0:] = exprzeros(6)
Edge_Net[28,32,0,0,0,0:] = exprzeros(6)
Edge_Net[28,33,0,0,0,0:] = exprzeros(6)
Edge_Net[28,34,0,0,0,0:] = exprzeros(6)
Edge_Net[28,35,0,0,0,0:] = exprzeros(6)
Edge[32,0,0,0,0] = expr(1)
Edge[32,1,0,0,0] = expr(1)
Edge[32,2,0,0,0] = expr(1)
Edge[32,3,0,0,0] = expr(1)
Edge[32,4,0,0,0] = expr(1)
Edge[32,5,0,0,0] = expr(1)
Edge[32,6,0,0,0] = expr(1)
Edge[32,7,0,0,0] = expr(1)
Edge[32,8,0,0,0] = expr(1)
Edge[32,9,0,0,0] = expr(1)
Edge[32,10,0,0,0] = expr(1)
Edge[32,11,0,0,0] = expr(1)
Edge[32,12,0,0,0] = expr(1)
Edge[32,13,0,0,0] = expr(1)
Edge[32,14,0,0,0] = expr(1)
Edge[32,15,0,0,0] = expr(1)
Edge[32,16,0,0,0] = expr(1)
Edge[32,17,0,0,0] = expr(1)
Edge[32,18,0,0,0] = expr(1)
Edge[32,19,0,0,0] = expr(1)
Edge[32,20,0,0,0] = expr(1)
Edge[32,21,0,0,0] = expr(1)
Edge[32,22,0,0,0] = expr(1)
Edge[32,23,0,0,0] = expr(1)
Edge[32,24,0,0,0] = expr(1)
Edge[32,25,0,0,0] = expr(1)
Edge[32,26,0,0,0] = expr(1)
Edge[32,27,0,0,0] = expr(1)
Edge[32,28,0,0,0] = expr(1)
Edge[32,29,0,0,0] = expr(1)
Edge[32,30,0,0,0] = expr(1)
Edge[32,31,0,0,0] = expr(1)
Edge[32,32,0,0,0] = expr(1)
Edge[32,33,0,0,0] = expr(1)
Edge[32,34,0,0,0] = expr(1)
Edge[32,35,0,0,0] = expr(1)
Edge_Net[32,0,0,0,0,0:] = exprzeros(6)
Edge_Net[32,1,0,0,0,0:] = exprzeros(6)
Edge_Net[32,2,0,0,0,0:] = exprzeros(6)
Edge_Net[32,3,0,0,0,0:] = exprzeros(6)
Edge_Net[32,4,0,0,0,0:] = exprzeros(6)
Edge_Net[32,5,0,0,0,0:] = exprzeros(6)
Edge_Net[32,6,0,0,0,0:] = exprzeros(6)
Edge_Net[32,7,0,0,0,0:] = exprzeros(6)
Edge_Net[32,8,0,0,0,0:] = exprzeros(6)
Edge_Net[32,9,0,0,0,0:] = exprzeros(6)
Edge_Net[32,10,0,0,0,0:] = exprzeros(6)
Edge_Net[32,11,0,0,0,0:] = exprzeros(6)
Edge_Net[32,12,0,0,0,0:] = exprzeros(6)
Edge_Net[32,13,0,0,0,0:] = exprzeros(6)
Edge_Net[32,14,0,0,0,0:] = exprzeros(6)
Edge_Net[32,15,0,0,0,0:] = exprzeros(6)
Edge_Net[32,16,0,0,0,0:] = exprzeros(6)
Edge_Net[32,17,0,0,0,0:] = exprzeros(6)
Edge_Net[32,18,0,0,0,0:] = exprzeros(6)
Edge_Net[32,19,0,0,0,0:] = exprzeros(6)
Edge_Net[32,20,0,0,0,0:] = exprzeros(6)
Edge_Net[32,21,0,0,0,0:] = exprzeros(6)
Edge_Net[32,22,0,0,0,0:] = exprzeros(6)
Edge_Net[32,23,0,0,0,0:] = exprzeros(6)
Edge_Net[32,24,0,0,0,0:] = exprzeros(6)
Edge_Net[32,25,0,0,0,0:] = exprzeros(6)
Edge_Net[32,26,0,0,0,0:] = exprzeros(6)
Edge_Net[32,27,0,0,0,0:] = exprzeros(6)
Edge_Net[32,28,0,0,0,0:] = exprzeros(6)
Edge_Net[32,29,0,0,0,0:] = exprzeros(6)
Edge_Net[32,30,0,0,0,0:] = exprzeros(6)
Edge_Net[32,31,0,0,0,0:] = exprzeros(6)
Edge_Net[32,32,0,0,0,0:] = exprzeros(6)
Edge_Net[32,33,0,0,0,0:] = exprzeros(6)
Edge_Net[32,34,0,0,0,0:] = exprzeros(6)
Edge_Net[32,35,0,0,0,0:] = exprzeros(6)
Edge[36,0,0,0,0] = expr(1)
Edge[36,1,0,0,0] = expr(1)
Edge[36,2,0,0,0] = expr(1)
Edge[36,3,0,0,0] = expr(1)
Edge[36,4,0,0,0] = expr(1)
Edge[36,5,0,0,0] = expr(1)
Edge[36,6,0,0,0] = expr(1)
Edge[36,7,0,0,0] = expr(1)
Edge[36,8,0,0,0] = expr(1)
Edge[36,9,0,0,0] = expr(1)
Edge[36,10,0,0,0] = expr(1)
Edge[36,11,0,0,0] = expr(1)
Edge[36,12,0,0,0] = expr(1)
Edge[36,13,0,0,0] = expr(1)
Edge[36,14,0,0,0] = expr(1)
Edge[36,15,0,0,0] = expr(1)
Edge[36,16,0,0,0] = expr(1)
Edge[36,17,0,0,0] = expr(1)
Edge[36,18,0,0,0] = expr(1)
Edge[36,19,0,0,0] = expr(1)
Edge[36,20,0,0,0] = expr(1)
Edge[36,21,0,0,0] = expr(1)
Edge[36,22,0,0,0] = expr(1)
Edge[36,23,0,0,0] = expr(1)
Edge[36,24,0,0,0] = expr(1)
Edge[36,25,0,0,0] = expr(1)
Edge[36,26,0,0,0] = expr(1)
Edge[36,27,0,0,0] = expr(1)
Edge[36,28,0,0,0] = expr(1)
Edge[36,29,0,0,0] = expr(1)
Edge[36,30,0,0,0] = expr(1)
Edge[36,31,0,0,0] = expr(1)
Edge[36,32,0,0,0] = expr(1)
Edge[36,33,0,0,0] = expr(1)
Edge[36,34,0,0,0] = expr(1)
Edge[36,35,0,0,0] = expr(1)
Edge_Net[36,0,0,0,0,0:] = exprzeros(6)
Edge_Net[36,1,0,0,0,0:] = exprzeros(6)
Edge_Net[36,2,0,0,0,0:] = exprzeros(6)
Edge_Net[36,3,0,0,0,0:] = exprzeros(6)
Edge_Net[36,4,0,0,0,0:] = exprzeros(6)
Edge_Net[36,5,0,0,0,0:] = exprzeros(6)
Edge_Net[36,6,0,0,0,0:] = exprzeros(6)
Edge_Net[36,7,0,0,0,0:] = exprzeros(6)
Edge_Net[36,8,0,0,0,0:] = exprzeros(6)
Edge_Net[36,9,0,0,0,0:] = exprzeros(6)
Edge_Net[36,10,0,0,0,0:] = exprzeros(6)
Edge_Net[36,11,0,0,0,0:] = exprzeros(6)
Edge_Net[36,12,0,0,0,0:] = exprzeros(6)
Edge_Net[36,13,0,0,0,0:] = exprzeros(6)
Edge_Net[36,14,0,0,0,0:] = exprzeros(6)
Edge_Net[36,15,0,0,0,0:] = exprzeros(6)
Edge_Net[36,16,0,0,0,0:] = exprzeros(6)
Edge_Net[36,17,0,0,0,0:] = exprzeros(6)
Edge_Net[36,18,0,0,0,0:] = exprzeros(6)
Edge_Net[36,19,0,0,0,0:] = exprzeros(6)
Edge_Net[36,20,0,0,0,0:] = exprzeros(6)
Edge_Net[36,21,0,0,0,0:] = exprzeros(6)
Edge_Net[36,22,0,0,0,0:] = exprzeros(6)
Edge_Net[36,23,0,0,0,0:] = exprzeros(6)
Edge_Net[36,24,0,0,0,0:] = exprzeros(6)
Edge_Net[36,25,0,0,0,0:] = exprzeros(6)
Edge_Net[36,26,0,0,0,0:] = exprzeros(6)
Edge_Net[36,27,0,0,0,0:] = exprzeros(6)
Edge_Net[36,28,0,0,0,0:] = exprzeros(6)
Edge_Net[36,29,0,0,0,0:] = exprzeros(6)
Edge_Net[36,30,0,0,0,0:] = exprzeros(6)
Edge_Net[36,31,0,0,0,0:] = exprzeros(6)
Edge_Net[36,32,0,0,0,0:] = exprzeros(6)
Edge_Net[36,33,0,0,0,0:] = exprzeros(6)
Edge_Net[36,34,0,0,0,0:] = exprzeros(6)
Edge_Net[36,35,0,0,0,0:] = exprzeros(6)
Edge[40,0,0,0,0] = expr(1)
Edge[40,1,0,0,0] = expr(1)
Edge[40,2,0,0,0] = expr(1)
Edge[40,3,0,0,0] = expr(1)
Edge[40,4,0,0,0] = expr(1)
Edge[40,5,0,0,0] = expr(1)
Edge[40,6,0,0,0] = expr(1)
Edge[40,7,0,0,0] = expr(1)
Edge[40,8,0,0,0] = expr(1)
Edge[40,9,0,0,0] = expr(1)
Edge[40,10,0,0,0] = expr(1)
Edge[40,11,0,0,0] = expr(1)
Edge[40,12,0,0,0] = expr(1)
Edge[40,13,0,0,0] = expr(1)
Edge[40,14,0,0,0] = expr(1)
Edge[40,15,0,0,0] = expr(1)
Edge[40,16,0,0,0] = expr(1)
Edge[40,17,0,0,0] = expr(1)
Edge[40,18,0,0,0] = expr(1)
Edge[40,19,0,0,0] = expr(1)
Edge[40,20,0,0,0] = expr(1)
Edge[40,21,0,0,0] = expr(1)
Edge[40,22,0,0,0] = expr(1)
Edge[40,23,0,0,0] = expr(1)
Edge[40,24,0,0,0] = expr(1)
Edge[40,25,0,0,0] = expr(1)
Edge[40,26,0,0,0] = expr(1)
Edge[40,27,0,0,0] = expr(1)
Edge[40,28,0,0,0] = expr(1)
Edge[40,29,0,0,0] = expr(1)
Edge[40,30,0,0,0] = expr(1)
Edge[40,31,0,0,0] = expr(1)
Edge[40,32,0,0,0] = expr(1)
Edge[40,33,0,0,0] = expr(1)
Edge[40,34,0,0,0] = expr(1)
Edge[40,35,0,0,0] = expr(1)
Edge_Net[40,0,0,0,0,0:] = exprzeros(6)
Edge_Net[40,1,0,0,0,0:] = exprzeros(6)
Edge_Net[40,2,0,0,0,0:] = exprzeros(6)
Edge_Net[40,3,0,0,0,0:] = exprzeros(6)
Edge_Net[40,4,0,0,0,0:] = exprzeros(6)
Edge_Net[40,5,0,0,0,0:] = exprzeros(6)
Edge_Net[40,6,0,0,0,0:] = exprzeros(6)
Edge_Net[40,7,0,0,0,0:] = exprzeros(6)
Edge_Net[40,8,0,0,0,0:] = exprzeros(6)
Edge_Net[40,9,0,0,0,0:] = exprzeros(6)
Edge_Net[40,10,0,0,0,0:] = exprzeros(6)
Edge_Net[40,11,0,0,0,0:] = exprzeros(6)
Edge_Net[40,12,0,0,0,0:] = exprzeros(6)
Edge_Net[40,13,0,0,0,0:] = exprzeros(6)
Edge_Net[40,14,0,0,0,0:] = exprzeros(6)
Edge_Net[40,15,0,0,0,0:] = exprzeros(6)
Edge_Net[40,16,0,0,0,0:] = exprzeros(6)
Edge_Net[40,17,0,0,0,0:] = exprzeros(6)
Edge_Net[40,18,0,0,0,0:] = exprzeros(6)
Edge_Net[40,19,0,0,0,0:] = exprzeros(6)
Edge_Net[40,20,0,0,0,0:] = exprzeros(6)
Edge_Net[40,21,0,0,0,0:] = exprzeros(6)
Edge_Net[40,22,0,0,0,0:] = exprzeros(6)
Edge_Net[40,23,0,0,0,0:] = exprzeros(6)
Edge_Net[40,24,0,0,0,0:] = exprzeros(6)
Edge_Net[40,25,0,0,0,0:] = exprzeros(6)
Edge_Net[40,26,0,0,0,0:] = exprzeros(6)
Edge_Net[40,27,0,0,0,0:] = exprzeros(6)
Edge_Net[40,28,0,0,0,0:] = exprzeros(6)
Edge_Net[40,29,0,0,0,0:] = exprzeros(6)
Edge_Net[40,30,0,0,0,0:] = exprzeros(6)
Edge_Net[40,31,0,0,0,0:] = exprzeros(6)
Edge_Net[40,32,0,0,0,0:] = exprzeros(6)
Edge_Net[40,33,0,0,0,0:] = exprzeros(6)
Edge_Net[40,34,0,0,0,0:] = exprzeros(6)
Edge_Net[40,35,0,0,0,0:] = exprzeros(6)
Edge[44,0,0,0,0] = expr(1)
Edge[44,1,0,0,0] = expr(1)
Edge[44,2,0,0,0] = expr(1)
Edge[44,3,0,0,0] = expr(1)
Edge[44,4,0,0,0] = expr(1)
Edge[44,5,0,0,0] = expr(1)
Edge[44,6,0,0,0] = expr(1)
Edge[44,7,0,0,0] = expr(1)
Edge[44,8,0,0,0] = expr(1)
Edge[44,9,0,0,0] = expr(1)
Edge[44,10,0,0,0] = expr(1)
Edge[44,11,0,0,0] = expr(1)
Edge[44,12,0,0,0] = expr(1)
Edge[44,13,0,0,0] = expr(1)
Edge[44,14,0,0,0] = expr(1)
Edge[44,15,0,0,0] = expr(1)
Edge[44,16,0,0,0] = expr(1)
Edge[44,17,0,0,0] = expr(1)
Edge[44,18,0,0,0] = expr(1)
Edge[44,19,0,0,0] = expr(1)
Edge[44,20,0,0,0] = expr(1)
Edge[44,21,0,0,0] = expr(1)
Edge[44,22,0,0,0] = expr(1)
Edge[44,23,0,0,0] = expr(1)
Edge[44,24,0,0,0] = expr(1)
Edge[44,25,0,0,0] = expr(1)
Edge[44,26,0,0,0] = expr(1)
Edge[44,27,0,0,0] = expr(1)
Edge[44,28,0,0,0] = expr(1)
Edge[44,29,0,0,0] = expr(1)
Edge[44,30,0,0,0] = expr(1)
Edge[44,31,0,0,0] = expr(1)
Edge[44,32,0,0,0] = expr(1)
Edge[44,33,0,0,0] = expr(1)
Edge[44,34,0,0,0] = expr(1)
Edge[44,35,0,0,0] = expr(1)
Edge_Net[44,0,0,0,0,0:] = exprzeros(6)
Edge_Net[44,1,0,0,0,0:] = exprzeros(6)
Edge_Net[44,2,0,0,0,0:] = exprzeros(6)
Edge_Net[44,3,0,0,0,0:] = exprzeros(6)
Edge_Net[44,4,0,0,0,0:] = exprzeros(6)
Edge_Net[44,5,0,0,0,0:] = exprzeros(6)
Edge_Net[44,6,0,0,0,0:] = exprzeros(6)
Edge_Net[44,7,0,0,0,0:] = exprzeros(6)
Edge_Net[44,8,0,0,0,0:] = exprzeros(6)
Edge_Net[44,9,0,0,0,0:] = exprzeros(6)
Edge_Net[44,10,0,0,0,0:] = exprzeros(6)
Edge_Net[44,11,0,0,0,0:] = exprzeros(6)
Edge_Net[44,12,0,0,0,0:] = exprzeros(6)
Edge_Net[44,13,0,0,0,0:] = exprzeros(6)
Edge_Net[44,14,0,0,0,0:] = exprzeros(6)
Edge_Net[44,15,0,0,0,0:] = exprzeros(6)
Edge_Net[44,16,0,0,0,0:] = exprzeros(6)
Edge_Net[44,17,0,0,0,0:] = exprzeros(6)
Edge_Net[44,18,0,0,0,0:] = exprzeros(6)
Edge_Net[44,19,0,0,0,0:] = exprzeros(6)
Edge_Net[44,20,0,0,0,0:] = exprzeros(6)
Edge_Net[44,21,0,0,0,0:] = exprzeros(6)
Edge_Net[44,22,0,0,0,0:] = exprzeros(6)
Edge_Net[44,23,0,0,0,0:] = exprzeros(6)
Edge_Net[44,24,0,0,0,0:] = exprzeros(6)
Edge_Net[44,25,0,0,0,0:] = exprzeros(6)
Edge_Net[44,26,0,0,0,0:] = exprzeros(6)
Edge_Net[44,27,0,0,0,0:] = exprzeros(6)
Edge_Net[44,28,0,0,0,0:] = exprzeros(6)
Edge_Net[44,29,0,0,0,0:] = exprzeros(6)
Edge_Net[44,30,0,0,0,0:] = exprzeros(6)
Edge_Net[44,31,0,0,0,0:] = exprzeros(6)
Edge_Net[44,32,0,0,0,0:] = exprzeros(6)
Edge_Net[44,33,0,0,0,0:] = exprzeros(6)
Edge_Net[44,34,0,0,0,0:] = exprzeros(6)
Edge_Net[44,35,0,0,0,0:] = exprzeros(6)
Edge[48,0,0,0,0] = expr(1)
Edge[48,1,0,0,0] = expr(1)
Edge[48,2,0,0,0] = expr(1)
Edge[48,3,0,0,0] = expr(1)
Edge[48,4,0,0,0] = expr(1)
Edge[48,5,0,0,0] = expr(1)
Edge[48,6,0,0,0] = expr(1)
Edge[48,7,0,0,0] = expr(1)
Edge[48,8,0,0,0] = expr(1)
Edge[48,9,0,0,0] = expr(1)
Edge[48,10,0,0,0] = expr(1)
Edge[48,11,0,0,0] = expr(1)
Edge[48,12,0,0,0] = expr(1)
Edge[48,13,0,0,0] = expr(1)
Edge[48,14,0,0,0] = expr(1)
Edge[48,15,0,0,0] = expr(1)
Edge[48,16,0,0,0] = expr(1)
Edge[48,17,0,0,0] = expr(1)
Edge[48,18,0,0,0] = expr(1)
Edge[48,19,0,0,0] = expr(1)
Edge[48,20,0,0,0] = expr(1)
Edge[48,21,0,0,0] = expr(1)
Edge[48,22,0,0,0] = expr(1)
Edge[48,23,0,0,0] = expr(1)
Edge[48,24,0,0,0] = expr(1)
Edge[48,25,0,0,0] = expr(1)
Edge[48,26,0,0,0] = expr(1)
Edge[48,27,0,0,0] = expr(1)
Edge[48,28,0,0,0] = expr(1)
Edge[48,29,0,0,0] = expr(1)
Edge[48,30,0,0,0] = expr(1)
Edge[48,31,0,0,0] = expr(1)
Edge[48,32,0,0,0] = expr(1)
Edge[48,33,0,0,0] = expr(1)
Edge[48,34,0,0,0] = expr(1)
Edge[48,35,0,0,0] = expr(1)
Edge_Net[48,0,0,0,0,0:] = exprzeros(6)
Edge_Net[48,1,0,0,0,0:] = exprzeros(6)
Edge_Net[48,2,0,0,0,0:] = exprzeros(6)
Edge_Net[48,3,0,0,0,0:] = exprzeros(6)
Edge_Net[48,4,0,0,0,0:] = exprzeros(6)
Edge_Net[48,5,0,0,0,0:] = exprzeros(6)
Edge_Net[48,6,0,0,0,0:] = exprzeros(6)
Edge_Net[48,7,0,0,0,0:] = exprzeros(6)
Edge_Net[48,8,0,0,0,0:] = exprzeros(6)
Edge_Net[48,9,0,0,0,0:] = exprzeros(6)
Edge_Net[48,10,0,0,0,0:] = exprzeros(6)
Edge_Net[48,11,0,0,0,0:] = exprzeros(6)
Edge_Net[48,12,0,0,0,0:] = exprzeros(6)
Edge_Net[48,13,0,0,0,0:] = exprzeros(6)
Edge_Net[48,14,0,0,0,0:] = exprzeros(6)
Edge_Net[48,15,0,0,0,0:] = exprzeros(6)
Edge_Net[48,16,0,0,0,0:] = exprzeros(6)
Edge_Net[48,17,0,0,0,0:] = exprzeros(6)
Edge_Net[48,18,0,0,0,0:] = exprzeros(6)
Edge_Net[48,19,0,0,0,0:] = exprzeros(6)
Edge_Net[48,20,0,0,0,0:] = exprzeros(6)
Edge_Net[48,21,0,0,0,0:] = exprzeros(6)
Edge_Net[48,22,0,0,0,0:] = exprzeros(6)
Edge_Net[48,23,0,0,0,0:] = exprzeros(6)
Edge_Net[48,24,0,0,0,0:] = exprzeros(6)
Edge_Net[48,25,0,0,0,0:] = exprzeros(6)
Edge_Net[48,26,0,0,0,0:] = exprzeros(6)
Edge_Net[48,27,0,0,0,0:] = exprzeros(6)
Edge_Net[48,28,0,0,0,0:] = exprzeros(6)
Edge_Net[48,29,0,0,0,0:] = exprzeros(6)
Edge_Net[48,30,0,0,0,0:] = exprzeros(6)
Edge_Net[48,31,0,0,0,0:] = exprzeros(6)
Edge_Net[48,32,0,0,0,0:] = exprzeros(6)
Edge_Net[48,33,0,0,0,0:] = exprzeros(6)
Edge_Net[48,34,0,0,0,0:] = exprzeros(6)
Edge_Net[48,35,0,0,0,0:] = exprzeros(6)
Edge[52,0,0,0,0] = expr(1)
Edge[52,1,0,0,0] = expr(1)
Edge[52,2,0,0,0] = expr(1)
Edge[52,3,0,0,0] = expr(1)
Edge[52,4,0,0,0] = expr(1)
Edge[52,5,0,0,0] = expr(1)
Edge[52,6,0,0,0] = expr(1)
Edge[52,7,0,0,0] = expr(1)
Edge[52,8,0,0,0] = expr(1)
Edge[52,9,0,0,0] = expr(1)
Edge[52,10,0,0,0] = expr(1)
Edge[52,11,0,0,0] = expr(1)
Edge[52,12,0,0,0] = expr(1)
Edge[52,13,0,0,0] = expr(1)
Edge[52,14,0,0,0] = expr(1)
Edge[52,15,0,0,0] = expr(1)
Edge[52,16,0,0,0] = expr(1)
Edge[52,17,0,0,0] = expr(1)
Edge[52,18,0,0,0] = expr(1)
Edge[52,19,0,0,0] = expr(1)
Edge[52,20,0,0,0] = expr(1)
Edge[52,21,0,0,0] = expr(1)
Edge[52,22,0,0,0] = expr(1)
Edge[52,23,0,0,0] = expr(1)
Edge[52,24,0,0,0] = expr(1)
Edge[52,25,0,0,0] = expr(1)
Edge[52,26,0,0,0] = expr(1)
Edge[52,27,0,0,0] = expr(1)
Edge[52,28,0,0,0] = expr(1)
Edge[52,29,0,0,0] = expr(1)
Edge[52,30,0,0,0] = expr(1)
Edge[52,31,0,0,0] = expr(1)
Edge[52,32,0,0,0] = expr(1)
Edge[52,33,0,0,0] = expr(1)
Edge[52,34,0,0,0] = expr(1)
Edge[52,35,0,0,0] = expr(1)
Edge_Net[52,0,0,0,0,0:] = exprzeros(6)
Edge_Net[52,1,0,0,0,0:] = exprzeros(6)
Edge_Net[52,2,0,0,0,0:] = exprzeros(6)
Edge_Net[52,3,0,0,0,0:] = exprzeros(6)
Edge_Net[52,4,0,0,0,0:] = exprzeros(6)
Edge_Net[52,5,0,0,0,0:] = exprzeros(6)
Edge_Net[52,6,0,0,0,0:] = exprzeros(6)
Edge_Net[52,7,0,0,0,0:] = exprzeros(6)
Edge_Net[52,8,0,0,0,0:] = exprzeros(6)
Edge_Net[52,9,0,0,0,0:] = exprzeros(6)
Edge_Net[52,10,0,0,0,0:] = exprzeros(6)
Edge_Net[52,11,0,0,0,0:] = exprzeros(6)
Edge_Net[52,12,0,0,0,0:] = exprzeros(6)
Edge_Net[52,13,0,0,0,0:] = exprzeros(6)
Edge_Net[52,14,0,0,0,0:] = exprzeros(6)
Edge_Net[52,15,0,0,0,0:] = exprzeros(6)
Edge_Net[52,16,0,0,0,0:] = exprzeros(6)
Edge_Net[52,17,0,0,0,0:] = exprzeros(6)
Edge_Net[52,18,0,0,0,0:] = exprzeros(6)
Edge_Net[52,19,0,0,0,0:] = exprzeros(6)
Edge_Net[52,20,0,0,0,0:] = exprzeros(6)
Edge_Net[52,21,0,0,0,0:] = exprzeros(6)
Edge_Net[52,22,0,0,0,0:] = exprzeros(6)
Edge_Net[52,23,0,0,0,0:] = exprzeros(6)
Edge_Net[52,24,0,0,0,0:] = exprzeros(6)
Edge_Net[52,25,0,0,0,0:] = exprzeros(6)
Edge_Net[52,26,0,0,0,0:] = exprzeros(6)
Edge_Net[52,27,0,0,0,0:] = exprzeros(6)
Edge_Net[52,28,0,0,0,0:] = exprzeros(6)
Edge_Net[52,29,0,0,0,0:] = exprzeros(6)
Edge_Net[52,30,0,0,0,0:] = exprzeros(6)
Edge_Net[52,31,0,0,0,0:] = exprzeros(6)
Edge_Net[52,32,0,0,0,0:] = exprzeros(6)
Edge_Net[52,33,0,0,0,0:] = exprzeros(6)
Edge_Net[52,34,0,0,0,0:] = exprzeros(6)
Edge_Net[52,35,0,0,0,0:] = exprzeros(6)
Edge[56,0,0,0,0] = expr(1)
Edge[56,1,0,0,0] = expr(1)
Edge[56,2,0,0,0] = expr(1)
Edge[56,3,0,0,0] = expr(1)
Edge[56,4,0,0,0] = expr(1)
Edge[56,5,0,0,0] = expr(1)
Edge[56,6,0,0,0] = expr(1)
Edge[56,7,0,0,0] = expr(1)
Edge[56,8,0,0,0] = expr(1)
Edge[56,9,0,0,0] = expr(1)
Edge[56,10,0,0,0] = expr(1)
Edge[56,11,0,0,0] = expr(1)
Edge[56,12,0,0,0] = expr(1)
Edge[56,13,0,0,0] = expr(1)
Edge[56,14,0,0,0] = expr(1)
Edge[56,15,0,0,0] = expr(1)
Edge[56,16,0,0,0] = expr(1)
Edge[56,17,0,0,0] = expr(1)
Edge[56,18,0,0,0] = expr(1)
Edge[56,19,0,0,0] = expr(1)
Edge[56,20,0,0,0] = expr(1)
Edge[56,21,0,0,0] = expr(1)
Edge[56,22,0,0,0] = expr(1)
Edge[56,23,0,0,0] = expr(1)
Edge[56,24,0,0,0] = expr(1)
Edge[56,25,0,0,0] = expr(1)
Edge[56,26,0,0,0] = expr(1)
Edge[56,27,0,0,0] = expr(1)
Edge[56,28,0,0,0] = expr(1)
Edge[56,29,0,0,0] = expr(1)
Edge[56,30,0,0,0] = expr(1)
Edge[56,31,0,0,0] = expr(1)
Edge[56,32,0,0,0] = expr(1)
Edge[56,33,0,0,0] = expr(1)
Edge[56,34,0,0,0] = expr(1)
Edge[56,35,0,0,0] = expr(1)
Edge_Net[56,0,0,0,0,0:] = exprzeros(6)
Edge_Net[56,1,0,0,0,0:] = exprzeros(6)
Edge_Net[56,2,0,0,0,0:] = exprzeros(6)
Edge_Net[56,3,0,0,0,0:] = exprzeros(6)
Edge_Net[56,4,0,0,0,0:] = exprzeros(6)
Edge_Net[56,5,0,0,0,0:] = exprzeros(6)
Edge_Net[56,6,0,0,0,0:] = exprzeros(6)
Edge_Net[56,7,0,0,0,0:] = exprzeros(6)
Edge_Net[56,8,0,0,0,0:] = exprzeros(6)
Edge_Net[56,9,0,0,0,0:] = exprzeros(6)
Edge_Net[56,10,0,0,0,0:] = exprzeros(6)
Edge_Net[56,11,0,0,0,0:] = exprzeros(6)
Edge_Net[56,12,0,0,0,0:] = exprzeros(6)
Edge_Net[56,13,0,0,0,0:] = exprzeros(6)
Edge_Net[56,14,0,0,0,0:] = exprzeros(6)
Edge_Net[56,15,0,0,0,0:] = exprzeros(6)
Edge_Net[56,16,0,0,0,0:] = exprzeros(6)
Edge_Net[56,17,0,0,0,0:] = exprzeros(6)
Edge_Net[56,18,0,0,0,0:] = exprzeros(6)
Edge_Net[56,19,0,0,0,0:] = exprzeros(6)
Edge_Net[56,20,0,0,0,0:] = exprzeros(6)
Edge_Net[56,21,0,0,0,0:] = exprzeros(6)
Edge_Net[56,22,0,0,0,0:] = exprzeros(6)
Edge_Net[56,23,0,0,0,0:] = exprzeros(6)
Edge_Net[56,24,0,0,0,0:] = exprzeros(6)
Edge_Net[56,25,0,0,0,0:] = exprzeros(6)
Edge_Net[56,26,0,0,0,0:] = exprzeros(6)
Edge_Net[56,27,0,0,0,0:] = exprzeros(6)
Edge_Net[56,28,0,0,0,0:] = exprzeros(6)
Edge_Net[56,29,0,0,0,0:] = exprzeros(6)
Edge_Net[56,30,0,0,0,0:] = exprzeros(6)
Edge_Net[56,31,0,0,0,0:] = exprzeros(6)
Edge_Net[56,32,0,0,0,0:] = exprzeros(6)
Edge_Net[56,33,0,0,0,0:] = exprzeros(6)
Edge_Net[56,34,0,0,0,0:] = exprzeros(6)
Edge_Net[56,35,0,0,0,0:] = exprzeros(6)
Edge[60,0,0,0,0] = expr(1)
Edge[60,1,0,0,0] = expr(1)
Edge[60,2,0,0,0] = expr(1)
Edge[60,3,0,0,0] = expr(1)
Edge[60,4,0,0,0] = expr(1)
Edge[60,5,0,0,0] = expr(1)
Edge[60,6,0,0,0] = expr(1)
Edge[60,7,0,0,0] = expr(1)
Edge[60,8,0,0,0] = expr(1)
Edge[60,9,0,0,0] = expr(1)
Edge[60,10,0,0,0] = expr(1)
Edge[60,11,0,0,0] = expr(1)
Edge[60,12,0,0,0] = expr(1)
Edge[60,13,0,0,0] = expr(1)
Edge[60,14,0,0,0] = expr(1)
Edge[60,15,0,0,0] = expr(1)
Edge[60,16,0,0,0] = expr(1)
Edge[60,17,0,0,0] = expr(1)
Edge[60,18,0,0,0] = expr(1)
Edge[60,19,0,0,0] = expr(1)
Edge[60,20,0,0,0] = expr(1)
Edge[60,21,0,0,0] = expr(1)
Edge[60,22,0,0,0] = expr(1)
Edge[60,23,0,0,0] = expr(1)
Edge[60,24,0,0,0] = expr(1)
Edge[60,25,0,0,0] = expr(1)
Edge[60,26,0,0,0] = expr(1)
Edge[60,27,0,0,0] = expr(1)
Edge[60,28,0,0,0] = expr(1)
Edge[60,29,0,0,0] = expr(1)
Edge[60,30,0,0,0] = expr(1)
Edge[60,31,0,0,0] = expr(1)
Edge[60,32,0,0,0] = expr(1)
Edge[60,33,0,0,0] = expr(1)
Edge[60,34,0,0,0] = expr(1)
Edge[60,35,0,0,0] = expr(1)
Edge_Net[60,0,0,0,0,0:] = exprzeros(6)
Edge_Net[60,1,0,0,0,0:] = exprzeros(6)
Edge_Net[60,2,0,0,0,0:] = exprzeros(6)
Edge_Net[60,3,0,0,0,0:] = exprzeros(6)
Edge_Net[60,4,0,0,0,0:] = exprzeros(6)
Edge_Net[60,5,0,0,0,0:] = exprzeros(6)
Edge_Net[60,6,0,0,0,0:] = exprzeros(6)
Edge_Net[60,7,0,0,0,0:] = exprzeros(6)
Edge_Net[60,8,0,0,0,0:] = exprzeros(6)
Edge_Net[60,9,0,0,0,0:] = exprzeros(6)
Edge_Net[60,10,0,0,0,0:] = exprzeros(6)
Edge_Net[60,11,0,0,0,0:] = exprzeros(6)
Edge_Net[60,12,0,0,0,0:] = exprzeros(6)
Edge_Net[60,13,0,0,0,0:] = exprzeros(6)
Edge_Net[60,14,0,0,0,0:] = exprzeros(6)
Edge_Net[60,15,0,0,0,0:] = exprzeros(6)
Edge_Net[60,16,0,0,0,0:] = exprzeros(6)
Edge_Net[60,17,0,0,0,0:] = exprzeros(6)
Edge_Net[60,18,0,0,0,0:] = exprzeros(6)
Edge_Net[60,19,0,0,0,0:] = exprzeros(6)
Edge_Net[60,20,0,0,0,0:] = exprzeros(6)
Edge_Net[60,21,0,0,0,0:] = exprzeros(6)
Edge_Net[60,22,0,0,0,0:] = exprzeros(6)
Edge_Net[60,23,0,0,0,0:] = exprzeros(6)
Edge_Net[60,24,0,0,0,0:] = exprzeros(6)
Edge_Net[60,25,0,0,0,0:] = exprzeros(6)
Edge_Net[60,26,0,0,0,0:] = exprzeros(6)
Edge_Net[60,27,0,0,0,0:] = exprzeros(6)
Edge_Net[60,28,0,0,0,0:] = exprzeros(6)
Edge_Net[60,29,0,0,0,0:] = exprzeros(6)
Edge_Net[60,30,0,0,0,0:] = exprzeros(6)
Edge_Net[60,31,0,0,0,0:] = exprzeros(6)
Edge_Net[60,32,0,0,0,0:] = exprzeros(6)
Edge_Net[60,33,0,0,0,0:] = exprzeros(6)
Edge_Net[60,34,0,0,0,0:] = exprzeros(6)
Edge_Net[60,35,0,0,0,0:] = exprzeros(6)
Edge[64,0,0,0,0] = expr(1)
Edge[64,1,0,0,0] = expr(1)
Edge[64,2,0,0,0] = expr(1)
Edge[64,3,0,0,0] = expr(1)
Edge[64,4,0,0,0] = expr(1)
Edge[64,5,0,0,0] = expr(1)
Edge[64,6,0,0,0] = expr(1)
Edge[64,7,0,0,0] = expr(1)
Edge[64,8,0,0,0] = expr(1)
Edge[64,9,0,0,0] = expr(1)
Edge[64,10,0,0,0] = expr(1)
Edge[64,11,0,0,0] = expr(1)
Edge[64,12,0,0,0] = expr(1)
Edge[64,13,0,0,0] = expr(1)
Edge[64,14,0,0,0] = expr(1)
Edge[64,15,0,0,0] = expr(1)
Edge[64,16,0,0,0] = expr(1)
Edge[64,17,0,0,0] = expr(1)
Edge[64,18,0,0,0] = expr(1)
Edge[64,19,0,0,0] = expr(1)
Edge[64,20,0,0,0] = expr(1)
Edge[64,21,0,0,0] = expr(1)
Edge[64,22,0,0,0] = expr(1)
Edge[64,23,0,0,0] = expr(1)
Edge[64,24,0,0,0] = expr(1)
Edge[64,25,0,0,0] = expr(1)
Edge[64,26,0,0,0] = expr(1)
Edge[64,27,0,0,0] = expr(1)
Edge[64,28,0,0,0] = expr(1)
Edge[64,29,0,0,0] = expr(1)
Edge[64,30,0,0,0] = expr(1)
Edge[64,31,0,0,0] = expr(1)
Edge[64,32,0,0,0] = expr(1)
Edge[64,33,0,0,0] = expr(1)
Edge[64,34,0,0,0] = expr(1)
Edge[64,35,0,0,0] = expr(1)
Edge_Net[64,0,0,0,0,0:] = exprzeros(6)
Edge_Net[64,1,0,0,0,0:] = exprzeros(6)
Edge_Net[64,2,0,0,0,0:] = exprzeros(6)
Edge_Net[64,3,0,0,0,0:] = exprzeros(6)
Edge_Net[64,4,0,0,0,0:] = exprzeros(6)
Edge_Net[64,5,0,0,0,0:] = exprzeros(6)
Edge_Net[64,6,0,0,0,0:] = exprzeros(6)
Edge_Net[64,7,0,0,0,0:] = exprzeros(6)
Edge_Net[64,8,0,0,0,0:] = exprzeros(6)
Edge_Net[64,9,0,0,0,0:] = exprzeros(6)
Edge_Net[64,10,0,0,0,0:] = exprzeros(6)
Edge_Net[64,11,0,0,0,0:] = exprzeros(6)
Edge_Net[64,12,0,0,0,0:] = exprzeros(6)
Edge_Net[64,13,0,0,0,0:] = exprzeros(6)
Edge_Net[64,14,0,0,0,0:] = exprzeros(6)
Edge_Net[64,15,0,0,0,0:] = exprzeros(6)
Edge_Net[64,16,0,0,0,0:] = exprzeros(6)
Edge_Net[64,17,0,0,0,0:] = exprzeros(6)
Edge_Net[64,18,0,0,0,0:] = exprzeros(6)
Edge_Net[64,19,0,0,0,0:] = exprzeros(6)
Edge_Net[64,20,0,0,0,0:] = exprzeros(6)
Edge_Net[64,21,0,0,0,0:] = exprzeros(6)
Edge_Net[64,22,0,0,0,0:] = exprzeros(6)
Edge_Net[64,23,0,0,0,0:] = exprzeros(6)
Edge_Net[64,24,0,0,0,0:] = exprzeros(6)
Edge_Net[64,25,0,0,0,0:] = exprzeros(6)
Edge_Net[64,26,0,0,0,0:] = exprzeros(6)
Edge_Net[64,27,0,0,0,0:] = exprzeros(6)
Edge_Net[64,28,0,0,0,0:] = exprzeros(6)
Edge_Net[64,29,0,0,0,0:] = exprzeros(6)
Edge_Net[64,30,0,0,0,0:] = exprzeros(6)
Edge_Net[64,31,0,0,0,0:] = exprzeros(6)
Edge_Net[64,32,0,0,0,0:] = exprzeros(6)
Edge_Net[64,33,0,0,0,0:] = exprzeros(6)
Edge_Net[64,34,0,0,0,0:] = exprzeros(6)
Edge_Net[64,35,0,0,0,0:] = exprzeros(6)
Edge[68,0,0,0,0] = expr(1)
Edge[68,1,0,0,0] = expr(1)
Edge[68,2,0,0,0] = expr(1)
Edge[68,3,0,0,0] = expr(1)
Edge[68,4,0,0,0] = expr(1)
Edge[68,5,0,0,0] = expr(1)
Edge[68,6,0,0,0] = expr(1)
Edge[68,7,0,0,0] = expr(1)
Edge[68,8,0,0,0] = expr(1)
Edge[68,9,0,0,0] = expr(1)
Edge[68,10,0,0,0] = expr(1)
Edge[68,11,0,0,0] = expr(1)
Edge[68,12,0,0,0] = expr(1)
Edge[68,13,0,0,0] = expr(1)
Edge[68,14,0,0,0] = expr(1)
Edge[68,15,0,0,0] = expr(1)
Edge[68,16,0,0,0] = expr(1)
Edge[68,17,0,0,0] = expr(1)
Edge[68,18,0,0,0] = expr(1)
Edge[68,19,0,0,0] = expr(1)
Edge[68,20,0,0,0] = expr(1)
Edge[68,21,0,0,0] = expr(1)
Edge[68,22,0,0,0] = expr(1)
Edge[68,23,0,0,0] = expr(1)
Edge[68,24,0,0,0] = expr(1)
Edge[68,25,0,0,0] = expr(1)
Edge[68,26,0,0,0] = expr(1)
Edge[68,27,0,0,0] = expr(1)
Edge[68,28,0,0,0] = expr(1)
Edge[68,29,0,0,0] = expr(1)
Edge[68,30,0,0,0] = expr(1)
Edge[68,31,0,0,0] = expr(1)
Edge[68,32,0,0,0] = expr(1)
Edge[68,33,0,0,0] = expr(1)
Edge[68,34,0,0,0] = expr(1)
Edge[68,35,0,0,0] = expr(1)
Edge_Net[68,0,0,0,0,0:] = exprzeros(6)
Edge_Net[68,1,0,0,0,0:] = exprzeros(6)
Edge_Net[68,2,0,0,0,0:] = exprzeros(6)
Edge_Net[68,3,0,0,0,0:] = exprzeros(6)
Edge_Net[68,4,0,0,0,0:] = exprzeros(6)
Edge_Net[68,5,0,0,0,0:] = exprzeros(6)
Edge_Net[68,6,0,0,0,0:] = exprzeros(6)
Edge_Net[68,7,0,0,0,0:] = exprzeros(6)
Edge_Net[68,8,0,0,0,0:] = exprzeros(6)
Edge_Net[68,9,0,0,0,0:] = exprzeros(6)
Edge_Net[68,10,0,0,0,0:] = exprzeros(6)
Edge_Net[68,11,0,0,0,0:] = exprzeros(6)
Edge_Net[68,12,0,0,0,0:] = exprzeros(6)
Edge_Net[68,13,0,0,0,0:] = exprzeros(6)
Edge_Net[68,14,0,0,0,0:] = exprzeros(6)
Edge_Net[68,15,0,0,0,0:] = exprzeros(6)
Edge_Net[68,16,0,0,0,0:] = exprzeros(6)
Edge_Net[68,17,0,0,0,0:] = exprzeros(6)
Edge_Net[68,18,0,0,0,0:] = exprzeros(6)
Edge_Net[68,19,0,0,0,0:] = exprzeros(6)
Edge_Net[68,20,0,0,0,0:] = exprzeros(6)
Edge_Net[68,21,0,0,0,0:] = exprzeros(6)
Edge_Net[68,22,0,0,0,0:] = exprzeros(6)
Edge_Net[68,23,0,0,0,0:] = exprzeros(6)
Edge_Net[68,24,0,0,0,0:] = exprzeros(6)
Edge_Net[68,25,0,0,0,0:] = exprzeros(6)
Edge_Net[68,26,0,0,0,0:] = exprzeros(6)
Edge_Net[68,27,0,0,0,0:] = exprzeros(6)
Edge_Net[68,28,0,0,0,0:] = exprzeros(6)
Edge_Net[68,29,0,0,0,0:] = exprzeros(6)
Edge_Net[68,30,0,0,0,0:] = exprzeros(6)
Edge_Net[68,31,0,0,0,0:] = exprzeros(6)
Edge_Net[68,32,0,0,0,0:] = exprzeros(6)
Edge_Net[68,33,0,0,0,0:] = exprzeros(6)
Edge_Net[68,34,0,0,0,0:] = exprzeros(6)
Edge_Net[68,35,0,0,0,0:] = exprzeros(6)
Edge[72,0,0,0,0] = expr(1)
Edge[72,1,0,0,0] = expr(1)
Edge[72,2,0,0,0] = expr(1)
Edge[72,3,0,0,0] = expr(1)
Edge[72,4,0,0,0] = expr(1)
Edge[72,5,0,0,0] = expr(1)
Edge[72,6,0,0,0] = expr(1)
Edge[72,7,0,0,0] = expr(1)
Edge[72,8,0,0,0] = expr(1)
Edge[72,9,0,0,0] = expr(1)
Edge[72,10,0,0,0] = expr(1)
Edge[72,11,0,0,0] = expr(1)
Edge[72,12,0,0,0] = expr(1)
Edge[72,13,0,0,0] = expr(1)
Edge[72,14,0,0,0] = expr(1)
Edge[72,15,0,0,0] = expr(1)
Edge[72,16,0,0,0] = expr(1)
Edge[72,17,0,0,0] = expr(1)
Edge[72,18,0,0,0] = expr(1)
Edge[72,19,0,0,0] = expr(1)
Edge[72,20,0,0,0] = expr(1)
Edge[72,21,0,0,0] = expr(1)
Edge[72,22,0,0,0] = expr(1)
Edge[72,23,0,0,0] = expr(1)
Edge[72,24,0,0,0] = expr(1)
Edge[72,25,0,0,0] = expr(1)
Edge[72,26,0,0,0] = expr(1)
Edge[72,27,0,0,0] = expr(1)
Edge[72,28,0,0,0] = expr(1)
Edge[72,29,0,0,0] = expr(1)
Edge[72,30,0,0,0] = expr(1)
Edge[72,31,0,0,0] = expr(1)
Edge[72,32,0,0,0] = expr(1)
Edge[72,33,0,0,0] = expr(1)
Edge[72,34,0,0,0] = expr(1)
Edge[72,35,0,0,0] = expr(1)
Edge_Net[72,0,0,0,0,0:] = exprzeros(6)
Edge_Net[72,1,0,0,0,0:] = exprzeros(6)
Edge_Net[72,2,0,0,0,0:] = exprzeros(6)
Edge_Net[72,3,0,0,0,0:] = exprzeros(6)
Edge_Net[72,4,0,0,0,0:] = exprzeros(6)
Edge_Net[72,5,0,0,0,0:] = exprzeros(6)
Edge_Net[72,6,0,0,0,0:] = exprzeros(6)
Edge_Net[72,7,0,0,0,0:] = exprzeros(6)
Edge_Net[72,8,0,0,0,0:] = exprzeros(6)
Edge_Net[72,9,0,0,0,0:] = exprzeros(6)
Edge_Net[72,10,0,0,0,0:] = exprzeros(6)
Edge_Net[72,11,0,0,0,0:] = exprzeros(6)
Edge_Net[72,12,0,0,0,0:] = exprzeros(6)
Edge_Net[72,13,0,0,0,0:] = exprzeros(6)
Edge_Net[72,14,0,0,0,0:] = exprzeros(6)
Edge_Net[72,15,0,0,0,0:] = exprzeros(6)
Edge_Net[72,16,0,0,0,0:] = exprzeros(6)
Edge_Net[72,17,0,0,0,0:] = exprzeros(6)
Edge_Net[72,18,0,0,0,0:] = exprzeros(6)
Edge_Net[72,19,0,0,0,0:] = exprzeros(6)
Edge_Net[72,20,0,0,0,0:] = exprzeros(6)
Edge_Net[72,21,0,0,0,0:] = exprzeros(6)
Edge_Net[72,22,0,0,0,0:] = exprzeros(6)
Edge_Net[72,23,0,0,0,0:] = exprzeros(6)
Edge_Net[72,24,0,0,0,0:] = exprzeros(6)
Edge_Net[72,25,0,0,0,0:] = exprzeros(6)
Edge_Net[72,26,0,0,0,0:] = exprzeros(6)
Edge_Net[72,27,0,0,0,0:] = exprzeros(6)
Edge_Net[72,28,0,0,0,0:] = exprzeros(6)
Edge_Net[72,29,0,0,0,0:] = exprzeros(6)
Edge_Net[72,30,0,0,0,0:] = exprzeros(6)
Edge_Net[72,31,0,0,0,0:] = exprzeros(6)
Edge_Net[72,32,0,0,0,0:] = exprzeros(6)
Edge_Net[72,33,0,0,0,0:] = exprzeros(6)
Edge_Net[72,34,0,0,0,0:] = exprzeros(6)
Edge_Net[72,35,0,0,0,0:] = exprzeros(6)
Edge[76,0,0,0,0] = expr(1)
Edge[76,1,0,0,0] = expr(1)
Edge[76,2,0,0,0] = expr(1)
Edge[76,3,0,0,0] = expr(1)
Edge[76,4,0,0,0] = expr(1)
Edge[76,5,0,0,0] = expr(1)
Edge[76,6,0,0,0] = expr(1)
Edge[76,7,0,0,0] = expr(1)
Edge[76,8,0,0,0] = expr(1)
Edge[76,9,0,0,0] = expr(1)
Edge[76,10,0,0,0] = expr(1)
Edge[76,11,0,0,0] = expr(1)
Edge[76,12,0,0,0] = expr(1)
Edge[76,13,0,0,0] = expr(1)
Edge[76,14,0,0,0] = expr(1)
Edge[76,15,0,0,0] = expr(1)
Edge[76,16,0,0,0] = expr(1)
Edge[76,17,0,0,0] = expr(1)
Edge[76,18,0,0,0] = expr(1)
Edge[76,19,0,0,0] = expr(1)
Edge[76,20,0,0,0] = expr(1)
Edge[76,21,0,0,0] = expr(1)
Edge[76,22,0,0,0] = expr(1)
Edge[76,23,0,0,0] = expr(1)
Edge[76,24,0,0,0] = expr(1)
Edge[76,25,0,0,0] = expr(1)
Edge[76,26,0,0,0] = expr(1)
Edge[76,27,0,0,0] = expr(1)
Edge[76,28,0,0,0] = expr(1)
Edge[76,29,0,0,0] = expr(1)
Edge[76,30,0,0,0] = expr(1)
Edge[76,31,0,0,0] = expr(1)
Edge[76,32,0,0,0] = expr(1)
Edge[76,33,0,0,0] = expr(1)
Edge[76,34,0,0,0] = expr(1)
Edge[76,35,0,0,0] = expr(1)
Edge_Net[76,0,0,0,0,0:] = exprzeros(6)
Edge_Net[76,1,0,0,0,0:] = exprzeros(6)
Edge_Net[76,2,0,0,0,0:] = exprzeros(6)
Edge_Net[76,3,0,0,0,0:] = exprzeros(6)
Edge_Net[76,4,0,0,0,0:] = exprzeros(6)
Edge_Net[76,5,0,0,0,0:] = exprzeros(6)
Edge_Net[76,6,0,0,0,0:] = exprzeros(6)
Edge_Net[76,7,0,0,0,0:] = exprzeros(6)
Edge_Net[76,8,0,0,0,0:] = exprzeros(6)
Edge_Net[76,9,0,0,0,0:] = exprzeros(6)
Edge_Net[76,10,0,0,0,0:] = exprzeros(6)
Edge_Net[76,11,0,0,0,0:] = exprzeros(6)
Edge_Net[76,12,0,0,0,0:] = exprzeros(6)
Edge_Net[76,13,0,0,0,0:] = exprzeros(6)
Edge_Net[76,14,0,0,0,0:] = exprzeros(6)
Edge_Net[76,15,0,0,0,0:] = exprzeros(6)
Edge_Net[76,16,0,0,0,0:] = exprzeros(6)
Edge_Net[76,17,0,0,0,0:] = exprzeros(6)
Edge_Net[76,18,0,0,0,0:] = exprzeros(6)
Edge_Net[76,19,0,0,0,0:] = exprzeros(6)
Edge_Net[76,20,0,0,0,0:] = exprzeros(6)
Edge_Net[76,21,0,0,0,0:] = exprzeros(6)
Edge_Net[76,22,0,0,0,0:] = exprzeros(6)
Edge_Net[76,23,0,0,0,0:] = exprzeros(6)
Edge_Net[76,24,0,0,0,0:] = exprzeros(6)
Edge_Net[76,25,0,0,0,0:] = exprzeros(6)
Edge_Net[76,26,0,0,0,0:] = exprzeros(6)
Edge_Net[76,27,0,0,0,0:] = exprzeros(6)
Edge_Net[76,28,0,0,0,0:] = exprzeros(6)
Edge_Net[76,29,0,0,0,0:] = exprzeros(6)
Edge_Net[76,30,0,0,0,0:] = exprzeros(6)
Edge_Net[76,31,0,0,0,0:] = exprzeros(6)
Edge_Net[76,32,0,0,0,0:] = exprzeros(6)
Edge_Net[76,33,0,0,0,0:] = exprzeros(6)
Edge_Net[76,34,0,0,0,0:] = exprzeros(6)
Edge_Net[76,35,0,0,0,0:] = exprzeros(6)

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
Edge[2,13,0,0,1] = expr(1)
Edge[2,14,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[2,1,0,0,1,0:] = exprzeros(6)
Edge_Net[2,2,0,0,1,0:] = exprzeros(6)
Edge_Net[2,3,0,0,1,0:] = exprzeros(6)
Edge_Net[2,4,0,0,1,0:] = exprzeros(6)
Edge_Net[2,5,0,0,1,0:] = exprzeros(6)
Edge_Net[2,6,0,0,1,0:] = exprzeros(6)
Edge_Net[2,7,0,0,1,0:] = exprzeros(6)
Edge_Net[2,8,0,0,1,0:] = exprzeros(6)
Edge_Net[2,9,0,0,1,0:] = exprzeros(6)
Edge_Net[2,10,0,0,1,0:] = exprzeros(6)
Edge_Net[2,11,0,0,1,0:] = exprzeros(6)
Edge_Net[2,12,0,0,1,0:] = exprzeros(6)
Edge_Net[2,13,0,0,1,0:] = exprzeros(6)
Edge_Net[2,14,0,0,1,0:] = exprzeros(6)
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
Edge[6,13,0,0,1] = expr(1)
Edge[6,14,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[6,1,0,0,1,0:] = exprzeros(6)
Edge_Net[6,2,0,0,1,0:] = exprzeros(6)
Edge_Net[6,3,0,0,1,0:] = exprzeros(6)
Edge_Net[6,4,0,0,1,0:] = exprzeros(6)
Edge_Net[6,5,0,0,1,0:] = exprzeros(6)
Edge_Net[6,6,0,0,1,0:] = exprzeros(6)
Edge_Net[6,7,0,0,1,0:] = exprzeros(6)
Edge_Net[6,8,0,0,1,0:] = exprzeros(6)
Edge_Net[6,9,0,0,1,0:] = exprzeros(6)
Edge_Net[6,10,0,0,1,0:] = exprzeros(6)
Edge_Net[6,11,0,0,1,0:] = exprzeros(6)
Edge_Net[6,12,0,0,1,0:] = exprzeros(6)
Edge_Net[6,13,0,0,1,0:] = exprzeros(6)
Edge_Net[6,14,0,0,1,0:] = exprzeros(6)
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
Edge[2,14,1,1,1] = expr(0)
Edge[2,15,1,1,1] = expr(0)
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
Edge[2,14,1,1,1] = expr(0)
Edge[2,15,1,1,1] = expr(0)
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
Edge[6,14,1,1,1] = expr(0)
Edge[6,15,1,1,1] = expr(0)
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
Edge[6,14,1,1,1] = expr(0)
Edge[6,15,1,1,1] = expr(0)
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
Edge[6,13,0,0,1] = expr(1)
Edge[6,14,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[6,1,0,0,1,0:] = exprzeros(6)
Edge_Net[6,2,0,0,1,0:] = exprzeros(6)
Edge_Net[6,3,0,0,1,0:] = exprzeros(6)
Edge_Net[6,4,0,0,1,0:] = exprzeros(6)
Edge_Net[6,5,0,0,1,0:] = exprzeros(6)
Edge_Net[6,6,0,0,1,0:] = exprzeros(6)
Edge_Net[6,7,0,0,1,0:] = exprzeros(6)
Edge_Net[6,8,0,0,1,0:] = exprzeros(6)
Edge_Net[6,9,0,0,1,0:] = exprzeros(6)
Edge_Net[6,10,0,0,1,0:] = exprzeros(6)
Edge_Net[6,11,0,0,1,0:] = exprzeros(6)
Edge_Net[6,12,0,0,1,0:] = exprzeros(6)
Edge_Net[6,13,0,0,1,0:] = exprzeros(6)
Edge_Net[6,14,0,0,1,0:] = exprzeros(6)
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
Edge[10,13,0,0,1] = expr(1)
Edge[10,14,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[10,1,0,0,1,0:] = exprzeros(6)
Edge_Net[10,2,0,0,1,0:] = exprzeros(6)
Edge_Net[10,3,0,0,1,0:] = exprzeros(6)
Edge_Net[10,4,0,0,1,0:] = exprzeros(6)
Edge_Net[10,5,0,0,1,0:] = exprzeros(6)
Edge_Net[10,6,0,0,1,0:] = exprzeros(6)
Edge_Net[10,7,0,0,1,0:] = exprzeros(6)
Edge_Net[10,8,0,0,1,0:] = exprzeros(6)
Edge_Net[10,9,0,0,1,0:] = exprzeros(6)
Edge_Net[10,10,0,0,1,0:] = exprzeros(6)
Edge_Net[10,11,0,0,1,0:] = exprzeros(6)
Edge_Net[10,12,0,0,1,0:] = exprzeros(6)
Edge_Net[10,13,0,0,1,0:] = exprzeros(6)
Edge_Net[10,14,0,0,1,0:] = exprzeros(6)
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
Edge[6,14,1,1,1] = expr(0)
Edge[6,15,1,1,1] = expr(0)
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
Edge[6,14,1,1,1] = expr(0)
Edge[6,15,1,1,1] = expr(0)
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
Edge[10,14,1,1,1] = expr(0)
Edge[10,15,1,1,1] = expr(0)
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
Edge[10,14,1,1,1] = expr(0)
Edge[10,15,1,1,1] = expr(0)
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
Edge[10,13,0,0,1] = expr(1)
Edge[10,14,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[10,1,0,0,1,0:] = exprzeros(6)
Edge_Net[10,2,0,0,1,0:] = exprzeros(6)
Edge_Net[10,3,0,0,1,0:] = exprzeros(6)
Edge_Net[10,4,0,0,1,0:] = exprzeros(6)
Edge_Net[10,5,0,0,1,0:] = exprzeros(6)
Edge_Net[10,6,0,0,1,0:] = exprzeros(6)
Edge_Net[10,7,0,0,1,0:] = exprzeros(6)
Edge_Net[10,8,0,0,1,0:] = exprzeros(6)
Edge_Net[10,9,0,0,1,0:] = exprzeros(6)
Edge_Net[10,10,0,0,1,0:] = exprzeros(6)
Edge_Net[10,11,0,0,1,0:] = exprzeros(6)
Edge_Net[10,12,0,0,1,0:] = exprzeros(6)
Edge_Net[10,13,0,0,1,0:] = exprzeros(6)
Edge_Net[10,14,0,0,1,0:] = exprzeros(6)
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
Edge[14,13,0,0,1] = expr(1)
Edge[14,14,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[14,1,0,0,1,0:] = exprzeros(6)
Edge_Net[14,2,0,0,1,0:] = exprzeros(6)
Edge_Net[14,3,0,0,1,0:] = exprzeros(6)
Edge_Net[14,4,0,0,1,0:] = exprzeros(6)
Edge_Net[14,5,0,0,1,0:] = exprzeros(6)
Edge_Net[14,6,0,0,1,0:] = exprzeros(6)
Edge_Net[14,7,0,0,1,0:] = exprzeros(6)
Edge_Net[14,8,0,0,1,0:] = exprzeros(6)
Edge_Net[14,9,0,0,1,0:] = exprzeros(6)
Edge_Net[14,10,0,0,1,0:] = exprzeros(6)
Edge_Net[14,11,0,0,1,0:] = exprzeros(6)
Edge_Net[14,12,0,0,1,0:] = exprzeros(6)
Edge_Net[14,13,0,0,1,0:] = exprzeros(6)
Edge_Net[14,14,0,0,1,0:] = exprzeros(6)
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
Edge[10,14,1,1,1] = expr(0)
Edge[10,15,1,1,1] = expr(0)
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
Edge[10,14,1,1,1] = expr(0)
Edge[10,15,1,1,1] = expr(0)
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
Edge[14,14,1,1,1] = expr(0)
Edge[14,15,1,1,1] = expr(0)
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
Edge[14,14,1,1,1] = expr(0)
Edge[14,15,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
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
Edge[14,13,0,0,1] = expr(1)
Edge[14,14,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[14,1,0,0,1,0:] = exprzeros(6)
Edge_Net[14,2,0,0,1,0:] = exprzeros(6)
Edge_Net[14,3,0,0,1,0:] = exprzeros(6)
Edge_Net[14,4,0,0,1,0:] = exprzeros(6)
Edge_Net[14,5,0,0,1,0:] = exprzeros(6)
Edge_Net[14,6,0,0,1,0:] = exprzeros(6)
Edge_Net[14,7,0,0,1,0:] = exprzeros(6)
Edge_Net[14,8,0,0,1,0:] = exprzeros(6)
Edge_Net[14,9,0,0,1,0:] = exprzeros(6)
Edge_Net[14,10,0,0,1,0:] = exprzeros(6)
Edge_Net[14,11,0,0,1,0:] = exprzeros(6)
Edge_Net[14,12,0,0,1,0:] = exprzeros(6)
Edge_Net[14,13,0,0,1,0:] = exprzeros(6)
Edge_Net[14,14,0,0,1,0:] = exprzeros(6)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[18,1,0,0,1] = expr(1)
Edge[18,2,0,0,1] = expr(1)
Edge[18,3,0,0,1] = expr(1)
Edge[18,4,0,0,1] = expr(1)
Edge[18,5,0,0,1] = expr(1)
Edge[18,6,0,0,1] = expr(1)
Edge[18,7,0,0,1] = expr(1)
Edge[18,8,0,0,1] = expr(1)
Edge[18,9,0,0,1] = expr(1)
Edge[18,10,0,0,1] = expr(1)
Edge[18,11,0,0,1] = expr(1)
Edge[18,12,0,0,1] = expr(1)
Edge[18,13,0,0,1] = expr(1)
Edge[18,14,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[18,1,0,0,1,0:] = exprzeros(6)
Edge_Net[18,2,0,0,1,0:] = exprzeros(6)
Edge_Net[18,3,0,0,1,0:] = exprzeros(6)
Edge_Net[18,4,0,0,1,0:] = exprzeros(6)
Edge_Net[18,5,0,0,1,0:] = exprzeros(6)
Edge_Net[18,6,0,0,1,0:] = exprzeros(6)
Edge_Net[18,7,0,0,1,0:] = exprzeros(6)
Edge_Net[18,8,0,0,1,0:] = exprzeros(6)
Edge_Net[18,9,0,0,1,0:] = exprzeros(6)
Edge_Net[18,10,0,0,1,0:] = exprzeros(6)
Edge_Net[18,11,0,0,1,0:] = exprzeros(6)
Edge_Net[18,12,0,0,1,0:] = exprzeros(6)
Edge_Net[18,13,0,0,1,0:] = exprzeros(6)
Edge_Net[18,14,0,0,1,0:] = exprzeros(6)
#(R)End initialize EdgeNet
#(L)Disable GIL
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
Edge[14,14,1,1,1] = expr(0)
Edge[14,15,1,1,1] = expr(0)
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
Edge[14,14,1,1,1] = expr(0)
Edge[14,15,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[18,0,1,1,1] = expr(0)
Edge[18,1,1,1,1] = expr(0)
Edge[18,2,1,1,1] = expr(0)
Edge[18,3,1,1,1] = expr(0)
Edge[18,4,1,1,1] = expr(0)
Edge[18,5,1,1,1] = expr(0)
Edge[18,6,1,1,1] = expr(0)
Edge[18,7,1,1,1] = expr(0)
Edge[18,8,1,1,1] = expr(0)
Edge[18,9,1,1,1] = expr(0)
Edge[18,10,1,1,1] = expr(0)
Edge[18,11,1,1,1] = expr(0)
Edge[18,12,1,1,1] = expr(0)
Edge[18,13,1,1,1] = expr(0)
Edge[18,14,1,1,1] = expr(0)
Edge[18,15,1,1,1] = expr(0)
Edge[18,0,1,1,1] = expr(0)
Edge[18,1,1,1,1] = expr(0)
Edge[18,2,1,1,1] = expr(0)
Edge[18,3,1,1,1] = expr(0)
Edge[18,4,1,1,1] = expr(0)
Edge[18,5,1,1,1] = expr(0)
Edge[18,6,1,1,1] = expr(0)
Edge[18,7,1,1,1] = expr(0)
Edge[18,8,1,1,1] = expr(0)
Edge[18,9,1,1,1] = expr(0)
Edge[18,10,1,1,1] = expr(0)
Edge[18,11,1,1,1] = expr(0)
Edge[18,12,1,1,1] = expr(0)
Edge[18,13,1,1,1] = expr(0)
Edge[18,14,1,1,1] = expr(0)
Edge[18,15,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[22,1,0,0,1] = expr(1)
Edge[22,2,0,0,1] = expr(1)
Edge[22,3,0,0,1] = expr(1)
Edge[22,4,0,0,1] = expr(1)
Edge[22,5,0,0,1] = expr(1)
Edge[22,6,0,0,1] = expr(1)
Edge[22,7,0,0,1] = expr(1)
Edge[22,8,0,0,1] = expr(1)
Edge[22,9,0,0,1] = expr(1)
Edge[22,10,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[22,1,0,0,1,0:] = exprzeros(6)
Edge_Net[22,2,0,0,1,0:] = exprzeros(6)
Edge_Net[22,3,0,0,1,0:] = exprzeros(6)
Edge_Net[22,4,0,0,1,0:] = exprzeros(6)
Edge_Net[22,5,0,0,1,0:] = exprzeros(6)
Edge_Net[22,6,0,0,1,0:] = exprzeros(6)
Edge_Net[22,7,0,0,1,0:] = exprzeros(6)
Edge_Net[22,8,0,0,1,0:] = exprzeros(6)
Edge_Net[22,9,0,0,1,0:] = exprzeros(6)
Edge_Net[22,10,0,0,1,0:] = exprzeros(6)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[26,1,0,0,1] = expr(1)
Edge[26,2,0,0,1] = expr(1)
Edge[26,3,0,0,1] = expr(1)
Edge[26,4,0,0,1] = expr(1)
Edge[26,5,0,0,1] = expr(1)
Edge[26,6,0,0,1] = expr(1)
Edge[26,7,0,0,1] = expr(1)
Edge[26,8,0,0,1] = expr(1)
Edge[26,9,0,0,1] = expr(1)
Edge[26,10,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[26,1,0,0,1,0:] = exprzeros(6)
Edge_Net[26,2,0,0,1,0:] = exprzeros(6)
Edge_Net[26,3,0,0,1,0:] = exprzeros(6)
Edge_Net[26,4,0,0,1,0:] = exprzeros(6)
Edge_Net[26,5,0,0,1,0:] = exprzeros(6)
Edge_Net[26,6,0,0,1,0:] = exprzeros(6)
Edge_Net[26,7,0,0,1,0:] = exprzeros(6)
Edge_Net[26,8,0,0,1,0:] = exprzeros(6)
Edge_Net[26,9,0,0,1,0:] = exprzeros(6)
Edge_Net[26,10,0,0,1,0:] = exprzeros(6)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[22,0,1,1,1] = expr(0)
Edge[22,1,1,1,1] = expr(0)
Edge[22,2,1,1,1] = expr(0)
Edge[22,3,1,1,1] = expr(0)
Edge[22,4,1,1,1] = expr(0)
Edge[22,5,1,1,1] = expr(0)
Edge[22,6,1,1,1] = expr(0)
Edge[22,7,1,1,1] = expr(0)
Edge[22,8,1,1,1] = expr(0)
Edge[22,9,1,1,1] = expr(0)
Edge[22,10,1,1,1] = expr(0)
Edge[22,11,1,1,1] = expr(0)
Edge[22,0,1,1,1] = expr(0)
Edge[22,1,1,1,1] = expr(0)
Edge[22,2,1,1,1] = expr(0)
Edge[22,3,1,1,1] = expr(0)
Edge[22,4,1,1,1] = expr(0)
Edge[22,5,1,1,1] = expr(0)
Edge[22,6,1,1,1] = expr(0)
Edge[22,7,1,1,1] = expr(0)
Edge[22,8,1,1,1] = expr(0)
Edge[22,9,1,1,1] = expr(0)
Edge[22,10,1,1,1] = expr(0)
Edge[22,11,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[26,0,1,1,1] = expr(0)
Edge[26,1,1,1,1] = expr(0)
Edge[26,2,1,1,1] = expr(0)
Edge[26,3,1,1,1] = expr(0)
Edge[26,4,1,1,1] = expr(0)
Edge[26,5,1,1,1] = expr(0)
Edge[26,6,1,1,1] = expr(0)
Edge[26,7,1,1,1] = expr(0)
Edge[26,8,1,1,1] = expr(0)
Edge[26,9,1,1,1] = expr(0)
Edge[26,10,1,1,1] = expr(0)
Edge[26,11,1,1,1] = expr(0)
Edge[26,0,1,1,1] = expr(0)
Edge[26,1,1,1,1] = expr(0)
Edge[26,2,1,1,1] = expr(0)
Edge[26,3,1,1,1] = expr(0)
Edge[26,4,1,1,1] = expr(0)
Edge[26,5,1,1,1] = expr(0)
Edge[26,6,1,1,1] = expr(0)
Edge[26,7,1,1,1] = expr(0)
Edge[26,8,1,1,1] = expr(0)
Edge[26,9,1,1,1] = expr(0)
Edge[26,10,1,1,1] = expr(0)
Edge[26,11,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[30,1,0,0,1] = expr(1)
Edge[30,2,0,0,1] = expr(1)
Edge[30,3,0,0,1] = expr(1)
Edge[30,4,0,0,1] = expr(1)
Edge[30,5,0,0,1] = expr(1)
Edge[30,6,0,0,1] = expr(1)
Edge[30,7,0,0,1] = expr(1)
Edge[30,8,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[30,1,0,0,1,0:] = exprzeros(6)
Edge_Net[30,2,0,0,1,0:] = exprzeros(6)
Edge_Net[30,3,0,0,1,0:] = exprzeros(6)
Edge_Net[30,4,0,0,1,0:] = exprzeros(6)
Edge_Net[30,5,0,0,1,0:] = exprzeros(6)
Edge_Net[30,6,0,0,1,0:] = exprzeros(6)
Edge_Net[30,7,0,0,1,0:] = exprzeros(6)
Edge_Net[30,8,0,0,1,0:] = exprzeros(6)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[34,1,0,0,1] = expr(1)
Edge[34,2,0,0,1] = expr(1)
Edge[34,3,0,0,1] = expr(1)
Edge[34,4,0,0,1] = expr(1)
Edge[34,5,0,0,1] = expr(1)
Edge[34,6,0,0,1] = expr(1)
Edge[34,7,0,0,1] = expr(1)
Edge[34,8,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[34,1,0,0,1,0:] = exprzeros(6)
Edge_Net[34,2,0,0,1,0:] = exprzeros(6)
Edge_Net[34,3,0,0,1,0:] = exprzeros(6)
Edge_Net[34,4,0,0,1,0:] = exprzeros(6)
Edge_Net[34,5,0,0,1,0:] = exprzeros(6)
Edge_Net[34,6,0,0,1,0:] = exprzeros(6)
Edge_Net[34,7,0,0,1,0:] = exprzeros(6)
Edge_Net[34,8,0,0,1,0:] = exprzeros(6)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[30,0,1,1,1] = expr(0)
Edge[30,1,1,1,1] = expr(0)
Edge[30,2,1,1,1] = expr(0)
Edge[30,3,1,1,1] = expr(0)
Edge[30,4,1,1,1] = expr(0)
Edge[30,5,1,1,1] = expr(0)
Edge[30,6,1,1,1] = expr(0)
Edge[30,7,1,1,1] = expr(0)
Edge[30,8,1,1,1] = expr(0)
Edge[30,9,1,1,1] = expr(0)
Edge[30,0,1,1,1] = expr(0)
Edge[30,1,1,1,1] = expr(0)
Edge[30,2,1,1,1] = expr(0)
Edge[30,3,1,1,1] = expr(0)
Edge[30,4,1,1,1] = expr(0)
Edge[30,5,1,1,1] = expr(0)
Edge[30,6,1,1,1] = expr(0)
Edge[30,7,1,1,1] = expr(0)
Edge[30,8,1,1,1] = expr(0)
Edge[30,9,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[34,0,1,1,1] = expr(0)
Edge[34,1,1,1,1] = expr(0)
Edge[34,2,1,1,1] = expr(0)
Edge[34,3,1,1,1] = expr(0)
Edge[34,4,1,1,1] = expr(0)
Edge[34,5,1,1,1] = expr(0)
Edge[34,6,1,1,1] = expr(0)
Edge[34,7,1,1,1] = expr(0)
Edge[34,8,1,1,1] = expr(0)
Edge[34,9,1,1,1] = expr(0)
Edge[34,0,1,1,1] = expr(0)
Edge[34,1,1,1,1] = expr(0)
Edge[34,2,1,1,1] = expr(0)
Edge[34,3,1,1,1] = expr(0)
Edge[34,4,1,1,1] = expr(0)
Edge[34,5,1,1,1] = expr(0)
Edge[34,6,1,1,1] = expr(0)
Edge[34,7,1,1,1] = expr(0)
Edge[34,8,1,1,1] = expr(0)
Edge[34,9,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[38,1,0,0,1] = expr(1)
Edge[38,2,0,0,1] = expr(1)
Edge[38,3,0,0,1] = expr(1)
Edge[38,4,0,0,1] = expr(1)
Edge[38,5,0,0,1] = expr(1)
Edge[38,6,0,0,1] = expr(1)
Edge[38,7,0,0,1] = expr(1)
Edge[38,8,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[38,1,0,0,1,0:] = exprzeros(6)
Edge_Net[38,2,0,0,1,0:] = exprzeros(6)
Edge_Net[38,3,0,0,1,0:] = exprzeros(6)
Edge_Net[38,4,0,0,1,0:] = exprzeros(6)
Edge_Net[38,5,0,0,1,0:] = exprzeros(6)
Edge_Net[38,6,0,0,1,0:] = exprzeros(6)
Edge_Net[38,7,0,0,1,0:] = exprzeros(6)
Edge_Net[38,8,0,0,1,0:] = exprzeros(6)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[42,1,0,0,1] = expr(1)
Edge[42,2,0,0,1] = expr(1)
Edge[42,3,0,0,1] = expr(1)
Edge[42,4,0,0,1] = expr(1)
Edge[42,5,0,0,1] = expr(1)
Edge[42,6,0,0,1] = expr(1)
Edge[42,7,0,0,1] = expr(1)
Edge[42,8,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[42,1,0,0,1,0:] = exprzeros(6)
Edge_Net[42,2,0,0,1,0:] = exprzeros(6)
Edge_Net[42,3,0,0,1,0:] = exprzeros(6)
Edge_Net[42,4,0,0,1,0:] = exprzeros(6)
Edge_Net[42,5,0,0,1,0:] = exprzeros(6)
Edge_Net[42,6,0,0,1,0:] = exprzeros(6)
Edge_Net[42,7,0,0,1,0:] = exprzeros(6)
Edge_Net[42,8,0,0,1,0:] = exprzeros(6)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[38,0,1,1,1] = expr(0)
Edge[38,1,1,1,1] = expr(0)
Edge[38,2,1,1,1] = expr(0)
Edge[38,3,1,1,1] = expr(0)
Edge[38,4,1,1,1] = expr(0)
Edge[38,5,1,1,1] = expr(0)
Edge[38,6,1,1,1] = expr(0)
Edge[38,7,1,1,1] = expr(0)
Edge[38,8,1,1,1] = expr(0)
Edge[38,9,1,1,1] = expr(0)
Edge[38,0,1,1,1] = expr(0)
Edge[38,1,1,1,1] = expr(0)
Edge[38,2,1,1,1] = expr(0)
Edge[38,3,1,1,1] = expr(0)
Edge[38,4,1,1,1] = expr(0)
Edge[38,5,1,1,1] = expr(0)
Edge[38,6,1,1,1] = expr(0)
Edge[38,7,1,1,1] = expr(0)
Edge[38,8,1,1,1] = expr(0)
Edge[38,9,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[42,0,1,1,1] = expr(0)
Edge[42,1,1,1,1] = expr(0)
Edge[42,2,1,1,1] = expr(0)
Edge[42,3,1,1,1] = expr(0)
Edge[42,4,1,1,1] = expr(0)
Edge[42,5,1,1,1] = expr(0)
Edge[42,6,1,1,1] = expr(0)
Edge[42,7,1,1,1] = expr(0)
Edge[42,8,1,1,1] = expr(0)
Edge[42,9,1,1,1] = expr(0)
Edge[42,0,1,1,1] = expr(0)
Edge[42,1,1,1,1] = expr(0)
Edge[42,2,1,1,1] = expr(0)
Edge[42,3,1,1,1] = expr(0)
Edge[42,4,1,1,1] = expr(0)
Edge[42,5,1,1,1] = expr(0)
Edge[42,6,1,1,1] = expr(0)
Edge[42,7,1,1,1] = expr(0)
Edge[42,8,1,1,1] = expr(0)
Edge[42,9,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[46,1,0,0,1] = expr(1)
Edge[46,2,0,0,1] = expr(1)
Edge[46,3,0,0,1] = expr(1)
Edge[46,4,0,0,1] = expr(1)
Edge[46,5,0,0,1] = expr(1)
Edge[46,6,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[46,1,0,0,1,0:] = exprzeros(6)
Edge_Net[46,2,0,0,1,0:] = exprzeros(6)
Edge_Net[46,3,0,0,1,0:] = exprzeros(6)
Edge_Net[46,4,0,0,1,0:] = exprzeros(6)
Edge_Net[46,5,0,0,1,0:] = exprzeros(6)
Edge_Net[46,6,0,0,1,0:] = exprzeros(6)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[50,1,0,0,1] = expr(1)
Edge[50,2,0,0,1] = expr(1)
Edge[50,3,0,0,1] = expr(1)
Edge[50,4,0,0,1] = expr(1)
Edge[50,5,0,0,1] = expr(1)
Edge[50,6,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[50,1,0,0,1,0:] = exprzeros(6)
Edge_Net[50,2,0,0,1,0:] = exprzeros(6)
Edge_Net[50,3,0,0,1,0:] = exprzeros(6)
Edge_Net[50,4,0,0,1,0:] = exprzeros(6)
Edge_Net[50,5,0,0,1,0:] = exprzeros(6)
Edge_Net[50,6,0,0,1,0:] = exprzeros(6)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[46,0,1,1,1] = expr(0)
Edge[46,1,1,1,1] = expr(0)
Edge[46,2,1,1,1] = expr(0)
Edge[46,3,1,1,1] = expr(0)
Edge[46,4,1,1,1] = expr(0)
Edge[46,5,1,1,1] = expr(0)
Edge[46,6,1,1,1] = expr(0)
Edge[46,7,1,1,1] = expr(0)
Edge[46,0,1,1,1] = expr(0)
Edge[46,1,1,1,1] = expr(0)
Edge[46,2,1,1,1] = expr(0)
Edge[46,3,1,1,1] = expr(0)
Edge[46,4,1,1,1] = expr(0)
Edge[46,5,1,1,1] = expr(0)
Edge[46,6,1,1,1] = expr(0)
Edge[46,7,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[50,0,1,1,1] = expr(0)
Edge[50,1,1,1,1] = expr(0)
Edge[50,2,1,1,1] = expr(0)
Edge[50,3,1,1,1] = expr(0)
Edge[50,4,1,1,1] = expr(0)
Edge[50,5,1,1,1] = expr(0)
Edge[50,6,1,1,1] = expr(0)
Edge[50,7,1,1,1] = expr(0)
Edge[50,0,1,1,1] = expr(0)
Edge[50,1,1,1,1] = expr(0)
Edge[50,2,1,1,1] = expr(0)
Edge[50,3,1,1,1] = expr(0)
Edge[50,4,1,1,1] = expr(0)
Edge[50,5,1,1,1] = expr(0)
Edge[50,6,1,1,1] = expr(0)
Edge[50,7,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[54,1,0,0,1] = expr(1)
Edge[54,2,0,0,1] = expr(1)
Edge[54,3,0,0,1] = expr(1)
Edge[54,4,0,0,1] = expr(1)
Edge[54,5,0,0,1] = expr(1)
Edge[54,6,0,0,1] = expr(1)
Edge[54,7,0,0,1] = expr(1)
Edge[54,8,0,0,1] = expr(1)
Edge[54,9,0,0,1] = expr(1)
Edge[54,10,0,0,1] = expr(1)
Edge[54,11,0,0,1] = expr(1)
Edge[54,12,0,0,1] = expr(1)
Edge[54,13,0,0,1] = expr(1)
Edge[54,14,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[54,1,0,0,1,0:] = exprzeros(6)
Edge_Net[54,2,0,0,1,0:] = exprzeros(6)
Edge_Net[54,3,0,0,1,0:] = exprzeros(6)
Edge_Net[54,4,0,0,1,0:] = exprzeros(6)
Edge_Net[54,5,0,0,1,0:] = exprzeros(6)
Edge_Net[54,6,0,0,1,0:] = exprzeros(6)
Edge_Net[54,7,0,0,1,0:] = exprzeros(6)
Edge_Net[54,8,0,0,1,0:] = exprzeros(6)
Edge_Net[54,9,0,0,1,0:] = exprzeros(6)
Edge_Net[54,10,0,0,1,0:] = exprzeros(6)
Edge_Net[54,11,0,0,1,0:] = exprzeros(6)
Edge_Net[54,12,0,0,1,0:] = exprzeros(6)
Edge_Net[54,13,0,0,1,0:] = exprzeros(6)
Edge_Net[54,14,0,0,1,0:] = exprzeros(6)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[58,1,0,0,1] = expr(1)
Edge[58,2,0,0,1] = expr(1)
Edge[58,3,0,0,1] = expr(1)
Edge[58,4,0,0,1] = expr(1)
Edge[58,5,0,0,1] = expr(1)
Edge[58,6,0,0,1] = expr(1)
Edge[58,7,0,0,1] = expr(1)
Edge[58,8,0,0,1] = expr(1)
Edge[58,9,0,0,1] = expr(1)
Edge[58,10,0,0,1] = expr(1)
Edge[58,11,0,0,1] = expr(1)
Edge[58,12,0,0,1] = expr(1)
Edge[58,13,0,0,1] = expr(1)
Edge[58,14,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[58,1,0,0,1,0:] = exprzeros(6)
Edge_Net[58,2,0,0,1,0:] = exprzeros(6)
Edge_Net[58,3,0,0,1,0:] = exprzeros(6)
Edge_Net[58,4,0,0,1,0:] = exprzeros(6)
Edge_Net[58,5,0,0,1,0:] = exprzeros(6)
Edge_Net[58,6,0,0,1,0:] = exprzeros(6)
Edge_Net[58,7,0,0,1,0:] = exprzeros(6)
Edge_Net[58,8,0,0,1,0:] = exprzeros(6)
Edge_Net[58,9,0,0,1,0:] = exprzeros(6)
Edge_Net[58,10,0,0,1,0:] = exprzeros(6)
Edge_Net[58,11,0,0,1,0:] = exprzeros(6)
Edge_Net[58,12,0,0,1,0:] = exprzeros(6)
Edge_Net[58,13,0,0,1,0:] = exprzeros(6)
Edge_Net[58,14,0,0,1,0:] = exprzeros(6)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[54,0,1,1,1] = expr(0)
Edge[54,1,1,1,1] = expr(0)
Edge[54,2,1,1,1] = expr(0)
Edge[54,3,1,1,1] = expr(0)
Edge[54,4,1,1,1] = expr(0)
Edge[54,5,1,1,1] = expr(0)
Edge[54,6,1,1,1] = expr(0)
Edge[54,7,1,1,1] = expr(0)
Edge[54,8,1,1,1] = expr(0)
Edge[54,9,1,1,1] = expr(0)
Edge[54,10,1,1,1] = expr(0)
Edge[54,11,1,1,1] = expr(0)
Edge[54,12,1,1,1] = expr(0)
Edge[54,13,1,1,1] = expr(0)
Edge[54,14,1,1,1] = expr(0)
Edge[54,15,1,1,1] = expr(0)
Edge[54,0,1,1,1] = expr(0)
Edge[54,1,1,1,1] = expr(0)
Edge[54,2,1,1,1] = expr(0)
Edge[54,3,1,1,1] = expr(0)
Edge[54,4,1,1,1] = expr(0)
Edge[54,5,1,1,1] = expr(0)
Edge[54,6,1,1,1] = expr(0)
Edge[54,7,1,1,1] = expr(0)
Edge[54,8,1,1,1] = expr(0)
Edge[54,9,1,1,1] = expr(0)
Edge[54,10,1,1,1] = expr(0)
Edge[54,11,1,1,1] = expr(0)
Edge[54,12,1,1,1] = expr(0)
Edge[54,13,1,1,1] = expr(0)
Edge[54,14,1,1,1] = expr(0)
Edge[54,15,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[58,0,1,1,1] = expr(0)
Edge[58,1,1,1,1] = expr(0)
Edge[58,2,1,1,1] = expr(0)
Edge[58,3,1,1,1] = expr(0)
Edge[58,4,1,1,1] = expr(0)
Edge[58,5,1,1,1] = expr(0)
Edge[58,6,1,1,1] = expr(0)
Edge[58,7,1,1,1] = expr(0)
Edge[58,8,1,1,1] = expr(0)
Edge[58,9,1,1,1] = expr(0)
Edge[58,10,1,1,1] = expr(0)
Edge[58,11,1,1,1] = expr(0)
Edge[58,12,1,1,1] = expr(0)
Edge[58,13,1,1,1] = expr(0)
Edge[58,14,1,1,1] = expr(0)
Edge[58,15,1,1,1] = expr(0)
Edge[58,0,1,1,1] = expr(0)
Edge[58,1,1,1,1] = expr(0)
Edge[58,2,1,1,1] = expr(0)
Edge[58,3,1,1,1] = expr(0)
Edge[58,4,1,1,1] = expr(0)
Edge[58,5,1,1,1] = expr(0)
Edge[58,6,1,1,1] = expr(0)
Edge[58,7,1,1,1] = expr(0)
Edge[58,8,1,1,1] = expr(0)
Edge[58,9,1,1,1] = expr(0)
Edge[58,10,1,1,1] = expr(0)
Edge[58,11,1,1,1] = expr(0)
Edge[58,12,1,1,1] = expr(0)
Edge[58,13,1,1,1] = expr(0)
Edge[58,14,1,1,1] = expr(0)
Edge[58,15,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[62,1,0,0,1] = expr(1)
Edge[62,2,0,0,1] = expr(1)
Edge[62,3,0,0,1] = expr(1)
Edge[62,4,0,0,1] = expr(1)
Edge[62,5,0,0,1] = expr(1)
Edge[62,6,0,0,1] = expr(1)
Edge[62,7,0,0,1] = expr(1)
Edge[62,8,0,0,1] = expr(1)
Edge[62,9,0,0,1] = expr(1)
Edge[62,10,0,0,1] = expr(1)
Edge[62,11,0,0,1] = expr(1)
Edge[62,12,0,0,1] = expr(1)
Edge[62,13,0,0,1] = expr(1)
Edge[62,14,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[62,1,0,0,1,0:] = exprzeros(6)
Edge_Net[62,2,0,0,1,0:] = exprzeros(6)
Edge_Net[62,3,0,0,1,0:] = exprzeros(6)
Edge_Net[62,4,0,0,1,0:] = exprzeros(6)
Edge_Net[62,5,0,0,1,0:] = exprzeros(6)
Edge_Net[62,6,0,0,1,0:] = exprzeros(6)
Edge_Net[62,7,0,0,1,0:] = exprzeros(6)
Edge_Net[62,8,0,0,1,0:] = exprzeros(6)
Edge_Net[62,9,0,0,1,0:] = exprzeros(6)
Edge_Net[62,10,0,0,1,0:] = exprzeros(6)
Edge_Net[62,11,0,0,1,0:] = exprzeros(6)
Edge_Net[62,12,0,0,1,0:] = exprzeros(6)
Edge_Net[62,13,0,0,1,0:] = exprzeros(6)
Edge_Net[62,14,0,0,1,0:] = exprzeros(6)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[66,1,0,0,1] = expr(1)
Edge[66,2,0,0,1] = expr(1)
Edge[66,3,0,0,1] = expr(1)
Edge[66,4,0,0,1] = expr(1)
Edge[66,5,0,0,1] = expr(1)
Edge[66,6,0,0,1] = expr(1)
Edge[66,7,0,0,1] = expr(1)
Edge[66,8,0,0,1] = expr(1)
Edge[66,9,0,0,1] = expr(1)
Edge[66,10,0,0,1] = expr(1)
Edge[66,11,0,0,1] = expr(1)
Edge[66,12,0,0,1] = expr(1)
Edge[66,13,0,0,1] = expr(1)
Edge[66,14,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[66,1,0,0,1,0:] = exprzeros(6)
Edge_Net[66,2,0,0,1,0:] = exprzeros(6)
Edge_Net[66,3,0,0,1,0:] = exprzeros(6)
Edge_Net[66,4,0,0,1,0:] = exprzeros(6)
Edge_Net[66,5,0,0,1,0:] = exprzeros(6)
Edge_Net[66,6,0,0,1,0:] = exprzeros(6)
Edge_Net[66,7,0,0,1,0:] = exprzeros(6)
Edge_Net[66,8,0,0,1,0:] = exprzeros(6)
Edge_Net[66,9,0,0,1,0:] = exprzeros(6)
Edge_Net[66,10,0,0,1,0:] = exprzeros(6)
Edge_Net[66,11,0,0,1,0:] = exprzeros(6)
Edge_Net[66,12,0,0,1,0:] = exprzeros(6)
Edge_Net[66,13,0,0,1,0:] = exprzeros(6)
Edge_Net[66,14,0,0,1,0:] = exprzeros(6)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[62,0,1,1,1] = expr(0)
Edge[62,1,1,1,1] = expr(0)
Edge[62,2,1,1,1] = expr(0)
Edge[62,3,1,1,1] = expr(0)
Edge[62,4,1,1,1] = expr(0)
Edge[62,5,1,1,1] = expr(0)
Edge[62,6,1,1,1] = expr(0)
Edge[62,7,1,1,1] = expr(0)
Edge[62,8,1,1,1] = expr(0)
Edge[62,9,1,1,1] = expr(0)
Edge[62,10,1,1,1] = expr(0)
Edge[62,11,1,1,1] = expr(0)
Edge[62,12,1,1,1] = expr(0)
Edge[62,13,1,1,1] = expr(0)
Edge[62,14,1,1,1] = expr(0)
Edge[62,15,1,1,1] = expr(0)
Edge[62,0,1,1,1] = expr(0)
Edge[62,1,1,1,1] = expr(0)
Edge[62,2,1,1,1] = expr(0)
Edge[62,3,1,1,1] = expr(0)
Edge[62,4,1,1,1] = expr(0)
Edge[62,5,1,1,1] = expr(0)
Edge[62,6,1,1,1] = expr(0)
Edge[62,7,1,1,1] = expr(0)
Edge[62,8,1,1,1] = expr(0)
Edge[62,9,1,1,1] = expr(0)
Edge[62,10,1,1,1] = expr(0)
Edge[62,11,1,1,1] = expr(0)
Edge[62,12,1,1,1] = expr(0)
Edge[62,13,1,1,1] = expr(0)
Edge[62,14,1,1,1] = expr(0)
Edge[62,15,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[66,0,1,1,1] = expr(0)
Edge[66,1,1,1,1] = expr(0)
Edge[66,2,1,1,1] = expr(0)
Edge[66,3,1,1,1] = expr(0)
Edge[66,4,1,1,1] = expr(0)
Edge[66,5,1,1,1] = expr(0)
Edge[66,6,1,1,1] = expr(0)
Edge[66,7,1,1,1] = expr(0)
Edge[66,8,1,1,1] = expr(0)
Edge[66,9,1,1,1] = expr(0)
Edge[66,10,1,1,1] = expr(0)
Edge[66,11,1,1,1] = expr(0)
Edge[66,12,1,1,1] = expr(0)
Edge[66,13,1,1,1] = expr(0)
Edge[66,14,1,1,1] = expr(0)
Edge[66,15,1,1,1] = expr(0)
Edge[66,0,1,1,1] = expr(0)
Edge[66,1,1,1,1] = expr(0)
Edge[66,2,1,1,1] = expr(0)
Edge[66,3,1,1,1] = expr(0)
Edge[66,4,1,1,1] = expr(0)
Edge[66,5,1,1,1] = expr(0)
Edge[66,6,1,1,1] = expr(0)
Edge[66,7,1,1,1] = expr(0)
Edge[66,8,1,1,1] = expr(0)
Edge[66,9,1,1,1] = expr(0)
Edge[66,10,1,1,1] = expr(0)
Edge[66,11,1,1,1] = expr(0)
Edge[66,12,1,1,1] = expr(0)
Edge[66,13,1,1,1] = expr(0)
Edge[66,14,1,1,1] = expr(0)
Edge[66,15,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[70,1,0,0,1] = expr(1)
Edge[70,2,0,0,1] = expr(1)
Edge[70,3,0,0,1] = expr(1)
Edge[70,4,0,0,1] = expr(1)
Edge[70,5,0,0,1] = expr(1)
Edge[70,6,0,0,1] = expr(1)
Edge[70,7,0,0,1] = expr(1)
Edge[70,8,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[70,1,0,0,1,0:] = exprzeros(6)
Edge_Net[70,2,0,0,1,0:] = exprzeros(6)
Edge_Net[70,3,0,0,1,0:] = exprzeros(6)
Edge_Net[70,4,0,0,1,0:] = exprzeros(6)
Edge_Net[70,5,0,0,1,0:] = exprzeros(6)
Edge_Net[70,6,0,0,1,0:] = exprzeros(6)
Edge_Net[70,7,0,0,1,0:] = exprzeros(6)
Edge_Net[70,8,0,0,1,0:] = exprzeros(6)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[74,1,0,0,1] = expr(1)
Edge[74,2,0,0,1] = expr(1)
Edge[74,3,0,0,1] = expr(1)
Edge[74,4,0,0,1] = expr(1)
Edge[74,5,0,0,1] = expr(1)
Edge[74,6,0,0,1] = expr(1)
Edge[74,7,0,0,1] = expr(1)
Edge[74,8,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[74,1,0,0,1,0:] = exprzeros(6)
Edge_Net[74,2,0,0,1,0:] = exprzeros(6)
Edge_Net[74,3,0,0,1,0:] = exprzeros(6)
Edge_Net[74,4,0,0,1,0:] = exprzeros(6)
Edge_Net[74,5,0,0,1,0:] = exprzeros(6)
Edge_Net[74,6,0,0,1,0:] = exprzeros(6)
Edge_Net[74,7,0,0,1,0:] = exprzeros(6)
Edge_Net[74,8,0,0,1,0:] = exprzeros(6)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[70,0,1,1,1] = expr(0)
Edge[70,1,1,1,1] = expr(0)
Edge[70,2,1,1,1] = expr(0)
Edge[70,3,1,1,1] = expr(0)
Edge[70,4,1,1,1] = expr(0)
Edge[70,5,1,1,1] = expr(0)
Edge[70,6,1,1,1] = expr(0)
Edge[70,7,1,1,1] = expr(0)
Edge[70,8,1,1,1] = expr(0)
Edge[70,9,1,1,1] = expr(0)
Edge[70,0,1,1,1] = expr(0)
Edge[70,1,1,1,1] = expr(0)
Edge[70,2,1,1,1] = expr(0)
Edge[70,3,1,1,1] = expr(0)
Edge[70,4,1,1,1] = expr(0)
Edge[70,5,1,1,1] = expr(0)
Edge[70,6,1,1,1] = expr(0)
Edge[70,7,1,1,1] = expr(0)
Edge[70,8,1,1,1] = expr(0)
Edge[70,9,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[74,0,1,1,1] = expr(0)
Edge[74,1,1,1,1] = expr(0)
Edge[74,2,1,1,1] = expr(0)
Edge[74,3,1,1,1] = expr(0)
Edge[74,4,1,1,1] = expr(0)
Edge[74,5,1,1,1] = expr(0)
Edge[74,6,1,1,1] = expr(0)
Edge[74,7,1,1,1] = expr(0)
Edge[74,8,1,1,1] = expr(0)
Edge[74,9,1,1,1] = expr(0)
Edge[74,0,1,1,1] = expr(0)
Edge[74,1,1,1,1] = expr(0)
Edge[74,2,1,1,1] = expr(0)
Edge[74,3,1,1,1] = expr(0)
Edge[74,4,1,1,1] = expr(0)
Edge[74,5,1,1,1] = expr(0)
Edge[74,6,1,1,1] = expr(0)
Edge[74,7,1,1,1] = expr(0)
Edge[74,8,1,1,1] = expr(0)
Edge[74,9,1,1,1] = expr(0)
#(R)End disable GIL

#Initialize N AIL1
Edge[2,20,0,0,1] = expr(1)
Edge[2,21,0,0,1] = expr(1)
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
Edge_Net[2,20,0,0,1,0:] = exprzeros(6)
Edge_Net[2,21,0,0,1,0:] = exprzeros(6)
Edge_Net[2,22,0,0,1,0:] = exprzeros(6)
Edge_Net[2,23,0,0,1,0:] = exprzeros(6)
Edge_Net[2,24,0,0,1,0:] = exprzeros(6)
Edge_Net[2,25,0,0,1,0:] = exprzeros(6)
Edge_Net[2,26,0,0,1,0:] = exprzeros(6)
Edge_Net[2,27,0,0,1,0:] = exprzeros(6)
Edge_Net[2,28,0,0,1,0:] = exprzeros(6)
Edge_Net[2,29,0,0,1,0:] = exprzeros(6)
Edge_Net[2,30,0,0,1,0:] = exprzeros(6)
Edge_Net[2,31,0,0,1,0:] = exprzeros(6)
Edge_Net[2,32,0,0,1,0:] = exprzeros(6)
Edge_Net[2,33,0,0,1,0:] = exprzeros(6)
Edge[6,20,0,0,1] = expr(1)
Edge[6,21,0,0,1] = expr(1)
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
Edge_Net[6,20,0,0,1,0:] = exprzeros(6)
Edge_Net[6,21,0,0,1,0:] = exprzeros(6)
Edge_Net[6,22,0,0,1,0:] = exprzeros(6)
Edge_Net[6,23,0,0,1,0:] = exprzeros(6)
Edge_Net[6,24,0,0,1,0:] = exprzeros(6)
Edge_Net[6,25,0,0,1,0:] = exprzeros(6)
Edge_Net[6,26,0,0,1,0:] = exprzeros(6)
Edge_Net[6,27,0,0,1,0:] = exprzeros(6)
Edge_Net[6,28,0,0,1,0:] = exprzeros(6)
Edge_Net[6,29,0,0,1,0:] = exprzeros(6)
Edge_Net[6,30,0,0,1,0:] = exprzeros(6)
Edge_Net[6,31,0,0,1,0:] = exprzeros(6)
Edge_Net[6,32,0,0,1,0:] = exprzeros(6)
Edge_Net[6,33,0,0,1,0:] = exprzeros(6)
Edge[2,19,1,1,1] = expr(0)
Edge[2,20,1,1,1] = expr(0)
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
Edge[6,19,1,1,1] = expr(0)
Edge[6,20,1,1,1] = expr(0)
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
Edge[6,20,0,0,1] = expr(1)
Edge[6,21,0,0,1] = expr(1)
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
Edge_Net[6,20,0,0,1,0:] = exprzeros(6)
Edge_Net[6,21,0,0,1,0:] = exprzeros(6)
Edge_Net[6,22,0,0,1,0:] = exprzeros(6)
Edge_Net[6,23,0,0,1,0:] = exprzeros(6)
Edge_Net[6,24,0,0,1,0:] = exprzeros(6)
Edge_Net[6,25,0,0,1,0:] = exprzeros(6)
Edge_Net[6,26,0,0,1,0:] = exprzeros(6)
Edge_Net[6,27,0,0,1,0:] = exprzeros(6)
Edge_Net[6,28,0,0,1,0:] = exprzeros(6)
Edge_Net[6,29,0,0,1,0:] = exprzeros(6)
Edge_Net[6,30,0,0,1,0:] = exprzeros(6)
Edge_Net[6,31,0,0,1,0:] = exprzeros(6)
Edge_Net[6,32,0,0,1,0:] = exprzeros(6)
Edge_Net[6,33,0,0,1,0:] = exprzeros(6)
Edge[10,20,0,0,1] = expr(1)
Edge[10,21,0,0,1] = expr(1)
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
Edge_Net[10,20,0,0,1,0:] = exprzeros(6)
Edge_Net[10,21,0,0,1,0:] = exprzeros(6)
Edge_Net[10,22,0,0,1,0:] = exprzeros(6)
Edge_Net[10,23,0,0,1,0:] = exprzeros(6)
Edge_Net[10,24,0,0,1,0:] = exprzeros(6)
Edge_Net[10,25,0,0,1,0:] = exprzeros(6)
Edge_Net[10,26,0,0,1,0:] = exprzeros(6)
Edge_Net[10,27,0,0,1,0:] = exprzeros(6)
Edge_Net[10,28,0,0,1,0:] = exprzeros(6)
Edge_Net[10,29,0,0,1,0:] = exprzeros(6)
Edge_Net[10,30,0,0,1,0:] = exprzeros(6)
Edge_Net[10,31,0,0,1,0:] = exprzeros(6)
Edge_Net[10,32,0,0,1,0:] = exprzeros(6)
Edge_Net[10,33,0,0,1,0:] = exprzeros(6)
Edge[6,19,1,1,1] = expr(0)
Edge[6,20,1,1,1] = expr(0)
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
Edge[10,19,1,1,1] = expr(0)
Edge[10,20,1,1,1] = expr(0)
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
Edge[10,20,0,0,1] = expr(1)
Edge[10,21,0,0,1] = expr(1)
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
Edge_Net[10,20,0,0,1,0:] = exprzeros(6)
Edge_Net[10,21,0,0,1,0:] = exprzeros(6)
Edge_Net[10,22,0,0,1,0:] = exprzeros(6)
Edge_Net[10,23,0,0,1,0:] = exprzeros(6)
Edge_Net[10,24,0,0,1,0:] = exprzeros(6)
Edge_Net[10,25,0,0,1,0:] = exprzeros(6)
Edge_Net[10,26,0,0,1,0:] = exprzeros(6)
Edge_Net[10,27,0,0,1,0:] = exprzeros(6)
Edge_Net[10,28,0,0,1,0:] = exprzeros(6)
Edge_Net[10,29,0,0,1,0:] = exprzeros(6)
Edge_Net[10,30,0,0,1,0:] = exprzeros(6)
Edge_Net[10,31,0,0,1,0:] = exprzeros(6)
Edge_Net[10,32,0,0,1,0:] = exprzeros(6)
Edge_Net[10,33,0,0,1,0:] = exprzeros(6)
Edge[14,20,0,0,1] = expr(1)
Edge[14,21,0,0,1] = expr(1)
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
Edge_Net[14,20,0,0,1,0:] = exprzeros(6)
Edge_Net[14,21,0,0,1,0:] = exprzeros(6)
Edge_Net[14,22,0,0,1,0:] = exprzeros(6)
Edge_Net[14,23,0,0,1,0:] = exprzeros(6)
Edge_Net[14,24,0,0,1,0:] = exprzeros(6)
Edge_Net[14,25,0,0,1,0:] = exprzeros(6)
Edge_Net[14,26,0,0,1,0:] = exprzeros(6)
Edge_Net[14,27,0,0,1,0:] = exprzeros(6)
Edge_Net[14,28,0,0,1,0:] = exprzeros(6)
Edge_Net[14,29,0,0,1,0:] = exprzeros(6)
Edge_Net[14,30,0,0,1,0:] = exprzeros(6)
Edge_Net[14,31,0,0,1,0:] = exprzeros(6)
Edge_Net[14,32,0,0,1,0:] = exprzeros(6)
Edge_Net[14,33,0,0,1,0:] = exprzeros(6)
Edge[10,19,1,1,1] = expr(0)
Edge[10,20,1,1,1] = expr(0)
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
Edge[14,19,1,1,1] = expr(0)
Edge[14,20,1,1,1] = expr(0)
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
Edge[14,20,0,0,1] = expr(1)
Edge[14,21,0,0,1] = expr(1)
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
Edge_Net[14,20,0,0,1,0:] = exprzeros(6)
Edge_Net[14,21,0,0,1,0:] = exprzeros(6)
Edge_Net[14,22,0,0,1,0:] = exprzeros(6)
Edge_Net[14,23,0,0,1,0:] = exprzeros(6)
Edge_Net[14,24,0,0,1,0:] = exprzeros(6)
Edge_Net[14,25,0,0,1,0:] = exprzeros(6)
Edge_Net[14,26,0,0,1,0:] = exprzeros(6)
Edge_Net[14,27,0,0,1,0:] = exprzeros(6)
Edge_Net[14,28,0,0,1,0:] = exprzeros(6)
Edge_Net[14,29,0,0,1,0:] = exprzeros(6)
Edge_Net[14,30,0,0,1,0:] = exprzeros(6)
Edge_Net[14,31,0,0,1,0:] = exprzeros(6)
Edge_Net[14,32,0,0,1,0:] = exprzeros(6)
Edge_Net[14,33,0,0,1,0:] = exprzeros(6)
Edge[18,20,0,0,1] = expr(1)
Edge[18,21,0,0,1] = expr(1)
Edge[18,22,0,0,1] = expr(1)
Edge[18,23,0,0,1] = expr(1)
Edge[18,24,0,0,1] = expr(1)
Edge[18,25,0,0,1] = expr(1)
Edge[18,26,0,0,1] = expr(1)
Edge[18,27,0,0,1] = expr(1)
Edge[18,28,0,0,1] = expr(1)
Edge[18,29,0,0,1] = expr(1)
Edge[18,30,0,0,1] = expr(1)
Edge[18,31,0,0,1] = expr(1)
Edge[18,32,0,0,1] = expr(1)
Edge[18,33,0,0,1] = expr(1)
Edge_Net[18,20,0,0,1,0:] = exprzeros(6)
Edge_Net[18,21,0,0,1,0:] = exprzeros(6)
Edge_Net[18,22,0,0,1,0:] = exprzeros(6)
Edge_Net[18,23,0,0,1,0:] = exprzeros(6)
Edge_Net[18,24,0,0,1,0:] = exprzeros(6)
Edge_Net[18,25,0,0,1,0:] = exprzeros(6)
Edge_Net[18,26,0,0,1,0:] = exprzeros(6)
Edge_Net[18,27,0,0,1,0:] = exprzeros(6)
Edge_Net[18,28,0,0,1,0:] = exprzeros(6)
Edge_Net[18,29,0,0,1,0:] = exprzeros(6)
Edge_Net[18,30,0,0,1,0:] = exprzeros(6)
Edge_Net[18,31,0,0,1,0:] = exprzeros(6)
Edge_Net[18,32,0,0,1,0:] = exprzeros(6)
Edge_Net[18,33,0,0,1,0:] = exprzeros(6)
Edge[14,19,1,1,1] = expr(0)
Edge[14,20,1,1,1] = expr(0)
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
Edge[18,19,1,1,1] = expr(0)
Edge[18,20,1,1,1] = expr(0)
Edge[18,21,1,1,1] = expr(0)
Edge[18,22,1,1,1] = expr(0)
Edge[18,23,1,1,1] = expr(0)
Edge[18,24,1,1,1] = expr(0)
Edge[18,25,1,1,1] = expr(0)
Edge[18,26,1,1,1] = expr(0)
Edge[18,27,1,1,1] = expr(0)
Edge[18,28,1,1,1] = expr(0)
Edge[18,29,1,1,1] = expr(0)
Edge[18,30,1,1,1] = expr(0)
Edge[18,31,1,1,1] = expr(0)
Edge[18,32,1,1,1] = expr(0)
Edge[18,33,1,1,1] = expr(0)
Edge[18,34,1,1,1] = expr(0)
Edge[18,35,1,1,1] = expr(0)
Edge[22,24,0,0,1] = expr(1)
Edge[22,25,0,0,1] = expr(1)
Edge[22,26,0,0,1] = expr(1)
Edge[22,27,0,0,1] = expr(1)
Edge[22,28,0,0,1] = expr(1)
Edge[22,29,0,0,1] = expr(1)
Edge[22,30,0,0,1] = expr(1)
Edge[22,31,0,0,1] = expr(1)
Edge[22,32,0,0,1] = expr(1)
Edge[22,33,0,0,1] = expr(1)
Edge_Net[22,24,0,0,1,0:] = exprzeros(6)
Edge_Net[22,25,0,0,1,0:] = exprzeros(6)
Edge_Net[22,26,0,0,1,0:] = exprzeros(6)
Edge_Net[22,27,0,0,1,0:] = exprzeros(6)
Edge_Net[22,28,0,0,1,0:] = exprzeros(6)
Edge_Net[22,29,0,0,1,0:] = exprzeros(6)
Edge_Net[22,30,0,0,1,0:] = exprzeros(6)
Edge_Net[22,31,0,0,1,0:] = exprzeros(6)
Edge_Net[22,32,0,0,1,0:] = exprzeros(6)
Edge_Net[22,33,0,0,1,0:] = exprzeros(6)
Edge[26,24,0,0,1] = expr(1)
Edge[26,25,0,0,1] = expr(1)
Edge[26,26,0,0,1] = expr(1)
Edge[26,27,0,0,1] = expr(1)
Edge[26,28,0,0,1] = expr(1)
Edge[26,29,0,0,1] = expr(1)
Edge[26,30,0,0,1] = expr(1)
Edge[26,31,0,0,1] = expr(1)
Edge[26,32,0,0,1] = expr(1)
Edge[26,33,0,0,1] = expr(1)
Edge_Net[26,24,0,0,1,0:] = exprzeros(6)
Edge_Net[26,25,0,0,1,0:] = exprzeros(6)
Edge_Net[26,26,0,0,1,0:] = exprzeros(6)
Edge_Net[26,27,0,0,1,0:] = exprzeros(6)
Edge_Net[26,28,0,0,1,0:] = exprzeros(6)
Edge_Net[26,29,0,0,1,0:] = exprzeros(6)
Edge_Net[26,30,0,0,1,0:] = exprzeros(6)
Edge_Net[26,31,0,0,1,0:] = exprzeros(6)
Edge_Net[26,32,0,0,1,0:] = exprzeros(6)
Edge_Net[26,33,0,0,1,0:] = exprzeros(6)
Edge[22,23,1,1,1] = expr(0)
Edge[22,24,1,1,1] = expr(0)
Edge[22,25,1,1,1] = expr(0)
Edge[22,26,1,1,1] = expr(0)
Edge[22,27,1,1,1] = expr(0)
Edge[22,28,1,1,1] = expr(0)
Edge[22,29,1,1,1] = expr(0)
Edge[22,30,1,1,1] = expr(0)
Edge[22,31,1,1,1] = expr(0)
Edge[22,32,1,1,1] = expr(0)
Edge[22,33,1,1,1] = expr(0)
Edge[22,34,1,1,1] = expr(0)
Edge[22,35,1,1,1] = expr(0)
Edge[26,23,1,1,1] = expr(0)
Edge[26,24,1,1,1] = expr(0)
Edge[26,25,1,1,1] = expr(0)
Edge[26,26,1,1,1] = expr(0)
Edge[26,27,1,1,1] = expr(0)
Edge[26,28,1,1,1] = expr(0)
Edge[26,29,1,1,1] = expr(0)
Edge[26,30,1,1,1] = expr(0)
Edge[26,31,1,1,1] = expr(0)
Edge[26,32,1,1,1] = expr(0)
Edge[26,33,1,1,1] = expr(0)
Edge[26,34,1,1,1] = expr(0)
Edge[26,35,1,1,1] = expr(0)
Edge[30,26,0,0,1] = expr(1)
Edge[30,27,0,0,1] = expr(1)
Edge[30,28,0,0,1] = expr(1)
Edge[30,29,0,0,1] = expr(1)
Edge[30,30,0,0,1] = expr(1)
Edge[30,31,0,0,1] = expr(1)
Edge[30,32,0,0,1] = expr(1)
Edge[30,33,0,0,1] = expr(1)
Edge_Net[30,26,0,0,1,0:] = exprzeros(6)
Edge_Net[30,27,0,0,1,0:] = exprzeros(6)
Edge_Net[30,28,0,0,1,0:] = exprzeros(6)
Edge_Net[30,29,0,0,1,0:] = exprzeros(6)
Edge_Net[30,30,0,0,1,0:] = exprzeros(6)
Edge_Net[30,31,0,0,1,0:] = exprzeros(6)
Edge_Net[30,32,0,0,1,0:] = exprzeros(6)
Edge_Net[30,33,0,0,1,0:] = exprzeros(6)
Edge[34,26,0,0,1] = expr(1)
Edge[34,27,0,0,1] = expr(1)
Edge[34,28,0,0,1] = expr(1)
Edge[34,29,0,0,1] = expr(1)
Edge[34,30,0,0,1] = expr(1)
Edge[34,31,0,0,1] = expr(1)
Edge[34,32,0,0,1] = expr(1)
Edge[34,33,0,0,1] = expr(1)
Edge_Net[34,26,0,0,1,0:] = exprzeros(6)
Edge_Net[34,27,0,0,1,0:] = exprzeros(6)
Edge_Net[34,28,0,0,1,0:] = exprzeros(6)
Edge_Net[34,29,0,0,1,0:] = exprzeros(6)
Edge_Net[34,30,0,0,1,0:] = exprzeros(6)
Edge_Net[34,31,0,0,1,0:] = exprzeros(6)
Edge_Net[34,32,0,0,1,0:] = exprzeros(6)
Edge_Net[34,33,0,0,1,0:] = exprzeros(6)
Edge[30,25,1,1,1] = expr(0)
Edge[30,26,1,1,1] = expr(0)
Edge[30,27,1,1,1] = expr(0)
Edge[30,28,1,1,1] = expr(0)
Edge[30,29,1,1,1] = expr(0)
Edge[30,30,1,1,1] = expr(0)
Edge[30,31,1,1,1] = expr(0)
Edge[30,32,1,1,1] = expr(0)
Edge[30,33,1,1,1] = expr(0)
Edge[30,34,1,1,1] = expr(0)
Edge[30,35,1,1,1] = expr(0)
Edge[34,25,1,1,1] = expr(0)
Edge[34,26,1,1,1] = expr(0)
Edge[34,27,1,1,1] = expr(0)
Edge[34,28,1,1,1] = expr(0)
Edge[34,29,1,1,1] = expr(0)
Edge[34,30,1,1,1] = expr(0)
Edge[34,31,1,1,1] = expr(0)
Edge[34,32,1,1,1] = expr(0)
Edge[34,33,1,1,1] = expr(0)
Edge[34,34,1,1,1] = expr(0)
Edge[34,35,1,1,1] = expr(0)
Edge[38,26,0,0,1] = expr(1)
Edge[38,27,0,0,1] = expr(1)
Edge[38,28,0,0,1] = expr(1)
Edge[38,29,0,0,1] = expr(1)
Edge[38,30,0,0,1] = expr(1)
Edge[38,31,0,0,1] = expr(1)
Edge[38,32,0,0,1] = expr(1)
Edge[38,33,0,0,1] = expr(1)
Edge_Net[38,26,0,0,1,0:] = exprzeros(6)
Edge_Net[38,27,0,0,1,0:] = exprzeros(6)
Edge_Net[38,28,0,0,1,0:] = exprzeros(6)
Edge_Net[38,29,0,0,1,0:] = exprzeros(6)
Edge_Net[38,30,0,0,1,0:] = exprzeros(6)
Edge_Net[38,31,0,0,1,0:] = exprzeros(6)
Edge_Net[38,32,0,0,1,0:] = exprzeros(6)
Edge_Net[38,33,0,0,1,0:] = exprzeros(6)
Edge[42,26,0,0,1] = expr(1)
Edge[42,27,0,0,1] = expr(1)
Edge[42,28,0,0,1] = expr(1)
Edge[42,29,0,0,1] = expr(1)
Edge[42,30,0,0,1] = expr(1)
Edge[42,31,0,0,1] = expr(1)
Edge[42,32,0,0,1] = expr(1)
Edge[42,33,0,0,1] = expr(1)
Edge_Net[42,26,0,0,1,0:] = exprzeros(6)
Edge_Net[42,27,0,0,1,0:] = exprzeros(6)
Edge_Net[42,28,0,0,1,0:] = exprzeros(6)
Edge_Net[42,29,0,0,1,0:] = exprzeros(6)
Edge_Net[42,30,0,0,1,0:] = exprzeros(6)
Edge_Net[42,31,0,0,1,0:] = exprzeros(6)
Edge_Net[42,32,0,0,1,0:] = exprzeros(6)
Edge_Net[42,33,0,0,1,0:] = exprzeros(6)
Edge[38,25,1,1,1] = expr(0)
Edge[38,26,1,1,1] = expr(0)
Edge[38,27,1,1,1] = expr(0)
Edge[38,28,1,1,1] = expr(0)
Edge[38,29,1,1,1] = expr(0)
Edge[38,30,1,1,1] = expr(0)
Edge[38,31,1,1,1] = expr(0)
Edge[38,32,1,1,1] = expr(0)
Edge[38,33,1,1,1] = expr(0)
Edge[38,34,1,1,1] = expr(0)
Edge[38,35,1,1,1] = expr(0)
Edge[42,25,1,1,1] = expr(0)
Edge[42,26,1,1,1] = expr(0)
Edge[42,27,1,1,1] = expr(0)
Edge[42,28,1,1,1] = expr(0)
Edge[42,29,1,1,1] = expr(0)
Edge[42,30,1,1,1] = expr(0)
Edge[42,31,1,1,1] = expr(0)
Edge[42,32,1,1,1] = expr(0)
Edge[42,33,1,1,1] = expr(0)
Edge[42,34,1,1,1] = expr(0)
Edge[42,35,1,1,1] = expr(0)
Edge[46,20,0,0,1] = expr(1)
Edge[46,21,0,0,1] = expr(1)
Edge[46,22,0,0,1] = expr(1)
Edge[46,23,0,0,1] = expr(1)
Edge[46,24,0,0,1] = expr(1)
Edge[46,25,0,0,1] = expr(1)
Edge[46,26,0,0,1] = expr(1)
Edge[46,27,0,0,1] = expr(1)
Edge[46,28,0,0,1] = expr(1)
Edge[46,29,0,0,1] = expr(1)
Edge[46,30,0,0,1] = expr(1)
Edge[46,31,0,0,1] = expr(1)
Edge[46,32,0,0,1] = expr(1)
Edge[46,33,0,0,1] = expr(1)
Edge_Net[46,20,0,0,1,0:] = exprzeros(6)
Edge_Net[46,21,0,0,1,0:] = exprzeros(6)
Edge_Net[46,22,0,0,1,0:] = exprzeros(6)
Edge_Net[46,23,0,0,1,0:] = exprzeros(6)
Edge_Net[46,24,0,0,1,0:] = exprzeros(6)
Edge_Net[46,25,0,0,1,0:] = exprzeros(6)
Edge_Net[46,26,0,0,1,0:] = exprzeros(6)
Edge_Net[46,27,0,0,1,0:] = exprzeros(6)
Edge_Net[46,28,0,0,1,0:] = exprzeros(6)
Edge_Net[46,29,0,0,1,0:] = exprzeros(6)
Edge_Net[46,30,0,0,1,0:] = exprzeros(6)
Edge_Net[46,31,0,0,1,0:] = exprzeros(6)
Edge_Net[46,32,0,0,1,0:] = exprzeros(6)
Edge_Net[46,33,0,0,1,0:] = exprzeros(6)
Edge[50,20,0,0,1] = expr(1)
Edge[50,21,0,0,1] = expr(1)
Edge[50,22,0,0,1] = expr(1)
Edge[50,23,0,0,1] = expr(1)
Edge[50,24,0,0,1] = expr(1)
Edge[50,25,0,0,1] = expr(1)
Edge[50,26,0,0,1] = expr(1)
Edge[50,27,0,0,1] = expr(1)
Edge[50,28,0,0,1] = expr(1)
Edge[50,29,0,0,1] = expr(1)
Edge[50,30,0,0,1] = expr(1)
Edge[50,31,0,0,1] = expr(1)
Edge[50,32,0,0,1] = expr(1)
Edge[50,33,0,0,1] = expr(1)
Edge_Net[50,20,0,0,1,0:] = exprzeros(6)
Edge_Net[50,21,0,0,1,0:] = exprzeros(6)
Edge_Net[50,22,0,0,1,0:] = exprzeros(6)
Edge_Net[50,23,0,0,1,0:] = exprzeros(6)
Edge_Net[50,24,0,0,1,0:] = exprzeros(6)
Edge_Net[50,25,0,0,1,0:] = exprzeros(6)
Edge_Net[50,26,0,0,1,0:] = exprzeros(6)
Edge_Net[50,27,0,0,1,0:] = exprzeros(6)
Edge_Net[50,28,0,0,1,0:] = exprzeros(6)
Edge_Net[50,29,0,0,1,0:] = exprzeros(6)
Edge_Net[50,30,0,0,1,0:] = exprzeros(6)
Edge_Net[50,31,0,0,1,0:] = exprzeros(6)
Edge_Net[50,32,0,0,1,0:] = exprzeros(6)
Edge_Net[50,33,0,0,1,0:] = exprzeros(6)
Edge[46,19,1,1,1] = expr(0)
Edge[46,20,1,1,1] = expr(0)
Edge[46,21,1,1,1] = expr(0)
Edge[46,22,1,1,1] = expr(0)
Edge[46,23,1,1,1] = expr(0)
Edge[46,24,1,1,1] = expr(0)
Edge[46,25,1,1,1] = expr(0)
Edge[46,26,1,1,1] = expr(0)
Edge[46,27,1,1,1] = expr(0)
Edge[46,28,1,1,1] = expr(0)
Edge[46,29,1,1,1] = expr(0)
Edge[46,30,1,1,1] = expr(0)
Edge[46,31,1,1,1] = expr(0)
Edge[46,32,1,1,1] = expr(0)
Edge[46,33,1,1,1] = expr(0)
Edge[46,34,1,1,1] = expr(0)
Edge[46,35,1,1,1] = expr(0)
Edge[50,19,1,1,1] = expr(0)
Edge[50,20,1,1,1] = expr(0)
Edge[50,21,1,1,1] = expr(0)
Edge[50,22,1,1,1] = expr(0)
Edge[50,23,1,1,1] = expr(0)
Edge[50,24,1,1,1] = expr(0)
Edge[50,25,1,1,1] = expr(0)
Edge[50,26,1,1,1] = expr(0)
Edge[50,27,1,1,1] = expr(0)
Edge[50,28,1,1,1] = expr(0)
Edge[50,29,1,1,1] = expr(0)
Edge[50,30,1,1,1] = expr(0)
Edge[50,31,1,1,1] = expr(0)
Edge[50,32,1,1,1] = expr(0)
Edge[50,33,1,1,1] = expr(0)
Edge[50,34,1,1,1] = expr(0)
Edge[50,35,1,1,1] = expr(0)
Edge[54,20,0,0,1] = expr(1)
Edge[54,21,0,0,1] = expr(1)
Edge[54,22,0,0,1] = expr(1)
Edge[54,23,0,0,1] = expr(1)
Edge[54,24,0,0,1] = expr(1)
Edge[54,25,0,0,1] = expr(1)
Edge[54,26,0,0,1] = expr(1)
Edge[54,27,0,0,1] = expr(1)
Edge[54,28,0,0,1] = expr(1)
Edge[54,29,0,0,1] = expr(1)
Edge[54,30,0,0,1] = expr(1)
Edge[54,31,0,0,1] = expr(1)
Edge[54,32,0,0,1] = expr(1)
Edge[54,33,0,0,1] = expr(1)
Edge_Net[54,20,0,0,1,0:] = exprzeros(6)
Edge_Net[54,21,0,0,1,0:] = exprzeros(6)
Edge_Net[54,22,0,0,1,0:] = exprzeros(6)
Edge_Net[54,23,0,0,1,0:] = exprzeros(6)
Edge_Net[54,24,0,0,1,0:] = exprzeros(6)
Edge_Net[54,25,0,0,1,0:] = exprzeros(6)
Edge_Net[54,26,0,0,1,0:] = exprzeros(6)
Edge_Net[54,27,0,0,1,0:] = exprzeros(6)
Edge_Net[54,28,0,0,1,0:] = exprzeros(6)
Edge_Net[54,29,0,0,1,0:] = exprzeros(6)
Edge_Net[54,30,0,0,1,0:] = exprzeros(6)
Edge_Net[54,31,0,0,1,0:] = exprzeros(6)
Edge_Net[54,32,0,0,1,0:] = exprzeros(6)
Edge_Net[54,33,0,0,1,0:] = exprzeros(6)
Edge[58,20,0,0,1] = expr(1)
Edge[58,21,0,0,1] = expr(1)
Edge[58,22,0,0,1] = expr(1)
Edge[58,23,0,0,1] = expr(1)
Edge[58,24,0,0,1] = expr(1)
Edge[58,25,0,0,1] = expr(1)
Edge[58,26,0,0,1] = expr(1)
Edge[58,27,0,0,1] = expr(1)
Edge[58,28,0,0,1] = expr(1)
Edge[58,29,0,0,1] = expr(1)
Edge[58,30,0,0,1] = expr(1)
Edge[58,31,0,0,1] = expr(1)
Edge[58,32,0,0,1] = expr(1)
Edge[58,33,0,0,1] = expr(1)
Edge_Net[58,20,0,0,1,0:] = exprzeros(6)
Edge_Net[58,21,0,0,1,0:] = exprzeros(6)
Edge_Net[58,22,0,0,1,0:] = exprzeros(6)
Edge_Net[58,23,0,0,1,0:] = exprzeros(6)
Edge_Net[58,24,0,0,1,0:] = exprzeros(6)
Edge_Net[58,25,0,0,1,0:] = exprzeros(6)
Edge_Net[58,26,0,0,1,0:] = exprzeros(6)
Edge_Net[58,27,0,0,1,0:] = exprzeros(6)
Edge_Net[58,28,0,0,1,0:] = exprzeros(6)
Edge_Net[58,29,0,0,1,0:] = exprzeros(6)
Edge_Net[58,30,0,0,1,0:] = exprzeros(6)
Edge_Net[58,31,0,0,1,0:] = exprzeros(6)
Edge_Net[58,32,0,0,1,0:] = exprzeros(6)
Edge_Net[58,33,0,0,1,0:] = exprzeros(6)
Edge[54,19,1,1,1] = expr(0)
Edge[54,20,1,1,1] = expr(0)
Edge[54,21,1,1,1] = expr(0)
Edge[54,22,1,1,1] = expr(0)
Edge[54,23,1,1,1] = expr(0)
Edge[54,24,1,1,1] = expr(0)
Edge[54,25,1,1,1] = expr(0)
Edge[54,26,1,1,1] = expr(0)
Edge[54,27,1,1,1] = expr(0)
Edge[54,28,1,1,1] = expr(0)
Edge[54,29,1,1,1] = expr(0)
Edge[54,30,1,1,1] = expr(0)
Edge[54,31,1,1,1] = expr(0)
Edge[54,32,1,1,1] = expr(0)
Edge[54,33,1,1,1] = expr(0)
Edge[54,34,1,1,1] = expr(0)
Edge[54,35,1,1,1] = expr(0)
Edge[58,19,1,1,1] = expr(0)
Edge[58,20,1,1,1] = expr(0)
Edge[58,21,1,1,1] = expr(0)
Edge[58,22,1,1,1] = expr(0)
Edge[58,23,1,1,1] = expr(0)
Edge[58,24,1,1,1] = expr(0)
Edge[58,25,1,1,1] = expr(0)
Edge[58,26,1,1,1] = expr(0)
Edge[58,27,1,1,1] = expr(0)
Edge[58,28,1,1,1] = expr(0)
Edge[58,29,1,1,1] = expr(0)
Edge[58,30,1,1,1] = expr(0)
Edge[58,31,1,1,1] = expr(0)
Edge[58,32,1,1,1] = expr(0)
Edge[58,33,1,1,1] = expr(0)
Edge[58,34,1,1,1] = expr(0)
Edge[58,35,1,1,1] = expr(0)
Edge[62,28,0,0,1] = expr(1)
Edge[62,29,0,0,1] = expr(1)
Edge[62,30,0,0,1] = expr(1)
Edge[62,31,0,0,1] = expr(1)
Edge[62,32,0,0,1] = expr(1)
Edge[62,33,0,0,1] = expr(1)
Edge_Net[62,28,0,0,1,0:] = exprzeros(6)
Edge_Net[62,29,0,0,1,0:] = exprzeros(6)
Edge_Net[62,30,0,0,1,0:] = exprzeros(6)
Edge_Net[62,31,0,0,1,0:] = exprzeros(6)
Edge_Net[62,32,0,0,1,0:] = exprzeros(6)
Edge_Net[62,33,0,0,1,0:] = exprzeros(6)
Edge[66,28,0,0,1] = expr(1)
Edge[66,29,0,0,1] = expr(1)
Edge[66,30,0,0,1] = expr(1)
Edge[66,31,0,0,1] = expr(1)
Edge[66,32,0,0,1] = expr(1)
Edge[66,33,0,0,1] = expr(1)
Edge_Net[66,28,0,0,1,0:] = exprzeros(6)
Edge_Net[66,29,0,0,1,0:] = exprzeros(6)
Edge_Net[66,30,0,0,1,0:] = exprzeros(6)
Edge_Net[66,31,0,0,1,0:] = exprzeros(6)
Edge_Net[66,32,0,0,1,0:] = exprzeros(6)
Edge_Net[66,33,0,0,1,0:] = exprzeros(6)
Edge[62,27,1,1,1] = expr(0)
Edge[62,28,1,1,1] = expr(0)
Edge[62,29,1,1,1] = expr(0)
Edge[62,30,1,1,1] = expr(0)
Edge[62,31,1,1,1] = expr(0)
Edge[62,32,1,1,1] = expr(0)
Edge[62,33,1,1,1] = expr(0)
Edge[62,34,1,1,1] = expr(0)
Edge[62,35,1,1,1] = expr(0)
Edge[66,27,1,1,1] = expr(0)
Edge[66,28,1,1,1] = expr(0)
Edge[66,29,1,1,1] = expr(0)
Edge[66,30,1,1,1] = expr(0)
Edge[66,31,1,1,1] = expr(0)
Edge[66,32,1,1,1] = expr(0)
Edge[66,33,1,1,1] = expr(0)
Edge[66,34,1,1,1] = expr(0)
Edge[66,35,1,1,1] = expr(0)
Edge[70,26,0,0,1] = expr(1)
Edge[70,27,0,0,1] = expr(1)
Edge[70,28,0,0,1] = expr(1)
Edge[70,29,0,0,1] = expr(1)
Edge[70,30,0,0,1] = expr(1)
Edge[70,31,0,0,1] = expr(1)
Edge[70,32,0,0,1] = expr(1)
Edge[70,33,0,0,1] = expr(1)
Edge_Net[70,26,0,0,1,0:] = exprzeros(6)
Edge_Net[70,27,0,0,1,0:] = exprzeros(6)
Edge_Net[70,28,0,0,1,0:] = exprzeros(6)
Edge_Net[70,29,0,0,1,0:] = exprzeros(6)
Edge_Net[70,30,0,0,1,0:] = exprzeros(6)
Edge_Net[70,31,0,0,1,0:] = exprzeros(6)
Edge_Net[70,32,0,0,1,0:] = exprzeros(6)
Edge_Net[70,33,0,0,1,0:] = exprzeros(6)
Edge[74,26,0,0,1] = expr(1)
Edge[74,27,0,0,1] = expr(1)
Edge[74,28,0,0,1] = expr(1)
Edge[74,29,0,0,1] = expr(1)
Edge[74,30,0,0,1] = expr(1)
Edge[74,31,0,0,1] = expr(1)
Edge[74,32,0,0,1] = expr(1)
Edge[74,33,0,0,1] = expr(1)
Edge_Net[74,26,0,0,1,0:] = exprzeros(6)
Edge_Net[74,27,0,0,1,0:] = exprzeros(6)
Edge_Net[74,28,0,0,1,0:] = exprzeros(6)
Edge_Net[74,29,0,0,1,0:] = exprzeros(6)
Edge_Net[74,30,0,0,1,0:] = exprzeros(6)
Edge_Net[74,31,0,0,1,0:] = exprzeros(6)
Edge_Net[74,32,0,0,1,0:] = exprzeros(6)
Edge_Net[74,33,0,0,1,0:] = exprzeros(6)
Edge[70,25,1,1,1] = expr(0)
Edge[70,26,1,1,1] = expr(0)
Edge[70,27,1,1,1] = expr(0)
Edge[70,28,1,1,1] = expr(0)
Edge[70,29,1,1,1] = expr(0)
Edge[70,30,1,1,1] = expr(0)
Edge[70,31,1,1,1] = expr(0)
Edge[70,32,1,1,1] = expr(0)
Edge[70,33,1,1,1] = expr(0)
Edge[70,34,1,1,1] = expr(0)
Edge[70,35,1,1,1] = expr(0)
Edge[74,25,1,1,1] = expr(0)
Edge[74,26,1,1,1] = expr(0)
Edge[74,27,1,1,1] = expr(0)
Edge[74,28,1,1,1] = expr(0)
Edge[74,29,1,1,1] = expr(0)
Edge[74,30,1,1,1] = expr(0)
Edge[74,31,1,1,1] = expr(0)
Edge[74,32,1,1,1] = expr(0)
Edge[74,33,1,1,1] = expr(0)
Edge[74,34,1,1,1] = expr(0)
Edge[74,35,1,1,1] = expr(0)

# Net-1 subNet-0 Terminal[0] to Terminal[4]
# AIL1(2,2,1,14) ==> AIL1(2,2,20,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet1[2,1:15,0,0,1,0] = exprones(14)
Edge_Net_Subnet1[2,1:15,0,0,2,0] = exprones(14)
Edge_Net[2,1:15,0,0,1,0] = exprones(14)
for x in range(2,2+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 1
Edge_Net_Subnet1[2,20:34,0,0,1,0] = exprones(14)
Edge_Net_Subnet1[2,20:34,0,0,2,0] = exprones(14)
Edge_Net[2,20:34,0,0,1,0] = exprones(14)
for x in range(2,2+1):
  for y in range(20,33+1) :
    outLayout[x][y][0][0] = 1
# Net-1 subNet-1 Terminal[0] to Terminal[1]
# AIL1(2,2,1,14) ==> AIL1(10,10,1,14)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet1[2,1:15,0,0,1,1] = exprones(14)
Edge_Net_Subnet1[2,1:15,0,0,2,1] = exprones(14)
Edge_Net[2,1:15,0,0,1,0] = exprones(14)
for x in range(2,2+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 1
Edge_Net_Subnet1[10,1:15,0,0,1,1] = exprones(14)
Edge_Net_Subnet1[10,1:15,0,0,2,1] = exprones(14)
Edge_Net[10,1:15,0,0,1,0] = exprones(14)
for x in range(10,10+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 1
# Net-1 subNet-2 Terminal[1] to Terminal[5]
# AIL1(10,10,1,14) ==> AIL1(10,10,20,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet1[10,1:15,0,0,1,2] = exprones(14)
Edge_Net_Subnet1[10,1:15,0,0,2,2] = exprones(14)
Edge_Net[10,1:15,0,0,1,0] = exprones(14)
for x in range(10,10+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 1
Edge_Net_Subnet1[10,20:34,0,0,1,2] = exprones(14)
Edge_Net_Subnet1[10,20:34,0,0,2,2] = exprones(14)
Edge_Net[10,20:34,0,0,1,0] = exprones(14)
for x in range(10,10+1):
  for y in range(20,33+1) :
    outLayout[x][y][0][0] = 1
# Net-1 subNet-3 Terminal[1] to Terminal[2]
# AIL1(10,10,1,14) ==> AIL1(18,18,1,14)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet1[10,1:15,0,0,1,3] = exprones(14)
Edge_Net_Subnet1[10,1:15,0,0,2,3] = exprones(14)
Edge_Net[10,1:15,0,0,1,0] = exprones(14)
for x in range(10,10+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 1
Edge_Net_Subnet1[18,1:15,0,0,1,3] = exprones(14)
Edge_Net_Subnet1[18,1:15,0,0,2,3] = exprones(14)
Edge_Net[18,1:15,0,0,1,0] = exprones(14)
for x in range(18,18+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 1
# Net-1 subNet-4 Terminal[2] to Terminal[6]
# AIL1(18,18,1,14) ==> AIL1(18,18,20,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet1[18,1:15,0,0,1,4] = exprones(14)
Edge_Net_Subnet1[18,1:15,0,0,2,4] = exprones(14)
Edge_Net[18,1:15,0,0,1,0] = exprones(14)
for x in range(18,18+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 1
Edge_Net_Subnet1[18,20:34,0,0,1,4] = exprones(14)
Edge_Net_Subnet1[18,20:34,0,0,2,4] = exprones(14)
Edge_Net[18,20:34,0,0,1,0] = exprones(14)
for x in range(18,18+1):
  for y in range(20,33+1) :
    outLayout[x][y][0][0] = 1
# Net-1 subNet-5 Terminal[2] to Terminal[3]
# AIL1(18,18,1,14) ==> AIL1(22,22,1,10)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet1[18,1:15,0,0,1,5] = exprones(14)
Edge_Net_Subnet1[18,1:15,0,0,2,5] = exprones(14)
Edge_Net[18,1:15,0,0,1,0] = exprones(14)
for x in range(18,18+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 1
Edge_Net_Subnet1[22,1:11,0,0,1,5] = exprones(10)
Edge_Net_Subnet1[22,1:11,0,0,2,5] = exprones(10)
Edge_Net[22,1:11,0,0,1,0] = exprones(10)
for x in range(22,22+1):
  for y in range(1,10+1) :
    outLayout[x][y][0][0] = 1
# Net-1 subNet-6 Terminal[3] to Terminal[7]
# AIL1(22,22,1,10) ==> AIL1(22,22,24,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet1[22,1:11,0,0,1,6] = exprones(10)
Edge_Net_Subnet1[22,1:11,0,0,2,6] = exprones(10)
Edge_Net[22,1:11,0,0,1,0] = exprones(10)
for x in range(22,22+1):
  for y in range(1,10+1) :
    outLayout[x][y][0][0] = 1
Edge_Net_Subnet1[22,24:34,0,0,1,6] = exprones(10)
Edge_Net_Subnet1[22,24:34,0,0,2,6] = exprones(10)
Edge_Net[22,24:34,0,0,1,0] = exprones(10)
for x in range(22,22+1):
  for y in range(24,33+1) :
    outLayout[x][y][0][0] = 1
# Net-2 subNet-0 Terminal[0] to Terminal[1]
# Poly(4,4,0,35) ==> Poly(8,8,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[4,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet2[4,0:36,0,0,2,0] = exprones(36)
Edge_Net[4,0:36,0,0,0,1] = exprones(36)
for x in range(4,4+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[8,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet2[8,0:36,0,0,2,0] = exprones(36)
Edge_Net[8,0:36,0,0,0,1] = exprones(36)
for x in range(8,8+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-1 Terminal[1] to Terminal[2]
# Poly(8,8,0,35) ==> Poly(12,12,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[8,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet2[8,0:36,0,0,2,1] = exprones(36)
Edge_Net[8,0:36,0,0,0,1] = exprones(36)
for x in range(8,8+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[12,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet2[12,0:36,0,0,2,1] = exprones(36)
Edge_Net[12,0:36,0,0,0,1] = exprones(36)
for x in range(12,12+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-2 Terminal[2] to Terminal[3]
# Poly(12,12,0,35) ==> Poly(16,16,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[12,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet2[12,0:36,0,0,2,2] = exprones(36)
Edge_Net[12,0:36,0,0,0,1] = exprones(36)
for x in range(12,12+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[16,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet2[16,0:36,0,0,2,2] = exprones(36)
Edge_Net[16,0:36,0,0,0,1] = exprones(36)
for x in range(16,16+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-3 Terminal[2] to Terminal[0]
# Poly(12,12,0,35) ==> Poly(4,4,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[12,0:36,0,0,0,3] = exprones(36)
Edge_Net_Subnet2[12,0:36,0,0,2,3] = exprones(36)
Edge_Net[12,0:36,0,0,0,1] = exprones(36)
for x in range(12,12+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[4,0:36,0,0,0,3] = exprones(36)
Edge_Net_Subnet2[4,0:36,0,0,2,3] = exprones(36)
Edge_Net[4,0:36,0,0,0,1] = exprones(36)
for x in range(4,4+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-4 Terminal[3] to Terminal[4]
# Poly(16,16,0,35) ==> Poly(24,24,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[16,0:36,0,0,0,4] = exprones(36)
Edge_Net_Subnet2[16,0:36,0,0,2,4] = exprones(36)
Edge_Net[16,0:36,0,0,0,1] = exprones(36)
for x in range(16,16+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[24,0:36,0,0,0,4] = exprones(36)
Edge_Net_Subnet2[24,0:36,0,0,2,4] = exprones(36)
Edge_Net[24,0:36,0,0,0,1] = exprones(36)
for x in range(24,24+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-5 Terminal[4] to Terminal[5]
# Poly(24,24,0,35) ==> AIL1(42,42,1,8)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[24,0:36,0,0,0,5] = exprones(36)
Edge_Net_Subnet2[24,0:36,0,0,2,5] = exprones(36)
Edge_Net[24,0:36,0,0,0,1] = exprones(36)
for x in range(24,24+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[42,1:9,0,0,1,5] = exprones(8)
Edge_Net_Subnet2[42,1:9,0,0,2,5] = exprones(8)
Edge_Net[42,1:9,0,0,1,1] = exprones(8)
for x in range(42,42+1):
  for y in range(1,8+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-6 Terminal[5] to Terminal[6]
# AIL1(42,42,1,8) ==> AIL1(46,46,1,6)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[42,1:9,0,0,1,6] = exprones(8)
Edge_Net_Subnet2[42,1:9,0,0,2,6] = exprones(8)
Edge_Net[42,1:9,0,0,1,1] = exprones(8)
for x in range(42,42+1):
  for y in range(1,8+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[46,1:7,0,0,1,6] = exprones(6)
Edge_Net_Subnet2[46,1:7,0,0,2,6] = exprones(6)
Edge_Net[46,1:7,0,0,1,1] = exprones(6)
for x in range(46,46+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-7 Terminal[6] to Terminal[7]
# AIL1(46,46,1,6) ==> AIL1(58,58,1,14)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[46,1:7,0,0,1,7] = exprones(6)
Edge_Net_Subnet2[46,1:7,0,0,2,7] = exprones(6)
Edge_Net[46,1:7,0,0,1,1] = exprones(6)
for x in range(46,46+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[58,1:15,0,0,1,7] = exprones(14)
Edge_Net_Subnet2[58,1:15,0,0,2,7] = exprones(14)
Edge_Net[58,1:15,0,0,1,1] = exprones(14)
for x in range(58,58+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-8 Terminal[7] to Terminal[8]
# AIL1(58,58,1,14) ==> AIL1(62,62,1,14)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[58,1:15,0,0,1,8] = exprones(14)
Edge_Net_Subnet2[58,1:15,0,0,2,8] = exprones(14)
Edge_Net[58,1:15,0,0,1,1] = exprones(14)
for x in range(58,58+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[62,1:15,0,0,1,8] = exprones(14)
Edge_Net_Subnet2[62,1:15,0,0,2,8] = exprones(14)
Edge_Net[62,1:15,0,0,1,1] = exprones(14)
for x in range(62,62+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-9 Terminal[8] to Terminal[9]
# AIL1(62,62,1,14) ==> AIL1(74,74,1,8)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[62,1:15,0,0,1,9] = exprones(14)
Edge_Net_Subnet2[62,1:15,0,0,2,9] = exprones(14)
Edge_Net[62,1:15,0,0,1,1] = exprones(14)
for x in range(62,62+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[74,1:9,0,0,1,9] = exprones(8)
Edge_Net_Subnet2[74,1:9,0,0,2,9] = exprones(8)
Edge_Net[74,1:9,0,0,1,1] = exprones(8)
for x in range(74,74+1):
  for y in range(1,8+1) :
    outLayout[x][y][0][0] = 2
# Net-4 subNet-0 Terminal[0] to Terminal[2]
# Poly(32,32,0,35) ==> Poly(32,32,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet4[32,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet4[32,0:36,0,0,2,0] = exprones(36)
Edge_Net[32,0:36,0,0,0,3] = exprones(36)
for x in range(32,32+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 4
Edge_Net_Subnet4[32,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet4[32,0:36,0,0,2,0] = exprones(36)
Edge_Net[32,0:36,0,0,0,3] = exprones(36)
for x in range(32,32+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 4
# Net-4 subNet-1 Terminal[0] to Terminal[1]
# Poly(32,32,0,35) ==> Poly(72,72,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet4[32,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet4[32,0:36,0,0,2,1] = exprones(36)
Edge_Net[32,0:36,0,0,0,3] = exprones(36)
for x in range(32,32+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 4
Edge_Net_Subnet4[72,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet4[72,0:36,0,0,2,1] = exprones(36)
Edge_Net[72,0:36,0,0,0,3] = exprones(36)
for x in range(72,72+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 4
# Net-4 subNet-2 Terminal[1] to Terminal[3]
# Poly(72,72,0,35) ==> Poly(72,72,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet4[72,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet4[72,0:36,0,0,2,2] = exprones(36)
Edge_Net[72,0:36,0,0,0,3] = exprones(36)
for x in range(72,72+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 4
Edge_Net_Subnet4[72,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet4[72,0:36,0,0,2,2] = exprones(36)
Edge_Net[72,0:36,0,0,0,3] = exprones(36)
for x in range(72,72+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 4
# Net-5 subNet-0 Terminal[0] to Terminal[2]
# AIL1(34,34,1,8) ==> AIL1(34,34,26,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet5[34,1:9,0,0,1,0] = exprones(8)
Edge_Net_Subnet5[34,1:9,0,0,2,0] = exprones(8)
Edge_Net[34,1:9,0,0,1,4] = exprones(8)
for x in range(34,34+1):
  for y in range(1,8+1) :
    outLayout[x][y][0][0] = 5
Edge_Net_Subnet5[34,26:34,0,0,1,0] = exprones(8)
Edge_Net_Subnet5[34,26:34,0,0,2,0] = exprones(8)
Edge_Net[34,26:34,0,0,1,4] = exprones(8)
for x in range(34,34+1):
  for y in range(26,33+1) :
    outLayout[x][y][0][0] = 5
# Net-5 subNet-1 Terminal[0] to Terminal[1]
# AIL1(34,34,1,8) ==> Poly(40,40,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet5[34,1:9,0,0,1,1] = exprones(8)
Edge_Net_Subnet5[34,1:9,0,0,2,1] = exprones(8)
Edge_Net[34,1:9,0,0,1,4] = exprones(8)
for x in range(34,34+1):
  for y in range(1,8+1) :
    outLayout[x][y][0][0] = 5
Edge_Net_Subnet5[40,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet5[40,0:36,0,0,2,1] = exprones(36)
Edge_Net[40,0:36,0,0,0,4] = exprones(36)
for x in range(40,40+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 5
# Net-5 subNet-2 Terminal[1] to Terminal[3]
# Poly(40,40,0,35) ==> Poly(40,40,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet5[40,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet5[40,0:36,0,0,2,2] = exprones(36)
Edge_Net[40,0:36,0,0,0,4] = exprones(36)
for x in range(40,40+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 5
Edge_Net_Subnet5[40,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet5[40,0:36,0,0,2,2] = exprones(36)
Edge_Net[40,0:36,0,0,0,4] = exprones(36)
for x in range(40,40+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 5
# Net-3 subNet-0 Terminal[0] to Terminal[6]
# AIL1(38,38,1,8) ==> AIL1(38,38,26,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[38,1:9,0,0,1,0] = exprones(8)
Edge_Net_Subnet3[38,1:9,0,0,2,0] = exprones(8)
Edge_Net[38,1:9,0,0,1,2] = exprones(8)
for x in range(38,38+1):
  for y in range(1,8+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[38,26:34,0,0,1,0] = exprones(8)
Edge_Net_Subnet3[38,26:34,0,0,2,0] = exprones(8)
Edge_Net[38,26:34,0,0,1,2] = exprones(8)
for x in range(38,38+1):
  for y in range(26,33+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-1 Terminal[6] to Terminal[7]
# AIL1(38,38,26,33) ==> AIL1(50,50,20,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[38,26:34,0,0,1,1] = exprones(8)
Edge_Net_Subnet3[38,26:34,0,0,2,1] = exprones(8)
Edge_Net[38,26:34,0,0,1,2] = exprones(8)
for x in range(38,38+1):
  for y in range(26,33+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[50,20:34,0,0,1,1] = exprones(14)
Edge_Net_Subnet3[50,20:34,0,0,2,1] = exprones(14)
Edge_Net[50,20:34,0,0,1,2] = exprones(14)
for x in range(50,50+1):
  for y in range(20,33+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-2 Terminal[7] to Terminal[8]
# AIL1(50,50,20,33) ==> AIL1(54,54,20,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[50,20:34,0,0,1,2] = exprones(14)
Edge_Net_Subnet3[50,20:34,0,0,2,2] = exprones(14)
Edge_Net[50,20:34,0,0,1,2] = exprones(14)
for x in range(50,50+1):
  for y in range(20,33+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[54,20:34,0,0,1,2] = exprones(14)
Edge_Net_Subnet3[54,20:34,0,0,2,2] = exprones(14)
Edge_Net[54,20:34,0,0,1,2] = exprones(14)
for x in range(54,54+1):
  for y in range(20,33+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-3 Terminal[8] to Terminal[9]
# AIL1(54,54,20,33) ==> AIL1(66,66,28,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[54,20:34,0,0,1,3] = exprones(14)
Edge_Net_Subnet3[54,20:34,0,0,2,3] = exprones(14)
Edge_Net[54,20:34,0,0,1,2] = exprones(14)
for x in range(54,54+1):
  for y in range(20,33+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[66,28:34,0,0,1,3] = exprones(6)
Edge_Net_Subnet3[66,28:34,0,0,2,3] = exprones(6)
Edge_Net[66,28:34,0,0,1,2] = exprones(6)
for x in range(66,66+1):
  for y in range(28,33+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-4 Terminal[9] to Terminal[10]
# AIL1(66,66,28,33) ==> AIL1(70,70,26,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[66,28:34,0,0,1,4] = exprones(6)
Edge_Net_Subnet3[66,28:34,0,0,2,4] = exprones(6)
Edge_Net[66,28:34,0,0,1,2] = exprones(6)
for x in range(66,66+1):
  for y in range(28,33+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[70,26:34,0,0,1,4] = exprones(8)
Edge_Net_Subnet3[70,26:34,0,0,2,4] = exprones(8)
Edge_Net[70,26:34,0,0,1,2] = exprones(8)
for x in range(70,70+1):
  for y in range(26,33+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-5 Terminal[6] to Terminal[5]
# AIL1(38,38,26,33) ==> Poly(24,24,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[38,26:34,0,0,1,5] = exprones(8)
Edge_Net_Subnet3[38,26:34,0,0,2,5] = exprones(8)
Edge_Net[38,26:34,0,0,1,2] = exprones(8)
for x in range(38,38+1):
  for y in range(26,33+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[24,0:36,0,0,0,5] = exprones(36)
Edge_Net_Subnet3[24,0:36,0,0,2,5] = exprones(36)
Edge_Net[24,0:36,0,0,0,2] = exprones(36)
for x in range(24,24+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-6 Terminal[5] to Terminal[4]
# Poly(24,24,0,35) ==> Poly(16,16,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[24,0:36,0,0,0,6] = exprones(36)
Edge_Net_Subnet3[24,0:36,0,0,2,6] = exprones(36)
Edge_Net[24,0:36,0,0,0,2] = exprones(36)
for x in range(24,24+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[16,0:36,0,0,0,6] = exprones(36)
Edge_Net_Subnet3[16,0:36,0,0,2,6] = exprones(36)
Edge_Net[16,0:36,0,0,0,2] = exprones(36)
for x in range(16,16+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-7 Terminal[4] to Terminal[3]
# Poly(16,16,0,35) ==> Poly(12,12,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[16,0:36,0,0,0,7] = exprones(36)
Edge_Net_Subnet3[16,0:36,0,0,2,7] = exprones(36)
Edge_Net[16,0:36,0,0,0,2] = exprones(36)
for x in range(16,16+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[12,0:36,0,0,0,7] = exprones(36)
Edge_Net_Subnet3[12,0:36,0,0,2,7] = exprones(36)
Edge_Net[12,0:36,0,0,0,2] = exprones(36)
for x in range(12,12+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-8 Terminal[3] to Terminal[2]
# Poly(12,12,0,35) ==> Poly(8,8,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[12,0:36,0,0,0,8] = exprones(36)
Edge_Net_Subnet3[12,0:36,0,0,2,8] = exprones(36)
Edge_Net[12,0:36,0,0,0,2] = exprones(36)
for x in range(12,12+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[8,0:36,0,0,0,8] = exprones(36)
Edge_Net_Subnet3[8,0:36,0,0,2,8] = exprones(36)
Edge_Net[8,0:36,0,0,0,2] = exprones(36)
for x in range(8,8+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-9 Terminal[2] to Terminal[1]
# Poly(8,8,0,35) ==> Poly(4,4,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[8,0:36,0,0,0,9] = exprones(36)
Edge_Net_Subnet3[8,0:36,0,0,2,9] = exprones(36)
Edge_Net[8,0:36,0,0,0,2] = exprones(36)
for x in range(8,8+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[4,0:36,0,0,0,9] = exprones(36)
Edge_Net_Subnet3[4,0:36,0,0,2,9] = exprones(36)
Edge_Net[4,0:36,0,0,0,2] = exprones(36)
for x in range(4,4+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
# Net-8 subNet-0 Terminal[0] to Terminal[3]
# Poly(48,48,0,35) ==> Poly(48,48,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet8[48,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet8[48,0:36,0,0,2,0] = exprones(36)
Edge_Net[48,0:36,0,0,0,7] = exprones(36)
for x in range(48,48+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
Edge_Net_Subnet8[48,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet8[48,0:36,0,0,2,0] = exprones(36)
Edge_Net[48,0:36,0,0,0,7] = exprones(36)
for x in range(48,48+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
# Net-8 subNet-1 Terminal[0] to Terminal[1]
# Poly(48,48,0,35) ==> Poly(56,56,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet8[48,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet8[48,0:36,0,0,2,1] = exprones(36)
Edge_Net[48,0:36,0,0,0,7] = exprones(36)
for x in range(48,48+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
Edge_Net_Subnet8[56,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet8[56,0:36,0,0,2,1] = exprones(36)
Edge_Net[56,0:36,0,0,0,7] = exprones(36)
for x in range(56,56+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
# Net-8 subNet-2 Terminal[1] to Terminal[4]
# Poly(56,56,0,35) ==> Poly(56,56,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet8[56,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet8[56,0:36,0,0,2,2] = exprones(36)
Edge_Net[56,0:36,0,0,0,7] = exprones(36)
for x in range(56,56+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
Edge_Net_Subnet8[56,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet8[56,0:36,0,0,2,2] = exprones(36)
Edge_Net[56,0:36,0,0,0,7] = exprones(36)
for x in range(56,56+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
# Net-8 subNet-3 Terminal[1] to Terminal[2]
# Poly(56,56,0,35) ==> Poly(64,64,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet8[56,0:36,0,0,0,3] = exprones(36)
Edge_Net_Subnet8[56,0:36,0,0,2,3] = exprones(36)
Edge_Net[56,0:36,0,0,0,7] = exprones(36)
for x in range(56,56+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
Edge_Net_Subnet8[64,0:36,0,0,0,3] = exprones(36)
Edge_Net_Subnet8[64,0:36,0,0,2,3] = exprones(36)
Edge_Net[64,0:36,0,0,0,7] = exprones(36)
for x in range(64,64+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
# Net-8 subNet-4 Terminal[2] to Terminal[5]
# Poly(64,64,0,35) ==> Poly(64,64,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet8[64,0:36,0,0,0,4] = exprones(36)
Edge_Net_Subnet8[64,0:36,0,0,2,4] = exprones(36)
Edge_Net[64,0:36,0,0,0,7] = exprones(36)
for x in range(64,64+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
Edge_Net_Subnet8[64,0:36,0,0,0,4] = exprones(36)
Edge_Net_Subnet8[64,0:36,0,0,2,4] = exprones(36)
Edge_Net[64,0:36,0,0,0,7] = exprones(36)
for x in range(64,64+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
# Net = 1 Subnet = 0 | Left -> Right [0,6] Top -> Bottom [0,35]
# Range R1(2,2,1,14)
# Range R2(2,2,20,33)
### Disable edges outside window
Edge_Net_Subnet1[6:85+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(103680)

### Consistency Constraints
Net1_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,0]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,6+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet1[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,0])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,6+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,2,trend,0,0],Xor(Edge_Net_Subnet1[x,y,2,trend,1,0],Edge_Net_Subnet1[x,y,2,trend,2,0])),And(~Edge_Net_Subnet1[x,y,2,trend,0,0],~Edge_Net_Subnet1[x,y,2,trend,1,0],~Edge_Net_Subnet1[x,y,2,trend,2,0]))for x in range(0,6+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,3,1,0,0],Xor(Edge_Net_Subnet1[x,y,3,1,1,0],Edge_Net_Subnet1[x,y,3,1,2,0])),And(~Edge_Net_Subnet1[x,y,3,1,0,0],~Edge_Net_Subnet1[x,y,3,1,1,0],~Edge_Net_Subnet1[x,y,3,1,2,0]))for x in range(0,6+1)])for y in range(0,35+1)]).to_cnf()
Net1_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,1,trend,2,0],Xor(Edge_Net_Subnet1[x,y,1,trend,0,0],Edge_Net_Subnet1[x,y,1,trend,1,0])),And(~Edge_Net_Subnet1[x,y,1,trend,2,0],~Edge_Net_Subnet1[x,y,1,trend,0,0],~Edge_Net_Subnet1[x,y,1,trend,1,0]))for x in range(0,6+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet0_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,0], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(0+1,7)]))for trend in range(0,1+1)])for x in range(0,6+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,0], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(0+1,7)]))for trend in range(0,1+1)])for x in range(0,6+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net1_Subnet0_C = And(Net1_Subnet0_C1, Net1_Subnet0_C2,Net1_Subnet0_C3_ME1_Mask,Net1_Subnet0_C4_MINT1_Mask,Net1_Subnet0_C5_AIL2GIL_Mask,Net1_Subnet0_C6,)
### Design Rules
Net1_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(0,6+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(0,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(0,6+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net1_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,0], ~Edge_Net_Subnet1[x-1,y,1,1,1,0]), And(Edge_Net_Subnet1[x+1,y,1,1,1,0], Edge_Net_Subnet1[x+2,y,1,1,1,0], Edge_Net_Subnet1[x+3,y,1,1,1,0], ))for x in range(1,6+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,0], ~Edge_Net_Subnet1[x+1,y,1,1,1,0]), And(Edge_Net_Subnet1[x-1,y,1,1,1,0], Edge_Net_Subnet1[x-2,y,1,1,1,0], Edge_Net_Subnet1[x-3,y,1,1,1,0], ))for x in range(3,6+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,6+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(0,6+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(0,6+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(0,6+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0]), And(Edge_Net_Subnet1[x,y+1,1,0,0,0], Edge_Net_Subnet1[x,y+2,1,0,0,0], Edge_Net_Subnet1[x,y+3,1,0,0,0], ))for x in range(0,6+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0]), And(Edge_Net_Subnet1[x,y-1,1,0,0,0], Edge_Net_Subnet1[x,y-2,1,0,0,0], Edge_Net_Subnet1[x,y-3,1,0,0,0], ))for x in range(0,6+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge_Net_Subnet1[x,y-1,1,0,0,0]), And(Edge_Net_Subnet1[x,y+1,1,0,0,0], Edge_Net_Subnet1[x,y+2,1,0,0,0], Edge_Net_Subnet1[x,y+3,1,0,0,0], ))for x in range(0,6+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge_Net_Subnet1[x,y+1,1,0,0,0]), And(Edge_Net_Subnet1[x,y-1,1,0,0,0], Edge_Net_Subnet1[x,y-2,1,0,0,0], Edge_Net_Subnet1[x,y-3,1,0,0,0], ))for x in range(0,6+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net1_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(0,6+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(0,6+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(0,6+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(0,6+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(0,6+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(0,6+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net1_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(0,6+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,6+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,0], ~Edge_Net_Subnet1[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet1[x+1,y,3,1,mask,0], Edge_Net_Subnet1[x+2,y,3,1,mask,0], Edge_Net_Subnet1[x+3,y,3,1,mask,0], Edge_Net_Subnet1[x+4,y,3,1,mask,0], Edge_Net_Subnet1[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(1,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,0], ~Edge_Net_Subnet1[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet1[x-1,y,3,1,mask,0], Edge_Net_Subnet1[x-2,y,3,1,mask,0], Edge_Net_Subnet1[x-3,y,3,1,mask,0], Edge_Net_Subnet1[x-4,y,3,1,mask,0], Edge_Net_Subnet1[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,0], And(Edge_Net_Subnet1[x+1,y,3,1,mask,0], Edge_Net_Subnet1[x+2,y,3,1,mask,0], Edge_Net_Subnet1[x+3,y,3,1,mask,0], Edge_Net_Subnet1[x+4,y,3,1,mask,0], Edge_Net_Subnet1[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(0, 0+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(0,6+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(0,6+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,6+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(0,6+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,0], ~Edge_Net_Subnet1[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet1[x+1,y,2,1,mask,0], Edge_Net_Subnet1[x+2,y,2,1,mask,0], Edge_Net_Subnet1[x+3,y,2,1,mask,0], Edge_Net_Subnet1[x+4,y,2,1,mask,0], Edge_Net_Subnet1[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(1,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,0], ~Edge_Net_Subnet1[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet1[x-1,y,2,1,mask,0], Edge_Net_Subnet1[x-2,y,2,1,mask,0], Edge_Net_Subnet1[x-3,y,2,1,mask,0], Edge_Net_Subnet1[x-4,y,2,1,mask,0], Edge_Net_Subnet1[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,0], And(Edge_Net_Subnet1[x-1,y,2,1,mask,0], Edge_Net_Subnet1[x-2,y,2,1,mask,0], Edge_Net_Subnet1[x-3,y,2,1,mask,0], Edge_Net_Subnet1[x-4,y,2,1,mask,0], Edge_Net_Subnet1[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(0,0+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,0], And(Edge_Net_Subnet1[x+1,y,2,1,mask,0], Edge_Net_Subnet1[x+2,y,2,1,mask,0], Edge_Net_Subnet1[x+3,y,2,1,mask,0], Edge_Net_Subnet1[x+4,y,2,1,mask,0], Edge_Net_Subnet1[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(6-1,0)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,0], ~Edge_Net_Subnet1[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet1[x,y+1,2,0,mask,0], Edge_Net_Subnet1[x,y+2,2,0,mask,0], Edge_Net_Subnet1[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,0], ~Edge_Net_Subnet1[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet1[x,y-1,2,0,mask,0], Edge_Net_Subnet1[x,y-2,2,0,mask,0], Edge_Net_Subnet1[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,0], And(Edge_Net_Subnet1[x,y+1,2,0,mask,0], Edge_Net_Subnet1[x,y+2,2,0,mask,0], Edge_Net_Subnet1[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,0], And(Edge_Net_Subnet1[x,y-1,2,0,mask,0], Edge_Net_Subnet1[x,y-2,2,0,mask,0], Edge_Net_Subnet1[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(35,35+1)]),
	).to_cnf()
Net1_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,6+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(0,6+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(0,6+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(0,6+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net1_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net1_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(0,6+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(0,6+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(4,35+1)]),
	).to_cnf()
Net1_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(0,6+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,6+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,6+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,6+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,6+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,6+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,6+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,6+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,6+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet0_DR = And(Net1_Subnet0_DR_Trend, Net1_Subnet0_DR_GIL_HorMinWidth,Net1_Subnet0_DR_GIL_HorMinSpacing,Net1_Subnet0_DR_GIL_VerMinSpacing,Net1_Subnet0_DR_AIL2_VerMinWidth,Net1_Subnet0_DR_AIL2_VerMinSpacing,Net1_Subnet0_DR_VerAIL2_HorMinSpacing,Net1_Subnet0_DR_MINT1AB_HorMinWidth,Net1_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net1_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net1_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net1_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net1_Subnet0_DR_M1AB_MinWidth,Net1_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net1_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net1_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net1_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net1_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net1_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net1_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net1_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net1_Subnet0_DR_V0_HorMinSpacing,Net1_Subnet0_DR_V1_HorMinSpacing,Net1_Subnet0_DR_V0_VerMinSpacing,Net1_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net1_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet1,[2,1,0,0, 2,2,0,0, 2,3,0,0, 2,4,0,0, 2,5,0,0, 2,6,0,0, 2,7,0,0, 2,8,0,0, 2,9,0,0, 2,10,0,0, 2,11,0,0, 2,12,0,0, 2,13,0,0, 2,14,0,0, ],14,0,0,1,6,35,3,0),
	RConstraints.R1(Edge_Net_Subnet1,[2,20,0,0, 2,21,0,0, 2,22,0,0, 2,23,0,0, 2,24,0,0, 2,25,0,0, 2,26,0,0, 2,27,0,0, 2,28,0,0, 2,29,0,0, 2,30,0,0, 2,31,0,0, 2,32,0,0, 2,33,0,0, ],14,0,0,1,6,35,3,0),
	).to_cnf()
Net1_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet1,Edge,Edge_Net,[2,1,0, 2,2,0, 2,3,0, 2,4,0, 2,5,0, 2,6,0, 2,7,0, 2,8,0, 2,9,0, 2,10,0, 2,11,0, 2,12,0, 2,13,0, 2,14,0, 2,15,0, 2,20,0, 2,21,0, 2,22,0, 2,23,0, 2,24,0, 2,25,0, 2,26,0, 2,27,0, 2,28,0, 2,29,0, 2,30,0, 2,31,0, 2,32,0, 2,33,0, 2,34,0, ],30,0,0,0,6,35,3,0,0),
	)
Net1_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,0],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(1,5+1)])for x in range(0,6+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	).to_cnf()
Net1_Subnet0_R = And(Net1_Subnet0_R1,Net1_Subnet0_R2,Net1_Subnet0_R3,)
Net1_Subnet0_Formula = And(Net1_Subnet0_C,Net1_Subnet0_DR,Net1_Subnet0_R)
# Net = 1 Subnet = 1 | Left -> Right [0,14] Top -> Bottom [0,18]
# Range R1(2,2,1,14)
# Range R2(10,10,1,14)
### Disable edges outside window
Edge_Net_Subnet1[0:14,18:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(9072)
Edge_Net_Subnet1[14:85+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(93312)

### Consistency Constraints
Net1_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,0]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,14+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet1[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,0])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,14+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,2,trend,0,1],Xor(Edge_Net_Subnet1[x,y,2,trend,1,1],Edge_Net_Subnet1[x,y,2,trend,2,1])),And(~Edge_Net_Subnet1[x,y,2,trend,0,1],~Edge_Net_Subnet1[x,y,2,trend,1,1],~Edge_Net_Subnet1[x,y,2,trend,2,1]))for x in range(0,14+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,3,1,0,1],Xor(Edge_Net_Subnet1[x,y,3,1,1,1],Edge_Net_Subnet1[x,y,3,1,2,1])),And(~Edge_Net_Subnet1[x,y,3,1,0,1],~Edge_Net_Subnet1[x,y,3,1,1,1],~Edge_Net_Subnet1[x,y,3,1,2,1]))for x in range(0,14+1)])for y in range(0,18+1)]).to_cnf()
Net1_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,1,trend,2,1],Xor(Edge_Net_Subnet1[x,y,1,trend,0,1],Edge_Net_Subnet1[x,y,1,trend,1,1])),And(~Edge_Net_Subnet1[x,y,1,trend,2,1],~Edge_Net_Subnet1[x,y,1,trend,0,1],~Edge_Net_Subnet1[x,y,1,trend,1,1]))for x in range(0,14+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(0,14+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(1+1,7)]))for trend in range(0,1+1)])for x in range(0,14+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(0,14+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(1+1,7)]))for trend in range(0,1+1)])for x in range(0,14+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
).to_cnf()
Net1_Subnet1_C = And(Net1_Subnet1_C1, Net1_Subnet1_C2,Net1_Subnet1_C3_ME1_Mask,Net1_Subnet1_C4_MINT1_Mask,Net1_Subnet1_C5_AIL2GIL_Mask,Net1_Subnet1_C6,)
### Design Rules
Net1_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(0,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(0,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(0,14+1)])for y in range(0,18+1)])for mask in range(0,2+1)])
	).to_cnf()
Net1_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,1], ~Edge_Net_Subnet1[x-1,y,1,1,1,1]), And(Edge_Net_Subnet1[x+1,y,1,1,1,1], Edge_Net_Subnet1[x+2,y,1,1,1,1], Edge_Net_Subnet1[x+3,y,1,1,1,1], ))for x in range(1,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,1], ~Edge_Net_Subnet1[x+1,y,1,1,1,1]), And(Edge_Net_Subnet1[x-1,y,1,1,1,1], Edge_Net_Subnet1[x-2,y,1,1,1,1], Edge_Net_Subnet1[x-3,y,1,1,1,1], ))for x in range(3,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,14+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(0,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(0,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(0,14+1)])for y in range(3,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1]), And(Edge_Net_Subnet1[x,y+1,1,0,0,1], Edge_Net_Subnet1[x,y+2,1,0,0,1], Edge_Net_Subnet1[x,y+3,1,0,0,1], ))for x in range(0,14+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge_Net_Subnet1[x,y-1,1,0,0,1]), And(Edge_Net_Subnet1[x,y+1,1,0,0,1], Edge_Net_Subnet1[x,y+2,1,0,0,1], Edge_Net_Subnet1[x,y+3,1,0,0,1], ))for x in range(0,14+1)])for y in range(0+1,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge_Net_Subnet1[x,y+1,1,0,0,1]), And(Edge_Net_Subnet1[x,y-1,1,0,0,1], Edge_Net_Subnet1[x,y-2,1,0,0,1], Edge_Net_Subnet1[x,y-3,1,0,0,1], ))for x in range(0,14+1)])for y in range(0+3,18+1)])
	).to_cnf()
Net1_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(0,14+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(0,14+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(0,14+1)])for y in range(0+3,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(0,14+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net1_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(0,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,14+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,1], ~Edge_Net_Subnet1[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet1[x+1,y,3,1,mask,1], Edge_Net_Subnet1[x+2,y,3,1,mask,1], Edge_Net_Subnet1[x+3,y,3,1,mask,1], Edge_Net_Subnet1[x+4,y,3,1,mask,1], Edge_Net_Subnet1[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(1,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,1], ~Edge_Net_Subnet1[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet1[x-1,y,3,1,mask,1], Edge_Net_Subnet1[x-2,y,3,1,mask,1], Edge_Net_Subnet1[x-3,y,3,1,mask,1], Edge_Net_Subnet1[x-4,y,3,1,mask,1], Edge_Net_Subnet1[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,1], And(Edge_Net_Subnet1[x+1,y,3,1,mask,1], Edge_Net_Subnet1[x+2,y,3,1,mask,1], Edge_Net_Subnet1[x+3,y,3,1,mask,1], Edge_Net_Subnet1[x+4,y,3,1,mask,1], Edge_Net_Subnet1[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(0, 0+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(3,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(0,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(0,14+1)])for y in range(2,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,14+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(0,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,1], ~Edge_Net_Subnet1[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet1[x+1,y,2,1,mask,1], Edge_Net_Subnet1[x+2,y,2,1,mask,1], Edge_Net_Subnet1[x+3,y,2,1,mask,1], Edge_Net_Subnet1[x+4,y,2,1,mask,1], Edge_Net_Subnet1[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(1,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,1], ~Edge_Net_Subnet1[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet1[x-1,y,2,1,mask,1], Edge_Net_Subnet1[x-2,y,2,1,mask,1], Edge_Net_Subnet1[x-3,y,2,1,mask,1], Edge_Net_Subnet1[x-4,y,2,1,mask,1], Edge_Net_Subnet1[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,1], And(Edge_Net_Subnet1[x-1,y,2,1,mask,1], Edge_Net_Subnet1[x-2,y,2,1,mask,1], Edge_Net_Subnet1[x-3,y,2,1,mask,1], Edge_Net_Subnet1[x-4,y,2,1,mask,1], Edge_Net_Subnet1[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(0,0+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,1], And(Edge_Net_Subnet1[x+1,y,2,1,mask,1], Edge_Net_Subnet1[x+2,y,2,1,mask,1], Edge_Net_Subnet1[x+3,y,2,1,mask,1], Edge_Net_Subnet1[x+4,y,2,1,mask,1], Edge_Net_Subnet1[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(14-1,0)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,1], ~Edge_Net_Subnet1[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet1[x,y+1,2,0,mask,1], Edge_Net_Subnet1[x,y+2,2,0,mask,1], Edge_Net_Subnet1[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0+1,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,1], ~Edge_Net_Subnet1[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet1[x,y-1,2,0,mask,1], Edge_Net_Subnet1[x,y-2,2,0,mask,1], Edge_Net_Subnet1[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0+3,18+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,1], And(Edge_Net_Subnet1[x,y+1,2,0,mask,1], Edge_Net_Subnet1[x,y+2,2,0,mask,1], Edge_Net_Subnet1[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,1], And(Edge_Net_Subnet1[x,y-1,2,0,mask,1], Edge_Net_Subnet1[x,y-2,2,0,mask,1], Edge_Net_Subnet1[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(18,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,14+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(0,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(0,14+1)])for y in range(2,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(0,14+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(4,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(0,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(0,14+1)])for y in range(3,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(4,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(0,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,14+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,14+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,14+1)])for y in range(2,18+1)]),
	).to_cnf()
Net1_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,14+1)])for y in range(2,18+1)]),
	).to_cnf()
Net1_Subnet1_DR = And(Net1_Subnet1_DR_Trend, Net1_Subnet1_DR_GIL_HorMinWidth,Net1_Subnet1_DR_GIL_HorMinSpacing,Net1_Subnet1_DR_GIL_VerMinSpacing,Net1_Subnet1_DR_AIL2_VerMinWidth,Net1_Subnet1_DR_AIL2_VerMinSpacing,Net1_Subnet1_DR_VerAIL2_HorMinSpacing,Net1_Subnet1_DR_MINT1AB_HorMinWidth,Net1_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net1_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net1_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net1_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net1_Subnet1_DR_M1AB_MinWidth,Net1_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net1_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net1_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net1_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net1_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net1_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net1_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net1_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net1_Subnet1_DR_V0_HorMinSpacing,Net1_Subnet1_DR_V1_HorMinSpacing,Net1_Subnet1_DR_V0_VerMinSpacing,Net1_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net1_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet1,[2,1,0,0, 2,2,0,0, 2,3,0,0, 2,4,0,0, 2,5,0,0, 2,6,0,0, 2,7,0,0, 2,8,0,0, 2,9,0,0, 2,10,0,0, 2,11,0,0, 2,12,0,0, 2,13,0,0, 2,14,0,0, ],14,0,0,1,14,18,3,1),
	RConstraints.R1(Edge_Net_Subnet1,[10,1,0,0, 10,2,0,0, 10,3,0,0, 10,4,0,0, 10,5,0,0, 10,6,0,0, 10,7,0,0, 10,8,0,0, 10,9,0,0, 10,10,0,0, 10,11,0,0, 10,12,0,0, 10,13,0,0, 10,14,0,0, ],14,0,0,1,14,18,3,1),
	).to_cnf()
Net1_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet1,Edge,Edge_Net,[2,1,0, 2,2,0, 2,3,0, 2,4,0, 2,5,0, 2,6,0, 2,7,0, 2,8,0, 2,9,0, 2,10,0, 2,11,0, 2,12,0, 2,13,0, 2,14,0, 2,15,0, 10,1,0, 10,2,0, 10,3,0, 10,4,0, 10,5,0, 10,6,0, 10,7,0, 10,8,0, 10,9,0, 10,10,0, 10,11,0, 10,12,0, 10,13,0, 10,14,0, 10,15,0, ],30,0,0,0,14,18,3,1,0),
	)
Net1_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,0],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(1,5+1)])for x in range(0,14+1)])for y in range(0,18+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	).to_cnf()
Net1_Subnet1_R = And(Net1_Subnet1_R1,Net1_Subnet1_R2,Net1_Subnet1_R3,)
Net1_Subnet1_Formula = And(Net1_Subnet1_C,Net1_Subnet1_DR,Net1_Subnet1_R)
# Net = 1 Subnet = 2 | Left -> Right [6,14] Top -> Bottom [0,35]
# Range R1(10,10,1,14)
# Range R2(10,10,20,33)
### Disable edges outside window
Edge_Net_Subnet1[0:6,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(7776)
Edge_Net_Subnet1[14:85+1,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(93312)

### Consistency Constraints
Net1_Subnet2_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,0]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet2_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet1[x,y,z,trend,mask,2]), Edge_Net[x,y,z,trend,mask,0])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet2_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,2,trend,0,2],Xor(Edge_Net_Subnet1[x,y,2,trend,1,2],Edge_Net_Subnet1[x,y,2,trend,2,2])),And(~Edge_Net_Subnet1[x,y,2,trend,0,2],~Edge_Net_Subnet1[x,y,2,trend,1,2],~Edge_Net_Subnet1[x,y,2,trend,2,2]))for x in range(6,14+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet2_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,3,1,0,2],Xor(Edge_Net_Subnet1[x,y,3,1,1,2],Edge_Net_Subnet1[x,y,3,1,2,2])),And(~Edge_Net_Subnet1[x,y,3,1,0,2],~Edge_Net_Subnet1[x,y,3,1,1,2],~Edge_Net_Subnet1[x,y,3,1,2,2]))for x in range(6,14+1)])for y in range(0,35+1)]).to_cnf()
Net1_Subnet2_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,1,trend,2,2],Xor(Edge_Net_Subnet1[x,y,1,trend,0,2],Edge_Net_Subnet1[x,y,1,trend,1,2])),And(~Edge_Net_Subnet1[x,y,1,trend,2,2],~Edge_Net_Subnet1[x,y,1,trend,0,2],~Edge_Net_Subnet1[x,y,1,trend,1,2]))for x in range(6,14+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet2_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(2+1,7)]))for trend in range(0,1+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(2+1,7)]))for trend in range(0,1+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net1_Subnet2_C = And(Net1_Subnet2_C1, Net1_Subnet2_C2,Net1_Subnet2_C3_ME1_Mask,Net1_Subnet2_C4_MINT1_Mask,Net1_Subnet2_C5_AIL2GIL_Mask,Net1_Subnet2_C6,)
### Design Rules
Net1_Subnet2_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(6,14+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net1_Subnet2_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,2], ~Edge_Net_Subnet1[x-1,y,1,1,1,2]), And(Edge_Net_Subnet1[x+1,y,1,1,1,2], Edge_Net_Subnet1[x+2,y,1,1,1,2], Edge_Net_Subnet1[x+3,y,1,1,1,2], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,2], ~Edge_Net_Subnet1[x+1,y,1,1,1,2]), And(Edge_Net_Subnet1[x-1,y,1,1,1,2], Edge_Net_Subnet1[x-2,y,1,1,1,2], Edge_Net_Subnet1[x-3,y,1,1,1,2], ))for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet2_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,2], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,2], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet2_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,2], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(6,14+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,2], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(6,14+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet2_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,2]), And(Edge_Net_Subnet1[x,y+1,1,0,0,2], Edge_Net_Subnet1[x,y+2,1,0,0,2], Edge_Net_Subnet1[x,y+3,1,0,0,2], ))for x in range(6,14+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,2]), And(Edge_Net_Subnet1[x,y-1,1,0,0,2], Edge_Net_Subnet1[x,y-2,1,0,0,2], Edge_Net_Subnet1[x,y-3,1,0,0,2], ))for x in range(6,14+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,2], ~Edge_Net_Subnet1[x,y-1,1,0,0,2]), And(Edge_Net_Subnet1[x,y+1,1,0,0,2], Edge_Net_Subnet1[x,y+2,1,0,0,2], Edge_Net_Subnet1[x,y+3,1,0,0,2], ))for x in range(6,14+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,2], ~Edge_Net_Subnet1[x,y+1,1,0,0,2]), And(Edge_Net_Subnet1[x,y-1,1,0,0,2], Edge_Net_Subnet1[x,y-2,1,0,0,2], Edge_Net_Subnet1[x,y-3,1,0,0,2], ))for x in range(6,14+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net1_Subnet2_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(6,14+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(6,14+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(6,14+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(6,14+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(6,14+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(6,14+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net1_Subnet2_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,2], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,2], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet2_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,2], ~Edge_Net_Subnet1[x-1,y,3,1,mask,2]), And(Edge_Net_Subnet1[x+1,y,3,1,mask,2], Edge_Net_Subnet1[x+2,y,3,1,mask,2], Edge_Net_Subnet1[x+3,y,3,1,mask,2], Edge_Net_Subnet1[x+4,y,3,1,mask,2], Edge_Net_Subnet1[x+5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,2], ~Edge_Net_Subnet1[x+1,y,3,1,mask,2]), And(Edge_Net_Subnet1[x-1,y,3,1,mask,2], Edge_Net_Subnet1[x-2,y,3,1,mask,2], Edge_Net_Subnet1[x-3,y,3,1,mask,2], Edge_Net_Subnet1[x-4,y,3,1,mask,2], Edge_Net_Subnet1[x-5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet2_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,2], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,2], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet2_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,2], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,2], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet2_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,2], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(6,14+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,2], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(6,14+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet2_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,2], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,2], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet2_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,2], ~Edge_Net_Subnet1[x-1,y,2,1,mask,2]), And(Edge_Net_Subnet1[x+1,y,2,1,mask,2], Edge_Net_Subnet1[x+2,y,2,1,mask,2], Edge_Net_Subnet1[x+3,y,2,1,mask,2], Edge_Net_Subnet1[x+4,y,2,1,mask,2], Edge_Net_Subnet1[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,2], ~Edge_Net_Subnet1[x+1,y,2,1,mask,2]), And(Edge_Net_Subnet1[x-1,y,2,1,mask,2], Edge_Net_Subnet1[x-2,y,2,1,mask,2], Edge_Net_Subnet1[x-3,y,2,1,mask,2], Edge_Net_Subnet1[x-4,y,2,1,mask,2], Edge_Net_Subnet1[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,2], And(Edge_Net_Subnet1[x-1,y,2,1,mask,2], Edge_Net_Subnet1[x-2,y,2,1,mask,2], Edge_Net_Subnet1[x-3,y,2,1,mask,2], Edge_Net_Subnet1[x-4,y,2,1,mask,2], Edge_Net_Subnet1[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(6,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,2], And(Edge_Net_Subnet1[x+1,y,2,1,mask,2], Edge_Net_Subnet1[x+2,y,2,1,mask,2], Edge_Net_Subnet1[x+3,y,2,1,mask,2], Edge_Net_Subnet1[x+4,y,2,1,mask,2], Edge_Net_Subnet1[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(14-1,6)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,2], ~Edge_Net_Subnet1[x,y-1,2,0,mask,2]), And(Edge_Net_Subnet1[x,y+1,2,0,mask,2], Edge_Net_Subnet1[x,y+2,2,0,mask,2], Edge_Net_Subnet1[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,2], ~Edge_Net_Subnet1[x,y+1,2,0,mask,2]), And(Edge_Net_Subnet1[x,y-1,2,0,mask,2], Edge_Net_Subnet1[x,y-2,2,0,mask,2], Edge_Net_Subnet1[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,2], And(Edge_Net_Subnet1[x,y+1,2,0,mask,2], Edge_Net_Subnet1[x,y+2,2,0,mask,2], Edge_Net_Subnet1[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,2], And(Edge_Net_Subnet1[x,y-1,2,0,mask,2], Edge_Net_Subnet1[x,y-2,2,0,mask,2], Edge_Net_Subnet1[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(35,35+1)]),
	).to_cnf()
Net1_Subnet2_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,2], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,2], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet2_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,2], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,2], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet2_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,2], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(6,14+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,2], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(6,14+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net1_Subnet2_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,2], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,2], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net1_Subnet2_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,2], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(6,14+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,2], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(6,14+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet2_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,2], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,2], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(4,35+1)]),
	).to_cnf()
Net1_Subnet2_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,2], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,2], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet2_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,2], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,2], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet2_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,2], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,2], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet2_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,2], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,2], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet2_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,2], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,2], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet2_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,2], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,2], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet2_DR = And(Net1_Subnet2_DR_Trend, Net1_Subnet2_DR_GIL_HorMinWidth,Net1_Subnet2_DR_GIL_HorMinSpacing,Net1_Subnet2_DR_GIL_VerMinSpacing,Net1_Subnet2_DR_AIL2_VerMinWidth,Net1_Subnet2_DR_AIL2_VerMinSpacing,Net1_Subnet2_DR_VerAIL2_HorMinSpacing,Net1_Subnet2_DR_MINT1AB_HorMinWidth,Net1_Subnet2_DR_MINT1_SameMask_VerMinSpacing,Net1_Subnet2_DR_MINT1_SameMask_HorMinSpacing,Net1_Subnet2_DR_MINT1_DiffMask_VerMinSpacing,Net1_Subnet2_DR_MINT1_DiffMask_HorMinSpacing,Net1_Subnet2_DR_M1AB_MinWidth,Net1_Subnet2_DR_HorM1_DiffMask_HorMinSpacing,Net1_Subnet2_DR_HorM1_SameMask_HorMinSpacing,Net1_Subnet2_DR_VerM1_DiffMask_VerMinSpacing,Net1_Subnet2_DR_VerM1_SameMask_VerMinSpacing,Net1_Subnet2_DR_HorM1_DiffMask_VerMinSpacing,Net1_Subnet2_DR_HorM1_SameMask_VerMinSpacing,Net1_Subnet2_DR_VerM1_DiffMask_HorMinSpacing,Net1_Subnet2_DR_VerM1_SameMask_HorMinSpacing,Net1_Subnet2_DR_V0_HorMinSpacing,Net1_Subnet2_DR_V1_HorMinSpacing,Net1_Subnet2_DR_V0_VerMinSpacing,Net1_Subnet2_DR_V1_VerMinSpacing,)
### Routability Constraints
Net1_Subnet2_R1 = And(
	RConstraints.R1(Edge_Net_Subnet1,[10,1,0,0, 10,2,0,0, 10,3,0,0, 10,4,0,0, 10,5,0,0, 10,6,0,0, 10,7,0,0, 10,8,0,0, 10,9,0,0, 10,10,0,0, 10,11,0,0, 10,12,0,0, 10,13,0,0, 10,14,0,0, ],14,6,0,1,14,35,3,2),
	RConstraints.R1(Edge_Net_Subnet1,[10,20,0,0, 10,21,0,0, 10,22,0,0, 10,23,0,0, 10,24,0,0, 10,25,0,0, 10,26,0,0, 10,27,0,0, 10,28,0,0, 10,29,0,0, 10,30,0,0, 10,31,0,0, 10,32,0,0, 10,33,0,0, ],14,6,0,1,14,35,3,2),
	).to_cnf()
Net1_Subnet2_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet1,Edge,Edge_Net,[10,1,0, 10,2,0, 10,3,0, 10,4,0, 10,5,0, 10,6,0, 10,7,0, 10,8,0, 10,9,0, 10,10,0, 10,11,0, 10,12,0, 10,13,0, 10,14,0, 10,15,0, 10,20,0, 10,21,0, 10,22,0, 10,23,0, 10,24,0, 10,25,0, 10,26,0, 10,27,0, 10,28,0, 10,29,0, 10,30,0, 10,31,0, 10,32,0, 10,33,0, 10,34,0, ],30,6,0,0,14,35,3,2,0),
	)
Net1_Subnet2_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,0],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(1,5+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	).to_cnf()
Net1_Subnet2_R = And(Net1_Subnet2_R1,Net1_Subnet2_R2,Net1_Subnet2_R3,)
Net1_Subnet2_Formula = And(Net1_Subnet2_C,Net1_Subnet2_DR,Net1_Subnet2_R)
# Net = 1 Subnet = 3 | Left -> Right [6,22] Top -> Bottom [0,18]
# Range R1(10,10,1,14)
# Range R2(18,18,1,14)
### Disable edges outside window
Edge_Net_Subnet1[0:6,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(7776)
Edge_Net_Subnet1[6:22,18:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(10368)
Edge_Net_Subnet1[22:85+1,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(82944)

### Consistency Constraints
Net1_Subnet3_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,0]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(6,22+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet3_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet1[x,y,z,trend,mask,3]), Edge_Net[x,y,z,trend,mask,0])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(6,22+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet3_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,2,trend,0,3],Xor(Edge_Net_Subnet1[x,y,2,trend,1,3],Edge_Net_Subnet1[x,y,2,trend,2,3])),And(~Edge_Net_Subnet1[x,y,2,trend,0,3],~Edge_Net_Subnet1[x,y,2,trend,1,3],~Edge_Net_Subnet1[x,y,2,trend,2,3]))for x in range(6,22+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet3_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,3,1,0,3],Xor(Edge_Net_Subnet1[x,y,3,1,1,3],Edge_Net_Subnet1[x,y,3,1,2,3])),And(~Edge_Net_Subnet1[x,y,3,1,0,3],~Edge_Net_Subnet1[x,y,3,1,1,3],~Edge_Net_Subnet1[x,y,3,1,2,3]))for x in range(6,22+1)])for y in range(0,18+1)]).to_cnf()
Net1_Subnet3_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,1,trend,2,3],Xor(Edge_Net_Subnet1[x,y,1,trend,0,3],Edge_Net_Subnet1[x,y,1,trend,1,3])),And(~Edge_Net_Subnet1[x,y,1,trend,2,3],~Edge_Net_Subnet1[x,y,1,trend,0,3],~Edge_Net_Subnet1[x,y,1,trend,1,3]))for x in range(6,22+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet3_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(6,22+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(3+1,7)]))for trend in range(0,1+1)])for x in range(6,22+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(6,22+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(3+1,7)]))for trend in range(0,1+1)])for x in range(6,22+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
).to_cnf()
Net1_Subnet3_C = And(Net1_Subnet3_C1, Net1_Subnet3_C2,Net1_Subnet3_C3_ME1_Mask,Net1_Subnet3_C4_MINT1_Mask,Net1_Subnet3_C5_AIL2GIL_Mask,Net1_Subnet3_C6,)
### Design Rules
Net1_Subnet3_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(6,22+1)])for y in range(0,18+1)])for mask in range(0,2+1)])
	).to_cnf()
Net1_Subnet3_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,3], ~Edge_Net_Subnet1[x-1,y,1,1,1,3]), And(Edge_Net_Subnet1[x+1,y,1,1,1,3], Edge_Net_Subnet1[x+2,y,1,1,1,3], Edge_Net_Subnet1[x+3,y,1,1,1,3], ))for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,3], ~Edge_Net_Subnet1[x+1,y,1,1,1,3]), And(Edge_Net_Subnet1[x-1,y,1,1,1,3], Edge_Net_Subnet1[x-2,y,1,1,1,3], Edge_Net_Subnet1[x-3,y,1,1,1,3], ))for x in range(6,22+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet3_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,3], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,3], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(6,22+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet3_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,3], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,3], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(6,22+1)])for y in range(3,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,3]), And(Edge_Net_Subnet1[x,y+1,1,0,0,3], Edge_Net_Subnet1[x,y+2,1,0,0,3], Edge_Net_Subnet1[x,y+3,1,0,0,3], ))for x in range(6,22+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,3], ~Edge_Net_Subnet1[x,y-1,1,0,0,3]), And(Edge_Net_Subnet1[x,y+1,1,0,0,3], Edge_Net_Subnet1[x,y+2,1,0,0,3], Edge_Net_Subnet1[x,y+3,1,0,0,3], ))for x in range(6,22+1)])for y in range(0+1,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,3], ~Edge_Net_Subnet1[x,y+1,1,0,0,3]), And(Edge_Net_Subnet1[x,y-1,1,0,0,3], Edge_Net_Subnet1[x,y-2,1,0,0,3], Edge_Net_Subnet1[x,y-3,1,0,0,3], ))for x in range(6,22+1)])for y in range(0+3,18+1)])
	).to_cnf()
Net1_Subnet3_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(6,22+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(6,22+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(6,22+1)])for y in range(0+3,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(6,22+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net1_Subnet3_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,3], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,3], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(6,22+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,3], ~Edge_Net_Subnet1[x-1,y,3,1,mask,3]), And(Edge_Net_Subnet1[x+1,y,3,1,mask,3], Edge_Net_Subnet1[x+2,y,3,1,mask,3], Edge_Net_Subnet1[x+3,y,3,1,mask,3], Edge_Net_Subnet1[x+4,y,3,1,mask,3], Edge_Net_Subnet1[x+5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,3], ~Edge_Net_Subnet1[x+1,y,3,1,mask,3]), And(Edge_Net_Subnet1[x-1,y,3,1,mask,3], Edge_Net_Subnet1[x-2,y,3,1,mask,3], Edge_Net_Subnet1[x-3,y,3,1,mask,3], Edge_Net_Subnet1[x-4,y,3,1,mask,3], Edge_Net_Subnet1[x-5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,3], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,3], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(3,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,3], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,3], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet3_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,3], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,3], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(6,22+1)])for y in range(2,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,3], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,3], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(6,22+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet3_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,3], ~Edge_Net_Subnet1[x-1,y,2,1,mask,3]), And(Edge_Net_Subnet1[x+1,y,2,1,mask,3], Edge_Net_Subnet1[x+2,y,2,1,mask,3], Edge_Net_Subnet1[x+3,y,2,1,mask,3], Edge_Net_Subnet1[x+4,y,2,1,mask,3], Edge_Net_Subnet1[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,3], ~Edge_Net_Subnet1[x+1,y,2,1,mask,3]), And(Edge_Net_Subnet1[x-1,y,2,1,mask,3], Edge_Net_Subnet1[x-2,y,2,1,mask,3], Edge_Net_Subnet1[x-3,y,2,1,mask,3], Edge_Net_Subnet1[x-4,y,2,1,mask,3], Edge_Net_Subnet1[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,3], And(Edge_Net_Subnet1[x-1,y,2,1,mask,3], Edge_Net_Subnet1[x-2,y,2,1,mask,3], Edge_Net_Subnet1[x-3,y,2,1,mask,3], Edge_Net_Subnet1[x-4,y,2,1,mask,3], Edge_Net_Subnet1[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(6,6+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,3], And(Edge_Net_Subnet1[x+1,y,2,1,mask,3], Edge_Net_Subnet1[x+2,y,2,1,mask,3], Edge_Net_Subnet1[x+3,y,2,1,mask,3], Edge_Net_Subnet1[x+4,y,2,1,mask,3], Edge_Net_Subnet1[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(22-1,6)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,3], ~Edge_Net_Subnet1[x,y-1,2,0,mask,3]), And(Edge_Net_Subnet1[x,y+1,2,0,mask,3], Edge_Net_Subnet1[x,y+2,2,0,mask,3], Edge_Net_Subnet1[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0+1,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,3], ~Edge_Net_Subnet1[x,y+1,2,0,mask,3]), And(Edge_Net_Subnet1[x,y-1,2,0,mask,3], Edge_Net_Subnet1[x,y-2,2,0,mask,3], Edge_Net_Subnet1[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0+3,18+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,3], And(Edge_Net_Subnet1[x,y+1,2,0,mask,3], Edge_Net_Subnet1[x,y+2,2,0,mask,3], Edge_Net_Subnet1[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,3], And(Edge_Net_Subnet1[x,y-1,2,0,mask,3], Edge_Net_Subnet1[x,y-2,2,0,mask,3], Edge_Net_Subnet1[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(18,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,3], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,3], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(6,22+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet3_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,3], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,3], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet3_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,3], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(6,22+1)])for y in range(2,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,3], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(6,22+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,3], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(4,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,3], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,3], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,3], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(6,22+1)])for y in range(3,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,3], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,3], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(4,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,3], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,3], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(6,22+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,3], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,3], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,3], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,3], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,22+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet3_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,3], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,3], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,22+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet3_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,3], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,3], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,22+1)])for y in range(2,18+1)]),
	).to_cnf()
Net1_Subnet3_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,3], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,22+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,3], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,22+1)])for y in range(2,18+1)]),
	).to_cnf()
Net1_Subnet3_DR = And(Net1_Subnet3_DR_Trend, Net1_Subnet3_DR_GIL_HorMinWidth,Net1_Subnet3_DR_GIL_HorMinSpacing,Net1_Subnet3_DR_GIL_VerMinSpacing,Net1_Subnet3_DR_AIL2_VerMinWidth,Net1_Subnet3_DR_AIL2_VerMinSpacing,Net1_Subnet3_DR_VerAIL2_HorMinSpacing,Net1_Subnet3_DR_MINT1AB_HorMinWidth,Net1_Subnet3_DR_MINT1_SameMask_VerMinSpacing,Net1_Subnet3_DR_MINT1_SameMask_HorMinSpacing,Net1_Subnet3_DR_MINT1_DiffMask_VerMinSpacing,Net1_Subnet3_DR_MINT1_DiffMask_HorMinSpacing,Net1_Subnet3_DR_M1AB_MinWidth,Net1_Subnet3_DR_HorM1_DiffMask_HorMinSpacing,Net1_Subnet3_DR_HorM1_SameMask_HorMinSpacing,Net1_Subnet3_DR_VerM1_DiffMask_VerMinSpacing,Net1_Subnet3_DR_VerM1_SameMask_VerMinSpacing,Net1_Subnet3_DR_HorM1_DiffMask_VerMinSpacing,Net1_Subnet3_DR_HorM1_SameMask_VerMinSpacing,Net1_Subnet3_DR_VerM1_DiffMask_HorMinSpacing,Net1_Subnet3_DR_VerM1_SameMask_HorMinSpacing,Net1_Subnet3_DR_V0_HorMinSpacing,Net1_Subnet3_DR_V1_HorMinSpacing,Net1_Subnet3_DR_V0_VerMinSpacing,Net1_Subnet3_DR_V1_VerMinSpacing,)
### Routability Constraints
Net1_Subnet3_R1 = And(
	RConstraints.R1(Edge_Net_Subnet1,[10,1,0,0, 10,2,0,0, 10,3,0,0, 10,4,0,0, 10,5,0,0, 10,6,0,0, 10,7,0,0, 10,8,0,0, 10,9,0,0, 10,10,0,0, 10,11,0,0, 10,12,0,0, 10,13,0,0, 10,14,0,0, ],14,6,0,1,22,18,3,3),
	RConstraints.R1(Edge_Net_Subnet1,[18,1,0,0, 18,2,0,0, 18,3,0,0, 18,4,0,0, 18,5,0,0, 18,6,0,0, 18,7,0,0, 18,8,0,0, 18,9,0,0, 18,10,0,0, 18,11,0,0, 18,12,0,0, 18,13,0,0, 18,14,0,0, ],14,6,0,1,22,18,3,3),
	).to_cnf()
Net1_Subnet3_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet1,Edge,Edge_Net,[10,1,0, 10,2,0, 10,3,0, 10,4,0, 10,5,0, 10,6,0, 10,7,0, 10,8,0, 10,9,0, 10,10,0, 10,11,0, 10,12,0, 10,13,0, 10,14,0, 10,15,0, 18,1,0, 18,2,0, 18,3,0, 18,4,0, 18,5,0, 18,6,0, 18,7,0, 18,8,0, 18,9,0, 18,10,0, 18,11,0, 18,12,0, 18,13,0, 18,14,0, 18,15,0, ],30,6,0,0,22,18,3,3,0),
	)
Net1_Subnet3_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,0],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(1,5+1)])for x in range(6,22+1)])for y in range(0,18+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	).to_cnf()
Net1_Subnet3_R = And(Net1_Subnet3_R1,Net1_Subnet3_R2,Net1_Subnet3_R3,)
Net1_Subnet3_Formula = And(Net1_Subnet3_C,Net1_Subnet3_DR,Net1_Subnet3_R)
# Net = 1 Subnet = 4 | Left -> Right [14,22] Top -> Bottom [0,35]
# Range R1(18,18,1,14)
# Range R2(18,18,20,33)
### Disable edges outside window
Edge_Net_Subnet1[0:14,0:35+1,0:3+1,0:2+1,0:2+1,4]=exprzeros(18144)
Edge_Net_Subnet1[22:85+1,0:35+1,0:3+1,0:2+1,0:2+1,4]=exprzeros(82944)

### Consistency Constraints
Net1_Subnet4_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,0]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(14,22+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet4_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet1[x,y,z,trend,mask,4]), Edge_Net[x,y,z,trend,mask,0])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(14,22+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet4_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,2,trend,0,4],Xor(Edge_Net_Subnet1[x,y,2,trend,1,4],Edge_Net_Subnet1[x,y,2,trend,2,4])),And(~Edge_Net_Subnet1[x,y,2,trend,0,4],~Edge_Net_Subnet1[x,y,2,trend,1,4],~Edge_Net_Subnet1[x,y,2,trend,2,4]))for x in range(14,22+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet4_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,3,1,0,4],Xor(Edge_Net_Subnet1[x,y,3,1,1,4],Edge_Net_Subnet1[x,y,3,1,2,4])),And(~Edge_Net_Subnet1[x,y,3,1,0,4],~Edge_Net_Subnet1[x,y,3,1,1,4],~Edge_Net_Subnet1[x,y,3,1,2,4]))for x in range(14,22+1)])for y in range(0,35+1)]).to_cnf()
Net1_Subnet4_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,1,trend,2,4],Xor(Edge_Net_Subnet1[x,y,1,trend,0,4],Edge_Net_Subnet1[x,y,1,trend,1,4])),And(~Edge_Net_Subnet1[x,y,1,trend,2,4],~Edge_Net_Subnet1[x,y,1,trend,0,4],~Edge_Net_Subnet1[x,y,1,trend,1,4]))for x in range(14,22+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet4_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,4], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(0,4)]))for trend in range(0,1+1)])for x in range(14,22+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,4], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(4+1,7)]))for trend in range(0,1+1)])for x in range(14,22+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,4], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(0,4)]))for trend in range(0,1+1)])for x in range(14,22+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,4], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(4+1,7)]))for trend in range(0,1+1)])for x in range(14,22+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net1_Subnet4_C = And(Net1_Subnet4_C1, Net1_Subnet4_C2,Net1_Subnet4_C3_ME1_Mask,Net1_Subnet4_C4_MINT1_Mask,Net1_Subnet4_C5_AIL2GIL_Mask,Net1_Subnet4_C6,)
### Design Rules
Net1_Subnet4_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(14,22+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net1_Subnet4_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,4], ~Edge_Net_Subnet1[x-1,y,1,1,1,4]), And(Edge_Net_Subnet1[x+1,y,1,1,1,4], Edge_Net_Subnet1[x+2,y,1,1,1,4], Edge_Net_Subnet1[x+3,y,1,1,1,4], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,4], ~Edge_Net_Subnet1[x+1,y,1,1,1,4]), And(Edge_Net_Subnet1[x-1,y,1,1,1,4], Edge_Net_Subnet1[x-2,y,1,1,1,4], Edge_Net_Subnet1[x-3,y,1,1,1,4], ))for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet4_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,4], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,4], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet4_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,4], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(14,22+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,4], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(14,22+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet4_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,4]), And(Edge_Net_Subnet1[x,y+1,1,0,0,4], Edge_Net_Subnet1[x,y+2,1,0,0,4], Edge_Net_Subnet1[x,y+3,1,0,0,4], ))for x in range(14,22+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,4]), And(Edge_Net_Subnet1[x,y-1,1,0,0,4], Edge_Net_Subnet1[x,y-2,1,0,0,4], Edge_Net_Subnet1[x,y-3,1,0,0,4], ))for x in range(14,22+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,4], ~Edge_Net_Subnet1[x,y-1,1,0,0,4]), And(Edge_Net_Subnet1[x,y+1,1,0,0,4], Edge_Net_Subnet1[x,y+2,1,0,0,4], Edge_Net_Subnet1[x,y+3,1,0,0,4], ))for x in range(14,22+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,4], ~Edge_Net_Subnet1[x,y+1,1,0,0,4]), And(Edge_Net_Subnet1[x,y-1,1,0,0,4], Edge_Net_Subnet1[x,y-2,1,0,0,4], Edge_Net_Subnet1[x,y-3,1,0,0,4], ))for x in range(14,22+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net1_Subnet4_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(14,22+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(14,22+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(14,22+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(14,22+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(14,22+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(14,22+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net1_Subnet4_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,4], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,4], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet4_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,4], ~Edge_Net_Subnet1[x-1,y,3,1,mask,4]), And(Edge_Net_Subnet1[x+1,y,3,1,mask,4], Edge_Net_Subnet1[x+2,y,3,1,mask,4], Edge_Net_Subnet1[x+3,y,3,1,mask,4], Edge_Net_Subnet1[x+4,y,3,1,mask,4], Edge_Net_Subnet1[x+5,y,3,1,mask,4], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,4], ~Edge_Net_Subnet1[x+1,y,3,1,mask,4]), And(Edge_Net_Subnet1[x-1,y,3,1,mask,4], Edge_Net_Subnet1[x-2,y,3,1,mask,4], Edge_Net_Subnet1[x-3,y,3,1,mask,4], Edge_Net_Subnet1[x-4,y,3,1,mask,4], Edge_Net_Subnet1[x-5,y,3,1,mask,4], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet4_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,4], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,4], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet4_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,4], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,4], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet4_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,4], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(14,22+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,4], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(14,22+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet4_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,4], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,4], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet4_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,4], ~Edge_Net_Subnet1[x-1,y,2,1,mask,4]), And(Edge_Net_Subnet1[x+1,y,2,1,mask,4], Edge_Net_Subnet1[x+2,y,2,1,mask,4], Edge_Net_Subnet1[x+3,y,2,1,mask,4], Edge_Net_Subnet1[x+4,y,2,1,mask,4], Edge_Net_Subnet1[x+5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,4], ~Edge_Net_Subnet1[x+1,y,2,1,mask,4]), And(Edge_Net_Subnet1[x-1,y,2,1,mask,4], Edge_Net_Subnet1[x-2,y,2,1,mask,4], Edge_Net_Subnet1[x-3,y,2,1,mask,4], Edge_Net_Subnet1[x-4,y,2,1,mask,4], Edge_Net_Subnet1[x-5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,4], And(Edge_Net_Subnet1[x-1,y,2,1,mask,4], Edge_Net_Subnet1[x-2,y,2,1,mask,4], Edge_Net_Subnet1[x-3,y,2,1,mask,4], Edge_Net_Subnet1[x-4,y,2,1,mask,4], Edge_Net_Subnet1[x-5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(14,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,4], And(Edge_Net_Subnet1[x+1,y,2,1,mask,4], Edge_Net_Subnet1[x+2,y,2,1,mask,4], Edge_Net_Subnet1[x+3,y,2,1,mask,4], Edge_Net_Subnet1[x+4,y,2,1,mask,4], Edge_Net_Subnet1[x+5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(22-1,14)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,4], ~Edge_Net_Subnet1[x,y-1,2,0,mask,4]), And(Edge_Net_Subnet1[x,y+1,2,0,mask,4], Edge_Net_Subnet1[x,y+2,2,0,mask,4], Edge_Net_Subnet1[x,y+3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,4], ~Edge_Net_Subnet1[x,y+1,2,0,mask,4]), And(Edge_Net_Subnet1[x,y-1,2,0,mask,4], Edge_Net_Subnet1[x,y-2,2,0,mask,4], Edge_Net_Subnet1[x,y-3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,4], And(Edge_Net_Subnet1[x,y+1,2,0,mask,4], Edge_Net_Subnet1[x,y+2,2,0,mask,4], Edge_Net_Subnet1[x,y+3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,4], And(Edge_Net_Subnet1[x,y-1,2,0,mask,4], Edge_Net_Subnet1[x,y-2,2,0,mask,4], Edge_Net_Subnet1[x,y-3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(35,35+1)]),
	).to_cnf()
Net1_Subnet4_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,4], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,4], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet4_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,4], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,4], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet4_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,4], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(14,22+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,4], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(14,22+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net1_Subnet4_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,4], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,4], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net1_Subnet4_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,4], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(14,22+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,4], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(14,22+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet4_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,4], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,4], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(4,35+1)]),
	).to_cnf()
Net1_Subnet4_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,4], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,4], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet4_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,4], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,4], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet4_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,4], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,4], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet4_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,4], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,4], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet4_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,4], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,4], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet4_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,4], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,4], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet4_DR = And(Net1_Subnet4_DR_Trend, Net1_Subnet4_DR_GIL_HorMinWidth,Net1_Subnet4_DR_GIL_HorMinSpacing,Net1_Subnet4_DR_GIL_VerMinSpacing,Net1_Subnet4_DR_AIL2_VerMinWidth,Net1_Subnet4_DR_AIL2_VerMinSpacing,Net1_Subnet4_DR_VerAIL2_HorMinSpacing,Net1_Subnet4_DR_MINT1AB_HorMinWidth,Net1_Subnet4_DR_MINT1_SameMask_VerMinSpacing,Net1_Subnet4_DR_MINT1_SameMask_HorMinSpacing,Net1_Subnet4_DR_MINT1_DiffMask_VerMinSpacing,Net1_Subnet4_DR_MINT1_DiffMask_HorMinSpacing,Net1_Subnet4_DR_M1AB_MinWidth,Net1_Subnet4_DR_HorM1_DiffMask_HorMinSpacing,Net1_Subnet4_DR_HorM1_SameMask_HorMinSpacing,Net1_Subnet4_DR_VerM1_DiffMask_VerMinSpacing,Net1_Subnet4_DR_VerM1_SameMask_VerMinSpacing,Net1_Subnet4_DR_HorM1_DiffMask_VerMinSpacing,Net1_Subnet4_DR_HorM1_SameMask_VerMinSpacing,Net1_Subnet4_DR_VerM1_DiffMask_HorMinSpacing,Net1_Subnet4_DR_VerM1_SameMask_HorMinSpacing,Net1_Subnet4_DR_V0_HorMinSpacing,Net1_Subnet4_DR_V1_HorMinSpacing,Net1_Subnet4_DR_V0_VerMinSpacing,Net1_Subnet4_DR_V1_VerMinSpacing,)
### Routability Constraints
Net1_Subnet4_R1 = And(
	RConstraints.R1(Edge_Net_Subnet1,[18,1,0,0, 18,2,0,0, 18,3,0,0, 18,4,0,0, 18,5,0,0, 18,6,0,0, 18,7,0,0, 18,8,0,0, 18,9,0,0, 18,10,0,0, 18,11,0,0, 18,12,0,0, 18,13,0,0, 18,14,0,0, ],14,14,0,1,22,35,3,4),
	RConstraints.R1(Edge_Net_Subnet1,[18,20,0,0, 18,21,0,0, 18,22,0,0, 18,23,0,0, 18,24,0,0, 18,25,0,0, 18,26,0,0, 18,27,0,0, 18,28,0,0, 18,29,0,0, 18,30,0,0, 18,31,0,0, 18,32,0,0, 18,33,0,0, ],14,14,0,1,22,35,3,4),
	).to_cnf()
Net1_Subnet4_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet1,Edge,Edge_Net,[18,1,0, 18,2,0, 18,3,0, 18,4,0, 18,5,0, 18,6,0, 18,7,0, 18,8,0, 18,9,0, 18,10,0, 18,11,0, 18,12,0, 18,13,0, 18,14,0, 18,15,0, 18,20,0, 18,21,0, 18,22,0, 18,23,0, 18,24,0, 18,25,0, 18,26,0, 18,27,0, 18,28,0, 18,29,0, 18,30,0, 18,31,0, 18,32,0, 18,33,0, 18,34,0, ],30,14,0,0,22,35,3,4,0),
	)
Net1_Subnet4_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,0],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(1,5+1)])for x in range(14,22+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	).to_cnf()
Net1_Subnet4_R = And(Net1_Subnet4_R1,Net1_Subnet4_R2,Net1_Subnet4_R3,)
Net1_Subnet4_Formula = And(Net1_Subnet4_C,Net1_Subnet4_DR,Net1_Subnet4_R)
# Net = 1 Subnet = 5 | Left -> Right [14,26] Top -> Bottom [0,18]
# Range R1(18,18,1,14)
# Range R2(22,22,1,10)
### Disable edges outside window
Edge_Net_Subnet1[0:14,0:35+1,0:3+1,0:2+1,0:2+1,5]=exprzeros(18144)
Edge_Net_Subnet1[14:26,18:35+1,0:3+1,0:2+1,0:2+1,5]=exprzeros(7776)
Edge_Net_Subnet1[26:85+1,0:35+1,0:3+1,0:2+1,0:2+1,5]=exprzeros(77760)

### Consistency Constraints
Net1_Subnet5_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,0]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(14,26+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet5_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet1[x,y,z,trend,mask,5]), Edge_Net[x,y,z,trend,mask,0])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(14,26+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet5_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,2,trend,0,5],Xor(Edge_Net_Subnet1[x,y,2,trend,1,5],Edge_Net_Subnet1[x,y,2,trend,2,5])),And(~Edge_Net_Subnet1[x,y,2,trend,0,5],~Edge_Net_Subnet1[x,y,2,trend,1,5],~Edge_Net_Subnet1[x,y,2,trend,2,5]))for x in range(14,26+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet5_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,3,1,0,5],Xor(Edge_Net_Subnet1[x,y,3,1,1,5],Edge_Net_Subnet1[x,y,3,1,2,5])),And(~Edge_Net_Subnet1[x,y,3,1,0,5],~Edge_Net_Subnet1[x,y,3,1,1,5],~Edge_Net_Subnet1[x,y,3,1,2,5]))for x in range(14,26+1)])for y in range(0,18+1)]).to_cnf()
Net1_Subnet5_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,1,trend,2,5],Xor(Edge_Net_Subnet1[x,y,1,trend,0,5],Edge_Net_Subnet1[x,y,1,trend,1,5])),And(~Edge_Net_Subnet1[x,y,1,trend,2,5],~Edge_Net_Subnet1[x,y,1,trend,0,5],~Edge_Net_Subnet1[x,y,1,trend,1,5]))for x in range(14,26+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet5_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,5], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(0,5)]))for trend in range(0,1+1)])for x in range(14,26+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,5], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(5+1,7)]))for trend in range(0,1+1)])for x in range(14,26+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,5], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(0,5)]))for trend in range(0,1+1)])for x in range(14,26+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,5], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(5+1,7)]))for trend in range(0,1+1)])for x in range(14,26+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
).to_cnf()
Net1_Subnet5_C = And(Net1_Subnet5_C1, Net1_Subnet5_C2,Net1_Subnet5_C3_ME1_Mask,Net1_Subnet5_C4_MINT1_Mask,Net1_Subnet5_C5_AIL2GIL_Mask,Net1_Subnet5_C6,)
### Design Rules
Net1_Subnet5_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(14,26+1)])for y in range(0,18+1)])for mask in range(0,2+1)])
	).to_cnf()
Net1_Subnet5_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,5], ~Edge_Net_Subnet1[x-1,y,1,1,1,5]), And(Edge_Net_Subnet1[x+1,y,1,1,1,5], Edge_Net_Subnet1[x+2,y,1,1,1,5], Edge_Net_Subnet1[x+3,y,1,1,1,5], ))for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,5], ~Edge_Net_Subnet1[x+1,y,1,1,1,5]), And(Edge_Net_Subnet1[x-1,y,1,1,1,5], Edge_Net_Subnet1[x-2,y,1,1,1,5], Edge_Net_Subnet1[x-3,y,1,1,1,5], ))for x in range(14,26+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet5_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,5], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,5], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(14,26+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet5_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,5], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,5], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(14,26+1)])for y in range(3,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,5]), And(Edge_Net_Subnet1[x,y+1,1,0,0,5], Edge_Net_Subnet1[x,y+2,1,0,0,5], Edge_Net_Subnet1[x,y+3,1,0,0,5], ))for x in range(14,26+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,5], ~Edge_Net_Subnet1[x,y-1,1,0,0,5]), And(Edge_Net_Subnet1[x,y+1,1,0,0,5], Edge_Net_Subnet1[x,y+2,1,0,0,5], Edge_Net_Subnet1[x,y+3,1,0,0,5], ))for x in range(14,26+1)])for y in range(0+1,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,5], ~Edge_Net_Subnet1[x,y+1,1,0,0,5]), And(Edge_Net_Subnet1[x,y-1,1,0,0,5], Edge_Net_Subnet1[x,y-2,1,0,0,5], Edge_Net_Subnet1[x,y-3,1,0,0,5], ))for x in range(14,26+1)])for y in range(0+3,18+1)])
	).to_cnf()
Net1_Subnet5_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,5], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(14,26+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,5], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(14,26+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,5], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(14,26+1)])for y in range(0+3,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,5], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(14,26+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net1_Subnet5_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,5], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,5], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(14,26+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,5], ~Edge_Net_Subnet1[x-1,y,3,1,mask,5]), And(Edge_Net_Subnet1[x+1,y,3,1,mask,5], Edge_Net_Subnet1[x+2,y,3,1,mask,5], Edge_Net_Subnet1[x+3,y,3,1,mask,5], Edge_Net_Subnet1[x+4,y,3,1,mask,5], Edge_Net_Subnet1[x+5,y,3,1,mask,5], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,5], ~Edge_Net_Subnet1[x+1,y,3,1,mask,5]), And(Edge_Net_Subnet1[x-1,y,3,1,mask,5], Edge_Net_Subnet1[x-2,y,3,1,mask,5], Edge_Net_Subnet1[x-3,y,3,1,mask,5], Edge_Net_Subnet1[x-4,y,3,1,mask,5], Edge_Net_Subnet1[x-5,y,3,1,mask,5], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,5], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,5], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(3,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,5], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,5], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet5_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,5], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,5], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(14,26+1)])for y in range(2,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,5], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,5], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(14,26+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet5_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,5], ~Edge_Net_Subnet1[x-1,y,2,1,mask,5]), And(Edge_Net_Subnet1[x+1,y,2,1,mask,5], Edge_Net_Subnet1[x+2,y,2,1,mask,5], Edge_Net_Subnet1[x+3,y,2,1,mask,5], Edge_Net_Subnet1[x+4,y,2,1,mask,5], Edge_Net_Subnet1[x+5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,5], ~Edge_Net_Subnet1[x+1,y,2,1,mask,5]), And(Edge_Net_Subnet1[x-1,y,2,1,mask,5], Edge_Net_Subnet1[x-2,y,2,1,mask,5], Edge_Net_Subnet1[x-3,y,2,1,mask,5], Edge_Net_Subnet1[x-4,y,2,1,mask,5], Edge_Net_Subnet1[x-5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,5], And(Edge_Net_Subnet1[x-1,y,2,1,mask,5], Edge_Net_Subnet1[x-2,y,2,1,mask,5], Edge_Net_Subnet1[x-3,y,2,1,mask,5], Edge_Net_Subnet1[x-4,y,2,1,mask,5], Edge_Net_Subnet1[x-5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(14,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,5], And(Edge_Net_Subnet1[x+1,y,2,1,mask,5], Edge_Net_Subnet1[x+2,y,2,1,mask,5], Edge_Net_Subnet1[x+3,y,2,1,mask,5], Edge_Net_Subnet1[x+4,y,2,1,mask,5], Edge_Net_Subnet1[x+5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(26-1,14)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,5], ~Edge_Net_Subnet1[x,y-1,2,0,mask,5]), And(Edge_Net_Subnet1[x,y+1,2,0,mask,5], Edge_Net_Subnet1[x,y+2,2,0,mask,5], Edge_Net_Subnet1[x,y+3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0+1,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,5], ~Edge_Net_Subnet1[x,y+1,2,0,mask,5]), And(Edge_Net_Subnet1[x,y-1,2,0,mask,5], Edge_Net_Subnet1[x,y-2,2,0,mask,5], Edge_Net_Subnet1[x,y-3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0+3,18+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,5], And(Edge_Net_Subnet1[x,y+1,2,0,mask,5], Edge_Net_Subnet1[x,y+2,2,0,mask,5], Edge_Net_Subnet1[x,y+3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,5], And(Edge_Net_Subnet1[x,y-1,2,0,mask,5], Edge_Net_Subnet1[x,y-2,2,0,mask,5], Edge_Net_Subnet1[x,y-3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(18,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,5], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,5], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(14,26+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet5_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,5], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,5], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet5_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,5], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(14,26+1)])for y in range(2,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,5], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(14,26+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,5], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(4,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,5], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,5], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,5], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(14,26+1)])for y in range(3,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,5], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,5], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(4,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,5], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,5], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(14,26+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,5], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,5], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,5], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,5], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,26+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet5_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,5], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,5], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,26+1)])for y in range(0,18+1)])
	).to_cnf()
Net1_Subnet5_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,5], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,5], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,26+1)])for y in range(2,18+1)]),
	).to_cnf()
Net1_Subnet5_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,5], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,26+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,5], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,26+1)])for y in range(2,18+1)]),
	).to_cnf()
Net1_Subnet5_DR = And(Net1_Subnet5_DR_Trend, Net1_Subnet5_DR_GIL_HorMinWidth,Net1_Subnet5_DR_GIL_HorMinSpacing,Net1_Subnet5_DR_GIL_VerMinSpacing,Net1_Subnet5_DR_AIL2_VerMinWidth,Net1_Subnet5_DR_AIL2_VerMinSpacing,Net1_Subnet5_DR_VerAIL2_HorMinSpacing,Net1_Subnet5_DR_MINT1AB_HorMinWidth,Net1_Subnet5_DR_MINT1_SameMask_VerMinSpacing,Net1_Subnet5_DR_MINT1_SameMask_HorMinSpacing,Net1_Subnet5_DR_MINT1_DiffMask_VerMinSpacing,Net1_Subnet5_DR_MINT1_DiffMask_HorMinSpacing,Net1_Subnet5_DR_M1AB_MinWidth,Net1_Subnet5_DR_HorM1_DiffMask_HorMinSpacing,Net1_Subnet5_DR_HorM1_SameMask_HorMinSpacing,Net1_Subnet5_DR_VerM1_DiffMask_VerMinSpacing,Net1_Subnet5_DR_VerM1_SameMask_VerMinSpacing,Net1_Subnet5_DR_HorM1_DiffMask_VerMinSpacing,Net1_Subnet5_DR_HorM1_SameMask_VerMinSpacing,Net1_Subnet5_DR_VerM1_DiffMask_HorMinSpacing,Net1_Subnet5_DR_VerM1_SameMask_HorMinSpacing,Net1_Subnet5_DR_V0_HorMinSpacing,Net1_Subnet5_DR_V1_HorMinSpacing,Net1_Subnet5_DR_V0_VerMinSpacing,Net1_Subnet5_DR_V1_VerMinSpacing,)
### Routability Constraints
Net1_Subnet5_R1 = And(
	RConstraints.R1(Edge_Net_Subnet1,[18,1,0,0, 18,2,0,0, 18,3,0,0, 18,4,0,0, 18,5,0,0, 18,6,0,0, 18,7,0,0, 18,8,0,0, 18,9,0,0, 18,10,0,0, 18,11,0,0, 18,12,0,0, 18,13,0,0, 18,14,0,0, ],14,14,0,1,26,18,3,5),
	RConstraints.R1(Edge_Net_Subnet1,[22,1,0,0, 22,2,0,0, 22,3,0,0, 22,4,0,0, 22,5,0,0, 22,6,0,0, 22,7,0,0, 22,8,0,0, 22,9,0,0, 22,10,0,0, ],10,14,0,1,26,18,3,5),
	).to_cnf()
Net1_Subnet5_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet1,Edge,Edge_Net,[18,1,0, 18,2,0, 18,3,0, 18,4,0, 18,5,0, 18,6,0, 18,7,0, 18,8,0, 18,9,0, 18,10,0, 18,11,0, 18,12,0, 18,13,0, 18,14,0, 18,15,0, 22,1,0, 22,2,0, 22,3,0, 22,4,0, 22,5,0, 22,6,0, 22,7,0, 22,8,0, 22,9,0, 22,10,0, 22,11,0, ],26,14,0,0,26,18,3,5,0),
	)
Net1_Subnet5_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,0],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(1,5+1)])for x in range(14,26+1)])for y in range(0,18+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	).to_cnf()
Net1_Subnet5_R = And(Net1_Subnet5_R1,Net1_Subnet5_R2,Net1_Subnet5_R3,)
Net1_Subnet5_Formula = And(Net1_Subnet5_C,Net1_Subnet5_DR,Net1_Subnet5_R)
# Net = 1 Subnet = 6 | Left -> Right [18,26] Top -> Bottom [0,35]
# Range R1(22,22,1,10)
# Range R2(22,22,24,33)
### Disable edges outside window
Edge_Net_Subnet1[0:18,0:35+1,0:3+1,0:2+1,0:2+1,6]=exprzeros(23328)
Edge_Net_Subnet1[26:85+1,0:35+1,0:3+1,0:2+1,0:2+1,6]=exprzeros(77760)

### Consistency Constraints
Net1_Subnet6_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,0]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(18,26+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet6_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet1[x,y,z,trend,mask,6]), Edge_Net[x,y,z,trend,mask,0])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(18,26+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet6_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,2,trend,0,6],Xor(Edge_Net_Subnet1[x,y,2,trend,1,6],Edge_Net_Subnet1[x,y,2,trend,2,6])),And(~Edge_Net_Subnet1[x,y,2,trend,0,6],~Edge_Net_Subnet1[x,y,2,trend,1,6],~Edge_Net_Subnet1[x,y,2,trend,2,6]))for x in range(18,26+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet6_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,3,1,0,6],Xor(Edge_Net_Subnet1[x,y,3,1,1,6],Edge_Net_Subnet1[x,y,3,1,2,6])),And(~Edge_Net_Subnet1[x,y,3,1,0,6],~Edge_Net_Subnet1[x,y,3,1,1,6],~Edge_Net_Subnet1[x,y,3,1,2,6]))for x in range(18,26+1)])for y in range(0,35+1)]).to_cnf()
Net1_Subnet6_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,1,trend,2,6],Xor(Edge_Net_Subnet1[x,y,1,trend,0,6],Edge_Net_Subnet1[x,y,1,trend,1,6])),And(~Edge_Net_Subnet1[x,y,1,trend,2,6],~Edge_Net_Subnet1[x,y,1,trend,0,6],~Edge_Net_Subnet1[x,y,1,trend,1,6]))for x in range(18,26+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet6_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,6], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(0,6)]))for trend in range(0,1+1)])for x in range(18,26+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,6], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(0,6)]))for trend in range(0,1+1)])for x in range(18,26+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net1_Subnet6_C = And(Net1_Subnet6_C1, Net1_Subnet6_C2,Net1_Subnet6_C3_ME1_Mask,Net1_Subnet6_C4_MINT1_Mask,Net1_Subnet6_C5_AIL2GIL_Mask,Net1_Subnet6_C6,)
### Design Rules
Net1_Subnet6_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(18,26+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net1_Subnet6_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,6], ~Edge_Net_Subnet1[x-1,y,1,1,1,6]), And(Edge_Net_Subnet1[x+1,y,1,1,1,6], Edge_Net_Subnet1[x+2,y,1,1,1,6], Edge_Net_Subnet1[x+3,y,1,1,1,6], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,6], ~Edge_Net_Subnet1[x+1,y,1,1,1,6]), And(Edge_Net_Subnet1[x-1,y,1,1,1,6], Edge_Net_Subnet1[x-2,y,1,1,1,6], Edge_Net_Subnet1[x-3,y,1,1,1,6], ))for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet6_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,6], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,6], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet6_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,6], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(18,26+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,6], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(18,26+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet6_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,6]), And(Edge_Net_Subnet1[x,y+1,1,0,0,6], Edge_Net_Subnet1[x,y+2,1,0,0,6], Edge_Net_Subnet1[x,y+3,1,0,0,6], ))for x in range(18,26+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,6]), And(Edge_Net_Subnet1[x,y-1,1,0,0,6], Edge_Net_Subnet1[x,y-2,1,0,0,6], Edge_Net_Subnet1[x,y-3,1,0,0,6], ))for x in range(18,26+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,6], ~Edge_Net_Subnet1[x,y-1,1,0,0,6]), And(Edge_Net_Subnet1[x,y+1,1,0,0,6], Edge_Net_Subnet1[x,y+2,1,0,0,6], Edge_Net_Subnet1[x,y+3,1,0,0,6], ))for x in range(18,26+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,6], ~Edge_Net_Subnet1[x,y+1,1,0,0,6]), And(Edge_Net_Subnet1[x,y-1,1,0,0,6], Edge_Net_Subnet1[x,y-2,1,0,0,6], Edge_Net_Subnet1[x,y-3,1,0,0,6], ))for x in range(18,26+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net1_Subnet6_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,6], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(18,26+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,6], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(18,26+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,6], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(18,26+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,6], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(18,26+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,6], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(18,26+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,6], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(18,26+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net1_Subnet6_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,6], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,6], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet6_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,6], ~Edge_Net_Subnet1[x-1,y,3,1,mask,6]), And(Edge_Net_Subnet1[x+1,y,3,1,mask,6], Edge_Net_Subnet1[x+2,y,3,1,mask,6], Edge_Net_Subnet1[x+3,y,3,1,mask,6], Edge_Net_Subnet1[x+4,y,3,1,mask,6], Edge_Net_Subnet1[x+5,y,3,1,mask,6], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,6], ~Edge_Net_Subnet1[x+1,y,3,1,mask,6]), And(Edge_Net_Subnet1[x-1,y,3,1,mask,6], Edge_Net_Subnet1[x-2,y,3,1,mask,6], Edge_Net_Subnet1[x-3,y,3,1,mask,6], Edge_Net_Subnet1[x-4,y,3,1,mask,6], Edge_Net_Subnet1[x-5,y,3,1,mask,6], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet6_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,6], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,6], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet6_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,6], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,6], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet6_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,6], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(18,26+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,6], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(18,26+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet6_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,6], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,6], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet6_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,6], ~Edge_Net_Subnet1[x-1,y,2,1,mask,6]), And(Edge_Net_Subnet1[x+1,y,2,1,mask,6], Edge_Net_Subnet1[x+2,y,2,1,mask,6], Edge_Net_Subnet1[x+3,y,2,1,mask,6], Edge_Net_Subnet1[x+4,y,2,1,mask,6], Edge_Net_Subnet1[x+5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,6], ~Edge_Net_Subnet1[x+1,y,2,1,mask,6]), And(Edge_Net_Subnet1[x-1,y,2,1,mask,6], Edge_Net_Subnet1[x-2,y,2,1,mask,6], Edge_Net_Subnet1[x-3,y,2,1,mask,6], Edge_Net_Subnet1[x-4,y,2,1,mask,6], Edge_Net_Subnet1[x-5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,6], And(Edge_Net_Subnet1[x-1,y,2,1,mask,6], Edge_Net_Subnet1[x-2,y,2,1,mask,6], Edge_Net_Subnet1[x-3,y,2,1,mask,6], Edge_Net_Subnet1[x-4,y,2,1,mask,6], Edge_Net_Subnet1[x-5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(18,18+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,6], And(Edge_Net_Subnet1[x+1,y,2,1,mask,6], Edge_Net_Subnet1[x+2,y,2,1,mask,6], Edge_Net_Subnet1[x+3,y,2,1,mask,6], Edge_Net_Subnet1[x+4,y,2,1,mask,6], Edge_Net_Subnet1[x+5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(26-1,18)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,6], ~Edge_Net_Subnet1[x,y-1,2,0,mask,6]), And(Edge_Net_Subnet1[x,y+1,2,0,mask,6], Edge_Net_Subnet1[x,y+2,2,0,mask,6], Edge_Net_Subnet1[x,y+3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,6], ~Edge_Net_Subnet1[x,y+1,2,0,mask,6]), And(Edge_Net_Subnet1[x,y-1,2,0,mask,6], Edge_Net_Subnet1[x,y-2,2,0,mask,6], Edge_Net_Subnet1[x,y-3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,6], And(Edge_Net_Subnet1[x,y+1,2,0,mask,6], Edge_Net_Subnet1[x,y+2,2,0,mask,6], Edge_Net_Subnet1[x,y+3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,6], And(Edge_Net_Subnet1[x,y-1,2,0,mask,6], Edge_Net_Subnet1[x,y-2,2,0,mask,6], Edge_Net_Subnet1[x,y-3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(35,35+1)]),
	).to_cnf()
Net1_Subnet6_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,6], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,6], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet6_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,6], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,6], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet6_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,6], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(18,26+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,6], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(18,26+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net1_Subnet6_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,6], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,6], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net1_Subnet6_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,6], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(18,26+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,6], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(18,26+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet6_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,6], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,6], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(4,35+1)]),
	).to_cnf()
Net1_Subnet6_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,6], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,6], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet6_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,6], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,6], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet6_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,6], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,6], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet6_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,6], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,6], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet6_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,6], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,6], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet6_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,6], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,6], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet6_DR = And(Net1_Subnet6_DR_Trend, Net1_Subnet6_DR_GIL_HorMinWidth,Net1_Subnet6_DR_GIL_HorMinSpacing,Net1_Subnet6_DR_GIL_VerMinSpacing,Net1_Subnet6_DR_AIL2_VerMinWidth,Net1_Subnet6_DR_AIL2_VerMinSpacing,Net1_Subnet6_DR_VerAIL2_HorMinSpacing,Net1_Subnet6_DR_MINT1AB_HorMinWidth,Net1_Subnet6_DR_MINT1_SameMask_VerMinSpacing,Net1_Subnet6_DR_MINT1_SameMask_HorMinSpacing,Net1_Subnet6_DR_MINT1_DiffMask_VerMinSpacing,Net1_Subnet6_DR_MINT1_DiffMask_HorMinSpacing,Net1_Subnet6_DR_M1AB_MinWidth,Net1_Subnet6_DR_HorM1_DiffMask_HorMinSpacing,Net1_Subnet6_DR_HorM1_SameMask_HorMinSpacing,Net1_Subnet6_DR_VerM1_DiffMask_VerMinSpacing,Net1_Subnet6_DR_VerM1_SameMask_VerMinSpacing,Net1_Subnet6_DR_HorM1_DiffMask_VerMinSpacing,Net1_Subnet6_DR_HorM1_SameMask_VerMinSpacing,Net1_Subnet6_DR_VerM1_DiffMask_HorMinSpacing,Net1_Subnet6_DR_VerM1_SameMask_HorMinSpacing,Net1_Subnet6_DR_V0_HorMinSpacing,Net1_Subnet6_DR_V1_HorMinSpacing,Net1_Subnet6_DR_V0_VerMinSpacing,Net1_Subnet6_DR_V1_VerMinSpacing,)
### Routability Constraints
Net1_Subnet6_R1 = And(
	RConstraints.R1(Edge_Net_Subnet1,[22,1,0,0, 22,2,0,0, 22,3,0,0, 22,4,0,0, 22,5,0,0, 22,6,0,0, 22,7,0,0, 22,8,0,0, 22,9,0,0, 22,10,0,0, ],10,18,0,1,26,35,3,6),
	RConstraints.R1(Edge_Net_Subnet1,[22,24,0,0, 22,25,0,0, 22,26,0,0, 22,27,0,0, 22,28,0,0, 22,29,0,0, 22,30,0,0, 22,31,0,0, 22,32,0,0, 22,33,0,0, ],10,18,0,1,26,35,3,6),
	).to_cnf()
Net1_Subnet6_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet1,Edge,Edge_Net,[22,1,0, 22,2,0, 22,3,0, 22,4,0, 22,5,0, 22,6,0, 22,7,0, 22,8,0, 22,9,0, 22,10,0, 22,11,0, 22,24,0, 22,25,0, 22,26,0, 22,27,0, 22,28,0, 22,29,0, 22,30,0, 22,31,0, 22,32,0, 22,33,0, 22,34,0, ],22,18,0,0,26,35,3,6,0),
	)
Net1_Subnet6_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,0],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(1,5+1)])for x in range(18,26+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	).to_cnf()
Net1_Subnet6_R = And(Net1_Subnet6_R1,Net1_Subnet6_R2,Net1_Subnet6_R3,)
Net1_Subnet6_Formula = And(Net1_Subnet6_C,Net1_Subnet6_DR,Net1_Subnet6_R)
# Net = 2 Subnet = 0 | Left -> Right [0,12] Top -> Bottom [0,35]
# Range R1(4,4,0,35)
# Range R2(8,8,0,35)
### Disable edges outside window
Edge_Net_Subnet2[12:85+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(95904)

### Consistency Constraints
Net2_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,0],Xor(Edge_Net_Subnet2[x,y,2,trend,1,0],Edge_Net_Subnet2[x,y,2,trend,2,0])),And(~Edge_Net_Subnet2[x,y,2,trend,0,0],~Edge_Net_Subnet2[x,y,2,trend,1,0],~Edge_Net_Subnet2[x,y,2,trend,2,0]))for x in range(0,12+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,0],Xor(Edge_Net_Subnet2[x,y,3,1,1,0],Edge_Net_Subnet2[x,y,3,1,2,0])),And(~Edge_Net_Subnet2[x,y,3,1,0,0],~Edge_Net_Subnet2[x,y,3,1,1,0],~Edge_Net_Subnet2[x,y,3,1,2,0]))for x in range(0,12+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,0],Xor(Edge_Net_Subnet2[x,y,1,trend,0,0],Edge_Net_Subnet2[x,y,1,trend,1,0])),And(~Edge_Net_Subnet2[x,y,1,trend,2,0],~Edge_Net_Subnet2[x,y,1,trend,0,0],~Edge_Net_Subnet2[x,y,1,trend,1,0]))for x in range(0,12+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet0_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,0], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0+1,10)]))for trend in range(0,1+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,0], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0+1,10)]))for trend in range(0,1+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet0_C = And(Net2_Subnet0_C1, Net2_Subnet0_C2,Net2_Subnet0_C3_ME1_Mask,Net2_Subnet0_C4_MINT1_Mask,Net2_Subnet0_C5_AIL2GIL_Mask,Net2_Subnet0_C6,)
### Design Rules
Net2_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(0,12+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge_Net_Subnet2[x-1,y,1,1,1,0]), And(Edge_Net_Subnet2[x+1,y,1,1,1,0], Edge_Net_Subnet2[x+2,y,1,1,1,0], Edge_Net_Subnet2[x+3,y,1,1,1,0], ))for x in range(1,12+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge_Net_Subnet2[x+1,y,1,1,1,0]), And(Edge_Net_Subnet2[x-1,y,1,1,1,0], Edge_Net_Subnet2[x-2,y,1,1,1,0], Edge_Net_Subnet2[x-3,y,1,1,1,0], ))for x in range(3,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(0,12+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(0,12+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0]), And(Edge_Net_Subnet2[x,y+1,1,0,0,0], Edge_Net_Subnet2[x,y+2,1,0,0,0], Edge_Net_Subnet2[x,y+3,1,0,0,0], ))for x in range(0,12+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0]), And(Edge_Net_Subnet2[x,y-1,1,0,0,0], Edge_Net_Subnet2[x,y-2,1,0,0,0], Edge_Net_Subnet2[x,y-3,1,0,0,0], ))for x in range(0,12+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge_Net_Subnet2[x,y-1,1,0,0,0]), And(Edge_Net_Subnet2[x,y+1,1,0,0,0], Edge_Net_Subnet2[x,y+2,1,0,0,0], Edge_Net_Subnet2[x,y+3,1,0,0,0], ))for x in range(0,12+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge_Net_Subnet2[x,y+1,1,0,0,0]), And(Edge_Net_Subnet2[x,y-1,1,0,0,0], Edge_Net_Subnet2[x,y-2,1,0,0,0], Edge_Net_Subnet2[x,y-3,1,0,0,0], ))for x in range(0,12+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(0,12+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(0,12+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(0,12+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(0,12+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(0,12+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(0,12+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge_Net_Subnet2[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,0], Edge_Net_Subnet2[x+2,y,3,1,mask,0], Edge_Net_Subnet2[x+3,y,3,1,mask,0], Edge_Net_Subnet2[x+4,y,3,1,mask,0], Edge_Net_Subnet2[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(1,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge_Net_Subnet2[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,0], Edge_Net_Subnet2[x-2,y,3,1,mask,0], Edge_Net_Subnet2[x-3,y,3,1,mask,0], Edge_Net_Subnet2[x-4,y,3,1,mask,0], Edge_Net_Subnet2[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,0], And(Edge_Net_Subnet2[x+1,y,3,1,mask,0], Edge_Net_Subnet2[x+2,y,3,1,mask,0], Edge_Net_Subnet2[x+3,y,3,1,mask,0], Edge_Net_Subnet2[x+4,y,3,1,mask,0], Edge_Net_Subnet2[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(0, 0+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(0,12+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(0,12+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge_Net_Subnet2[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,0], Edge_Net_Subnet2[x+2,y,2,1,mask,0], Edge_Net_Subnet2[x+3,y,2,1,mask,0], Edge_Net_Subnet2[x+4,y,2,1,mask,0], Edge_Net_Subnet2[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(1,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge_Net_Subnet2[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,0], Edge_Net_Subnet2[x-2,y,2,1,mask,0], Edge_Net_Subnet2[x-3,y,2,1,mask,0], Edge_Net_Subnet2[x-4,y,2,1,mask,0], Edge_Net_Subnet2[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(Edge_Net_Subnet2[x-1,y,2,1,mask,0], Edge_Net_Subnet2[x-2,y,2,1,mask,0], Edge_Net_Subnet2[x-3,y,2,1,mask,0], Edge_Net_Subnet2[x-4,y,2,1,mask,0], Edge_Net_Subnet2[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(0,0+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(Edge_Net_Subnet2[x+1,y,2,1,mask,0], Edge_Net_Subnet2[x+2,y,2,1,mask,0], Edge_Net_Subnet2[x+3,y,2,1,mask,0], Edge_Net_Subnet2[x+4,y,2,1,mask,0], Edge_Net_Subnet2[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(12-1,0)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge_Net_Subnet2[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,0], Edge_Net_Subnet2[x,y+2,2,0,mask,0], Edge_Net_Subnet2[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge_Net_Subnet2[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,0], Edge_Net_Subnet2[x,y-2,2,0,mask,0], Edge_Net_Subnet2[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,0], And(Edge_Net_Subnet2[x,y+1,2,0,mask,0], Edge_Net_Subnet2[x,y+2,2,0,mask,0], Edge_Net_Subnet2[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,0], And(Edge_Net_Subnet2[x,y-1,2,0,mask,0], Edge_Net_Subnet2[x,y-2,2,0,mask,0], Edge_Net_Subnet2[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(0,12+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(0,12+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(0,12+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(0,12+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,12+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet0_DR = And(Net2_Subnet0_DR_Trend, Net2_Subnet0_DR_GIL_HorMinWidth,Net2_Subnet0_DR_GIL_HorMinSpacing,Net2_Subnet0_DR_GIL_VerMinSpacing,Net2_Subnet0_DR_AIL2_VerMinWidth,Net2_Subnet0_DR_AIL2_VerMinSpacing,Net2_Subnet0_DR_VerAIL2_HorMinSpacing,Net2_Subnet0_DR_MINT1AB_HorMinWidth,Net2_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet0_DR_M1AB_MinWidth,Net2_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet0_DR_V0_HorMinSpacing,Net2_Subnet0_DR_V1_HorMinSpacing,Net2_Subnet0_DR_V0_VerMinSpacing,Net2_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[4,0,0,0, 4,1,0,0, 4,2,0,0, 4,3,0,0, 4,4,0,0, 4,5,0,0, 4,6,0,0, 4,7,0,0, 4,8,0,0, 4,9,0,0, 4,10,0,0, 4,11,0,0, 4,12,0,0, 4,13,0,0, 4,14,0,0, 4,15,0,0, 4,16,0,0, 4,17,0,0, 4,18,0,0, 4,19,0,0, 4,20,0,0, 4,21,0,0, 4,22,0,0, 4,23,0,0, 4,24,0,0, 4,25,0,0, 4,26,0,0, 4,27,0,0, 4,28,0,0, 4,29,0,0, 4,30,0,0, 4,31,0,0, 4,32,0,0, 4,33,0,0, 4,34,0,0, 4,35,0,0, ],36,0,0,1,12,35,3,0),
	RConstraints.R1(Edge_Net_Subnet2,[8,0,0,0, 8,1,0,0, 8,2,0,0, 8,3,0,0, 8,4,0,0, 8,5,0,0, 8,6,0,0, 8,7,0,0, 8,8,0,0, 8,9,0,0, 8,10,0,0, 8,11,0,0, 8,12,0,0, 8,13,0,0, 8,14,0,0, 8,15,0,0, 8,16,0,0, 8,17,0,0, 8,18,0,0, 8,19,0,0, 8,20,0,0, 8,21,0,0, 8,22,0,0, 8,23,0,0, 8,24,0,0, 8,25,0,0, 8,26,0,0, 8,27,0,0, 8,28,0,0, 8,29,0,0, 8,30,0,0, 8,31,0,0, 8,32,0,0, 8,33,0,0, 8,34,0,0, 8,35,0,0, ],36,0,0,1,12,35,3,0),
	).to_cnf()
Net2_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[4,0,0, 4,1,0, 4,2,0, 4,3,0, 4,4,0, 4,5,0, 4,6,0, 4,7,0, 4,8,0, 4,9,0, 4,10,0, 4,11,0, 4,12,0, 4,13,0, 4,14,0, 4,15,0, 4,16,0, 4,17,0, 4,18,0, 4,19,0, 4,20,0, 4,21,0, 4,22,0, 4,23,0, 4,24,0, 4,25,0, 4,26,0, 4,27,0, 4,28,0, 4,29,0, 4,30,0, 4,31,0, 4,32,0, 4,33,0, 4,34,0, 4,35,0, 8,0,0, 8,1,0, 8,2,0, 8,3,0, 8,4,0, 8,5,0, 8,6,0, 8,7,0, 8,8,0, 8,9,0, 8,10,0, 8,11,0, 8,12,0, 8,13,0, 8,14,0, 8,15,0, 8,16,0, 8,17,0, 8,18,0, 8,19,0, 8,20,0, 8,21,0, 8,22,0, 8,23,0, 8,24,0, 8,25,0, 8,26,0, 8,27,0, 8,28,0, 8,29,0, 8,30,0, 8,31,0, 8,32,0, 8,33,0, 8,34,0, 8,35,0, ],72,0,0,0,12,35,3,0,1),
	)
Net2_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,5+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet0_R = And(Net2_Subnet0_R1,Net2_Subnet0_R2,Net2_Subnet0_R3,)
Net2_Subnet0_Formula = And(Net2_Subnet0_C,Net2_Subnet0_DR,Net2_Subnet0_R)
# Net = 2 Subnet = 1 | Left -> Right [4,16] Top -> Bottom [0,35]
# Range R1(8,8,0,35)
# Range R2(12,12,0,35)
### Disable edges outside window
Edge_Net_Subnet2[0:4,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(5184)
Edge_Net_Subnet2[16:85+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(90720)

### Consistency Constraints
Net2_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,1],Xor(Edge_Net_Subnet2[x,y,2,trend,1,1],Edge_Net_Subnet2[x,y,2,trend,2,1])),And(~Edge_Net_Subnet2[x,y,2,trend,0,1],~Edge_Net_Subnet2[x,y,2,trend,1,1],~Edge_Net_Subnet2[x,y,2,trend,2,1]))for x in range(4,16+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,1],Xor(Edge_Net_Subnet2[x,y,3,1,1,1],Edge_Net_Subnet2[x,y,3,1,2,1])),And(~Edge_Net_Subnet2[x,y,3,1,0,1],~Edge_Net_Subnet2[x,y,3,1,1,1],~Edge_Net_Subnet2[x,y,3,1,2,1]))for x in range(4,16+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,1],Xor(Edge_Net_Subnet2[x,y,1,trend,0,1],Edge_Net_Subnet2[x,y,1,trend,1,1])),And(~Edge_Net_Subnet2[x,y,1,trend,2,1],~Edge_Net_Subnet2[x,y,1,trend,0,1],~Edge_Net_Subnet2[x,y,1,trend,1,1]))for x in range(4,16+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(1+1,10)]))for trend in range(0,1+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(1+1,10)]))for trend in range(0,1+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet1_C = And(Net2_Subnet1_C1, Net2_Subnet1_C2,Net2_Subnet1_C3_ME1_Mask,Net2_Subnet1_C4_MINT1_Mask,Net2_Subnet1_C5_AIL2GIL_Mask,Net2_Subnet1_C6,)
### Design Rules
Net2_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(4,16+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,1], ~Edge_Net_Subnet2[x-1,y,1,1,1,1]), And(Edge_Net_Subnet2[x+1,y,1,1,1,1], Edge_Net_Subnet2[x+2,y,1,1,1,1], Edge_Net_Subnet2[x+3,y,1,1,1,1], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,1], ~Edge_Net_Subnet2[x+1,y,1,1,1,1]), And(Edge_Net_Subnet2[x-1,y,1,1,1,1], Edge_Net_Subnet2[x-2,y,1,1,1,1], Edge_Net_Subnet2[x-3,y,1,1,1,1], ))for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(4,16+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(4,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1]), And(Edge_Net_Subnet2[x,y+1,1,0,0,1], Edge_Net_Subnet2[x,y+2,1,0,0,1], Edge_Net_Subnet2[x,y+3,1,0,0,1], ))for x in range(4,16+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1]), And(Edge_Net_Subnet2[x,y-1,1,0,0,1], Edge_Net_Subnet2[x,y-2,1,0,0,1], Edge_Net_Subnet2[x,y-3,1,0,0,1], ))for x in range(4,16+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge_Net_Subnet2[x,y-1,1,0,0,1]), And(Edge_Net_Subnet2[x,y+1,1,0,0,1], Edge_Net_Subnet2[x,y+2,1,0,0,1], Edge_Net_Subnet2[x,y+3,1,0,0,1], ))for x in range(4,16+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge_Net_Subnet2[x,y+1,1,0,0,1]), And(Edge_Net_Subnet2[x,y-1,1,0,0,1], Edge_Net_Subnet2[x,y-2,1,0,0,1], Edge_Net_Subnet2[x,y-3,1,0,0,1], ))for x in range(4,16+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(4,16+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(4,16+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(4,16+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(4,16+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(4,16+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(4,16+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,1], ~Edge_Net_Subnet2[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,1], Edge_Net_Subnet2[x+2,y,3,1,mask,1], Edge_Net_Subnet2[x+3,y,3,1,mask,1], Edge_Net_Subnet2[x+4,y,3,1,mask,1], Edge_Net_Subnet2[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,1], ~Edge_Net_Subnet2[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,1], Edge_Net_Subnet2[x-2,y,3,1,mask,1], Edge_Net_Subnet2[x-3,y,3,1,mask,1], Edge_Net_Subnet2[x-4,y,3,1,mask,1], Edge_Net_Subnet2[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(4,16+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(4,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,1], ~Edge_Net_Subnet2[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,1], Edge_Net_Subnet2[x+2,y,2,1,mask,1], Edge_Net_Subnet2[x+3,y,2,1,mask,1], Edge_Net_Subnet2[x+4,y,2,1,mask,1], Edge_Net_Subnet2[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,1], ~Edge_Net_Subnet2[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,1], Edge_Net_Subnet2[x-2,y,2,1,mask,1], Edge_Net_Subnet2[x-3,y,2,1,mask,1], Edge_Net_Subnet2[x-4,y,2,1,mask,1], Edge_Net_Subnet2[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,1], And(Edge_Net_Subnet2[x-1,y,2,1,mask,1], Edge_Net_Subnet2[x-2,y,2,1,mask,1], Edge_Net_Subnet2[x-3,y,2,1,mask,1], Edge_Net_Subnet2[x-4,y,2,1,mask,1], Edge_Net_Subnet2[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(4,4+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,1], And(Edge_Net_Subnet2[x+1,y,2,1,mask,1], Edge_Net_Subnet2[x+2,y,2,1,mask,1], Edge_Net_Subnet2[x+3,y,2,1,mask,1], Edge_Net_Subnet2[x+4,y,2,1,mask,1], Edge_Net_Subnet2[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(16-1,4)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,1], ~Edge_Net_Subnet2[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,1], Edge_Net_Subnet2[x,y+2,2,0,mask,1], Edge_Net_Subnet2[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,1], ~Edge_Net_Subnet2[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,1], Edge_Net_Subnet2[x,y-2,2,0,mask,1], Edge_Net_Subnet2[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,1], And(Edge_Net_Subnet2[x,y+1,2,0,mask,1], Edge_Net_Subnet2[x,y+2,2,0,mask,1], Edge_Net_Subnet2[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,1], And(Edge_Net_Subnet2[x,y-1,2,0,mask,1], Edge_Net_Subnet2[x,y-2,2,0,mask,1], Edge_Net_Subnet2[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(4,16+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(4,16+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(4,16+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(4,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet1_DR = And(Net2_Subnet1_DR_Trend, Net2_Subnet1_DR_GIL_HorMinWidth,Net2_Subnet1_DR_GIL_HorMinSpacing,Net2_Subnet1_DR_GIL_VerMinSpacing,Net2_Subnet1_DR_AIL2_VerMinWidth,Net2_Subnet1_DR_AIL2_VerMinSpacing,Net2_Subnet1_DR_VerAIL2_HorMinSpacing,Net2_Subnet1_DR_MINT1AB_HorMinWidth,Net2_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet1_DR_M1AB_MinWidth,Net2_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet1_DR_V0_HorMinSpacing,Net2_Subnet1_DR_V1_HorMinSpacing,Net2_Subnet1_DR_V0_VerMinSpacing,Net2_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[8,0,0,0, 8,1,0,0, 8,2,0,0, 8,3,0,0, 8,4,0,0, 8,5,0,0, 8,6,0,0, 8,7,0,0, 8,8,0,0, 8,9,0,0, 8,10,0,0, 8,11,0,0, 8,12,0,0, 8,13,0,0, 8,14,0,0, 8,15,0,0, 8,16,0,0, 8,17,0,0, 8,18,0,0, 8,19,0,0, 8,20,0,0, 8,21,0,0, 8,22,0,0, 8,23,0,0, 8,24,0,0, 8,25,0,0, 8,26,0,0, 8,27,0,0, 8,28,0,0, 8,29,0,0, 8,30,0,0, 8,31,0,0, 8,32,0,0, 8,33,0,0, 8,34,0,0, 8,35,0,0, ],36,4,0,1,16,35,3,1),
	RConstraints.R1(Edge_Net_Subnet2,[12,0,0,0, 12,1,0,0, 12,2,0,0, 12,3,0,0, 12,4,0,0, 12,5,0,0, 12,6,0,0, 12,7,0,0, 12,8,0,0, 12,9,0,0, 12,10,0,0, 12,11,0,0, 12,12,0,0, 12,13,0,0, 12,14,0,0, 12,15,0,0, 12,16,0,0, 12,17,0,0, 12,18,0,0, 12,19,0,0, 12,20,0,0, 12,21,0,0, 12,22,0,0, 12,23,0,0, 12,24,0,0, 12,25,0,0, 12,26,0,0, 12,27,0,0, 12,28,0,0, 12,29,0,0, 12,30,0,0, 12,31,0,0, 12,32,0,0, 12,33,0,0, 12,34,0,0, 12,35,0,0, ],36,4,0,1,16,35,3,1),
	).to_cnf()
Net2_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[8,0,0, 8,1,0, 8,2,0, 8,3,0, 8,4,0, 8,5,0, 8,6,0, 8,7,0, 8,8,0, 8,9,0, 8,10,0, 8,11,0, 8,12,0, 8,13,0, 8,14,0, 8,15,0, 8,16,0, 8,17,0, 8,18,0, 8,19,0, 8,20,0, 8,21,0, 8,22,0, 8,23,0, 8,24,0, 8,25,0, 8,26,0, 8,27,0, 8,28,0, 8,29,0, 8,30,0, 8,31,0, 8,32,0, 8,33,0, 8,34,0, 8,35,0, 12,0,0, 12,1,0, 12,2,0, 12,3,0, 12,4,0, 12,5,0, 12,6,0, 12,7,0, 12,8,0, 12,9,0, 12,10,0, 12,11,0, 12,12,0, 12,13,0, 12,14,0, 12,15,0, 12,16,0, 12,17,0, 12,18,0, 12,19,0, 12,20,0, 12,21,0, 12,22,0, 12,23,0, 12,24,0, 12,25,0, 12,26,0, 12,27,0, 12,28,0, 12,29,0, 12,30,0, 12,31,0, 12,32,0, 12,33,0, 12,34,0, 12,35,0, ],72,4,0,0,16,35,3,1,1),
	)
Net2_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,5+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet1_R = And(Net2_Subnet1_R1,Net2_Subnet1_R2,Net2_Subnet1_R3,)
Net2_Subnet1_Formula = And(Net2_Subnet1_C,Net2_Subnet1_DR,Net2_Subnet1_R)
# Net = 2 Subnet = 2 | Left -> Right [8,20] Top -> Bottom [0,35]
# Range R1(12,12,0,35)
# Range R2(16,16,0,35)
### Disable edges outside window
Edge_Net_Subnet2[0:8,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(10368)
Edge_Net_Subnet2[20:85+1,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(85536)

### Consistency Constraints
Net2_Subnet2_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet2_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,2]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet2_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,2],Xor(Edge_Net_Subnet2[x,y,2,trend,1,2],Edge_Net_Subnet2[x,y,2,trend,2,2])),And(~Edge_Net_Subnet2[x,y,2,trend,0,2],~Edge_Net_Subnet2[x,y,2,trend,1,2],~Edge_Net_Subnet2[x,y,2,trend,2,2]))for x in range(8,20+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet2_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,2],Xor(Edge_Net_Subnet2[x,y,3,1,1,2],Edge_Net_Subnet2[x,y,3,1,2,2])),And(~Edge_Net_Subnet2[x,y,3,1,0,2],~Edge_Net_Subnet2[x,y,3,1,1,2],~Edge_Net_Subnet2[x,y,3,1,2,2]))for x in range(8,20+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet2_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,2],Xor(Edge_Net_Subnet2[x,y,1,trend,0,2],Edge_Net_Subnet2[x,y,1,trend,1,2])),And(~Edge_Net_Subnet2[x,y,1,trend,2,2],~Edge_Net_Subnet2[x,y,1,trend,0,2],~Edge_Net_Subnet2[x,y,1,trend,1,2]))for x in range(8,20+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet2_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(2+1,10)]))for trend in range(0,1+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(2+1,10)]))for trend in range(0,1+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet2_C = And(Net2_Subnet2_C1, Net2_Subnet2_C2,Net2_Subnet2_C3_ME1_Mask,Net2_Subnet2_C4_MINT1_Mask,Net2_Subnet2_C5_AIL2GIL_Mask,Net2_Subnet2_C6,)
### Design Rules
Net2_Subnet2_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(8,20+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet2_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,2], ~Edge_Net_Subnet2[x-1,y,1,1,1,2]), And(Edge_Net_Subnet2[x+1,y,1,1,1,2], Edge_Net_Subnet2[x+2,y,1,1,1,2], Edge_Net_Subnet2[x+3,y,1,1,1,2], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,2], ~Edge_Net_Subnet2[x+1,y,1,1,1,2]), And(Edge_Net_Subnet2[x-1,y,1,1,1,2], Edge_Net_Subnet2[x-2,y,1,1,1,2], Edge_Net_Subnet2[x-3,y,1,1,1,2], ))for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,2], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,2], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,2], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(8,20+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,2], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(8,20+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2]), And(Edge_Net_Subnet2[x,y+1,1,0,0,2], Edge_Net_Subnet2[x,y+2,1,0,0,2], Edge_Net_Subnet2[x,y+3,1,0,0,2], ))for x in range(8,20+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2]), And(Edge_Net_Subnet2[x,y-1,1,0,0,2], Edge_Net_Subnet2[x,y-2,1,0,0,2], Edge_Net_Subnet2[x,y-3,1,0,0,2], ))for x in range(8,20+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge_Net_Subnet2[x,y-1,1,0,0,2]), And(Edge_Net_Subnet2[x,y+1,1,0,0,2], Edge_Net_Subnet2[x,y+2,1,0,0,2], Edge_Net_Subnet2[x,y+3,1,0,0,2], ))for x in range(8,20+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge_Net_Subnet2[x,y+1,1,0,0,2]), And(Edge_Net_Subnet2[x,y-1,1,0,0,2], Edge_Net_Subnet2[x,y-2,1,0,0,2], Edge_Net_Subnet2[x,y-3,1,0,0,2], ))for x in range(8,20+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet2_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(8,20+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(8,20+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(8,20+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(8,20+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(8,20+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(8,20+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet2_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,2], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,2], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,2], ~Edge_Net_Subnet2[x-1,y,3,1,mask,2]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,2], Edge_Net_Subnet2[x+2,y,3,1,mask,2], Edge_Net_Subnet2[x+3,y,3,1,mask,2], Edge_Net_Subnet2[x+4,y,3,1,mask,2], Edge_Net_Subnet2[x+5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,2], ~Edge_Net_Subnet2[x+1,y,3,1,mask,2]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,2], Edge_Net_Subnet2[x-2,y,3,1,mask,2], Edge_Net_Subnet2[x-3,y,3,1,mask,2], Edge_Net_Subnet2[x-4,y,3,1,mask,2], Edge_Net_Subnet2[x-5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,2], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,2], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,2], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,2], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,2], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(8,20+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,2], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(8,20+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,2], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,2], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,2], ~Edge_Net_Subnet2[x-1,y,2,1,mask,2]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,2], Edge_Net_Subnet2[x+2,y,2,1,mask,2], Edge_Net_Subnet2[x+3,y,2,1,mask,2], Edge_Net_Subnet2[x+4,y,2,1,mask,2], Edge_Net_Subnet2[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,2], ~Edge_Net_Subnet2[x+1,y,2,1,mask,2]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,2], Edge_Net_Subnet2[x-2,y,2,1,mask,2], Edge_Net_Subnet2[x-3,y,2,1,mask,2], Edge_Net_Subnet2[x-4,y,2,1,mask,2], Edge_Net_Subnet2[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,2], And(Edge_Net_Subnet2[x-1,y,2,1,mask,2], Edge_Net_Subnet2[x-2,y,2,1,mask,2], Edge_Net_Subnet2[x-3,y,2,1,mask,2], Edge_Net_Subnet2[x-4,y,2,1,mask,2], Edge_Net_Subnet2[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(8,8+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,2], And(Edge_Net_Subnet2[x+1,y,2,1,mask,2], Edge_Net_Subnet2[x+2,y,2,1,mask,2], Edge_Net_Subnet2[x+3,y,2,1,mask,2], Edge_Net_Subnet2[x+4,y,2,1,mask,2], Edge_Net_Subnet2[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(20-1,8)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,2], ~Edge_Net_Subnet2[x,y-1,2,0,mask,2]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,2], Edge_Net_Subnet2[x,y+2,2,0,mask,2], Edge_Net_Subnet2[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,2], ~Edge_Net_Subnet2[x,y+1,2,0,mask,2]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,2], Edge_Net_Subnet2[x,y-2,2,0,mask,2], Edge_Net_Subnet2[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,2], And(Edge_Net_Subnet2[x,y+1,2,0,mask,2], Edge_Net_Subnet2[x,y+2,2,0,mask,2], Edge_Net_Subnet2[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,2], And(Edge_Net_Subnet2[x,y-1,2,0,mask,2], Edge_Net_Subnet2[x,y-2,2,0,mask,2], Edge_Net_Subnet2[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,2], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,2], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,2], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,2], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,2], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(8,20+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,2], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(8,20+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet2_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,2], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,2], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet2_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,2], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(8,20+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,2], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(8,20+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,2], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,2], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,2], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,2], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,2], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,2], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,2], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,2], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,2], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,2], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,2], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,2], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,2], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,2], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet2_DR = And(Net2_Subnet2_DR_Trend, Net2_Subnet2_DR_GIL_HorMinWidth,Net2_Subnet2_DR_GIL_HorMinSpacing,Net2_Subnet2_DR_GIL_VerMinSpacing,Net2_Subnet2_DR_AIL2_VerMinWidth,Net2_Subnet2_DR_AIL2_VerMinSpacing,Net2_Subnet2_DR_VerAIL2_HorMinSpacing,Net2_Subnet2_DR_MINT1AB_HorMinWidth,Net2_Subnet2_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet2_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet2_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet2_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet2_DR_M1AB_MinWidth,Net2_Subnet2_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet2_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet2_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet2_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet2_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet2_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet2_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet2_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet2_DR_V0_HorMinSpacing,Net2_Subnet2_DR_V1_HorMinSpacing,Net2_Subnet2_DR_V0_VerMinSpacing,Net2_Subnet2_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet2_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[12,0,0,0, 12,1,0,0, 12,2,0,0, 12,3,0,0, 12,4,0,0, 12,5,0,0, 12,6,0,0, 12,7,0,0, 12,8,0,0, 12,9,0,0, 12,10,0,0, 12,11,0,0, 12,12,0,0, 12,13,0,0, 12,14,0,0, 12,15,0,0, 12,16,0,0, 12,17,0,0, 12,18,0,0, 12,19,0,0, 12,20,0,0, 12,21,0,0, 12,22,0,0, 12,23,0,0, 12,24,0,0, 12,25,0,0, 12,26,0,0, 12,27,0,0, 12,28,0,0, 12,29,0,0, 12,30,0,0, 12,31,0,0, 12,32,0,0, 12,33,0,0, 12,34,0,0, 12,35,0,0, ],36,8,0,1,20,35,3,2),
	RConstraints.R1(Edge_Net_Subnet2,[16,0,0,0, 16,1,0,0, 16,2,0,0, 16,3,0,0, 16,4,0,0, 16,5,0,0, 16,6,0,0, 16,7,0,0, 16,8,0,0, 16,9,0,0, 16,10,0,0, 16,11,0,0, 16,12,0,0, 16,13,0,0, 16,14,0,0, 16,15,0,0, 16,16,0,0, 16,17,0,0, 16,18,0,0, 16,19,0,0, 16,20,0,0, 16,21,0,0, 16,22,0,0, 16,23,0,0, 16,24,0,0, 16,25,0,0, 16,26,0,0, 16,27,0,0, 16,28,0,0, 16,29,0,0, 16,30,0,0, 16,31,0,0, 16,32,0,0, 16,33,0,0, 16,34,0,0, 16,35,0,0, ],36,8,0,1,20,35,3,2),
	).to_cnf()
Net2_Subnet2_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[12,0,0, 12,1,0, 12,2,0, 12,3,0, 12,4,0, 12,5,0, 12,6,0, 12,7,0, 12,8,0, 12,9,0, 12,10,0, 12,11,0, 12,12,0, 12,13,0, 12,14,0, 12,15,0, 12,16,0, 12,17,0, 12,18,0, 12,19,0, 12,20,0, 12,21,0, 12,22,0, 12,23,0, 12,24,0, 12,25,0, 12,26,0, 12,27,0, 12,28,0, 12,29,0, 12,30,0, 12,31,0, 12,32,0, 12,33,0, 12,34,0, 12,35,0, 16,0,0, 16,1,0, 16,2,0, 16,3,0, 16,4,0, 16,5,0, 16,6,0, 16,7,0, 16,8,0, 16,9,0, 16,10,0, 16,11,0, 16,12,0, 16,13,0, 16,14,0, 16,15,0, 16,16,0, 16,17,0, 16,18,0, 16,19,0, 16,20,0, 16,21,0, 16,22,0, 16,23,0, 16,24,0, 16,25,0, 16,26,0, 16,27,0, 16,28,0, 16,29,0, 16,30,0, 16,31,0, 16,32,0, 16,33,0, 16,34,0, 16,35,0, ],72,8,0,0,20,35,3,2,1),
	)
Net2_Subnet2_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,5+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet2_R = And(Net2_Subnet2_R1,Net2_Subnet2_R2,Net2_Subnet2_R3,)
Net2_Subnet2_Formula = And(Net2_Subnet2_C,Net2_Subnet2_DR,Net2_Subnet2_R)
# Net = 2 Subnet = 3 | Left -> Right [0,16] Top -> Bottom [0,35]
# Range R1(12,12,0,35)
# Range R2(4,4,0,35)
### Disable edges outside window
Edge_Net_Subnet2[16:85+1,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(90720)

### Consistency Constraints
Net2_Subnet3_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet3_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,3]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet3_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,3],Xor(Edge_Net_Subnet2[x,y,2,trend,1,3],Edge_Net_Subnet2[x,y,2,trend,2,3])),And(~Edge_Net_Subnet2[x,y,2,trend,0,3],~Edge_Net_Subnet2[x,y,2,trend,1,3],~Edge_Net_Subnet2[x,y,2,trend,2,3]))for x in range(0,16+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet3_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,3],Xor(Edge_Net_Subnet2[x,y,3,1,1,3],Edge_Net_Subnet2[x,y,3,1,2,3])),And(~Edge_Net_Subnet2[x,y,3,1,0,3],~Edge_Net_Subnet2[x,y,3,1,1,3],~Edge_Net_Subnet2[x,y,3,1,2,3]))for x in range(0,16+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet3_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,3],Xor(Edge_Net_Subnet2[x,y,1,trend,0,3],Edge_Net_Subnet2[x,y,1,trend,1,3])),And(~Edge_Net_Subnet2[x,y,1,trend,2,3],~Edge_Net_Subnet2[x,y,1,trend,0,3],~Edge_Net_Subnet2[x,y,1,trend,1,3]))for x in range(0,16+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet3_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(3+1,10)]))for trend in range(0,1+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(3+1,10)]))for trend in range(0,1+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet3_C = And(Net2_Subnet3_C1, Net2_Subnet3_C2,Net2_Subnet3_C3_ME1_Mask,Net2_Subnet3_C4_MINT1_Mask,Net2_Subnet3_C5_AIL2GIL_Mask,Net2_Subnet3_C6,)
### Design Rules
Net2_Subnet3_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(0,16+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet3_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,3], ~Edge_Net_Subnet2[x-1,y,1,1,1,3]), And(Edge_Net_Subnet2[x+1,y,1,1,1,3], Edge_Net_Subnet2[x+2,y,1,1,1,3], Edge_Net_Subnet2[x+3,y,1,1,1,3], ))for x in range(1,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,3], ~Edge_Net_Subnet2[x+1,y,1,1,1,3]), And(Edge_Net_Subnet2[x-1,y,1,1,1,3], Edge_Net_Subnet2[x-2,y,1,1,1,3], Edge_Net_Subnet2[x-3,y,1,1,1,3], ))for x in range(3,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,3], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,3], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,3], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(0,16+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,3], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(0,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3]), And(Edge_Net_Subnet2[x,y+1,1,0,0,3], Edge_Net_Subnet2[x,y+2,1,0,0,3], Edge_Net_Subnet2[x,y+3,1,0,0,3], ))for x in range(0,16+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3]), And(Edge_Net_Subnet2[x,y-1,1,0,0,3], Edge_Net_Subnet2[x,y-2,1,0,0,3], Edge_Net_Subnet2[x,y-3,1,0,0,3], ))for x in range(0,16+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge_Net_Subnet2[x,y-1,1,0,0,3]), And(Edge_Net_Subnet2[x,y+1,1,0,0,3], Edge_Net_Subnet2[x,y+2,1,0,0,3], Edge_Net_Subnet2[x,y+3,1,0,0,3], ))for x in range(0,16+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge_Net_Subnet2[x,y+1,1,0,0,3]), And(Edge_Net_Subnet2[x,y-1,1,0,0,3], Edge_Net_Subnet2[x,y-2,1,0,0,3], Edge_Net_Subnet2[x,y-3,1,0,0,3], ))for x in range(0,16+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet3_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(0,16+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(0,16+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(0,16+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(0,16+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(0,16+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(0,16+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet3_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,3], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,3], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,3], ~Edge_Net_Subnet2[x-1,y,3,1,mask,3]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,3], Edge_Net_Subnet2[x+2,y,3,1,mask,3], Edge_Net_Subnet2[x+3,y,3,1,mask,3], Edge_Net_Subnet2[x+4,y,3,1,mask,3], Edge_Net_Subnet2[x+5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(1,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,3], ~Edge_Net_Subnet2[x+1,y,3,1,mask,3]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,3], Edge_Net_Subnet2[x-2,y,3,1,mask,3], Edge_Net_Subnet2[x-3,y,3,1,mask,3], Edge_Net_Subnet2[x-4,y,3,1,mask,3], Edge_Net_Subnet2[x-5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,3], And(Edge_Net_Subnet2[x+1,y,3,1,mask,3], Edge_Net_Subnet2[x+2,y,3,1,mask,3], Edge_Net_Subnet2[x+3,y,3,1,mask,3], Edge_Net_Subnet2[x+4,y,3,1,mask,3], Edge_Net_Subnet2[x+5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(0, 0+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,3], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,3], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,3], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,3], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,3], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(0,16+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,3], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(0,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,3], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,3], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,3], ~Edge_Net_Subnet2[x-1,y,2,1,mask,3]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,3], Edge_Net_Subnet2[x+2,y,2,1,mask,3], Edge_Net_Subnet2[x+3,y,2,1,mask,3], Edge_Net_Subnet2[x+4,y,2,1,mask,3], Edge_Net_Subnet2[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(1,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,3], ~Edge_Net_Subnet2[x+1,y,2,1,mask,3]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,3], Edge_Net_Subnet2[x-2,y,2,1,mask,3], Edge_Net_Subnet2[x-3,y,2,1,mask,3], Edge_Net_Subnet2[x-4,y,2,1,mask,3], Edge_Net_Subnet2[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,3], And(Edge_Net_Subnet2[x-1,y,2,1,mask,3], Edge_Net_Subnet2[x-2,y,2,1,mask,3], Edge_Net_Subnet2[x-3,y,2,1,mask,3], Edge_Net_Subnet2[x-4,y,2,1,mask,3], Edge_Net_Subnet2[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(0,0+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,3], And(Edge_Net_Subnet2[x+1,y,2,1,mask,3], Edge_Net_Subnet2[x+2,y,2,1,mask,3], Edge_Net_Subnet2[x+3,y,2,1,mask,3], Edge_Net_Subnet2[x+4,y,2,1,mask,3], Edge_Net_Subnet2[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(16-1,0)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,3], ~Edge_Net_Subnet2[x,y-1,2,0,mask,3]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,3], Edge_Net_Subnet2[x,y+2,2,0,mask,3], Edge_Net_Subnet2[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,3], ~Edge_Net_Subnet2[x,y+1,2,0,mask,3]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,3], Edge_Net_Subnet2[x,y-2,2,0,mask,3], Edge_Net_Subnet2[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,3], And(Edge_Net_Subnet2[x,y+1,2,0,mask,3], Edge_Net_Subnet2[x,y+2,2,0,mask,3], Edge_Net_Subnet2[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,3], And(Edge_Net_Subnet2[x,y-1,2,0,mask,3], Edge_Net_Subnet2[x,y-2,2,0,mask,3], Edge_Net_Subnet2[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,3], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,3], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,3], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,3], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,3], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(0,16+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,3], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(0,16+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet3_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,3], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,3], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet3_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,3], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(0,16+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,3], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(0,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,3], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,3], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,3], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,3], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,3], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,3], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,3], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,3], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,3], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,3], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,3], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,3], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,3], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,3], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet3_DR = And(Net2_Subnet3_DR_Trend, Net2_Subnet3_DR_GIL_HorMinWidth,Net2_Subnet3_DR_GIL_HorMinSpacing,Net2_Subnet3_DR_GIL_VerMinSpacing,Net2_Subnet3_DR_AIL2_VerMinWidth,Net2_Subnet3_DR_AIL2_VerMinSpacing,Net2_Subnet3_DR_VerAIL2_HorMinSpacing,Net2_Subnet3_DR_MINT1AB_HorMinWidth,Net2_Subnet3_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet3_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet3_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet3_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet3_DR_M1AB_MinWidth,Net2_Subnet3_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet3_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet3_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet3_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet3_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet3_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet3_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet3_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet3_DR_V0_HorMinSpacing,Net2_Subnet3_DR_V1_HorMinSpacing,Net2_Subnet3_DR_V0_VerMinSpacing,Net2_Subnet3_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet3_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[12,0,0,0, 12,1,0,0, 12,2,0,0, 12,3,0,0, 12,4,0,0, 12,5,0,0, 12,6,0,0, 12,7,0,0, 12,8,0,0, 12,9,0,0, 12,10,0,0, 12,11,0,0, 12,12,0,0, 12,13,0,0, 12,14,0,0, 12,15,0,0, 12,16,0,0, 12,17,0,0, 12,18,0,0, 12,19,0,0, 12,20,0,0, 12,21,0,0, 12,22,0,0, 12,23,0,0, 12,24,0,0, 12,25,0,0, 12,26,0,0, 12,27,0,0, 12,28,0,0, 12,29,0,0, 12,30,0,0, 12,31,0,0, 12,32,0,0, 12,33,0,0, 12,34,0,0, 12,35,0,0, ],36,0,0,1,16,35,3,3),
	RConstraints.R1(Edge_Net_Subnet2,[4,0,0,0, 4,1,0,0, 4,2,0,0, 4,3,0,0, 4,4,0,0, 4,5,0,0, 4,6,0,0, 4,7,0,0, 4,8,0,0, 4,9,0,0, 4,10,0,0, 4,11,0,0, 4,12,0,0, 4,13,0,0, 4,14,0,0, 4,15,0,0, 4,16,0,0, 4,17,0,0, 4,18,0,0, 4,19,0,0, 4,20,0,0, 4,21,0,0, 4,22,0,0, 4,23,0,0, 4,24,0,0, 4,25,0,0, 4,26,0,0, 4,27,0,0, 4,28,0,0, 4,29,0,0, 4,30,0,0, 4,31,0,0, 4,32,0,0, 4,33,0,0, 4,34,0,0, 4,35,0,0, ],36,0,0,1,16,35,3,3),
	).to_cnf()
Net2_Subnet3_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[12,0,0, 12,1,0, 12,2,0, 12,3,0, 12,4,0, 12,5,0, 12,6,0, 12,7,0, 12,8,0, 12,9,0, 12,10,0, 12,11,0, 12,12,0, 12,13,0, 12,14,0, 12,15,0, 12,16,0, 12,17,0, 12,18,0, 12,19,0, 12,20,0, 12,21,0, 12,22,0, 12,23,0, 12,24,0, 12,25,0, 12,26,0, 12,27,0, 12,28,0, 12,29,0, 12,30,0, 12,31,0, 12,32,0, 12,33,0, 12,34,0, 12,35,0, 4,0,0, 4,1,0, 4,2,0, 4,3,0, 4,4,0, 4,5,0, 4,6,0, 4,7,0, 4,8,0, 4,9,0, 4,10,0, 4,11,0, 4,12,0, 4,13,0, 4,14,0, 4,15,0, 4,16,0, 4,17,0, 4,18,0, 4,19,0, 4,20,0, 4,21,0, 4,22,0, 4,23,0, 4,24,0, 4,25,0, 4,26,0, 4,27,0, 4,28,0, 4,29,0, 4,30,0, 4,31,0, 4,32,0, 4,33,0, 4,34,0, 4,35,0, ],72,0,0,0,16,35,3,3,1),
	)
Net2_Subnet3_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,5+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet3_R = And(Net2_Subnet3_R1,Net2_Subnet3_R2,Net2_Subnet3_R3,)
Net2_Subnet3_Formula = And(Net2_Subnet3_C,Net2_Subnet3_DR,Net2_Subnet3_R)
# Net = 2 Subnet = 4 | Left -> Right [12,28] Top -> Bottom [0,35]
# Range R1(16,16,0,35)
# Range R2(24,24,0,35)
### Disable edges outside window
Edge_Net_Subnet2[0:12,0:35+1,0:3+1,0:2+1,0:2+1,4]=exprzeros(15552)
Edge_Net_Subnet2[28:85+1,0:35+1,0:3+1,0:2+1,0:2+1,4]=exprzeros(75168)

### Consistency Constraints
Net2_Subnet4_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet4_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,4]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet4_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,4],Xor(Edge_Net_Subnet2[x,y,2,trend,1,4],Edge_Net_Subnet2[x,y,2,trend,2,4])),And(~Edge_Net_Subnet2[x,y,2,trend,0,4],~Edge_Net_Subnet2[x,y,2,trend,1,4],~Edge_Net_Subnet2[x,y,2,trend,2,4]))for x in range(12,28+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet4_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,4],Xor(Edge_Net_Subnet2[x,y,3,1,1,4],Edge_Net_Subnet2[x,y,3,1,2,4])),And(~Edge_Net_Subnet2[x,y,3,1,0,4],~Edge_Net_Subnet2[x,y,3,1,1,4],~Edge_Net_Subnet2[x,y,3,1,2,4]))for x in range(12,28+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet4_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,4],Xor(Edge_Net_Subnet2[x,y,1,trend,0,4],Edge_Net_Subnet2[x,y,1,trend,1,4])),And(~Edge_Net_Subnet2[x,y,1,trend,2,4],~Edge_Net_Subnet2[x,y,1,trend,0,4],~Edge_Net_Subnet2[x,y,1,trend,1,4]))for x in range(12,28+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet4_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,4], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,4)]))for trend in range(0,1+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,4], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(4+1,10)]))for trend in range(0,1+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,4], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,4)]))for trend in range(0,1+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,4], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(4+1,10)]))for trend in range(0,1+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet4_C = And(Net2_Subnet4_C1, Net2_Subnet4_C2,Net2_Subnet4_C3_ME1_Mask,Net2_Subnet4_C4_MINT1_Mask,Net2_Subnet4_C5_AIL2GIL_Mask,Net2_Subnet4_C6,)
### Design Rules
Net2_Subnet4_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(12,28+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet4_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,4], ~Edge_Net_Subnet2[x-1,y,1,1,1,4]), And(Edge_Net_Subnet2[x+1,y,1,1,1,4], Edge_Net_Subnet2[x+2,y,1,1,1,4], Edge_Net_Subnet2[x+3,y,1,1,1,4], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,4], ~Edge_Net_Subnet2[x+1,y,1,1,1,4]), And(Edge_Net_Subnet2[x-1,y,1,1,1,4], Edge_Net_Subnet2[x-2,y,1,1,1,4], Edge_Net_Subnet2[x-3,y,1,1,1,4], ))for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet4_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,4], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,4], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet4_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,4], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(12,28+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,4], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(12,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet4_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,4]), And(Edge_Net_Subnet2[x,y+1,1,0,0,4], Edge_Net_Subnet2[x,y+2,1,0,0,4], Edge_Net_Subnet2[x,y+3,1,0,0,4], ))for x in range(12,28+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,4]), And(Edge_Net_Subnet2[x,y-1,1,0,0,4], Edge_Net_Subnet2[x,y-2,1,0,0,4], Edge_Net_Subnet2[x,y-3,1,0,0,4], ))for x in range(12,28+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,4], ~Edge_Net_Subnet2[x,y-1,1,0,0,4]), And(Edge_Net_Subnet2[x,y+1,1,0,0,4], Edge_Net_Subnet2[x,y+2,1,0,0,4], Edge_Net_Subnet2[x,y+3,1,0,0,4], ))for x in range(12,28+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,4], ~Edge_Net_Subnet2[x,y+1,1,0,0,4]), And(Edge_Net_Subnet2[x,y-1,1,0,0,4], Edge_Net_Subnet2[x,y-2,1,0,0,4], Edge_Net_Subnet2[x,y-3,1,0,0,4], ))for x in range(12,28+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet4_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(12,28+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(12,28+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(12,28+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(12,28+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(12,28+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(12,28+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet4_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,4], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,4], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet4_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,4], ~Edge_Net_Subnet2[x-1,y,3,1,mask,4]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,4], Edge_Net_Subnet2[x+2,y,3,1,mask,4], Edge_Net_Subnet2[x+3,y,3,1,mask,4], Edge_Net_Subnet2[x+4,y,3,1,mask,4], Edge_Net_Subnet2[x+5,y,3,1,mask,4], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,4], ~Edge_Net_Subnet2[x+1,y,3,1,mask,4]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,4], Edge_Net_Subnet2[x-2,y,3,1,mask,4], Edge_Net_Subnet2[x-3,y,3,1,mask,4], Edge_Net_Subnet2[x-4,y,3,1,mask,4], Edge_Net_Subnet2[x-5,y,3,1,mask,4], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet4_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,4], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,4], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet4_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,4], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,4], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet4_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,4], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(12,28+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,4], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(12,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet4_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,4], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,4], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet4_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,4], ~Edge_Net_Subnet2[x-1,y,2,1,mask,4]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,4], Edge_Net_Subnet2[x+2,y,2,1,mask,4], Edge_Net_Subnet2[x+3,y,2,1,mask,4], Edge_Net_Subnet2[x+4,y,2,1,mask,4], Edge_Net_Subnet2[x+5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,4], ~Edge_Net_Subnet2[x+1,y,2,1,mask,4]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,4], Edge_Net_Subnet2[x-2,y,2,1,mask,4], Edge_Net_Subnet2[x-3,y,2,1,mask,4], Edge_Net_Subnet2[x-4,y,2,1,mask,4], Edge_Net_Subnet2[x-5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,4], And(Edge_Net_Subnet2[x-1,y,2,1,mask,4], Edge_Net_Subnet2[x-2,y,2,1,mask,4], Edge_Net_Subnet2[x-3,y,2,1,mask,4], Edge_Net_Subnet2[x-4,y,2,1,mask,4], Edge_Net_Subnet2[x-5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(12,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,4], And(Edge_Net_Subnet2[x+1,y,2,1,mask,4], Edge_Net_Subnet2[x+2,y,2,1,mask,4], Edge_Net_Subnet2[x+3,y,2,1,mask,4], Edge_Net_Subnet2[x+4,y,2,1,mask,4], Edge_Net_Subnet2[x+5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(28-1,12)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,4], ~Edge_Net_Subnet2[x,y-1,2,0,mask,4]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,4], Edge_Net_Subnet2[x,y+2,2,0,mask,4], Edge_Net_Subnet2[x,y+3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,4], ~Edge_Net_Subnet2[x,y+1,2,0,mask,4]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,4], Edge_Net_Subnet2[x,y-2,2,0,mask,4], Edge_Net_Subnet2[x,y-3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,4], And(Edge_Net_Subnet2[x,y+1,2,0,mask,4], Edge_Net_Subnet2[x,y+2,2,0,mask,4], Edge_Net_Subnet2[x,y+3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,4], And(Edge_Net_Subnet2[x,y-1,2,0,mask,4], Edge_Net_Subnet2[x,y-2,2,0,mask,4], Edge_Net_Subnet2[x,y-3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet4_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,4], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,4], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet4_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,4], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,4], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet4_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,4], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(12,28+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,4], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(12,28+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet4_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,4], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,4], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet4_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,4], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(12,28+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,4], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(12,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet4_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,4], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,4], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet4_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,4], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,4], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet4_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,4], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,4], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet4_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,4], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,4], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet4_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,4], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,4], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet4_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,4], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,4], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet4_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,4], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,4], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet4_DR = And(Net2_Subnet4_DR_Trend, Net2_Subnet4_DR_GIL_HorMinWidth,Net2_Subnet4_DR_GIL_HorMinSpacing,Net2_Subnet4_DR_GIL_VerMinSpacing,Net2_Subnet4_DR_AIL2_VerMinWidth,Net2_Subnet4_DR_AIL2_VerMinSpacing,Net2_Subnet4_DR_VerAIL2_HorMinSpacing,Net2_Subnet4_DR_MINT1AB_HorMinWidth,Net2_Subnet4_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet4_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet4_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet4_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet4_DR_M1AB_MinWidth,Net2_Subnet4_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet4_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet4_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet4_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet4_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet4_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet4_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet4_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet4_DR_V0_HorMinSpacing,Net2_Subnet4_DR_V1_HorMinSpacing,Net2_Subnet4_DR_V0_VerMinSpacing,Net2_Subnet4_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet4_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[16,0,0,0, 16,1,0,0, 16,2,0,0, 16,3,0,0, 16,4,0,0, 16,5,0,0, 16,6,0,0, 16,7,0,0, 16,8,0,0, 16,9,0,0, 16,10,0,0, 16,11,0,0, 16,12,0,0, 16,13,0,0, 16,14,0,0, 16,15,0,0, 16,16,0,0, 16,17,0,0, 16,18,0,0, 16,19,0,0, 16,20,0,0, 16,21,0,0, 16,22,0,0, 16,23,0,0, 16,24,0,0, 16,25,0,0, 16,26,0,0, 16,27,0,0, 16,28,0,0, 16,29,0,0, 16,30,0,0, 16,31,0,0, 16,32,0,0, 16,33,0,0, 16,34,0,0, 16,35,0,0, ],36,12,0,1,28,35,3,4),
	RConstraints.R1(Edge_Net_Subnet2,[24,0,0,0, 24,1,0,0, 24,2,0,0, 24,3,0,0, 24,4,0,0, 24,5,0,0, 24,6,0,0, 24,7,0,0, 24,8,0,0, 24,9,0,0, 24,10,0,0, 24,11,0,0, 24,12,0,0, 24,13,0,0, 24,14,0,0, 24,15,0,0, 24,16,0,0, 24,17,0,0, 24,18,0,0, 24,19,0,0, 24,20,0,0, 24,21,0,0, 24,22,0,0, 24,23,0,0, 24,24,0,0, 24,25,0,0, 24,26,0,0, 24,27,0,0, 24,28,0,0, 24,29,0,0, 24,30,0,0, 24,31,0,0, 24,32,0,0, 24,33,0,0, 24,34,0,0, 24,35,0,0, ],36,12,0,1,28,35,3,4),
	).to_cnf()
Net2_Subnet4_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[16,0,0, 16,1,0, 16,2,0, 16,3,0, 16,4,0, 16,5,0, 16,6,0, 16,7,0, 16,8,0, 16,9,0, 16,10,0, 16,11,0, 16,12,0, 16,13,0, 16,14,0, 16,15,0, 16,16,0, 16,17,0, 16,18,0, 16,19,0, 16,20,0, 16,21,0, 16,22,0, 16,23,0, 16,24,0, 16,25,0, 16,26,0, 16,27,0, 16,28,0, 16,29,0, 16,30,0, 16,31,0, 16,32,0, 16,33,0, 16,34,0, 16,35,0, 24,0,0, 24,1,0, 24,2,0, 24,3,0, 24,4,0, 24,5,0, 24,6,0, 24,7,0, 24,8,0, 24,9,0, 24,10,0, 24,11,0, 24,12,0, 24,13,0, 24,14,0, 24,15,0, 24,16,0, 24,17,0, 24,18,0, 24,19,0, 24,20,0, 24,21,0, 24,22,0, 24,23,0, 24,24,0, 24,25,0, 24,26,0, 24,27,0, 24,28,0, 24,29,0, 24,30,0, 24,31,0, 24,32,0, 24,33,0, 24,34,0, 24,35,0, ],72,12,0,0,28,35,3,4,1),
	)
Net2_Subnet4_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,5+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet4_R = And(Net2_Subnet4_R1,Net2_Subnet4_R2,Net2_Subnet4_R3,)
Net2_Subnet4_Formula = And(Net2_Subnet4_C,Net2_Subnet4_DR,Net2_Subnet4_R)
# Net = 2 Subnet = 5 | Left -> Right [20,46] Top -> Bottom [0,35]
# Range R1(24,24,0,35)
# Range R2(42,42,1,8)
### Disable edges outside window
Edge_Net_Subnet2[0:20,0:35+1,0:3+1,0:2+1,0:2+1,5]=exprzeros(25920)
Edge_Net_Subnet2[46:85+1,0:35+1,0:3+1,0:2+1,0:2+1,5]=exprzeros(51840)

### Consistency Constraints
Net2_Subnet5_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(20,46+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet5_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,5]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(20,46+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet5_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,5],Xor(Edge_Net_Subnet2[x,y,2,trend,1,5],Edge_Net_Subnet2[x,y,2,trend,2,5])),And(~Edge_Net_Subnet2[x,y,2,trend,0,5],~Edge_Net_Subnet2[x,y,2,trend,1,5],~Edge_Net_Subnet2[x,y,2,trend,2,5]))for x in range(20,46+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet5_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,5],Xor(Edge_Net_Subnet2[x,y,3,1,1,5],Edge_Net_Subnet2[x,y,3,1,2,5])),And(~Edge_Net_Subnet2[x,y,3,1,0,5],~Edge_Net_Subnet2[x,y,3,1,1,5],~Edge_Net_Subnet2[x,y,3,1,2,5]))for x in range(20,46+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet5_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,5],Xor(Edge_Net_Subnet2[x,y,1,trend,0,5],Edge_Net_Subnet2[x,y,1,trend,1,5])),And(~Edge_Net_Subnet2[x,y,1,trend,2,5],~Edge_Net_Subnet2[x,y,1,trend,0,5],~Edge_Net_Subnet2[x,y,1,trend,1,5]))for x in range(20,46+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet5_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,5], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,5)]))for trend in range(0,1+1)])for x in range(20,46+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,5], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(5+1,10)]))for trend in range(0,1+1)])for x in range(20,46+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,5], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,5)]))for trend in range(0,1+1)])for x in range(20,46+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,5], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(5+1,10)]))for trend in range(0,1+1)])for x in range(20,46+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet5_C = And(Net2_Subnet5_C1, Net2_Subnet5_C2,Net2_Subnet5_C3_ME1_Mask,Net2_Subnet5_C4_MINT1_Mask,Net2_Subnet5_C5_AIL2GIL_Mask,Net2_Subnet5_C6,)
### Design Rules
Net2_Subnet5_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(20,46+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet5_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,5], ~Edge_Net_Subnet2[x-1,y,1,1,1,5]), And(Edge_Net_Subnet2[x+1,y,1,1,1,5], Edge_Net_Subnet2[x+2,y,1,1,1,5], Edge_Net_Subnet2[x+3,y,1,1,1,5], ))for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,5], ~Edge_Net_Subnet2[x+1,y,1,1,1,5]), And(Edge_Net_Subnet2[x-1,y,1,1,1,5], Edge_Net_Subnet2[x-2,y,1,1,1,5], Edge_Net_Subnet2[x-3,y,1,1,1,5], ))for x in range(20,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,5], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,5], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(20,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,5], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(20,46+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,5], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(20,46+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5]), And(Edge_Net_Subnet2[x,y+1,1,0,0,5], Edge_Net_Subnet2[x,y+2,1,0,0,5], Edge_Net_Subnet2[x,y+3,1,0,0,5], ))for x in range(20,46+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5]), And(Edge_Net_Subnet2[x,y-1,1,0,0,5], Edge_Net_Subnet2[x,y-2,1,0,0,5], Edge_Net_Subnet2[x,y-3,1,0,0,5], ))for x in range(20,46+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge_Net_Subnet2[x,y-1,1,0,0,5]), And(Edge_Net_Subnet2[x,y+1,1,0,0,5], Edge_Net_Subnet2[x,y+2,1,0,0,5], Edge_Net_Subnet2[x,y+3,1,0,0,5], ))for x in range(20,46+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge_Net_Subnet2[x,y+1,1,0,0,5]), And(Edge_Net_Subnet2[x,y-1,1,0,0,5], Edge_Net_Subnet2[x,y-2,1,0,0,5], Edge_Net_Subnet2[x,y-3,1,0,0,5], ))for x in range(20,46+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet5_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(20,46+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(20,46+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(20,46+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(20,46+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(20,46+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(20,46+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet5_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,5], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,5], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(20,46+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,5], ~Edge_Net_Subnet2[x-1,y,3,1,mask,5]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,5], Edge_Net_Subnet2[x+2,y,3,1,mask,5], Edge_Net_Subnet2[x+3,y,3,1,mask,5], Edge_Net_Subnet2[x+4,y,3,1,mask,5], Edge_Net_Subnet2[x+5,y,3,1,mask,5], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,5], ~Edge_Net_Subnet2[x+1,y,3,1,mask,5]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,5], Edge_Net_Subnet2[x-2,y,3,1,mask,5], Edge_Net_Subnet2[x-3,y,3,1,mask,5], Edge_Net_Subnet2[x-4,y,3,1,mask,5], Edge_Net_Subnet2[x-5,y,3,1,mask,5], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,5], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,5], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,5], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,5], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,5], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(20,46+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,5], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(20,46+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,5], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,5], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(20,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,5], ~Edge_Net_Subnet2[x-1,y,2,1,mask,5]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,5], Edge_Net_Subnet2[x+2,y,2,1,mask,5], Edge_Net_Subnet2[x+3,y,2,1,mask,5], Edge_Net_Subnet2[x+4,y,2,1,mask,5], Edge_Net_Subnet2[x+5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,5], ~Edge_Net_Subnet2[x+1,y,2,1,mask,5]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,5], Edge_Net_Subnet2[x-2,y,2,1,mask,5], Edge_Net_Subnet2[x-3,y,2,1,mask,5], Edge_Net_Subnet2[x-4,y,2,1,mask,5], Edge_Net_Subnet2[x-5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,5], And(Edge_Net_Subnet2[x-1,y,2,1,mask,5], Edge_Net_Subnet2[x-2,y,2,1,mask,5], Edge_Net_Subnet2[x-3,y,2,1,mask,5], Edge_Net_Subnet2[x-4,y,2,1,mask,5], Edge_Net_Subnet2[x-5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(20,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,5], And(Edge_Net_Subnet2[x+1,y,2,1,mask,5], Edge_Net_Subnet2[x+2,y,2,1,mask,5], Edge_Net_Subnet2[x+3,y,2,1,mask,5], Edge_Net_Subnet2[x+4,y,2,1,mask,5], Edge_Net_Subnet2[x+5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(46-1,20)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,5], ~Edge_Net_Subnet2[x,y-1,2,0,mask,5]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,5], Edge_Net_Subnet2[x,y+2,2,0,mask,5], Edge_Net_Subnet2[x,y+3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,5], ~Edge_Net_Subnet2[x,y+1,2,0,mask,5]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,5], Edge_Net_Subnet2[x,y-2,2,0,mask,5], Edge_Net_Subnet2[x,y-3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,5], And(Edge_Net_Subnet2[x,y+1,2,0,mask,5], Edge_Net_Subnet2[x,y+2,2,0,mask,5], Edge_Net_Subnet2[x,y+3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,5], And(Edge_Net_Subnet2[x,y-1,2,0,mask,5], Edge_Net_Subnet2[x,y-2,2,0,mask,5], Edge_Net_Subnet2[x,y-3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,5], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,5], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(20,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,5], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,5], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,5], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(20,46+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,5], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(20,46+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet5_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,5], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,5], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet5_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,5], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(20,46+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,5], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(20,46+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,5], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,5], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,5], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,5], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(20,46+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,5], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,5], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,46+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,5], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,5], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,5], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,5], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,5], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,46+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,5], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,46+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,5], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,46+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,5], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,46+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet5_DR = And(Net2_Subnet5_DR_Trend, Net2_Subnet5_DR_GIL_HorMinWidth,Net2_Subnet5_DR_GIL_HorMinSpacing,Net2_Subnet5_DR_GIL_VerMinSpacing,Net2_Subnet5_DR_AIL2_VerMinWidth,Net2_Subnet5_DR_AIL2_VerMinSpacing,Net2_Subnet5_DR_VerAIL2_HorMinSpacing,Net2_Subnet5_DR_MINT1AB_HorMinWidth,Net2_Subnet5_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet5_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet5_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet5_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet5_DR_M1AB_MinWidth,Net2_Subnet5_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet5_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet5_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet5_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet5_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet5_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet5_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet5_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet5_DR_V0_HorMinSpacing,Net2_Subnet5_DR_V1_HorMinSpacing,Net2_Subnet5_DR_V0_VerMinSpacing,Net2_Subnet5_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet5_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[24,0,0,0, 24,1,0,0, 24,2,0,0, 24,3,0,0, 24,4,0,0, 24,5,0,0, 24,6,0,0, 24,7,0,0, 24,8,0,0, 24,9,0,0, 24,10,0,0, 24,11,0,0, 24,12,0,0, 24,13,0,0, 24,14,0,0, 24,15,0,0, 24,16,0,0, 24,17,0,0, 24,18,0,0, 24,19,0,0, 24,20,0,0, 24,21,0,0, 24,22,0,0, 24,23,0,0, 24,24,0,0, 24,25,0,0, 24,26,0,0, 24,27,0,0, 24,28,0,0, 24,29,0,0, 24,30,0,0, 24,31,0,0, 24,32,0,0, 24,33,0,0, 24,34,0,0, 24,35,0,0, ],36,20,0,1,46,35,3,5),
	RConstraints.R1(Edge_Net_Subnet2,[42,1,0,0, 42,2,0,0, 42,3,0,0, 42,4,0,0, 42,5,0,0, 42,6,0,0, 42,7,0,0, 42,8,0,0, ],8,20,0,1,46,35,3,5),
	).to_cnf()
Net2_Subnet5_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[24,0,0, 24,1,0, 24,2,0, 24,3,0, 24,4,0, 24,5,0, 24,6,0, 24,7,0, 24,8,0, 24,9,0, 24,10,0, 24,11,0, 24,12,0, 24,13,0, 24,14,0, 24,15,0, 24,16,0, 24,17,0, 24,18,0, 24,19,0, 24,20,0, 24,21,0, 24,22,0, 24,23,0, 24,24,0, 24,25,0, 24,26,0, 24,27,0, 24,28,0, 24,29,0, 24,30,0, 24,31,0, 24,32,0, 24,33,0, 24,34,0, 24,35,0, 42,1,0, 42,2,0, 42,3,0, 42,4,0, 42,5,0, 42,6,0, 42,7,0, 42,8,0, 42,9,0, ],45,20,0,0,46,35,3,5,1),
	)
Net2_Subnet5_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(20,46+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,5+1)])for x in range(20,46+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet5_R = And(Net2_Subnet5_R1,Net2_Subnet5_R2,Net2_Subnet5_R3,)
Net2_Subnet5_Formula = And(Net2_Subnet5_C,Net2_Subnet5_DR,Net2_Subnet5_R)
# Net = 2 Subnet = 6 | Left -> Right [38,50] Top -> Bottom [0,12]
# Range R1(42,42,1,8)
# Range R2(46,46,1,6)
### Disable edges outside window
Edge_Net_Subnet2[0:38,0:35+1,0:3+1,0:2+1,0:2+1,6]=exprzeros(49248)
Edge_Net_Subnet2[38:50,12:35+1,0:3+1,0:2+1,0:2+1,6]=exprzeros(10368)
Edge_Net_Subnet2[50:85+1,0:35+1,0:3+1,0:2+1,0:2+1,6]=exprzeros(46656)

### Consistency Constraints
Net2_Subnet6_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(38,50+1)])for y in range(0,12+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet6_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,6]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(38,50+1)])for y in range(0,12+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet6_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,6],Xor(Edge_Net_Subnet2[x,y,2,trend,1,6],Edge_Net_Subnet2[x,y,2,trend,2,6])),And(~Edge_Net_Subnet2[x,y,2,trend,0,6],~Edge_Net_Subnet2[x,y,2,trend,1,6],~Edge_Net_Subnet2[x,y,2,trend,2,6]))for x in range(38,50+1)])for y in range(0,12+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet6_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,6],Xor(Edge_Net_Subnet2[x,y,3,1,1,6],Edge_Net_Subnet2[x,y,3,1,2,6])),And(~Edge_Net_Subnet2[x,y,3,1,0,6],~Edge_Net_Subnet2[x,y,3,1,1,6],~Edge_Net_Subnet2[x,y,3,1,2,6]))for x in range(38,50+1)])for y in range(0,12+1)]).to_cnf()
Net2_Subnet6_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,6],Xor(Edge_Net_Subnet2[x,y,1,trend,0,6],Edge_Net_Subnet2[x,y,1,trend,1,6])),And(~Edge_Net_Subnet2[x,y,1,trend,2,6],~Edge_Net_Subnet2[x,y,1,trend,0,6],~Edge_Net_Subnet2[x,y,1,trend,1,6]))for x in range(38,50+1)])for y in range(0,12+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet6_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,6], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,6)]))for trend in range(0,1+1)])for x in range(38,50+1)])for y in range(0,12+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,6], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(6+1,10)]))for trend in range(0,1+1)])for x in range(38,50+1)])for y in range(0,12+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,6], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,6)]))for trend in range(0,1+1)])for x in range(38,50+1)])for y in range(0,12+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,6], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(6+1,10)]))for trend in range(0,1+1)])for x in range(38,50+1)])for y in range(0,12+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet6_C = And(Net2_Subnet6_C1, Net2_Subnet6_C2,Net2_Subnet6_C3_ME1_Mask,Net2_Subnet6_C4_MINT1_Mask,Net2_Subnet6_C5_AIL2GIL_Mask,Net2_Subnet6_C6,)
### Design Rules
Net2_Subnet6_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(38,50+1)])for y in range(0,12+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet6_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,6], ~Edge_Net_Subnet2[x-1,y,1,1,1,6]), And(Edge_Net_Subnet2[x+1,y,1,1,1,6], Edge_Net_Subnet2[x+2,y,1,1,1,6], Edge_Net_Subnet2[x+3,y,1,1,1,6], ))for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,6], ~Edge_Net_Subnet2[x+1,y,1,1,1,6]), And(Edge_Net_Subnet2[x-1,y,1,1,1,6], Edge_Net_Subnet2[x-2,y,1,1,1,6], Edge_Net_Subnet2[x-3,y,1,1,1,6], ))for x in range(38,50+1)])for y in range(0,12+1)])
	).to_cnf()
Net2_Subnet6_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,6], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,6], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(38,50+1)])for y in range(0,12+1)])
	).to_cnf()
Net2_Subnet6_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,6], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,6], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(38,50+1)])for y in range(3,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,6]), And(Edge_Net_Subnet2[x,y+1,1,0,0,6], Edge_Net_Subnet2[x,y+2,1,0,0,6], Edge_Net_Subnet2[x,y+3,1,0,0,6], ))for x in range(38,50+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,6], ~Edge_Net_Subnet2[x,y-1,1,0,0,6]), And(Edge_Net_Subnet2[x,y+1,1,0,0,6], Edge_Net_Subnet2[x,y+2,1,0,0,6], Edge_Net_Subnet2[x,y+3,1,0,0,6], ))for x in range(38,50+1)])for y in range(0+1,12+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,6], ~Edge_Net_Subnet2[x,y+1,1,0,0,6]), And(Edge_Net_Subnet2[x,y-1,1,0,0,6], Edge_Net_Subnet2[x,y-2,1,0,0,6], Edge_Net_Subnet2[x,y-3,1,0,0,6], ))for x in range(38,50+1)])for y in range(0+3,12+1)])
	).to_cnf()
Net2_Subnet6_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,6], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(38,50+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,6], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(38,50+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,6], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(38,50+1)])for y in range(0+3,12+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,6], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(38,50+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet6_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,6], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,6], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(38,50+1)])for y in range(0,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,6], ~Edge_Net_Subnet2[x-1,y,3,1,mask,6]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,6], Edge_Net_Subnet2[x+2,y,3,1,mask,6], Edge_Net_Subnet2[x+3,y,3,1,mask,6], Edge_Net_Subnet2[x+4,y,3,1,mask,6], Edge_Net_Subnet2[x+5,y,3,1,mask,6], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,6], ~Edge_Net_Subnet2[x+1,y,3,1,mask,6]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,6], Edge_Net_Subnet2[x-2,y,3,1,mask,6], Edge_Net_Subnet2[x-3,y,3,1,mask,6], Edge_Net_Subnet2[x-4,y,3,1,mask,6], Edge_Net_Subnet2[x-5,y,3,1,mask,6], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,6], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,6], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(3,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,6], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,6], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)])
	).to_cnf()
Net2_Subnet6_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,6], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,6], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(38,50+1)])for y in range(2,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,6], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,6], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(38,50+1)])for y in range(0,12+1)])
	).to_cnf()
Net2_Subnet6_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,6], ~Edge_Net_Subnet2[x-1,y,2,1,mask,6]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,6], Edge_Net_Subnet2[x+2,y,2,1,mask,6], Edge_Net_Subnet2[x+3,y,2,1,mask,6], Edge_Net_Subnet2[x+4,y,2,1,mask,6], Edge_Net_Subnet2[x+5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,6], ~Edge_Net_Subnet2[x+1,y,2,1,mask,6]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,6], Edge_Net_Subnet2[x-2,y,2,1,mask,6], Edge_Net_Subnet2[x-3,y,2,1,mask,6], Edge_Net_Subnet2[x-4,y,2,1,mask,6], Edge_Net_Subnet2[x-5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,6], And(Edge_Net_Subnet2[x-1,y,2,1,mask,6], Edge_Net_Subnet2[x-2,y,2,1,mask,6], Edge_Net_Subnet2[x-3,y,2,1,mask,6], Edge_Net_Subnet2[x-4,y,2,1,mask,6], Edge_Net_Subnet2[x-5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(38,38+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,6], And(Edge_Net_Subnet2[x+1,y,2,1,mask,6], Edge_Net_Subnet2[x+2,y,2,1,mask,6], Edge_Net_Subnet2[x+3,y,2,1,mask,6], Edge_Net_Subnet2[x+4,y,2,1,mask,6], Edge_Net_Subnet2[x+5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(50-1,38)])for y in range(0,12+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,6], ~Edge_Net_Subnet2[x,y-1,2,0,mask,6]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,6], Edge_Net_Subnet2[x,y+2,2,0,mask,6], Edge_Net_Subnet2[x,y+3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0+1,12+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,6], ~Edge_Net_Subnet2[x,y+1,2,0,mask,6]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,6], Edge_Net_Subnet2[x,y-2,2,0,mask,6], Edge_Net_Subnet2[x,y-3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0+3,12+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,6], And(Edge_Net_Subnet2[x,y+1,2,0,mask,6], Edge_Net_Subnet2[x,y+2,2,0,mask,6], Edge_Net_Subnet2[x,y+3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,6], And(Edge_Net_Subnet2[x,y-1,2,0,mask,6], Edge_Net_Subnet2[x,y-2,2,0,mask,6], Edge_Net_Subnet2[x,y-3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(12,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,6], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,6], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(38,50+1)])for y in range(0,12+1)])
	).to_cnf()
Net2_Subnet6_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,6], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,6], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)])
	).to_cnf()
Net2_Subnet6_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,6], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(38,50+1)])for y in range(2,12+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,6], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(38,50+1)])for y in range(0,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,6], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(4,12+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,6], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,6], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,6], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(38,50+1)])for y in range(3,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,6], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,6], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(4,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,6], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,6], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(38,50+1)])for y in range(0,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,6], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,6], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,6], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,6], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(38,50+1)])for y in range(0,12+1)])
	).to_cnf()
Net2_Subnet6_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,6], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,6], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(38,50+1)])for y in range(0,12+1)])
	).to_cnf()
Net2_Subnet6_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,6], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,6], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(38,50+1)])for y in range(2,12+1)]),
	).to_cnf()
Net2_Subnet6_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,6], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(38,50+1)])for y in range(0,12+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,6], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(38,50+1)])for y in range(2,12+1)]),
	).to_cnf()
Net2_Subnet6_DR = And(Net2_Subnet6_DR_Trend, Net2_Subnet6_DR_GIL_HorMinWidth,Net2_Subnet6_DR_GIL_HorMinSpacing,Net2_Subnet6_DR_GIL_VerMinSpacing,Net2_Subnet6_DR_AIL2_VerMinWidth,Net2_Subnet6_DR_AIL2_VerMinSpacing,Net2_Subnet6_DR_VerAIL2_HorMinSpacing,Net2_Subnet6_DR_MINT1AB_HorMinWidth,Net2_Subnet6_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet6_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet6_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet6_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet6_DR_M1AB_MinWidth,Net2_Subnet6_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet6_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet6_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet6_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet6_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet6_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet6_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet6_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet6_DR_V0_HorMinSpacing,Net2_Subnet6_DR_V1_HorMinSpacing,Net2_Subnet6_DR_V0_VerMinSpacing,Net2_Subnet6_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet6_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[42,1,0,0, 42,2,0,0, 42,3,0,0, 42,4,0,0, 42,5,0,0, 42,6,0,0, 42,7,0,0, 42,8,0,0, ],8,38,0,1,50,12,3,6),
	RConstraints.R1(Edge_Net_Subnet2,[46,1,0,0, 46,2,0,0, 46,3,0,0, 46,4,0,0, 46,5,0,0, 46,6,0,0, ],6,38,0,1,50,12,3,6),
	).to_cnf()
Net2_Subnet6_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[42,1,0, 42,2,0, 42,3,0, 42,4,0, 42,5,0, 42,6,0, 42,7,0, 42,8,0, 42,9,0, 46,1,0, 46,2,0, 46,3,0, 46,4,0, 46,5,0, 46,6,0, 46,7,0, ],16,38,0,0,50,12,3,6,1),
	)
Net2_Subnet6_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(38,50+1)])for y in range(0,12+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,5+1)])for x in range(38,50+1)])for y in range(0,12+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet6_R = And(Net2_Subnet6_R1,Net2_Subnet6_R2,Net2_Subnet6_R3,)
Net2_Subnet6_Formula = And(Net2_Subnet6_C,Net2_Subnet6_DR,Net2_Subnet6_R)
# Net = 2 Subnet = 7 | Left -> Right [42,62] Top -> Bottom [0,18]
# Range R1(46,46,1,6)
# Range R2(58,58,1,14)
### Disable edges outside window
Edge_Net_Subnet2[0:42,0:35+1,0:3+1,0:2+1,0:2+1,7]=exprzeros(54432)
Edge_Net_Subnet2[42:62,18:35+1,0:3+1,0:2+1,0:2+1,7]=exprzeros(12960)
Edge_Net_Subnet2[62:85+1,0:35+1,0:3+1,0:2+1,0:2+1,7]=exprzeros(31104)

### Consistency Constraints
Net2_Subnet7_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(42,62+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet7_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,7]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(42,62+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet7_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,7],Xor(Edge_Net_Subnet2[x,y,2,trend,1,7],Edge_Net_Subnet2[x,y,2,trend,2,7])),And(~Edge_Net_Subnet2[x,y,2,trend,0,7],~Edge_Net_Subnet2[x,y,2,trend,1,7],~Edge_Net_Subnet2[x,y,2,trend,2,7]))for x in range(42,62+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet7_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,7],Xor(Edge_Net_Subnet2[x,y,3,1,1,7],Edge_Net_Subnet2[x,y,3,1,2,7])),And(~Edge_Net_Subnet2[x,y,3,1,0,7],~Edge_Net_Subnet2[x,y,3,1,1,7],~Edge_Net_Subnet2[x,y,3,1,2,7]))for x in range(42,62+1)])for y in range(0,18+1)]).to_cnf()
Net2_Subnet7_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,7],Xor(Edge_Net_Subnet2[x,y,1,trend,0,7],Edge_Net_Subnet2[x,y,1,trend,1,7])),And(~Edge_Net_Subnet2[x,y,1,trend,2,7],~Edge_Net_Subnet2[x,y,1,trend,0,7],~Edge_Net_Subnet2[x,y,1,trend,1,7]))for x in range(42,62+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet7_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,7], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,7)]))for trend in range(0,1+1)])for x in range(42,62+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,7], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(7+1,10)]))for trend in range(0,1+1)])for x in range(42,62+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,7], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,7)]))for trend in range(0,1+1)])for x in range(42,62+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,7], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(7+1,10)]))for trend in range(0,1+1)])for x in range(42,62+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet7_C = And(Net2_Subnet7_C1, Net2_Subnet7_C2,Net2_Subnet7_C3_ME1_Mask,Net2_Subnet7_C4_MINT1_Mask,Net2_Subnet7_C5_AIL2GIL_Mask,Net2_Subnet7_C6,)
### Design Rules
Net2_Subnet7_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(42,62+1)])for y in range(0,18+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet7_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,7], ~Edge_Net_Subnet2[x-1,y,1,1,1,7]), And(Edge_Net_Subnet2[x+1,y,1,1,1,7], Edge_Net_Subnet2[x+2,y,1,1,1,7], Edge_Net_Subnet2[x+3,y,1,1,1,7], ))for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,7], ~Edge_Net_Subnet2[x+1,y,1,1,1,7]), And(Edge_Net_Subnet2[x-1,y,1,1,1,7], Edge_Net_Subnet2[x-2,y,1,1,1,7], Edge_Net_Subnet2[x-3,y,1,1,1,7], ))for x in range(42,62+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet7_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,7], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,7], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(42,62+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet7_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,7], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,7], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(42,62+1)])for y in range(3,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7]), And(Edge_Net_Subnet2[x,y+1,1,0,0,7], Edge_Net_Subnet2[x,y+2,1,0,0,7], Edge_Net_Subnet2[x,y+3,1,0,0,7], ))for x in range(42,62+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge_Net_Subnet2[x,y-1,1,0,0,7]), And(Edge_Net_Subnet2[x,y+1,1,0,0,7], Edge_Net_Subnet2[x,y+2,1,0,0,7], Edge_Net_Subnet2[x,y+3,1,0,0,7], ))for x in range(42,62+1)])for y in range(0+1,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge_Net_Subnet2[x,y+1,1,0,0,7]), And(Edge_Net_Subnet2[x,y-1,1,0,0,7], Edge_Net_Subnet2[x,y-2,1,0,0,7], Edge_Net_Subnet2[x,y-3,1,0,0,7], ))for x in range(42,62+1)])for y in range(0+3,18+1)])
	).to_cnf()
Net2_Subnet7_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(42,62+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(42,62+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(42,62+1)])for y in range(0+3,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(42,62+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet7_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,7], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,7], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(42,62+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,7], ~Edge_Net_Subnet2[x-1,y,3,1,mask,7]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,7], Edge_Net_Subnet2[x+2,y,3,1,mask,7], Edge_Net_Subnet2[x+3,y,3,1,mask,7], Edge_Net_Subnet2[x+4,y,3,1,mask,7], Edge_Net_Subnet2[x+5,y,3,1,mask,7], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,7], ~Edge_Net_Subnet2[x+1,y,3,1,mask,7]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,7], Edge_Net_Subnet2[x-2,y,3,1,mask,7], Edge_Net_Subnet2[x-3,y,3,1,mask,7], Edge_Net_Subnet2[x-4,y,3,1,mask,7], Edge_Net_Subnet2[x-5,y,3,1,mask,7], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,7], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,7], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(3,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,7], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,7], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet7_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,7], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,7], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(42,62+1)])for y in range(2,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,7], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,7], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(42,62+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet7_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,7], ~Edge_Net_Subnet2[x-1,y,2,1,mask,7]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,7], Edge_Net_Subnet2[x+2,y,2,1,mask,7], Edge_Net_Subnet2[x+3,y,2,1,mask,7], Edge_Net_Subnet2[x+4,y,2,1,mask,7], Edge_Net_Subnet2[x+5,y,2,1,mask,7], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,7], ~Edge_Net_Subnet2[x+1,y,2,1,mask,7]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,7], Edge_Net_Subnet2[x-2,y,2,1,mask,7], Edge_Net_Subnet2[x-3,y,2,1,mask,7], Edge_Net_Subnet2[x-4,y,2,1,mask,7], Edge_Net_Subnet2[x-5,y,2,1,mask,7], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,7], And(Edge_Net_Subnet2[x-1,y,2,1,mask,7], Edge_Net_Subnet2[x-2,y,2,1,mask,7], Edge_Net_Subnet2[x-3,y,2,1,mask,7], Edge_Net_Subnet2[x-4,y,2,1,mask,7], Edge_Net_Subnet2[x-5,y,2,1,mask,7], ))for mask in range(1,2+1)])for x in range(42,42+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,7], And(Edge_Net_Subnet2[x+1,y,2,1,mask,7], Edge_Net_Subnet2[x+2,y,2,1,mask,7], Edge_Net_Subnet2[x+3,y,2,1,mask,7], Edge_Net_Subnet2[x+4,y,2,1,mask,7], Edge_Net_Subnet2[x+5,y,2,1,mask,7], ))for mask in range(1,2+1)])for x in range(62-1,42)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,7], ~Edge_Net_Subnet2[x,y-1,2,0,mask,7]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,7], Edge_Net_Subnet2[x,y+2,2,0,mask,7], Edge_Net_Subnet2[x,y+3,2,0,mask,7], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0+1,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,7], ~Edge_Net_Subnet2[x,y+1,2,0,mask,7]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,7], Edge_Net_Subnet2[x,y-2,2,0,mask,7], Edge_Net_Subnet2[x,y-3,2,0,mask,7], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0+3,18+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,7], And(Edge_Net_Subnet2[x,y+1,2,0,mask,7], Edge_Net_Subnet2[x,y+2,2,0,mask,7], Edge_Net_Subnet2[x,y+3,2,0,mask,7], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,7], And(Edge_Net_Subnet2[x,y-1,2,0,mask,7], Edge_Net_Subnet2[x,y-2,2,0,mask,7], Edge_Net_Subnet2[x,y-3,2,0,mask,7], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(18,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,7], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,7], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(42,62+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet7_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,7], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,7], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet7_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,7], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(42,62+1)])for y in range(2,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,7], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(42,62+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,7], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(4,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,7], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,7], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,7], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(42,62+1)])for y in range(3,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,7], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,7], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(4,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,7], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,7], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(42,62+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,7], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,7], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,7], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,7], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(42,62+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet7_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,7], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,7], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(42,62+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet7_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,7], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,7], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(42,62+1)])for y in range(2,18+1)]),
	).to_cnf()
Net2_Subnet7_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,7], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(42,62+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,7], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(42,62+1)])for y in range(2,18+1)]),
	).to_cnf()
Net2_Subnet7_DR = And(Net2_Subnet7_DR_Trend, Net2_Subnet7_DR_GIL_HorMinWidth,Net2_Subnet7_DR_GIL_HorMinSpacing,Net2_Subnet7_DR_GIL_VerMinSpacing,Net2_Subnet7_DR_AIL2_VerMinWidth,Net2_Subnet7_DR_AIL2_VerMinSpacing,Net2_Subnet7_DR_VerAIL2_HorMinSpacing,Net2_Subnet7_DR_MINT1AB_HorMinWidth,Net2_Subnet7_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet7_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet7_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet7_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet7_DR_M1AB_MinWidth,Net2_Subnet7_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet7_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet7_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet7_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet7_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet7_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet7_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet7_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet7_DR_V0_HorMinSpacing,Net2_Subnet7_DR_V1_HorMinSpacing,Net2_Subnet7_DR_V0_VerMinSpacing,Net2_Subnet7_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet7_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[46,1,0,0, 46,2,0,0, 46,3,0,0, 46,4,0,0, 46,5,0,0, 46,6,0,0, ],6,42,0,1,62,18,3,7),
	RConstraints.R1(Edge_Net_Subnet2,[58,1,0,0, 58,2,0,0, 58,3,0,0, 58,4,0,0, 58,5,0,0, 58,6,0,0, 58,7,0,0, 58,8,0,0, 58,9,0,0, 58,10,0,0, 58,11,0,0, 58,12,0,0, 58,13,0,0, 58,14,0,0, ],14,42,0,1,62,18,3,7),
	).to_cnf()
Net2_Subnet7_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[46,1,0, 46,2,0, 46,3,0, 46,4,0, 46,5,0, 46,6,0, 46,7,0, 58,1,0, 58,2,0, 58,3,0, 58,4,0, 58,5,0, 58,6,0, 58,7,0, 58,8,0, 58,9,0, 58,10,0, 58,11,0, 58,12,0, 58,13,0, 58,14,0, 58,15,0, ],22,42,0,0,62,18,3,7,1),
	)
Net2_Subnet7_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(42,62+1)])for y in range(0,18+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,5+1)])for x in range(42,62+1)])for y in range(0,18+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet7_R = And(Net2_Subnet7_R1,Net2_Subnet7_R2,Net2_Subnet7_R3,)
Net2_Subnet7_Formula = And(Net2_Subnet7_C,Net2_Subnet7_DR,Net2_Subnet7_R)
# Net = 2 Subnet = 8 | Left -> Right [54,66] Top -> Bottom [0,18]
# Range R1(58,58,1,14)
# Range R2(62,62,1,14)
### Disable edges outside window
Edge_Net_Subnet2[0:54,0:35+1,0:3+1,0:2+1,0:2+1,8]=exprzeros(69984)
Edge_Net_Subnet2[54:66,18:35+1,0:3+1,0:2+1,0:2+1,8]=exprzeros(7776)
Edge_Net_Subnet2[66:85+1,0:35+1,0:3+1,0:2+1,0:2+1,8]=exprzeros(25920)

### Consistency Constraints
Net2_Subnet8_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(54,66+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet8_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,8]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(54,66+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet8_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,8],Xor(Edge_Net_Subnet2[x,y,2,trend,1,8],Edge_Net_Subnet2[x,y,2,trend,2,8])),And(~Edge_Net_Subnet2[x,y,2,trend,0,8],~Edge_Net_Subnet2[x,y,2,trend,1,8],~Edge_Net_Subnet2[x,y,2,trend,2,8]))for x in range(54,66+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet8_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,8],Xor(Edge_Net_Subnet2[x,y,3,1,1,8],Edge_Net_Subnet2[x,y,3,1,2,8])),And(~Edge_Net_Subnet2[x,y,3,1,0,8],~Edge_Net_Subnet2[x,y,3,1,1,8],~Edge_Net_Subnet2[x,y,3,1,2,8]))for x in range(54,66+1)])for y in range(0,18+1)]).to_cnf()
Net2_Subnet8_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,8],Xor(Edge_Net_Subnet2[x,y,1,trend,0,8],Edge_Net_Subnet2[x,y,1,trend,1,8])),And(~Edge_Net_Subnet2[x,y,1,trend,2,8],~Edge_Net_Subnet2[x,y,1,trend,0,8],~Edge_Net_Subnet2[x,y,1,trend,1,8]))for x in range(54,66+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet8_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,8], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,8)]))for trend in range(0,1+1)])for x in range(54,66+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,8], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(8+1,10)]))for trend in range(0,1+1)])for x in range(54,66+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,8], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,8)]))for trend in range(0,1+1)])for x in range(54,66+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,8], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(8+1,10)]))for trend in range(0,1+1)])for x in range(54,66+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet8_C = And(Net2_Subnet8_C1, Net2_Subnet8_C2,Net2_Subnet8_C3_ME1_Mask,Net2_Subnet8_C4_MINT1_Mask,Net2_Subnet8_C5_AIL2GIL_Mask,Net2_Subnet8_C6,)
### Design Rules
Net2_Subnet8_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(54,66+1)])for y in range(0,18+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet8_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,8], ~Edge_Net_Subnet2[x-1,y,1,1,1,8]), And(Edge_Net_Subnet2[x+1,y,1,1,1,8], Edge_Net_Subnet2[x+2,y,1,1,1,8], Edge_Net_Subnet2[x+3,y,1,1,1,8], ))for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,8], ~Edge_Net_Subnet2[x+1,y,1,1,1,8]), And(Edge_Net_Subnet2[x-1,y,1,1,1,8], Edge_Net_Subnet2[x-2,y,1,1,1,8], Edge_Net_Subnet2[x-3,y,1,1,1,8], ))for x in range(54,66+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet8_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,8], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,8], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(54,66+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet8_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,8], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,8], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(54,66+1)])for y in range(3,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8]), And(Edge_Net_Subnet2[x,y+1,1,0,0,8], Edge_Net_Subnet2[x,y+2,1,0,0,8], Edge_Net_Subnet2[x,y+3,1,0,0,8], ))for x in range(54,66+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge_Net_Subnet2[x,y-1,1,0,0,8]), And(Edge_Net_Subnet2[x,y+1,1,0,0,8], Edge_Net_Subnet2[x,y+2,1,0,0,8], Edge_Net_Subnet2[x,y+3,1,0,0,8], ))for x in range(54,66+1)])for y in range(0+1,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge_Net_Subnet2[x,y+1,1,0,0,8]), And(Edge_Net_Subnet2[x,y-1,1,0,0,8], Edge_Net_Subnet2[x,y-2,1,0,0,8], Edge_Net_Subnet2[x,y-3,1,0,0,8], ))for x in range(54,66+1)])for y in range(0+3,18+1)])
	).to_cnf()
Net2_Subnet8_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(54,66+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(54,66+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(54,66+1)])for y in range(0+3,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(54,66+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet8_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,8], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,8], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(54,66+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,8], ~Edge_Net_Subnet2[x-1,y,3,1,mask,8]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,8], Edge_Net_Subnet2[x+2,y,3,1,mask,8], Edge_Net_Subnet2[x+3,y,3,1,mask,8], Edge_Net_Subnet2[x+4,y,3,1,mask,8], Edge_Net_Subnet2[x+5,y,3,1,mask,8], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,8], ~Edge_Net_Subnet2[x+1,y,3,1,mask,8]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,8], Edge_Net_Subnet2[x-2,y,3,1,mask,8], Edge_Net_Subnet2[x-3,y,3,1,mask,8], Edge_Net_Subnet2[x-4,y,3,1,mask,8], Edge_Net_Subnet2[x-5,y,3,1,mask,8], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,8], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,8], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(3,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,8], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,8], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet8_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,8], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,8], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(54,66+1)])for y in range(2,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,8], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,8], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(54,66+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet8_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,8], ~Edge_Net_Subnet2[x-1,y,2,1,mask,8]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,8], Edge_Net_Subnet2[x+2,y,2,1,mask,8], Edge_Net_Subnet2[x+3,y,2,1,mask,8], Edge_Net_Subnet2[x+4,y,2,1,mask,8], Edge_Net_Subnet2[x+5,y,2,1,mask,8], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,8], ~Edge_Net_Subnet2[x+1,y,2,1,mask,8]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,8], Edge_Net_Subnet2[x-2,y,2,1,mask,8], Edge_Net_Subnet2[x-3,y,2,1,mask,8], Edge_Net_Subnet2[x-4,y,2,1,mask,8], Edge_Net_Subnet2[x-5,y,2,1,mask,8], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,8], And(Edge_Net_Subnet2[x-1,y,2,1,mask,8], Edge_Net_Subnet2[x-2,y,2,1,mask,8], Edge_Net_Subnet2[x-3,y,2,1,mask,8], Edge_Net_Subnet2[x-4,y,2,1,mask,8], Edge_Net_Subnet2[x-5,y,2,1,mask,8], ))for mask in range(1,2+1)])for x in range(54,54+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,8], And(Edge_Net_Subnet2[x+1,y,2,1,mask,8], Edge_Net_Subnet2[x+2,y,2,1,mask,8], Edge_Net_Subnet2[x+3,y,2,1,mask,8], Edge_Net_Subnet2[x+4,y,2,1,mask,8], Edge_Net_Subnet2[x+5,y,2,1,mask,8], ))for mask in range(1,2+1)])for x in range(66-1,54)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,8], ~Edge_Net_Subnet2[x,y-1,2,0,mask,8]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,8], Edge_Net_Subnet2[x,y+2,2,0,mask,8], Edge_Net_Subnet2[x,y+3,2,0,mask,8], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0+1,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,8], ~Edge_Net_Subnet2[x,y+1,2,0,mask,8]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,8], Edge_Net_Subnet2[x,y-2,2,0,mask,8], Edge_Net_Subnet2[x,y-3,2,0,mask,8], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0+3,18+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,8], And(Edge_Net_Subnet2[x,y+1,2,0,mask,8], Edge_Net_Subnet2[x,y+2,2,0,mask,8], Edge_Net_Subnet2[x,y+3,2,0,mask,8], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,8], And(Edge_Net_Subnet2[x,y-1,2,0,mask,8], Edge_Net_Subnet2[x,y-2,2,0,mask,8], Edge_Net_Subnet2[x,y-3,2,0,mask,8], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(18,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,8], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,8], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(54,66+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet8_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,8], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,8], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet8_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,8], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(54,66+1)])for y in range(2,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,8], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(54,66+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,8], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(4,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,8], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,8], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,8], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(54,66+1)])for y in range(3,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,8], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,8], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(4,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,8], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,8], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(54,66+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,8], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,8], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,8], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,8], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(54,66+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet8_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,8], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,8], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(54,66+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet8_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,8], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,8], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(54,66+1)])for y in range(2,18+1)]),
	).to_cnf()
Net2_Subnet8_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,8], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(54,66+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,8], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(54,66+1)])for y in range(2,18+1)]),
	).to_cnf()
Net2_Subnet8_DR = And(Net2_Subnet8_DR_Trend, Net2_Subnet8_DR_GIL_HorMinWidth,Net2_Subnet8_DR_GIL_HorMinSpacing,Net2_Subnet8_DR_GIL_VerMinSpacing,Net2_Subnet8_DR_AIL2_VerMinWidth,Net2_Subnet8_DR_AIL2_VerMinSpacing,Net2_Subnet8_DR_VerAIL2_HorMinSpacing,Net2_Subnet8_DR_MINT1AB_HorMinWidth,Net2_Subnet8_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet8_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet8_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet8_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet8_DR_M1AB_MinWidth,Net2_Subnet8_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet8_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet8_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet8_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet8_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet8_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet8_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet8_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet8_DR_V0_HorMinSpacing,Net2_Subnet8_DR_V1_HorMinSpacing,Net2_Subnet8_DR_V0_VerMinSpacing,Net2_Subnet8_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet8_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[58,1,0,0, 58,2,0,0, 58,3,0,0, 58,4,0,0, 58,5,0,0, 58,6,0,0, 58,7,0,0, 58,8,0,0, 58,9,0,0, 58,10,0,0, 58,11,0,0, 58,12,0,0, 58,13,0,0, 58,14,0,0, ],14,54,0,1,66,18,3,8),
	RConstraints.R1(Edge_Net_Subnet2,[62,1,0,0, 62,2,0,0, 62,3,0,0, 62,4,0,0, 62,5,0,0, 62,6,0,0, 62,7,0,0, 62,8,0,0, 62,9,0,0, 62,10,0,0, 62,11,0,0, 62,12,0,0, 62,13,0,0, 62,14,0,0, ],14,54,0,1,66,18,3,8),
	).to_cnf()
Net2_Subnet8_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[58,1,0, 58,2,0, 58,3,0, 58,4,0, 58,5,0, 58,6,0, 58,7,0, 58,8,0, 58,9,0, 58,10,0, 58,11,0, 58,12,0, 58,13,0, 58,14,0, 58,15,0, 62,1,0, 62,2,0, 62,3,0, 62,4,0, 62,5,0, 62,6,0, 62,7,0, 62,8,0, 62,9,0, 62,10,0, 62,11,0, 62,12,0, 62,13,0, 62,14,0, 62,15,0, ],30,54,0,0,66,18,3,8,1),
	)
Net2_Subnet8_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(54,66+1)])for y in range(0,18+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,5+1)])for x in range(54,66+1)])for y in range(0,18+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet8_R = And(Net2_Subnet8_R1,Net2_Subnet8_R2,Net2_Subnet8_R3,)
Net2_Subnet8_Formula = And(Net2_Subnet8_C,Net2_Subnet8_DR,Net2_Subnet8_R)
# Net = 2 Subnet = 9 | Left -> Right [58,78] Top -> Bottom [0,18]
# Range R1(62,62,1,14)
# Range R2(74,74,1,8)
### Disable edges outside window
Edge_Net_Subnet2[0:58,0:35+1,0:3+1,0:2+1,0:2+1,9]=exprzeros(75168)
Edge_Net_Subnet2[58:78,18:35+1,0:3+1,0:2+1,0:2+1,9]=exprzeros(12960)
Edge_Net_Subnet2[78:85+1,0:35+1,0:3+1,0:2+1,0:2+1,9]=exprzeros(10368)

### Consistency Constraints
Net2_Subnet9_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(58,78+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet9_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,9]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(58,78+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet9_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,9],Xor(Edge_Net_Subnet2[x,y,2,trend,1,9],Edge_Net_Subnet2[x,y,2,trend,2,9])),And(~Edge_Net_Subnet2[x,y,2,trend,0,9],~Edge_Net_Subnet2[x,y,2,trend,1,9],~Edge_Net_Subnet2[x,y,2,trend,2,9]))for x in range(58,78+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet9_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,9],Xor(Edge_Net_Subnet2[x,y,3,1,1,9],Edge_Net_Subnet2[x,y,3,1,2,9])),And(~Edge_Net_Subnet2[x,y,3,1,0,9],~Edge_Net_Subnet2[x,y,3,1,1,9],~Edge_Net_Subnet2[x,y,3,1,2,9]))for x in range(58,78+1)])for y in range(0,18+1)]).to_cnf()
Net2_Subnet9_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,9],Xor(Edge_Net_Subnet2[x,y,1,trend,0,9],Edge_Net_Subnet2[x,y,1,trend,1,9])),And(~Edge_Net_Subnet2[x,y,1,trend,2,9],~Edge_Net_Subnet2[x,y,1,trend,0,9],~Edge_Net_Subnet2[x,y,1,trend,1,9]))for x in range(58,78+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet9_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,9], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,9)]))for trend in range(0,1+1)])for x in range(58,78+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,9], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,9)]))for trend in range(0,1+1)])for x in range(58,78+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet9_C = And(Net2_Subnet9_C1, Net2_Subnet9_C2,Net2_Subnet9_C3_ME1_Mask,Net2_Subnet9_C4_MINT1_Mask,Net2_Subnet9_C5_AIL2GIL_Mask,Net2_Subnet9_C6,)
### Design Rules
Net2_Subnet9_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(58,78+1)])for y in range(0,18+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet9_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,9], ~Edge_Net_Subnet2[x-1,y,1,1,1,9]), And(Edge_Net_Subnet2[x+1,y,1,1,1,9], Edge_Net_Subnet2[x+2,y,1,1,1,9], Edge_Net_Subnet2[x+3,y,1,1,1,9], ))for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,9], ~Edge_Net_Subnet2[x+1,y,1,1,1,9]), And(Edge_Net_Subnet2[x-1,y,1,1,1,9], Edge_Net_Subnet2[x-2,y,1,1,1,9], Edge_Net_Subnet2[x-3,y,1,1,1,9], ))for x in range(58,78+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet9_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,9], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,9], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(58,78+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet9_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,9], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,9], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(58,78+1)])for y in range(3,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,9]), And(Edge_Net_Subnet2[x,y+1,1,0,0,9], Edge_Net_Subnet2[x,y+2,1,0,0,9], Edge_Net_Subnet2[x,y+3,1,0,0,9], ))for x in range(58,78+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,9], ~Edge_Net_Subnet2[x,y-1,1,0,0,9]), And(Edge_Net_Subnet2[x,y+1,1,0,0,9], Edge_Net_Subnet2[x,y+2,1,0,0,9], Edge_Net_Subnet2[x,y+3,1,0,0,9], ))for x in range(58,78+1)])for y in range(0+1,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,9], ~Edge_Net_Subnet2[x,y+1,1,0,0,9]), And(Edge_Net_Subnet2[x,y-1,1,0,0,9], Edge_Net_Subnet2[x,y-2,1,0,0,9], Edge_Net_Subnet2[x,y-3,1,0,0,9], ))for x in range(58,78+1)])for y in range(0+3,18+1)])
	).to_cnf()
Net2_Subnet9_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,9], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(58,78+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,9], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(58,78+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,9], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(58,78+1)])for y in range(0+3,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,9], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(58,78+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet9_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,9], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,9], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(58,78+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,9], ~Edge_Net_Subnet2[x-1,y,3,1,mask,9]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,9], Edge_Net_Subnet2[x+2,y,3,1,mask,9], Edge_Net_Subnet2[x+3,y,3,1,mask,9], Edge_Net_Subnet2[x+4,y,3,1,mask,9], Edge_Net_Subnet2[x+5,y,3,1,mask,9], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,9], ~Edge_Net_Subnet2[x+1,y,3,1,mask,9]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,9], Edge_Net_Subnet2[x-2,y,3,1,mask,9], Edge_Net_Subnet2[x-3,y,3,1,mask,9], Edge_Net_Subnet2[x-4,y,3,1,mask,9], Edge_Net_Subnet2[x-5,y,3,1,mask,9], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,9], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,9], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(3,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,9], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,9], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet9_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,9], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,9], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(58,78+1)])for y in range(2,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,9], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,9], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(58,78+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet9_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,9], ~Edge_Net_Subnet2[x-1,y,2,1,mask,9]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,9], Edge_Net_Subnet2[x+2,y,2,1,mask,9], Edge_Net_Subnet2[x+3,y,2,1,mask,9], Edge_Net_Subnet2[x+4,y,2,1,mask,9], Edge_Net_Subnet2[x+5,y,2,1,mask,9], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,9], ~Edge_Net_Subnet2[x+1,y,2,1,mask,9]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,9], Edge_Net_Subnet2[x-2,y,2,1,mask,9], Edge_Net_Subnet2[x-3,y,2,1,mask,9], Edge_Net_Subnet2[x-4,y,2,1,mask,9], Edge_Net_Subnet2[x-5,y,2,1,mask,9], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,9], And(Edge_Net_Subnet2[x-1,y,2,1,mask,9], Edge_Net_Subnet2[x-2,y,2,1,mask,9], Edge_Net_Subnet2[x-3,y,2,1,mask,9], Edge_Net_Subnet2[x-4,y,2,1,mask,9], Edge_Net_Subnet2[x-5,y,2,1,mask,9], ))for mask in range(1,2+1)])for x in range(58,58+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,9], And(Edge_Net_Subnet2[x+1,y,2,1,mask,9], Edge_Net_Subnet2[x+2,y,2,1,mask,9], Edge_Net_Subnet2[x+3,y,2,1,mask,9], Edge_Net_Subnet2[x+4,y,2,1,mask,9], Edge_Net_Subnet2[x+5,y,2,1,mask,9], ))for mask in range(1,2+1)])for x in range(78-1,58)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,9], ~Edge_Net_Subnet2[x,y-1,2,0,mask,9]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,9], Edge_Net_Subnet2[x,y+2,2,0,mask,9], Edge_Net_Subnet2[x,y+3,2,0,mask,9], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0+1,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,9], ~Edge_Net_Subnet2[x,y+1,2,0,mask,9]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,9], Edge_Net_Subnet2[x,y-2,2,0,mask,9], Edge_Net_Subnet2[x,y-3,2,0,mask,9], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0+3,18+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,9], And(Edge_Net_Subnet2[x,y+1,2,0,mask,9], Edge_Net_Subnet2[x,y+2,2,0,mask,9], Edge_Net_Subnet2[x,y+3,2,0,mask,9], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,9], And(Edge_Net_Subnet2[x,y-1,2,0,mask,9], Edge_Net_Subnet2[x,y-2,2,0,mask,9], Edge_Net_Subnet2[x,y-3,2,0,mask,9], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(18,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,9], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,9], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(58,78+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet9_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,9], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,9], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet9_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,9], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(58,78+1)])for y in range(2,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,9], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(58,78+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,9], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(4,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,9], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,9], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,9], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(58,78+1)])for y in range(3,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,9], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,9], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(4,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,9], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,9], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(58,78+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,9], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,9], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,9], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,9], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(58,78+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet9_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,9], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,9], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(58,78+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet9_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,9], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,9], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(58,78+1)])for y in range(2,18+1)]),
	).to_cnf()
Net2_Subnet9_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,9], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(58,78+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,9], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(58,78+1)])for y in range(2,18+1)]),
	).to_cnf()
Net2_Subnet9_DR = And(Net2_Subnet9_DR_Trend, Net2_Subnet9_DR_GIL_HorMinWidth,Net2_Subnet9_DR_GIL_HorMinSpacing,Net2_Subnet9_DR_GIL_VerMinSpacing,Net2_Subnet9_DR_AIL2_VerMinWidth,Net2_Subnet9_DR_AIL2_VerMinSpacing,Net2_Subnet9_DR_VerAIL2_HorMinSpacing,Net2_Subnet9_DR_MINT1AB_HorMinWidth,Net2_Subnet9_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet9_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet9_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet9_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet9_DR_M1AB_MinWidth,Net2_Subnet9_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet9_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet9_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet9_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet9_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet9_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet9_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet9_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet9_DR_V0_HorMinSpacing,Net2_Subnet9_DR_V1_HorMinSpacing,Net2_Subnet9_DR_V0_VerMinSpacing,Net2_Subnet9_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet9_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[62,1,0,0, 62,2,0,0, 62,3,0,0, 62,4,0,0, 62,5,0,0, 62,6,0,0, 62,7,0,0, 62,8,0,0, 62,9,0,0, 62,10,0,0, 62,11,0,0, 62,12,0,0, 62,13,0,0, 62,14,0,0, ],14,58,0,1,78,18,3,9),
	RConstraints.R1(Edge_Net_Subnet2,[74,1,0,0, 74,2,0,0, 74,3,0,0, 74,4,0,0, 74,5,0,0, 74,6,0,0, 74,7,0,0, 74,8,0,0, ],8,58,0,1,78,18,3,9),
	).to_cnf()
Net2_Subnet9_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[62,1,0, 62,2,0, 62,3,0, 62,4,0, 62,5,0, 62,6,0, 62,7,0, 62,8,0, 62,9,0, 62,10,0, 62,11,0, 62,12,0, 62,13,0, 62,14,0, 62,15,0, 74,1,0, 74,2,0, 74,3,0, 74,4,0, 74,5,0, 74,6,0, 74,7,0, 74,8,0, 74,9,0, ],24,58,0,0,78,18,3,9,1),
	)
Net2_Subnet9_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(58,78+1)])for y in range(0,18+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,5+1)])for x in range(58,78+1)])for y in range(0,18+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet9_R = And(Net2_Subnet9_R1,Net2_Subnet9_R2,Net2_Subnet9_R3,)
Net2_Subnet9_Formula = And(Net2_Subnet9_C,Net2_Subnet9_DR,Net2_Subnet9_R)
# Net = 4 Subnet = 1 | Left -> Right [28,76] Top -> Bottom [0,35]
# Range R1(32,32,0,35)
# Range R2(72,72,0,35)
### Disable edges outside window
Edge_Net_Subnet4[0:28,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(36288)
Edge_Net_Subnet4[76:85+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(12960)

### Consistency Constraints
Net4_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,3]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(28,76+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net4_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet4[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,3])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(28,76+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net4_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet4[x,y,2,trend,0,1],Xor(Edge_Net_Subnet4[x,y,2,trend,1,1],Edge_Net_Subnet4[x,y,2,trend,2,1])),And(~Edge_Net_Subnet4[x,y,2,trend,0,1],~Edge_Net_Subnet4[x,y,2,trend,1,1],~Edge_Net_Subnet4[x,y,2,trend,2,1]))for x in range(28,76+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net4_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet4[x,y,3,1,0,1],Xor(Edge_Net_Subnet4[x,y,3,1,1,1],Edge_Net_Subnet4[x,y,3,1,2,1])),And(~Edge_Net_Subnet4[x,y,3,1,0,1],~Edge_Net_Subnet4[x,y,3,1,1,1],~Edge_Net_Subnet4[x,y,3,1,2,1]))for x in range(28,76+1)])for y in range(0,35+1)]).to_cnf()
Net4_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet4[x,y,1,trend,2,1],Xor(Edge_Net_Subnet4[x,y,1,trend,0,1],Edge_Net_Subnet4[x,y,1,trend,1,1])),And(~Edge_Net_Subnet4[x,y,1,trend,2,1],~Edge_Net_Subnet4[x,y,1,trend,0,1],~Edge_Net_Subnet4[x,y,1,trend,1,1]))for x in range(28,76+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net4_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet4[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(28,76+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet4[x,y,z,trend,2,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(28,76+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet4[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(28,76+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet4[x,y,z,trend,1,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(28,76+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net4_Subnet1_C = And(Net4_Subnet1_C1, Net4_Subnet1_C2,Net4_Subnet1_C3_ME1_Mask,Net4_Subnet1_C4_MINT1_Mask,Net4_Subnet1_C5_AIL2GIL_Mask,Net4_Subnet1_C6,)
### Design Rules
Net4_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(28,76+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net4_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,1,1,1,1], ~Edge_Net_Subnet4[x-1,y,1,1,1,1]), And(Edge_Net_Subnet4[x+1,y,1,1,1,1], Edge_Net_Subnet4[x+2,y,1,1,1,1], Edge_Net_Subnet4[x+3,y,1,1,1,1], ))for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,1,1,1,1], ~Edge_Net_Subnet4[x+1,y,1,1,1,1]), And(Edge_Net_Subnet4[x-1,y,1,1,1,1], Edge_Net_Subnet4[x-2,y,1,1,1,1], Edge_Net_Subnet4[x-3,y,1,1,1,1], ))for x in range(28,76+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(28,76+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(28,76+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(28,76+1)])for y in range(3,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1]), And(Edge_Net_Subnet4[x,y+1,1,0,0,1], Edge_Net_Subnet4[x,y+2,1,0,0,1], Edge_Net_Subnet4[x,y+3,1,0,0,1], ))for x in range(28,76+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1]), And(Edge_Net_Subnet4[x,y-1,1,0,0,1], Edge_Net_Subnet4[x,y-2,1,0,0,1], Edge_Net_Subnet4[x,y-3,1,0,0,1], ))for x in range(28,76+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge_Net_Subnet4[x,y-1,1,0,0,1]), And(Edge_Net_Subnet4[x,y+1,1,0,0,1], Edge_Net_Subnet4[x,y+2,1,0,0,1], Edge_Net_Subnet4[x,y+3,1,0,0,1], ))for x in range(28,76+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge_Net_Subnet4[x,y+1,1,0,0,1]), And(Edge_Net_Subnet4[x,y-1,1,0,0,1], Edge_Net_Subnet4[x,y-2,1,0,0,1], Edge_Net_Subnet4[x,y-3,1,0,0,1], ))for x in range(28,76+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net4_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(28,76+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(28,76+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(28,76+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(28,76+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(28,76+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(28,76+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net4_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(28,76+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,3,1,mask,1], ~Edge_Net_Subnet4[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet4[x+1,y,3,1,mask,1], Edge_Net_Subnet4[x+2,y,3,1,mask,1], Edge_Net_Subnet4[x+3,y,3,1,mask,1], Edge_Net_Subnet4[x+4,y,3,1,mask,1], Edge_Net_Subnet4[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,3,1,mask,1], ~Edge_Net_Subnet4[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet4[x-1,y,3,1,mask,1], Edge_Net_Subnet4[x-2,y,3,1,mask,1], Edge_Net_Subnet4[x-3,y,3,1,mask,1], Edge_Net_Subnet4[x-4,y,3,1,mask,1], Edge_Net_Subnet4[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(3,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(28,76+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(28,76+1)])for y in range(2,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(28,76+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,2,1,mask,1], ~Edge_Net_Subnet4[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet4[x+1,y,2,1,mask,1], Edge_Net_Subnet4[x+2,y,2,1,mask,1], Edge_Net_Subnet4[x+3,y,2,1,mask,1], Edge_Net_Subnet4[x+4,y,2,1,mask,1], Edge_Net_Subnet4[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,2,1,mask,1], ~Edge_Net_Subnet4[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet4[x-1,y,2,1,mask,1], Edge_Net_Subnet4[x-2,y,2,1,mask,1], Edge_Net_Subnet4[x-3,y,2,1,mask,1], Edge_Net_Subnet4[x-4,y,2,1,mask,1], Edge_Net_Subnet4[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,1], And(Edge_Net_Subnet4[x-1,y,2,1,mask,1], Edge_Net_Subnet4[x-2,y,2,1,mask,1], Edge_Net_Subnet4[x-3,y,2,1,mask,1], Edge_Net_Subnet4[x-4,y,2,1,mask,1], Edge_Net_Subnet4[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(28,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,1], And(Edge_Net_Subnet4[x+1,y,2,1,mask,1], Edge_Net_Subnet4[x+2,y,2,1,mask,1], Edge_Net_Subnet4[x+3,y,2,1,mask,1], Edge_Net_Subnet4[x+4,y,2,1,mask,1], Edge_Net_Subnet4[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(76-1,28)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,1], ~Edge_Net_Subnet4[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet4[x,y+1,2,0,mask,1], Edge_Net_Subnet4[x,y+2,2,0,mask,1], Edge_Net_Subnet4[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,1], ~Edge_Net_Subnet4[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet4[x,y-1,2,0,mask,1], Edge_Net_Subnet4[x,y-2,2,0,mask,1], Edge_Net_Subnet4[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet4[x,y,2,0,mask,1], And(Edge_Net_Subnet4[x,y+1,2,0,mask,1], Edge_Net_Subnet4[x,y+2,2,0,mask,1], Edge_Net_Subnet4[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet4[x,y,2,0,mask,1], And(Edge_Net_Subnet4[x,y-1,2,0,mask,1], Edge_Net_Subnet4[x,y-2,2,0,mask,1], Edge_Net_Subnet4[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(35,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(28,76+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(28,76+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(28,76+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net4_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net4_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(28,76+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(28,76+1)])for y in range(3,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(4,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(28,76+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(28,76+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(28,76+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(28,76+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(28,76+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(28,76+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(28,76+1)])for y in range(2,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(28,76+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(28,76+1)])for y in range(2,35+1)]),
	).to_cnf()
Net4_Subnet1_DR = And(Net4_Subnet1_DR_Trend, Net4_Subnet1_DR_GIL_HorMinWidth,Net4_Subnet1_DR_GIL_HorMinSpacing,Net4_Subnet1_DR_GIL_VerMinSpacing,Net4_Subnet1_DR_AIL2_VerMinWidth,Net4_Subnet1_DR_AIL2_VerMinSpacing,Net4_Subnet1_DR_VerAIL2_HorMinSpacing,Net4_Subnet1_DR_MINT1AB_HorMinWidth,Net4_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net4_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net4_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net4_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net4_Subnet1_DR_M1AB_MinWidth,Net4_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net4_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net4_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net4_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net4_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net4_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net4_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net4_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net4_Subnet1_DR_V0_HorMinSpacing,Net4_Subnet1_DR_V1_HorMinSpacing,Net4_Subnet1_DR_V0_VerMinSpacing,Net4_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net4_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet4,[32,0,0,0, 32,1,0,0, 32,2,0,0, 32,3,0,0, 32,4,0,0, 32,5,0,0, 32,6,0,0, 32,7,0,0, 32,8,0,0, 32,9,0,0, 32,10,0,0, 32,11,0,0, 32,12,0,0, 32,13,0,0, 32,14,0,0, 32,15,0,0, 32,16,0,0, 32,17,0,0, 32,18,0,0, 32,19,0,0, 32,20,0,0, 32,21,0,0, 32,22,0,0, 32,23,0,0, 32,24,0,0, 32,25,0,0, 32,26,0,0, 32,27,0,0, 32,28,0,0, 32,29,0,0, 32,30,0,0, 32,31,0,0, 32,32,0,0, 32,33,0,0, 32,34,0,0, 32,35,0,0, ],36,28,0,1,76,35,3,1),
	RConstraints.R1(Edge_Net_Subnet4,[72,0,0,0, 72,1,0,0, 72,2,0,0, 72,3,0,0, 72,4,0,0, 72,5,0,0, 72,6,0,0, 72,7,0,0, 72,8,0,0, 72,9,0,0, 72,10,0,0, 72,11,0,0, 72,12,0,0, 72,13,0,0, 72,14,0,0, 72,15,0,0, 72,16,0,0, 72,17,0,0, 72,18,0,0, 72,19,0,0, 72,20,0,0, 72,21,0,0, 72,22,0,0, 72,23,0,0, 72,24,0,0, 72,25,0,0, 72,26,0,0, 72,27,0,0, 72,28,0,0, 72,29,0,0, 72,30,0,0, 72,31,0,0, 72,32,0,0, 72,33,0,0, 72,34,0,0, 72,35,0,0, ],36,28,0,1,76,35,3,1),
	).to_cnf()
Net4_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet4,Edge,Edge_Net,[32,0,0, 32,1,0, 32,2,0, 32,3,0, 32,4,0, 32,5,0, 32,6,0, 32,7,0, 32,8,0, 32,9,0, 32,10,0, 32,11,0, 32,12,0, 32,13,0, 32,14,0, 32,15,0, 32,16,0, 32,17,0, 32,18,0, 32,19,0, 32,20,0, 32,21,0, 32,22,0, 32,23,0, 32,24,0, 32,25,0, 32,26,0, 32,27,0, 32,28,0, 32,29,0, 32,30,0, 32,31,0, 32,32,0, 32,33,0, 32,34,0, 32,35,0, 72,0,0, 72,1,0, 72,2,0, 72,3,0, 72,4,0, 72,5,0, 72,6,0, 72,7,0, 72,8,0, 72,9,0, 72,10,0, 72,11,0, 72,12,0, 72,13,0, 72,14,0, 72,15,0, 72,16,0, 72,17,0, 72,18,0, 72,19,0, 72,20,0, 72,21,0, 72,22,0, 72,23,0, 72,24,0, 72,25,0, 72,26,0, 72,27,0, 72,28,0, 72,29,0, 72,30,0, 72,31,0, 72,32,0, 72,33,0, 72,34,0, 72,35,0, ],72,28,0,0,76,35,3,1,3),
	)
Net4_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,3],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,2+1)])for x in range(28,76+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,3],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(4,5+1)])for x in range(28,76+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net4_Subnet1_R = And(Net4_Subnet1_R1,Net4_Subnet1_R2,Net4_Subnet1_R3,)
Net4_Subnet1_Formula = And(Net4_Subnet1_C,Net4_Subnet1_DR,Net4_Subnet1_R)
# Net = 5 Subnet = 0 | Left -> Right [30,38] Top -> Bottom [0,35]
# Range R1(34,34,1,8)
# Range R2(34,34,26,33)
### Disable edges outside window
Edge_Net_Subnet5[0:30,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(38880)
Edge_Net_Subnet5[38:85+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(62208)

### Consistency Constraints
Net5_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,4]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(30,38+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net5_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet5[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,4])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(30,38+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net5_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet5[x,y,2,trend,0,0],Xor(Edge_Net_Subnet5[x,y,2,trend,1,0],Edge_Net_Subnet5[x,y,2,trend,2,0])),And(~Edge_Net_Subnet5[x,y,2,trend,0,0],~Edge_Net_Subnet5[x,y,2,trend,1,0],~Edge_Net_Subnet5[x,y,2,trend,2,0]))for x in range(30,38+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net5_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet5[x,y,3,1,0,0],Xor(Edge_Net_Subnet5[x,y,3,1,1,0],Edge_Net_Subnet5[x,y,3,1,2,0])),And(~Edge_Net_Subnet5[x,y,3,1,0,0],~Edge_Net_Subnet5[x,y,3,1,1,0],~Edge_Net_Subnet5[x,y,3,1,2,0]))for x in range(30,38+1)])for y in range(0,35+1)]).to_cnf()
Net5_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet5[x,y,1,trend,2,0],Xor(Edge_Net_Subnet5[x,y,1,trend,0,0],Edge_Net_Subnet5[x,y,1,trend,1,0])),And(~Edge_Net_Subnet5[x,y,1,trend,2,0],~Edge_Net_Subnet5[x,y,1,trend,0,0],~Edge_Net_Subnet5[x,y,1,trend,1,0]))for x in range(30,38+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net5_Subnet0_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,z,trend,1,0], And(*[And(~Edge_Net_Subnet5[x,y,z,trend,2,s2])for s2 in range(0+1,3)]))for trend in range(0,1+1)])for x in range(30,38+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,z,trend,2,0], And(*[And(~Edge_Net_Subnet5[x,y,z,trend,1,s2])for s2 in range(0+1,3)]))for trend in range(0,1+1)])for x in range(30,38+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net5_Subnet0_C = And(Net5_Subnet0_C1, Net5_Subnet0_C2,Net5_Subnet0_C3_ME1_Mask,Net5_Subnet0_C4_MINT1_Mask,Net5_Subnet0_C5_AIL2GIL_Mask,Net5_Subnet0_C6,)
### Design Rules
Net5_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(30,38+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net5_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,1,1,1,0], ~Edge_Net_Subnet5[x-1,y,1,1,1,0]), And(Edge_Net_Subnet5[x+1,y,1,1,1,0], Edge_Net_Subnet5[x+2,y,1,1,1,0], Edge_Net_Subnet5[x+3,y,1,1,1,0], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,1,1,1,0], ~Edge_Net_Subnet5[x+1,y,1,1,1,0]), And(Edge_Net_Subnet5[x-1,y,1,1,1,0], Edge_Net_Subnet5[x-2,y,1,1,1,0], Edge_Net_Subnet5[x-3,y,1,1,1,0], ))for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(30,38+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(30,38+1)])for y in range(3,35+1)]),
	).to_cnf()
Net5_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,0]), And(Edge_Net_Subnet5[x,y+1,1,0,0,0], Edge_Net_Subnet5[x,y+2,1,0,0,0], Edge_Net_Subnet5[x,y+3,1,0,0,0], ))for x in range(30,38+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,0]), And(Edge_Net_Subnet5[x,y-1,1,0,0,0], Edge_Net_Subnet5[x,y-2,1,0,0,0], Edge_Net_Subnet5[x,y-3,1,0,0,0], ))for x in range(30,38+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,0], ~Edge_Net_Subnet5[x,y-1,1,0,0,0]), And(Edge_Net_Subnet5[x,y+1,1,0,0,0], Edge_Net_Subnet5[x,y+2,1,0,0,0], Edge_Net_Subnet5[x,y+3,1,0,0,0], ))for x in range(30,38+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,0], ~Edge_Net_Subnet5[x,y+1,1,0,0,0]), And(Edge_Net_Subnet5[x,y-1,1,0,0,0], Edge_Net_Subnet5[x,y-2,1,0,0,0], Edge_Net_Subnet5[x,y-3,1,0,0,0], ))for x in range(30,38+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net5_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(30,38+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(30,38+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(30,38+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(30,38+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(30,38+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(30,38+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net5_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,3,1,mask,0], ~Edge_Net_Subnet5[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet5[x+1,y,3,1,mask,0], Edge_Net_Subnet5[x+2,y,3,1,mask,0], Edge_Net_Subnet5[x+3,y,3,1,mask,0], Edge_Net_Subnet5[x+4,y,3,1,mask,0], Edge_Net_Subnet5[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,3,1,mask,0], ~Edge_Net_Subnet5[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet5[x-1,y,3,1,mask,0], Edge_Net_Subnet5[x-2,y,3,1,mask,0], Edge_Net_Subnet5[x-3,y,3,1,mask,0], Edge_Net_Subnet5[x-4,y,3,1,mask,0], Edge_Net_Subnet5[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(3,35+1)]),
	).to_cnf()
Net5_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(30,38+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(30,38+1)])for y in range(2,35+1)]),
	).to_cnf()
Net5_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,2,1,mask,0], ~Edge_Net_Subnet5[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet5[x+1,y,2,1,mask,0], Edge_Net_Subnet5[x+2,y,2,1,mask,0], Edge_Net_Subnet5[x+3,y,2,1,mask,0], Edge_Net_Subnet5[x+4,y,2,1,mask,0], Edge_Net_Subnet5[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,2,1,mask,0], ~Edge_Net_Subnet5[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet5[x-1,y,2,1,mask,0], Edge_Net_Subnet5[x-2,y,2,1,mask,0], Edge_Net_Subnet5[x-3,y,2,1,mask,0], Edge_Net_Subnet5[x-4,y,2,1,mask,0], Edge_Net_Subnet5[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,0], And(Edge_Net_Subnet5[x-1,y,2,1,mask,0], Edge_Net_Subnet5[x-2,y,2,1,mask,0], Edge_Net_Subnet5[x-3,y,2,1,mask,0], Edge_Net_Subnet5[x-4,y,2,1,mask,0], Edge_Net_Subnet5[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(30,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,0], And(Edge_Net_Subnet5[x+1,y,2,1,mask,0], Edge_Net_Subnet5[x+2,y,2,1,mask,0], Edge_Net_Subnet5[x+3,y,2,1,mask,0], Edge_Net_Subnet5[x+4,y,2,1,mask,0], Edge_Net_Subnet5[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(38-1,30)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,0], ~Edge_Net_Subnet5[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet5[x,y+1,2,0,mask,0], Edge_Net_Subnet5[x,y+2,2,0,mask,0], Edge_Net_Subnet5[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,0], ~Edge_Net_Subnet5[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet5[x,y-1,2,0,mask,0], Edge_Net_Subnet5[x,y-2,2,0,mask,0], Edge_Net_Subnet5[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet5[x,y,2,0,mask,0], And(Edge_Net_Subnet5[x,y+1,2,0,mask,0], Edge_Net_Subnet5[x,y+2,2,0,mask,0], Edge_Net_Subnet5[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet5[x,y,2,0,mask,0], And(Edge_Net_Subnet5[x,y-1,2,0,mask,0], Edge_Net_Subnet5[x,y-2,2,0,mask,0], Edge_Net_Subnet5[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(35,35+1)]),
	).to_cnf()
Net5_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(30,38+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(30,38+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net5_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net5_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(30,38+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(30,38+1)])for y in range(3,35+1)]),
	).to_cnf()
Net5_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(4,35+1)]),
	).to_cnf()
Net5_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(2,35+1)]),
	).to_cnf()
Net5_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(2,35+1)]),
	).to_cnf()
Net5_Subnet0_DR = And(Net5_Subnet0_DR_Trend, Net5_Subnet0_DR_GIL_HorMinWidth,Net5_Subnet0_DR_GIL_HorMinSpacing,Net5_Subnet0_DR_GIL_VerMinSpacing,Net5_Subnet0_DR_AIL2_VerMinWidth,Net5_Subnet0_DR_AIL2_VerMinSpacing,Net5_Subnet0_DR_VerAIL2_HorMinSpacing,Net5_Subnet0_DR_MINT1AB_HorMinWidth,Net5_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net5_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net5_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net5_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net5_Subnet0_DR_M1AB_MinWidth,Net5_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net5_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net5_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net5_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net5_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net5_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net5_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net5_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net5_Subnet0_DR_V0_HorMinSpacing,Net5_Subnet0_DR_V1_HorMinSpacing,Net5_Subnet0_DR_V0_VerMinSpacing,Net5_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net5_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet5,[34,1,0,0, 34,2,0,0, 34,3,0,0, 34,4,0,0, 34,5,0,0, 34,6,0,0, 34,7,0,0, 34,8,0,0, ],8,30,0,1,38,35,3,0),
	RConstraints.R1(Edge_Net_Subnet5,[34,26,0,0, 34,27,0,0, 34,28,0,0, 34,29,0,0, 34,30,0,0, 34,31,0,0, 34,32,0,0, 34,33,0,0, ],8,30,0,1,38,35,3,0),
	).to_cnf()
Net5_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet5,Edge,Edge_Net,[34,1,0, 34,2,0, 34,3,0, 34,4,0, 34,5,0, 34,6,0, 34,7,0, 34,8,0, 34,9,0, 34,26,0, 34,27,0, 34,28,0, 34,29,0, 34,30,0, 34,31,0, 34,32,0, 34,33,0, 34,34,0, ],18,30,0,0,38,35,3,0,4),
	)
Net5_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,4],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,3+1)])for x in range(30,38+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,4],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(5,5+1)])for x in range(30,38+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net5_Subnet0_R = And(Net5_Subnet0_R1,Net5_Subnet0_R2,Net5_Subnet0_R3,)
Net5_Subnet0_Formula = And(Net5_Subnet0_C,Net5_Subnet0_DR,Net5_Subnet0_R)
# Net = 5 Subnet = 1 | Left -> Right [30,44] Top -> Bottom [0,35]
# Range R1(34,34,1,8)
# Range R2(40,40,0,35)
### Disable edges outside window
Edge_Net_Subnet5[0:30,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(38880)
Edge_Net_Subnet5[44:85+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(54432)

### Consistency Constraints
Net5_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,4]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(30,44+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net5_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet5[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,4])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(30,44+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net5_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet5[x,y,2,trend,0,1],Xor(Edge_Net_Subnet5[x,y,2,trend,1,1],Edge_Net_Subnet5[x,y,2,trend,2,1])),And(~Edge_Net_Subnet5[x,y,2,trend,0,1],~Edge_Net_Subnet5[x,y,2,trend,1,1],~Edge_Net_Subnet5[x,y,2,trend,2,1]))for x in range(30,44+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net5_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet5[x,y,3,1,0,1],Xor(Edge_Net_Subnet5[x,y,3,1,1,1],Edge_Net_Subnet5[x,y,3,1,2,1])),And(~Edge_Net_Subnet5[x,y,3,1,0,1],~Edge_Net_Subnet5[x,y,3,1,1,1],~Edge_Net_Subnet5[x,y,3,1,2,1]))for x in range(30,44+1)])for y in range(0,35+1)]).to_cnf()
Net5_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet5[x,y,1,trend,2,1],Xor(Edge_Net_Subnet5[x,y,1,trend,0,1],Edge_Net_Subnet5[x,y,1,trend,1,1])),And(~Edge_Net_Subnet5[x,y,1,trend,2,1],~Edge_Net_Subnet5[x,y,1,trend,0,1],~Edge_Net_Subnet5[x,y,1,trend,1,1]))for x in range(30,44+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net5_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet5[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(30,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet5[x,y,z,trend,2,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(30,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet5[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(30,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet5[x,y,z,trend,1,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(30,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net5_Subnet1_C = And(Net5_Subnet1_C1, Net5_Subnet1_C2,Net5_Subnet1_C3_ME1_Mask,Net5_Subnet1_C4_MINT1_Mask,Net5_Subnet1_C5_AIL2GIL_Mask,Net5_Subnet1_C6,)
### Design Rules
Net5_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(30,44+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net5_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,1,1,1,1], ~Edge_Net_Subnet5[x-1,y,1,1,1,1]), And(Edge_Net_Subnet5[x+1,y,1,1,1,1], Edge_Net_Subnet5[x+2,y,1,1,1,1], Edge_Net_Subnet5[x+3,y,1,1,1,1], ))for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,1,1,1,1], ~Edge_Net_Subnet5[x+1,y,1,1,1,1]), And(Edge_Net_Subnet5[x-1,y,1,1,1,1], Edge_Net_Subnet5[x-2,y,1,1,1,1], Edge_Net_Subnet5[x-3,y,1,1,1,1], ))for x in range(30,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(30,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(30,44+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(30,44+1)])for y in range(3,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1]), And(Edge_Net_Subnet5[x,y+1,1,0,0,1], Edge_Net_Subnet5[x,y+2,1,0,0,1], Edge_Net_Subnet5[x,y+3,1,0,0,1], ))for x in range(30,44+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1]), And(Edge_Net_Subnet5[x,y-1,1,0,0,1], Edge_Net_Subnet5[x,y-2,1,0,0,1], Edge_Net_Subnet5[x,y-3,1,0,0,1], ))for x in range(30,44+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge_Net_Subnet5[x,y-1,1,0,0,1]), And(Edge_Net_Subnet5[x,y+1,1,0,0,1], Edge_Net_Subnet5[x,y+2,1,0,0,1], Edge_Net_Subnet5[x,y+3,1,0,0,1], ))for x in range(30,44+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge_Net_Subnet5[x,y+1,1,0,0,1]), And(Edge_Net_Subnet5[x,y-1,1,0,0,1], Edge_Net_Subnet5[x,y-2,1,0,0,1], Edge_Net_Subnet5[x,y-3,1,0,0,1], ))for x in range(30,44+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net5_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(30,44+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(30,44+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(30,44+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(30,44+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(30,44+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(30,44+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net5_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(30,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,3,1,mask,1], ~Edge_Net_Subnet5[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet5[x+1,y,3,1,mask,1], Edge_Net_Subnet5[x+2,y,3,1,mask,1], Edge_Net_Subnet5[x+3,y,3,1,mask,1], Edge_Net_Subnet5[x+4,y,3,1,mask,1], Edge_Net_Subnet5[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,3,1,mask,1], ~Edge_Net_Subnet5[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet5[x-1,y,3,1,mask,1], Edge_Net_Subnet5[x-2,y,3,1,mask,1], Edge_Net_Subnet5[x-3,y,3,1,mask,1], Edge_Net_Subnet5[x-4,y,3,1,mask,1], Edge_Net_Subnet5[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(3,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(30,44+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(30,44+1)])for y in range(2,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(30,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,2,1,mask,1], ~Edge_Net_Subnet5[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet5[x+1,y,2,1,mask,1], Edge_Net_Subnet5[x+2,y,2,1,mask,1], Edge_Net_Subnet5[x+3,y,2,1,mask,1], Edge_Net_Subnet5[x+4,y,2,1,mask,1], Edge_Net_Subnet5[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,2,1,mask,1], ~Edge_Net_Subnet5[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet5[x-1,y,2,1,mask,1], Edge_Net_Subnet5[x-2,y,2,1,mask,1], Edge_Net_Subnet5[x-3,y,2,1,mask,1], Edge_Net_Subnet5[x-4,y,2,1,mask,1], Edge_Net_Subnet5[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,1], And(Edge_Net_Subnet5[x-1,y,2,1,mask,1], Edge_Net_Subnet5[x-2,y,2,1,mask,1], Edge_Net_Subnet5[x-3,y,2,1,mask,1], Edge_Net_Subnet5[x-4,y,2,1,mask,1], Edge_Net_Subnet5[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(30,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,1], And(Edge_Net_Subnet5[x+1,y,2,1,mask,1], Edge_Net_Subnet5[x+2,y,2,1,mask,1], Edge_Net_Subnet5[x+3,y,2,1,mask,1], Edge_Net_Subnet5[x+4,y,2,1,mask,1], Edge_Net_Subnet5[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(44-1,30)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,1], ~Edge_Net_Subnet5[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet5[x,y+1,2,0,mask,1], Edge_Net_Subnet5[x,y+2,2,0,mask,1], Edge_Net_Subnet5[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,1], ~Edge_Net_Subnet5[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet5[x,y-1,2,0,mask,1], Edge_Net_Subnet5[x,y-2,2,0,mask,1], Edge_Net_Subnet5[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet5[x,y,2,0,mask,1], And(Edge_Net_Subnet5[x,y+1,2,0,mask,1], Edge_Net_Subnet5[x,y+2,2,0,mask,1], Edge_Net_Subnet5[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet5[x,y,2,0,mask,1], And(Edge_Net_Subnet5[x,y-1,2,0,mask,1], Edge_Net_Subnet5[x,y-2,2,0,mask,1], Edge_Net_Subnet5[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(35,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(30,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(30,44+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(30,44+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net5_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net5_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(30,44+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(30,44+1)])for y in range(3,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(4,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(30,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(30,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(30,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(30,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(30,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(30,44+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(30,44+1)])for y in range(2,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(30,44+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(30,44+1)])for y in range(2,35+1)]),
	).to_cnf()
Net5_Subnet1_DR = And(Net5_Subnet1_DR_Trend, Net5_Subnet1_DR_GIL_HorMinWidth,Net5_Subnet1_DR_GIL_HorMinSpacing,Net5_Subnet1_DR_GIL_VerMinSpacing,Net5_Subnet1_DR_AIL2_VerMinWidth,Net5_Subnet1_DR_AIL2_VerMinSpacing,Net5_Subnet1_DR_VerAIL2_HorMinSpacing,Net5_Subnet1_DR_MINT1AB_HorMinWidth,Net5_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net5_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net5_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net5_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net5_Subnet1_DR_M1AB_MinWidth,Net5_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net5_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net5_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net5_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net5_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net5_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net5_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net5_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net5_Subnet1_DR_V0_HorMinSpacing,Net5_Subnet1_DR_V1_HorMinSpacing,Net5_Subnet1_DR_V0_VerMinSpacing,Net5_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net5_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet5,[34,1,0,0, 34,2,0,0, 34,3,0,0, 34,4,0,0, 34,5,0,0, 34,6,0,0, 34,7,0,0, 34,8,0,0, ],8,30,0,1,44,35,3,1),
	RConstraints.R1(Edge_Net_Subnet5,[40,0,0,0, 40,1,0,0, 40,2,0,0, 40,3,0,0, 40,4,0,0, 40,5,0,0, 40,6,0,0, 40,7,0,0, 40,8,0,0, 40,9,0,0, 40,10,0,0, 40,11,0,0, 40,12,0,0, 40,13,0,0, 40,14,0,0, 40,15,0,0, 40,16,0,0, 40,17,0,0, 40,18,0,0, 40,19,0,0, 40,20,0,0, 40,21,0,0, 40,22,0,0, 40,23,0,0, 40,24,0,0, 40,25,0,0, 40,26,0,0, 40,27,0,0, 40,28,0,0, 40,29,0,0, 40,30,0,0, 40,31,0,0, 40,32,0,0, 40,33,0,0, 40,34,0,0, 40,35,0,0, ],36,30,0,1,44,35,3,1),
	).to_cnf()
Net5_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet5,Edge,Edge_Net,[34,1,0, 34,2,0, 34,3,0, 34,4,0, 34,5,0, 34,6,0, 34,7,0, 34,8,0, 34,9,0, 40,0,0, 40,1,0, 40,2,0, 40,3,0, 40,4,0, 40,5,0, 40,6,0, 40,7,0, 40,8,0, 40,9,0, 40,10,0, 40,11,0, 40,12,0, 40,13,0, 40,14,0, 40,15,0, 40,16,0, 40,17,0, 40,18,0, 40,19,0, 40,20,0, 40,21,0, 40,22,0, 40,23,0, 40,24,0, 40,25,0, 40,26,0, 40,27,0, 40,28,0, 40,29,0, 40,30,0, 40,31,0, 40,32,0, 40,33,0, 40,34,0, 40,35,0, ],45,30,0,0,44,35,3,1,4),
	)
Net5_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,4],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,3+1)])for x in range(30,44+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,4],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(5,5+1)])for x in range(30,44+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net5_Subnet1_R = And(Net5_Subnet1_R1,Net5_Subnet1_R2,Net5_Subnet1_R3,)
Net5_Subnet1_Formula = And(Net5_Subnet1_C,Net5_Subnet1_DR,Net5_Subnet1_R)
# Net = 3 Subnet = 0 | Left -> Right [34,42] Top -> Bottom [0,35]
# Range R1(38,38,1,8)
# Range R2(38,38,26,33)
### Disable edges outside window
Edge_Net_Subnet3[0:34,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(44064)
Edge_Net_Subnet3[42:85+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(57024)

### Consistency Constraints
Net3_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,0],Xor(Edge_Net_Subnet3[x,y,2,trend,1,0],Edge_Net_Subnet3[x,y,2,trend,2,0])),And(~Edge_Net_Subnet3[x,y,2,trend,0,0],~Edge_Net_Subnet3[x,y,2,trend,1,0],~Edge_Net_Subnet3[x,y,2,trend,2,0]))for x in range(34,42+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,0],Xor(Edge_Net_Subnet3[x,y,3,1,1,0],Edge_Net_Subnet3[x,y,3,1,2,0])),And(~Edge_Net_Subnet3[x,y,3,1,0,0],~Edge_Net_Subnet3[x,y,3,1,1,0],~Edge_Net_Subnet3[x,y,3,1,2,0]))for x in range(34,42+1)])for y in range(0,35+1)]).to_cnf()
Net3_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,0],Xor(Edge_Net_Subnet3[x,y,1,trend,0,0],Edge_Net_Subnet3[x,y,1,trend,1,0])),And(~Edge_Net_Subnet3[x,y,1,trend,2,0],~Edge_Net_Subnet3[x,y,1,trend,0,0],~Edge_Net_Subnet3[x,y,1,trend,1,0]))for x in range(34,42+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet0_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,0], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0+1,10)]))for trend in range(0,1+1)])for x in range(34,42+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,0], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0+1,10)]))for trend in range(0,1+1)])for x in range(34,42+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet0_C = And(Net3_Subnet0_C1, Net3_Subnet0_C2,Net3_Subnet0_C3_ME1_Mask,Net3_Subnet0_C4_MINT1_Mask,Net3_Subnet0_C5_AIL2GIL_Mask,Net3_Subnet0_C6,)
### Design Rules
Net3_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(34,42+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge_Net_Subnet3[x-1,y,1,1,1,0]), And(Edge_Net_Subnet3[x+1,y,1,1,1,0], Edge_Net_Subnet3[x+2,y,1,1,1,0], Edge_Net_Subnet3[x+3,y,1,1,1,0], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge_Net_Subnet3[x+1,y,1,1,1,0]), And(Edge_Net_Subnet3[x-1,y,1,1,1,0], Edge_Net_Subnet3[x-2,y,1,1,1,0], Edge_Net_Subnet3[x-3,y,1,1,1,0], ))for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(34,42+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(34,42+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0]), And(Edge_Net_Subnet3[x,y+1,1,0,0,0], Edge_Net_Subnet3[x,y+2,1,0,0,0], Edge_Net_Subnet3[x,y+3,1,0,0,0], ))for x in range(34,42+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0]), And(Edge_Net_Subnet3[x,y-1,1,0,0,0], Edge_Net_Subnet3[x,y-2,1,0,0,0], Edge_Net_Subnet3[x,y-3,1,0,0,0], ))for x in range(34,42+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge_Net_Subnet3[x,y-1,1,0,0,0]), And(Edge_Net_Subnet3[x,y+1,1,0,0,0], Edge_Net_Subnet3[x,y+2,1,0,0,0], Edge_Net_Subnet3[x,y+3,1,0,0,0], ))for x in range(34,42+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge_Net_Subnet3[x,y+1,1,0,0,0]), And(Edge_Net_Subnet3[x,y-1,1,0,0,0], Edge_Net_Subnet3[x,y-2,1,0,0,0], Edge_Net_Subnet3[x,y-3,1,0,0,0], ))for x in range(34,42+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net3_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(34,42+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(34,42+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(34,42+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(34,42+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(34,42+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(34,42+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net3_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge_Net_Subnet3[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,0], Edge_Net_Subnet3[x+2,y,3,1,mask,0], Edge_Net_Subnet3[x+3,y,3,1,mask,0], Edge_Net_Subnet3[x+4,y,3,1,mask,0], Edge_Net_Subnet3[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge_Net_Subnet3[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,0], Edge_Net_Subnet3[x-2,y,3,1,mask,0], Edge_Net_Subnet3[x-3,y,3,1,mask,0], Edge_Net_Subnet3[x-4,y,3,1,mask,0], Edge_Net_Subnet3[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(34,42+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(34,42+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge_Net_Subnet3[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,0], Edge_Net_Subnet3[x+2,y,2,1,mask,0], Edge_Net_Subnet3[x+3,y,2,1,mask,0], Edge_Net_Subnet3[x+4,y,2,1,mask,0], Edge_Net_Subnet3[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge_Net_Subnet3[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,0], Edge_Net_Subnet3[x-2,y,2,1,mask,0], Edge_Net_Subnet3[x-3,y,2,1,mask,0], Edge_Net_Subnet3[x-4,y,2,1,mask,0], Edge_Net_Subnet3[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(Edge_Net_Subnet3[x-1,y,2,1,mask,0], Edge_Net_Subnet3[x-2,y,2,1,mask,0], Edge_Net_Subnet3[x-3,y,2,1,mask,0], Edge_Net_Subnet3[x-4,y,2,1,mask,0], Edge_Net_Subnet3[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(34,34+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(Edge_Net_Subnet3[x+1,y,2,1,mask,0], Edge_Net_Subnet3[x+2,y,2,1,mask,0], Edge_Net_Subnet3[x+3,y,2,1,mask,0], Edge_Net_Subnet3[x+4,y,2,1,mask,0], Edge_Net_Subnet3[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(42-1,34)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge_Net_Subnet3[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,0], Edge_Net_Subnet3[x,y+2,2,0,mask,0], Edge_Net_Subnet3[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge_Net_Subnet3[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,0], Edge_Net_Subnet3[x,y-2,2,0,mask,0], Edge_Net_Subnet3[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,0], And(Edge_Net_Subnet3[x,y+1,2,0,mask,0], Edge_Net_Subnet3[x,y+2,2,0,mask,0], Edge_Net_Subnet3[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,0], And(Edge_Net_Subnet3[x,y-1,2,0,mask,0], Edge_Net_Subnet3[x,y-2,2,0,mask,0], Edge_Net_Subnet3[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(34,42+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(34,42+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net3_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net3_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(34,42+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(34,42+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(4,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet0_DR = And(Net3_Subnet0_DR_Trend, Net3_Subnet0_DR_GIL_HorMinWidth,Net3_Subnet0_DR_GIL_HorMinSpacing,Net3_Subnet0_DR_GIL_VerMinSpacing,Net3_Subnet0_DR_AIL2_VerMinWidth,Net3_Subnet0_DR_AIL2_VerMinSpacing,Net3_Subnet0_DR_VerAIL2_HorMinSpacing,Net3_Subnet0_DR_MINT1AB_HorMinWidth,Net3_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet0_DR_M1AB_MinWidth,Net3_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet0_DR_V0_HorMinSpacing,Net3_Subnet0_DR_V1_HorMinSpacing,Net3_Subnet0_DR_V0_VerMinSpacing,Net3_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[38,1,0,0, 38,2,0,0, 38,3,0,0, 38,4,0,0, 38,5,0,0, 38,6,0,0, 38,7,0,0, 38,8,0,0, ],8,34,0,1,42,35,3,0),
	RConstraints.R1(Edge_Net_Subnet3,[38,26,0,0, 38,27,0,0, 38,28,0,0, 38,29,0,0, 38,30,0,0, 38,31,0,0, 38,32,0,0, 38,33,0,0, ],8,34,0,1,42,35,3,0),
	).to_cnf()
Net3_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[38,1,0, 38,2,0, 38,3,0, 38,4,0, 38,5,0, 38,6,0, 38,7,0, 38,8,0, 38,9,0, 38,26,0, 38,27,0, 38,28,0, 38,29,0, 38,30,0, 38,31,0, 38,32,0, 38,33,0, 38,34,0, ],18,34,0,0,42,35,3,0,2),
	)
Net3_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(34,42+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,5+1)])for x in range(34,42+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet0_R = And(Net3_Subnet0_R1,Net3_Subnet0_R2,Net3_Subnet0_R3,)
Net3_Subnet0_Formula = And(Net3_Subnet0_C,Net3_Subnet0_DR,Net3_Subnet0_R)
# Net = 3 Subnet = 1 | Left -> Right [34,54] Top -> Bottom [16,35]
# Range R1(38,38,26,33)
# Range R2(50,50,20,33)
### Disable edges outside window
Edge_Net_Subnet3[0:34,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(44064)
Edge_Net_Subnet3[34:54,0:16,0:3+1,0:2+1,0:2+1,1]=exprzeros(11520)
Edge_Net_Subnet3[54:85+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(41472)

### Consistency Constraints
Net3_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(34,54+1)])for y in range(16,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(34,54+1)])for y in range(16,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,1],Xor(Edge_Net_Subnet3[x,y,2,trend,1,1],Edge_Net_Subnet3[x,y,2,trend,2,1])),And(~Edge_Net_Subnet3[x,y,2,trend,0,1],~Edge_Net_Subnet3[x,y,2,trend,1,1],~Edge_Net_Subnet3[x,y,2,trend,2,1]))for x in range(34,54+1)])for y in range(16,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,1],Xor(Edge_Net_Subnet3[x,y,3,1,1,1],Edge_Net_Subnet3[x,y,3,1,2,1])),And(~Edge_Net_Subnet3[x,y,3,1,0,1],~Edge_Net_Subnet3[x,y,3,1,1,1],~Edge_Net_Subnet3[x,y,3,1,2,1]))for x in range(34,54+1)])for y in range(16,35+1)]).to_cnf()
Net3_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,1],Xor(Edge_Net_Subnet3[x,y,1,trend,0,1],Edge_Net_Subnet3[x,y,1,trend,1,1])),And(~Edge_Net_Subnet3[x,y,1,trend,2,1],~Edge_Net_Subnet3[x,y,1,trend,0,1],~Edge_Net_Subnet3[x,y,1,trend,1,1]))for x in range(34,54+1)])for y in range(16,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(34,54+1)])for y in range(16,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(1+1,10)]))for trend in range(0,1+1)])for x in range(34,54+1)])for y in range(16,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(34,54+1)])for y in range(16,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(1+1,10)]))for trend in range(0,1+1)])for x in range(34,54+1)])for y in range(16,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet1_C = And(Net3_Subnet1_C1, Net3_Subnet1_C2,Net3_Subnet1_C3_ME1_Mask,Net3_Subnet1_C4_MINT1_Mask,Net3_Subnet1_C5_AIL2GIL_Mask,Net3_Subnet1_C6,)
### Design Rules
Net3_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(34,54+1)])for y in range(16,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,1], ~Edge_Net_Subnet3[x-1,y,1,1,1,1]), And(Edge_Net_Subnet3[x+1,y,1,1,1,1], Edge_Net_Subnet3[x+2,y,1,1,1,1], Edge_Net_Subnet3[x+3,y,1,1,1,1], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,1], ~Edge_Net_Subnet3[x+1,y,1,1,1,1]), And(Edge_Net_Subnet3[x-1,y,1,1,1,1], Edge_Net_Subnet3[x-2,y,1,1,1,1], Edge_Net_Subnet3[x-3,y,1,1,1,1], ))for x in range(34,54+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(34,54+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(34,54+1)])for y in range(16,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1]), And(Edge_Net_Subnet3[x,y-1,1,0,0,1], Edge_Net_Subnet3[x,y-2,1,0,0,1], Edge_Net_Subnet3[x,y-3,1,0,0,1], ))for x in range(34,54+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1], ~Edge_Net_Subnet3[x,y-1,1,0,0,1]), And(Edge_Net_Subnet3[x,y+1,1,0,0,1], Edge_Net_Subnet3[x,y+2,1,0,0,1], Edge_Net_Subnet3[x,y+3,1,0,0,1], ))for x in range(34,54+1)])for y in range(16,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1], ~Edge_Net_Subnet3[x,y+1,1,0,0,1]), And(Edge_Net_Subnet3[x,y-1,1,0,0,1], Edge_Net_Subnet3[x,y-2,1,0,0,1], Edge_Net_Subnet3[x,y-3,1,0,0,1], ))for x in range(34,54+1)])for y in range(16,35-1+1)])
	).to_cnf()
Net3_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(34,54+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(34,54+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(34,54+1)])for y in range(16,35-3+1)])
	).to_cnf()
Net3_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,1], ~Edge_Net_Subnet3[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,1], Edge_Net_Subnet3[x+2,y,3,1,mask,1], Edge_Net_Subnet3[x+3,y,3,1,mask,1], Edge_Net_Subnet3[x+4,y,3,1,mask,1], Edge_Net_Subnet3[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,1], ~Edge_Net_Subnet3[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,1], Edge_Net_Subnet3[x-2,y,3,1,mask,1], Edge_Net_Subnet3[x-3,y,3,1,mask,1], Edge_Net_Subnet3[x-4,y,3,1,mask,1], Edge_Net_Subnet3[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(34,54+1)])for y in range(16,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(34,54+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,1], ~Edge_Net_Subnet3[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,1], Edge_Net_Subnet3[x+2,y,2,1,mask,1], Edge_Net_Subnet3[x+3,y,2,1,mask,1], Edge_Net_Subnet3[x+4,y,2,1,mask,1], Edge_Net_Subnet3[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,1], ~Edge_Net_Subnet3[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,1], Edge_Net_Subnet3[x-2,y,2,1,mask,1], Edge_Net_Subnet3[x-3,y,2,1,mask,1], Edge_Net_Subnet3[x-4,y,2,1,mask,1], Edge_Net_Subnet3[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,1], And(Edge_Net_Subnet3[x-1,y,2,1,mask,1], Edge_Net_Subnet3[x-2,y,2,1,mask,1], Edge_Net_Subnet3[x-3,y,2,1,mask,1], Edge_Net_Subnet3[x-4,y,2,1,mask,1], Edge_Net_Subnet3[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(34,34+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,1], And(Edge_Net_Subnet3[x+1,y,2,1,mask,1], Edge_Net_Subnet3[x+2,y,2,1,mask,1], Edge_Net_Subnet3[x+3,y,2,1,mask,1], Edge_Net_Subnet3[x+4,y,2,1,mask,1], Edge_Net_Subnet3[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(54-1,34)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,1], ~Edge_Net_Subnet3[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,1], Edge_Net_Subnet3[x,y+2,2,0,mask,1], Edge_Net_Subnet3[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,1], ~Edge_Net_Subnet3[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,1], Edge_Net_Subnet3[x,y-2,2,0,mask,1], Edge_Net_Subnet3[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,1], And(Edge_Net_Subnet3[x,y+1,2,0,mask,1], Edge_Net_Subnet3[x,y+2,2,0,mask,1], Edge_Net_Subnet3[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,16+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,1], And(Edge_Net_Subnet3[x,y-1,2,0,mask,1], Edge_Net_Subnet3[x,y-2,2,0,mask,1], Edge_Net_Subnet3[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(34,54+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(34,54+1)])for y in range(16,35-2+1)]),
	).to_cnf()
Net3_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35-4+1)]),
	).to_cnf()
Net3_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(34,54+1)])for y in range(16,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(34,54+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(34,54+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(34,54+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(34,54+1)])for y in range(16,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(34,54+1)])for y in range(16,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(34,54+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet1_DR = And(Net3_Subnet1_DR_Trend, Net3_Subnet1_DR_GIL_HorMinWidth,Net3_Subnet1_DR_GIL_HorMinSpacing,Net3_Subnet1_DR_GIL_VerMinSpacing,Net3_Subnet1_DR_AIL2_VerMinWidth,Net3_Subnet1_DR_AIL2_VerMinSpacing,Net3_Subnet1_DR_VerAIL2_HorMinSpacing,Net3_Subnet1_DR_MINT1AB_HorMinWidth,Net3_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet1_DR_M1AB_MinWidth,Net3_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet1_DR_V0_HorMinSpacing,Net3_Subnet1_DR_V1_HorMinSpacing,Net3_Subnet1_DR_V0_VerMinSpacing,Net3_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[38,26,0,0, 38,27,0,0, 38,28,0,0, 38,29,0,0, 38,30,0,0, 38,31,0,0, 38,32,0,0, 38,33,0,0, ],8,34,16,1,54,35,3,1),
	RConstraints.R1(Edge_Net_Subnet3,[50,20,0,0, 50,21,0,0, 50,22,0,0, 50,23,0,0, 50,24,0,0, 50,25,0,0, 50,26,0,0, 50,27,0,0, 50,28,0,0, 50,29,0,0, 50,30,0,0, 50,31,0,0, 50,32,0,0, 50,33,0,0, ],14,34,16,1,54,35,3,1),
	).to_cnf()
Net3_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[38,26,0, 38,27,0, 38,28,0, 38,29,0, 38,30,0, 38,31,0, 38,32,0, 38,33,0, 38,34,0, 50,20,0, 50,21,0, 50,22,0, 50,23,0, 50,24,0, 50,25,0, 50,26,0, 50,27,0, 50,28,0, 50,29,0, 50,30,0, 50,31,0, 50,32,0, 50,33,0, 50,34,0, ],24,34,16,0,54,35,3,1,2),
	)
Net3_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(34,54+1)])for y in range(16,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,5+1)])for x in range(34,54+1)])for y in range(16,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet1_R = And(Net3_Subnet1_R1,Net3_Subnet1_R2,Net3_Subnet1_R3,)
Net3_Subnet1_Formula = And(Net3_Subnet1_C,Net3_Subnet1_DR,Net3_Subnet1_R)
# Net = 3 Subnet = 2 | Left -> Right [46,58] Top -> Bottom [16,35]
# Range R1(50,50,20,33)
# Range R2(54,54,20,33)
### Disable edges outside window
Edge_Net_Subnet3[0:46,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(59616)
Edge_Net_Subnet3[46:58,0:16,0:3+1,0:2+1,0:2+1,2]=exprzeros(6912)
Edge_Net_Subnet3[58:85+1,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(36288)

### Consistency Constraints
Net3_Subnet2_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(46,58+1)])for y in range(16,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet2_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,2]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(46,58+1)])for y in range(16,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet2_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,2],Xor(Edge_Net_Subnet3[x,y,2,trend,1,2],Edge_Net_Subnet3[x,y,2,trend,2,2])),And(~Edge_Net_Subnet3[x,y,2,trend,0,2],~Edge_Net_Subnet3[x,y,2,trend,1,2],~Edge_Net_Subnet3[x,y,2,trend,2,2]))for x in range(46,58+1)])for y in range(16,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet2_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,2],Xor(Edge_Net_Subnet3[x,y,3,1,1,2],Edge_Net_Subnet3[x,y,3,1,2,2])),And(~Edge_Net_Subnet3[x,y,3,1,0,2],~Edge_Net_Subnet3[x,y,3,1,1,2],~Edge_Net_Subnet3[x,y,3,1,2,2]))for x in range(46,58+1)])for y in range(16,35+1)]).to_cnf()
Net3_Subnet2_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,2],Xor(Edge_Net_Subnet3[x,y,1,trend,0,2],Edge_Net_Subnet3[x,y,1,trend,1,2])),And(~Edge_Net_Subnet3[x,y,1,trend,2,2],~Edge_Net_Subnet3[x,y,1,trend,0,2],~Edge_Net_Subnet3[x,y,1,trend,1,2]))for x in range(46,58+1)])for y in range(16,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet2_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(46,58+1)])for y in range(16,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(2+1,10)]))for trend in range(0,1+1)])for x in range(46,58+1)])for y in range(16,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(46,58+1)])for y in range(16,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(2+1,10)]))for trend in range(0,1+1)])for x in range(46,58+1)])for y in range(16,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet2_C = And(Net3_Subnet2_C1, Net3_Subnet2_C2,Net3_Subnet2_C3_ME1_Mask,Net3_Subnet2_C4_MINT1_Mask,Net3_Subnet2_C5_AIL2GIL_Mask,Net3_Subnet2_C6,)
### Design Rules
Net3_Subnet2_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(46,58+1)])for y in range(16,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet2_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,2], ~Edge_Net_Subnet3[x-1,y,1,1,1,2]), And(Edge_Net_Subnet3[x+1,y,1,1,1,2], Edge_Net_Subnet3[x+2,y,1,1,1,2], Edge_Net_Subnet3[x+3,y,1,1,1,2], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,2], ~Edge_Net_Subnet3[x+1,y,1,1,1,2]), And(Edge_Net_Subnet3[x-1,y,1,1,1,2], Edge_Net_Subnet3[x-2,y,1,1,1,2], Edge_Net_Subnet3[x-3,y,1,1,1,2], ))for x in range(46,58+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet2_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,2], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,2], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(46,58+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet2_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,2], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(46,58+1)])for y in range(16,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,2], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2]), And(Edge_Net_Subnet3[x,y-1,1,0,0,2], Edge_Net_Subnet3[x,y-2,1,0,0,2], Edge_Net_Subnet3[x,y-3,1,0,0,2], ))for x in range(46,58+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge_Net_Subnet3[x,y-1,1,0,0,2]), And(Edge_Net_Subnet3[x,y+1,1,0,0,2], Edge_Net_Subnet3[x,y+2,1,0,0,2], Edge_Net_Subnet3[x,y+3,1,0,0,2], ))for x in range(46,58+1)])for y in range(16,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge_Net_Subnet3[x,y+1,1,0,0,2]), And(Edge_Net_Subnet3[x,y-1,1,0,0,2], Edge_Net_Subnet3[x,y-2,1,0,0,2], Edge_Net_Subnet3[x,y-3,1,0,0,2], ))for x in range(46,58+1)])for y in range(16,35-1+1)])
	).to_cnf()
Net3_Subnet2_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(46,58+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(46,58+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(46,58+1)])for y in range(16,35-3+1)])
	).to_cnf()
Net3_Subnet2_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,2], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,2], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,2], ~Edge_Net_Subnet3[x-1,y,3,1,mask,2]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,2], Edge_Net_Subnet3[x+2,y,3,1,mask,2], Edge_Net_Subnet3[x+3,y,3,1,mask,2], Edge_Net_Subnet3[x+4,y,3,1,mask,2], Edge_Net_Subnet3[x+5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,2], ~Edge_Net_Subnet3[x+1,y,3,1,mask,2]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,2], Edge_Net_Subnet3[x-2,y,3,1,mask,2], Edge_Net_Subnet3[x-3,y,3,1,mask,2], Edge_Net_Subnet3[x-4,y,3,1,mask,2], Edge_Net_Subnet3[x-5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,2], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,2], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,2], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,2], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet2_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,2], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(46,58+1)])for y in range(16,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,2], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,2], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,2], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(46,58+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet2_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,2], ~Edge_Net_Subnet3[x-1,y,2,1,mask,2]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,2], Edge_Net_Subnet3[x+2,y,2,1,mask,2], Edge_Net_Subnet3[x+3,y,2,1,mask,2], Edge_Net_Subnet3[x+4,y,2,1,mask,2], Edge_Net_Subnet3[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,2], ~Edge_Net_Subnet3[x+1,y,2,1,mask,2]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,2], Edge_Net_Subnet3[x-2,y,2,1,mask,2], Edge_Net_Subnet3[x-3,y,2,1,mask,2], Edge_Net_Subnet3[x-4,y,2,1,mask,2], Edge_Net_Subnet3[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,2], And(Edge_Net_Subnet3[x-1,y,2,1,mask,2], Edge_Net_Subnet3[x-2,y,2,1,mask,2], Edge_Net_Subnet3[x-3,y,2,1,mask,2], Edge_Net_Subnet3[x-4,y,2,1,mask,2], Edge_Net_Subnet3[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(46,46+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,2], And(Edge_Net_Subnet3[x+1,y,2,1,mask,2], Edge_Net_Subnet3[x+2,y,2,1,mask,2], Edge_Net_Subnet3[x+3,y,2,1,mask,2], Edge_Net_Subnet3[x+4,y,2,1,mask,2], Edge_Net_Subnet3[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(58-1,46)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,2], ~Edge_Net_Subnet3[x,y-1,2,0,mask,2]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,2], Edge_Net_Subnet3[x,y+2,2,0,mask,2], Edge_Net_Subnet3[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,2], ~Edge_Net_Subnet3[x,y+1,2,0,mask,2]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,2], Edge_Net_Subnet3[x,y-2,2,0,mask,2], Edge_Net_Subnet3[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,2], And(Edge_Net_Subnet3[x,y+1,2,0,mask,2], Edge_Net_Subnet3[x,y+2,2,0,mask,2], Edge_Net_Subnet3[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,16+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,2], And(Edge_Net_Subnet3[x,y-1,2,0,mask,2], Edge_Net_Subnet3[x,y-2,2,0,mask,2], Edge_Net_Subnet3[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,2], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,2], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(46,58+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet2_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,2], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,2], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet2_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,2], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,2], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(46,58+1)])for y in range(16,35-2+1)]),
	).to_cnf()
Net3_Subnet2_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,2], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,2], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35-4+1)]),
	).to_cnf()
Net3_Subnet2_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,2], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(46,58+1)])for y in range(16,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,2], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,2], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,2], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,2], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,2], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(46,58+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,2], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,2], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,2], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,2], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(46,58+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet2_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,2], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,2], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(46,58+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet2_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,2], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(46,58+1)])for y in range(16,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,2], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,2], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(46,58+1)])for y in range(16,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,2], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(46,58+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet2_DR = And(Net3_Subnet2_DR_Trend, Net3_Subnet2_DR_GIL_HorMinWidth,Net3_Subnet2_DR_GIL_HorMinSpacing,Net3_Subnet2_DR_GIL_VerMinSpacing,Net3_Subnet2_DR_AIL2_VerMinWidth,Net3_Subnet2_DR_AIL2_VerMinSpacing,Net3_Subnet2_DR_VerAIL2_HorMinSpacing,Net3_Subnet2_DR_MINT1AB_HorMinWidth,Net3_Subnet2_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet2_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet2_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet2_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet2_DR_M1AB_MinWidth,Net3_Subnet2_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet2_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet2_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet2_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet2_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet2_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet2_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet2_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet2_DR_V0_HorMinSpacing,Net3_Subnet2_DR_V1_HorMinSpacing,Net3_Subnet2_DR_V0_VerMinSpacing,Net3_Subnet2_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet2_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[50,20,0,0, 50,21,0,0, 50,22,0,0, 50,23,0,0, 50,24,0,0, 50,25,0,0, 50,26,0,0, 50,27,0,0, 50,28,0,0, 50,29,0,0, 50,30,0,0, 50,31,0,0, 50,32,0,0, 50,33,0,0, ],14,46,16,1,58,35,3,2),
	RConstraints.R1(Edge_Net_Subnet3,[54,20,0,0, 54,21,0,0, 54,22,0,0, 54,23,0,0, 54,24,0,0, 54,25,0,0, 54,26,0,0, 54,27,0,0, 54,28,0,0, 54,29,0,0, 54,30,0,0, 54,31,0,0, 54,32,0,0, 54,33,0,0, ],14,46,16,1,58,35,3,2),
	).to_cnf()
Net3_Subnet2_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[50,20,0, 50,21,0, 50,22,0, 50,23,0, 50,24,0, 50,25,0, 50,26,0, 50,27,0, 50,28,0, 50,29,0, 50,30,0, 50,31,0, 50,32,0, 50,33,0, 50,34,0, 54,20,0, 54,21,0, 54,22,0, 54,23,0, 54,24,0, 54,25,0, 54,26,0, 54,27,0, 54,28,0, 54,29,0, 54,30,0, 54,31,0, 54,32,0, 54,33,0, 54,34,0, ],30,46,16,0,58,35,3,2,2),
	)
Net3_Subnet2_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(46,58+1)])for y in range(16,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,5+1)])for x in range(46,58+1)])for y in range(16,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet2_R = And(Net3_Subnet2_R1,Net3_Subnet2_R2,Net3_Subnet2_R3,)
Net3_Subnet2_Formula = And(Net3_Subnet2_C,Net3_Subnet2_DR,Net3_Subnet2_R)
# Net = 3 Subnet = 3 | Left -> Right [50,70] Top -> Bottom [16,35]
# Range R1(54,54,20,33)
# Range R2(66,66,28,33)
### Disable edges outside window
Edge_Net_Subnet3[0:50,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(64800)
Edge_Net_Subnet3[50:70,0:16,0:3+1,0:2+1,0:2+1,3]=exprzeros(11520)
Edge_Net_Subnet3[70:85+1,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(20736)

### Consistency Constraints
Net3_Subnet3_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(50,70+1)])for y in range(16,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet3_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,3]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(50,70+1)])for y in range(16,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet3_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,3],Xor(Edge_Net_Subnet3[x,y,2,trend,1,3],Edge_Net_Subnet3[x,y,2,trend,2,3])),And(~Edge_Net_Subnet3[x,y,2,trend,0,3],~Edge_Net_Subnet3[x,y,2,trend,1,3],~Edge_Net_Subnet3[x,y,2,trend,2,3]))for x in range(50,70+1)])for y in range(16,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet3_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,3],Xor(Edge_Net_Subnet3[x,y,3,1,1,3],Edge_Net_Subnet3[x,y,3,1,2,3])),And(~Edge_Net_Subnet3[x,y,3,1,0,3],~Edge_Net_Subnet3[x,y,3,1,1,3],~Edge_Net_Subnet3[x,y,3,1,2,3]))for x in range(50,70+1)])for y in range(16,35+1)]).to_cnf()
Net3_Subnet3_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,3],Xor(Edge_Net_Subnet3[x,y,1,trend,0,3],Edge_Net_Subnet3[x,y,1,trend,1,3])),And(~Edge_Net_Subnet3[x,y,1,trend,2,3],~Edge_Net_Subnet3[x,y,1,trend,0,3],~Edge_Net_Subnet3[x,y,1,trend,1,3]))for x in range(50,70+1)])for y in range(16,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet3_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(50,70+1)])for y in range(16,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(3+1,10)]))for trend in range(0,1+1)])for x in range(50,70+1)])for y in range(16,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(50,70+1)])for y in range(16,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(3+1,10)]))for trend in range(0,1+1)])for x in range(50,70+1)])for y in range(16,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet3_C = And(Net3_Subnet3_C1, Net3_Subnet3_C2,Net3_Subnet3_C3_ME1_Mask,Net3_Subnet3_C4_MINT1_Mask,Net3_Subnet3_C5_AIL2GIL_Mask,Net3_Subnet3_C6,)
### Design Rules
Net3_Subnet3_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(50,70+1)])for y in range(16,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet3_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,3], ~Edge_Net_Subnet3[x-1,y,1,1,1,3]), And(Edge_Net_Subnet3[x+1,y,1,1,1,3], Edge_Net_Subnet3[x+2,y,1,1,1,3], Edge_Net_Subnet3[x+3,y,1,1,1,3], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,3], ~Edge_Net_Subnet3[x+1,y,1,1,1,3]), And(Edge_Net_Subnet3[x-1,y,1,1,1,3], Edge_Net_Subnet3[x-2,y,1,1,1,3], Edge_Net_Subnet3[x-3,y,1,1,1,3], ))for x in range(50,70+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet3_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,3], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,3], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(50,70+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet3_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,3], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(50,70+1)])for y in range(16,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,3], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet3_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,3]), And(Edge_Net_Subnet3[x,y-1,1,0,0,3], Edge_Net_Subnet3[x,y-2,1,0,0,3], Edge_Net_Subnet3[x,y-3,1,0,0,3], ))for x in range(50,70+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,3], ~Edge_Net_Subnet3[x,y-1,1,0,0,3]), And(Edge_Net_Subnet3[x,y+1,1,0,0,3], Edge_Net_Subnet3[x,y+2,1,0,0,3], Edge_Net_Subnet3[x,y+3,1,0,0,3], ))for x in range(50,70+1)])for y in range(16,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,3], ~Edge_Net_Subnet3[x,y+1,1,0,0,3]), And(Edge_Net_Subnet3[x,y-1,1,0,0,3], Edge_Net_Subnet3[x,y-2,1,0,0,3], Edge_Net_Subnet3[x,y-3,1,0,0,3], ))for x in range(50,70+1)])for y in range(16,35-1+1)])
	).to_cnf()
Net3_Subnet3_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(50,70+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(50,70+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(50,70+1)])for y in range(16,35-3+1)])
	).to_cnf()
Net3_Subnet3_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,3], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,3], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet3_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,3], ~Edge_Net_Subnet3[x-1,y,3,1,mask,3]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,3], Edge_Net_Subnet3[x+2,y,3,1,mask,3], Edge_Net_Subnet3[x+3,y,3,1,mask,3], Edge_Net_Subnet3[x+4,y,3,1,mask,3], Edge_Net_Subnet3[x+5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,3], ~Edge_Net_Subnet3[x+1,y,3,1,mask,3]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,3], Edge_Net_Subnet3[x-2,y,3,1,mask,3], Edge_Net_Subnet3[x-3,y,3,1,mask,3], Edge_Net_Subnet3[x-4,y,3,1,mask,3], Edge_Net_Subnet3[x-5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet3_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,3], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,3], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet3_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,3], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,3], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet3_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,3], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(50,70+1)])for y in range(16,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,3], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet3_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,3], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,3], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(50,70+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet3_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,3], ~Edge_Net_Subnet3[x-1,y,2,1,mask,3]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,3], Edge_Net_Subnet3[x+2,y,2,1,mask,3], Edge_Net_Subnet3[x+3,y,2,1,mask,3], Edge_Net_Subnet3[x+4,y,2,1,mask,3], Edge_Net_Subnet3[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,3], ~Edge_Net_Subnet3[x+1,y,2,1,mask,3]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,3], Edge_Net_Subnet3[x-2,y,2,1,mask,3], Edge_Net_Subnet3[x-3,y,2,1,mask,3], Edge_Net_Subnet3[x-4,y,2,1,mask,3], Edge_Net_Subnet3[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,3], And(Edge_Net_Subnet3[x-1,y,2,1,mask,3], Edge_Net_Subnet3[x-2,y,2,1,mask,3], Edge_Net_Subnet3[x-3,y,2,1,mask,3], Edge_Net_Subnet3[x-4,y,2,1,mask,3], Edge_Net_Subnet3[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(50,50+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,3], And(Edge_Net_Subnet3[x+1,y,2,1,mask,3], Edge_Net_Subnet3[x+2,y,2,1,mask,3], Edge_Net_Subnet3[x+3,y,2,1,mask,3], Edge_Net_Subnet3[x+4,y,2,1,mask,3], Edge_Net_Subnet3[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(70-1,50)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,3], ~Edge_Net_Subnet3[x,y-1,2,0,mask,3]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,3], Edge_Net_Subnet3[x,y+2,2,0,mask,3], Edge_Net_Subnet3[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,3], ~Edge_Net_Subnet3[x,y+1,2,0,mask,3]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,3], Edge_Net_Subnet3[x,y-2,2,0,mask,3], Edge_Net_Subnet3[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,3], And(Edge_Net_Subnet3[x,y+1,2,0,mask,3], Edge_Net_Subnet3[x,y+2,2,0,mask,3], Edge_Net_Subnet3[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,16+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,3], And(Edge_Net_Subnet3[x,y-1,2,0,mask,3], Edge_Net_Subnet3[x,y-2,2,0,mask,3], Edge_Net_Subnet3[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet3_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,3], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,3], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(50,70+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet3_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,3], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,3], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet3_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,3], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,3], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(50,70+1)])for y in range(16,35-2+1)]),
	).to_cnf()
Net3_Subnet3_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,3], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,3], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35-4+1)]),
	).to_cnf()
Net3_Subnet3_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,3], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(50,70+1)])for y in range(16,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,3], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet3_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,3], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,3], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet3_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,3], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,3], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(50,70+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet3_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,3], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,3], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet3_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,3], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,3], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(50,70+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet3_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,3], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,3], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(50,70+1)])for y in range(16,35+1)])
	).to_cnf()
Net3_Subnet3_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,3], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(50,70+1)])for y in range(16,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,3], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet3_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,3], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(50,70+1)])for y in range(16,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,3], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(50,70+1)])for y in range(16,35+1)]),
	).to_cnf()
Net3_Subnet3_DR = And(Net3_Subnet3_DR_Trend, Net3_Subnet3_DR_GIL_HorMinWidth,Net3_Subnet3_DR_GIL_HorMinSpacing,Net3_Subnet3_DR_GIL_VerMinSpacing,Net3_Subnet3_DR_AIL2_VerMinWidth,Net3_Subnet3_DR_AIL2_VerMinSpacing,Net3_Subnet3_DR_VerAIL2_HorMinSpacing,Net3_Subnet3_DR_MINT1AB_HorMinWidth,Net3_Subnet3_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet3_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet3_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet3_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet3_DR_M1AB_MinWidth,Net3_Subnet3_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet3_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet3_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet3_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet3_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet3_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet3_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet3_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet3_DR_V0_HorMinSpacing,Net3_Subnet3_DR_V1_HorMinSpacing,Net3_Subnet3_DR_V0_VerMinSpacing,Net3_Subnet3_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet3_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[54,20,0,0, 54,21,0,0, 54,22,0,0, 54,23,0,0, 54,24,0,0, 54,25,0,0, 54,26,0,0, 54,27,0,0, 54,28,0,0, 54,29,0,0, 54,30,0,0, 54,31,0,0, 54,32,0,0, 54,33,0,0, ],14,50,16,1,70,35,3,3),
	RConstraints.R1(Edge_Net_Subnet3,[66,28,0,0, 66,29,0,0, 66,30,0,0, 66,31,0,0, 66,32,0,0, 66,33,0,0, ],6,50,16,1,70,35,3,3),
	).to_cnf()
Net3_Subnet3_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[54,20,0, 54,21,0, 54,22,0, 54,23,0, 54,24,0, 54,25,0, 54,26,0, 54,27,0, 54,28,0, 54,29,0, 54,30,0, 54,31,0, 54,32,0, 54,33,0, 54,34,0, 66,28,0, 66,29,0, 66,30,0, 66,31,0, 66,32,0, 66,33,0, 66,34,0, ],22,50,16,0,70,35,3,3,2),
	)
Net3_Subnet3_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(50,70+1)])for y in range(16,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,5+1)])for x in range(50,70+1)])for y in range(16,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet3_R = And(Net3_Subnet3_R1,Net3_Subnet3_R2,Net3_Subnet3_R3,)
Net3_Subnet3_Formula = And(Net3_Subnet3_C,Net3_Subnet3_DR,Net3_Subnet3_R)
# Net = 3 Subnet = 4 | Left -> Right [62,74] Top -> Bottom [22,35]
# Range R1(66,66,28,33)
# Range R2(70,70,26,33)
### Disable edges outside window
Edge_Net_Subnet3[0:62,0:35+1,0:3+1,0:2+1,0:2+1,4]=exprzeros(80352)
Edge_Net_Subnet3[62:74,0:22,0:3+1,0:2+1,0:2+1,4]=exprzeros(9504)
Edge_Net_Subnet3[74:85+1,0:35+1,0:3+1,0:2+1,0:2+1,4]=exprzeros(15552)

### Consistency Constraints
Net3_Subnet4_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(62,74+1)])for y in range(22,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet4_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,4]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(62,74+1)])for y in range(22,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet4_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,4],Xor(Edge_Net_Subnet3[x,y,2,trend,1,4],Edge_Net_Subnet3[x,y,2,trend,2,4])),And(~Edge_Net_Subnet3[x,y,2,trend,0,4],~Edge_Net_Subnet3[x,y,2,trend,1,4],~Edge_Net_Subnet3[x,y,2,trend,2,4]))for x in range(62,74+1)])for y in range(22,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet4_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,4],Xor(Edge_Net_Subnet3[x,y,3,1,1,4],Edge_Net_Subnet3[x,y,3,1,2,4])),And(~Edge_Net_Subnet3[x,y,3,1,0,4],~Edge_Net_Subnet3[x,y,3,1,1,4],~Edge_Net_Subnet3[x,y,3,1,2,4]))for x in range(62,74+1)])for y in range(22,35+1)]).to_cnf()
Net3_Subnet4_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,4],Xor(Edge_Net_Subnet3[x,y,1,trend,0,4],Edge_Net_Subnet3[x,y,1,trend,1,4])),And(~Edge_Net_Subnet3[x,y,1,trend,2,4],~Edge_Net_Subnet3[x,y,1,trend,0,4],~Edge_Net_Subnet3[x,y,1,trend,1,4]))for x in range(62,74+1)])for y in range(22,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet4_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,4], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0,4)]))for trend in range(0,1+1)])for x in range(62,74+1)])for y in range(22,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,4], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(4+1,10)]))for trend in range(0,1+1)])for x in range(62,74+1)])for y in range(22,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,4], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0,4)]))for trend in range(0,1+1)])for x in range(62,74+1)])for y in range(22,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,4], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(4+1,10)]))for trend in range(0,1+1)])for x in range(62,74+1)])for y in range(22,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet4_C = And(Net3_Subnet4_C1, Net3_Subnet4_C2,Net3_Subnet4_C3_ME1_Mask,Net3_Subnet4_C4_MINT1_Mask,Net3_Subnet4_C5_AIL2GIL_Mask,Net3_Subnet4_C6,)
### Design Rules
Net3_Subnet4_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(62,74+1)])for y in range(22,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet4_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,4], ~Edge_Net_Subnet3[x-1,y,1,1,1,4]), And(Edge_Net_Subnet3[x+1,y,1,1,1,4], Edge_Net_Subnet3[x+2,y,1,1,1,4], Edge_Net_Subnet3[x+3,y,1,1,1,4], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,4], ~Edge_Net_Subnet3[x+1,y,1,1,1,4]), And(Edge_Net_Subnet3[x-1,y,1,1,1,4], Edge_Net_Subnet3[x-2,y,1,1,1,4], Edge_Net_Subnet3[x-3,y,1,1,1,4], ))for x in range(62,74+1)])for y in range(22,35+1)])
	).to_cnf()
Net3_Subnet4_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,4], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,4], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(62,74+1)])for y in range(22,35+1)])
	).to_cnf()
Net3_Subnet4_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,4], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(62,74+1)])for y in range(22,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,4], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	).to_cnf()
Net3_Subnet4_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,4]), And(Edge_Net_Subnet3[x,y-1,1,0,0,4], Edge_Net_Subnet3[x,y-2,1,0,0,4], Edge_Net_Subnet3[x,y-3,1,0,0,4], ))for x in range(62,74+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,4], ~Edge_Net_Subnet3[x,y-1,1,0,0,4]), And(Edge_Net_Subnet3[x,y+1,1,0,0,4], Edge_Net_Subnet3[x,y+2,1,0,0,4], Edge_Net_Subnet3[x,y+3,1,0,0,4], ))for x in range(62,74+1)])for y in range(22,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,4], ~Edge_Net_Subnet3[x,y+1,1,0,0,4]), And(Edge_Net_Subnet3[x,y-1,1,0,0,4], Edge_Net_Subnet3[x,y-2,1,0,0,4], Edge_Net_Subnet3[x,y-3,1,0,0,4], ))for x in range(62,74+1)])for y in range(22,35-1+1)])
	).to_cnf()
Net3_Subnet4_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(62,74+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(62,74+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(62,74+1)])for y in range(22,35-3+1)])
	).to_cnf()
Net3_Subnet4_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,4], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,4], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	).to_cnf()
Net3_Subnet4_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,4], ~Edge_Net_Subnet3[x-1,y,3,1,mask,4]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,4], Edge_Net_Subnet3[x+2,y,3,1,mask,4], Edge_Net_Subnet3[x+3,y,3,1,mask,4], Edge_Net_Subnet3[x+4,y,3,1,mask,4], Edge_Net_Subnet3[x+5,y,3,1,mask,4], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,4], ~Edge_Net_Subnet3[x+1,y,3,1,mask,4]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,4], Edge_Net_Subnet3[x-2,y,3,1,mask,4], Edge_Net_Subnet3[x-3,y,3,1,mask,4], Edge_Net_Subnet3[x-4,y,3,1,mask,4], Edge_Net_Subnet3[x-5,y,3,1,mask,4], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	).to_cnf()
Net3_Subnet4_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,4], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,4], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	).to_cnf()
Net3_Subnet4_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,4], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,4], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)])
	).to_cnf()
Net3_Subnet4_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,4], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(62,74+1)])for y in range(22,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,4], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	).to_cnf()
Net3_Subnet4_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,4], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,4], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(62,74+1)])for y in range(22,35+1)])
	).to_cnf()
Net3_Subnet4_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,4], ~Edge_Net_Subnet3[x-1,y,2,1,mask,4]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,4], Edge_Net_Subnet3[x+2,y,2,1,mask,4], Edge_Net_Subnet3[x+3,y,2,1,mask,4], Edge_Net_Subnet3[x+4,y,2,1,mask,4], Edge_Net_Subnet3[x+5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,4], ~Edge_Net_Subnet3[x+1,y,2,1,mask,4]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,4], Edge_Net_Subnet3[x-2,y,2,1,mask,4], Edge_Net_Subnet3[x-3,y,2,1,mask,4], Edge_Net_Subnet3[x-4,y,2,1,mask,4], Edge_Net_Subnet3[x-5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,4], And(Edge_Net_Subnet3[x-1,y,2,1,mask,4], Edge_Net_Subnet3[x-2,y,2,1,mask,4], Edge_Net_Subnet3[x-3,y,2,1,mask,4], Edge_Net_Subnet3[x-4,y,2,1,mask,4], Edge_Net_Subnet3[x-5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(62,62+1)])for y in range(22,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,4], And(Edge_Net_Subnet3[x+1,y,2,1,mask,4], Edge_Net_Subnet3[x+2,y,2,1,mask,4], Edge_Net_Subnet3[x+3,y,2,1,mask,4], Edge_Net_Subnet3[x+4,y,2,1,mask,4], Edge_Net_Subnet3[x+5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(74-1,62)])for y in range(22,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,4], ~Edge_Net_Subnet3[x,y-1,2,0,mask,4]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,4], Edge_Net_Subnet3[x,y+2,2,0,mask,4], Edge_Net_Subnet3[x,y+3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,4], ~Edge_Net_Subnet3[x,y+1,2,0,mask,4]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,4], Edge_Net_Subnet3[x,y-2,2,0,mask,4], Edge_Net_Subnet3[x,y-3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,4], And(Edge_Net_Subnet3[x,y+1,2,0,mask,4], Edge_Net_Subnet3[x,y+2,2,0,mask,4], Edge_Net_Subnet3[x,y+3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,22+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,4], And(Edge_Net_Subnet3[x,y-1,2,0,mask,4], Edge_Net_Subnet3[x,y-2,2,0,mask,4], Edge_Net_Subnet3[x,y-3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet4_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,4], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,4], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(62,74+1)])for y in range(22,35+1)])
	).to_cnf()
Net3_Subnet4_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,4], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,4], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)])
	).to_cnf()
Net3_Subnet4_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,4], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,4], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(62,74+1)])for y in range(22,35-2+1)]),
	).to_cnf()
Net3_Subnet4_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,4], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,4], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35-4+1)]),
	).to_cnf()
Net3_Subnet4_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,4], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(62,74+1)])for y in range(22,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,4], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	).to_cnf()
Net3_Subnet4_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,4], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,4], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	).to_cnf()
Net3_Subnet4_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,4], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,4], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(62,74+1)])for y in range(22,35+1)]),
	).to_cnf()
Net3_Subnet4_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,4], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,4], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	).to_cnf()
Net3_Subnet4_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,4], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,4], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(62,74+1)])for y in range(22,35+1)])
	).to_cnf()
Net3_Subnet4_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,4], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,4], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(62,74+1)])for y in range(22,35+1)])
	).to_cnf()
Net3_Subnet4_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,4], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(62,74+1)])for y in range(22,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,4], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	).to_cnf()
Net3_Subnet4_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,4], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(62,74+1)])for y in range(22,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,4], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(62,74+1)])for y in range(22,35+1)]),
	).to_cnf()
Net3_Subnet4_DR = And(Net3_Subnet4_DR_Trend, Net3_Subnet4_DR_GIL_HorMinWidth,Net3_Subnet4_DR_GIL_HorMinSpacing,Net3_Subnet4_DR_GIL_VerMinSpacing,Net3_Subnet4_DR_AIL2_VerMinWidth,Net3_Subnet4_DR_AIL2_VerMinSpacing,Net3_Subnet4_DR_VerAIL2_HorMinSpacing,Net3_Subnet4_DR_MINT1AB_HorMinWidth,Net3_Subnet4_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet4_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet4_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet4_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet4_DR_M1AB_MinWidth,Net3_Subnet4_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet4_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet4_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet4_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet4_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet4_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet4_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet4_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet4_DR_V0_HorMinSpacing,Net3_Subnet4_DR_V1_HorMinSpacing,Net3_Subnet4_DR_V0_VerMinSpacing,Net3_Subnet4_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet4_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[66,28,0,0, 66,29,0,0, 66,30,0,0, 66,31,0,0, 66,32,0,0, 66,33,0,0, ],6,62,22,1,74,35,3,4),
	RConstraints.R1(Edge_Net_Subnet3,[70,26,0,0, 70,27,0,0, 70,28,0,0, 70,29,0,0, 70,30,0,0, 70,31,0,0, 70,32,0,0, 70,33,0,0, ],8,62,22,1,74,35,3,4),
	).to_cnf()
Net3_Subnet4_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[66,28,0, 66,29,0, 66,30,0, 66,31,0, 66,32,0, 66,33,0, 66,34,0, 70,26,0, 70,27,0, 70,28,0, 70,29,0, 70,30,0, 70,31,0, 70,32,0, 70,33,0, 70,34,0, ],16,62,22,0,74,35,3,4,2),
	)
Net3_Subnet4_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(62,74+1)])for y in range(22,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,5+1)])for x in range(62,74+1)])for y in range(22,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet4_R = And(Net3_Subnet4_R1,Net3_Subnet4_R2,Net3_Subnet4_R3,)
Net3_Subnet4_Formula = And(Net3_Subnet4_C,Net3_Subnet4_DR,Net3_Subnet4_R)
# Net = 3 Subnet = 5 | Left -> Right [20,42] Top -> Bottom [0,35]
# Range R1(38,38,26,33)
# Range R2(24,24,0,35)
### Disable edges outside window
Edge_Net_Subnet3[0:20,0:35+1,0:3+1,0:2+1,0:2+1,5]=exprzeros(25920)
Edge_Net_Subnet3[42:85+1,0:35+1,0:3+1,0:2+1,0:2+1,5]=exprzeros(57024)

### Consistency Constraints
Net3_Subnet5_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(20,42+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet5_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,5]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(20,42+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet5_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,5],Xor(Edge_Net_Subnet3[x,y,2,trend,1,5],Edge_Net_Subnet3[x,y,2,trend,2,5])),And(~Edge_Net_Subnet3[x,y,2,trend,0,5],~Edge_Net_Subnet3[x,y,2,trend,1,5],~Edge_Net_Subnet3[x,y,2,trend,2,5]))for x in range(20,42+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet5_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,5],Xor(Edge_Net_Subnet3[x,y,3,1,1,5],Edge_Net_Subnet3[x,y,3,1,2,5])),And(~Edge_Net_Subnet3[x,y,3,1,0,5],~Edge_Net_Subnet3[x,y,3,1,1,5],~Edge_Net_Subnet3[x,y,3,1,2,5]))for x in range(20,42+1)])for y in range(0,35+1)]).to_cnf()
Net3_Subnet5_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,5],Xor(Edge_Net_Subnet3[x,y,1,trend,0,5],Edge_Net_Subnet3[x,y,1,trend,1,5])),And(~Edge_Net_Subnet3[x,y,1,trend,2,5],~Edge_Net_Subnet3[x,y,1,trend,0,5],~Edge_Net_Subnet3[x,y,1,trend,1,5]))for x in range(20,42+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet5_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,5], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0,5)]))for trend in range(0,1+1)])for x in range(20,42+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,5], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(5+1,10)]))for trend in range(0,1+1)])for x in range(20,42+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,5], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0,5)]))for trend in range(0,1+1)])for x in range(20,42+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,5], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(5+1,10)]))for trend in range(0,1+1)])for x in range(20,42+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet5_C = And(Net3_Subnet5_C1, Net3_Subnet5_C2,Net3_Subnet5_C3_ME1_Mask,Net3_Subnet5_C4_MINT1_Mask,Net3_Subnet5_C5_AIL2GIL_Mask,Net3_Subnet5_C6,)
### Design Rules
Net3_Subnet5_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(20,42+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet5_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,5], ~Edge_Net_Subnet3[x-1,y,1,1,1,5]), And(Edge_Net_Subnet3[x+1,y,1,1,1,5], Edge_Net_Subnet3[x+2,y,1,1,1,5], Edge_Net_Subnet3[x+3,y,1,1,1,5], ))for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,5], ~Edge_Net_Subnet3[x+1,y,1,1,1,5]), And(Edge_Net_Subnet3[x-1,y,1,1,1,5], Edge_Net_Subnet3[x-2,y,1,1,1,5], Edge_Net_Subnet3[x-3,y,1,1,1,5], ))for x in range(20,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet5_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,5], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,5], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(20,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet5_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,5], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(20,42+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,5], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(20,42+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet5_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,5]), And(Edge_Net_Subnet3[x,y+1,1,0,0,5], Edge_Net_Subnet3[x,y+2,1,0,0,5], Edge_Net_Subnet3[x,y+3,1,0,0,5], ))for x in range(20,42+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,5]), And(Edge_Net_Subnet3[x,y-1,1,0,0,5], Edge_Net_Subnet3[x,y-2,1,0,0,5], Edge_Net_Subnet3[x,y-3,1,0,0,5], ))for x in range(20,42+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,5], ~Edge_Net_Subnet3[x,y-1,1,0,0,5]), And(Edge_Net_Subnet3[x,y+1,1,0,0,5], Edge_Net_Subnet3[x,y+2,1,0,0,5], Edge_Net_Subnet3[x,y+3,1,0,0,5], ))for x in range(20,42+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,5], ~Edge_Net_Subnet3[x,y+1,1,0,0,5]), And(Edge_Net_Subnet3[x,y-1,1,0,0,5], Edge_Net_Subnet3[x,y-2,1,0,0,5], Edge_Net_Subnet3[x,y-3,1,0,0,5], ))for x in range(20,42+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net3_Subnet5_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,5], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(20,42+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,5], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(20,42+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,5], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(20,42+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,5], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(20,42+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,5], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(20,42+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,5], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(20,42+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net3_Subnet5_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,5], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,5], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(20,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet5_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,5], ~Edge_Net_Subnet3[x-1,y,3,1,mask,5]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,5], Edge_Net_Subnet3[x+2,y,3,1,mask,5], Edge_Net_Subnet3[x+3,y,3,1,mask,5], Edge_Net_Subnet3[x+4,y,3,1,mask,5], Edge_Net_Subnet3[x+5,y,3,1,mask,5], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,5], ~Edge_Net_Subnet3[x+1,y,3,1,mask,5]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,5], Edge_Net_Subnet3[x-2,y,3,1,mask,5], Edge_Net_Subnet3[x-3,y,3,1,mask,5], Edge_Net_Subnet3[x-4,y,3,1,mask,5], Edge_Net_Subnet3[x-5,y,3,1,mask,5], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet5_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,5], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,5], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet5_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,5], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,5], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet5_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,5], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(20,42+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,5], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(20,42+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet5_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,5], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,5], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(20,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet5_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,5], ~Edge_Net_Subnet3[x-1,y,2,1,mask,5]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,5], Edge_Net_Subnet3[x+2,y,2,1,mask,5], Edge_Net_Subnet3[x+3,y,2,1,mask,5], Edge_Net_Subnet3[x+4,y,2,1,mask,5], Edge_Net_Subnet3[x+5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,5], ~Edge_Net_Subnet3[x+1,y,2,1,mask,5]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,5], Edge_Net_Subnet3[x-2,y,2,1,mask,5], Edge_Net_Subnet3[x-3,y,2,1,mask,5], Edge_Net_Subnet3[x-4,y,2,1,mask,5], Edge_Net_Subnet3[x-5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,5], And(Edge_Net_Subnet3[x-1,y,2,1,mask,5], Edge_Net_Subnet3[x-2,y,2,1,mask,5], Edge_Net_Subnet3[x-3,y,2,1,mask,5], Edge_Net_Subnet3[x-4,y,2,1,mask,5], Edge_Net_Subnet3[x-5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(20,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,5], And(Edge_Net_Subnet3[x+1,y,2,1,mask,5], Edge_Net_Subnet3[x+2,y,2,1,mask,5], Edge_Net_Subnet3[x+3,y,2,1,mask,5], Edge_Net_Subnet3[x+4,y,2,1,mask,5], Edge_Net_Subnet3[x+5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(42-1,20)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,5], ~Edge_Net_Subnet3[x,y-1,2,0,mask,5]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,5], Edge_Net_Subnet3[x,y+2,2,0,mask,5], Edge_Net_Subnet3[x,y+3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,5], ~Edge_Net_Subnet3[x,y+1,2,0,mask,5]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,5], Edge_Net_Subnet3[x,y-2,2,0,mask,5], Edge_Net_Subnet3[x,y-3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,5], And(Edge_Net_Subnet3[x,y+1,2,0,mask,5], Edge_Net_Subnet3[x,y+2,2,0,mask,5], Edge_Net_Subnet3[x,y+3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,5], And(Edge_Net_Subnet3[x,y-1,2,0,mask,5], Edge_Net_Subnet3[x,y-2,2,0,mask,5], Edge_Net_Subnet3[x,y-3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet5_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,5], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,5], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(20,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet5_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,5], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,5], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet5_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,5], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(20,42+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,5], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(20,42+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net3_Subnet5_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,5], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,5], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net3_Subnet5_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,5], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(20,42+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,5], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(20,42+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet5_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,5], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,5], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(4,35+1)]),
	).to_cnf()
Net3_Subnet5_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,5], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,5], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(20,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet5_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,5], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,5], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet5_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,5], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,5], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet5_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,5], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,5], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet5_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,5], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,42+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,5], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,42+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet5_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,5], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,42+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,5], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,42+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet5_DR = And(Net3_Subnet5_DR_Trend, Net3_Subnet5_DR_GIL_HorMinWidth,Net3_Subnet5_DR_GIL_HorMinSpacing,Net3_Subnet5_DR_GIL_VerMinSpacing,Net3_Subnet5_DR_AIL2_VerMinWidth,Net3_Subnet5_DR_AIL2_VerMinSpacing,Net3_Subnet5_DR_VerAIL2_HorMinSpacing,Net3_Subnet5_DR_MINT1AB_HorMinWidth,Net3_Subnet5_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet5_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet5_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet5_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet5_DR_M1AB_MinWidth,Net3_Subnet5_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet5_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet5_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet5_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet5_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet5_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet5_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet5_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet5_DR_V0_HorMinSpacing,Net3_Subnet5_DR_V1_HorMinSpacing,Net3_Subnet5_DR_V0_VerMinSpacing,Net3_Subnet5_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet5_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[38,26,0,0, 38,27,0,0, 38,28,0,0, 38,29,0,0, 38,30,0,0, 38,31,0,0, 38,32,0,0, 38,33,0,0, ],8,20,0,1,42,35,3,5),
	RConstraints.R1(Edge_Net_Subnet3,[24,0,0,0, 24,1,0,0, 24,2,0,0, 24,3,0,0, 24,4,0,0, 24,5,0,0, 24,6,0,0, 24,7,0,0, 24,8,0,0, 24,9,0,0, 24,10,0,0, 24,11,0,0, 24,12,0,0, 24,13,0,0, 24,14,0,0, 24,15,0,0, 24,16,0,0, 24,17,0,0, 24,18,0,0, 24,19,0,0, 24,20,0,0, 24,21,0,0, 24,22,0,0, 24,23,0,0, 24,24,0,0, 24,25,0,0, 24,26,0,0, 24,27,0,0, 24,28,0,0, 24,29,0,0, 24,30,0,0, 24,31,0,0, 24,32,0,0, 24,33,0,0, 24,34,0,0, 24,35,0,0, ],36,20,0,1,42,35,3,5),
	).to_cnf()
Net3_Subnet5_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[38,26,0, 38,27,0, 38,28,0, 38,29,0, 38,30,0, 38,31,0, 38,32,0, 38,33,0, 38,34,0, 24,0,0, 24,1,0, 24,2,0, 24,3,0, 24,4,0, 24,5,0, 24,6,0, 24,7,0, 24,8,0, 24,9,0, 24,10,0, 24,11,0, 24,12,0, 24,13,0, 24,14,0, 24,15,0, 24,16,0, 24,17,0, 24,18,0, 24,19,0, 24,20,0, 24,21,0, 24,22,0, 24,23,0, 24,24,0, 24,25,0, 24,26,0, 24,27,0, 24,28,0, 24,29,0, 24,30,0, 24,31,0, 24,32,0, 24,33,0, 24,34,0, 24,35,0, ],45,20,0,0,42,35,3,5,2),
	)
Net3_Subnet5_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(20,42+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,5+1)])for x in range(20,42+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet5_R = And(Net3_Subnet5_R1,Net3_Subnet5_R2,Net3_Subnet5_R3,)
Net3_Subnet5_Formula = And(Net3_Subnet5_C,Net3_Subnet5_DR,Net3_Subnet5_R)
# Net = 3 Subnet = 6 | Left -> Right [12,28] Top -> Bottom [0,35]
# Range R1(24,24,0,35)
# Range R2(16,16,0,35)
### Disable edges outside window
Edge_Net_Subnet3[0:12,0:35+1,0:3+1,0:2+1,0:2+1,6]=exprzeros(15552)
Edge_Net_Subnet3[28:85+1,0:35+1,0:3+1,0:2+1,0:2+1,6]=exprzeros(75168)

### Consistency Constraints
Net3_Subnet6_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet6_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,6]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet6_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,6],Xor(Edge_Net_Subnet3[x,y,2,trend,1,6],Edge_Net_Subnet3[x,y,2,trend,2,6])),And(~Edge_Net_Subnet3[x,y,2,trend,0,6],~Edge_Net_Subnet3[x,y,2,trend,1,6],~Edge_Net_Subnet3[x,y,2,trend,2,6]))for x in range(12,28+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet6_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,6],Xor(Edge_Net_Subnet3[x,y,3,1,1,6],Edge_Net_Subnet3[x,y,3,1,2,6])),And(~Edge_Net_Subnet3[x,y,3,1,0,6],~Edge_Net_Subnet3[x,y,3,1,1,6],~Edge_Net_Subnet3[x,y,3,1,2,6]))for x in range(12,28+1)])for y in range(0,35+1)]).to_cnf()
Net3_Subnet6_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,6],Xor(Edge_Net_Subnet3[x,y,1,trend,0,6],Edge_Net_Subnet3[x,y,1,trend,1,6])),And(~Edge_Net_Subnet3[x,y,1,trend,2,6],~Edge_Net_Subnet3[x,y,1,trend,0,6],~Edge_Net_Subnet3[x,y,1,trend,1,6]))for x in range(12,28+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet6_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,6], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0,6)]))for trend in range(0,1+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,6], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(6+1,10)]))for trend in range(0,1+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,6], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0,6)]))for trend in range(0,1+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,6], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(6+1,10)]))for trend in range(0,1+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet6_C = And(Net3_Subnet6_C1, Net3_Subnet6_C2,Net3_Subnet6_C3_ME1_Mask,Net3_Subnet6_C4_MINT1_Mask,Net3_Subnet6_C5_AIL2GIL_Mask,Net3_Subnet6_C6,)
### Design Rules
Net3_Subnet6_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(12,28+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet6_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,6], ~Edge_Net_Subnet3[x-1,y,1,1,1,6]), And(Edge_Net_Subnet3[x+1,y,1,1,1,6], Edge_Net_Subnet3[x+2,y,1,1,1,6], Edge_Net_Subnet3[x+3,y,1,1,1,6], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,6], ~Edge_Net_Subnet3[x+1,y,1,1,1,6]), And(Edge_Net_Subnet3[x-1,y,1,1,1,6], Edge_Net_Subnet3[x-2,y,1,1,1,6], Edge_Net_Subnet3[x-3,y,1,1,1,6], ))for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet6_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,6], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,6], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet6_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,6], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(12,28+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,6], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(12,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet6_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,6]), And(Edge_Net_Subnet3[x,y+1,1,0,0,6], Edge_Net_Subnet3[x,y+2,1,0,0,6], Edge_Net_Subnet3[x,y+3,1,0,0,6], ))for x in range(12,28+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,6]), And(Edge_Net_Subnet3[x,y-1,1,0,0,6], Edge_Net_Subnet3[x,y-2,1,0,0,6], Edge_Net_Subnet3[x,y-3,1,0,0,6], ))for x in range(12,28+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,6], ~Edge_Net_Subnet3[x,y-1,1,0,0,6]), And(Edge_Net_Subnet3[x,y+1,1,0,0,6], Edge_Net_Subnet3[x,y+2,1,0,0,6], Edge_Net_Subnet3[x,y+3,1,0,0,6], ))for x in range(12,28+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,6], ~Edge_Net_Subnet3[x,y+1,1,0,0,6]), And(Edge_Net_Subnet3[x,y-1,1,0,0,6], Edge_Net_Subnet3[x,y-2,1,0,0,6], Edge_Net_Subnet3[x,y-3,1,0,0,6], ))for x in range(12,28+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net3_Subnet6_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,6], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(12,28+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,6], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(12,28+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,6], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(12,28+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,6], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(12,28+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,6], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(12,28+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,6], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(12,28+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net3_Subnet6_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,6], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,6], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet6_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,6], ~Edge_Net_Subnet3[x-1,y,3,1,mask,6]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,6], Edge_Net_Subnet3[x+2,y,3,1,mask,6], Edge_Net_Subnet3[x+3,y,3,1,mask,6], Edge_Net_Subnet3[x+4,y,3,1,mask,6], Edge_Net_Subnet3[x+5,y,3,1,mask,6], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,6], ~Edge_Net_Subnet3[x+1,y,3,1,mask,6]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,6], Edge_Net_Subnet3[x-2,y,3,1,mask,6], Edge_Net_Subnet3[x-3,y,3,1,mask,6], Edge_Net_Subnet3[x-4,y,3,1,mask,6], Edge_Net_Subnet3[x-5,y,3,1,mask,6], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet6_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,6], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,6], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet6_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,6], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,6], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet6_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,6], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(12,28+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,6], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(12,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet6_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,6], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,6], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet6_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,6], ~Edge_Net_Subnet3[x-1,y,2,1,mask,6]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,6], Edge_Net_Subnet3[x+2,y,2,1,mask,6], Edge_Net_Subnet3[x+3,y,2,1,mask,6], Edge_Net_Subnet3[x+4,y,2,1,mask,6], Edge_Net_Subnet3[x+5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,6], ~Edge_Net_Subnet3[x+1,y,2,1,mask,6]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,6], Edge_Net_Subnet3[x-2,y,2,1,mask,6], Edge_Net_Subnet3[x-3,y,2,1,mask,6], Edge_Net_Subnet3[x-4,y,2,1,mask,6], Edge_Net_Subnet3[x-5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,6], And(Edge_Net_Subnet3[x-1,y,2,1,mask,6], Edge_Net_Subnet3[x-2,y,2,1,mask,6], Edge_Net_Subnet3[x-3,y,2,1,mask,6], Edge_Net_Subnet3[x-4,y,2,1,mask,6], Edge_Net_Subnet3[x-5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(12,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,6], And(Edge_Net_Subnet3[x+1,y,2,1,mask,6], Edge_Net_Subnet3[x+2,y,2,1,mask,6], Edge_Net_Subnet3[x+3,y,2,1,mask,6], Edge_Net_Subnet3[x+4,y,2,1,mask,6], Edge_Net_Subnet3[x+5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(28-1,12)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,6], ~Edge_Net_Subnet3[x,y-1,2,0,mask,6]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,6], Edge_Net_Subnet3[x,y+2,2,0,mask,6], Edge_Net_Subnet3[x,y+3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,6], ~Edge_Net_Subnet3[x,y+1,2,0,mask,6]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,6], Edge_Net_Subnet3[x,y-2,2,0,mask,6], Edge_Net_Subnet3[x,y-3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,6], And(Edge_Net_Subnet3[x,y+1,2,0,mask,6], Edge_Net_Subnet3[x,y+2,2,0,mask,6], Edge_Net_Subnet3[x,y+3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,6], And(Edge_Net_Subnet3[x,y-1,2,0,mask,6], Edge_Net_Subnet3[x,y-2,2,0,mask,6], Edge_Net_Subnet3[x,y-3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet6_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,6], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,6], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet6_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,6], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,6], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet6_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,6], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(12,28+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,6], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(12,28+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net3_Subnet6_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,6], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,6], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net3_Subnet6_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,6], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(12,28+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,6], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(12,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet6_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,6], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,6], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(4,35+1)]),
	).to_cnf()
Net3_Subnet6_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,6], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,6], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(12,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet6_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,6], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,6], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet6_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,6], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,6], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet6_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,6], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,6], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet6_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,6], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,6], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet6_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,6], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,6], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet6_DR = And(Net3_Subnet6_DR_Trend, Net3_Subnet6_DR_GIL_HorMinWidth,Net3_Subnet6_DR_GIL_HorMinSpacing,Net3_Subnet6_DR_GIL_VerMinSpacing,Net3_Subnet6_DR_AIL2_VerMinWidth,Net3_Subnet6_DR_AIL2_VerMinSpacing,Net3_Subnet6_DR_VerAIL2_HorMinSpacing,Net3_Subnet6_DR_MINT1AB_HorMinWidth,Net3_Subnet6_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet6_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet6_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet6_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet6_DR_M1AB_MinWidth,Net3_Subnet6_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet6_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet6_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet6_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet6_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet6_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet6_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet6_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet6_DR_V0_HorMinSpacing,Net3_Subnet6_DR_V1_HorMinSpacing,Net3_Subnet6_DR_V0_VerMinSpacing,Net3_Subnet6_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet6_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[24,0,0,0, 24,1,0,0, 24,2,0,0, 24,3,0,0, 24,4,0,0, 24,5,0,0, 24,6,0,0, 24,7,0,0, 24,8,0,0, 24,9,0,0, 24,10,0,0, 24,11,0,0, 24,12,0,0, 24,13,0,0, 24,14,0,0, 24,15,0,0, 24,16,0,0, 24,17,0,0, 24,18,0,0, 24,19,0,0, 24,20,0,0, 24,21,0,0, 24,22,0,0, 24,23,0,0, 24,24,0,0, 24,25,0,0, 24,26,0,0, 24,27,0,0, 24,28,0,0, 24,29,0,0, 24,30,0,0, 24,31,0,0, 24,32,0,0, 24,33,0,0, 24,34,0,0, 24,35,0,0, ],36,12,0,1,28,35,3,6),
	RConstraints.R1(Edge_Net_Subnet3,[16,0,0,0, 16,1,0,0, 16,2,0,0, 16,3,0,0, 16,4,0,0, 16,5,0,0, 16,6,0,0, 16,7,0,0, 16,8,0,0, 16,9,0,0, 16,10,0,0, 16,11,0,0, 16,12,0,0, 16,13,0,0, 16,14,0,0, 16,15,0,0, 16,16,0,0, 16,17,0,0, 16,18,0,0, 16,19,0,0, 16,20,0,0, 16,21,0,0, 16,22,0,0, 16,23,0,0, 16,24,0,0, 16,25,0,0, 16,26,0,0, 16,27,0,0, 16,28,0,0, 16,29,0,0, 16,30,0,0, 16,31,0,0, 16,32,0,0, 16,33,0,0, 16,34,0,0, 16,35,0,0, ],36,12,0,1,28,35,3,6),
	).to_cnf()
Net3_Subnet6_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[24,0,0, 24,1,0, 24,2,0, 24,3,0, 24,4,0, 24,5,0, 24,6,0, 24,7,0, 24,8,0, 24,9,0, 24,10,0, 24,11,0, 24,12,0, 24,13,0, 24,14,0, 24,15,0, 24,16,0, 24,17,0, 24,18,0, 24,19,0, 24,20,0, 24,21,0, 24,22,0, 24,23,0, 24,24,0, 24,25,0, 24,26,0, 24,27,0, 24,28,0, 24,29,0, 24,30,0, 24,31,0, 24,32,0, 24,33,0, 24,34,0, 24,35,0, 16,0,0, 16,1,0, 16,2,0, 16,3,0, 16,4,0, 16,5,0, 16,6,0, 16,7,0, 16,8,0, 16,9,0, 16,10,0, 16,11,0, 16,12,0, 16,13,0, 16,14,0, 16,15,0, 16,16,0, 16,17,0, 16,18,0, 16,19,0, 16,20,0, 16,21,0, 16,22,0, 16,23,0, 16,24,0, 16,25,0, 16,26,0, 16,27,0, 16,28,0, 16,29,0, 16,30,0, 16,31,0, 16,32,0, 16,33,0, 16,34,0, 16,35,0, ],72,12,0,0,28,35,3,6,2),
	)
Net3_Subnet6_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,5+1)])for x in range(12,28+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet6_R = And(Net3_Subnet6_R1,Net3_Subnet6_R2,Net3_Subnet6_R3,)
Net3_Subnet6_Formula = And(Net3_Subnet6_C,Net3_Subnet6_DR,Net3_Subnet6_R)
# Net = 3 Subnet = 7 | Left -> Right [8,20] Top -> Bottom [0,35]
# Range R1(16,16,0,35)
# Range R2(12,12,0,35)
### Disable edges outside window
Edge_Net_Subnet3[0:8,0:35+1,0:3+1,0:2+1,0:2+1,7]=exprzeros(10368)
Edge_Net_Subnet3[20:85+1,0:35+1,0:3+1,0:2+1,0:2+1,7]=exprzeros(85536)

### Consistency Constraints
Net3_Subnet7_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet7_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,7]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet7_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,7],Xor(Edge_Net_Subnet3[x,y,2,trend,1,7],Edge_Net_Subnet3[x,y,2,trend,2,7])),And(~Edge_Net_Subnet3[x,y,2,trend,0,7],~Edge_Net_Subnet3[x,y,2,trend,1,7],~Edge_Net_Subnet3[x,y,2,trend,2,7]))for x in range(8,20+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet7_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,7],Xor(Edge_Net_Subnet3[x,y,3,1,1,7],Edge_Net_Subnet3[x,y,3,1,2,7])),And(~Edge_Net_Subnet3[x,y,3,1,0,7],~Edge_Net_Subnet3[x,y,3,1,1,7],~Edge_Net_Subnet3[x,y,3,1,2,7]))for x in range(8,20+1)])for y in range(0,35+1)]).to_cnf()
Net3_Subnet7_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,7],Xor(Edge_Net_Subnet3[x,y,1,trend,0,7],Edge_Net_Subnet3[x,y,1,trend,1,7])),And(~Edge_Net_Subnet3[x,y,1,trend,2,7],~Edge_Net_Subnet3[x,y,1,trend,0,7],~Edge_Net_Subnet3[x,y,1,trend,1,7]))for x in range(8,20+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet7_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,7], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0,7)]))for trend in range(0,1+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,7], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(7+1,10)]))for trend in range(0,1+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,7], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0,7)]))for trend in range(0,1+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,7], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(7+1,10)]))for trend in range(0,1+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet7_C = And(Net3_Subnet7_C1, Net3_Subnet7_C2,Net3_Subnet7_C3_ME1_Mask,Net3_Subnet7_C4_MINT1_Mask,Net3_Subnet7_C5_AIL2GIL_Mask,Net3_Subnet7_C6,)
### Design Rules
Net3_Subnet7_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(8,20+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet7_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,7], ~Edge_Net_Subnet3[x-1,y,1,1,1,7]), And(Edge_Net_Subnet3[x+1,y,1,1,1,7], Edge_Net_Subnet3[x+2,y,1,1,1,7], Edge_Net_Subnet3[x+3,y,1,1,1,7], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,7], ~Edge_Net_Subnet3[x+1,y,1,1,1,7]), And(Edge_Net_Subnet3[x-1,y,1,1,1,7], Edge_Net_Subnet3[x-2,y,1,1,1,7], Edge_Net_Subnet3[x-3,y,1,1,1,7], ))for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet7_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,7], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,7], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet7_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,7], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(8,20+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,7], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(8,20+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet7_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,7]), And(Edge_Net_Subnet3[x,y+1,1,0,0,7], Edge_Net_Subnet3[x,y+2,1,0,0,7], Edge_Net_Subnet3[x,y+3,1,0,0,7], ))for x in range(8,20+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,7]), And(Edge_Net_Subnet3[x,y-1,1,0,0,7], Edge_Net_Subnet3[x,y-2,1,0,0,7], Edge_Net_Subnet3[x,y-3,1,0,0,7], ))for x in range(8,20+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,7], ~Edge_Net_Subnet3[x,y-1,1,0,0,7]), And(Edge_Net_Subnet3[x,y+1,1,0,0,7], Edge_Net_Subnet3[x,y+2,1,0,0,7], Edge_Net_Subnet3[x,y+3,1,0,0,7], ))for x in range(8,20+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,7], ~Edge_Net_Subnet3[x,y+1,1,0,0,7]), And(Edge_Net_Subnet3[x,y-1,1,0,0,7], Edge_Net_Subnet3[x,y-2,1,0,0,7], Edge_Net_Subnet3[x,y-3,1,0,0,7], ))for x in range(8,20+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net3_Subnet7_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,7], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(8,20+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,7], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(8,20+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,7], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(8,20+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,7], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(8,20+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,7], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(8,20+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,7], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(8,20+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net3_Subnet7_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,7], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,7], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet7_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,7], ~Edge_Net_Subnet3[x-1,y,3,1,mask,7]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,7], Edge_Net_Subnet3[x+2,y,3,1,mask,7], Edge_Net_Subnet3[x+3,y,3,1,mask,7], Edge_Net_Subnet3[x+4,y,3,1,mask,7], Edge_Net_Subnet3[x+5,y,3,1,mask,7], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,7], ~Edge_Net_Subnet3[x+1,y,3,1,mask,7]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,7], Edge_Net_Subnet3[x-2,y,3,1,mask,7], Edge_Net_Subnet3[x-3,y,3,1,mask,7], Edge_Net_Subnet3[x-4,y,3,1,mask,7], Edge_Net_Subnet3[x-5,y,3,1,mask,7], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet7_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,7], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,7], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet7_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,7], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,7], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet7_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,7], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(8,20+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,7], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(8,20+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet7_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,7], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,7], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet7_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,7], ~Edge_Net_Subnet3[x-1,y,2,1,mask,7]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,7], Edge_Net_Subnet3[x+2,y,2,1,mask,7], Edge_Net_Subnet3[x+3,y,2,1,mask,7], Edge_Net_Subnet3[x+4,y,2,1,mask,7], Edge_Net_Subnet3[x+5,y,2,1,mask,7], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,7], ~Edge_Net_Subnet3[x+1,y,2,1,mask,7]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,7], Edge_Net_Subnet3[x-2,y,2,1,mask,7], Edge_Net_Subnet3[x-3,y,2,1,mask,7], Edge_Net_Subnet3[x-4,y,2,1,mask,7], Edge_Net_Subnet3[x-5,y,2,1,mask,7], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,7], And(Edge_Net_Subnet3[x-1,y,2,1,mask,7], Edge_Net_Subnet3[x-2,y,2,1,mask,7], Edge_Net_Subnet3[x-3,y,2,1,mask,7], Edge_Net_Subnet3[x-4,y,2,1,mask,7], Edge_Net_Subnet3[x-5,y,2,1,mask,7], ))for mask in range(1,2+1)])for x in range(8,8+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,7], And(Edge_Net_Subnet3[x+1,y,2,1,mask,7], Edge_Net_Subnet3[x+2,y,2,1,mask,7], Edge_Net_Subnet3[x+3,y,2,1,mask,7], Edge_Net_Subnet3[x+4,y,2,1,mask,7], Edge_Net_Subnet3[x+5,y,2,1,mask,7], ))for mask in range(1,2+1)])for x in range(20-1,8)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,7], ~Edge_Net_Subnet3[x,y-1,2,0,mask,7]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,7], Edge_Net_Subnet3[x,y+2,2,0,mask,7], Edge_Net_Subnet3[x,y+3,2,0,mask,7], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,7], ~Edge_Net_Subnet3[x,y+1,2,0,mask,7]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,7], Edge_Net_Subnet3[x,y-2,2,0,mask,7], Edge_Net_Subnet3[x,y-3,2,0,mask,7], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,7], And(Edge_Net_Subnet3[x,y+1,2,0,mask,7], Edge_Net_Subnet3[x,y+2,2,0,mask,7], Edge_Net_Subnet3[x,y+3,2,0,mask,7], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,7], And(Edge_Net_Subnet3[x,y-1,2,0,mask,7], Edge_Net_Subnet3[x,y-2,2,0,mask,7], Edge_Net_Subnet3[x,y-3,2,0,mask,7], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet7_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,7], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,7], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet7_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,7], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,7], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet7_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,7], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(8,20+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,7], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(8,20+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net3_Subnet7_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,7], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,7], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net3_Subnet7_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,7], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(8,20+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,7], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(8,20+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet7_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,7], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,7], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(4,35+1)]),
	).to_cnf()
Net3_Subnet7_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,7], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,7], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(8,20+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet7_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,7], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,7], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet7_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,7], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,7], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet7_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,7], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,7], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet7_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,7], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,7], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet7_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,7], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,7], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(8,20+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet7_DR = And(Net3_Subnet7_DR_Trend, Net3_Subnet7_DR_GIL_HorMinWidth,Net3_Subnet7_DR_GIL_HorMinSpacing,Net3_Subnet7_DR_GIL_VerMinSpacing,Net3_Subnet7_DR_AIL2_VerMinWidth,Net3_Subnet7_DR_AIL2_VerMinSpacing,Net3_Subnet7_DR_VerAIL2_HorMinSpacing,Net3_Subnet7_DR_MINT1AB_HorMinWidth,Net3_Subnet7_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet7_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet7_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet7_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet7_DR_M1AB_MinWidth,Net3_Subnet7_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet7_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet7_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet7_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet7_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet7_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet7_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet7_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet7_DR_V0_HorMinSpacing,Net3_Subnet7_DR_V1_HorMinSpacing,Net3_Subnet7_DR_V0_VerMinSpacing,Net3_Subnet7_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet7_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[16,0,0,0, 16,1,0,0, 16,2,0,0, 16,3,0,0, 16,4,0,0, 16,5,0,0, 16,6,0,0, 16,7,0,0, 16,8,0,0, 16,9,0,0, 16,10,0,0, 16,11,0,0, 16,12,0,0, 16,13,0,0, 16,14,0,0, 16,15,0,0, 16,16,0,0, 16,17,0,0, 16,18,0,0, 16,19,0,0, 16,20,0,0, 16,21,0,0, 16,22,0,0, 16,23,0,0, 16,24,0,0, 16,25,0,0, 16,26,0,0, 16,27,0,0, 16,28,0,0, 16,29,0,0, 16,30,0,0, 16,31,0,0, 16,32,0,0, 16,33,0,0, 16,34,0,0, 16,35,0,0, ],36,8,0,1,20,35,3,7),
	RConstraints.R1(Edge_Net_Subnet3,[12,0,0,0, 12,1,0,0, 12,2,0,0, 12,3,0,0, 12,4,0,0, 12,5,0,0, 12,6,0,0, 12,7,0,0, 12,8,0,0, 12,9,0,0, 12,10,0,0, 12,11,0,0, 12,12,0,0, 12,13,0,0, 12,14,0,0, 12,15,0,0, 12,16,0,0, 12,17,0,0, 12,18,0,0, 12,19,0,0, 12,20,0,0, 12,21,0,0, 12,22,0,0, 12,23,0,0, 12,24,0,0, 12,25,0,0, 12,26,0,0, 12,27,0,0, 12,28,0,0, 12,29,0,0, 12,30,0,0, 12,31,0,0, 12,32,0,0, 12,33,0,0, 12,34,0,0, 12,35,0,0, ],36,8,0,1,20,35,3,7),
	).to_cnf()
Net3_Subnet7_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[16,0,0, 16,1,0, 16,2,0, 16,3,0, 16,4,0, 16,5,0, 16,6,0, 16,7,0, 16,8,0, 16,9,0, 16,10,0, 16,11,0, 16,12,0, 16,13,0, 16,14,0, 16,15,0, 16,16,0, 16,17,0, 16,18,0, 16,19,0, 16,20,0, 16,21,0, 16,22,0, 16,23,0, 16,24,0, 16,25,0, 16,26,0, 16,27,0, 16,28,0, 16,29,0, 16,30,0, 16,31,0, 16,32,0, 16,33,0, 16,34,0, 16,35,0, 12,0,0, 12,1,0, 12,2,0, 12,3,0, 12,4,0, 12,5,0, 12,6,0, 12,7,0, 12,8,0, 12,9,0, 12,10,0, 12,11,0, 12,12,0, 12,13,0, 12,14,0, 12,15,0, 12,16,0, 12,17,0, 12,18,0, 12,19,0, 12,20,0, 12,21,0, 12,22,0, 12,23,0, 12,24,0, 12,25,0, 12,26,0, 12,27,0, 12,28,0, 12,29,0, 12,30,0, 12,31,0, 12,32,0, 12,33,0, 12,34,0, 12,35,0, ],72,8,0,0,20,35,3,7,2),
	)
Net3_Subnet7_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,5+1)])for x in range(8,20+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet7_R = And(Net3_Subnet7_R1,Net3_Subnet7_R2,Net3_Subnet7_R3,)
Net3_Subnet7_Formula = And(Net3_Subnet7_C,Net3_Subnet7_DR,Net3_Subnet7_R)
# Net = 3 Subnet = 8 | Left -> Right [4,16] Top -> Bottom [0,35]
# Range R1(12,12,0,35)
# Range R2(8,8,0,35)
### Disable edges outside window
Edge_Net_Subnet3[0:4,0:35+1,0:3+1,0:2+1,0:2+1,8]=exprzeros(5184)
Edge_Net_Subnet3[16:85+1,0:35+1,0:3+1,0:2+1,0:2+1,8]=exprzeros(90720)

### Consistency Constraints
Net3_Subnet8_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet8_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,8]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet8_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,8],Xor(Edge_Net_Subnet3[x,y,2,trend,1,8],Edge_Net_Subnet3[x,y,2,trend,2,8])),And(~Edge_Net_Subnet3[x,y,2,trend,0,8],~Edge_Net_Subnet3[x,y,2,trend,1,8],~Edge_Net_Subnet3[x,y,2,trend,2,8]))for x in range(4,16+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet8_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,8],Xor(Edge_Net_Subnet3[x,y,3,1,1,8],Edge_Net_Subnet3[x,y,3,1,2,8])),And(~Edge_Net_Subnet3[x,y,3,1,0,8],~Edge_Net_Subnet3[x,y,3,1,1,8],~Edge_Net_Subnet3[x,y,3,1,2,8]))for x in range(4,16+1)])for y in range(0,35+1)]).to_cnf()
Net3_Subnet8_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,8],Xor(Edge_Net_Subnet3[x,y,1,trend,0,8],Edge_Net_Subnet3[x,y,1,trend,1,8])),And(~Edge_Net_Subnet3[x,y,1,trend,2,8],~Edge_Net_Subnet3[x,y,1,trend,0,8],~Edge_Net_Subnet3[x,y,1,trend,1,8]))for x in range(4,16+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet8_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,8], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0,8)]))for trend in range(0,1+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,8], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(8+1,10)]))for trend in range(0,1+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,8], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0,8)]))for trend in range(0,1+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,8], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(8+1,10)]))for trend in range(0,1+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet8_C = And(Net3_Subnet8_C1, Net3_Subnet8_C2,Net3_Subnet8_C3_ME1_Mask,Net3_Subnet8_C4_MINT1_Mask,Net3_Subnet8_C5_AIL2GIL_Mask,Net3_Subnet8_C6,)
### Design Rules
Net3_Subnet8_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(4,16+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet8_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,8], ~Edge_Net_Subnet3[x-1,y,1,1,1,8]), And(Edge_Net_Subnet3[x+1,y,1,1,1,8], Edge_Net_Subnet3[x+2,y,1,1,1,8], Edge_Net_Subnet3[x+3,y,1,1,1,8], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,8], ~Edge_Net_Subnet3[x+1,y,1,1,1,8]), And(Edge_Net_Subnet3[x-1,y,1,1,1,8], Edge_Net_Subnet3[x-2,y,1,1,1,8], Edge_Net_Subnet3[x-3,y,1,1,1,8], ))for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet8_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,8], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,8], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet8_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,8], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(4,16+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,8], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(4,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet8_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,8]), And(Edge_Net_Subnet3[x,y+1,1,0,0,8], Edge_Net_Subnet3[x,y+2,1,0,0,8], Edge_Net_Subnet3[x,y+3,1,0,0,8], ))for x in range(4,16+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,8]), And(Edge_Net_Subnet3[x,y-1,1,0,0,8], Edge_Net_Subnet3[x,y-2,1,0,0,8], Edge_Net_Subnet3[x,y-3,1,0,0,8], ))for x in range(4,16+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,8], ~Edge_Net_Subnet3[x,y-1,1,0,0,8]), And(Edge_Net_Subnet3[x,y+1,1,0,0,8], Edge_Net_Subnet3[x,y+2,1,0,0,8], Edge_Net_Subnet3[x,y+3,1,0,0,8], ))for x in range(4,16+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,8], ~Edge_Net_Subnet3[x,y+1,1,0,0,8]), And(Edge_Net_Subnet3[x,y-1,1,0,0,8], Edge_Net_Subnet3[x,y-2,1,0,0,8], Edge_Net_Subnet3[x,y-3,1,0,0,8], ))for x in range(4,16+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net3_Subnet8_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,8], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(4,16+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,8], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(4,16+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,8], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(4,16+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,8], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(4,16+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,8], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(4,16+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,8], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(4,16+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net3_Subnet8_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,8], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,8], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet8_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,8], ~Edge_Net_Subnet3[x-1,y,3,1,mask,8]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,8], Edge_Net_Subnet3[x+2,y,3,1,mask,8], Edge_Net_Subnet3[x+3,y,3,1,mask,8], Edge_Net_Subnet3[x+4,y,3,1,mask,8], Edge_Net_Subnet3[x+5,y,3,1,mask,8], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,8], ~Edge_Net_Subnet3[x+1,y,3,1,mask,8]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,8], Edge_Net_Subnet3[x-2,y,3,1,mask,8], Edge_Net_Subnet3[x-3,y,3,1,mask,8], Edge_Net_Subnet3[x-4,y,3,1,mask,8], Edge_Net_Subnet3[x-5,y,3,1,mask,8], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet8_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,8], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,8], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet8_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,8], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,8], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet8_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,8], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(4,16+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,8], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(4,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet8_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,8], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,8], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet8_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,8], ~Edge_Net_Subnet3[x-1,y,2,1,mask,8]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,8], Edge_Net_Subnet3[x+2,y,2,1,mask,8], Edge_Net_Subnet3[x+3,y,2,1,mask,8], Edge_Net_Subnet3[x+4,y,2,1,mask,8], Edge_Net_Subnet3[x+5,y,2,1,mask,8], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,8], ~Edge_Net_Subnet3[x+1,y,2,1,mask,8]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,8], Edge_Net_Subnet3[x-2,y,2,1,mask,8], Edge_Net_Subnet3[x-3,y,2,1,mask,8], Edge_Net_Subnet3[x-4,y,2,1,mask,8], Edge_Net_Subnet3[x-5,y,2,1,mask,8], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,8], And(Edge_Net_Subnet3[x-1,y,2,1,mask,8], Edge_Net_Subnet3[x-2,y,2,1,mask,8], Edge_Net_Subnet3[x-3,y,2,1,mask,8], Edge_Net_Subnet3[x-4,y,2,1,mask,8], Edge_Net_Subnet3[x-5,y,2,1,mask,8], ))for mask in range(1,2+1)])for x in range(4,4+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,8], And(Edge_Net_Subnet3[x+1,y,2,1,mask,8], Edge_Net_Subnet3[x+2,y,2,1,mask,8], Edge_Net_Subnet3[x+3,y,2,1,mask,8], Edge_Net_Subnet3[x+4,y,2,1,mask,8], Edge_Net_Subnet3[x+5,y,2,1,mask,8], ))for mask in range(1,2+1)])for x in range(16-1,4)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,8], ~Edge_Net_Subnet3[x,y-1,2,0,mask,8]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,8], Edge_Net_Subnet3[x,y+2,2,0,mask,8], Edge_Net_Subnet3[x,y+3,2,0,mask,8], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,8], ~Edge_Net_Subnet3[x,y+1,2,0,mask,8]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,8], Edge_Net_Subnet3[x,y-2,2,0,mask,8], Edge_Net_Subnet3[x,y-3,2,0,mask,8], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,8], And(Edge_Net_Subnet3[x,y+1,2,0,mask,8], Edge_Net_Subnet3[x,y+2,2,0,mask,8], Edge_Net_Subnet3[x,y+3,2,0,mask,8], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,8], And(Edge_Net_Subnet3[x,y-1,2,0,mask,8], Edge_Net_Subnet3[x,y-2,2,0,mask,8], Edge_Net_Subnet3[x,y-3,2,0,mask,8], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet8_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,8], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,8], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet8_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,8], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,8], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet8_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,8], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(4,16+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,8], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(4,16+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net3_Subnet8_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,8], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,8], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net3_Subnet8_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,8], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(4,16+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,8], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(4,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet8_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,8], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,8], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(4,35+1)]),
	).to_cnf()
Net3_Subnet8_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,8], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,8], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet8_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,8], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,8], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet8_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,8], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,8], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet8_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,8], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,8], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet8_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,8], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,8], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet8_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,8], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,8], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet8_DR = And(Net3_Subnet8_DR_Trend, Net3_Subnet8_DR_GIL_HorMinWidth,Net3_Subnet8_DR_GIL_HorMinSpacing,Net3_Subnet8_DR_GIL_VerMinSpacing,Net3_Subnet8_DR_AIL2_VerMinWidth,Net3_Subnet8_DR_AIL2_VerMinSpacing,Net3_Subnet8_DR_VerAIL2_HorMinSpacing,Net3_Subnet8_DR_MINT1AB_HorMinWidth,Net3_Subnet8_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet8_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet8_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet8_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet8_DR_M1AB_MinWidth,Net3_Subnet8_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet8_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet8_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet8_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet8_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet8_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet8_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet8_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet8_DR_V0_HorMinSpacing,Net3_Subnet8_DR_V1_HorMinSpacing,Net3_Subnet8_DR_V0_VerMinSpacing,Net3_Subnet8_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet8_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[12,0,0,0, 12,1,0,0, 12,2,0,0, 12,3,0,0, 12,4,0,0, 12,5,0,0, 12,6,0,0, 12,7,0,0, 12,8,0,0, 12,9,0,0, 12,10,0,0, 12,11,0,0, 12,12,0,0, 12,13,0,0, 12,14,0,0, 12,15,0,0, 12,16,0,0, 12,17,0,0, 12,18,0,0, 12,19,0,0, 12,20,0,0, 12,21,0,0, 12,22,0,0, 12,23,0,0, 12,24,0,0, 12,25,0,0, 12,26,0,0, 12,27,0,0, 12,28,0,0, 12,29,0,0, 12,30,0,0, 12,31,0,0, 12,32,0,0, 12,33,0,0, 12,34,0,0, 12,35,0,0, ],36,4,0,1,16,35,3,8),
	RConstraints.R1(Edge_Net_Subnet3,[8,0,0,0, 8,1,0,0, 8,2,0,0, 8,3,0,0, 8,4,0,0, 8,5,0,0, 8,6,0,0, 8,7,0,0, 8,8,0,0, 8,9,0,0, 8,10,0,0, 8,11,0,0, 8,12,0,0, 8,13,0,0, 8,14,0,0, 8,15,0,0, 8,16,0,0, 8,17,0,0, 8,18,0,0, 8,19,0,0, 8,20,0,0, 8,21,0,0, 8,22,0,0, 8,23,0,0, 8,24,0,0, 8,25,0,0, 8,26,0,0, 8,27,0,0, 8,28,0,0, 8,29,0,0, 8,30,0,0, 8,31,0,0, 8,32,0,0, 8,33,0,0, 8,34,0,0, 8,35,0,0, ],36,4,0,1,16,35,3,8),
	).to_cnf()
Net3_Subnet8_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[12,0,0, 12,1,0, 12,2,0, 12,3,0, 12,4,0, 12,5,0, 12,6,0, 12,7,0, 12,8,0, 12,9,0, 12,10,0, 12,11,0, 12,12,0, 12,13,0, 12,14,0, 12,15,0, 12,16,0, 12,17,0, 12,18,0, 12,19,0, 12,20,0, 12,21,0, 12,22,0, 12,23,0, 12,24,0, 12,25,0, 12,26,0, 12,27,0, 12,28,0, 12,29,0, 12,30,0, 12,31,0, 12,32,0, 12,33,0, 12,34,0, 12,35,0, 8,0,0, 8,1,0, 8,2,0, 8,3,0, 8,4,0, 8,5,0, 8,6,0, 8,7,0, 8,8,0, 8,9,0, 8,10,0, 8,11,0, 8,12,0, 8,13,0, 8,14,0, 8,15,0, 8,16,0, 8,17,0, 8,18,0, 8,19,0, 8,20,0, 8,21,0, 8,22,0, 8,23,0, 8,24,0, 8,25,0, 8,26,0, 8,27,0, 8,28,0, 8,29,0, 8,30,0, 8,31,0, 8,32,0, 8,33,0, 8,34,0, 8,35,0, ],72,4,0,0,16,35,3,8,2),
	)
Net3_Subnet8_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,5+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet8_R = And(Net3_Subnet8_R1,Net3_Subnet8_R2,Net3_Subnet8_R3,)
Net3_Subnet8_Formula = And(Net3_Subnet8_C,Net3_Subnet8_DR,Net3_Subnet8_R)
# Net = 3 Subnet = 9 | Left -> Right [0,12] Top -> Bottom [0,35]
# Range R1(8,8,0,35)
# Range R2(4,4,0,35)
### Disable edges outside window
Edge_Net_Subnet3[12:85+1,0:35+1,0:3+1,0:2+1,0:2+1,9]=exprzeros(95904)

### Consistency Constraints
Net3_Subnet9_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet9_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,9]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet9_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,9],Xor(Edge_Net_Subnet3[x,y,2,trend,1,9],Edge_Net_Subnet3[x,y,2,trend,2,9])),And(~Edge_Net_Subnet3[x,y,2,trend,0,9],~Edge_Net_Subnet3[x,y,2,trend,1,9],~Edge_Net_Subnet3[x,y,2,trend,2,9]))for x in range(0,12+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet9_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,9],Xor(Edge_Net_Subnet3[x,y,3,1,1,9],Edge_Net_Subnet3[x,y,3,1,2,9])),And(~Edge_Net_Subnet3[x,y,3,1,0,9],~Edge_Net_Subnet3[x,y,3,1,1,9],~Edge_Net_Subnet3[x,y,3,1,2,9]))for x in range(0,12+1)])for y in range(0,35+1)]).to_cnf()
Net3_Subnet9_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,9],Xor(Edge_Net_Subnet3[x,y,1,trend,0,9],Edge_Net_Subnet3[x,y,1,trend,1,9])),And(~Edge_Net_Subnet3[x,y,1,trend,2,9],~Edge_Net_Subnet3[x,y,1,trend,0,9],~Edge_Net_Subnet3[x,y,1,trend,1,9]))for x in range(0,12+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet9_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,9], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0,9)]))for trend in range(0,1+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,9], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0,9)]))for trend in range(0,1+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet9_C = And(Net3_Subnet9_C1, Net3_Subnet9_C2,Net3_Subnet9_C3_ME1_Mask,Net3_Subnet9_C4_MINT1_Mask,Net3_Subnet9_C5_AIL2GIL_Mask,Net3_Subnet9_C6,)
### Design Rules
Net3_Subnet9_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(0,12+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet9_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,9], ~Edge_Net_Subnet3[x-1,y,1,1,1,9]), And(Edge_Net_Subnet3[x+1,y,1,1,1,9], Edge_Net_Subnet3[x+2,y,1,1,1,9], Edge_Net_Subnet3[x+3,y,1,1,1,9], ))for x in range(1,12+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,9], ~Edge_Net_Subnet3[x+1,y,1,1,1,9]), And(Edge_Net_Subnet3[x-1,y,1,1,1,9], Edge_Net_Subnet3[x-2,y,1,1,1,9], Edge_Net_Subnet3[x-3,y,1,1,1,9], ))for x in range(3,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet9_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,9], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,9], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet9_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,9], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(0,12+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,9], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(0,12+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet9_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,9]), And(Edge_Net_Subnet3[x,y+1,1,0,0,9], Edge_Net_Subnet3[x,y+2,1,0,0,9], Edge_Net_Subnet3[x,y+3,1,0,0,9], ))for x in range(0,12+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,9]), And(Edge_Net_Subnet3[x,y-1,1,0,0,9], Edge_Net_Subnet3[x,y-2,1,0,0,9], Edge_Net_Subnet3[x,y-3,1,0,0,9], ))for x in range(0,12+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,9], ~Edge_Net_Subnet3[x,y-1,1,0,0,9]), And(Edge_Net_Subnet3[x,y+1,1,0,0,9], Edge_Net_Subnet3[x,y+2,1,0,0,9], Edge_Net_Subnet3[x,y+3,1,0,0,9], ))for x in range(0,12+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,9], ~Edge_Net_Subnet3[x,y+1,1,0,0,9]), And(Edge_Net_Subnet3[x,y-1,1,0,0,9], Edge_Net_Subnet3[x,y-2,1,0,0,9], Edge_Net_Subnet3[x,y-3,1,0,0,9], ))for x in range(0,12+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net3_Subnet9_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,9], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(0,12+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,9], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(0,12+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,9], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(0,12+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,9], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(0,12+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,9], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(0,12+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,9], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(0,12+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net3_Subnet9_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,9], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,9], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet9_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,9], ~Edge_Net_Subnet3[x-1,y,3,1,mask,9]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,9], Edge_Net_Subnet3[x+2,y,3,1,mask,9], Edge_Net_Subnet3[x+3,y,3,1,mask,9], Edge_Net_Subnet3[x+4,y,3,1,mask,9], Edge_Net_Subnet3[x+5,y,3,1,mask,9], ))for mask in range(1,2+1)])for x in range(1,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,9], ~Edge_Net_Subnet3[x+1,y,3,1,mask,9]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,9], Edge_Net_Subnet3[x-2,y,3,1,mask,9], Edge_Net_Subnet3[x-3,y,3,1,mask,9], Edge_Net_Subnet3[x-4,y,3,1,mask,9], Edge_Net_Subnet3[x-5,y,3,1,mask,9], ))for mask in range(1,2+1)])for x in range(5,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,9], And(Edge_Net_Subnet3[x+1,y,3,1,mask,9], Edge_Net_Subnet3[x+2,y,3,1,mask,9], Edge_Net_Subnet3[x+3,y,3,1,mask,9], Edge_Net_Subnet3[x+4,y,3,1,mask,9], Edge_Net_Subnet3[x+5,y,3,1,mask,9], ))for mask in range(1,2+1)])for x in range(0, 0+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet9_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,9], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,9], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet9_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,9], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,9], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet9_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,9], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(0,12+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,9], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(0,12+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet9_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,9], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,9], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet9_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,9], ~Edge_Net_Subnet3[x-1,y,2,1,mask,9]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,9], Edge_Net_Subnet3[x+2,y,2,1,mask,9], Edge_Net_Subnet3[x+3,y,2,1,mask,9], Edge_Net_Subnet3[x+4,y,2,1,mask,9], Edge_Net_Subnet3[x+5,y,2,1,mask,9], ))for mask in range(1,2+1)])for x in range(1,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,9], ~Edge_Net_Subnet3[x+1,y,2,1,mask,9]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,9], Edge_Net_Subnet3[x-2,y,2,1,mask,9], Edge_Net_Subnet3[x-3,y,2,1,mask,9], Edge_Net_Subnet3[x-4,y,2,1,mask,9], Edge_Net_Subnet3[x-5,y,2,1,mask,9], ))for mask in range(1,2+1)])for x in range(5,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,9], And(Edge_Net_Subnet3[x-1,y,2,1,mask,9], Edge_Net_Subnet3[x-2,y,2,1,mask,9], Edge_Net_Subnet3[x-3,y,2,1,mask,9], Edge_Net_Subnet3[x-4,y,2,1,mask,9], Edge_Net_Subnet3[x-5,y,2,1,mask,9], ))for mask in range(1,2+1)])for x in range(0,0+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,9], And(Edge_Net_Subnet3[x+1,y,2,1,mask,9], Edge_Net_Subnet3[x+2,y,2,1,mask,9], Edge_Net_Subnet3[x+3,y,2,1,mask,9], Edge_Net_Subnet3[x+4,y,2,1,mask,9], Edge_Net_Subnet3[x+5,y,2,1,mask,9], ))for mask in range(1,2+1)])for x in range(12-1,0)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,9], ~Edge_Net_Subnet3[x,y-1,2,0,mask,9]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,9], Edge_Net_Subnet3[x,y+2,2,0,mask,9], Edge_Net_Subnet3[x,y+3,2,0,mask,9], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,9], ~Edge_Net_Subnet3[x,y+1,2,0,mask,9]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,9], Edge_Net_Subnet3[x,y-2,2,0,mask,9], Edge_Net_Subnet3[x,y-3,2,0,mask,9], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,9], And(Edge_Net_Subnet3[x,y+1,2,0,mask,9], Edge_Net_Subnet3[x,y+2,2,0,mask,9], Edge_Net_Subnet3[x,y+3,2,0,mask,9], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,9], And(Edge_Net_Subnet3[x,y-1,2,0,mask,9], Edge_Net_Subnet3[x,y-2,2,0,mask,9], Edge_Net_Subnet3[x,y-3,2,0,mask,9], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet9_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,9], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,9], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet9_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,9], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,9], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet9_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,9], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(0,12+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,9], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(0,12+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net3_Subnet9_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,9], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,9], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net3_Subnet9_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,9], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(0,12+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,9], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(0,12+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet9_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,9], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,9], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(4,35+1)]),
	).to_cnf()
Net3_Subnet9_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,9], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,9], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet9_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,9], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,9], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,12+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet9_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,9], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,9], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet9_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,9], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,9], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet9_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,9], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,9], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet9_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,9], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,9], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet9_DR = And(Net3_Subnet9_DR_Trend, Net3_Subnet9_DR_GIL_HorMinWidth,Net3_Subnet9_DR_GIL_HorMinSpacing,Net3_Subnet9_DR_GIL_VerMinSpacing,Net3_Subnet9_DR_AIL2_VerMinWidth,Net3_Subnet9_DR_AIL2_VerMinSpacing,Net3_Subnet9_DR_VerAIL2_HorMinSpacing,Net3_Subnet9_DR_MINT1AB_HorMinWidth,Net3_Subnet9_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet9_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet9_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet9_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet9_DR_M1AB_MinWidth,Net3_Subnet9_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet9_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet9_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet9_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet9_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet9_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet9_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet9_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet9_DR_V0_HorMinSpacing,Net3_Subnet9_DR_V1_HorMinSpacing,Net3_Subnet9_DR_V0_VerMinSpacing,Net3_Subnet9_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet9_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[8,0,0,0, 8,1,0,0, 8,2,0,0, 8,3,0,0, 8,4,0,0, 8,5,0,0, 8,6,0,0, 8,7,0,0, 8,8,0,0, 8,9,0,0, 8,10,0,0, 8,11,0,0, 8,12,0,0, 8,13,0,0, 8,14,0,0, 8,15,0,0, 8,16,0,0, 8,17,0,0, 8,18,0,0, 8,19,0,0, 8,20,0,0, 8,21,0,0, 8,22,0,0, 8,23,0,0, 8,24,0,0, 8,25,0,0, 8,26,0,0, 8,27,0,0, 8,28,0,0, 8,29,0,0, 8,30,0,0, 8,31,0,0, 8,32,0,0, 8,33,0,0, 8,34,0,0, 8,35,0,0, ],36,0,0,1,12,35,3,9),
	RConstraints.R1(Edge_Net_Subnet3,[4,0,0,0, 4,1,0,0, 4,2,0,0, 4,3,0,0, 4,4,0,0, 4,5,0,0, 4,6,0,0, 4,7,0,0, 4,8,0,0, 4,9,0,0, 4,10,0,0, 4,11,0,0, 4,12,0,0, 4,13,0,0, 4,14,0,0, 4,15,0,0, 4,16,0,0, 4,17,0,0, 4,18,0,0, 4,19,0,0, 4,20,0,0, 4,21,0,0, 4,22,0,0, 4,23,0,0, 4,24,0,0, 4,25,0,0, 4,26,0,0, 4,27,0,0, 4,28,0,0, 4,29,0,0, 4,30,0,0, 4,31,0,0, 4,32,0,0, 4,33,0,0, 4,34,0,0, 4,35,0,0, ],36,0,0,1,12,35,3,9),
	).to_cnf()
Net3_Subnet9_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[8,0,0, 8,1,0, 8,2,0, 8,3,0, 8,4,0, 8,5,0, 8,6,0, 8,7,0, 8,8,0, 8,9,0, 8,10,0, 8,11,0, 8,12,0, 8,13,0, 8,14,0, 8,15,0, 8,16,0, 8,17,0, 8,18,0, 8,19,0, 8,20,0, 8,21,0, 8,22,0, 8,23,0, 8,24,0, 8,25,0, 8,26,0, 8,27,0, 8,28,0, 8,29,0, 8,30,0, 8,31,0, 8,32,0, 8,33,0, 8,34,0, 8,35,0, 4,0,0, 4,1,0, 4,2,0, 4,3,0, 4,4,0, 4,5,0, 4,6,0, 4,7,0, 4,8,0, 4,9,0, 4,10,0, 4,11,0, 4,12,0, 4,13,0, 4,14,0, 4,15,0, 4,16,0, 4,17,0, 4,18,0, 4,19,0, 4,20,0, 4,21,0, 4,22,0, 4,23,0, 4,24,0, 4,25,0, 4,26,0, 4,27,0, 4,28,0, 4,29,0, 4,30,0, 4,31,0, 4,32,0, 4,33,0, 4,34,0, 4,35,0, ],72,0,0,0,12,35,3,9,2),
	)
Net3_Subnet9_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,5+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet9_R = And(Net3_Subnet9_R1,Net3_Subnet9_R2,Net3_Subnet9_R3,)
Net3_Subnet9_Formula = And(Net3_Subnet9_C,Net3_Subnet9_DR,Net3_Subnet9_R)
# Net = 8 Subnet = 1 | Left -> Right [44,60] Top -> Bottom [0,35]
# Range R1(48,48,0,35)
# Range R2(56,56,0,35)
### Disable edges outside window
Edge_Net_Subnet8[0:44,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(57024)
Edge_Net_Subnet8[60:85+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(33696)

### Consistency Constraints
Net8_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,7]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(44,60+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net8_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet8[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,7])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(44,60+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net8_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet8[x,y,2,trend,0,1],Xor(Edge_Net_Subnet8[x,y,2,trend,1,1],Edge_Net_Subnet8[x,y,2,trend,2,1])),And(~Edge_Net_Subnet8[x,y,2,trend,0,1],~Edge_Net_Subnet8[x,y,2,trend,1,1],~Edge_Net_Subnet8[x,y,2,trend,2,1]))for x in range(44,60+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net8_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet8[x,y,3,1,0,1],Xor(Edge_Net_Subnet8[x,y,3,1,1,1],Edge_Net_Subnet8[x,y,3,1,2,1])),And(~Edge_Net_Subnet8[x,y,3,1,0,1],~Edge_Net_Subnet8[x,y,3,1,1,1],~Edge_Net_Subnet8[x,y,3,1,2,1]))for x in range(44,60+1)])for y in range(0,35+1)]).to_cnf()
Net8_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet8[x,y,1,trend,2,1],Xor(Edge_Net_Subnet8[x,y,1,trend,0,1],Edge_Net_Subnet8[x,y,1,trend,1,1])),And(~Edge_Net_Subnet8[x,y,1,trend,2,1],~Edge_Net_Subnet8[x,y,1,trend,0,1],~Edge_Net_Subnet8[x,y,1,trend,1,1]))for x in range(44,60+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net8_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(44,60+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,2,s2])for s2 in range(1+1,5)]))for trend in range(0,1+1)])for x in range(44,60+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(44,60+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,1,s2])for s2 in range(1+1,5)]))for trend in range(0,1+1)])for x in range(44,60+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net8_Subnet1_C = And(Net8_Subnet1_C1, Net8_Subnet1_C2,Net8_Subnet1_C3_ME1_Mask,Net8_Subnet1_C4_MINT1_Mask,Net8_Subnet1_C5_AIL2GIL_Mask,Net8_Subnet1_C6,)
### Design Rules
Net8_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(44,60+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net8_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,1,1,1,1], ~Edge_Net_Subnet8[x-1,y,1,1,1,1]), And(Edge_Net_Subnet8[x+1,y,1,1,1,1], Edge_Net_Subnet8[x+2,y,1,1,1,1], Edge_Net_Subnet8[x+3,y,1,1,1,1], ))for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,1,1,1,1], ~Edge_Net_Subnet8[x+1,y,1,1,1,1]), And(Edge_Net_Subnet8[x-1,y,1,1,1,1], Edge_Net_Subnet8[x-2,y,1,1,1,1], Edge_Net_Subnet8[x-3,y,1,1,1,1], ))for x in range(44,60+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(44,60+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(44,60+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(44,60+1)])for y in range(3,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1]), And(Edge_Net_Subnet8[x,y+1,1,0,0,1], Edge_Net_Subnet8[x,y+2,1,0,0,1], Edge_Net_Subnet8[x,y+3,1,0,0,1], ))for x in range(44,60+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1]), And(Edge_Net_Subnet8[x,y-1,1,0,0,1], Edge_Net_Subnet8[x,y-2,1,0,0,1], Edge_Net_Subnet8[x,y-3,1,0,0,1], ))for x in range(44,60+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge_Net_Subnet8[x,y-1,1,0,0,1]), And(Edge_Net_Subnet8[x,y+1,1,0,0,1], Edge_Net_Subnet8[x,y+2,1,0,0,1], Edge_Net_Subnet8[x,y+3,1,0,0,1], ))for x in range(44,60+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge_Net_Subnet8[x,y+1,1,0,0,1]), And(Edge_Net_Subnet8[x,y-1,1,0,0,1], Edge_Net_Subnet8[x,y-2,1,0,0,1], Edge_Net_Subnet8[x,y-3,1,0,0,1], ))for x in range(44,60+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net8_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(44,60+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(44,60+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(44,60+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(44,60+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(44,60+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(44,60+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net8_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(44,60+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,3,1,mask,1], ~Edge_Net_Subnet8[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet8[x+1,y,3,1,mask,1], Edge_Net_Subnet8[x+2,y,3,1,mask,1], Edge_Net_Subnet8[x+3,y,3,1,mask,1], Edge_Net_Subnet8[x+4,y,3,1,mask,1], Edge_Net_Subnet8[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,3,1,mask,1], ~Edge_Net_Subnet8[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet8[x-1,y,3,1,mask,1], Edge_Net_Subnet8[x-2,y,3,1,mask,1], Edge_Net_Subnet8[x-3,y,3,1,mask,1], Edge_Net_Subnet8[x-4,y,3,1,mask,1], Edge_Net_Subnet8[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(3,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(44,60+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(44,60+1)])for y in range(2,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(44,60+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,2,1,mask,1], ~Edge_Net_Subnet8[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet8[x+1,y,2,1,mask,1], Edge_Net_Subnet8[x+2,y,2,1,mask,1], Edge_Net_Subnet8[x+3,y,2,1,mask,1], Edge_Net_Subnet8[x+4,y,2,1,mask,1], Edge_Net_Subnet8[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,2,1,mask,1], ~Edge_Net_Subnet8[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet8[x-1,y,2,1,mask,1], Edge_Net_Subnet8[x-2,y,2,1,mask,1], Edge_Net_Subnet8[x-3,y,2,1,mask,1], Edge_Net_Subnet8[x-4,y,2,1,mask,1], Edge_Net_Subnet8[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,1], And(Edge_Net_Subnet8[x-1,y,2,1,mask,1], Edge_Net_Subnet8[x-2,y,2,1,mask,1], Edge_Net_Subnet8[x-3,y,2,1,mask,1], Edge_Net_Subnet8[x-4,y,2,1,mask,1], Edge_Net_Subnet8[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(44,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,1], And(Edge_Net_Subnet8[x+1,y,2,1,mask,1], Edge_Net_Subnet8[x+2,y,2,1,mask,1], Edge_Net_Subnet8[x+3,y,2,1,mask,1], Edge_Net_Subnet8[x+4,y,2,1,mask,1], Edge_Net_Subnet8[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(60-1,44)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,1], ~Edge_Net_Subnet8[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet8[x,y+1,2,0,mask,1], Edge_Net_Subnet8[x,y+2,2,0,mask,1], Edge_Net_Subnet8[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,1], ~Edge_Net_Subnet8[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet8[x,y-1,2,0,mask,1], Edge_Net_Subnet8[x,y-2,2,0,mask,1], Edge_Net_Subnet8[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet8[x,y,2,0,mask,1], And(Edge_Net_Subnet8[x,y+1,2,0,mask,1], Edge_Net_Subnet8[x,y+2,2,0,mask,1], Edge_Net_Subnet8[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet8[x,y,2,0,mask,1], And(Edge_Net_Subnet8[x,y-1,2,0,mask,1], Edge_Net_Subnet8[x,y-2,2,0,mask,1], Edge_Net_Subnet8[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(35,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(44,60+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(44,60+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(44,60+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net8_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net8_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(44,60+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(44,60+1)])for y in range(3,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(4,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(44,60+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(44,60+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(44,60+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(44,60+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(44,60+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(44,60+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(44,60+1)])for y in range(2,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(44,60+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(44,60+1)])for y in range(2,35+1)]),
	).to_cnf()
Net8_Subnet1_DR = And(Net8_Subnet1_DR_Trend, Net8_Subnet1_DR_GIL_HorMinWidth,Net8_Subnet1_DR_GIL_HorMinSpacing,Net8_Subnet1_DR_GIL_VerMinSpacing,Net8_Subnet1_DR_AIL2_VerMinWidth,Net8_Subnet1_DR_AIL2_VerMinSpacing,Net8_Subnet1_DR_VerAIL2_HorMinSpacing,Net8_Subnet1_DR_MINT1AB_HorMinWidth,Net8_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net8_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net8_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net8_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net8_Subnet1_DR_M1AB_MinWidth,Net8_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net8_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net8_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net8_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net8_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net8_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net8_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net8_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net8_Subnet1_DR_V0_HorMinSpacing,Net8_Subnet1_DR_V1_HorMinSpacing,Net8_Subnet1_DR_V0_VerMinSpacing,Net8_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net8_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet8,[48,0,0,0, 48,1,0,0, 48,2,0,0, 48,3,0,0, 48,4,0,0, 48,5,0,0, 48,6,0,0, 48,7,0,0, 48,8,0,0, 48,9,0,0, 48,10,0,0, 48,11,0,0, 48,12,0,0, 48,13,0,0, 48,14,0,0, 48,15,0,0, 48,16,0,0, 48,17,0,0, 48,18,0,0, 48,19,0,0, 48,20,0,0, 48,21,0,0, 48,22,0,0, 48,23,0,0, 48,24,0,0, 48,25,0,0, 48,26,0,0, 48,27,0,0, 48,28,0,0, 48,29,0,0, 48,30,0,0, 48,31,0,0, 48,32,0,0, 48,33,0,0, 48,34,0,0, 48,35,0,0, ],36,44,0,1,60,35,3,1),
	RConstraints.R1(Edge_Net_Subnet8,[56,0,0,0, 56,1,0,0, 56,2,0,0, 56,3,0,0, 56,4,0,0, 56,5,0,0, 56,6,0,0, 56,7,0,0, 56,8,0,0, 56,9,0,0, 56,10,0,0, 56,11,0,0, 56,12,0,0, 56,13,0,0, 56,14,0,0, 56,15,0,0, 56,16,0,0, 56,17,0,0, 56,18,0,0, 56,19,0,0, 56,20,0,0, 56,21,0,0, 56,22,0,0, 56,23,0,0, 56,24,0,0, 56,25,0,0, 56,26,0,0, 56,27,0,0, 56,28,0,0, 56,29,0,0, 56,30,0,0, 56,31,0,0, 56,32,0,0, 56,33,0,0, 56,34,0,0, 56,35,0,0, ],36,44,0,1,60,35,3,1),
	).to_cnf()
Net8_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet8,Edge,Edge_Net,[48,0,0, 48,1,0, 48,2,0, 48,3,0, 48,4,0, 48,5,0, 48,6,0, 48,7,0, 48,8,0, 48,9,0, 48,10,0, 48,11,0, 48,12,0, 48,13,0, 48,14,0, 48,15,0, 48,16,0, 48,17,0, 48,18,0, 48,19,0, 48,20,0, 48,21,0, 48,22,0, 48,23,0, 48,24,0, 48,25,0, 48,26,0, 48,27,0, 48,28,0, 48,29,0, 48,30,0, 48,31,0, 48,32,0, 48,33,0, 48,34,0, 48,35,0, 56,0,0, 56,1,0, 56,2,0, 56,3,0, 56,4,0, 56,5,0, 56,6,0, 56,7,0, 56,8,0, 56,9,0, 56,10,0, 56,11,0, 56,12,0, 56,13,0, 56,14,0, 56,15,0, 56,16,0, 56,17,0, 56,18,0, 56,19,0, 56,20,0, 56,21,0, 56,22,0, 56,23,0, 56,24,0, 56,25,0, 56,26,0, 56,27,0, 56,28,0, 56,29,0, 56,30,0, 56,31,0, 56,32,0, 56,33,0, 56,34,0, 56,35,0, ],72,44,0,0,60,35,3,1,7),
	)
Net8_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,7],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,6+1)])for x in range(44,60+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,7],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(8,5+1)])for x in range(44,60+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net8_Subnet1_R = And(Net8_Subnet1_R1,Net8_Subnet1_R2,Net8_Subnet1_R3,)
Net8_Subnet1_Formula = And(Net8_Subnet1_C,Net8_Subnet1_DR,Net8_Subnet1_R)
# Net = 8 Subnet = 3 | Left -> Right [52,68] Top -> Bottom [0,35]
# Range R1(56,56,0,35)
# Range R2(64,64,0,35)
### Disable edges outside window
Edge_Net_Subnet8[0:52,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(67392)
Edge_Net_Subnet8[68:85+1,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(23328)

### Consistency Constraints
Net8_Subnet3_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,7]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(52,68+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net8_Subnet3_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet8[x,y,z,trend,mask,3]), Edge_Net[x,y,z,trend,mask,7])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(52,68+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net8_Subnet3_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet8[x,y,2,trend,0,3],Xor(Edge_Net_Subnet8[x,y,2,trend,1,3],Edge_Net_Subnet8[x,y,2,trend,2,3])),And(~Edge_Net_Subnet8[x,y,2,trend,0,3],~Edge_Net_Subnet8[x,y,2,trend,1,3],~Edge_Net_Subnet8[x,y,2,trend,2,3]))for x in range(52,68+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net8_Subnet3_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet8[x,y,3,1,0,3],Xor(Edge_Net_Subnet8[x,y,3,1,1,3],Edge_Net_Subnet8[x,y,3,1,2,3])),And(~Edge_Net_Subnet8[x,y,3,1,0,3],~Edge_Net_Subnet8[x,y,3,1,1,3],~Edge_Net_Subnet8[x,y,3,1,2,3]))for x in range(52,68+1)])for y in range(0,35+1)]).to_cnf()
Net8_Subnet3_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet8[x,y,1,trend,2,3],Xor(Edge_Net_Subnet8[x,y,1,trend,0,3],Edge_Net_Subnet8[x,y,1,trend,1,3])),And(~Edge_Net_Subnet8[x,y,1,trend,2,3],~Edge_Net_Subnet8[x,y,1,trend,0,3],~Edge_Net_Subnet8[x,y,1,trend,1,3]))for x in range(52,68+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net8_Subnet3_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,2,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(52,68+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,2,s2])for s2 in range(3+1,5)]))for trend in range(0,1+1)])for x in range(52,68+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,1,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(52,68+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,1,s2])for s2 in range(3+1,5)]))for trend in range(0,1+1)])for x in range(52,68+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net8_Subnet3_C = And(Net8_Subnet3_C1, Net8_Subnet3_C2,Net8_Subnet3_C3_ME1_Mask,Net8_Subnet3_C4_MINT1_Mask,Net8_Subnet3_C5_AIL2GIL_Mask,Net8_Subnet3_C6,)
### Design Rules
Net8_Subnet3_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(52,68+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net8_Subnet3_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,1,1,1,3], ~Edge_Net_Subnet8[x-1,y,1,1,1,3]), And(Edge_Net_Subnet8[x+1,y,1,1,1,3], Edge_Net_Subnet8[x+2,y,1,1,1,3], Edge_Net_Subnet8[x+3,y,1,1,1,3], ))for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,1,1,1,3], ~Edge_Net_Subnet8[x+1,y,1,1,1,3]), And(Edge_Net_Subnet8[x-1,y,1,1,1,3], Edge_Net_Subnet8[x-2,y,1,1,1,3], Edge_Net_Subnet8[x-3,y,1,1,1,3], ))for x in range(52,68+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet3_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,1,1,3], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,1,1,3], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(52,68+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet3_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,1,1,3], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(52,68+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,1,1,3], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(52,68+1)])for y in range(3,35+1)]),
	).to_cnf()
Net8_Subnet3_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,3]), And(Edge_Net_Subnet8[x,y+1,1,0,0,3], Edge_Net_Subnet8[x,y+2,1,0,0,3], Edge_Net_Subnet8[x,y+3,1,0,0,3], ))for x in range(52,68+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,3]), And(Edge_Net_Subnet8[x,y-1,1,0,0,3], Edge_Net_Subnet8[x,y-2,1,0,0,3], Edge_Net_Subnet8[x,y-3,1,0,0,3], ))for x in range(52,68+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,3], ~Edge_Net_Subnet8[x,y-1,1,0,0,3]), And(Edge_Net_Subnet8[x,y+1,1,0,0,3], Edge_Net_Subnet8[x,y+2,1,0,0,3], Edge_Net_Subnet8[x,y+3,1,0,0,3], ))for x in range(52,68+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,3], ~Edge_Net_Subnet8[x,y+1,1,0,0,3]), And(Edge_Net_Subnet8[x,y-1,1,0,0,3], Edge_Net_Subnet8[x,y-2,1,0,0,3], Edge_Net_Subnet8[x,y-3,1,0,0,3], ))for x in range(52,68+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net8_Subnet3_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(52,68+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(52,68+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(52,68+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(52,68+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(52,68+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(52,68+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net8_Subnet3_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,0,0,3], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,0,0,3], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(52,68+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet3_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,3,1,mask,3], ~Edge_Net_Subnet8[x-1,y,3,1,mask,3]), And(Edge_Net_Subnet8[x+1,y,3,1,mask,3], Edge_Net_Subnet8[x+2,y,3,1,mask,3], Edge_Net_Subnet8[x+3,y,3,1,mask,3], Edge_Net_Subnet8[x+4,y,3,1,mask,3], Edge_Net_Subnet8[x+5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,3,1,mask,3], ~Edge_Net_Subnet8[x+1,y,3,1,mask,3]), And(Edge_Net_Subnet8[x-1,y,3,1,mask,3], Edge_Net_Subnet8[x-2,y,3,1,mask,3], Edge_Net_Subnet8[x-3,y,3,1,mask,3], Edge_Net_Subnet8[x-4,y,3,1,mask,3], Edge_Net_Subnet8[x-5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet3_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,mask,3], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,mask,3], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(3,35+1)]),
	).to_cnf()
Net8_Subnet3_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,mask,3], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,mask,3], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet3_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,1,3], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(52,68+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,1,3], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(52,68+1)])for y in range(2,35+1)]),
	).to_cnf()
Net8_Subnet3_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,1,3], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,1,3], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(52,68+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet3_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,2,1,mask,3], ~Edge_Net_Subnet8[x-1,y,2,1,mask,3]), And(Edge_Net_Subnet8[x+1,y,2,1,mask,3], Edge_Net_Subnet8[x+2,y,2,1,mask,3], Edge_Net_Subnet8[x+3,y,2,1,mask,3], Edge_Net_Subnet8[x+4,y,2,1,mask,3], Edge_Net_Subnet8[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,2,1,mask,3], ~Edge_Net_Subnet8[x+1,y,2,1,mask,3]), And(Edge_Net_Subnet8[x-1,y,2,1,mask,3], Edge_Net_Subnet8[x-2,y,2,1,mask,3], Edge_Net_Subnet8[x-3,y,2,1,mask,3], Edge_Net_Subnet8[x-4,y,2,1,mask,3], Edge_Net_Subnet8[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,3], And(Edge_Net_Subnet8[x-1,y,2,1,mask,3], Edge_Net_Subnet8[x-2,y,2,1,mask,3], Edge_Net_Subnet8[x-3,y,2,1,mask,3], Edge_Net_Subnet8[x-4,y,2,1,mask,3], Edge_Net_Subnet8[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(52,52+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,3], And(Edge_Net_Subnet8[x+1,y,2,1,mask,3], Edge_Net_Subnet8[x+2,y,2,1,mask,3], Edge_Net_Subnet8[x+3,y,2,1,mask,3], Edge_Net_Subnet8[x+4,y,2,1,mask,3], Edge_Net_Subnet8[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(68-1,52)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,3], ~Edge_Net_Subnet8[x,y-1,2,0,mask,3]), And(Edge_Net_Subnet8[x,y+1,2,0,mask,3], Edge_Net_Subnet8[x,y+2,2,0,mask,3], Edge_Net_Subnet8[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,3], ~Edge_Net_Subnet8[x,y+1,2,0,mask,3]), And(Edge_Net_Subnet8[x,y-1,2,0,mask,3], Edge_Net_Subnet8[x,y-2,2,0,mask,3], Edge_Net_Subnet8[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet8[x,y,2,0,mask,3], And(Edge_Net_Subnet8[x,y+1,2,0,mask,3], Edge_Net_Subnet8[x,y+2,2,0,mask,3], Edge_Net_Subnet8[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet8[x,y,2,0,mask,3], And(Edge_Net_Subnet8[x,y-1,2,0,mask,3], Edge_Net_Subnet8[x,y-2,2,0,mask,3], Edge_Net_Subnet8[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(35,35+1)]),
	).to_cnf()
Net8_Subnet3_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,1,3], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,1,3], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(52,68+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet3_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,mask,3], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,mask,3], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet3_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,1,3], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(52,68+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,1,3], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(52,68+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net8_Subnet3_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,3], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,3], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net8_Subnet3_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,1,3], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(52,68+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,1,3], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(52,68+1)])for y in range(3,35+1)]),
	).to_cnf()
Net8_Subnet3_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,3], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,3], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(4,35+1)]),
	).to_cnf()
Net8_Subnet3_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,1,3], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,1,3], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(52,68+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet3_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,mask,3], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,mask,3], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(52,68+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet3_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,1,2,mask,3], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,1,2,mask,3], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(52,68+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet3_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,2,2,mask,3], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(52,68+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,2,2,mask,3], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(52,68+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet3_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,2,mask,3], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(52,68+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,2,mask,3], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(52,68+1)])for y in range(2,35+1)]),
	).to_cnf()
Net8_Subnet3_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,2,mask,3], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(52,68+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,2,mask,3], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(52,68+1)])for y in range(2,35+1)]),
	).to_cnf()
Net8_Subnet3_DR = And(Net8_Subnet3_DR_Trend, Net8_Subnet3_DR_GIL_HorMinWidth,Net8_Subnet3_DR_GIL_HorMinSpacing,Net8_Subnet3_DR_GIL_VerMinSpacing,Net8_Subnet3_DR_AIL2_VerMinWidth,Net8_Subnet3_DR_AIL2_VerMinSpacing,Net8_Subnet3_DR_VerAIL2_HorMinSpacing,Net8_Subnet3_DR_MINT1AB_HorMinWidth,Net8_Subnet3_DR_MINT1_SameMask_VerMinSpacing,Net8_Subnet3_DR_MINT1_SameMask_HorMinSpacing,Net8_Subnet3_DR_MINT1_DiffMask_VerMinSpacing,Net8_Subnet3_DR_MINT1_DiffMask_HorMinSpacing,Net8_Subnet3_DR_M1AB_MinWidth,Net8_Subnet3_DR_HorM1_DiffMask_HorMinSpacing,Net8_Subnet3_DR_HorM1_SameMask_HorMinSpacing,Net8_Subnet3_DR_VerM1_DiffMask_VerMinSpacing,Net8_Subnet3_DR_VerM1_SameMask_VerMinSpacing,Net8_Subnet3_DR_HorM1_DiffMask_VerMinSpacing,Net8_Subnet3_DR_HorM1_SameMask_VerMinSpacing,Net8_Subnet3_DR_VerM1_DiffMask_HorMinSpacing,Net8_Subnet3_DR_VerM1_SameMask_HorMinSpacing,Net8_Subnet3_DR_V0_HorMinSpacing,Net8_Subnet3_DR_V1_HorMinSpacing,Net8_Subnet3_DR_V0_VerMinSpacing,Net8_Subnet3_DR_V1_VerMinSpacing,)
### Routability Constraints
Net8_Subnet3_R1 = And(
	RConstraints.R1(Edge_Net_Subnet8,[56,0,0,0, 56,1,0,0, 56,2,0,0, 56,3,0,0, 56,4,0,0, 56,5,0,0, 56,6,0,0, 56,7,0,0, 56,8,0,0, 56,9,0,0, 56,10,0,0, 56,11,0,0, 56,12,0,0, 56,13,0,0, 56,14,0,0, 56,15,0,0, 56,16,0,0, 56,17,0,0, 56,18,0,0, 56,19,0,0, 56,20,0,0, 56,21,0,0, 56,22,0,0, 56,23,0,0, 56,24,0,0, 56,25,0,0, 56,26,0,0, 56,27,0,0, 56,28,0,0, 56,29,0,0, 56,30,0,0, 56,31,0,0, 56,32,0,0, 56,33,0,0, 56,34,0,0, 56,35,0,0, ],36,52,0,1,68,35,3,3),
	RConstraints.R1(Edge_Net_Subnet8,[64,0,0,0, 64,1,0,0, 64,2,0,0, 64,3,0,0, 64,4,0,0, 64,5,0,0, 64,6,0,0, 64,7,0,0, 64,8,0,0, 64,9,0,0, 64,10,0,0, 64,11,0,0, 64,12,0,0, 64,13,0,0, 64,14,0,0, 64,15,0,0, 64,16,0,0, 64,17,0,0, 64,18,0,0, 64,19,0,0, 64,20,0,0, 64,21,0,0, 64,22,0,0, 64,23,0,0, 64,24,0,0, 64,25,0,0, 64,26,0,0, 64,27,0,0, 64,28,0,0, 64,29,0,0, 64,30,0,0, 64,31,0,0, 64,32,0,0, 64,33,0,0, 64,34,0,0, 64,35,0,0, ],36,52,0,1,68,35,3,3),
	).to_cnf()
Net8_Subnet3_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet8,Edge,Edge_Net,[56,0,0, 56,1,0, 56,2,0, 56,3,0, 56,4,0, 56,5,0, 56,6,0, 56,7,0, 56,8,0, 56,9,0, 56,10,0, 56,11,0, 56,12,0, 56,13,0, 56,14,0, 56,15,0, 56,16,0, 56,17,0, 56,18,0, 56,19,0, 56,20,0, 56,21,0, 56,22,0, 56,23,0, 56,24,0, 56,25,0, 56,26,0, 56,27,0, 56,28,0, 56,29,0, 56,30,0, 56,31,0, 56,32,0, 56,33,0, 56,34,0, 56,35,0, 64,0,0, 64,1,0, 64,2,0, 64,3,0, 64,4,0, 64,5,0, 64,6,0, 64,7,0, 64,8,0, 64,9,0, 64,10,0, 64,11,0, 64,12,0, 64,13,0, 64,14,0, 64,15,0, 64,16,0, 64,17,0, 64,18,0, 64,19,0, 64,20,0, 64,21,0, 64,22,0, 64,23,0, 64,24,0, 64,25,0, 64,26,0, 64,27,0, 64,28,0, 64,29,0, 64,30,0, 64,31,0, 64,32,0, 64,33,0, 64,34,0, 64,35,0, ],72,52,0,0,68,35,3,3,7),
	)
Net8_Subnet3_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,7],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,6+1)])for x in range(52,68+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,7],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(8,5+1)])for x in range(52,68+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net8_Subnet3_R = And(Net8_Subnet3_R1,Net8_Subnet3_R2,Net8_Subnet3_R3,)
Net8_Subnet3_Formula = And(Net8_Subnet3_C,Net8_Subnet3_DR,Net8_Subnet3_R)
FORMULA = And(Net1_Subnet0_Formula, Net1_Subnet1_Formula, Net1_Subnet2_Formula, Net1_Subnet3_Formula, Net1_Subnet4_Formula, Net1_Subnet5_Formula, Net1_Subnet6_Formula, Net2_Subnet0_Formula, Net2_Subnet1_Formula, Net2_Subnet2_Formula, Net2_Subnet3_Formula, Net2_Subnet4_Formula, Net2_Subnet5_Formula, Net2_Subnet6_Formula, Net2_Subnet7_Formula, Net2_Subnet8_Formula, Net2_Subnet9_Formula, Net4_Subnet1_Formula, Net5_Subnet0_Formula, Net5_Subnet1_Formula, Net3_Subnet0_Formula, Net3_Subnet1_Formula, Net3_Subnet2_Formula, Net3_Subnet3_Formula, Net3_Subnet4_Formula, Net3_Subnet5_Formula, Net3_Subnet6_Formula, Net3_Subnet7_Formula, Net3_Subnet8_Formula, Net3_Subnet9_Formula, Net8_Subnet1_Formula, Net8_Subnet3_Formula, )
endTime = time.time()
print('Total Time = ', endTime-startTime)
setOut.clauseDistribution(FORMULA)
setOut.setUpLayoutViaFromResult(FORMULA.satisfy_one(),outLayout,subnetRec,6)
print('#edge = 32725')