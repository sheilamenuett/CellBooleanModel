from pyeda.inter import *
import RConstraints
import time
import setOut
startTime = time.time()
# ===> Instruction(Create)  2D Routing Style p(e) <===
# ===> Edges[X, Y, Z, Trends, Masks]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge = exprvars('edge', 78, 36, 4, 3, 3)

# ===> Instruction(Create)  2D Routing Style p(e,n) <===
# ===> Edge_Net[X, Y, Z, Trends, Masks, Nets]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge_Net = exprvars('edge_net', 78, 36, 4, 3, 3, 13)

# ===> Instruction(Create)  2D Routing Style p(e,n,s) <===
# ===> Edge_Net_Subnet_NetID[X, Y, Z, Trends, Masks, Subnets]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge_Net_Subnet9 = exprvars('edge_net_subnet9', 78, 36, 4, 3, 3, 1)
Edge_Net_Subnet11 = exprvars('edge_net_subnet11', 78, 36, 4, 3, 3, 1)
Edge_Net_Subnet12 = exprvars('edge_net_subnet12', 78, 36, 4, 3, 3, 1)
Edge_Net_Subnet1 = exprvars('edge_net_subnet1', 78, 36, 4, 3, 3, 1)
Edge_Net_Subnet3 = exprvars('edge_net_subnet3', 78, 36, 4, 3, 3, 3)
Edge_Net_Subnet2 = exprvars('edge_net_subnet2', 78, 36, 4, 3, 3, 5)
Edge_Net_Subnet4 = exprvars('edge_net_subnet4', 78, 36, 4, 3, 3, 3)
Edge_Net_Subnet5 = exprvars('edge_net_subnet5', 78, 36, 4, 3, 3, 3)
Edge_Net_Subnet6 = exprvars('edge_net_subnet6', 78, 36, 4, 3, 3, 7)
Edge_Net_Subnet8 = exprvars('edge_net_subnet8', 78, 36, 4, 3, 3, 3)
Edge_Net_Subnet7 = exprvars('edge_net_subnet7', 78, 36, 4, 3, 3, 5)

outLayout=[[[[0 for trend in range(3)] for z in range(4)] for y in range(36)] for x in range(78)]

subnetRec=[[[[0 for trend in range(3)] for z in range(4)] for y in range(36)] for x in range(78)]

MaxX = 77
MaxY = 35
MaxZ = 3
#Net = 13
#cellName = DFFRNQ_X1_DFINH_combined
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
Edge_Net[0,0,0,0,0,0:] = exprzeros(13)
Edge_Net[0,1,0,0,0,0:] = exprzeros(13)
Edge_Net[0,2,0,0,0,0:] = exprzeros(13)
Edge_Net[0,3,0,0,0,0:] = exprzeros(13)
Edge_Net[0,4,0,0,0,0:] = exprzeros(13)
Edge_Net[0,5,0,0,0,0:] = exprzeros(13)
Edge_Net[0,6,0,0,0,0:] = exprzeros(13)
Edge_Net[0,7,0,0,0,0:] = exprzeros(13)
Edge_Net[0,8,0,0,0,0:] = exprzeros(13)
Edge_Net[0,9,0,0,0,0:] = exprzeros(13)
Edge_Net[0,10,0,0,0,0:] = exprzeros(13)
Edge_Net[0,11,0,0,0,0:] = exprzeros(13)
Edge_Net[0,12,0,0,0,0:] = exprzeros(13)
Edge_Net[0,13,0,0,0,0:] = exprzeros(13)
Edge_Net[0,14,0,0,0,0:] = exprzeros(13)
Edge_Net[0,15,0,0,0,0:] = exprzeros(13)
Edge_Net[0,16,0,0,0,0:] = exprzeros(13)
Edge_Net[0,17,0,0,0,0:] = exprzeros(13)
Edge_Net[0,18,0,0,0,0:] = exprzeros(13)
Edge_Net[0,19,0,0,0,0:] = exprzeros(13)
Edge_Net[0,20,0,0,0,0:] = exprzeros(13)
Edge_Net[0,21,0,0,0,0:] = exprzeros(13)
Edge_Net[0,22,0,0,0,0:] = exprzeros(13)
Edge_Net[0,23,0,0,0,0:] = exprzeros(13)
Edge_Net[0,24,0,0,0,0:] = exprzeros(13)
Edge_Net[0,25,0,0,0,0:] = exprzeros(13)
Edge_Net[0,26,0,0,0,0:] = exprzeros(13)
Edge_Net[0,27,0,0,0,0:] = exprzeros(13)
Edge_Net[0,28,0,0,0,0:] = exprzeros(13)
Edge_Net[0,29,0,0,0,0:] = exprzeros(13)
Edge_Net[0,30,0,0,0,0:] = exprzeros(13)
Edge_Net[0,31,0,0,0,0:] = exprzeros(13)
Edge_Net[0,32,0,0,0,0:] = exprzeros(13)
Edge_Net[0,33,0,0,0,0:] = exprzeros(13)
Edge_Net[0,34,0,0,0,0:] = exprzeros(13)
Edge_Net[0,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[4,0,0,0,0,0:] = exprzeros(13)
Edge_Net[4,1,0,0,0,0:] = exprzeros(13)
Edge_Net[4,2,0,0,0,0:] = exprzeros(13)
Edge_Net[4,3,0,0,0,0:] = exprzeros(13)
Edge_Net[4,4,0,0,0,0:] = exprzeros(13)
Edge_Net[4,5,0,0,0,0:] = exprzeros(13)
Edge_Net[4,6,0,0,0,0:] = exprzeros(13)
Edge_Net[4,7,0,0,0,0:] = exprzeros(13)
Edge_Net[4,8,0,0,0,0:] = exprzeros(13)
Edge_Net[4,9,0,0,0,0:] = exprzeros(13)
Edge_Net[4,10,0,0,0,0:] = exprzeros(13)
Edge_Net[4,11,0,0,0,0:] = exprzeros(13)
Edge_Net[4,12,0,0,0,0:] = exprzeros(13)
Edge_Net[4,13,0,0,0,0:] = exprzeros(13)
Edge_Net[4,14,0,0,0,0:] = exprzeros(13)
Edge_Net[4,15,0,0,0,0:] = exprzeros(13)
Edge_Net[4,16,0,0,0,0:] = exprzeros(13)
Edge_Net[4,17,0,0,0,0:] = exprzeros(13)
Edge_Net[4,18,0,0,0,0:] = exprzeros(13)
Edge_Net[4,19,0,0,0,0:] = exprzeros(13)
Edge_Net[4,20,0,0,0,0:] = exprzeros(13)
Edge_Net[4,21,0,0,0,0:] = exprzeros(13)
Edge_Net[4,22,0,0,0,0:] = exprzeros(13)
Edge_Net[4,23,0,0,0,0:] = exprzeros(13)
Edge_Net[4,24,0,0,0,0:] = exprzeros(13)
Edge_Net[4,25,0,0,0,0:] = exprzeros(13)
Edge_Net[4,26,0,0,0,0:] = exprzeros(13)
Edge_Net[4,27,0,0,0,0:] = exprzeros(13)
Edge_Net[4,28,0,0,0,0:] = exprzeros(13)
Edge_Net[4,29,0,0,0,0:] = exprzeros(13)
Edge_Net[4,30,0,0,0,0:] = exprzeros(13)
Edge_Net[4,31,0,0,0,0:] = exprzeros(13)
Edge_Net[4,32,0,0,0,0:] = exprzeros(13)
Edge_Net[4,33,0,0,0,0:] = exprzeros(13)
Edge_Net[4,34,0,0,0,0:] = exprzeros(13)
Edge_Net[4,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[8,0,0,0,0,0:] = exprzeros(13)
Edge_Net[8,1,0,0,0,0:] = exprzeros(13)
Edge_Net[8,2,0,0,0,0:] = exprzeros(13)
Edge_Net[8,3,0,0,0,0:] = exprzeros(13)
Edge_Net[8,4,0,0,0,0:] = exprzeros(13)
Edge_Net[8,5,0,0,0,0:] = exprzeros(13)
Edge_Net[8,6,0,0,0,0:] = exprzeros(13)
Edge_Net[8,7,0,0,0,0:] = exprzeros(13)
Edge_Net[8,8,0,0,0,0:] = exprzeros(13)
Edge_Net[8,9,0,0,0,0:] = exprzeros(13)
Edge_Net[8,10,0,0,0,0:] = exprzeros(13)
Edge_Net[8,11,0,0,0,0:] = exprzeros(13)
Edge_Net[8,12,0,0,0,0:] = exprzeros(13)
Edge_Net[8,13,0,0,0,0:] = exprzeros(13)
Edge_Net[8,14,0,0,0,0:] = exprzeros(13)
Edge_Net[8,15,0,0,0,0:] = exprzeros(13)
Edge_Net[8,16,0,0,0,0:] = exprzeros(13)
Edge_Net[8,17,0,0,0,0:] = exprzeros(13)
Edge_Net[8,18,0,0,0,0:] = exprzeros(13)
Edge_Net[8,19,0,0,0,0:] = exprzeros(13)
Edge_Net[8,20,0,0,0,0:] = exprzeros(13)
Edge_Net[8,21,0,0,0,0:] = exprzeros(13)
Edge_Net[8,22,0,0,0,0:] = exprzeros(13)
Edge_Net[8,23,0,0,0,0:] = exprzeros(13)
Edge_Net[8,24,0,0,0,0:] = exprzeros(13)
Edge_Net[8,25,0,0,0,0:] = exprzeros(13)
Edge_Net[8,26,0,0,0,0:] = exprzeros(13)
Edge_Net[8,27,0,0,0,0:] = exprzeros(13)
Edge_Net[8,28,0,0,0,0:] = exprzeros(13)
Edge_Net[8,29,0,0,0,0:] = exprzeros(13)
Edge_Net[8,30,0,0,0,0:] = exprzeros(13)
Edge_Net[8,31,0,0,0,0:] = exprzeros(13)
Edge_Net[8,32,0,0,0,0:] = exprzeros(13)
Edge_Net[8,33,0,0,0,0:] = exprzeros(13)
Edge_Net[8,34,0,0,0,0:] = exprzeros(13)
Edge_Net[8,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[12,0,0,0,0,0:] = exprzeros(13)
Edge_Net[12,1,0,0,0,0:] = exprzeros(13)
Edge_Net[12,2,0,0,0,0:] = exprzeros(13)
Edge_Net[12,3,0,0,0,0:] = exprzeros(13)
Edge_Net[12,4,0,0,0,0:] = exprzeros(13)
Edge_Net[12,5,0,0,0,0:] = exprzeros(13)
Edge_Net[12,6,0,0,0,0:] = exprzeros(13)
Edge_Net[12,7,0,0,0,0:] = exprzeros(13)
Edge_Net[12,8,0,0,0,0:] = exprzeros(13)
Edge_Net[12,9,0,0,0,0:] = exprzeros(13)
Edge_Net[12,10,0,0,0,0:] = exprzeros(13)
Edge_Net[12,11,0,0,0,0:] = exprzeros(13)
Edge_Net[12,12,0,0,0,0:] = exprzeros(13)
Edge_Net[12,13,0,0,0,0:] = exprzeros(13)
Edge_Net[12,14,0,0,0,0:] = exprzeros(13)
Edge_Net[12,15,0,0,0,0:] = exprzeros(13)
Edge_Net[12,16,0,0,0,0:] = exprzeros(13)
Edge_Net[12,17,0,0,0,0:] = exprzeros(13)
Edge_Net[12,18,0,0,0,0:] = exprzeros(13)
Edge_Net[12,19,0,0,0,0:] = exprzeros(13)
Edge_Net[12,20,0,0,0,0:] = exprzeros(13)
Edge_Net[12,21,0,0,0,0:] = exprzeros(13)
Edge_Net[12,22,0,0,0,0:] = exprzeros(13)
Edge_Net[12,23,0,0,0,0:] = exprzeros(13)
Edge_Net[12,24,0,0,0,0:] = exprzeros(13)
Edge_Net[12,25,0,0,0,0:] = exprzeros(13)
Edge_Net[12,26,0,0,0,0:] = exprzeros(13)
Edge_Net[12,27,0,0,0,0:] = exprzeros(13)
Edge_Net[12,28,0,0,0,0:] = exprzeros(13)
Edge_Net[12,29,0,0,0,0:] = exprzeros(13)
Edge_Net[12,30,0,0,0,0:] = exprzeros(13)
Edge_Net[12,31,0,0,0,0:] = exprzeros(13)
Edge_Net[12,32,0,0,0,0:] = exprzeros(13)
Edge_Net[12,33,0,0,0,0:] = exprzeros(13)
Edge_Net[12,34,0,0,0,0:] = exprzeros(13)
Edge_Net[12,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[16,0,0,0,0,0:] = exprzeros(13)
Edge_Net[16,1,0,0,0,0:] = exprzeros(13)
Edge_Net[16,2,0,0,0,0:] = exprzeros(13)
Edge_Net[16,3,0,0,0,0:] = exprzeros(13)
Edge_Net[16,4,0,0,0,0:] = exprzeros(13)
Edge_Net[16,5,0,0,0,0:] = exprzeros(13)
Edge_Net[16,6,0,0,0,0:] = exprzeros(13)
Edge_Net[16,7,0,0,0,0:] = exprzeros(13)
Edge_Net[16,8,0,0,0,0:] = exprzeros(13)
Edge_Net[16,9,0,0,0,0:] = exprzeros(13)
Edge_Net[16,10,0,0,0,0:] = exprzeros(13)
Edge_Net[16,11,0,0,0,0:] = exprzeros(13)
Edge_Net[16,12,0,0,0,0:] = exprzeros(13)
Edge_Net[16,13,0,0,0,0:] = exprzeros(13)
Edge_Net[16,14,0,0,0,0:] = exprzeros(13)
Edge_Net[16,15,0,0,0,0:] = exprzeros(13)
Edge_Net[16,16,0,0,0,0:] = exprzeros(13)
Edge_Net[16,17,0,0,0,0:] = exprzeros(13)
Edge_Net[16,18,0,0,0,0:] = exprzeros(13)
Edge_Net[16,19,0,0,0,0:] = exprzeros(13)
Edge_Net[16,20,0,0,0,0:] = exprzeros(13)
Edge_Net[16,21,0,0,0,0:] = exprzeros(13)
Edge_Net[16,22,0,0,0,0:] = exprzeros(13)
Edge_Net[16,23,0,0,0,0:] = exprzeros(13)
Edge_Net[16,24,0,0,0,0:] = exprzeros(13)
Edge_Net[16,25,0,0,0,0:] = exprzeros(13)
Edge_Net[16,26,0,0,0,0:] = exprzeros(13)
Edge_Net[16,27,0,0,0,0:] = exprzeros(13)
Edge_Net[16,28,0,0,0,0:] = exprzeros(13)
Edge_Net[16,29,0,0,0,0:] = exprzeros(13)
Edge_Net[16,30,0,0,0,0:] = exprzeros(13)
Edge_Net[16,31,0,0,0,0:] = exprzeros(13)
Edge_Net[16,32,0,0,0,0:] = exprzeros(13)
Edge_Net[16,33,0,0,0,0:] = exprzeros(13)
Edge_Net[16,34,0,0,0,0:] = exprzeros(13)
Edge_Net[16,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[20,0,0,0,0,0:] = exprzeros(13)
Edge_Net[20,1,0,0,0,0:] = exprzeros(13)
Edge_Net[20,2,0,0,0,0:] = exprzeros(13)
Edge_Net[20,3,0,0,0,0:] = exprzeros(13)
Edge_Net[20,4,0,0,0,0:] = exprzeros(13)
Edge_Net[20,5,0,0,0,0:] = exprzeros(13)
Edge_Net[20,6,0,0,0,0:] = exprzeros(13)
Edge_Net[20,7,0,0,0,0:] = exprzeros(13)
Edge_Net[20,8,0,0,0,0:] = exprzeros(13)
Edge_Net[20,9,0,0,0,0:] = exprzeros(13)
Edge_Net[20,10,0,0,0,0:] = exprzeros(13)
Edge_Net[20,11,0,0,0,0:] = exprzeros(13)
Edge_Net[20,12,0,0,0,0:] = exprzeros(13)
Edge_Net[20,13,0,0,0,0:] = exprzeros(13)
Edge_Net[20,14,0,0,0,0:] = exprzeros(13)
Edge_Net[20,15,0,0,0,0:] = exprzeros(13)
Edge_Net[20,16,0,0,0,0:] = exprzeros(13)
Edge_Net[20,17,0,0,0,0:] = exprzeros(13)
Edge_Net[20,18,0,0,0,0:] = exprzeros(13)
Edge_Net[20,19,0,0,0,0:] = exprzeros(13)
Edge_Net[20,20,0,0,0,0:] = exprzeros(13)
Edge_Net[20,21,0,0,0,0:] = exprzeros(13)
Edge_Net[20,22,0,0,0,0:] = exprzeros(13)
Edge_Net[20,23,0,0,0,0:] = exprzeros(13)
Edge_Net[20,24,0,0,0,0:] = exprzeros(13)
Edge_Net[20,25,0,0,0,0:] = exprzeros(13)
Edge_Net[20,26,0,0,0,0:] = exprzeros(13)
Edge_Net[20,27,0,0,0,0:] = exprzeros(13)
Edge_Net[20,28,0,0,0,0:] = exprzeros(13)
Edge_Net[20,29,0,0,0,0:] = exprzeros(13)
Edge_Net[20,30,0,0,0,0:] = exprzeros(13)
Edge_Net[20,31,0,0,0,0:] = exprzeros(13)
Edge_Net[20,32,0,0,0,0:] = exprzeros(13)
Edge_Net[20,33,0,0,0,0:] = exprzeros(13)
Edge_Net[20,34,0,0,0,0:] = exprzeros(13)
Edge_Net[20,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[24,0,0,0,0,0:] = exprzeros(13)
Edge_Net[24,1,0,0,0,0:] = exprzeros(13)
Edge_Net[24,2,0,0,0,0:] = exprzeros(13)
Edge_Net[24,3,0,0,0,0:] = exprzeros(13)
Edge_Net[24,4,0,0,0,0:] = exprzeros(13)
Edge_Net[24,5,0,0,0,0:] = exprzeros(13)
Edge_Net[24,6,0,0,0,0:] = exprzeros(13)
Edge_Net[24,7,0,0,0,0:] = exprzeros(13)
Edge_Net[24,8,0,0,0,0:] = exprzeros(13)
Edge_Net[24,9,0,0,0,0:] = exprzeros(13)
Edge_Net[24,10,0,0,0,0:] = exprzeros(13)
Edge_Net[24,11,0,0,0,0:] = exprzeros(13)
Edge_Net[24,12,0,0,0,0:] = exprzeros(13)
Edge_Net[24,13,0,0,0,0:] = exprzeros(13)
Edge_Net[24,14,0,0,0,0:] = exprzeros(13)
Edge_Net[24,15,0,0,0,0:] = exprzeros(13)
Edge_Net[24,16,0,0,0,0:] = exprzeros(13)
Edge_Net[24,17,0,0,0,0:] = exprzeros(13)
Edge_Net[24,18,0,0,0,0:] = exprzeros(13)
Edge_Net[24,19,0,0,0,0:] = exprzeros(13)
Edge_Net[24,20,0,0,0,0:] = exprzeros(13)
Edge_Net[24,21,0,0,0,0:] = exprzeros(13)
Edge_Net[24,22,0,0,0,0:] = exprzeros(13)
Edge_Net[24,23,0,0,0,0:] = exprzeros(13)
Edge_Net[24,24,0,0,0,0:] = exprzeros(13)
Edge_Net[24,25,0,0,0,0:] = exprzeros(13)
Edge_Net[24,26,0,0,0,0:] = exprzeros(13)
Edge_Net[24,27,0,0,0,0:] = exprzeros(13)
Edge_Net[24,28,0,0,0,0:] = exprzeros(13)
Edge_Net[24,29,0,0,0,0:] = exprzeros(13)
Edge_Net[24,30,0,0,0,0:] = exprzeros(13)
Edge_Net[24,31,0,0,0,0:] = exprzeros(13)
Edge_Net[24,32,0,0,0,0:] = exprzeros(13)
Edge_Net[24,33,0,0,0,0:] = exprzeros(13)
Edge_Net[24,34,0,0,0,0:] = exprzeros(13)
Edge_Net[24,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[28,0,0,0,0,0:] = exprzeros(13)
Edge_Net[28,1,0,0,0,0:] = exprzeros(13)
Edge_Net[28,2,0,0,0,0:] = exprzeros(13)
Edge_Net[28,3,0,0,0,0:] = exprzeros(13)
Edge_Net[28,4,0,0,0,0:] = exprzeros(13)
Edge_Net[28,5,0,0,0,0:] = exprzeros(13)
Edge_Net[28,6,0,0,0,0:] = exprzeros(13)
Edge_Net[28,7,0,0,0,0:] = exprzeros(13)
Edge_Net[28,8,0,0,0,0:] = exprzeros(13)
Edge_Net[28,9,0,0,0,0:] = exprzeros(13)
Edge_Net[28,10,0,0,0,0:] = exprzeros(13)
Edge_Net[28,11,0,0,0,0:] = exprzeros(13)
Edge_Net[28,12,0,0,0,0:] = exprzeros(13)
Edge_Net[28,13,0,0,0,0:] = exprzeros(13)
Edge_Net[28,14,0,0,0,0:] = exprzeros(13)
Edge_Net[28,15,0,0,0,0:] = exprzeros(13)
Edge_Net[28,16,0,0,0,0:] = exprzeros(13)
Edge_Net[28,17,0,0,0,0:] = exprzeros(13)
Edge_Net[28,18,0,0,0,0:] = exprzeros(13)
Edge_Net[28,19,0,0,0,0:] = exprzeros(13)
Edge_Net[28,20,0,0,0,0:] = exprzeros(13)
Edge_Net[28,21,0,0,0,0:] = exprzeros(13)
Edge_Net[28,22,0,0,0,0:] = exprzeros(13)
Edge_Net[28,23,0,0,0,0:] = exprzeros(13)
Edge_Net[28,24,0,0,0,0:] = exprzeros(13)
Edge_Net[28,25,0,0,0,0:] = exprzeros(13)
Edge_Net[28,26,0,0,0,0:] = exprzeros(13)
Edge_Net[28,27,0,0,0,0:] = exprzeros(13)
Edge_Net[28,28,0,0,0,0:] = exprzeros(13)
Edge_Net[28,29,0,0,0,0:] = exprzeros(13)
Edge_Net[28,30,0,0,0,0:] = exprzeros(13)
Edge_Net[28,31,0,0,0,0:] = exprzeros(13)
Edge_Net[28,32,0,0,0,0:] = exprzeros(13)
Edge_Net[28,33,0,0,0,0:] = exprzeros(13)
Edge_Net[28,34,0,0,0,0:] = exprzeros(13)
Edge_Net[28,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[32,0,0,0,0,0:] = exprzeros(13)
Edge_Net[32,1,0,0,0,0:] = exprzeros(13)
Edge_Net[32,2,0,0,0,0:] = exprzeros(13)
Edge_Net[32,3,0,0,0,0:] = exprzeros(13)
Edge_Net[32,4,0,0,0,0:] = exprzeros(13)
Edge_Net[32,5,0,0,0,0:] = exprzeros(13)
Edge_Net[32,6,0,0,0,0:] = exprzeros(13)
Edge_Net[32,7,0,0,0,0:] = exprzeros(13)
Edge_Net[32,8,0,0,0,0:] = exprzeros(13)
Edge_Net[32,9,0,0,0,0:] = exprzeros(13)
Edge_Net[32,10,0,0,0,0:] = exprzeros(13)
Edge_Net[32,11,0,0,0,0:] = exprzeros(13)
Edge_Net[32,12,0,0,0,0:] = exprzeros(13)
Edge_Net[32,13,0,0,0,0:] = exprzeros(13)
Edge_Net[32,14,0,0,0,0:] = exprzeros(13)
Edge_Net[32,15,0,0,0,0:] = exprzeros(13)
Edge_Net[32,16,0,0,0,0:] = exprzeros(13)
Edge_Net[32,17,0,0,0,0:] = exprzeros(13)
Edge_Net[32,18,0,0,0,0:] = exprzeros(13)
Edge_Net[32,19,0,0,0,0:] = exprzeros(13)
Edge_Net[32,20,0,0,0,0:] = exprzeros(13)
Edge_Net[32,21,0,0,0,0:] = exprzeros(13)
Edge_Net[32,22,0,0,0,0:] = exprzeros(13)
Edge_Net[32,23,0,0,0,0:] = exprzeros(13)
Edge_Net[32,24,0,0,0,0:] = exprzeros(13)
Edge_Net[32,25,0,0,0,0:] = exprzeros(13)
Edge_Net[32,26,0,0,0,0:] = exprzeros(13)
Edge_Net[32,27,0,0,0,0:] = exprzeros(13)
Edge_Net[32,28,0,0,0,0:] = exprzeros(13)
Edge_Net[32,29,0,0,0,0:] = exprzeros(13)
Edge_Net[32,30,0,0,0,0:] = exprzeros(13)
Edge_Net[32,31,0,0,0,0:] = exprzeros(13)
Edge_Net[32,32,0,0,0,0:] = exprzeros(13)
Edge_Net[32,33,0,0,0,0:] = exprzeros(13)
Edge_Net[32,34,0,0,0,0:] = exprzeros(13)
Edge_Net[32,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[36,0,0,0,0,0:] = exprzeros(13)
Edge_Net[36,1,0,0,0,0:] = exprzeros(13)
Edge_Net[36,2,0,0,0,0:] = exprzeros(13)
Edge_Net[36,3,0,0,0,0:] = exprzeros(13)
Edge_Net[36,4,0,0,0,0:] = exprzeros(13)
Edge_Net[36,5,0,0,0,0:] = exprzeros(13)
Edge_Net[36,6,0,0,0,0:] = exprzeros(13)
Edge_Net[36,7,0,0,0,0:] = exprzeros(13)
Edge_Net[36,8,0,0,0,0:] = exprzeros(13)
Edge_Net[36,9,0,0,0,0:] = exprzeros(13)
Edge_Net[36,10,0,0,0,0:] = exprzeros(13)
Edge_Net[36,11,0,0,0,0:] = exprzeros(13)
Edge_Net[36,12,0,0,0,0:] = exprzeros(13)
Edge_Net[36,13,0,0,0,0:] = exprzeros(13)
Edge_Net[36,14,0,0,0,0:] = exprzeros(13)
Edge_Net[36,15,0,0,0,0:] = exprzeros(13)
Edge_Net[36,16,0,0,0,0:] = exprzeros(13)
Edge_Net[36,17,0,0,0,0:] = exprzeros(13)
Edge_Net[36,18,0,0,0,0:] = exprzeros(13)
Edge_Net[36,19,0,0,0,0:] = exprzeros(13)
Edge_Net[36,20,0,0,0,0:] = exprzeros(13)
Edge_Net[36,21,0,0,0,0:] = exprzeros(13)
Edge_Net[36,22,0,0,0,0:] = exprzeros(13)
Edge_Net[36,23,0,0,0,0:] = exprzeros(13)
Edge_Net[36,24,0,0,0,0:] = exprzeros(13)
Edge_Net[36,25,0,0,0,0:] = exprzeros(13)
Edge_Net[36,26,0,0,0,0:] = exprzeros(13)
Edge_Net[36,27,0,0,0,0:] = exprzeros(13)
Edge_Net[36,28,0,0,0,0:] = exprzeros(13)
Edge_Net[36,29,0,0,0,0:] = exprzeros(13)
Edge_Net[36,30,0,0,0,0:] = exprzeros(13)
Edge_Net[36,31,0,0,0,0:] = exprzeros(13)
Edge_Net[36,32,0,0,0,0:] = exprzeros(13)
Edge_Net[36,33,0,0,0,0:] = exprzeros(13)
Edge_Net[36,34,0,0,0,0:] = exprzeros(13)
Edge_Net[36,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[40,0,0,0,0,0:] = exprzeros(13)
Edge_Net[40,1,0,0,0,0:] = exprzeros(13)
Edge_Net[40,2,0,0,0,0:] = exprzeros(13)
Edge_Net[40,3,0,0,0,0:] = exprzeros(13)
Edge_Net[40,4,0,0,0,0:] = exprzeros(13)
Edge_Net[40,5,0,0,0,0:] = exprzeros(13)
Edge_Net[40,6,0,0,0,0:] = exprzeros(13)
Edge_Net[40,7,0,0,0,0:] = exprzeros(13)
Edge_Net[40,8,0,0,0,0:] = exprzeros(13)
Edge_Net[40,9,0,0,0,0:] = exprzeros(13)
Edge_Net[40,10,0,0,0,0:] = exprzeros(13)
Edge_Net[40,11,0,0,0,0:] = exprzeros(13)
Edge_Net[40,12,0,0,0,0:] = exprzeros(13)
Edge_Net[40,13,0,0,0,0:] = exprzeros(13)
Edge_Net[40,14,0,0,0,0:] = exprzeros(13)
Edge_Net[40,15,0,0,0,0:] = exprzeros(13)
Edge_Net[40,16,0,0,0,0:] = exprzeros(13)
Edge_Net[40,17,0,0,0,0:] = exprzeros(13)
Edge_Net[40,18,0,0,0,0:] = exprzeros(13)
Edge_Net[40,19,0,0,0,0:] = exprzeros(13)
Edge_Net[40,20,0,0,0,0:] = exprzeros(13)
Edge_Net[40,21,0,0,0,0:] = exprzeros(13)
Edge_Net[40,22,0,0,0,0:] = exprzeros(13)
Edge_Net[40,23,0,0,0,0:] = exprzeros(13)
Edge_Net[40,24,0,0,0,0:] = exprzeros(13)
Edge_Net[40,25,0,0,0,0:] = exprzeros(13)
Edge_Net[40,26,0,0,0,0:] = exprzeros(13)
Edge_Net[40,27,0,0,0,0:] = exprzeros(13)
Edge_Net[40,28,0,0,0,0:] = exprzeros(13)
Edge_Net[40,29,0,0,0,0:] = exprzeros(13)
Edge_Net[40,30,0,0,0,0:] = exprzeros(13)
Edge_Net[40,31,0,0,0,0:] = exprzeros(13)
Edge_Net[40,32,0,0,0,0:] = exprzeros(13)
Edge_Net[40,33,0,0,0,0:] = exprzeros(13)
Edge_Net[40,34,0,0,0,0:] = exprzeros(13)
Edge_Net[40,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[44,0,0,0,0,0:] = exprzeros(13)
Edge_Net[44,1,0,0,0,0:] = exprzeros(13)
Edge_Net[44,2,0,0,0,0:] = exprzeros(13)
Edge_Net[44,3,0,0,0,0:] = exprzeros(13)
Edge_Net[44,4,0,0,0,0:] = exprzeros(13)
Edge_Net[44,5,0,0,0,0:] = exprzeros(13)
Edge_Net[44,6,0,0,0,0:] = exprzeros(13)
Edge_Net[44,7,0,0,0,0:] = exprzeros(13)
Edge_Net[44,8,0,0,0,0:] = exprzeros(13)
Edge_Net[44,9,0,0,0,0:] = exprzeros(13)
Edge_Net[44,10,0,0,0,0:] = exprzeros(13)
Edge_Net[44,11,0,0,0,0:] = exprzeros(13)
Edge_Net[44,12,0,0,0,0:] = exprzeros(13)
Edge_Net[44,13,0,0,0,0:] = exprzeros(13)
Edge_Net[44,14,0,0,0,0:] = exprzeros(13)
Edge_Net[44,15,0,0,0,0:] = exprzeros(13)
Edge_Net[44,16,0,0,0,0:] = exprzeros(13)
Edge_Net[44,17,0,0,0,0:] = exprzeros(13)
Edge_Net[44,18,0,0,0,0:] = exprzeros(13)
Edge_Net[44,19,0,0,0,0:] = exprzeros(13)
Edge_Net[44,20,0,0,0,0:] = exprzeros(13)
Edge_Net[44,21,0,0,0,0:] = exprzeros(13)
Edge_Net[44,22,0,0,0,0:] = exprzeros(13)
Edge_Net[44,23,0,0,0,0:] = exprzeros(13)
Edge_Net[44,24,0,0,0,0:] = exprzeros(13)
Edge_Net[44,25,0,0,0,0:] = exprzeros(13)
Edge_Net[44,26,0,0,0,0:] = exprzeros(13)
Edge_Net[44,27,0,0,0,0:] = exprzeros(13)
Edge_Net[44,28,0,0,0,0:] = exprzeros(13)
Edge_Net[44,29,0,0,0,0:] = exprzeros(13)
Edge_Net[44,30,0,0,0,0:] = exprzeros(13)
Edge_Net[44,31,0,0,0,0:] = exprzeros(13)
Edge_Net[44,32,0,0,0,0:] = exprzeros(13)
Edge_Net[44,33,0,0,0,0:] = exprzeros(13)
Edge_Net[44,34,0,0,0,0:] = exprzeros(13)
Edge_Net[44,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[48,0,0,0,0,0:] = exprzeros(13)
Edge_Net[48,1,0,0,0,0:] = exprzeros(13)
Edge_Net[48,2,0,0,0,0:] = exprzeros(13)
Edge_Net[48,3,0,0,0,0:] = exprzeros(13)
Edge_Net[48,4,0,0,0,0:] = exprzeros(13)
Edge_Net[48,5,0,0,0,0:] = exprzeros(13)
Edge_Net[48,6,0,0,0,0:] = exprzeros(13)
Edge_Net[48,7,0,0,0,0:] = exprzeros(13)
Edge_Net[48,8,0,0,0,0:] = exprzeros(13)
Edge_Net[48,9,0,0,0,0:] = exprzeros(13)
Edge_Net[48,10,0,0,0,0:] = exprzeros(13)
Edge_Net[48,11,0,0,0,0:] = exprzeros(13)
Edge_Net[48,12,0,0,0,0:] = exprzeros(13)
Edge_Net[48,13,0,0,0,0:] = exprzeros(13)
Edge_Net[48,14,0,0,0,0:] = exprzeros(13)
Edge_Net[48,15,0,0,0,0:] = exprzeros(13)
Edge_Net[48,16,0,0,0,0:] = exprzeros(13)
Edge_Net[48,17,0,0,0,0:] = exprzeros(13)
Edge_Net[48,18,0,0,0,0:] = exprzeros(13)
Edge_Net[48,19,0,0,0,0:] = exprzeros(13)
Edge_Net[48,20,0,0,0,0:] = exprzeros(13)
Edge_Net[48,21,0,0,0,0:] = exprzeros(13)
Edge_Net[48,22,0,0,0,0:] = exprzeros(13)
Edge_Net[48,23,0,0,0,0:] = exprzeros(13)
Edge_Net[48,24,0,0,0,0:] = exprzeros(13)
Edge_Net[48,25,0,0,0,0:] = exprzeros(13)
Edge_Net[48,26,0,0,0,0:] = exprzeros(13)
Edge_Net[48,27,0,0,0,0:] = exprzeros(13)
Edge_Net[48,28,0,0,0,0:] = exprzeros(13)
Edge_Net[48,29,0,0,0,0:] = exprzeros(13)
Edge_Net[48,30,0,0,0,0:] = exprzeros(13)
Edge_Net[48,31,0,0,0,0:] = exprzeros(13)
Edge_Net[48,32,0,0,0,0:] = exprzeros(13)
Edge_Net[48,33,0,0,0,0:] = exprzeros(13)
Edge_Net[48,34,0,0,0,0:] = exprzeros(13)
Edge_Net[48,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[52,0,0,0,0,0:] = exprzeros(13)
Edge_Net[52,1,0,0,0,0:] = exprzeros(13)
Edge_Net[52,2,0,0,0,0:] = exprzeros(13)
Edge_Net[52,3,0,0,0,0:] = exprzeros(13)
Edge_Net[52,4,0,0,0,0:] = exprzeros(13)
Edge_Net[52,5,0,0,0,0:] = exprzeros(13)
Edge_Net[52,6,0,0,0,0:] = exprzeros(13)
Edge_Net[52,7,0,0,0,0:] = exprzeros(13)
Edge_Net[52,8,0,0,0,0:] = exprzeros(13)
Edge_Net[52,9,0,0,0,0:] = exprzeros(13)
Edge_Net[52,10,0,0,0,0:] = exprzeros(13)
Edge_Net[52,11,0,0,0,0:] = exprzeros(13)
Edge_Net[52,12,0,0,0,0:] = exprzeros(13)
Edge_Net[52,13,0,0,0,0:] = exprzeros(13)
Edge_Net[52,14,0,0,0,0:] = exprzeros(13)
Edge_Net[52,15,0,0,0,0:] = exprzeros(13)
Edge_Net[52,16,0,0,0,0:] = exprzeros(13)
Edge_Net[52,17,0,0,0,0:] = exprzeros(13)
Edge_Net[52,18,0,0,0,0:] = exprzeros(13)
Edge_Net[52,19,0,0,0,0:] = exprzeros(13)
Edge_Net[52,20,0,0,0,0:] = exprzeros(13)
Edge_Net[52,21,0,0,0,0:] = exprzeros(13)
Edge_Net[52,22,0,0,0,0:] = exprzeros(13)
Edge_Net[52,23,0,0,0,0:] = exprzeros(13)
Edge_Net[52,24,0,0,0,0:] = exprzeros(13)
Edge_Net[52,25,0,0,0,0:] = exprzeros(13)
Edge_Net[52,26,0,0,0,0:] = exprzeros(13)
Edge_Net[52,27,0,0,0,0:] = exprzeros(13)
Edge_Net[52,28,0,0,0,0:] = exprzeros(13)
Edge_Net[52,29,0,0,0,0:] = exprzeros(13)
Edge_Net[52,30,0,0,0,0:] = exprzeros(13)
Edge_Net[52,31,0,0,0,0:] = exprzeros(13)
Edge_Net[52,32,0,0,0,0:] = exprzeros(13)
Edge_Net[52,33,0,0,0,0:] = exprzeros(13)
Edge_Net[52,34,0,0,0,0:] = exprzeros(13)
Edge_Net[52,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[56,0,0,0,0,0:] = exprzeros(13)
Edge_Net[56,1,0,0,0,0:] = exprzeros(13)
Edge_Net[56,2,0,0,0,0:] = exprzeros(13)
Edge_Net[56,3,0,0,0,0:] = exprzeros(13)
Edge_Net[56,4,0,0,0,0:] = exprzeros(13)
Edge_Net[56,5,0,0,0,0:] = exprzeros(13)
Edge_Net[56,6,0,0,0,0:] = exprzeros(13)
Edge_Net[56,7,0,0,0,0:] = exprzeros(13)
Edge_Net[56,8,0,0,0,0:] = exprzeros(13)
Edge_Net[56,9,0,0,0,0:] = exprzeros(13)
Edge_Net[56,10,0,0,0,0:] = exprzeros(13)
Edge_Net[56,11,0,0,0,0:] = exprzeros(13)
Edge_Net[56,12,0,0,0,0:] = exprzeros(13)
Edge_Net[56,13,0,0,0,0:] = exprzeros(13)
Edge_Net[56,14,0,0,0,0:] = exprzeros(13)
Edge_Net[56,15,0,0,0,0:] = exprzeros(13)
Edge_Net[56,16,0,0,0,0:] = exprzeros(13)
Edge_Net[56,17,0,0,0,0:] = exprzeros(13)
Edge_Net[56,18,0,0,0,0:] = exprzeros(13)
Edge_Net[56,19,0,0,0,0:] = exprzeros(13)
Edge_Net[56,20,0,0,0,0:] = exprzeros(13)
Edge_Net[56,21,0,0,0,0:] = exprzeros(13)
Edge_Net[56,22,0,0,0,0:] = exprzeros(13)
Edge_Net[56,23,0,0,0,0:] = exprzeros(13)
Edge_Net[56,24,0,0,0,0:] = exprzeros(13)
Edge_Net[56,25,0,0,0,0:] = exprzeros(13)
Edge_Net[56,26,0,0,0,0:] = exprzeros(13)
Edge_Net[56,27,0,0,0,0:] = exprzeros(13)
Edge_Net[56,28,0,0,0,0:] = exprzeros(13)
Edge_Net[56,29,0,0,0,0:] = exprzeros(13)
Edge_Net[56,30,0,0,0,0:] = exprzeros(13)
Edge_Net[56,31,0,0,0,0:] = exprzeros(13)
Edge_Net[56,32,0,0,0,0:] = exprzeros(13)
Edge_Net[56,33,0,0,0,0:] = exprzeros(13)
Edge_Net[56,34,0,0,0,0:] = exprzeros(13)
Edge_Net[56,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[60,0,0,0,0,0:] = exprzeros(13)
Edge_Net[60,1,0,0,0,0:] = exprzeros(13)
Edge_Net[60,2,0,0,0,0:] = exprzeros(13)
Edge_Net[60,3,0,0,0,0:] = exprzeros(13)
Edge_Net[60,4,0,0,0,0:] = exprzeros(13)
Edge_Net[60,5,0,0,0,0:] = exprzeros(13)
Edge_Net[60,6,0,0,0,0:] = exprzeros(13)
Edge_Net[60,7,0,0,0,0:] = exprzeros(13)
Edge_Net[60,8,0,0,0,0:] = exprzeros(13)
Edge_Net[60,9,0,0,0,0:] = exprzeros(13)
Edge_Net[60,10,0,0,0,0:] = exprzeros(13)
Edge_Net[60,11,0,0,0,0:] = exprzeros(13)
Edge_Net[60,12,0,0,0,0:] = exprzeros(13)
Edge_Net[60,13,0,0,0,0:] = exprzeros(13)
Edge_Net[60,14,0,0,0,0:] = exprzeros(13)
Edge_Net[60,15,0,0,0,0:] = exprzeros(13)
Edge_Net[60,16,0,0,0,0:] = exprzeros(13)
Edge_Net[60,17,0,0,0,0:] = exprzeros(13)
Edge_Net[60,18,0,0,0,0:] = exprzeros(13)
Edge_Net[60,19,0,0,0,0:] = exprzeros(13)
Edge_Net[60,20,0,0,0,0:] = exprzeros(13)
Edge_Net[60,21,0,0,0,0:] = exprzeros(13)
Edge_Net[60,22,0,0,0,0:] = exprzeros(13)
Edge_Net[60,23,0,0,0,0:] = exprzeros(13)
Edge_Net[60,24,0,0,0,0:] = exprzeros(13)
Edge_Net[60,25,0,0,0,0:] = exprzeros(13)
Edge_Net[60,26,0,0,0,0:] = exprzeros(13)
Edge_Net[60,27,0,0,0,0:] = exprzeros(13)
Edge_Net[60,28,0,0,0,0:] = exprzeros(13)
Edge_Net[60,29,0,0,0,0:] = exprzeros(13)
Edge_Net[60,30,0,0,0,0:] = exprzeros(13)
Edge_Net[60,31,0,0,0,0:] = exprzeros(13)
Edge_Net[60,32,0,0,0,0:] = exprzeros(13)
Edge_Net[60,33,0,0,0,0:] = exprzeros(13)
Edge_Net[60,34,0,0,0,0:] = exprzeros(13)
Edge_Net[60,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[64,0,0,0,0,0:] = exprzeros(13)
Edge_Net[64,1,0,0,0,0:] = exprzeros(13)
Edge_Net[64,2,0,0,0,0:] = exprzeros(13)
Edge_Net[64,3,0,0,0,0:] = exprzeros(13)
Edge_Net[64,4,0,0,0,0:] = exprzeros(13)
Edge_Net[64,5,0,0,0,0:] = exprzeros(13)
Edge_Net[64,6,0,0,0,0:] = exprzeros(13)
Edge_Net[64,7,0,0,0,0:] = exprzeros(13)
Edge_Net[64,8,0,0,0,0:] = exprzeros(13)
Edge_Net[64,9,0,0,0,0:] = exprzeros(13)
Edge_Net[64,10,0,0,0,0:] = exprzeros(13)
Edge_Net[64,11,0,0,0,0:] = exprzeros(13)
Edge_Net[64,12,0,0,0,0:] = exprzeros(13)
Edge_Net[64,13,0,0,0,0:] = exprzeros(13)
Edge_Net[64,14,0,0,0,0:] = exprzeros(13)
Edge_Net[64,15,0,0,0,0:] = exprzeros(13)
Edge_Net[64,16,0,0,0,0:] = exprzeros(13)
Edge_Net[64,17,0,0,0,0:] = exprzeros(13)
Edge_Net[64,18,0,0,0,0:] = exprzeros(13)
Edge_Net[64,19,0,0,0,0:] = exprzeros(13)
Edge_Net[64,20,0,0,0,0:] = exprzeros(13)
Edge_Net[64,21,0,0,0,0:] = exprzeros(13)
Edge_Net[64,22,0,0,0,0:] = exprzeros(13)
Edge_Net[64,23,0,0,0,0:] = exprzeros(13)
Edge_Net[64,24,0,0,0,0:] = exprzeros(13)
Edge_Net[64,25,0,0,0,0:] = exprzeros(13)
Edge_Net[64,26,0,0,0,0:] = exprzeros(13)
Edge_Net[64,27,0,0,0,0:] = exprzeros(13)
Edge_Net[64,28,0,0,0,0:] = exprzeros(13)
Edge_Net[64,29,0,0,0,0:] = exprzeros(13)
Edge_Net[64,30,0,0,0,0:] = exprzeros(13)
Edge_Net[64,31,0,0,0,0:] = exprzeros(13)
Edge_Net[64,32,0,0,0,0:] = exprzeros(13)
Edge_Net[64,33,0,0,0,0:] = exprzeros(13)
Edge_Net[64,34,0,0,0,0:] = exprzeros(13)
Edge_Net[64,35,0,0,0,0:] = exprzeros(13)
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
Edge_Net[68,0,0,0,0,0:] = exprzeros(13)
Edge_Net[68,1,0,0,0,0:] = exprzeros(13)
Edge_Net[68,2,0,0,0,0:] = exprzeros(13)
Edge_Net[68,3,0,0,0,0:] = exprzeros(13)
Edge_Net[68,4,0,0,0,0:] = exprzeros(13)
Edge_Net[68,5,0,0,0,0:] = exprzeros(13)
Edge_Net[68,6,0,0,0,0:] = exprzeros(13)
Edge_Net[68,7,0,0,0,0:] = exprzeros(13)
Edge_Net[68,8,0,0,0,0:] = exprzeros(13)
Edge_Net[68,9,0,0,0,0:] = exprzeros(13)
Edge_Net[68,10,0,0,0,0:] = exprzeros(13)
Edge_Net[68,11,0,0,0,0:] = exprzeros(13)
Edge_Net[68,12,0,0,0,0:] = exprzeros(13)
Edge_Net[68,13,0,0,0,0:] = exprzeros(13)
Edge_Net[68,14,0,0,0,0:] = exprzeros(13)
Edge_Net[68,15,0,0,0,0:] = exprzeros(13)
Edge_Net[68,16,0,0,0,0:] = exprzeros(13)
Edge_Net[68,17,0,0,0,0:] = exprzeros(13)
Edge_Net[68,18,0,0,0,0:] = exprzeros(13)
Edge_Net[68,19,0,0,0,0:] = exprzeros(13)
Edge_Net[68,20,0,0,0,0:] = exprzeros(13)
Edge_Net[68,21,0,0,0,0:] = exprzeros(13)
Edge_Net[68,22,0,0,0,0:] = exprzeros(13)
Edge_Net[68,23,0,0,0,0:] = exprzeros(13)
Edge_Net[68,24,0,0,0,0:] = exprzeros(13)
Edge_Net[68,25,0,0,0,0:] = exprzeros(13)
Edge_Net[68,26,0,0,0,0:] = exprzeros(13)
Edge_Net[68,27,0,0,0,0:] = exprzeros(13)
Edge_Net[68,28,0,0,0,0:] = exprzeros(13)
Edge_Net[68,29,0,0,0,0:] = exprzeros(13)
Edge_Net[68,30,0,0,0,0:] = exprzeros(13)
Edge_Net[68,31,0,0,0,0:] = exprzeros(13)
Edge_Net[68,32,0,0,0,0:] = exprzeros(13)
Edge_Net[68,33,0,0,0,0:] = exprzeros(13)
Edge_Net[68,34,0,0,0,0:] = exprzeros(13)
Edge_Net[68,35,0,0,0,0:] = exprzeros(13)

#Initialize P AIL1
#store in
#(L)Initialize Edge
Edge[2,1,0,0,1] = expr(1)
Edge[2,2,0,0,1] = expr(1)
Edge[2,3,0,0,1] = expr(1)
Edge[2,4,0,0,1] = expr(1)
Edge[2,5,0,0,1] = expr(1)
Edge[2,6,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[2,1,0,0,1,0:] = exprzeros(13)
Edge_Net[2,2,0,0,1,0:] = exprzeros(13)
Edge_Net[2,3,0,0,1,0:] = exprzeros(13)
Edge_Net[2,4,0,0,1,0:] = exprzeros(13)
Edge_Net[2,5,0,0,1,0:] = exprzeros(13)
Edge_Net[2,6,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[6,1,0,0,1] = expr(1)
Edge[6,2,0,0,1] = expr(1)
Edge[6,3,0,0,1] = expr(1)
Edge[6,4,0,0,1] = expr(1)
Edge[6,5,0,0,1] = expr(1)
Edge[6,6,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[6,1,0,0,1,0:] = exprzeros(13)
Edge_Net[6,2,0,0,1,0:] = exprzeros(13)
Edge_Net[6,3,0,0,1,0:] = exprzeros(13)
Edge_Net[6,4,0,0,1,0:] = exprzeros(13)
Edge_Net[6,5,0,0,1,0:] = exprzeros(13)
Edge_Net[6,6,0,0,1,0:] = exprzeros(13)
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
Edge[2,0,1,1,1] = expr(0)
Edge[2,1,1,1,1] = expr(0)
Edge[2,2,1,1,1] = expr(0)
Edge[2,3,1,1,1] = expr(0)
Edge[2,4,1,1,1] = expr(0)
Edge[2,5,1,1,1] = expr(0)
Edge[2,6,1,1,1] = expr(0)
Edge[2,7,1,1,1] = expr(0)
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
Edge[6,0,1,1,1] = expr(0)
Edge[6,1,1,1,1] = expr(0)
Edge[6,2,1,1,1] = expr(0)
Edge[6,3,1,1,1] = expr(0)
Edge[6,4,1,1,1] = expr(0)
Edge[6,5,1,1,1] = expr(0)
Edge[6,6,1,1,1] = expr(0)
Edge[6,7,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[6,1,0,0,1] = expr(1)
Edge[6,2,0,0,1] = expr(1)
Edge[6,3,0,0,1] = expr(1)
Edge[6,4,0,0,1] = expr(1)
Edge[6,5,0,0,1] = expr(1)
Edge[6,6,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[6,1,0,0,1,0:] = exprzeros(13)
Edge_Net[6,2,0,0,1,0:] = exprzeros(13)
Edge_Net[6,3,0,0,1,0:] = exprzeros(13)
Edge_Net[6,4,0,0,1,0:] = exprzeros(13)
Edge_Net[6,5,0,0,1,0:] = exprzeros(13)
Edge_Net[6,6,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[10,1,0,0,1] = expr(1)
Edge[10,2,0,0,1] = expr(1)
Edge[10,3,0,0,1] = expr(1)
Edge[10,4,0,0,1] = expr(1)
Edge[10,5,0,0,1] = expr(1)
Edge[10,6,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[10,1,0,0,1,0:] = exprzeros(13)
Edge_Net[10,2,0,0,1,0:] = exprzeros(13)
Edge_Net[10,3,0,0,1,0:] = exprzeros(13)
Edge_Net[10,4,0,0,1,0:] = exprzeros(13)
Edge_Net[10,5,0,0,1,0:] = exprzeros(13)
Edge_Net[10,6,0,0,1,0:] = exprzeros(13)
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
Edge[6,0,1,1,1] = expr(0)
Edge[6,1,1,1,1] = expr(0)
Edge[6,2,1,1,1] = expr(0)
Edge[6,3,1,1,1] = expr(0)
Edge[6,4,1,1,1] = expr(0)
Edge[6,5,1,1,1] = expr(0)
Edge[6,6,1,1,1] = expr(0)
Edge[6,7,1,1,1] = expr(0)
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
Edge[10,0,1,1,1] = expr(0)
Edge[10,1,1,1,1] = expr(0)
Edge[10,2,1,1,1] = expr(0)
Edge[10,3,1,1,1] = expr(0)
Edge[10,4,1,1,1] = expr(0)
Edge[10,5,1,1,1] = expr(0)
Edge[10,6,1,1,1] = expr(0)
Edge[10,7,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[10,1,0,0,1] = expr(1)
Edge[10,2,0,0,1] = expr(1)
Edge[10,3,0,0,1] = expr(1)
Edge[10,4,0,0,1] = expr(1)
Edge[10,5,0,0,1] = expr(1)
Edge[10,6,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[10,1,0,0,1,0:] = exprzeros(13)
Edge_Net[10,2,0,0,1,0:] = exprzeros(13)
Edge_Net[10,3,0,0,1,0:] = exprzeros(13)
Edge_Net[10,4,0,0,1,0:] = exprzeros(13)
Edge_Net[10,5,0,0,1,0:] = exprzeros(13)
Edge_Net[10,6,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[14,1,0,0,1] = expr(1)
Edge[14,2,0,0,1] = expr(1)
Edge[14,3,0,0,1] = expr(1)
Edge[14,4,0,0,1] = expr(1)
Edge[14,5,0,0,1] = expr(1)
Edge[14,6,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[14,1,0,0,1,0:] = exprzeros(13)
Edge_Net[14,2,0,0,1,0:] = exprzeros(13)
Edge_Net[14,3,0,0,1,0:] = exprzeros(13)
Edge_Net[14,4,0,0,1,0:] = exprzeros(13)
Edge_Net[14,5,0,0,1,0:] = exprzeros(13)
Edge_Net[14,6,0,0,1,0:] = exprzeros(13)
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
Edge[10,0,1,1,1] = expr(0)
Edge[10,1,1,1,1] = expr(0)
Edge[10,2,1,1,1] = expr(0)
Edge[10,3,1,1,1] = expr(0)
Edge[10,4,1,1,1] = expr(0)
Edge[10,5,1,1,1] = expr(0)
Edge[10,6,1,1,1] = expr(0)
Edge[10,7,1,1,1] = expr(0)
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
Edge[14,0,1,1,1] = expr(0)
Edge[14,1,1,1,1] = expr(0)
Edge[14,2,1,1,1] = expr(0)
Edge[14,3,1,1,1] = expr(0)
Edge[14,4,1,1,1] = expr(0)
Edge[14,5,1,1,1] = expr(0)
Edge[14,6,1,1,1] = expr(0)
Edge[14,7,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[14,1,0,0,1] = expr(1)
Edge[14,2,0,0,1] = expr(1)
Edge[14,3,0,0,1] = expr(1)
Edge[14,4,0,0,1] = expr(1)
Edge[14,5,0,0,1] = expr(1)
Edge[14,6,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[14,1,0,0,1,0:] = exprzeros(13)
Edge_Net[14,2,0,0,1,0:] = exprzeros(13)
Edge_Net[14,3,0,0,1,0:] = exprzeros(13)
Edge_Net[14,4,0,0,1,0:] = exprzeros(13)
Edge_Net[14,5,0,0,1,0:] = exprzeros(13)
Edge_Net[14,6,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[18,1,0,0,1] = expr(1)
Edge[18,2,0,0,1] = expr(1)
Edge[18,3,0,0,1] = expr(1)
Edge[18,4,0,0,1] = expr(1)
Edge[18,5,0,0,1] = expr(1)
Edge[18,6,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[18,1,0,0,1,0:] = exprzeros(13)
Edge_Net[18,2,0,0,1,0:] = exprzeros(13)
Edge_Net[18,3,0,0,1,0:] = exprzeros(13)
Edge_Net[18,4,0,0,1,0:] = exprzeros(13)
Edge_Net[18,5,0,0,1,0:] = exprzeros(13)
Edge_Net[18,6,0,0,1,0:] = exprzeros(13)
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
Edge[14,0,1,1,1] = expr(0)
Edge[14,1,1,1,1] = expr(0)
Edge[14,2,1,1,1] = expr(0)
Edge[14,3,1,1,1] = expr(0)
Edge[14,4,1,1,1] = expr(0)
Edge[14,5,1,1,1] = expr(0)
Edge[14,6,1,1,1] = expr(0)
Edge[14,7,1,1,1] = expr(0)
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
Edge[18,0,1,1,1] = expr(0)
Edge[18,1,1,1,1] = expr(0)
Edge[18,2,1,1,1] = expr(0)
Edge[18,3,1,1,1] = expr(0)
Edge[18,4,1,1,1] = expr(0)
Edge[18,5,1,1,1] = expr(0)
Edge[18,6,1,1,1] = expr(0)
Edge[18,7,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[18,1,0,0,1] = expr(1)
Edge[18,2,0,0,1] = expr(1)
Edge[18,3,0,0,1] = expr(1)
Edge[18,4,0,0,1] = expr(1)
Edge[18,5,0,0,1] = expr(1)
Edge[18,6,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[18,1,0,0,1,0:] = exprzeros(13)
Edge_Net[18,2,0,0,1,0:] = exprzeros(13)
Edge_Net[18,3,0,0,1,0:] = exprzeros(13)
Edge_Net[18,4,0,0,1,0:] = exprzeros(13)
Edge_Net[18,5,0,0,1,0:] = exprzeros(13)
Edge_Net[18,6,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[22,1,0,0,1] = expr(1)
Edge[22,2,0,0,1] = expr(1)
Edge[22,3,0,0,1] = expr(1)
Edge[22,4,0,0,1] = expr(1)
Edge[22,5,0,0,1] = expr(1)
Edge[22,6,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[22,1,0,0,1,0:] = exprzeros(13)
Edge_Net[22,2,0,0,1,0:] = exprzeros(13)
Edge_Net[22,3,0,0,1,0:] = exprzeros(13)
Edge_Net[22,4,0,0,1,0:] = exprzeros(13)
Edge_Net[22,5,0,0,1,0:] = exprzeros(13)
Edge_Net[22,6,0,0,1,0:] = exprzeros(13)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[18,0,1,1,1] = expr(0)
Edge[18,1,1,1,1] = expr(0)
Edge[18,2,1,1,1] = expr(0)
Edge[18,3,1,1,1] = expr(0)
Edge[18,4,1,1,1] = expr(0)
Edge[18,5,1,1,1] = expr(0)
Edge[18,6,1,1,1] = expr(0)
Edge[18,7,1,1,1] = expr(0)
Edge[18,0,1,1,1] = expr(0)
Edge[18,1,1,1,1] = expr(0)
Edge[18,2,1,1,1] = expr(0)
Edge[18,3,1,1,1] = expr(0)
Edge[18,4,1,1,1] = expr(0)
Edge[18,5,1,1,1] = expr(0)
Edge[18,6,1,1,1] = expr(0)
Edge[18,7,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[22,0,1,1,1] = expr(0)
Edge[22,1,1,1,1] = expr(0)
Edge[22,2,1,1,1] = expr(0)
Edge[22,3,1,1,1] = expr(0)
Edge[22,4,1,1,1] = expr(0)
Edge[22,5,1,1,1] = expr(0)
Edge[22,6,1,1,1] = expr(0)
Edge[22,7,1,1,1] = expr(0)
Edge[22,0,1,1,1] = expr(0)
Edge[22,1,1,1,1] = expr(0)
Edge[22,2,1,1,1] = expr(0)
Edge[22,3,1,1,1] = expr(0)
Edge[22,4,1,1,1] = expr(0)
Edge[22,5,1,1,1] = expr(0)
Edge[22,6,1,1,1] = expr(0)
Edge[22,7,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[22,1,0,0,1] = expr(1)
Edge[22,2,0,0,1] = expr(1)
Edge[22,3,0,0,1] = expr(1)
Edge[22,4,0,0,1] = expr(1)
Edge[22,5,0,0,1] = expr(1)
Edge[22,6,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[22,1,0,0,1,0:] = exprzeros(13)
Edge_Net[22,2,0,0,1,0:] = exprzeros(13)
Edge_Net[22,3,0,0,1,0:] = exprzeros(13)
Edge_Net[22,4,0,0,1,0:] = exprzeros(13)
Edge_Net[22,5,0,0,1,0:] = exprzeros(13)
Edge_Net[22,6,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[26,1,0,0,1] = expr(1)
Edge[26,2,0,0,1] = expr(1)
Edge[26,3,0,0,1] = expr(1)
Edge[26,4,0,0,1] = expr(1)
Edge[26,5,0,0,1] = expr(1)
Edge[26,6,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[26,1,0,0,1,0:] = exprzeros(13)
Edge_Net[26,2,0,0,1,0:] = exprzeros(13)
Edge_Net[26,3,0,0,1,0:] = exprzeros(13)
Edge_Net[26,4,0,0,1,0:] = exprzeros(13)
Edge_Net[26,5,0,0,1,0:] = exprzeros(13)
Edge_Net[26,6,0,0,1,0:] = exprzeros(13)
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
Edge[22,0,1,1,1] = expr(0)
Edge[22,1,1,1,1] = expr(0)
Edge[22,2,1,1,1] = expr(0)
Edge[22,3,1,1,1] = expr(0)
Edge[22,4,1,1,1] = expr(0)
Edge[22,5,1,1,1] = expr(0)
Edge[22,6,1,1,1] = expr(0)
Edge[22,7,1,1,1] = expr(0)
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
Edge[26,0,1,1,1] = expr(0)
Edge[26,1,1,1,1] = expr(0)
Edge[26,2,1,1,1] = expr(0)
Edge[26,3,1,1,1] = expr(0)
Edge[26,4,1,1,1] = expr(0)
Edge[26,5,1,1,1] = expr(0)
Edge[26,6,1,1,1] = expr(0)
Edge[26,7,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[26,1,0,0,1] = expr(1)
Edge[26,2,0,0,1] = expr(1)
Edge[26,3,0,0,1] = expr(1)
Edge[26,4,0,0,1] = expr(1)
Edge[26,5,0,0,1] = expr(1)
Edge[26,6,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[26,1,0,0,1,0:] = exprzeros(13)
Edge_Net[26,2,0,0,1,0:] = exprzeros(13)
Edge_Net[26,3,0,0,1,0:] = exprzeros(13)
Edge_Net[26,4,0,0,1,0:] = exprzeros(13)
Edge_Net[26,5,0,0,1,0:] = exprzeros(13)
Edge_Net[26,6,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[30,1,0,0,1] = expr(1)
Edge[30,2,0,0,1] = expr(1)
Edge[30,3,0,0,1] = expr(1)
Edge[30,4,0,0,1] = expr(1)
Edge[30,5,0,0,1] = expr(1)
Edge[30,6,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[30,1,0,0,1,0:] = exprzeros(13)
Edge_Net[30,2,0,0,1,0:] = exprzeros(13)
Edge_Net[30,3,0,0,1,0:] = exprzeros(13)
Edge_Net[30,4,0,0,1,0:] = exprzeros(13)
Edge_Net[30,5,0,0,1,0:] = exprzeros(13)
Edge_Net[30,6,0,0,1,0:] = exprzeros(13)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[26,0,1,1,1] = expr(0)
Edge[26,1,1,1,1] = expr(0)
Edge[26,2,1,1,1] = expr(0)
Edge[26,3,1,1,1] = expr(0)
Edge[26,4,1,1,1] = expr(0)
Edge[26,5,1,1,1] = expr(0)
Edge[26,6,1,1,1] = expr(0)
Edge[26,7,1,1,1] = expr(0)
Edge[26,0,1,1,1] = expr(0)
Edge[26,1,1,1,1] = expr(0)
Edge[26,2,1,1,1] = expr(0)
Edge[26,3,1,1,1] = expr(0)
Edge[26,4,1,1,1] = expr(0)
Edge[26,5,1,1,1] = expr(0)
Edge[26,6,1,1,1] = expr(0)
Edge[26,7,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[30,0,1,1,1] = expr(0)
Edge[30,1,1,1,1] = expr(0)
Edge[30,2,1,1,1] = expr(0)
Edge[30,3,1,1,1] = expr(0)
Edge[30,4,1,1,1] = expr(0)
Edge[30,5,1,1,1] = expr(0)
Edge[30,6,1,1,1] = expr(0)
Edge[30,7,1,1,1] = expr(0)
Edge[30,0,1,1,1] = expr(0)
Edge[30,1,1,1,1] = expr(0)
Edge[30,2,1,1,1] = expr(0)
Edge[30,3,1,1,1] = expr(0)
Edge[30,4,1,1,1] = expr(0)
Edge[30,5,1,1,1] = expr(0)
Edge[30,6,1,1,1] = expr(0)
Edge[30,7,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[30,1,0,0,1] = expr(1)
Edge[30,2,0,0,1] = expr(1)
Edge[30,3,0,0,1] = expr(1)
Edge[30,4,0,0,1] = expr(1)
Edge[30,5,0,0,1] = expr(1)
Edge[30,6,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[30,1,0,0,1,0:] = exprzeros(13)
Edge_Net[30,2,0,0,1,0:] = exprzeros(13)
Edge_Net[30,3,0,0,1,0:] = exprzeros(13)
Edge_Net[30,4,0,0,1,0:] = exprzeros(13)
Edge_Net[30,5,0,0,1,0:] = exprzeros(13)
Edge_Net[30,6,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[34,1,0,0,1] = expr(1)
Edge[34,2,0,0,1] = expr(1)
Edge[34,3,0,0,1] = expr(1)
Edge[34,4,0,0,1] = expr(1)
Edge[34,5,0,0,1] = expr(1)
Edge[34,6,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[34,1,0,0,1,0:] = exprzeros(13)
Edge_Net[34,2,0,0,1,0:] = exprzeros(13)
Edge_Net[34,3,0,0,1,0:] = exprzeros(13)
Edge_Net[34,4,0,0,1,0:] = exprzeros(13)
Edge_Net[34,5,0,0,1,0:] = exprzeros(13)
Edge_Net[34,6,0,0,1,0:] = exprzeros(13)
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
Edge[30,0,1,1,1] = expr(0)
Edge[30,1,1,1,1] = expr(0)
Edge[30,2,1,1,1] = expr(0)
Edge[30,3,1,1,1] = expr(0)
Edge[30,4,1,1,1] = expr(0)
Edge[30,5,1,1,1] = expr(0)
Edge[30,6,1,1,1] = expr(0)
Edge[30,7,1,1,1] = expr(0)
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
Edge[34,0,1,1,1] = expr(0)
Edge[34,1,1,1,1] = expr(0)
Edge[34,2,1,1,1] = expr(0)
Edge[34,3,1,1,1] = expr(0)
Edge[34,4,1,1,1] = expr(0)
Edge[34,5,1,1,1] = expr(0)
Edge[34,6,1,1,1] = expr(0)
Edge[34,7,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[34,1,0,0,1] = expr(1)
Edge[34,2,0,0,1] = expr(1)
Edge[34,3,0,0,1] = expr(1)
Edge[34,4,0,0,1] = expr(1)
Edge[34,5,0,0,1] = expr(1)
Edge[34,6,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[34,1,0,0,1,0:] = exprzeros(13)
Edge_Net[34,2,0,0,1,0:] = exprzeros(13)
Edge_Net[34,3,0,0,1,0:] = exprzeros(13)
Edge_Net[34,4,0,0,1,0:] = exprzeros(13)
Edge_Net[34,5,0,0,1,0:] = exprzeros(13)
Edge_Net[34,6,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[38,1,0,0,1] = expr(1)
Edge[38,2,0,0,1] = expr(1)
Edge[38,3,0,0,1] = expr(1)
Edge[38,4,0,0,1] = expr(1)
Edge[38,5,0,0,1] = expr(1)
Edge[38,6,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[38,1,0,0,1,0:] = exprzeros(13)
Edge_Net[38,2,0,0,1,0:] = exprzeros(13)
Edge_Net[38,3,0,0,1,0:] = exprzeros(13)
Edge_Net[38,4,0,0,1,0:] = exprzeros(13)
Edge_Net[38,5,0,0,1,0:] = exprzeros(13)
Edge_Net[38,6,0,0,1,0:] = exprzeros(13)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[34,0,1,1,1] = expr(0)
Edge[34,1,1,1,1] = expr(0)
Edge[34,2,1,1,1] = expr(0)
Edge[34,3,1,1,1] = expr(0)
Edge[34,4,1,1,1] = expr(0)
Edge[34,5,1,1,1] = expr(0)
Edge[34,6,1,1,1] = expr(0)
Edge[34,7,1,1,1] = expr(0)
Edge[34,0,1,1,1] = expr(0)
Edge[34,1,1,1,1] = expr(0)
Edge[34,2,1,1,1] = expr(0)
Edge[34,3,1,1,1] = expr(0)
Edge[34,4,1,1,1] = expr(0)
Edge[34,5,1,1,1] = expr(0)
Edge[34,6,1,1,1] = expr(0)
Edge[34,7,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[38,0,1,1,1] = expr(0)
Edge[38,1,1,1,1] = expr(0)
Edge[38,2,1,1,1] = expr(0)
Edge[38,3,1,1,1] = expr(0)
Edge[38,4,1,1,1] = expr(0)
Edge[38,5,1,1,1] = expr(0)
Edge[38,6,1,1,1] = expr(0)
Edge[38,7,1,1,1] = expr(0)
Edge[38,0,1,1,1] = expr(0)
Edge[38,1,1,1,1] = expr(0)
Edge[38,2,1,1,1] = expr(0)
Edge[38,3,1,1,1] = expr(0)
Edge[38,4,1,1,1] = expr(0)
Edge[38,5,1,1,1] = expr(0)
Edge[38,6,1,1,1] = expr(0)
Edge[38,7,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[38,1,0,0,1] = expr(1)
Edge[38,2,0,0,1] = expr(1)
Edge[38,3,0,0,1] = expr(1)
Edge[38,4,0,0,1] = expr(1)
Edge[38,5,0,0,1] = expr(1)
Edge[38,6,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[38,1,0,0,1,0:] = exprzeros(13)
Edge_Net[38,2,0,0,1,0:] = exprzeros(13)
Edge_Net[38,3,0,0,1,0:] = exprzeros(13)
Edge_Net[38,4,0,0,1,0:] = exprzeros(13)
Edge_Net[38,5,0,0,1,0:] = exprzeros(13)
Edge_Net[38,6,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[42,1,0,0,1] = expr(1)
Edge[42,2,0,0,1] = expr(1)
Edge[42,3,0,0,1] = expr(1)
Edge[42,4,0,0,1] = expr(1)
Edge[42,5,0,0,1] = expr(1)
Edge[42,6,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[42,1,0,0,1,0:] = exprzeros(13)
Edge_Net[42,2,0,0,1,0:] = exprzeros(13)
Edge_Net[42,3,0,0,1,0:] = exprzeros(13)
Edge_Net[42,4,0,0,1,0:] = exprzeros(13)
Edge_Net[42,5,0,0,1,0:] = exprzeros(13)
Edge_Net[42,6,0,0,1,0:] = exprzeros(13)
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
Edge[38,0,1,1,1] = expr(0)
Edge[38,1,1,1,1] = expr(0)
Edge[38,2,1,1,1] = expr(0)
Edge[38,3,1,1,1] = expr(0)
Edge[38,4,1,1,1] = expr(0)
Edge[38,5,1,1,1] = expr(0)
Edge[38,6,1,1,1] = expr(0)
Edge[38,7,1,1,1] = expr(0)
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
Edge[42,0,1,1,1] = expr(0)
Edge[42,1,1,1,1] = expr(0)
Edge[42,2,1,1,1] = expr(0)
Edge[42,3,1,1,1] = expr(0)
Edge[42,4,1,1,1] = expr(0)
Edge[42,5,1,1,1] = expr(0)
Edge[42,6,1,1,1] = expr(0)
Edge[42,7,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[42,1,0,0,1] = expr(1)
Edge[42,2,0,0,1] = expr(1)
Edge[42,3,0,0,1] = expr(1)
Edge[42,4,0,0,1] = expr(1)
Edge[42,5,0,0,1] = expr(1)
Edge[42,6,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[42,1,0,0,1,0:] = exprzeros(13)
Edge_Net[42,2,0,0,1,0:] = exprzeros(13)
Edge_Net[42,3,0,0,1,0:] = exprzeros(13)
Edge_Net[42,4,0,0,1,0:] = exprzeros(13)
Edge_Net[42,5,0,0,1,0:] = exprzeros(13)
Edge_Net[42,6,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[46,1,0,0,1] = expr(1)
Edge[46,2,0,0,1] = expr(1)
Edge[46,3,0,0,1] = expr(1)
Edge[46,4,0,0,1] = expr(1)
Edge[46,5,0,0,1] = expr(1)
Edge[46,6,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[46,1,0,0,1,0:] = exprzeros(13)
Edge_Net[46,2,0,0,1,0:] = exprzeros(13)
Edge_Net[46,3,0,0,1,0:] = exprzeros(13)
Edge_Net[46,4,0,0,1,0:] = exprzeros(13)
Edge_Net[46,5,0,0,1,0:] = exprzeros(13)
Edge_Net[46,6,0,0,1,0:] = exprzeros(13)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[42,0,1,1,1] = expr(0)
Edge[42,1,1,1,1] = expr(0)
Edge[42,2,1,1,1] = expr(0)
Edge[42,3,1,1,1] = expr(0)
Edge[42,4,1,1,1] = expr(0)
Edge[42,5,1,1,1] = expr(0)
Edge[42,6,1,1,1] = expr(0)
Edge[42,7,1,1,1] = expr(0)
Edge[42,0,1,1,1] = expr(0)
Edge[42,1,1,1,1] = expr(0)
Edge[42,2,1,1,1] = expr(0)
Edge[42,3,1,1,1] = expr(0)
Edge[42,4,1,1,1] = expr(0)
Edge[42,5,1,1,1] = expr(0)
Edge[42,6,1,1,1] = expr(0)
Edge[42,7,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
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
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[50,1,0,0,1] = expr(1)
Edge[50,2,0,0,1] = expr(1)
Edge[50,3,0,0,1] = expr(1)
Edge[50,4,0,0,1] = expr(1)
Edge[50,5,0,0,1] = expr(1)
Edge[50,6,0,0,1] = expr(1)
Edge[50,7,0,0,1] = expr(1)
Edge[50,8,0,0,1] = expr(1)
Edge[50,9,0,0,1] = expr(1)
Edge[50,10,0,0,1] = expr(1)
Edge[50,11,0,0,1] = expr(1)
Edge[50,12,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[50,1,0,0,1,0:] = exprzeros(13)
Edge_Net[50,2,0,0,1,0:] = exprzeros(13)
Edge_Net[50,3,0,0,1,0:] = exprzeros(13)
Edge_Net[50,4,0,0,1,0:] = exprzeros(13)
Edge_Net[50,5,0,0,1,0:] = exprzeros(13)
Edge_Net[50,6,0,0,1,0:] = exprzeros(13)
Edge_Net[50,7,0,0,1,0:] = exprzeros(13)
Edge_Net[50,8,0,0,1,0:] = exprzeros(13)
Edge_Net[50,9,0,0,1,0:] = exprzeros(13)
Edge_Net[50,10,0,0,1,0:] = exprzeros(13)
Edge_Net[50,11,0,0,1,0:] = exprzeros(13)
Edge_Net[50,12,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
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
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[54,1,0,0,1,0:] = exprzeros(13)
Edge_Net[54,2,0,0,1,0:] = exprzeros(13)
Edge_Net[54,3,0,0,1,0:] = exprzeros(13)
Edge_Net[54,4,0,0,1,0:] = exprzeros(13)
Edge_Net[54,5,0,0,1,0:] = exprzeros(13)
Edge_Net[54,6,0,0,1,0:] = exprzeros(13)
Edge_Net[54,7,0,0,1,0:] = exprzeros(13)
Edge_Net[54,8,0,0,1,0:] = exprzeros(13)
Edge_Net[54,9,0,0,1,0:] = exprzeros(13)
Edge_Net[54,10,0,0,1,0:] = exprzeros(13)
Edge_Net[54,11,0,0,1,0:] = exprzeros(13)
Edge_Net[54,12,0,0,1,0:] = exprzeros(13)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[50,0,1,1,1] = expr(0)
Edge[50,1,1,1,1] = expr(0)
Edge[50,2,1,1,1] = expr(0)
Edge[50,3,1,1,1] = expr(0)
Edge[50,4,1,1,1] = expr(0)
Edge[50,5,1,1,1] = expr(0)
Edge[50,6,1,1,1] = expr(0)
Edge[50,7,1,1,1] = expr(0)
Edge[50,8,1,1,1] = expr(0)
Edge[50,9,1,1,1] = expr(0)
Edge[50,10,1,1,1] = expr(0)
Edge[50,11,1,1,1] = expr(0)
Edge[50,12,1,1,1] = expr(0)
Edge[50,13,1,1,1] = expr(0)
Edge[50,0,1,1,1] = expr(0)
Edge[50,1,1,1,1] = expr(0)
Edge[50,2,1,1,1] = expr(0)
Edge[50,3,1,1,1] = expr(0)
Edge[50,4,1,1,1] = expr(0)
Edge[50,5,1,1,1] = expr(0)
Edge[50,6,1,1,1] = expr(0)
Edge[50,7,1,1,1] = expr(0)
Edge[50,8,1,1,1] = expr(0)
Edge[50,9,1,1,1] = expr(0)
Edge[50,10,1,1,1] = expr(0)
Edge[50,11,1,1,1] = expr(0)
Edge[50,12,1,1,1] = expr(0)
Edge[50,13,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
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
#(R)End disable GIL
#store in
#(L)Initialize Edge
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
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[58,1,0,0,1,0:] = exprzeros(13)
Edge_Net[58,2,0,0,1,0:] = exprzeros(13)
Edge_Net[58,3,0,0,1,0:] = exprzeros(13)
Edge_Net[58,4,0,0,1,0:] = exprzeros(13)
Edge_Net[58,5,0,0,1,0:] = exprzeros(13)
Edge_Net[58,6,0,0,1,0:] = exprzeros(13)
Edge_Net[58,7,0,0,1,0:] = exprzeros(13)
Edge_Net[58,8,0,0,1,0:] = exprzeros(13)
Edge_Net[58,9,0,0,1,0:] = exprzeros(13)
Edge_Net[58,10,0,0,1,0:] = exprzeros(13)
#(L)End initialize EdgeNet
#(R)Initialize Edge
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
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[62,1,0,0,1,0:] = exprzeros(13)
Edge_Net[62,2,0,0,1,0:] = exprzeros(13)
Edge_Net[62,3,0,0,1,0:] = exprzeros(13)
Edge_Net[62,4,0,0,1,0:] = exprzeros(13)
Edge_Net[62,5,0,0,1,0:] = exprzeros(13)
Edge_Net[62,6,0,0,1,0:] = exprzeros(13)
Edge_Net[62,7,0,0,1,0:] = exprzeros(13)
Edge_Net[62,8,0,0,1,0:] = exprzeros(13)
Edge_Net[62,9,0,0,1,0:] = exprzeros(13)
Edge_Net[62,10,0,0,1,0:] = exprzeros(13)
#(R)End initialize EdgeNet
#(L)Disable GIL
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
#(L)End disable GIL
#(R)Disable GIL
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
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[62,1,0,0,1,0:] = exprzeros(13)
Edge_Net[62,2,0,0,1,0:] = exprzeros(13)
Edge_Net[62,3,0,0,1,0:] = exprzeros(13)
Edge_Net[62,4,0,0,1,0:] = exprzeros(13)
Edge_Net[62,5,0,0,1,0:] = exprzeros(13)
Edge_Net[62,6,0,0,1,0:] = exprzeros(13)
Edge_Net[62,7,0,0,1,0:] = exprzeros(13)
Edge_Net[62,8,0,0,1,0:] = exprzeros(13)
Edge_Net[62,9,0,0,1,0:] = exprzeros(13)
Edge_Net[62,10,0,0,1,0:] = exprzeros(13)
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
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[66,1,0,0,1,0:] = exprzeros(13)
Edge_Net[66,2,0,0,1,0:] = exprzeros(13)
Edge_Net[66,3,0,0,1,0:] = exprzeros(13)
Edge_Net[66,4,0,0,1,0:] = exprzeros(13)
Edge_Net[66,5,0,0,1,0:] = exprzeros(13)
Edge_Net[66,6,0,0,1,0:] = exprzeros(13)
Edge_Net[66,7,0,0,1,0:] = exprzeros(13)
Edge_Net[66,8,0,0,1,0:] = exprzeros(13)
Edge_Net[66,9,0,0,1,0:] = exprzeros(13)
Edge_Net[66,10,0,0,1,0:] = exprzeros(13)
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
#(R)End disable GIL

#Initialize N AIL1
Edge[2,28,0,0,1] = expr(1)
Edge[2,29,0,0,1] = expr(1)
Edge[2,30,0,0,1] = expr(1)
Edge[2,31,0,0,1] = expr(1)
Edge[2,32,0,0,1] = expr(1)
Edge[2,33,0,0,1] = expr(1)
Edge_Net[2,28,0,0,1,0:] = exprzeros(13)
Edge_Net[2,29,0,0,1,0:] = exprzeros(13)
Edge_Net[2,30,0,0,1,0:] = exprzeros(13)
Edge_Net[2,31,0,0,1,0:] = exprzeros(13)
Edge_Net[2,32,0,0,1,0:] = exprzeros(13)
Edge_Net[2,33,0,0,1,0:] = exprzeros(13)
Edge[6,28,0,0,1] = expr(1)
Edge[6,29,0,0,1] = expr(1)
Edge[6,30,0,0,1] = expr(1)
Edge[6,31,0,0,1] = expr(1)
Edge[6,32,0,0,1] = expr(1)
Edge[6,33,0,0,1] = expr(1)
Edge_Net[6,28,0,0,1,0:] = exprzeros(13)
Edge_Net[6,29,0,0,1,0:] = exprzeros(13)
Edge_Net[6,30,0,0,1,0:] = exprzeros(13)
Edge_Net[6,31,0,0,1,0:] = exprzeros(13)
Edge_Net[6,32,0,0,1,0:] = exprzeros(13)
Edge_Net[6,33,0,0,1,0:] = exprzeros(13)
Edge[2,27,1,1,1] = expr(0)
Edge[2,28,1,1,1] = expr(0)
Edge[2,29,1,1,1] = expr(0)
Edge[2,30,1,1,1] = expr(0)
Edge[2,31,1,1,1] = expr(0)
Edge[2,32,1,1,1] = expr(0)
Edge[2,33,1,1,1] = expr(0)
Edge[2,34,1,1,1] = expr(0)
Edge[2,35,1,1,1] = expr(0)
Edge[6,27,1,1,1] = expr(0)
Edge[6,28,1,1,1] = expr(0)
Edge[6,29,1,1,1] = expr(0)
Edge[6,30,1,1,1] = expr(0)
Edge[6,31,1,1,1] = expr(0)
Edge[6,32,1,1,1] = expr(0)
Edge[6,33,1,1,1] = expr(0)
Edge[6,34,1,1,1] = expr(0)
Edge[6,35,1,1,1] = expr(0)
Edge[6,28,0,0,1] = expr(1)
Edge[6,29,0,0,1] = expr(1)
Edge[6,30,0,0,1] = expr(1)
Edge[6,31,0,0,1] = expr(1)
Edge[6,32,0,0,1] = expr(1)
Edge[6,33,0,0,1] = expr(1)
Edge_Net[6,28,0,0,1,0:] = exprzeros(13)
Edge_Net[6,29,0,0,1,0:] = exprzeros(13)
Edge_Net[6,30,0,0,1,0:] = exprzeros(13)
Edge_Net[6,31,0,0,1,0:] = exprzeros(13)
Edge_Net[6,32,0,0,1,0:] = exprzeros(13)
Edge_Net[6,33,0,0,1,0:] = exprzeros(13)
Edge[10,28,0,0,1] = expr(1)
Edge[10,29,0,0,1] = expr(1)
Edge[10,30,0,0,1] = expr(1)
Edge[10,31,0,0,1] = expr(1)
Edge[10,32,0,0,1] = expr(1)
Edge[10,33,0,0,1] = expr(1)
Edge_Net[10,28,0,0,1,0:] = exprzeros(13)
Edge_Net[10,29,0,0,1,0:] = exprzeros(13)
Edge_Net[10,30,0,0,1,0:] = exprzeros(13)
Edge_Net[10,31,0,0,1,0:] = exprzeros(13)
Edge_Net[10,32,0,0,1,0:] = exprzeros(13)
Edge_Net[10,33,0,0,1,0:] = exprzeros(13)
Edge[6,27,1,1,1] = expr(0)
Edge[6,28,1,1,1] = expr(0)
Edge[6,29,1,1,1] = expr(0)
Edge[6,30,1,1,1] = expr(0)
Edge[6,31,1,1,1] = expr(0)
Edge[6,32,1,1,1] = expr(0)
Edge[6,33,1,1,1] = expr(0)
Edge[6,34,1,1,1] = expr(0)
Edge[6,35,1,1,1] = expr(0)
Edge[10,27,1,1,1] = expr(0)
Edge[10,28,1,1,1] = expr(0)
Edge[10,29,1,1,1] = expr(0)
Edge[10,30,1,1,1] = expr(0)
Edge[10,31,1,1,1] = expr(0)
Edge[10,32,1,1,1] = expr(0)
Edge[10,33,1,1,1] = expr(0)
Edge[10,34,1,1,1] = expr(0)
Edge[10,35,1,1,1] = expr(0)
Edge[10,28,0,0,1] = expr(1)
Edge[10,29,0,0,1] = expr(1)
Edge[10,30,0,0,1] = expr(1)
Edge[10,31,0,0,1] = expr(1)
Edge[10,32,0,0,1] = expr(1)
Edge[10,33,0,0,1] = expr(1)
Edge_Net[10,28,0,0,1,0:] = exprzeros(13)
Edge_Net[10,29,0,0,1,0:] = exprzeros(13)
Edge_Net[10,30,0,0,1,0:] = exprzeros(13)
Edge_Net[10,31,0,0,1,0:] = exprzeros(13)
Edge_Net[10,32,0,0,1,0:] = exprzeros(13)
Edge_Net[10,33,0,0,1,0:] = exprzeros(13)
Edge[14,28,0,0,1] = expr(1)
Edge[14,29,0,0,1] = expr(1)
Edge[14,30,0,0,1] = expr(1)
Edge[14,31,0,0,1] = expr(1)
Edge[14,32,0,0,1] = expr(1)
Edge[14,33,0,0,1] = expr(1)
Edge_Net[14,28,0,0,1,0:] = exprzeros(13)
Edge_Net[14,29,0,0,1,0:] = exprzeros(13)
Edge_Net[14,30,0,0,1,0:] = exprzeros(13)
Edge_Net[14,31,0,0,1,0:] = exprzeros(13)
Edge_Net[14,32,0,0,1,0:] = exprzeros(13)
Edge_Net[14,33,0,0,1,0:] = exprzeros(13)
Edge[10,27,1,1,1] = expr(0)
Edge[10,28,1,1,1] = expr(0)
Edge[10,29,1,1,1] = expr(0)
Edge[10,30,1,1,1] = expr(0)
Edge[10,31,1,1,1] = expr(0)
Edge[10,32,1,1,1] = expr(0)
Edge[10,33,1,1,1] = expr(0)
Edge[10,34,1,1,1] = expr(0)
Edge[10,35,1,1,1] = expr(0)
Edge[14,27,1,1,1] = expr(0)
Edge[14,28,1,1,1] = expr(0)
Edge[14,29,1,1,1] = expr(0)
Edge[14,30,1,1,1] = expr(0)
Edge[14,31,1,1,1] = expr(0)
Edge[14,32,1,1,1] = expr(0)
Edge[14,33,1,1,1] = expr(0)
Edge[14,34,1,1,1] = expr(0)
Edge[14,35,1,1,1] = expr(0)
Edge[14,28,0,0,1] = expr(1)
Edge[14,29,0,0,1] = expr(1)
Edge[14,30,0,0,1] = expr(1)
Edge[14,31,0,0,1] = expr(1)
Edge[14,32,0,0,1] = expr(1)
Edge[14,33,0,0,1] = expr(1)
Edge_Net[14,28,0,0,1,0:] = exprzeros(13)
Edge_Net[14,29,0,0,1,0:] = exprzeros(13)
Edge_Net[14,30,0,0,1,0:] = exprzeros(13)
Edge_Net[14,31,0,0,1,0:] = exprzeros(13)
Edge_Net[14,32,0,0,1,0:] = exprzeros(13)
Edge_Net[14,33,0,0,1,0:] = exprzeros(13)
Edge[18,28,0,0,1] = expr(1)
Edge[18,29,0,0,1] = expr(1)
Edge[18,30,0,0,1] = expr(1)
Edge[18,31,0,0,1] = expr(1)
Edge[18,32,0,0,1] = expr(1)
Edge[18,33,0,0,1] = expr(1)
Edge_Net[18,28,0,0,1,0:] = exprzeros(13)
Edge_Net[18,29,0,0,1,0:] = exprzeros(13)
Edge_Net[18,30,0,0,1,0:] = exprzeros(13)
Edge_Net[18,31,0,0,1,0:] = exprzeros(13)
Edge_Net[18,32,0,0,1,0:] = exprzeros(13)
Edge_Net[18,33,0,0,1,0:] = exprzeros(13)
Edge[14,27,1,1,1] = expr(0)
Edge[14,28,1,1,1] = expr(0)
Edge[14,29,1,1,1] = expr(0)
Edge[14,30,1,1,1] = expr(0)
Edge[14,31,1,1,1] = expr(0)
Edge[14,32,1,1,1] = expr(0)
Edge[14,33,1,1,1] = expr(0)
Edge[14,34,1,1,1] = expr(0)
Edge[14,35,1,1,1] = expr(0)
Edge[18,27,1,1,1] = expr(0)
Edge[18,28,1,1,1] = expr(0)
Edge[18,29,1,1,1] = expr(0)
Edge[18,30,1,1,1] = expr(0)
Edge[18,31,1,1,1] = expr(0)
Edge[18,32,1,1,1] = expr(0)
Edge[18,33,1,1,1] = expr(0)
Edge[18,34,1,1,1] = expr(0)
Edge[18,35,1,1,1] = expr(0)
Edge[18,28,0,0,1] = expr(1)
Edge[18,29,0,0,1] = expr(1)
Edge[18,30,0,0,1] = expr(1)
Edge[18,31,0,0,1] = expr(1)
Edge[18,32,0,0,1] = expr(1)
Edge[18,33,0,0,1] = expr(1)
Edge_Net[18,28,0,0,1,0:] = exprzeros(13)
Edge_Net[18,29,0,0,1,0:] = exprzeros(13)
Edge_Net[18,30,0,0,1,0:] = exprzeros(13)
Edge_Net[18,31,0,0,1,0:] = exprzeros(13)
Edge_Net[18,32,0,0,1,0:] = exprzeros(13)
Edge_Net[18,33,0,0,1,0:] = exprzeros(13)
Edge[22,28,0,0,1] = expr(1)
Edge[22,29,0,0,1] = expr(1)
Edge[22,30,0,0,1] = expr(1)
Edge[22,31,0,0,1] = expr(1)
Edge[22,32,0,0,1] = expr(1)
Edge[22,33,0,0,1] = expr(1)
Edge_Net[22,28,0,0,1,0:] = exprzeros(13)
Edge_Net[22,29,0,0,1,0:] = exprzeros(13)
Edge_Net[22,30,0,0,1,0:] = exprzeros(13)
Edge_Net[22,31,0,0,1,0:] = exprzeros(13)
Edge_Net[22,32,0,0,1,0:] = exprzeros(13)
Edge_Net[22,33,0,0,1,0:] = exprzeros(13)
Edge[18,27,1,1,1] = expr(0)
Edge[18,28,1,1,1] = expr(0)
Edge[18,29,1,1,1] = expr(0)
Edge[18,30,1,1,1] = expr(0)
Edge[18,31,1,1,1] = expr(0)
Edge[18,32,1,1,1] = expr(0)
Edge[18,33,1,1,1] = expr(0)
Edge[18,34,1,1,1] = expr(0)
Edge[18,35,1,1,1] = expr(0)
Edge[22,27,1,1,1] = expr(0)
Edge[22,28,1,1,1] = expr(0)
Edge[22,29,1,1,1] = expr(0)
Edge[22,30,1,1,1] = expr(0)
Edge[22,31,1,1,1] = expr(0)
Edge[22,32,1,1,1] = expr(0)
Edge[22,33,1,1,1] = expr(0)
Edge[22,34,1,1,1] = expr(0)
Edge[22,35,1,1,1] = expr(0)
Edge[22,28,0,0,1] = expr(1)
Edge[22,29,0,0,1] = expr(1)
Edge[22,30,0,0,1] = expr(1)
Edge[22,31,0,0,1] = expr(1)
Edge[22,32,0,0,1] = expr(1)
Edge[22,33,0,0,1] = expr(1)
Edge_Net[22,28,0,0,1,0:] = exprzeros(13)
Edge_Net[22,29,0,0,1,0:] = exprzeros(13)
Edge_Net[22,30,0,0,1,0:] = exprzeros(13)
Edge_Net[22,31,0,0,1,0:] = exprzeros(13)
Edge_Net[22,32,0,0,1,0:] = exprzeros(13)
Edge_Net[22,33,0,0,1,0:] = exprzeros(13)
Edge[26,28,0,0,1] = expr(1)
Edge[26,29,0,0,1] = expr(1)
Edge[26,30,0,0,1] = expr(1)
Edge[26,31,0,0,1] = expr(1)
Edge[26,32,0,0,1] = expr(1)
Edge[26,33,0,0,1] = expr(1)
Edge_Net[26,28,0,0,1,0:] = exprzeros(13)
Edge_Net[26,29,0,0,1,0:] = exprzeros(13)
Edge_Net[26,30,0,0,1,0:] = exprzeros(13)
Edge_Net[26,31,0,0,1,0:] = exprzeros(13)
Edge_Net[26,32,0,0,1,0:] = exprzeros(13)
Edge_Net[26,33,0,0,1,0:] = exprzeros(13)
Edge[22,27,1,1,1] = expr(0)
Edge[22,28,1,1,1] = expr(0)
Edge[22,29,1,1,1] = expr(0)
Edge[22,30,1,1,1] = expr(0)
Edge[22,31,1,1,1] = expr(0)
Edge[22,32,1,1,1] = expr(0)
Edge[22,33,1,1,1] = expr(0)
Edge[22,34,1,1,1] = expr(0)
Edge[22,35,1,1,1] = expr(0)
Edge[26,27,1,1,1] = expr(0)
Edge[26,28,1,1,1] = expr(0)
Edge[26,29,1,1,1] = expr(0)
Edge[26,30,1,1,1] = expr(0)
Edge[26,31,1,1,1] = expr(0)
Edge[26,32,1,1,1] = expr(0)
Edge[26,33,1,1,1] = expr(0)
Edge[26,34,1,1,1] = expr(0)
Edge[26,35,1,1,1] = expr(0)
Edge[26,28,0,0,1] = expr(1)
Edge[26,29,0,0,1] = expr(1)
Edge[26,30,0,0,1] = expr(1)
Edge[26,31,0,0,1] = expr(1)
Edge[26,32,0,0,1] = expr(1)
Edge[26,33,0,0,1] = expr(1)
Edge_Net[26,28,0,0,1,0:] = exprzeros(13)
Edge_Net[26,29,0,0,1,0:] = exprzeros(13)
Edge_Net[26,30,0,0,1,0:] = exprzeros(13)
Edge_Net[26,31,0,0,1,0:] = exprzeros(13)
Edge_Net[26,32,0,0,1,0:] = exprzeros(13)
Edge_Net[26,33,0,0,1,0:] = exprzeros(13)
Edge[30,28,0,0,1] = expr(1)
Edge[30,29,0,0,1] = expr(1)
Edge[30,30,0,0,1] = expr(1)
Edge[30,31,0,0,1] = expr(1)
Edge[30,32,0,0,1] = expr(1)
Edge[30,33,0,0,1] = expr(1)
Edge_Net[30,28,0,0,1,0:] = exprzeros(13)
Edge_Net[30,29,0,0,1,0:] = exprzeros(13)
Edge_Net[30,30,0,0,1,0:] = exprzeros(13)
Edge_Net[30,31,0,0,1,0:] = exprzeros(13)
Edge_Net[30,32,0,0,1,0:] = exprzeros(13)
Edge_Net[30,33,0,0,1,0:] = exprzeros(13)
Edge[26,27,1,1,1] = expr(0)
Edge[26,28,1,1,1] = expr(0)
Edge[26,29,1,1,1] = expr(0)
Edge[26,30,1,1,1] = expr(0)
Edge[26,31,1,1,1] = expr(0)
Edge[26,32,1,1,1] = expr(0)
Edge[26,33,1,1,1] = expr(0)
Edge[26,34,1,1,1] = expr(0)
Edge[26,35,1,1,1] = expr(0)
Edge[30,27,1,1,1] = expr(0)
Edge[30,28,1,1,1] = expr(0)
Edge[30,29,1,1,1] = expr(0)
Edge[30,30,1,1,1] = expr(0)
Edge[30,31,1,1,1] = expr(0)
Edge[30,32,1,1,1] = expr(0)
Edge[30,33,1,1,1] = expr(0)
Edge[30,34,1,1,1] = expr(0)
Edge[30,35,1,1,1] = expr(0)
Edge[30,28,0,0,1] = expr(1)
Edge[30,29,0,0,1] = expr(1)
Edge[30,30,0,0,1] = expr(1)
Edge[30,31,0,0,1] = expr(1)
Edge[30,32,0,0,1] = expr(1)
Edge[30,33,0,0,1] = expr(1)
Edge_Net[30,28,0,0,1,0:] = exprzeros(13)
Edge_Net[30,29,0,0,1,0:] = exprzeros(13)
Edge_Net[30,30,0,0,1,0:] = exprzeros(13)
Edge_Net[30,31,0,0,1,0:] = exprzeros(13)
Edge_Net[30,32,0,0,1,0:] = exprzeros(13)
Edge_Net[30,33,0,0,1,0:] = exprzeros(13)
Edge[34,28,0,0,1] = expr(1)
Edge[34,29,0,0,1] = expr(1)
Edge[34,30,0,0,1] = expr(1)
Edge[34,31,0,0,1] = expr(1)
Edge[34,32,0,0,1] = expr(1)
Edge[34,33,0,0,1] = expr(1)
Edge_Net[34,28,0,0,1,0:] = exprzeros(13)
Edge_Net[34,29,0,0,1,0:] = exprzeros(13)
Edge_Net[34,30,0,0,1,0:] = exprzeros(13)
Edge_Net[34,31,0,0,1,0:] = exprzeros(13)
Edge_Net[34,32,0,0,1,0:] = exprzeros(13)
Edge_Net[34,33,0,0,1,0:] = exprzeros(13)
Edge[30,27,1,1,1] = expr(0)
Edge[30,28,1,1,1] = expr(0)
Edge[30,29,1,1,1] = expr(0)
Edge[30,30,1,1,1] = expr(0)
Edge[30,31,1,1,1] = expr(0)
Edge[30,32,1,1,1] = expr(0)
Edge[30,33,1,1,1] = expr(0)
Edge[30,34,1,1,1] = expr(0)
Edge[30,35,1,1,1] = expr(0)
Edge[34,27,1,1,1] = expr(0)
Edge[34,28,1,1,1] = expr(0)
Edge[34,29,1,1,1] = expr(0)
Edge[34,30,1,1,1] = expr(0)
Edge[34,31,1,1,1] = expr(0)
Edge[34,32,1,1,1] = expr(0)
Edge[34,33,1,1,1] = expr(0)
Edge[34,34,1,1,1] = expr(0)
Edge[34,35,1,1,1] = expr(0)
Edge[34,28,0,0,1] = expr(1)
Edge[34,29,0,0,1] = expr(1)
Edge[34,30,0,0,1] = expr(1)
Edge[34,31,0,0,1] = expr(1)
Edge[34,32,0,0,1] = expr(1)
Edge[34,33,0,0,1] = expr(1)
Edge_Net[34,28,0,0,1,0:] = exprzeros(13)
Edge_Net[34,29,0,0,1,0:] = exprzeros(13)
Edge_Net[34,30,0,0,1,0:] = exprzeros(13)
Edge_Net[34,31,0,0,1,0:] = exprzeros(13)
Edge_Net[34,32,0,0,1,0:] = exprzeros(13)
Edge_Net[34,33,0,0,1,0:] = exprzeros(13)
Edge[38,28,0,0,1] = expr(1)
Edge[38,29,0,0,1] = expr(1)
Edge[38,30,0,0,1] = expr(1)
Edge[38,31,0,0,1] = expr(1)
Edge[38,32,0,0,1] = expr(1)
Edge[38,33,0,0,1] = expr(1)
Edge_Net[38,28,0,0,1,0:] = exprzeros(13)
Edge_Net[38,29,0,0,1,0:] = exprzeros(13)
Edge_Net[38,30,0,0,1,0:] = exprzeros(13)
Edge_Net[38,31,0,0,1,0:] = exprzeros(13)
Edge_Net[38,32,0,0,1,0:] = exprzeros(13)
Edge_Net[38,33,0,0,1,0:] = exprzeros(13)
Edge[34,27,1,1,1] = expr(0)
Edge[34,28,1,1,1] = expr(0)
Edge[34,29,1,1,1] = expr(0)
Edge[34,30,1,1,1] = expr(0)
Edge[34,31,1,1,1] = expr(0)
Edge[34,32,1,1,1] = expr(0)
Edge[34,33,1,1,1] = expr(0)
Edge[34,34,1,1,1] = expr(0)
Edge[34,35,1,1,1] = expr(0)
Edge[38,27,1,1,1] = expr(0)
Edge[38,28,1,1,1] = expr(0)
Edge[38,29,1,1,1] = expr(0)
Edge[38,30,1,1,1] = expr(0)
Edge[38,31,1,1,1] = expr(0)
Edge[38,32,1,1,1] = expr(0)
Edge[38,33,1,1,1] = expr(0)
Edge[38,34,1,1,1] = expr(0)
Edge[38,35,1,1,1] = expr(0)
Edge[38,28,0,0,1] = expr(1)
Edge[38,29,0,0,1] = expr(1)
Edge[38,30,0,0,1] = expr(1)
Edge[38,31,0,0,1] = expr(1)
Edge[38,32,0,0,1] = expr(1)
Edge[38,33,0,0,1] = expr(1)
Edge_Net[38,28,0,0,1,0:] = exprzeros(13)
Edge_Net[38,29,0,0,1,0:] = exprzeros(13)
Edge_Net[38,30,0,0,1,0:] = exprzeros(13)
Edge_Net[38,31,0,0,1,0:] = exprzeros(13)
Edge_Net[38,32,0,0,1,0:] = exprzeros(13)
Edge_Net[38,33,0,0,1,0:] = exprzeros(13)
Edge[42,28,0,0,1] = expr(1)
Edge[42,29,0,0,1] = expr(1)
Edge[42,30,0,0,1] = expr(1)
Edge[42,31,0,0,1] = expr(1)
Edge[42,32,0,0,1] = expr(1)
Edge[42,33,0,0,1] = expr(1)
Edge_Net[42,28,0,0,1,0:] = exprzeros(13)
Edge_Net[42,29,0,0,1,0:] = exprzeros(13)
Edge_Net[42,30,0,0,1,0:] = exprzeros(13)
Edge_Net[42,31,0,0,1,0:] = exprzeros(13)
Edge_Net[42,32,0,0,1,0:] = exprzeros(13)
Edge_Net[42,33,0,0,1,0:] = exprzeros(13)
Edge[38,27,1,1,1] = expr(0)
Edge[38,28,1,1,1] = expr(0)
Edge[38,29,1,1,1] = expr(0)
Edge[38,30,1,1,1] = expr(0)
Edge[38,31,1,1,1] = expr(0)
Edge[38,32,1,1,1] = expr(0)
Edge[38,33,1,1,1] = expr(0)
Edge[38,34,1,1,1] = expr(0)
Edge[38,35,1,1,1] = expr(0)
Edge[42,27,1,1,1] = expr(0)
Edge[42,28,1,1,1] = expr(0)
Edge[42,29,1,1,1] = expr(0)
Edge[42,30,1,1,1] = expr(0)
Edge[42,31,1,1,1] = expr(0)
Edge[42,32,1,1,1] = expr(0)
Edge[42,33,1,1,1] = expr(0)
Edge[42,34,1,1,1] = expr(0)
Edge[42,35,1,1,1] = expr(0)
Edge[42,28,0,0,1] = expr(1)
Edge[42,29,0,0,1] = expr(1)
Edge[42,30,0,0,1] = expr(1)
Edge[42,31,0,0,1] = expr(1)
Edge[42,32,0,0,1] = expr(1)
Edge[42,33,0,0,1] = expr(1)
Edge_Net[42,28,0,0,1,0:] = exprzeros(13)
Edge_Net[42,29,0,0,1,0:] = exprzeros(13)
Edge_Net[42,30,0,0,1,0:] = exprzeros(13)
Edge_Net[42,31,0,0,1,0:] = exprzeros(13)
Edge_Net[42,32,0,0,1,0:] = exprzeros(13)
Edge_Net[42,33,0,0,1,0:] = exprzeros(13)
Edge[46,28,0,0,1] = expr(1)
Edge[46,29,0,0,1] = expr(1)
Edge[46,30,0,0,1] = expr(1)
Edge[46,31,0,0,1] = expr(1)
Edge[46,32,0,0,1] = expr(1)
Edge[46,33,0,0,1] = expr(1)
Edge_Net[46,28,0,0,1,0:] = exprzeros(13)
Edge_Net[46,29,0,0,1,0:] = exprzeros(13)
Edge_Net[46,30,0,0,1,0:] = exprzeros(13)
Edge_Net[46,31,0,0,1,0:] = exprzeros(13)
Edge_Net[46,32,0,0,1,0:] = exprzeros(13)
Edge_Net[46,33,0,0,1,0:] = exprzeros(13)
Edge[42,27,1,1,1] = expr(0)
Edge[42,28,1,1,1] = expr(0)
Edge[42,29,1,1,1] = expr(0)
Edge[42,30,1,1,1] = expr(0)
Edge[42,31,1,1,1] = expr(0)
Edge[42,32,1,1,1] = expr(0)
Edge[42,33,1,1,1] = expr(0)
Edge[42,34,1,1,1] = expr(0)
Edge[42,35,1,1,1] = expr(0)
Edge[46,27,1,1,1] = expr(0)
Edge[46,28,1,1,1] = expr(0)
Edge[46,29,1,1,1] = expr(0)
Edge[46,30,1,1,1] = expr(0)
Edge[46,31,1,1,1] = expr(0)
Edge[46,32,1,1,1] = expr(0)
Edge[46,33,1,1,1] = expr(0)
Edge[46,34,1,1,1] = expr(0)
Edge[46,35,1,1,1] = expr(0)
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
Edge_Net[50,22,0,0,1,0:] = exprzeros(13)
Edge_Net[50,23,0,0,1,0:] = exprzeros(13)
Edge_Net[50,24,0,0,1,0:] = exprzeros(13)
Edge_Net[50,25,0,0,1,0:] = exprzeros(13)
Edge_Net[50,26,0,0,1,0:] = exprzeros(13)
Edge_Net[50,27,0,0,1,0:] = exprzeros(13)
Edge_Net[50,28,0,0,1,0:] = exprzeros(13)
Edge_Net[50,29,0,0,1,0:] = exprzeros(13)
Edge_Net[50,30,0,0,1,0:] = exprzeros(13)
Edge_Net[50,31,0,0,1,0:] = exprzeros(13)
Edge_Net[50,32,0,0,1,0:] = exprzeros(13)
Edge_Net[50,33,0,0,1,0:] = exprzeros(13)
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
Edge_Net[54,22,0,0,1,0:] = exprzeros(13)
Edge_Net[54,23,0,0,1,0:] = exprzeros(13)
Edge_Net[54,24,0,0,1,0:] = exprzeros(13)
Edge_Net[54,25,0,0,1,0:] = exprzeros(13)
Edge_Net[54,26,0,0,1,0:] = exprzeros(13)
Edge_Net[54,27,0,0,1,0:] = exprzeros(13)
Edge_Net[54,28,0,0,1,0:] = exprzeros(13)
Edge_Net[54,29,0,0,1,0:] = exprzeros(13)
Edge_Net[54,30,0,0,1,0:] = exprzeros(13)
Edge_Net[54,31,0,0,1,0:] = exprzeros(13)
Edge_Net[54,32,0,0,1,0:] = exprzeros(13)
Edge_Net[54,33,0,0,1,0:] = exprzeros(13)
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
Edge[58,26,0,0,1] = expr(1)
Edge[58,27,0,0,1] = expr(1)
Edge[58,28,0,0,1] = expr(1)
Edge[58,29,0,0,1] = expr(1)
Edge[58,30,0,0,1] = expr(1)
Edge[58,31,0,0,1] = expr(1)
Edge[58,32,0,0,1] = expr(1)
Edge[58,33,0,0,1] = expr(1)
Edge_Net[58,26,0,0,1,0:] = exprzeros(13)
Edge_Net[58,27,0,0,1,0:] = exprzeros(13)
Edge_Net[58,28,0,0,1,0:] = exprzeros(13)
Edge_Net[58,29,0,0,1,0:] = exprzeros(13)
Edge_Net[58,30,0,0,1,0:] = exprzeros(13)
Edge_Net[58,31,0,0,1,0:] = exprzeros(13)
Edge_Net[58,32,0,0,1,0:] = exprzeros(13)
Edge_Net[58,33,0,0,1,0:] = exprzeros(13)
Edge[62,26,0,0,1] = expr(1)
Edge[62,27,0,0,1] = expr(1)
Edge[62,28,0,0,1] = expr(1)
Edge[62,29,0,0,1] = expr(1)
Edge[62,30,0,0,1] = expr(1)
Edge[62,31,0,0,1] = expr(1)
Edge[62,32,0,0,1] = expr(1)
Edge[62,33,0,0,1] = expr(1)
Edge_Net[62,26,0,0,1,0:] = exprzeros(13)
Edge_Net[62,27,0,0,1,0:] = exprzeros(13)
Edge_Net[62,28,0,0,1,0:] = exprzeros(13)
Edge_Net[62,29,0,0,1,0:] = exprzeros(13)
Edge_Net[62,30,0,0,1,0:] = exprzeros(13)
Edge_Net[62,31,0,0,1,0:] = exprzeros(13)
Edge_Net[62,32,0,0,1,0:] = exprzeros(13)
Edge_Net[62,33,0,0,1,0:] = exprzeros(13)
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
Edge[62,25,1,1,1] = expr(0)
Edge[62,26,1,1,1] = expr(0)
Edge[62,27,1,1,1] = expr(0)
Edge[62,28,1,1,1] = expr(0)
Edge[62,29,1,1,1] = expr(0)
Edge[62,30,1,1,1] = expr(0)
Edge[62,31,1,1,1] = expr(0)
Edge[62,32,1,1,1] = expr(0)
Edge[62,33,1,1,1] = expr(0)
Edge[62,34,1,1,1] = expr(0)
Edge[62,35,1,1,1] = expr(0)
Edge[62,26,0,0,1] = expr(1)
Edge[62,27,0,0,1] = expr(1)
Edge[62,28,0,0,1] = expr(1)
Edge[62,29,0,0,1] = expr(1)
Edge[62,30,0,0,1] = expr(1)
Edge[62,31,0,0,1] = expr(1)
Edge[62,32,0,0,1] = expr(1)
Edge[62,33,0,0,1] = expr(1)
Edge_Net[62,26,0,0,1,0:] = exprzeros(13)
Edge_Net[62,27,0,0,1,0:] = exprzeros(13)
Edge_Net[62,28,0,0,1,0:] = exprzeros(13)
Edge_Net[62,29,0,0,1,0:] = exprzeros(13)
Edge_Net[62,30,0,0,1,0:] = exprzeros(13)
Edge_Net[62,31,0,0,1,0:] = exprzeros(13)
Edge_Net[62,32,0,0,1,0:] = exprzeros(13)
Edge_Net[62,33,0,0,1,0:] = exprzeros(13)
Edge[66,26,0,0,1] = expr(1)
Edge[66,27,0,0,1] = expr(1)
Edge[66,28,0,0,1] = expr(1)
Edge[66,29,0,0,1] = expr(1)
Edge[66,30,0,0,1] = expr(1)
Edge[66,31,0,0,1] = expr(1)
Edge[66,32,0,0,1] = expr(1)
Edge[66,33,0,0,1] = expr(1)
Edge_Net[66,26,0,0,1,0:] = exprzeros(13)
Edge_Net[66,27,0,0,1,0:] = exprzeros(13)
Edge_Net[66,28,0,0,1,0:] = exprzeros(13)
Edge_Net[66,29,0,0,1,0:] = exprzeros(13)
Edge_Net[66,30,0,0,1,0:] = exprzeros(13)
Edge_Net[66,31,0,0,1,0:] = exprzeros(13)
Edge_Net[66,32,0,0,1,0:] = exprzeros(13)
Edge_Net[66,33,0,0,1,0:] = exprzeros(13)
Edge[62,25,1,1,1] = expr(0)
Edge[62,26,1,1,1] = expr(0)
Edge[62,27,1,1,1] = expr(0)
Edge[62,28,1,1,1] = expr(0)
Edge[62,29,1,1,1] = expr(0)
Edge[62,30,1,1,1] = expr(0)
Edge[62,31,1,1,1] = expr(0)
Edge[62,32,1,1,1] = expr(0)
Edge[62,33,1,1,1] = expr(0)
Edge[62,34,1,1,1] = expr(0)
Edge[62,35,1,1,1] = expr(0)
Edge[66,25,1,1,1] = expr(0)
Edge[66,26,1,1,1] = expr(0)
Edge[66,27,1,1,1] = expr(0)
Edge[66,28,1,1,1] = expr(0)
Edge[66,29,1,1,1] = expr(0)
Edge[66,30,1,1,1] = expr(0)
Edge[66,31,1,1,1] = expr(0)
Edge[66,32,1,1,1] = expr(0)
Edge[66,33,1,1,1] = expr(0)
Edge[66,34,1,1,1] = expr(0)
Edge[66,35,1,1,1] = expr(0)

# Net-9 subNet-0 Terminal[0] to Terminal[1]
# AIL1(26,26,1,6) ==> AIL1(26,26,28,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet9[26,1:7,0,0,1,0] = exprones(6)
Edge_Net_Subnet9[26,1:7,0,0,2,0] = exprones(6)
Edge_Net[26,1:7,0,0,1,8] = exprones(6)
for x in range(26,26+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 9
Edge_Net_Subnet9[26,28:34,0,0,1,0] = exprones(6)
Edge_Net_Subnet9[26,28:34,0,0,2,0] = exprones(6)
Edge_Net[26,28:34,0,0,1,8] = exprones(6)
for x in range(26,26+1):
  for y in range(28,33+1) :
    outLayout[x][y][0][0] = 9
# Net-11 subNet-0 Terminal[0] to Terminal[1]
# AIL1(42,42,1,6) ==> AIL1(42,42,28,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet11[42,1:7,0,0,1,0] = exprones(6)
Edge_Net_Subnet11[42,1:7,0,0,2,0] = exprones(6)
Edge_Net[42,1:7,0,0,1,10] = exprones(6)
for x in range(42,42+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 11
Edge_Net_Subnet11[42,28:34,0,0,1,0] = exprones(6)
Edge_Net_Subnet11[42,28:34,0,0,2,0] = exprones(6)
Edge_Net[42,28:34,0,0,1,10] = exprones(6)
for x in range(42,42+1):
  for y in range(28,33+1) :
    outLayout[x][y][0][0] = 11
# Net-12 subNet-0 Terminal[0] to Terminal[1]
# AIL1(54,54,1,12) ==> AIL1(54,54,22,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet12[54,1:13,0,0,1,0] = exprones(12)
Edge_Net_Subnet12[54,1:13,0,0,2,0] = exprones(12)
Edge_Net[54,1:13,0,0,1,11] = exprones(12)
for x in range(54,54+1):
  for y in range(1,12+1) :
    outLayout[x][y][0][0] = 12
Edge_Net_Subnet12[54,22:34,0,0,1,0] = exprones(12)
Edge_Net_Subnet12[54,22:34,0,0,2,0] = exprones(12)
Edge_Net[54,22:34,0,0,1,11] = exprones(12)
for x in range(54,54+1):
  for y in range(22,33+1) :
    outLayout[x][y][0][0] = 12
# Net-1 subNet-0 Terminal[0] to Terminal[1]
# AIL1(2,2,1,6) ==> AIL1(18,18,1,6)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet1[2,1:7,0,0,1,0] = exprones(6)
Edge_Net_Subnet1[2,1:7,0,0,2,0] = exprones(6)
Edge_Net[2,1:7,0,0,1,0] = exprones(6)
for x in range(2,2+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 1
Edge_Net_Subnet1[18,1:7,0,0,1,0] = exprones(6)
Edge_Net_Subnet1[18,1:7,0,0,2,0] = exprones(6)
Edge_Net[18,1:7,0,0,1,0] = exprones(6)
for x in range(18,18+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 1
# Net-3 subNet-0 Terminal[0] to Terminal[1]
# Poly(4,4,0,35) ==> Poly(8,8,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[4,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet3[4,0:36,0,0,2,0] = exprones(36)
Edge_Net[4,0:36,0,0,0,2] = exprones(36)
for x in range(4,4+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[8,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet3[8,0:36,0,0,2,0] = exprones(36)
Edge_Net[8,0:36,0,0,0,2] = exprones(36)
for x in range(8,8+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-1 Terminal[1] to Terminal[2]
# Poly(8,8,0,35) ==> Poly(8,8,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[8,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet3[8,0:36,0,0,2,1] = exprones(36)
Edge_Net[8,0:36,0,0,0,2] = exprones(36)
for x in range(8,8+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[8,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet3[8,0:36,0,0,2,1] = exprones(36)
Edge_Net[8,0:36,0,0,0,2] = exprones(36)
for x in range(8,8+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-2 Terminal[2] to Terminal[3]
# Poly(8,8,0,35) ==> Poly(12,12,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[8,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet3[8,0:36,0,0,2,2] = exprones(36)
Edge_Net[8,0:36,0,0,0,2] = exprones(36)
for x in range(8,8+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[12,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet3[12,0:36,0,0,2,2] = exprones(36)
Edge_Net[12,0:36,0,0,0,2] = exprones(36)
for x in range(12,12+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 3
# Net-2 subNet-0 Terminal[0] to Terminal[3]
# AIL1(10,10,1,6) ==> AIL1(2,2,28,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[10,1:7,0,0,1,0] = exprones(6)
Edge_Net_Subnet2[10,1:7,0,0,2,0] = exprones(6)
Edge_Net[10,1:7,0,0,1,1] = exprones(6)
for x in range(10,10+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[2,28:34,0,0,1,0] = exprones(6)
Edge_Net_Subnet2[2,28:34,0,0,2,0] = exprones(6)
Edge_Net[2,28:34,0,0,1,1] = exprones(6)
for x in range(2,2+1):
  for y in range(28,33+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-1 Terminal[0] to Terminal[1]
# AIL1(10,10,1,6) ==> Poly(44,44,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[10,1:7,0,0,1,1] = exprones(6)
Edge_Net_Subnet2[10,1:7,0,0,2,1] = exprones(6)
Edge_Net[10,1:7,0,0,1,1] = exprones(6)
for x in range(10,10+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[44,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet2[44,0:36,0,0,2,1] = exprones(36)
Edge_Net[44,0:36,0,0,0,1] = exprones(36)
for x in range(44,44+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-2 Terminal[1] to Terminal[4]
# Poly(44,44,0,35) ==> Poly(44,44,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[44,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet2[44,0:36,0,0,2,2] = exprones(36)
Edge_Net[44,0:36,0,0,0,1] = exprones(36)
for x in range(44,44+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[44,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet2[44,0:36,0,0,2,2] = exprones(36)
Edge_Net[44,0:36,0,0,0,1] = exprones(36)
for x in range(44,44+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-3 Terminal[1] to Terminal[2]
# Poly(44,44,0,35) ==> Poly(52,52,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[44,0:36,0,0,0,3] = exprones(36)
Edge_Net_Subnet2[44,0:36,0,0,2,3] = exprones(36)
Edge_Net[44,0:36,0,0,0,1] = exprones(36)
for x in range(44,44+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[52,0:36,0,0,0,3] = exprones(36)
Edge_Net_Subnet2[52,0:36,0,0,2,3] = exprones(36)
Edge_Net[52,0:36,0,0,0,1] = exprones(36)
for x in range(52,52+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-4 Terminal[2] to Terminal[5]
# Poly(52,52,0,35) ==> Poly(52,52,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[52,0:36,0,0,0,4] = exprones(36)
Edge_Net_Subnet2[52,0:36,0,0,2,4] = exprones(36)
Edge_Net[52,0:36,0,0,0,1] = exprones(36)
for x in range(52,52+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[52,0:36,0,0,0,4] = exprones(36)
Edge_Net_Subnet2[52,0:36,0,0,2,4] = exprones(36)
Edge_Net[52,0:36,0,0,0,1] = exprones(36)
for x in range(52,52+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-4 subNet-0 Terminal[0] to Terminal[2]
# Poly(12,12,0,35) ==> Poly(4,4,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet4[12,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet4[12,0:36,0,0,2,0] = exprones(36)
Edge_Net[12,0:36,0,0,0,3] = exprones(36)
for x in range(12,12+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 4
Edge_Net_Subnet4[4,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet4[4,0:36,0,0,2,0] = exprones(36)
Edge_Net[4,0:36,0,0,0,3] = exprones(36)
for x in range(4,4+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 4
# Net-4 subNet-1 Terminal[0] to Terminal[1]
# Poly(12,12,0,35) ==> AIL1(38,38,1,6)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet4[12,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet4[12,0:36,0,0,2,1] = exprones(36)
Edge_Net[12,0:36,0,0,0,3] = exprones(36)
for x in range(12,12+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 4
Edge_Net_Subnet4[38,1:7,0,0,1,1] = exprones(6)
Edge_Net_Subnet4[38,1:7,0,0,2,1] = exprones(6)
Edge_Net[38,1:7,0,0,1,3] = exprones(6)
for x in range(38,38+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 4
# Net-4 subNet-2 Terminal[1] to Terminal[3]
# AIL1(38,38,1,6) ==> AIL1(38,38,28,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet4[38,1:7,0,0,1,2] = exprones(6)
Edge_Net_Subnet4[38,1:7,0,0,2,2] = exprones(6)
Edge_Net[38,1:7,0,0,1,3] = exprones(6)
for x in range(38,38+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 4
Edge_Net_Subnet4[38,28:34,0,0,1,2] = exprones(6)
Edge_Net_Subnet4[38,28:34,0,0,2,2] = exprones(6)
Edge_Net[38,28:34,0,0,1,3] = exprones(6)
for x in range(38,38+1):
  for y in range(28,33+1) :
    outLayout[x][y][0][0] = 4
# Net-5 subNet-0 Terminal[0] to Terminal[2]
# Poly(16,16,0,35) ==> Poly(16,16,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet5[16,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet5[16,0:36,0,0,2,0] = exprones(36)
Edge_Net[16,0:36,0,0,0,4] = exprones(36)
for x in range(16,16+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 5
Edge_Net_Subnet5[16,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet5[16,0:36,0,0,2,0] = exprones(36)
Edge_Net[16,0:36,0,0,0,4] = exprones(36)
for x in range(16,16+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 5
# Net-5 subNet-1 Terminal[0] to Terminal[1]
# Poly(16,16,0,35) ==> AIL1(34,34,1,6)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet5[16,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet5[16,0:36,0,0,2,1] = exprones(36)
Edge_Net[16,0:36,0,0,0,4] = exprones(36)
for x in range(16,16+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 5
Edge_Net_Subnet5[34,1:7,0,0,1,1] = exprones(6)
Edge_Net_Subnet5[34,1:7,0,0,2,1] = exprones(6)
Edge_Net[34,1:7,0,0,1,4] = exprones(6)
for x in range(34,34+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 5
# Net-5 subNet-2 Terminal[1] to Terminal[3]
# AIL1(34,34,1,6) ==> AIL1(34,34,28,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet5[34,1:7,0,0,1,2] = exprones(6)
Edge_Net_Subnet5[34,1:7,0,0,2,2] = exprones(6)
Edge_Net[34,1:7,0,0,1,4] = exprones(6)
for x in range(34,34+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 5
Edge_Net_Subnet5[34,28:34,0,0,1,2] = exprones(6)
Edge_Net_Subnet5[34,28:34,0,0,2,2] = exprones(6)
Edge_Net[34,28:34,0,0,1,4] = exprones(6)
for x in range(34,34+1):
  for y in range(28,33+1) :
    outLayout[x][y][0][0] = 5
# Net-6 subNet-0 Terminal[0] to Terminal[4]
# Poly(20,20,0,35) ==> Poly(24,24,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet6[20,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet6[20,0:36,0,0,2,0] = exprones(36)
Edge_Net[20,0:36,0,0,0,5] = exprones(36)
for x in range(20,20+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
Edge_Net_Subnet6[24,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet6[24,0:36,0,0,2,0] = exprones(36)
Edge_Net[24,0:36,0,0,0,5] = exprones(36)
for x in range(24,24+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
# Net-6 subNet-1 Terminal[4] to Terminal[1]
# Poly(24,24,0,35) ==> Poly(36,36,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet6[24,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet6[24,0:36,0,0,2,1] = exprones(36)
Edge_Net[24,0:36,0,0,0,5] = exprones(36)
for x in range(24,24+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
Edge_Net_Subnet6[36,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet6[36,0:36,0,0,2,1] = exprones(36)
Edge_Net[36,0:36,0,0,0,5] = exprones(36)
for x in range(36,36+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
# Net-6 subNet-2 Terminal[1] to Terminal[5]
# Poly(36,36,0,35) ==> Poly(40,40,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet6[36,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet6[36,0:36,0,0,2,2] = exprones(36)
Edge_Net[36,0:36,0,0,0,5] = exprones(36)
for x in range(36,36+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
Edge_Net_Subnet6[40,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet6[40,0:36,0,0,2,2] = exprones(36)
Edge_Net[40,0:36,0,0,0,5] = exprones(36)
for x in range(40,40+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
# Net-6 subNet-3 Terminal[1] to Terminal[0]
# Poly(36,36,0,35) ==> Poly(20,20,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet6[36,0:36,0,0,0,3] = exprones(36)
Edge_Net_Subnet6[36,0:36,0,0,2,3] = exprones(36)
Edge_Net[36,0:36,0,0,0,5] = exprones(36)
for x in range(36,36+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
Edge_Net_Subnet6[20,0:36,0,0,0,3] = exprones(36)
Edge_Net_Subnet6[20,0:36,0,0,2,3] = exprones(36)
Edge_Net[20,0:36,0,0,0,5] = exprones(36)
for x in range(20,20+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
# Net-6 subNet-4 Terminal[5] to Terminal[6]
# Poly(40,40,0,35) ==> Poly(60,60,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet6[40,0:36,0,0,0,4] = exprones(36)
Edge_Net_Subnet6[40,0:36,0,0,2,4] = exprones(36)
Edge_Net[40,0:36,0,0,0,5] = exprones(36)
for x in range(40,40+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
Edge_Net_Subnet6[60,0:36,0,0,0,4] = exprones(36)
Edge_Net_Subnet6[60,0:36,0,0,2,4] = exprones(36)
Edge_Net[60,0:36,0,0,0,5] = exprones(36)
for x in range(60,60+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
# Net-6 subNet-5 Terminal[6] to Terminal[2]
# Poly(60,60,0,35) ==> Poly(60,60,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet6[60,0:36,0,0,0,5] = exprones(36)
Edge_Net_Subnet6[60,0:36,0,0,2,5] = exprones(36)
Edge_Net[60,0:36,0,0,0,5] = exprones(36)
for x in range(60,60+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
Edge_Net_Subnet6[60,0:36,0,0,0,5] = exprones(36)
Edge_Net_Subnet6[60,0:36,0,0,2,5] = exprones(36)
Edge_Net[60,0:36,0,0,0,5] = exprones(36)
for x in range(60,60+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
# Net-6 subNet-6 Terminal[6] to Terminal[7]
# Poly(60,60,0,35) ==> AIL1(66,66,26,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet6[60,0:36,0,0,0,6] = exprones(36)
Edge_Net_Subnet6[60,0:36,0,0,2,6] = exprones(36)
Edge_Net[60,0:36,0,0,0,5] = exprones(36)
for x in range(60,60+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 6
Edge_Net_Subnet6[66,26:34,0,0,1,6] = exprones(8)
Edge_Net_Subnet6[66,26:34,0,0,2,6] = exprones(8)
Edge_Net[66,26:34,0,0,1,5] = exprones(8)
for x in range(66,66+1):
  for y in range(26,33+1) :
    outLayout[x][y][0][0] = 6
# Net-8 subNet-0 Terminal[0] to Terminal[2]
# AIL1(22,22,1,6) ==> AIL1(22,22,28,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet8[22,1:7,0,0,1,0] = exprones(6)
Edge_Net_Subnet8[22,1:7,0,0,2,0] = exprones(6)
Edge_Net[22,1:7,0,0,1,7] = exprones(6)
for x in range(22,22+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 8
Edge_Net_Subnet8[22,28:34,0,0,1,0] = exprones(6)
Edge_Net_Subnet8[22,28:34,0,0,2,0] = exprones(6)
Edge_Net[22,28:34,0,0,1,7] = exprones(6)
for x in range(22,22+1):
  for y in range(28,33+1) :
    outLayout[x][y][0][0] = 8
# Net-8 subNet-1 Terminal[0] to Terminal[1]
# AIL1(22,22,1,6) ==> Poly(32,32,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet8[22,1:7,0,0,1,1] = exprones(6)
Edge_Net_Subnet8[22,1:7,0,0,2,1] = exprones(6)
Edge_Net[22,1:7,0,0,1,7] = exprones(6)
for x in range(22,22+1):
  for y in range(1,6+1) :
    outLayout[x][y][0][0] = 8
Edge_Net_Subnet8[32,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet8[32,0:36,0,0,2,1] = exprones(36)
Edge_Net[32,0:36,0,0,0,7] = exprones(36)
for x in range(32,32+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
# Net-8 subNet-2 Terminal[1] to Terminal[3]
# Poly(32,32,0,35) ==> Poly(32,32,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet8[32,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet8[32,0:36,0,0,2,2] = exprones(36)
Edge_Net[32,0:36,0,0,0,7] = exprones(36)
for x in range(32,32+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
Edge_Net_Subnet8[32,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet8[32,0:36,0,0,2,2] = exprones(36)
Edge_Net[32,0:36,0,0,0,7] = exprones(36)
for x in range(32,32+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 8
# Net-7 subNet-0 Terminal[0] to Terminal[3]
# Poly(24,24,0,35) ==> Poly(20,20,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet7[24,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet7[24,0:36,0,0,2,0] = exprones(36)
Edge_Net[24,0:36,0,0,0,6] = exprones(36)
for x in range(24,24+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 7
Edge_Net_Subnet7[20,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet7[20,0:36,0,0,2,0] = exprones(36)
Edge_Net[20,0:36,0,0,0,6] = exprones(36)
for x in range(20,20+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 7
# Net-7 subNet-1 Terminal[0] to Terminal[4]
# Poly(24,24,0,35) ==> Poly(36,36,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet7[24,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet7[24,0:36,0,0,2,1] = exprones(36)
Edge_Net[24,0:36,0,0,0,6] = exprones(36)
for x in range(24,24+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 7
Edge_Net_Subnet7[36,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet7[36,0:36,0,0,2,1] = exprones(36)
Edge_Net[36,0:36,0,0,0,6] = exprones(36)
for x in range(36,36+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 7
# Net-7 subNet-2 Terminal[4] to Terminal[1]
# Poly(36,36,0,35) ==> Poly(40,40,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet7[36,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet7[36,0:36,0,0,2,2] = exprones(36)
Edge_Net[36,0:36,0,0,0,6] = exprones(36)
for x in range(36,36+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 7
Edge_Net_Subnet7[40,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet7[40,0:36,0,0,2,2] = exprones(36)
Edge_Net[40,0:36,0,0,0,6] = exprones(36)
for x in range(40,40+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 7
# Net-7 subNet-3 Terminal[1] to Terminal[0]
# Poly(40,40,0,35) ==> Poly(24,24,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet7[40,0:36,0,0,0,3] = exprones(36)
Edge_Net_Subnet7[40,0:36,0,0,2,3] = exprones(36)
Edge_Net[40,0:36,0,0,0,6] = exprones(36)
for x in range(40,40+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 7
Edge_Net_Subnet7[24,0:36,0,0,0,3] = exprones(36)
Edge_Net_Subnet7[24,0:36,0,0,2,3] = exprones(36)
Edge_Net[24,0:36,0,0,0,6] = exprones(36)
for x in range(24,24+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 7
# Net-7 subNet-4 Terminal[1] to Terminal[2]
# Poly(40,40,0,35) ==> AIL1(58,58,1,10)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet7[40,0:36,0,0,0,4] = exprones(36)
Edge_Net_Subnet7[40,0:36,0,0,2,4] = exprones(36)
Edge_Net[40,0:36,0,0,0,6] = exprones(36)
for x in range(40,40+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 7
Edge_Net_Subnet7[58,1:11,0,0,1,4] = exprones(10)
Edge_Net_Subnet7[58,1:11,0,0,2,4] = exprones(10)
Edge_Net[58,1:11,0,0,1,6] = exprones(10)
for x in range(58,58+1):
  for y in range(1,10+1) :
    outLayout[x][y][0][0] = 7
# Net = 9 Subnet = 0 | Left -> Right [22,30] Top -> Bottom [0,35]
# Range R1(26,26,1,6)
# Range R2(26,26,28,33)
### Disable edges outside window
Edge_Net_Subnet9[0:22,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(28512)
Edge_Net_Subnet9[30:77+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(62208)

### Consistency Constraints
Net9_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,8]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(22,30+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net9_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet9[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,8])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(22,30+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net9_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet9[x,y,2,trend,0,0],Xor(Edge_Net_Subnet9[x,y,2,trend,1,0],Edge_Net_Subnet9[x,y,2,trend,2,0])),And(~Edge_Net_Subnet9[x,y,2,trend,0,0],~Edge_Net_Subnet9[x,y,2,trend,1,0],~Edge_Net_Subnet9[x,y,2,trend,2,0]))for x in range(22,30+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net9_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet9[x,y,3,1,0,0],Xor(Edge_Net_Subnet9[x,y,3,1,1,0],Edge_Net_Subnet9[x,y,3,1,2,0])),And(~Edge_Net_Subnet9[x,y,3,1,0,0],~Edge_Net_Subnet9[x,y,3,1,1,0],~Edge_Net_Subnet9[x,y,3,1,2,0]))for x in range(22,30+1)])for y in range(0,35+1)]).to_cnf()
Net9_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet9[x,y,1,trend,2,0],Xor(Edge_Net_Subnet9[x,y,1,trend,0,0],Edge_Net_Subnet9[x,y,1,trend,1,0])),And(~Edge_Net_Subnet9[x,y,1,trend,2,0],~Edge_Net_Subnet9[x,y,1,trend,0,0],~Edge_Net_Subnet9[x,y,1,trend,1,0]))for x in range(22,30+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net9_Subnet0_C6 = And(
1,1
).to_cnf()
Net9_Subnet0_C = And(Net9_Subnet0_C1, Net9_Subnet0_C2,Net9_Subnet0_C3_ME1_Mask,Net9_Subnet0_C4_MINT1_Mask,Net9_Subnet0_C5_AIL2GIL_Mask,Net9_Subnet0_C6,)
### Design Rules
Net9_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(22,30+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net9_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet9[x,y,1,1,1,0], ~Edge_Net_Subnet9[x-1,y,1,1,1,0]), And(Edge_Net_Subnet9[x+1,y,1,1,1,0], Edge_Net_Subnet9[x+2,y,1,1,1,0], Edge_Net_Subnet9[x+3,y,1,1,1,0], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet9[x,y,1,1,1,0], ~Edge_Net_Subnet9[x+1,y,1,1,1,0]), And(Edge_Net_Subnet9[x-1,y,1,1,1,0], Edge_Net_Subnet9[x-2,y,1,1,1,0], Edge_Net_Subnet9[x-3,y,1,1,1,0], ))for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net9_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net9_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet9[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(22,30+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet9[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(22,30+1)])for y in range(3,35+1)]),
	).to_cnf()
Net9_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,1,0,0,0]), And(Edge_Net_Subnet9[x,y+1,1,0,0,0], Edge_Net_Subnet9[x,y+2,1,0,0,0], Edge_Net_Subnet9[x,y+3,1,0,0,0], ))for x in range(22,30+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,1,0,0,0]), And(Edge_Net_Subnet9[x,y-1,1,0,0,0], Edge_Net_Subnet9[x,y-2,1,0,0,0], Edge_Net_Subnet9[x,y-3,1,0,0,0], ))for x in range(22,30+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,1,0,0,0], ~Edge_Net_Subnet9[x,y-1,1,0,0,0]), And(Edge_Net_Subnet9[x,y+1,1,0,0,0], Edge_Net_Subnet9[x,y+2,1,0,0,0], Edge_Net_Subnet9[x,y+3,1,0,0,0], ))for x in range(22,30+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,1,0,0,0], ~Edge_Net_Subnet9[x,y+1,1,0,0,0]), And(Edge_Net_Subnet9[x,y-1,1,0,0,0], Edge_Net_Subnet9[x,y-2,1,0,0,0], Edge_Net_Subnet9[x,y-3,1,0,0,0], ))for x in range(22,30+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net9_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(22,30+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(22,30+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(22,30+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(22,30+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(22,30+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(22,30+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net9_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet9[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet9[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	).to_cnf()
Net9_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet9[x,y,3,1,mask,0], ~Edge_Net_Subnet9[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet9[x+1,y,3,1,mask,0], Edge_Net_Subnet9[x+2,y,3,1,mask,0], Edge_Net_Subnet9[x+3,y,3,1,mask,0], Edge_Net_Subnet9[x+4,y,3,1,mask,0], Edge_Net_Subnet9[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet9[x,y,3,1,mask,0], ~Edge_Net_Subnet9[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet9[x-1,y,3,1,mask,0], Edge_Net_Subnet9[x-2,y,3,1,mask,0], Edge_Net_Subnet9[x-3,y,3,1,mask,0], Edge_Net_Subnet9[x-4,y,3,1,mask,0], Edge_Net_Subnet9[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	).to_cnf()
Net9_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet9[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet9[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(3,35+1)]),
	).to_cnf()
Net9_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net9_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet9[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(22,30+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet9[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(22,30+1)])for y in range(2,35+1)]),
	).to_cnf()
Net9_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net9_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet9[x,y,2,1,mask,0], ~Edge_Net_Subnet9[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet9[x+1,y,2,1,mask,0], Edge_Net_Subnet9[x+2,y,2,1,mask,0], Edge_Net_Subnet9[x+3,y,2,1,mask,0], Edge_Net_Subnet9[x+4,y,2,1,mask,0], Edge_Net_Subnet9[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet9[x,y,2,1,mask,0], ~Edge_Net_Subnet9[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet9[x-1,y,2,1,mask,0], Edge_Net_Subnet9[x-2,y,2,1,mask,0], Edge_Net_Subnet9[x-3,y,2,1,mask,0], Edge_Net_Subnet9[x-4,y,2,1,mask,0], Edge_Net_Subnet9[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet9[x,y,2,1,mask,0], And(Edge_Net_Subnet9[x-1,y,2,1,mask,0], Edge_Net_Subnet9[x-2,y,2,1,mask,0], Edge_Net_Subnet9[x-3,y,2,1,mask,0], Edge_Net_Subnet9[x-4,y,2,1,mask,0], Edge_Net_Subnet9[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(22,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet9[x,y,2,1,mask,0], And(Edge_Net_Subnet9[x+1,y,2,1,mask,0], Edge_Net_Subnet9[x+2,y,2,1,mask,0], Edge_Net_Subnet9[x+3,y,2,1,mask,0], Edge_Net_Subnet9[x+4,y,2,1,mask,0], Edge_Net_Subnet9[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(30-1,22)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,2,0,mask,0], ~Edge_Net_Subnet9[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet9[x,y+1,2,0,mask,0], Edge_Net_Subnet9[x,y+2,2,0,mask,0], Edge_Net_Subnet9[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,2,0,mask,0], ~Edge_Net_Subnet9[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet9[x,y-1,2,0,mask,0], Edge_Net_Subnet9[x,y-2,2,0,mask,0], Edge_Net_Subnet9[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet9[x,y,2,0,mask,0], And(Edge_Net_Subnet9[x,y+1,2,0,mask,0], Edge_Net_Subnet9[x,y+2,2,0,mask,0], Edge_Net_Subnet9[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet9[x,y,2,0,mask,0], And(Edge_Net_Subnet9[x,y-1,2,0,mask,0], Edge_Net_Subnet9[x,y-2,2,0,mask,0], Edge_Net_Subnet9[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(35,35+1)]),
	).to_cnf()
Net9_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net9_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net9_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(22,30+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(22,30+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net9_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet9[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net9_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet9[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(22,30+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet9[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(22,30+1)])for y in range(3,35+1)]),
	).to_cnf()
Net9_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet9[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet9[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(4,35+1)]),
	).to_cnf()
Net9_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet9[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet9[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	).to_cnf()
Net9_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet9[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet9[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	).to_cnf()
Net9_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet9[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet9[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net9_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet9[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet9[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net9_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet9[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet9[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(2,35+1)]),
	).to_cnf()
Net9_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet9[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet9[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(2,35+1)]),
	).to_cnf()
Net9_Subnet0_DR = And(Net9_Subnet0_DR_Trend, Net9_Subnet0_DR_GIL_HorMinWidth,Net9_Subnet0_DR_GIL_HorMinSpacing,Net9_Subnet0_DR_GIL_VerMinSpacing,Net9_Subnet0_DR_AIL2_VerMinWidth,Net9_Subnet0_DR_AIL2_VerMinSpacing,Net9_Subnet0_DR_VerAIL2_HorMinSpacing,Net9_Subnet0_DR_MINT1AB_HorMinWidth,Net9_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net9_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net9_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net9_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net9_Subnet0_DR_M1AB_MinWidth,Net9_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net9_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net9_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net9_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net9_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net9_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net9_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net9_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net9_Subnet0_DR_V0_HorMinSpacing,Net9_Subnet0_DR_V1_HorMinSpacing,Net9_Subnet0_DR_V0_VerMinSpacing,Net9_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net9_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet9,[26,1,0,0, 26,2,0,0, 26,3,0,0, 26,4,0,0, 26,5,0,0, 26,6,0,0, ],6,22,0,1,30,35,3,0),
	RConstraints.R1(Edge_Net_Subnet9,[26,28,0,0, 26,29,0,0, 26,30,0,0, 26,31,0,0, 26,32,0,0, 26,33,0,0, ],6,22,0,1,30,35,3,0),
	).to_cnf()
Net9_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet9,Edge,Edge_Net,[26,1,0, 26,2,0, 26,3,0, 26,4,0, 26,5,0, 26,6,0, 26,7,0, 26,28,0, 26,29,0, 26,30,0, 26,31,0, 26,32,0, 26,33,0, 26,34,0, ],14,22,0,0,30,35,3,0,8),
	)
Net9_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,8],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,7+1)])for x in range(22,30+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,8],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(9,12+1)])for x in range(22,30+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net9_Subnet0_R = And(Net9_Subnet0_R1,Net9_Subnet0_R2,Net9_Subnet0_R3,)
Net9_Subnet0_Formula = And(Net9_Subnet0_C,Net9_Subnet0_DR,Net9_Subnet0_R)
# Net = 11 Subnet = 0 | Left -> Right [38,46] Top -> Bottom [0,35]
# Range R1(42,42,1,6)
# Range R2(42,42,28,33)
### Disable edges outside window
Edge_Net_Subnet11[0:38,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(49248)
Edge_Net_Subnet11[46:77+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(41472)

### Consistency Constraints
Net11_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,10]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(38,46+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net11_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet11[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,10])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(38,46+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net11_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet11[x,y,2,trend,0,0],Xor(Edge_Net_Subnet11[x,y,2,trend,1,0],Edge_Net_Subnet11[x,y,2,trend,2,0])),And(~Edge_Net_Subnet11[x,y,2,trend,0,0],~Edge_Net_Subnet11[x,y,2,trend,1,0],~Edge_Net_Subnet11[x,y,2,trend,2,0]))for x in range(38,46+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net11_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet11[x,y,3,1,0,0],Xor(Edge_Net_Subnet11[x,y,3,1,1,0],Edge_Net_Subnet11[x,y,3,1,2,0])),And(~Edge_Net_Subnet11[x,y,3,1,0,0],~Edge_Net_Subnet11[x,y,3,1,1,0],~Edge_Net_Subnet11[x,y,3,1,2,0]))for x in range(38,46+1)])for y in range(0,35+1)]).to_cnf()
Net11_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet11[x,y,1,trend,2,0],Xor(Edge_Net_Subnet11[x,y,1,trend,0,0],Edge_Net_Subnet11[x,y,1,trend,1,0])),And(~Edge_Net_Subnet11[x,y,1,trend,2,0],~Edge_Net_Subnet11[x,y,1,trend,0,0],~Edge_Net_Subnet11[x,y,1,trend,1,0]))for x in range(38,46+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net11_Subnet0_C6 = And(
1,1
).to_cnf()
Net11_Subnet0_C = And(Net11_Subnet0_C1, Net11_Subnet0_C2,Net11_Subnet0_C3_ME1_Mask,Net11_Subnet0_C4_MINT1_Mask,Net11_Subnet0_C5_AIL2GIL_Mask,Net11_Subnet0_C6,)
### Design Rules
Net11_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(38,46+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net11_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet11[x,y,1,1,1,0], ~Edge_Net_Subnet11[x-1,y,1,1,1,0]), And(Edge_Net_Subnet11[x+1,y,1,1,1,0], Edge_Net_Subnet11[x+2,y,1,1,1,0], Edge_Net_Subnet11[x+3,y,1,1,1,0], ))for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet11[x,y,1,1,1,0], ~Edge_Net_Subnet11[x+1,y,1,1,1,0]), And(Edge_Net_Subnet11[x-1,y,1,1,1,0], Edge_Net_Subnet11[x-2,y,1,1,1,0], Edge_Net_Subnet11[x-3,y,1,1,1,0], ))for x in range(38,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net11_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(38,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net11_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet11[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(38,46+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet11[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(38,46+1)])for y in range(3,35+1)]),
	).to_cnf()
Net11_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,1,0,0,0]), And(Edge_Net_Subnet11[x,y+1,1,0,0,0], Edge_Net_Subnet11[x,y+2,1,0,0,0], Edge_Net_Subnet11[x,y+3,1,0,0,0], ))for x in range(38,46+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,1,0,0,0]), And(Edge_Net_Subnet11[x,y-1,1,0,0,0], Edge_Net_Subnet11[x,y-2,1,0,0,0], Edge_Net_Subnet11[x,y-3,1,0,0,0], ))for x in range(38,46+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,1,0,0,0], ~Edge_Net_Subnet11[x,y-1,1,0,0,0]), And(Edge_Net_Subnet11[x,y+1,1,0,0,0], Edge_Net_Subnet11[x,y+2,1,0,0,0], Edge_Net_Subnet11[x,y+3,1,0,0,0], ))for x in range(38,46+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,1,0,0,0], ~Edge_Net_Subnet11[x,y+1,1,0,0,0]), And(Edge_Net_Subnet11[x,y-1,1,0,0,0], Edge_Net_Subnet11[x,y-2,1,0,0,0], Edge_Net_Subnet11[x,y-3,1,0,0,0], ))for x in range(38,46+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net11_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(38,46+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(38,46+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(38,46+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(38,46+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(38,46+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(38,46+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net11_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet11[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet11[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(38,46+1)])for y in range(0,35+1)]),
	).to_cnf()
Net11_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet11[x,y,3,1,mask,0], ~Edge_Net_Subnet11[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet11[x+1,y,3,1,mask,0], Edge_Net_Subnet11[x+2,y,3,1,mask,0], Edge_Net_Subnet11[x+3,y,3,1,mask,0], Edge_Net_Subnet11[x+4,y,3,1,mask,0], Edge_Net_Subnet11[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet11[x,y,3,1,mask,0], ~Edge_Net_Subnet11[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet11[x-1,y,3,1,mask,0], Edge_Net_Subnet11[x-2,y,3,1,mask,0], Edge_Net_Subnet11[x-3,y,3,1,mask,0], Edge_Net_Subnet11[x-4,y,3,1,mask,0], Edge_Net_Subnet11[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,35+1)]),
	).to_cnf()
Net11_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet11[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet11[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(3,35+1)]),
	).to_cnf()
Net11_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net11_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet11[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(38,46+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet11[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(38,46+1)])for y in range(2,35+1)]),
	).to_cnf()
Net11_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(38,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net11_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet11[x,y,2,1,mask,0], ~Edge_Net_Subnet11[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet11[x+1,y,2,1,mask,0], Edge_Net_Subnet11[x+2,y,2,1,mask,0], Edge_Net_Subnet11[x+3,y,2,1,mask,0], Edge_Net_Subnet11[x+4,y,2,1,mask,0], Edge_Net_Subnet11[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet11[x,y,2,1,mask,0], ~Edge_Net_Subnet11[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet11[x-1,y,2,1,mask,0], Edge_Net_Subnet11[x-2,y,2,1,mask,0], Edge_Net_Subnet11[x-3,y,2,1,mask,0], Edge_Net_Subnet11[x-4,y,2,1,mask,0], Edge_Net_Subnet11[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet11[x,y,2,1,mask,0], And(Edge_Net_Subnet11[x-1,y,2,1,mask,0], Edge_Net_Subnet11[x-2,y,2,1,mask,0], Edge_Net_Subnet11[x-3,y,2,1,mask,0], Edge_Net_Subnet11[x-4,y,2,1,mask,0], Edge_Net_Subnet11[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(38,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet11[x,y,2,1,mask,0], And(Edge_Net_Subnet11[x+1,y,2,1,mask,0], Edge_Net_Subnet11[x+2,y,2,1,mask,0], Edge_Net_Subnet11[x+3,y,2,1,mask,0], Edge_Net_Subnet11[x+4,y,2,1,mask,0], Edge_Net_Subnet11[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(46-1,38)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,2,0,mask,0], ~Edge_Net_Subnet11[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet11[x,y+1,2,0,mask,0], Edge_Net_Subnet11[x,y+2,2,0,mask,0], Edge_Net_Subnet11[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,2,0,mask,0], ~Edge_Net_Subnet11[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet11[x,y-1,2,0,mask,0], Edge_Net_Subnet11[x,y-2,2,0,mask,0], Edge_Net_Subnet11[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet11[x,y,2,0,mask,0], And(Edge_Net_Subnet11[x,y+1,2,0,mask,0], Edge_Net_Subnet11[x,y+2,2,0,mask,0], Edge_Net_Subnet11[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet11[x,y,2,0,mask,0], And(Edge_Net_Subnet11[x,y-1,2,0,mask,0], Edge_Net_Subnet11[x,y-2,2,0,mask,0], Edge_Net_Subnet11[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(35,35+1)]),
	).to_cnf()
Net11_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(38,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net11_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net11_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(38,46+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(38,46+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net11_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet11[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net11_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet11[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(38,46+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet11[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(38,46+1)])for y in range(3,35+1)]),
	).to_cnf()
Net11_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet11[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet11[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(4,35+1)]),
	).to_cnf()
Net11_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet11[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet11[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(38,46+1)])for y in range(0,35+1)]),
	).to_cnf()
Net11_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet11[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet11[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(38,46+1)])for y in range(0,35+1)]),
	).to_cnf()
Net11_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet11[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet11[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(38,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net11_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet11[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(38,46+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet11[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(38,46+1)])for y in range(0,35+1)])
	).to_cnf()
Net11_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet11[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(38,46+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet11[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(38,46+1)])for y in range(2,35+1)]),
	).to_cnf()
Net11_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet11[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(38,46+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet11[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(38,46+1)])for y in range(2,35+1)]),
	).to_cnf()
Net11_Subnet0_DR = And(Net11_Subnet0_DR_Trend, Net11_Subnet0_DR_GIL_HorMinWidth,Net11_Subnet0_DR_GIL_HorMinSpacing,Net11_Subnet0_DR_GIL_VerMinSpacing,Net11_Subnet0_DR_AIL2_VerMinWidth,Net11_Subnet0_DR_AIL2_VerMinSpacing,Net11_Subnet0_DR_VerAIL2_HorMinSpacing,Net11_Subnet0_DR_MINT1AB_HorMinWidth,Net11_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net11_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net11_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net11_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net11_Subnet0_DR_M1AB_MinWidth,Net11_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net11_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net11_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net11_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net11_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net11_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net11_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net11_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net11_Subnet0_DR_V0_HorMinSpacing,Net11_Subnet0_DR_V1_HorMinSpacing,Net11_Subnet0_DR_V0_VerMinSpacing,Net11_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net11_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet11,[42,1,0,0, 42,2,0,0, 42,3,0,0, 42,4,0,0, 42,5,0,0, 42,6,0,0, ],6,38,0,1,46,35,3,0),
	RConstraints.R1(Edge_Net_Subnet11,[42,28,0,0, 42,29,0,0, 42,30,0,0, 42,31,0,0, 42,32,0,0, 42,33,0,0, ],6,38,0,1,46,35,3,0),
	).to_cnf()
Net11_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet11,Edge,Edge_Net,[42,1,0, 42,2,0, 42,3,0, 42,4,0, 42,5,0, 42,6,0, 42,7,0, 42,28,0, 42,29,0, 42,30,0, 42,31,0, 42,32,0, 42,33,0, 42,34,0, ],14,38,0,0,46,35,3,0,10),
	)
Net11_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,10],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,9+1)])for x in range(38,46+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,10],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(11,12+1)])for x in range(38,46+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net11_Subnet0_R = And(Net11_Subnet0_R1,Net11_Subnet0_R2,Net11_Subnet0_R3,)
Net11_Subnet0_Formula = And(Net11_Subnet0_C,Net11_Subnet0_DR,Net11_Subnet0_R)
# Net = 12 Subnet = 0 | Left -> Right [50,58] Top -> Bottom [0,35]
# Range R1(54,54,1,12)
# Range R2(54,54,22,33)
### Disable edges outside window
Edge_Net_Subnet12[0:50,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(64800)
Edge_Net_Subnet12[58:77+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(25920)

### Consistency Constraints
Net12_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,11]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(50,58+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net12_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet12[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,11])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(50,58+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net12_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet12[x,y,2,trend,0,0],Xor(Edge_Net_Subnet12[x,y,2,trend,1,0],Edge_Net_Subnet12[x,y,2,trend,2,0])),And(~Edge_Net_Subnet12[x,y,2,trend,0,0],~Edge_Net_Subnet12[x,y,2,trend,1,0],~Edge_Net_Subnet12[x,y,2,trend,2,0]))for x in range(50,58+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net12_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet12[x,y,3,1,0,0],Xor(Edge_Net_Subnet12[x,y,3,1,1,0],Edge_Net_Subnet12[x,y,3,1,2,0])),And(~Edge_Net_Subnet12[x,y,3,1,0,0],~Edge_Net_Subnet12[x,y,3,1,1,0],~Edge_Net_Subnet12[x,y,3,1,2,0]))for x in range(50,58+1)])for y in range(0,35+1)]).to_cnf()
Net12_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet12[x,y,1,trend,2,0],Xor(Edge_Net_Subnet12[x,y,1,trend,0,0],Edge_Net_Subnet12[x,y,1,trend,1,0])),And(~Edge_Net_Subnet12[x,y,1,trend,2,0],~Edge_Net_Subnet12[x,y,1,trend,0,0],~Edge_Net_Subnet12[x,y,1,trend,1,0]))for x in range(50,58+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net12_Subnet0_C6 = And(
1,1
).to_cnf()
Net12_Subnet0_C = And(Net12_Subnet0_C1, Net12_Subnet0_C2,Net12_Subnet0_C3_ME1_Mask,Net12_Subnet0_C4_MINT1_Mask,Net12_Subnet0_C5_AIL2GIL_Mask,Net12_Subnet0_C6,)
### Design Rules
Net12_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(50,58+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net12_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet12[x,y,1,1,1,0], ~Edge_Net_Subnet12[x-1,y,1,1,1,0]), And(Edge_Net_Subnet12[x+1,y,1,1,1,0], Edge_Net_Subnet12[x+2,y,1,1,1,0], Edge_Net_Subnet12[x+3,y,1,1,1,0], ))for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet12[x,y,1,1,1,0], ~Edge_Net_Subnet12[x+1,y,1,1,1,0]), And(Edge_Net_Subnet12[x-1,y,1,1,1,0], Edge_Net_Subnet12[x-2,y,1,1,1,0], Edge_Net_Subnet12[x-3,y,1,1,1,0], ))for x in range(50,58+1)])for y in range(0,35+1)])
	).to_cnf()
Net12_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(50,58+1)])for y in range(0,35+1)])
	).to_cnf()
Net12_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet12[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(50,58+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet12[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(50,58+1)])for y in range(3,35+1)]),
	).to_cnf()
Net12_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,1,0,0,0]), And(Edge_Net_Subnet12[x,y+1,1,0,0,0], Edge_Net_Subnet12[x,y+2,1,0,0,0], Edge_Net_Subnet12[x,y+3,1,0,0,0], ))for x in range(50,58+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,1,0,0,0]), And(Edge_Net_Subnet12[x,y-1,1,0,0,0], Edge_Net_Subnet12[x,y-2,1,0,0,0], Edge_Net_Subnet12[x,y-3,1,0,0,0], ))for x in range(50,58+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,1,0,0,0], ~Edge_Net_Subnet12[x,y-1,1,0,0,0]), And(Edge_Net_Subnet12[x,y+1,1,0,0,0], Edge_Net_Subnet12[x,y+2,1,0,0,0], Edge_Net_Subnet12[x,y+3,1,0,0,0], ))for x in range(50,58+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,1,0,0,0], ~Edge_Net_Subnet12[x,y+1,1,0,0,0]), And(Edge_Net_Subnet12[x,y-1,1,0,0,0], Edge_Net_Subnet12[x,y-2,1,0,0,0], Edge_Net_Subnet12[x,y-3,1,0,0,0], ))for x in range(50,58+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net12_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(50,58+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(50,58+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(50,58+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(50,58+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(50,58+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(50,58+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net12_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet12[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet12[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(50,58+1)])for y in range(0,35+1)]),
	).to_cnf()
Net12_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet12[x,y,3,1,mask,0], ~Edge_Net_Subnet12[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet12[x+1,y,3,1,mask,0], Edge_Net_Subnet12[x+2,y,3,1,mask,0], Edge_Net_Subnet12[x+3,y,3,1,mask,0], Edge_Net_Subnet12[x+4,y,3,1,mask,0], Edge_Net_Subnet12[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet12[x,y,3,1,mask,0], ~Edge_Net_Subnet12[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet12[x-1,y,3,1,mask,0], Edge_Net_Subnet12[x-2,y,3,1,mask,0], Edge_Net_Subnet12[x-3,y,3,1,mask,0], Edge_Net_Subnet12[x-4,y,3,1,mask,0], Edge_Net_Subnet12[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,35+1)]),
	).to_cnf()
Net12_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet12[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet12[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(3,35+1)]),
	).to_cnf()
Net12_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,35+1)])
	).to_cnf()
Net12_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet12[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(50,58+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet12[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(50,58+1)])for y in range(2,35+1)]),
	).to_cnf()
Net12_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(50,58+1)])for y in range(0,35+1)])
	).to_cnf()
Net12_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet12[x,y,2,1,mask,0], ~Edge_Net_Subnet12[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet12[x+1,y,2,1,mask,0], Edge_Net_Subnet12[x+2,y,2,1,mask,0], Edge_Net_Subnet12[x+3,y,2,1,mask,0], Edge_Net_Subnet12[x+4,y,2,1,mask,0], Edge_Net_Subnet12[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet12[x,y,2,1,mask,0], ~Edge_Net_Subnet12[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet12[x-1,y,2,1,mask,0], Edge_Net_Subnet12[x-2,y,2,1,mask,0], Edge_Net_Subnet12[x-3,y,2,1,mask,0], Edge_Net_Subnet12[x-4,y,2,1,mask,0], Edge_Net_Subnet12[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet12[x,y,2,1,mask,0], And(Edge_Net_Subnet12[x-1,y,2,1,mask,0], Edge_Net_Subnet12[x-2,y,2,1,mask,0], Edge_Net_Subnet12[x-3,y,2,1,mask,0], Edge_Net_Subnet12[x-4,y,2,1,mask,0], Edge_Net_Subnet12[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(50,50+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet12[x,y,2,1,mask,0], And(Edge_Net_Subnet12[x+1,y,2,1,mask,0], Edge_Net_Subnet12[x+2,y,2,1,mask,0], Edge_Net_Subnet12[x+3,y,2,1,mask,0], Edge_Net_Subnet12[x+4,y,2,1,mask,0], Edge_Net_Subnet12[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(58-1,50)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,2,0,mask,0], ~Edge_Net_Subnet12[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet12[x,y+1,2,0,mask,0], Edge_Net_Subnet12[x,y+2,2,0,mask,0], Edge_Net_Subnet12[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,2,0,mask,0], ~Edge_Net_Subnet12[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet12[x,y-1,2,0,mask,0], Edge_Net_Subnet12[x,y-2,2,0,mask,0], Edge_Net_Subnet12[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet12[x,y,2,0,mask,0], And(Edge_Net_Subnet12[x,y+1,2,0,mask,0], Edge_Net_Subnet12[x,y+2,2,0,mask,0], Edge_Net_Subnet12[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet12[x,y,2,0,mask,0], And(Edge_Net_Subnet12[x,y-1,2,0,mask,0], Edge_Net_Subnet12[x,y-2,2,0,mask,0], Edge_Net_Subnet12[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(35,35+1)]),
	).to_cnf()
Net12_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(50,58+1)])for y in range(0,35+1)])
	).to_cnf()
Net12_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,35+1)])
	).to_cnf()
Net12_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(50,58+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(50,58+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net12_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet12[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net12_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet12[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(50,58+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet12[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(50,58+1)])for y in range(3,35+1)]),
	).to_cnf()
Net12_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet12[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet12[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(4,35+1)]),
	).to_cnf()
Net12_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet12[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet12[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(50,58+1)])for y in range(0,35+1)]),
	).to_cnf()
Net12_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet12[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet12[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(50,58+1)])for y in range(0,35+1)]),
	).to_cnf()
Net12_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet12[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet12[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(50,58+1)])for y in range(0,35+1)])
	).to_cnf()
Net12_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet12[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(50,58+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet12[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(50,58+1)])for y in range(0,35+1)])
	).to_cnf()
Net12_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet12[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(50,58+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet12[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(50,58+1)])for y in range(2,35+1)]),
	).to_cnf()
Net12_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet12[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(50,58+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet12[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(50,58+1)])for y in range(2,35+1)]),
	).to_cnf()
Net12_Subnet0_DR = And(Net12_Subnet0_DR_Trend, Net12_Subnet0_DR_GIL_HorMinWidth,Net12_Subnet0_DR_GIL_HorMinSpacing,Net12_Subnet0_DR_GIL_VerMinSpacing,Net12_Subnet0_DR_AIL2_VerMinWidth,Net12_Subnet0_DR_AIL2_VerMinSpacing,Net12_Subnet0_DR_VerAIL2_HorMinSpacing,Net12_Subnet0_DR_MINT1AB_HorMinWidth,Net12_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net12_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net12_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net12_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net12_Subnet0_DR_M1AB_MinWidth,Net12_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net12_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net12_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net12_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net12_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net12_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net12_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net12_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net12_Subnet0_DR_V0_HorMinSpacing,Net12_Subnet0_DR_V1_HorMinSpacing,Net12_Subnet0_DR_V0_VerMinSpacing,Net12_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net12_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet12,[54,1,0,0, 54,2,0,0, 54,3,0,0, 54,4,0,0, 54,5,0,0, 54,6,0,0, 54,7,0,0, 54,8,0,0, 54,9,0,0, 54,10,0,0, 54,11,0,0, 54,12,0,0, ],12,50,0,1,58,35,3,0),
	RConstraints.R1(Edge_Net_Subnet12,[54,22,0,0, 54,23,0,0, 54,24,0,0, 54,25,0,0, 54,26,0,0, 54,27,0,0, 54,28,0,0, 54,29,0,0, 54,30,0,0, 54,31,0,0, 54,32,0,0, 54,33,0,0, ],12,50,0,1,58,35,3,0),
	).to_cnf()
Net12_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet12,Edge,Edge_Net,[54,1,0, 54,2,0, 54,3,0, 54,4,0, 54,5,0, 54,6,0, 54,7,0, 54,8,0, 54,9,0, 54,10,0, 54,11,0, 54,12,0, 54,13,0, 54,22,0, 54,23,0, 54,24,0, 54,25,0, 54,26,0, 54,27,0, 54,28,0, 54,29,0, 54,30,0, 54,31,0, 54,32,0, 54,33,0, 54,34,0, ],26,50,0,0,58,35,3,0,11),
	)
Net12_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,11],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,10+1)])for x in range(50,58+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,11],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(12,12+1)])for x in range(50,58+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net12_Subnet0_R = And(Net12_Subnet0_R1,Net12_Subnet0_R2,Net12_Subnet0_R3,)
Net12_Subnet0_Formula = And(Net12_Subnet0_C,Net12_Subnet0_DR,Net12_Subnet0_R)
# Net = 1 Subnet = 0 | Left -> Right [0,22] Top -> Bottom [0,10]
# Range R1(2,2,1,6)
# Range R2(18,18,1,6)
### Disable edges outside window
Edge_Net_Subnet1[0:22,10:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(20592)
Edge_Net_Subnet1[22:77+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(72576)

### Consistency Constraints
Net1_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,0]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,22+1)])for y in range(0,10+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet1[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,0])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,22+1)])for y in range(0,10+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,2,trend,0,0],Xor(Edge_Net_Subnet1[x,y,2,trend,1,0],Edge_Net_Subnet1[x,y,2,trend,2,0])),And(~Edge_Net_Subnet1[x,y,2,trend,0,0],~Edge_Net_Subnet1[x,y,2,trend,1,0],~Edge_Net_Subnet1[x,y,2,trend,2,0]))for x in range(0,22+1)])for y in range(0,10+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,3,1,0,0],Xor(Edge_Net_Subnet1[x,y,3,1,1,0],Edge_Net_Subnet1[x,y,3,1,2,0])),And(~Edge_Net_Subnet1[x,y,3,1,0,0],~Edge_Net_Subnet1[x,y,3,1,1,0],~Edge_Net_Subnet1[x,y,3,1,2,0]))for x in range(0,22+1)])for y in range(0,10+1)]).to_cnf()
Net1_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,1,trend,2,0],Xor(Edge_Net_Subnet1[x,y,1,trend,0,0],Edge_Net_Subnet1[x,y,1,trend,1,0])),And(~Edge_Net_Subnet1[x,y,1,trend,2,0],~Edge_Net_Subnet1[x,y,1,trend,0,0],~Edge_Net_Subnet1[x,y,1,trend,1,0]))for x in range(0,22+1)])for y in range(0,10+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet0_C6 = And(
1,1
).to_cnf()
Net1_Subnet0_C = And(Net1_Subnet0_C1, Net1_Subnet0_C2,Net1_Subnet0_C3_ME1_Mask,Net1_Subnet0_C4_MINT1_Mask,Net1_Subnet0_C5_AIL2GIL_Mask,Net1_Subnet0_C6,)
### Design Rules
Net1_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(0,22+1)])for y in range(0,10+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(0,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(0,22+1)])for y in range(0,10+1)])for mask in range(0,2+1)])
	).to_cnf()
Net1_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,0], ~Edge_Net_Subnet1[x-1,y,1,1,1,0]), And(Edge_Net_Subnet1[x+1,y,1,1,1,0], Edge_Net_Subnet1[x+2,y,1,1,1,0], Edge_Net_Subnet1[x+3,y,1,1,1,0], ))for x in range(1,22+1)])for y in range(0,10+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,0], ~Edge_Net_Subnet1[x+1,y,1,1,1,0]), And(Edge_Net_Subnet1[x-1,y,1,1,1,0], Edge_Net_Subnet1[x-2,y,1,1,1,0], Edge_Net_Subnet1[x-3,y,1,1,1,0], ))for x in range(3,22+1)])for y in range(0,10+1)])
	).to_cnf()
Net1_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,22+1)])for y in range(0,10+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(0,22+1)])for y in range(0,10+1)])
	).to_cnf()
Net1_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(0,22+1)])for y in range(0,10+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(0,22+1)])for y in range(3,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0]), And(Edge_Net_Subnet1[x,y+1,1,0,0,0], Edge_Net_Subnet1[x,y+2,1,0,0,0], Edge_Net_Subnet1[x,y+3,1,0,0,0], ))for x in range(0,22+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge_Net_Subnet1[x,y-1,1,0,0,0]), And(Edge_Net_Subnet1[x,y+1,1,0,0,0], Edge_Net_Subnet1[x,y+2,1,0,0,0], Edge_Net_Subnet1[x,y+3,1,0,0,0], ))for x in range(0,22+1)])for y in range(0+1,10+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge_Net_Subnet1[x,y+1,1,0,0,0]), And(Edge_Net_Subnet1[x,y-1,1,0,0,0], Edge_Net_Subnet1[x,y-2,1,0,0,0], Edge_Net_Subnet1[x,y-3,1,0,0,0], ))for x in range(0,22+1)])for y in range(0+3,10+1)])
	).to_cnf()
Net1_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(0,22+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(0,22+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(0,22+1)])for y in range(0+3,10+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(0,22+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net1_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(0,22+1)])for y in range(0,10+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,22+1)])for y in range(0,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,0], ~Edge_Net_Subnet1[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet1[x+1,y,3,1,mask,0], Edge_Net_Subnet1[x+2,y,3,1,mask,0], Edge_Net_Subnet1[x+3,y,3,1,mask,0], Edge_Net_Subnet1[x+4,y,3,1,mask,0], Edge_Net_Subnet1[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(1,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,0], ~Edge_Net_Subnet1[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet1[x-1,y,3,1,mask,0], Edge_Net_Subnet1[x-2,y,3,1,mask,0], Edge_Net_Subnet1[x-3,y,3,1,mask,0], Edge_Net_Subnet1[x-4,y,3,1,mask,0], Edge_Net_Subnet1[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,0], And(Edge_Net_Subnet1[x+1,y,3,1,mask,0], Edge_Net_Subnet1[x+2,y,3,1,mask,0], Edge_Net_Subnet1[x+3,y,3,1,mask,0], Edge_Net_Subnet1[x+4,y,3,1,mask,0], Edge_Net_Subnet1[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(0, 0+1)])for y in range(0,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(3,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(0,10+1)])
	).to_cnf()
Net1_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(0,22+1)])for y in range(0,10+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(0,22+1)])for y in range(2,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,22+1)])for y in range(0,10+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(0,22+1)])for y in range(0,10+1)])
	).to_cnf()
Net1_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,0], ~Edge_Net_Subnet1[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet1[x+1,y,2,1,mask,0], Edge_Net_Subnet1[x+2,y,2,1,mask,0], Edge_Net_Subnet1[x+3,y,2,1,mask,0], Edge_Net_Subnet1[x+4,y,2,1,mask,0], Edge_Net_Subnet1[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(1,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,0], ~Edge_Net_Subnet1[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet1[x-1,y,2,1,mask,0], Edge_Net_Subnet1[x-2,y,2,1,mask,0], Edge_Net_Subnet1[x-3,y,2,1,mask,0], Edge_Net_Subnet1[x-4,y,2,1,mask,0], Edge_Net_Subnet1[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,0], And(Edge_Net_Subnet1[x-1,y,2,1,mask,0], Edge_Net_Subnet1[x-2,y,2,1,mask,0], Edge_Net_Subnet1[x-3,y,2,1,mask,0], Edge_Net_Subnet1[x-4,y,2,1,mask,0], Edge_Net_Subnet1[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(0,0+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,0], And(Edge_Net_Subnet1[x+1,y,2,1,mask,0], Edge_Net_Subnet1[x+2,y,2,1,mask,0], Edge_Net_Subnet1[x+3,y,2,1,mask,0], Edge_Net_Subnet1[x+4,y,2,1,mask,0], Edge_Net_Subnet1[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(22-1,0)])for y in range(0,10+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,0], ~Edge_Net_Subnet1[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet1[x,y+1,2,0,mask,0], Edge_Net_Subnet1[x,y+2,2,0,mask,0], Edge_Net_Subnet1[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(0+1,10+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,0], ~Edge_Net_Subnet1[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet1[x,y-1,2,0,mask,0], Edge_Net_Subnet1[x,y-2,2,0,mask,0], Edge_Net_Subnet1[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(0+3,10+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,0], And(Edge_Net_Subnet1[x,y+1,2,0,mask,0], Edge_Net_Subnet1[x,y+2,2,0,mask,0], Edge_Net_Subnet1[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,0], And(Edge_Net_Subnet1[x,y-1,2,0,mask,0], Edge_Net_Subnet1[x,y-2,2,0,mask,0], Edge_Net_Subnet1[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(10,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,22+1)])for y in range(0,10+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(0,22+1)])for y in range(0,10+1)])
	).to_cnf()
Net1_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(0,10+1)])
	).to_cnf()
Net1_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(0,22+1)])for y in range(2,10+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(0,22+1)])for y in range(0,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(4,10+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(0,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(0,22+1)])for y in range(0,10+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(0,22+1)])for y in range(3,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(4,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(0,22+1)])for y in range(0,10+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,22+1)])for y in range(0,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,22+1)])for y in range(0,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,22+1)])for y in range(0,10+1)])
	).to_cnf()
Net1_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,22+1)])for y in range(0,10+1)])
	).to_cnf()
Net1_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,22+1)])for y in range(2,10+1)]),
	).to_cnf()
Net1_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,22+1)])for y in range(0,10+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,22+1)])for y in range(2,10+1)]),
	).to_cnf()
Net1_Subnet0_DR = And(Net1_Subnet0_DR_Trend, Net1_Subnet0_DR_GIL_HorMinWidth,Net1_Subnet0_DR_GIL_HorMinSpacing,Net1_Subnet0_DR_GIL_VerMinSpacing,Net1_Subnet0_DR_AIL2_VerMinWidth,Net1_Subnet0_DR_AIL2_VerMinSpacing,Net1_Subnet0_DR_VerAIL2_HorMinSpacing,Net1_Subnet0_DR_MINT1AB_HorMinWidth,Net1_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net1_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net1_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net1_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net1_Subnet0_DR_M1AB_MinWidth,Net1_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net1_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net1_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net1_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net1_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net1_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net1_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net1_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net1_Subnet0_DR_V0_HorMinSpacing,Net1_Subnet0_DR_V1_HorMinSpacing,Net1_Subnet0_DR_V0_VerMinSpacing,Net1_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net1_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet1,[2,1,0,0, 2,2,0,0, 2,3,0,0, 2,4,0,0, 2,5,0,0, 2,6,0,0, ],6,0,0,1,22,10,3,0),
	RConstraints.R1(Edge_Net_Subnet1,[18,1,0,0, 18,2,0,0, 18,3,0,0, 18,4,0,0, 18,5,0,0, 18,6,0,0, ],6,0,0,1,22,10,3,0),
	).to_cnf()
Net1_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet1,Edge,Edge_Net,[2,1,0, 2,2,0, 2,3,0, 2,4,0, 2,5,0, 2,6,0, 2,7,0, 18,1,0, 18,2,0, 18,3,0, 18,4,0, 18,5,0, 18,6,0, 18,7,0, ],14,0,0,0,22,10,3,0,0),
	)
Net1_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,0],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(1,12+1)])for x in range(0,22+1)])for y in range(0,10+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	).to_cnf()
Net1_Subnet0_R = And(Net1_Subnet0_R1,Net1_Subnet0_R2,Net1_Subnet0_R3,)
Net1_Subnet0_Formula = And(Net1_Subnet0_C,Net1_Subnet0_DR,Net1_Subnet0_R)
# Net = 3 Subnet = 0 | Left -> Right [0,12] Top -> Bottom [0,35]
# Range R1(4,4,0,35)
# Range R2(8,8,0,35)
### Disable edges outside window
Edge_Net_Subnet3[12:77+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(85536)

### Consistency Constraints
Net3_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,0],Xor(Edge_Net_Subnet3[x,y,2,trend,1,0],Edge_Net_Subnet3[x,y,2,trend,2,0])),And(~Edge_Net_Subnet3[x,y,2,trend,0,0],~Edge_Net_Subnet3[x,y,2,trend,1,0],~Edge_Net_Subnet3[x,y,2,trend,2,0]))for x in range(0,12+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,0],Xor(Edge_Net_Subnet3[x,y,3,1,1,0],Edge_Net_Subnet3[x,y,3,1,2,0])),And(~Edge_Net_Subnet3[x,y,3,1,0,0],~Edge_Net_Subnet3[x,y,3,1,1,0],~Edge_Net_Subnet3[x,y,3,1,2,0]))for x in range(0,12+1)])for y in range(0,35+1)]).to_cnf()
Net3_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,0],Xor(Edge_Net_Subnet3[x,y,1,trend,0,0],Edge_Net_Subnet3[x,y,1,trend,1,0])),And(~Edge_Net_Subnet3[x,y,1,trend,2,0],~Edge_Net_Subnet3[x,y,1,trend,0,0],~Edge_Net_Subnet3[x,y,1,trend,1,0]))for x in range(0,12+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet0_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,0], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0+1,3)]))for trend in range(0,1+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,0], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0+1,3)]))for trend in range(0,1+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet0_C = And(Net3_Subnet0_C1, Net3_Subnet0_C2,Net3_Subnet0_C3_ME1_Mask,Net3_Subnet0_C4_MINT1_Mask,Net3_Subnet0_C5_AIL2GIL_Mask,Net3_Subnet0_C6,)
### Design Rules
Net3_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(0,12+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge_Net_Subnet3[x-1,y,1,1,1,0]), And(Edge_Net_Subnet3[x+1,y,1,1,1,0], Edge_Net_Subnet3[x+2,y,1,1,1,0], Edge_Net_Subnet3[x+3,y,1,1,1,0], ))for x in range(1,12+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge_Net_Subnet3[x+1,y,1,1,1,0]), And(Edge_Net_Subnet3[x-1,y,1,1,1,0], Edge_Net_Subnet3[x-2,y,1,1,1,0], Edge_Net_Subnet3[x-3,y,1,1,1,0], ))for x in range(3,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(0,12+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(0,12+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0]), And(Edge_Net_Subnet3[x,y+1,1,0,0,0], Edge_Net_Subnet3[x,y+2,1,0,0,0], Edge_Net_Subnet3[x,y+3,1,0,0,0], ))for x in range(0,12+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0]), And(Edge_Net_Subnet3[x,y-1,1,0,0,0], Edge_Net_Subnet3[x,y-2,1,0,0,0], Edge_Net_Subnet3[x,y-3,1,0,0,0], ))for x in range(0,12+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge_Net_Subnet3[x,y-1,1,0,0,0]), And(Edge_Net_Subnet3[x,y+1,1,0,0,0], Edge_Net_Subnet3[x,y+2,1,0,0,0], Edge_Net_Subnet3[x,y+3,1,0,0,0], ))for x in range(0,12+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge_Net_Subnet3[x,y+1,1,0,0,0]), And(Edge_Net_Subnet3[x,y-1,1,0,0,0], Edge_Net_Subnet3[x,y-2,1,0,0,0], Edge_Net_Subnet3[x,y-3,1,0,0,0], ))for x in range(0,12+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net3_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(0,12+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(0,12+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(0,12+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(0,12+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(0,12+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(0,12+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net3_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge_Net_Subnet3[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,0], Edge_Net_Subnet3[x+2,y,3,1,mask,0], Edge_Net_Subnet3[x+3,y,3,1,mask,0], Edge_Net_Subnet3[x+4,y,3,1,mask,0], Edge_Net_Subnet3[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(1,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge_Net_Subnet3[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,0], Edge_Net_Subnet3[x-2,y,3,1,mask,0], Edge_Net_Subnet3[x-3,y,3,1,mask,0], Edge_Net_Subnet3[x-4,y,3,1,mask,0], Edge_Net_Subnet3[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,0], And(Edge_Net_Subnet3[x+1,y,3,1,mask,0], Edge_Net_Subnet3[x+2,y,3,1,mask,0], Edge_Net_Subnet3[x+3,y,3,1,mask,0], Edge_Net_Subnet3[x+4,y,3,1,mask,0], Edge_Net_Subnet3[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(0, 0+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(0,12+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(0,12+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge_Net_Subnet3[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,0], Edge_Net_Subnet3[x+2,y,2,1,mask,0], Edge_Net_Subnet3[x+3,y,2,1,mask,0], Edge_Net_Subnet3[x+4,y,2,1,mask,0], Edge_Net_Subnet3[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(1,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge_Net_Subnet3[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,0], Edge_Net_Subnet3[x-2,y,2,1,mask,0], Edge_Net_Subnet3[x-3,y,2,1,mask,0], Edge_Net_Subnet3[x-4,y,2,1,mask,0], Edge_Net_Subnet3[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(Edge_Net_Subnet3[x-1,y,2,1,mask,0], Edge_Net_Subnet3[x-2,y,2,1,mask,0], Edge_Net_Subnet3[x-3,y,2,1,mask,0], Edge_Net_Subnet3[x-4,y,2,1,mask,0], Edge_Net_Subnet3[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(0,0+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(Edge_Net_Subnet3[x+1,y,2,1,mask,0], Edge_Net_Subnet3[x+2,y,2,1,mask,0], Edge_Net_Subnet3[x+3,y,2,1,mask,0], Edge_Net_Subnet3[x+4,y,2,1,mask,0], Edge_Net_Subnet3[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(12-1,0)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge_Net_Subnet3[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,0], Edge_Net_Subnet3[x,y+2,2,0,mask,0], Edge_Net_Subnet3[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge_Net_Subnet3[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,0], Edge_Net_Subnet3[x,y-2,2,0,mask,0], Edge_Net_Subnet3[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,0], And(Edge_Net_Subnet3[x,y+1,2,0,mask,0], Edge_Net_Subnet3[x,y+2,2,0,mask,0], Edge_Net_Subnet3[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,0], And(Edge_Net_Subnet3[x,y-1,2,0,mask,0], Edge_Net_Subnet3[x,y-2,2,0,mask,0], Edge_Net_Subnet3[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(0,12+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(0,12+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net3_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net3_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(0,12+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(0,12+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(4,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,12+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,12+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,12+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet0_DR = And(Net3_Subnet0_DR_Trend, Net3_Subnet0_DR_GIL_HorMinWidth,Net3_Subnet0_DR_GIL_HorMinSpacing,Net3_Subnet0_DR_GIL_VerMinSpacing,Net3_Subnet0_DR_AIL2_VerMinWidth,Net3_Subnet0_DR_AIL2_VerMinSpacing,Net3_Subnet0_DR_VerAIL2_HorMinSpacing,Net3_Subnet0_DR_MINT1AB_HorMinWidth,Net3_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet0_DR_M1AB_MinWidth,Net3_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet0_DR_V0_HorMinSpacing,Net3_Subnet0_DR_V1_HorMinSpacing,Net3_Subnet0_DR_V0_VerMinSpacing,Net3_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[4,0,0,0, 4,1,0,0, 4,2,0,0, 4,3,0,0, 4,4,0,0, 4,5,0,0, 4,6,0,0, 4,7,0,0, 4,8,0,0, 4,9,0,0, 4,10,0,0, 4,11,0,0, 4,12,0,0, 4,13,0,0, 4,14,0,0, 4,15,0,0, 4,16,0,0, 4,17,0,0, 4,18,0,0, 4,19,0,0, 4,20,0,0, 4,21,0,0, 4,22,0,0, 4,23,0,0, 4,24,0,0, 4,25,0,0, 4,26,0,0, 4,27,0,0, 4,28,0,0, 4,29,0,0, 4,30,0,0, 4,31,0,0, 4,32,0,0, 4,33,0,0, 4,34,0,0, 4,35,0,0, ],36,0,0,1,12,35,3,0),
	RConstraints.R1(Edge_Net_Subnet3,[8,0,0,0, 8,1,0,0, 8,2,0,0, 8,3,0,0, 8,4,0,0, 8,5,0,0, 8,6,0,0, 8,7,0,0, 8,8,0,0, 8,9,0,0, 8,10,0,0, 8,11,0,0, 8,12,0,0, 8,13,0,0, 8,14,0,0, 8,15,0,0, 8,16,0,0, 8,17,0,0, 8,18,0,0, 8,19,0,0, 8,20,0,0, 8,21,0,0, 8,22,0,0, 8,23,0,0, 8,24,0,0, 8,25,0,0, 8,26,0,0, 8,27,0,0, 8,28,0,0, 8,29,0,0, 8,30,0,0, 8,31,0,0, 8,32,0,0, 8,33,0,0, 8,34,0,0, 8,35,0,0, ],36,0,0,1,12,35,3,0),
	).to_cnf()
Net3_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[4,0,0, 4,1,0, 4,2,0, 4,3,0, 4,4,0, 4,5,0, 4,6,0, 4,7,0, 4,8,0, 4,9,0, 4,10,0, 4,11,0, 4,12,0, 4,13,0, 4,14,0, 4,15,0, 4,16,0, 4,17,0, 4,18,0, 4,19,0, 4,20,0, 4,21,0, 4,22,0, 4,23,0, 4,24,0, 4,25,0, 4,26,0, 4,27,0, 4,28,0, 4,29,0, 4,30,0, 4,31,0, 4,32,0, 4,33,0, 4,34,0, 4,35,0, 8,0,0, 8,1,0, 8,2,0, 8,3,0, 8,4,0, 8,5,0, 8,6,0, 8,7,0, 8,8,0, 8,9,0, 8,10,0, 8,11,0, 8,12,0, 8,13,0, 8,14,0, 8,15,0, 8,16,0, 8,17,0, 8,18,0, 8,19,0, 8,20,0, 8,21,0, 8,22,0, 8,23,0, 8,24,0, 8,25,0, 8,26,0, 8,27,0, 8,28,0, 8,29,0, 8,30,0, 8,31,0, 8,32,0, 8,33,0, 8,34,0, 8,35,0, ],72,0,0,0,12,35,3,0,2),
	)
Net3_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,12+1)])for x in range(0,12+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet0_R = And(Net3_Subnet0_R1,Net3_Subnet0_R2,Net3_Subnet0_R3,)
Net3_Subnet0_Formula = And(Net3_Subnet0_C,Net3_Subnet0_DR,Net3_Subnet0_R)
# Net = 3 Subnet = 2 | Left -> Right [4,16] Top -> Bottom [0,35]
# Range R1(8,8,0,35)
# Range R2(12,12,0,35)
### Disable edges outside window
Edge_Net_Subnet3[0:4,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(5184)
Edge_Net_Subnet3[16:77+1,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(80352)

### Consistency Constraints
Net3_Subnet2_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet2_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,2]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet2_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,2],Xor(Edge_Net_Subnet3[x,y,2,trend,1,2],Edge_Net_Subnet3[x,y,2,trend,2,2])),And(~Edge_Net_Subnet3[x,y,2,trend,0,2],~Edge_Net_Subnet3[x,y,2,trend,1,2],~Edge_Net_Subnet3[x,y,2,trend,2,2]))for x in range(4,16+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet2_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,2],Xor(Edge_Net_Subnet3[x,y,3,1,1,2],Edge_Net_Subnet3[x,y,3,1,2,2])),And(~Edge_Net_Subnet3[x,y,3,1,0,2],~Edge_Net_Subnet3[x,y,3,1,1,2],~Edge_Net_Subnet3[x,y,3,1,2,2]))for x in range(4,16+1)])for y in range(0,35+1)]).to_cnf()
Net3_Subnet2_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,2],Xor(Edge_Net_Subnet3[x,y,1,trend,0,2],Edge_Net_Subnet3[x,y,1,trend,1,2])),And(~Edge_Net_Subnet3[x,y,1,trend,2,2],~Edge_Net_Subnet3[x,y,1,trend,0,2],~Edge_Net_Subnet3[x,y,1,trend,1,2]))for x in range(4,16+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet2_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet2_C = And(Net3_Subnet2_C1, Net3_Subnet2_C2,Net3_Subnet2_C3_ME1_Mask,Net3_Subnet2_C4_MINT1_Mask,Net3_Subnet2_C5_AIL2GIL_Mask,Net3_Subnet2_C6,)
### Design Rules
Net3_Subnet2_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(4,16+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet2_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,2], ~Edge_Net_Subnet3[x-1,y,1,1,1,2]), And(Edge_Net_Subnet3[x+1,y,1,1,1,2], Edge_Net_Subnet3[x+2,y,1,1,1,2], Edge_Net_Subnet3[x+3,y,1,1,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,2], ~Edge_Net_Subnet3[x+1,y,1,1,1,2]), And(Edge_Net_Subnet3[x-1,y,1,1,1,2], Edge_Net_Subnet3[x-2,y,1,1,1,2], Edge_Net_Subnet3[x-3,y,1,1,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,2], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,2], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,2], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(4,16+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,2], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(4,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2]), And(Edge_Net_Subnet3[x,y+1,1,0,0,2], Edge_Net_Subnet3[x,y+2,1,0,0,2], Edge_Net_Subnet3[x,y+3,1,0,0,2], ))for x in range(4,16+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2]), And(Edge_Net_Subnet3[x,y-1,1,0,0,2], Edge_Net_Subnet3[x,y-2,1,0,0,2], Edge_Net_Subnet3[x,y-3,1,0,0,2], ))for x in range(4,16+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge_Net_Subnet3[x,y-1,1,0,0,2]), And(Edge_Net_Subnet3[x,y+1,1,0,0,2], Edge_Net_Subnet3[x,y+2,1,0,0,2], Edge_Net_Subnet3[x,y+3,1,0,0,2], ))for x in range(4,16+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge_Net_Subnet3[x,y+1,1,0,0,2]), And(Edge_Net_Subnet3[x,y-1,1,0,0,2], Edge_Net_Subnet3[x,y-2,1,0,0,2], Edge_Net_Subnet3[x,y-3,1,0,0,2], ))for x in range(4,16+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net3_Subnet2_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(4,16+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(4,16+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(4,16+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(4,16+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(4,16+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(4,16+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net3_Subnet2_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,2], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,2], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,2], ~Edge_Net_Subnet3[x-1,y,3,1,mask,2]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,2], Edge_Net_Subnet3[x+2,y,3,1,mask,2], Edge_Net_Subnet3[x+3,y,3,1,mask,2], Edge_Net_Subnet3[x+4,y,3,1,mask,2], Edge_Net_Subnet3[x+5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,2], ~Edge_Net_Subnet3[x+1,y,3,1,mask,2]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,2], Edge_Net_Subnet3[x-2,y,3,1,mask,2], Edge_Net_Subnet3[x-3,y,3,1,mask,2], Edge_Net_Subnet3[x-4,y,3,1,mask,2], Edge_Net_Subnet3[x-5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,2], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,2], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,2], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,2], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,2], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(4,16+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,2], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(4,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,2], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,2], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,2], ~Edge_Net_Subnet3[x-1,y,2,1,mask,2]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,2], Edge_Net_Subnet3[x+2,y,2,1,mask,2], Edge_Net_Subnet3[x+3,y,2,1,mask,2], Edge_Net_Subnet3[x+4,y,2,1,mask,2], Edge_Net_Subnet3[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,2], ~Edge_Net_Subnet3[x+1,y,2,1,mask,2]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,2], Edge_Net_Subnet3[x-2,y,2,1,mask,2], Edge_Net_Subnet3[x-3,y,2,1,mask,2], Edge_Net_Subnet3[x-4,y,2,1,mask,2], Edge_Net_Subnet3[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,2], And(Edge_Net_Subnet3[x-1,y,2,1,mask,2], Edge_Net_Subnet3[x-2,y,2,1,mask,2], Edge_Net_Subnet3[x-3,y,2,1,mask,2], Edge_Net_Subnet3[x-4,y,2,1,mask,2], Edge_Net_Subnet3[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(4,4+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,2], And(Edge_Net_Subnet3[x+1,y,2,1,mask,2], Edge_Net_Subnet3[x+2,y,2,1,mask,2], Edge_Net_Subnet3[x+3,y,2,1,mask,2], Edge_Net_Subnet3[x+4,y,2,1,mask,2], Edge_Net_Subnet3[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(16-1,4)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,2], ~Edge_Net_Subnet3[x,y-1,2,0,mask,2]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,2], Edge_Net_Subnet3[x,y+2,2,0,mask,2], Edge_Net_Subnet3[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,2], ~Edge_Net_Subnet3[x,y+1,2,0,mask,2]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,2], Edge_Net_Subnet3[x,y-2,2,0,mask,2], Edge_Net_Subnet3[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,2], And(Edge_Net_Subnet3[x,y+1,2,0,mask,2], Edge_Net_Subnet3[x,y+2,2,0,mask,2], Edge_Net_Subnet3[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,2], And(Edge_Net_Subnet3[x,y-1,2,0,mask,2], Edge_Net_Subnet3[x,y-2,2,0,mask,2], Edge_Net_Subnet3[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,2], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,2], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,2], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,2], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,2], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(4,16+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,2], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(4,16+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net3_Subnet2_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,2], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,2], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net3_Subnet2_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,2], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(4,16+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,2], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(4,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,2], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,2], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(4,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,2], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,2], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(4,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,2], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,2], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,2], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,2], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,2], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,2], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,2], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,2], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,2], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,2], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(4,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet2_DR = And(Net3_Subnet2_DR_Trend, Net3_Subnet2_DR_GIL_HorMinWidth,Net3_Subnet2_DR_GIL_HorMinSpacing,Net3_Subnet2_DR_GIL_VerMinSpacing,Net3_Subnet2_DR_AIL2_VerMinWidth,Net3_Subnet2_DR_AIL2_VerMinSpacing,Net3_Subnet2_DR_VerAIL2_HorMinSpacing,Net3_Subnet2_DR_MINT1AB_HorMinWidth,Net3_Subnet2_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet2_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet2_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet2_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet2_DR_M1AB_MinWidth,Net3_Subnet2_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet2_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet2_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet2_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet2_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet2_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet2_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet2_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet2_DR_V0_HorMinSpacing,Net3_Subnet2_DR_V1_HorMinSpacing,Net3_Subnet2_DR_V0_VerMinSpacing,Net3_Subnet2_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet2_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[8,0,0,0, 8,1,0,0, 8,2,0,0, 8,3,0,0, 8,4,0,0, 8,5,0,0, 8,6,0,0, 8,7,0,0, 8,8,0,0, 8,9,0,0, 8,10,0,0, 8,11,0,0, 8,12,0,0, 8,13,0,0, 8,14,0,0, 8,15,0,0, 8,16,0,0, 8,17,0,0, 8,18,0,0, 8,19,0,0, 8,20,0,0, 8,21,0,0, 8,22,0,0, 8,23,0,0, 8,24,0,0, 8,25,0,0, 8,26,0,0, 8,27,0,0, 8,28,0,0, 8,29,0,0, 8,30,0,0, 8,31,0,0, 8,32,0,0, 8,33,0,0, 8,34,0,0, 8,35,0,0, ],36,4,0,1,16,35,3,2),
	RConstraints.R1(Edge_Net_Subnet3,[12,0,0,0, 12,1,0,0, 12,2,0,0, 12,3,0,0, 12,4,0,0, 12,5,0,0, 12,6,0,0, 12,7,0,0, 12,8,0,0, 12,9,0,0, 12,10,0,0, 12,11,0,0, 12,12,0,0, 12,13,0,0, 12,14,0,0, 12,15,0,0, 12,16,0,0, 12,17,0,0, 12,18,0,0, 12,19,0,0, 12,20,0,0, 12,21,0,0, 12,22,0,0, 12,23,0,0, 12,24,0,0, 12,25,0,0, 12,26,0,0, 12,27,0,0, 12,28,0,0, 12,29,0,0, 12,30,0,0, 12,31,0,0, 12,32,0,0, 12,33,0,0, 12,34,0,0, 12,35,0,0, ],36,4,0,1,16,35,3,2),
	).to_cnf()
Net3_Subnet2_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[8,0,0, 8,1,0, 8,2,0, 8,3,0, 8,4,0, 8,5,0, 8,6,0, 8,7,0, 8,8,0, 8,9,0, 8,10,0, 8,11,0, 8,12,0, 8,13,0, 8,14,0, 8,15,0, 8,16,0, 8,17,0, 8,18,0, 8,19,0, 8,20,0, 8,21,0, 8,22,0, 8,23,0, 8,24,0, 8,25,0, 8,26,0, 8,27,0, 8,28,0, 8,29,0, 8,30,0, 8,31,0, 8,32,0, 8,33,0, 8,34,0, 8,35,0, 12,0,0, 12,1,0, 12,2,0, 12,3,0, 12,4,0, 12,5,0, 12,6,0, 12,7,0, 12,8,0, 12,9,0, 12,10,0, 12,11,0, 12,12,0, 12,13,0, 12,14,0, 12,15,0, 12,16,0, 12,17,0, 12,18,0, 12,19,0, 12,20,0, 12,21,0, 12,22,0, 12,23,0, 12,24,0, 12,25,0, 12,26,0, 12,27,0, 12,28,0, 12,29,0, 12,30,0, 12,31,0, 12,32,0, 12,33,0, 12,34,0, 12,35,0, ],72,4,0,0,16,35,3,2,2),
	)
Net3_Subnet2_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(3,12+1)])for x in range(4,16+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net3_Subnet2_R = And(Net3_Subnet2_R1,Net3_Subnet2_R2,Net3_Subnet2_R3,)
Net3_Subnet2_Formula = And(Net3_Subnet2_C,Net3_Subnet2_DR,Net3_Subnet2_R)
# Net = 2 Subnet = 0 | Left -> Right [0,14] Top -> Bottom [0,35]
# Range R1(10,10,1,6)
# Range R2(2,2,28,33)
### Disable edges outside window
Edge_Net_Subnet2[14:77+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(82944)

### Consistency Constraints
Net2_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,14+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,14+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,0],Xor(Edge_Net_Subnet2[x,y,2,trend,1,0],Edge_Net_Subnet2[x,y,2,trend,2,0])),And(~Edge_Net_Subnet2[x,y,2,trend,0,0],~Edge_Net_Subnet2[x,y,2,trend,1,0],~Edge_Net_Subnet2[x,y,2,trend,2,0]))for x in range(0,14+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,0],Xor(Edge_Net_Subnet2[x,y,3,1,1,0],Edge_Net_Subnet2[x,y,3,1,2,0])),And(~Edge_Net_Subnet2[x,y,3,1,0,0],~Edge_Net_Subnet2[x,y,3,1,1,0],~Edge_Net_Subnet2[x,y,3,1,2,0]))for x in range(0,14+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,0],Xor(Edge_Net_Subnet2[x,y,1,trend,0,0],Edge_Net_Subnet2[x,y,1,trend,1,0])),And(~Edge_Net_Subnet2[x,y,1,trend,2,0],~Edge_Net_Subnet2[x,y,1,trend,0,0],~Edge_Net_Subnet2[x,y,1,trend,1,0]))for x in range(0,14+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet0_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,0], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0+1,5)]))for trend in range(0,1+1)])for x in range(0,14+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,0], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0+1,5)]))for trend in range(0,1+1)])for x in range(0,14+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet0_C = And(Net2_Subnet0_C1, Net2_Subnet0_C2,Net2_Subnet0_C3_ME1_Mask,Net2_Subnet0_C4_MINT1_Mask,Net2_Subnet0_C5_AIL2GIL_Mask,Net2_Subnet0_C6,)
### Design Rules
Net2_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(0,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(0,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(0,14+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge_Net_Subnet2[x-1,y,1,1,1,0]), And(Edge_Net_Subnet2[x+1,y,1,1,1,0], Edge_Net_Subnet2[x+2,y,1,1,1,0], Edge_Net_Subnet2[x+3,y,1,1,1,0], ))for x in range(1,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge_Net_Subnet2[x+1,y,1,1,1,0]), And(Edge_Net_Subnet2[x-1,y,1,1,1,0], Edge_Net_Subnet2[x-2,y,1,1,1,0], Edge_Net_Subnet2[x-3,y,1,1,1,0], ))for x in range(3,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,14+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(0,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(0,14+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(0,14+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0]), And(Edge_Net_Subnet2[x,y+1,1,0,0,0], Edge_Net_Subnet2[x,y+2,1,0,0,0], Edge_Net_Subnet2[x,y+3,1,0,0,0], ))for x in range(0,14+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0]), And(Edge_Net_Subnet2[x,y-1,1,0,0,0], Edge_Net_Subnet2[x,y-2,1,0,0,0], Edge_Net_Subnet2[x,y-3,1,0,0,0], ))for x in range(0,14+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge_Net_Subnet2[x,y-1,1,0,0,0]), And(Edge_Net_Subnet2[x,y+1,1,0,0,0], Edge_Net_Subnet2[x,y+2,1,0,0,0], Edge_Net_Subnet2[x,y+3,1,0,0,0], ))for x in range(0,14+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge_Net_Subnet2[x,y+1,1,0,0,0]), And(Edge_Net_Subnet2[x,y-1,1,0,0,0], Edge_Net_Subnet2[x,y-2,1,0,0,0], Edge_Net_Subnet2[x,y-3,1,0,0,0], ))for x in range(0,14+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(0,14+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(0,14+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(0,14+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(0,14+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(0,14+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(0,14+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(0,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge_Net_Subnet2[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,0], Edge_Net_Subnet2[x+2,y,3,1,mask,0], Edge_Net_Subnet2[x+3,y,3,1,mask,0], Edge_Net_Subnet2[x+4,y,3,1,mask,0], Edge_Net_Subnet2[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(1,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge_Net_Subnet2[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,0], Edge_Net_Subnet2[x-2,y,3,1,mask,0], Edge_Net_Subnet2[x-3,y,3,1,mask,0], Edge_Net_Subnet2[x-4,y,3,1,mask,0], Edge_Net_Subnet2[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,0], And(Edge_Net_Subnet2[x+1,y,3,1,mask,0], Edge_Net_Subnet2[x+2,y,3,1,mask,0], Edge_Net_Subnet2[x+3,y,3,1,mask,0], Edge_Net_Subnet2[x+4,y,3,1,mask,0], Edge_Net_Subnet2[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(0, 0+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(0,14+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(0,14+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,14+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(0,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge_Net_Subnet2[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,0], Edge_Net_Subnet2[x+2,y,2,1,mask,0], Edge_Net_Subnet2[x+3,y,2,1,mask,0], Edge_Net_Subnet2[x+4,y,2,1,mask,0], Edge_Net_Subnet2[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(1,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge_Net_Subnet2[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,0], Edge_Net_Subnet2[x-2,y,2,1,mask,0], Edge_Net_Subnet2[x-3,y,2,1,mask,0], Edge_Net_Subnet2[x-4,y,2,1,mask,0], Edge_Net_Subnet2[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(Edge_Net_Subnet2[x-1,y,2,1,mask,0], Edge_Net_Subnet2[x-2,y,2,1,mask,0], Edge_Net_Subnet2[x-3,y,2,1,mask,0], Edge_Net_Subnet2[x-4,y,2,1,mask,0], Edge_Net_Subnet2[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(0,0+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(Edge_Net_Subnet2[x+1,y,2,1,mask,0], Edge_Net_Subnet2[x+2,y,2,1,mask,0], Edge_Net_Subnet2[x+3,y,2,1,mask,0], Edge_Net_Subnet2[x+4,y,2,1,mask,0], Edge_Net_Subnet2[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(14-1,0)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge_Net_Subnet2[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,0], Edge_Net_Subnet2[x,y+2,2,0,mask,0], Edge_Net_Subnet2[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge_Net_Subnet2[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,0], Edge_Net_Subnet2[x,y-2,2,0,mask,0], Edge_Net_Subnet2[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,0], And(Edge_Net_Subnet2[x,y+1,2,0,mask,0], Edge_Net_Subnet2[x,y+2,2,0,mask,0], Edge_Net_Subnet2[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,0], And(Edge_Net_Subnet2[x,y-1,2,0,mask,0], Edge_Net_Subnet2[x,y-2,2,0,mask,0], Edge_Net_Subnet2[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,14+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(0,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(0,14+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(0,14+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(0,14+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(0,14+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(0,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,14+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,14+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,14+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,14+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet0_DR = And(Net2_Subnet0_DR_Trend, Net2_Subnet0_DR_GIL_HorMinWidth,Net2_Subnet0_DR_GIL_HorMinSpacing,Net2_Subnet0_DR_GIL_VerMinSpacing,Net2_Subnet0_DR_AIL2_VerMinWidth,Net2_Subnet0_DR_AIL2_VerMinSpacing,Net2_Subnet0_DR_VerAIL2_HorMinSpacing,Net2_Subnet0_DR_MINT1AB_HorMinWidth,Net2_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet0_DR_M1AB_MinWidth,Net2_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet0_DR_V0_HorMinSpacing,Net2_Subnet0_DR_V1_HorMinSpacing,Net2_Subnet0_DR_V0_VerMinSpacing,Net2_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[10,1,0,0, 10,2,0,0, 10,3,0,0, 10,4,0,0, 10,5,0,0, 10,6,0,0, ],6,0,0,1,14,35,3,0),
	RConstraints.R1(Edge_Net_Subnet2,[2,28,0,0, 2,29,0,0, 2,30,0,0, 2,31,0,0, 2,32,0,0, 2,33,0,0, ],6,0,0,1,14,35,3,0),
	).to_cnf()
Net2_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[10,1,0, 10,2,0, 10,3,0, 10,4,0, 10,5,0, 10,6,0, 10,7,0, 2,28,0, 2,29,0, 2,30,0, 2,31,0, 2,32,0, 2,33,0, 2,34,0, ],14,0,0,0,14,35,3,0,1),
	)
Net2_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(0,14+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,12+1)])for x in range(0,14+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet0_R = And(Net2_Subnet0_R1,Net2_Subnet0_R2,Net2_Subnet0_R3,)
Net2_Subnet0_Formula = And(Net2_Subnet0_C,Net2_Subnet0_DR,Net2_Subnet0_R)
# Net = 2 Subnet = 1 | Left -> Right [6,48] Top -> Bottom [0,35]
# Range R1(10,10,1,6)
# Range R2(44,44,0,35)
### Disable edges outside window
Edge_Net_Subnet2[0:6,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(7776)
Edge_Net_Subnet2[48:77+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(38880)

### Consistency Constraints
Net2_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(6,48+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(6,48+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,1],Xor(Edge_Net_Subnet2[x,y,2,trend,1,1],Edge_Net_Subnet2[x,y,2,trend,2,1])),And(~Edge_Net_Subnet2[x,y,2,trend,0,1],~Edge_Net_Subnet2[x,y,2,trend,1,1],~Edge_Net_Subnet2[x,y,2,trend,2,1]))for x in range(6,48+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,1],Xor(Edge_Net_Subnet2[x,y,3,1,1,1],Edge_Net_Subnet2[x,y,3,1,2,1])),And(~Edge_Net_Subnet2[x,y,3,1,0,1],~Edge_Net_Subnet2[x,y,3,1,1,1],~Edge_Net_Subnet2[x,y,3,1,2,1]))for x in range(6,48+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,1],Xor(Edge_Net_Subnet2[x,y,1,trend,0,1],Edge_Net_Subnet2[x,y,1,trend,1,1])),And(~Edge_Net_Subnet2[x,y,1,trend,2,1],~Edge_Net_Subnet2[x,y,1,trend,0,1],~Edge_Net_Subnet2[x,y,1,trend,1,1]))for x in range(6,48+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(6,48+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(1+1,5)]))for trend in range(0,1+1)])for x in range(6,48+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(6,48+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(1+1,5)]))for trend in range(0,1+1)])for x in range(6,48+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet1_C = And(Net2_Subnet1_C1, Net2_Subnet1_C2,Net2_Subnet1_C3_ME1_Mask,Net2_Subnet1_C4_MINT1_Mask,Net2_Subnet1_C5_AIL2GIL_Mask,Net2_Subnet1_C6,)
### Design Rules
Net2_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(6,48+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,1], ~Edge_Net_Subnet2[x-1,y,1,1,1,1]), And(Edge_Net_Subnet2[x+1,y,1,1,1,1], Edge_Net_Subnet2[x+2,y,1,1,1,1], Edge_Net_Subnet2[x+3,y,1,1,1,1], ))for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,1], ~Edge_Net_Subnet2[x+1,y,1,1,1,1]), And(Edge_Net_Subnet2[x-1,y,1,1,1,1], Edge_Net_Subnet2[x-2,y,1,1,1,1], Edge_Net_Subnet2[x-3,y,1,1,1,1], ))for x in range(6,48+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(6,48+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(6,48+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(6,48+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1]), And(Edge_Net_Subnet2[x,y+1,1,0,0,1], Edge_Net_Subnet2[x,y+2,1,0,0,1], Edge_Net_Subnet2[x,y+3,1,0,0,1], ))for x in range(6,48+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1]), And(Edge_Net_Subnet2[x,y-1,1,0,0,1], Edge_Net_Subnet2[x,y-2,1,0,0,1], Edge_Net_Subnet2[x,y-3,1,0,0,1], ))for x in range(6,48+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge_Net_Subnet2[x,y-1,1,0,0,1]), And(Edge_Net_Subnet2[x,y+1,1,0,0,1], Edge_Net_Subnet2[x,y+2,1,0,0,1], Edge_Net_Subnet2[x,y+3,1,0,0,1], ))for x in range(6,48+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge_Net_Subnet2[x,y+1,1,0,0,1]), And(Edge_Net_Subnet2[x,y-1,1,0,0,1], Edge_Net_Subnet2[x,y-2,1,0,0,1], Edge_Net_Subnet2[x,y-3,1,0,0,1], ))for x in range(6,48+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(6,48+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(6,48+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(6,48+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(6,48+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(6,48+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(6,48+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(6,48+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,1], ~Edge_Net_Subnet2[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,1], Edge_Net_Subnet2[x+2,y,3,1,mask,1], Edge_Net_Subnet2[x+3,y,3,1,mask,1], Edge_Net_Subnet2[x+4,y,3,1,mask,1], Edge_Net_Subnet2[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,1], ~Edge_Net_Subnet2[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,1], Edge_Net_Subnet2[x-2,y,3,1,mask,1], Edge_Net_Subnet2[x-3,y,3,1,mask,1], Edge_Net_Subnet2[x-4,y,3,1,mask,1], Edge_Net_Subnet2[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(6,48+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(6,48+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(6,48+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,1], ~Edge_Net_Subnet2[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,1], Edge_Net_Subnet2[x+2,y,2,1,mask,1], Edge_Net_Subnet2[x+3,y,2,1,mask,1], Edge_Net_Subnet2[x+4,y,2,1,mask,1], Edge_Net_Subnet2[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,1], ~Edge_Net_Subnet2[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,1], Edge_Net_Subnet2[x-2,y,2,1,mask,1], Edge_Net_Subnet2[x-3,y,2,1,mask,1], Edge_Net_Subnet2[x-4,y,2,1,mask,1], Edge_Net_Subnet2[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,1], And(Edge_Net_Subnet2[x-1,y,2,1,mask,1], Edge_Net_Subnet2[x-2,y,2,1,mask,1], Edge_Net_Subnet2[x-3,y,2,1,mask,1], Edge_Net_Subnet2[x-4,y,2,1,mask,1], Edge_Net_Subnet2[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(6,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,1], And(Edge_Net_Subnet2[x+1,y,2,1,mask,1], Edge_Net_Subnet2[x+2,y,2,1,mask,1], Edge_Net_Subnet2[x+3,y,2,1,mask,1], Edge_Net_Subnet2[x+4,y,2,1,mask,1], Edge_Net_Subnet2[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(48-1,6)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,1], ~Edge_Net_Subnet2[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,1], Edge_Net_Subnet2[x,y+2,2,0,mask,1], Edge_Net_Subnet2[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,1], ~Edge_Net_Subnet2[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,1], Edge_Net_Subnet2[x,y-2,2,0,mask,1], Edge_Net_Subnet2[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,1], And(Edge_Net_Subnet2[x,y+1,2,0,mask,1], Edge_Net_Subnet2[x,y+2,2,0,mask,1], Edge_Net_Subnet2[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,1], And(Edge_Net_Subnet2[x,y-1,2,0,mask,1], Edge_Net_Subnet2[x,y-2,2,0,mask,1], Edge_Net_Subnet2[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(6,48+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(6,48+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(6,48+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(6,48+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(6,48+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(6,48+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,48+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,48+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,48+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,48+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,48+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,48+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,48+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,48+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet1_DR = And(Net2_Subnet1_DR_Trend, Net2_Subnet1_DR_GIL_HorMinWidth,Net2_Subnet1_DR_GIL_HorMinSpacing,Net2_Subnet1_DR_GIL_VerMinSpacing,Net2_Subnet1_DR_AIL2_VerMinWidth,Net2_Subnet1_DR_AIL2_VerMinSpacing,Net2_Subnet1_DR_VerAIL2_HorMinSpacing,Net2_Subnet1_DR_MINT1AB_HorMinWidth,Net2_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet1_DR_M1AB_MinWidth,Net2_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet1_DR_V0_HorMinSpacing,Net2_Subnet1_DR_V1_HorMinSpacing,Net2_Subnet1_DR_V0_VerMinSpacing,Net2_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[10,1,0,0, 10,2,0,0, 10,3,0,0, 10,4,0,0, 10,5,0,0, 10,6,0,0, ],6,6,0,1,48,35,3,1),
	RConstraints.R1(Edge_Net_Subnet2,[44,0,0,0, 44,1,0,0, 44,2,0,0, 44,3,0,0, 44,4,0,0, 44,5,0,0, 44,6,0,0, 44,7,0,0, 44,8,0,0, 44,9,0,0, 44,10,0,0, 44,11,0,0, 44,12,0,0, 44,13,0,0, 44,14,0,0, 44,15,0,0, 44,16,0,0, 44,17,0,0, 44,18,0,0, 44,19,0,0, 44,20,0,0, 44,21,0,0, 44,22,0,0, 44,23,0,0, 44,24,0,0, 44,25,0,0, 44,26,0,0, 44,27,0,0, 44,28,0,0, 44,29,0,0, 44,30,0,0, 44,31,0,0, 44,32,0,0, 44,33,0,0, 44,34,0,0, 44,35,0,0, ],36,6,0,1,48,35,3,1),
	).to_cnf()
Net2_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[10,1,0, 10,2,0, 10,3,0, 10,4,0, 10,5,0, 10,6,0, 10,7,0, 44,0,0, 44,1,0, 44,2,0, 44,3,0, 44,4,0, 44,5,0, 44,6,0, 44,7,0, 44,8,0, 44,9,0, 44,10,0, 44,11,0, 44,12,0, 44,13,0, 44,14,0, 44,15,0, 44,16,0, 44,17,0, 44,18,0, 44,19,0, 44,20,0, 44,21,0, 44,22,0, 44,23,0, 44,24,0, 44,25,0, 44,26,0, 44,27,0, 44,28,0, 44,29,0, 44,30,0, 44,31,0, 44,32,0, 44,33,0, 44,34,0, 44,35,0, ],43,6,0,0,48,35,3,1,1),
	)
Net2_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(6,48+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,12+1)])for x in range(6,48+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet1_R = And(Net2_Subnet1_R1,Net2_Subnet1_R2,Net2_Subnet1_R3,)
Net2_Subnet1_Formula = And(Net2_Subnet1_C,Net2_Subnet1_DR,Net2_Subnet1_R)
# Net = 2 Subnet = 3 | Left -> Right [40,56] Top -> Bottom [0,35]
# Range R1(44,44,0,35)
# Range R2(52,52,0,35)
### Disable edges outside window
Edge_Net_Subnet2[0:40,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(51840)
Edge_Net_Subnet2[56:77+1,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(28512)

### Consistency Constraints
Net2_Subnet3_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(40,56+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet3_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,3]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(40,56+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet3_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,3],Xor(Edge_Net_Subnet2[x,y,2,trend,1,3],Edge_Net_Subnet2[x,y,2,trend,2,3])),And(~Edge_Net_Subnet2[x,y,2,trend,0,3],~Edge_Net_Subnet2[x,y,2,trend,1,3],~Edge_Net_Subnet2[x,y,2,trend,2,3]))for x in range(40,56+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet3_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,3],Xor(Edge_Net_Subnet2[x,y,3,1,1,3],Edge_Net_Subnet2[x,y,3,1,2,3])),And(~Edge_Net_Subnet2[x,y,3,1,0,3],~Edge_Net_Subnet2[x,y,3,1,1,3],~Edge_Net_Subnet2[x,y,3,1,2,3]))for x in range(40,56+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet3_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,3],Xor(Edge_Net_Subnet2[x,y,1,trend,0,3],Edge_Net_Subnet2[x,y,1,trend,1,3])),And(~Edge_Net_Subnet2[x,y,1,trend,2,3],~Edge_Net_Subnet2[x,y,1,trend,0,3],~Edge_Net_Subnet2[x,y,1,trend,1,3]))for x in range(40,56+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet3_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(40,56+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(3+1,5)]))for trend in range(0,1+1)])for x in range(40,56+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(40,56+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(3+1,5)]))for trend in range(0,1+1)])for x in range(40,56+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet3_C = And(Net2_Subnet3_C1, Net2_Subnet3_C2,Net2_Subnet3_C3_ME1_Mask,Net2_Subnet3_C4_MINT1_Mask,Net2_Subnet3_C5_AIL2GIL_Mask,Net2_Subnet3_C6,)
### Design Rules
Net2_Subnet3_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(40,56+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet3_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,3], ~Edge_Net_Subnet2[x-1,y,1,1,1,3]), And(Edge_Net_Subnet2[x+1,y,1,1,1,3], Edge_Net_Subnet2[x+2,y,1,1,1,3], Edge_Net_Subnet2[x+3,y,1,1,1,3], ))for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,3], ~Edge_Net_Subnet2[x+1,y,1,1,1,3]), And(Edge_Net_Subnet2[x-1,y,1,1,1,3], Edge_Net_Subnet2[x-2,y,1,1,1,3], Edge_Net_Subnet2[x-3,y,1,1,1,3], ))for x in range(40,56+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,3], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,3], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(40,56+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,3], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(40,56+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,3], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(40,56+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3]), And(Edge_Net_Subnet2[x,y+1,1,0,0,3], Edge_Net_Subnet2[x,y+2,1,0,0,3], Edge_Net_Subnet2[x,y+3,1,0,0,3], ))for x in range(40,56+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3]), And(Edge_Net_Subnet2[x,y-1,1,0,0,3], Edge_Net_Subnet2[x,y-2,1,0,0,3], Edge_Net_Subnet2[x,y-3,1,0,0,3], ))for x in range(40,56+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge_Net_Subnet2[x,y-1,1,0,0,3]), And(Edge_Net_Subnet2[x,y+1,1,0,0,3], Edge_Net_Subnet2[x,y+2,1,0,0,3], Edge_Net_Subnet2[x,y+3,1,0,0,3], ))for x in range(40,56+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge_Net_Subnet2[x,y+1,1,0,0,3]), And(Edge_Net_Subnet2[x,y-1,1,0,0,3], Edge_Net_Subnet2[x,y-2,1,0,0,3], Edge_Net_Subnet2[x,y-3,1,0,0,3], ))for x in range(40,56+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet3_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(40,56+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(40,56+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(40,56+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(40,56+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(40,56+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(40,56+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet3_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,3], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,3], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(40,56+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,3], ~Edge_Net_Subnet2[x-1,y,3,1,mask,3]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,3], Edge_Net_Subnet2[x+2,y,3,1,mask,3], Edge_Net_Subnet2[x+3,y,3,1,mask,3], Edge_Net_Subnet2[x+4,y,3,1,mask,3], Edge_Net_Subnet2[x+5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,3], ~Edge_Net_Subnet2[x+1,y,3,1,mask,3]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,3], Edge_Net_Subnet2[x-2,y,3,1,mask,3], Edge_Net_Subnet2[x-3,y,3,1,mask,3], Edge_Net_Subnet2[x-4,y,3,1,mask,3], Edge_Net_Subnet2[x-5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,3], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,3], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,3], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,3], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,3], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(40,56+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,3], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(40,56+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,3], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,3], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(40,56+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,3], ~Edge_Net_Subnet2[x-1,y,2,1,mask,3]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,3], Edge_Net_Subnet2[x+2,y,2,1,mask,3], Edge_Net_Subnet2[x+3,y,2,1,mask,3], Edge_Net_Subnet2[x+4,y,2,1,mask,3], Edge_Net_Subnet2[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,3], ~Edge_Net_Subnet2[x+1,y,2,1,mask,3]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,3], Edge_Net_Subnet2[x-2,y,2,1,mask,3], Edge_Net_Subnet2[x-3,y,2,1,mask,3], Edge_Net_Subnet2[x-4,y,2,1,mask,3], Edge_Net_Subnet2[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,3], And(Edge_Net_Subnet2[x-1,y,2,1,mask,3], Edge_Net_Subnet2[x-2,y,2,1,mask,3], Edge_Net_Subnet2[x-3,y,2,1,mask,3], Edge_Net_Subnet2[x-4,y,2,1,mask,3], Edge_Net_Subnet2[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(40,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,3], And(Edge_Net_Subnet2[x+1,y,2,1,mask,3], Edge_Net_Subnet2[x+2,y,2,1,mask,3], Edge_Net_Subnet2[x+3,y,2,1,mask,3], Edge_Net_Subnet2[x+4,y,2,1,mask,3], Edge_Net_Subnet2[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(56-1,40)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,3], ~Edge_Net_Subnet2[x,y-1,2,0,mask,3]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,3], Edge_Net_Subnet2[x,y+2,2,0,mask,3], Edge_Net_Subnet2[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,3], ~Edge_Net_Subnet2[x,y+1,2,0,mask,3]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,3], Edge_Net_Subnet2[x,y-2,2,0,mask,3], Edge_Net_Subnet2[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,3], And(Edge_Net_Subnet2[x,y+1,2,0,mask,3], Edge_Net_Subnet2[x,y+2,2,0,mask,3], Edge_Net_Subnet2[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,3], And(Edge_Net_Subnet2[x,y-1,2,0,mask,3], Edge_Net_Subnet2[x,y-2,2,0,mask,3], Edge_Net_Subnet2[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,3], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,3], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(40,56+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,3], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,3], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,3], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(40,56+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,3], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(40,56+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet3_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,3], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,3], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet3_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,3], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(40,56+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,3], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(40,56+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,3], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,3], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,3], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,3], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(40,56+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,3], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,3], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(40,56+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,3], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,3], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(40,56+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,3], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(40,56+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,3], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(40,56+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,3], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(40,56+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,3], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(40,56+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,3], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(40,56+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,3], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(40,56+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet3_DR = And(Net2_Subnet3_DR_Trend, Net2_Subnet3_DR_GIL_HorMinWidth,Net2_Subnet3_DR_GIL_HorMinSpacing,Net2_Subnet3_DR_GIL_VerMinSpacing,Net2_Subnet3_DR_AIL2_VerMinWidth,Net2_Subnet3_DR_AIL2_VerMinSpacing,Net2_Subnet3_DR_VerAIL2_HorMinSpacing,Net2_Subnet3_DR_MINT1AB_HorMinWidth,Net2_Subnet3_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet3_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet3_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet3_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet3_DR_M1AB_MinWidth,Net2_Subnet3_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet3_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet3_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet3_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet3_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet3_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet3_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet3_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet3_DR_V0_HorMinSpacing,Net2_Subnet3_DR_V1_HorMinSpacing,Net2_Subnet3_DR_V0_VerMinSpacing,Net2_Subnet3_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet3_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[44,0,0,0, 44,1,0,0, 44,2,0,0, 44,3,0,0, 44,4,0,0, 44,5,0,0, 44,6,0,0, 44,7,0,0, 44,8,0,0, 44,9,0,0, 44,10,0,0, 44,11,0,0, 44,12,0,0, 44,13,0,0, 44,14,0,0, 44,15,0,0, 44,16,0,0, 44,17,0,0, 44,18,0,0, 44,19,0,0, 44,20,0,0, 44,21,0,0, 44,22,0,0, 44,23,0,0, 44,24,0,0, 44,25,0,0, 44,26,0,0, 44,27,0,0, 44,28,0,0, 44,29,0,0, 44,30,0,0, 44,31,0,0, 44,32,0,0, 44,33,0,0, 44,34,0,0, 44,35,0,0, ],36,40,0,1,56,35,3,3),
	RConstraints.R1(Edge_Net_Subnet2,[52,0,0,0, 52,1,0,0, 52,2,0,0, 52,3,0,0, 52,4,0,0, 52,5,0,0, 52,6,0,0, 52,7,0,0, 52,8,0,0, 52,9,0,0, 52,10,0,0, 52,11,0,0, 52,12,0,0, 52,13,0,0, 52,14,0,0, 52,15,0,0, 52,16,0,0, 52,17,0,0, 52,18,0,0, 52,19,0,0, 52,20,0,0, 52,21,0,0, 52,22,0,0, 52,23,0,0, 52,24,0,0, 52,25,0,0, 52,26,0,0, 52,27,0,0, 52,28,0,0, 52,29,0,0, 52,30,0,0, 52,31,0,0, 52,32,0,0, 52,33,0,0, 52,34,0,0, 52,35,0,0, ],36,40,0,1,56,35,3,3),
	).to_cnf()
Net2_Subnet3_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[44,0,0, 44,1,0, 44,2,0, 44,3,0, 44,4,0, 44,5,0, 44,6,0, 44,7,0, 44,8,0, 44,9,0, 44,10,0, 44,11,0, 44,12,0, 44,13,0, 44,14,0, 44,15,0, 44,16,0, 44,17,0, 44,18,0, 44,19,0, 44,20,0, 44,21,0, 44,22,0, 44,23,0, 44,24,0, 44,25,0, 44,26,0, 44,27,0, 44,28,0, 44,29,0, 44,30,0, 44,31,0, 44,32,0, 44,33,0, 44,34,0, 44,35,0, 52,0,0, 52,1,0, 52,2,0, 52,3,0, 52,4,0, 52,5,0, 52,6,0, 52,7,0, 52,8,0, 52,9,0, 52,10,0, 52,11,0, 52,12,0, 52,13,0, 52,14,0, 52,15,0, 52,16,0, 52,17,0, 52,18,0, 52,19,0, 52,20,0, 52,21,0, 52,22,0, 52,23,0, 52,24,0, 52,25,0, 52,26,0, 52,27,0, 52,28,0, 52,29,0, 52,30,0, 52,31,0, 52,32,0, 52,33,0, 52,34,0, 52,35,0, ],72,40,0,0,56,35,3,3,1),
	)
Net2_Subnet3_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(40,56+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,12+1)])for x in range(40,56+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet3_R = And(Net2_Subnet3_R1,Net2_Subnet3_R2,Net2_Subnet3_R3,)
Net2_Subnet3_Formula = And(Net2_Subnet3_C,Net2_Subnet3_DR,Net2_Subnet3_R)
# Net = 4 Subnet = 0 | Left -> Right [0,16] Top -> Bottom [0,35]
# Range R1(12,12,0,35)
# Range R2(4,4,0,35)
### Disable edges outside window
Edge_Net_Subnet4[16:77+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(80352)

### Consistency Constraints
Net4_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,3]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net4_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet4[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,3])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net4_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet4[x,y,2,trend,0,0],Xor(Edge_Net_Subnet4[x,y,2,trend,1,0],Edge_Net_Subnet4[x,y,2,trend,2,0])),And(~Edge_Net_Subnet4[x,y,2,trend,0,0],~Edge_Net_Subnet4[x,y,2,trend,1,0],~Edge_Net_Subnet4[x,y,2,trend,2,0]))for x in range(0,16+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net4_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet4[x,y,3,1,0,0],Xor(Edge_Net_Subnet4[x,y,3,1,1,0],Edge_Net_Subnet4[x,y,3,1,2,0])),And(~Edge_Net_Subnet4[x,y,3,1,0,0],~Edge_Net_Subnet4[x,y,3,1,1,0],~Edge_Net_Subnet4[x,y,3,1,2,0]))for x in range(0,16+1)])for y in range(0,35+1)]).to_cnf()
Net4_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet4[x,y,1,trend,2,0],Xor(Edge_Net_Subnet4[x,y,1,trend,0,0],Edge_Net_Subnet4[x,y,1,trend,1,0])),And(~Edge_Net_Subnet4[x,y,1,trend,2,0],~Edge_Net_Subnet4[x,y,1,trend,0,0],~Edge_Net_Subnet4[x,y,1,trend,1,0]))for x in range(0,16+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net4_Subnet0_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,z,trend,1,0], And(*[And(~Edge_Net_Subnet4[x,y,z,trend,2,s2])for s2 in range(0+1,3)]))for trend in range(0,1+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,z,trend,2,0], And(*[And(~Edge_Net_Subnet4[x,y,z,trend,1,s2])for s2 in range(0+1,3)]))for trend in range(0,1+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net4_Subnet0_C = And(Net4_Subnet0_C1, Net4_Subnet0_C2,Net4_Subnet0_C3_ME1_Mask,Net4_Subnet0_C4_MINT1_Mask,Net4_Subnet0_C5_AIL2GIL_Mask,Net4_Subnet0_C6,)
### Design Rules
Net4_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(0,16+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net4_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,1,1,1,0], ~Edge_Net_Subnet4[x-1,y,1,1,1,0]), And(Edge_Net_Subnet4[x+1,y,1,1,1,0], Edge_Net_Subnet4[x+2,y,1,1,1,0], Edge_Net_Subnet4[x+3,y,1,1,1,0], ))for x in range(1,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,1,1,1,0], ~Edge_Net_Subnet4[x+1,y,1,1,1,0]), And(Edge_Net_Subnet4[x-1,y,1,1,1,0], Edge_Net_Subnet4[x-2,y,1,1,1,0], Edge_Net_Subnet4[x-3,y,1,1,1,0], ))for x in range(3,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(0,16+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(0,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net4_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,0]), And(Edge_Net_Subnet4[x,y+1,1,0,0,0], Edge_Net_Subnet4[x,y+2,1,0,0,0], Edge_Net_Subnet4[x,y+3,1,0,0,0], ))for x in range(0,16+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,0]), And(Edge_Net_Subnet4[x,y-1,1,0,0,0], Edge_Net_Subnet4[x,y-2,1,0,0,0], Edge_Net_Subnet4[x,y-3,1,0,0,0], ))for x in range(0,16+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,0], ~Edge_Net_Subnet4[x,y-1,1,0,0,0]), And(Edge_Net_Subnet4[x,y+1,1,0,0,0], Edge_Net_Subnet4[x,y+2,1,0,0,0], Edge_Net_Subnet4[x,y+3,1,0,0,0], ))for x in range(0,16+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,0], ~Edge_Net_Subnet4[x,y+1,1,0,0,0]), And(Edge_Net_Subnet4[x,y-1,1,0,0,0], Edge_Net_Subnet4[x,y-2,1,0,0,0], Edge_Net_Subnet4[x,y-3,1,0,0,0], ))for x in range(0,16+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net4_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(0,16+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(0,16+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(0,16+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(0,16+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(0,16+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(0,16+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net4_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,3,1,mask,0], ~Edge_Net_Subnet4[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet4[x+1,y,3,1,mask,0], Edge_Net_Subnet4[x+2,y,3,1,mask,0], Edge_Net_Subnet4[x+3,y,3,1,mask,0], Edge_Net_Subnet4[x+4,y,3,1,mask,0], Edge_Net_Subnet4[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(1,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,3,1,mask,0], ~Edge_Net_Subnet4[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet4[x-1,y,3,1,mask,0], Edge_Net_Subnet4[x-2,y,3,1,mask,0], Edge_Net_Subnet4[x-3,y,3,1,mask,0], Edge_Net_Subnet4[x-4,y,3,1,mask,0], Edge_Net_Subnet4[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,mask,0], And(Edge_Net_Subnet4[x+1,y,3,1,mask,0], Edge_Net_Subnet4[x+2,y,3,1,mask,0], Edge_Net_Subnet4[x+3,y,3,1,mask,0], Edge_Net_Subnet4[x+4,y,3,1,mask,0], Edge_Net_Subnet4[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(0, 0+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net4_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(0,16+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(0,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net4_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,2,1,mask,0], ~Edge_Net_Subnet4[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet4[x+1,y,2,1,mask,0], Edge_Net_Subnet4[x+2,y,2,1,mask,0], Edge_Net_Subnet4[x+3,y,2,1,mask,0], Edge_Net_Subnet4[x+4,y,2,1,mask,0], Edge_Net_Subnet4[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(1,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,2,1,mask,0], ~Edge_Net_Subnet4[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet4[x-1,y,2,1,mask,0], Edge_Net_Subnet4[x-2,y,2,1,mask,0], Edge_Net_Subnet4[x-3,y,2,1,mask,0], Edge_Net_Subnet4[x-4,y,2,1,mask,0], Edge_Net_Subnet4[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,0], And(Edge_Net_Subnet4[x-1,y,2,1,mask,0], Edge_Net_Subnet4[x-2,y,2,1,mask,0], Edge_Net_Subnet4[x-3,y,2,1,mask,0], Edge_Net_Subnet4[x-4,y,2,1,mask,0], Edge_Net_Subnet4[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(0,0+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,0], And(Edge_Net_Subnet4[x+1,y,2,1,mask,0], Edge_Net_Subnet4[x+2,y,2,1,mask,0], Edge_Net_Subnet4[x+3,y,2,1,mask,0], Edge_Net_Subnet4[x+4,y,2,1,mask,0], Edge_Net_Subnet4[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(16-1,0)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,0], ~Edge_Net_Subnet4[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet4[x,y+1,2,0,mask,0], Edge_Net_Subnet4[x,y+2,2,0,mask,0], Edge_Net_Subnet4[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,0], ~Edge_Net_Subnet4[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet4[x,y-1,2,0,mask,0], Edge_Net_Subnet4[x,y-2,2,0,mask,0], Edge_Net_Subnet4[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet4[x,y,2,0,mask,0], And(Edge_Net_Subnet4[x,y+1,2,0,mask,0], Edge_Net_Subnet4[x,y+2,2,0,mask,0], Edge_Net_Subnet4[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet4[x,y,2,0,mask,0], And(Edge_Net_Subnet4[x,y-1,2,0,mask,0], Edge_Net_Subnet4[x,y-2,2,0,mask,0], Edge_Net_Subnet4[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(35,35+1)]),
	).to_cnf()
Net4_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(0,16+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(0,16+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net4_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net4_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(0,16+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(0,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net4_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(4,35+1)]),
	).to_cnf()
Net4_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net4_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net4_Subnet0_DR = And(Net4_Subnet0_DR_Trend, Net4_Subnet0_DR_GIL_HorMinWidth,Net4_Subnet0_DR_GIL_HorMinSpacing,Net4_Subnet0_DR_GIL_VerMinSpacing,Net4_Subnet0_DR_AIL2_VerMinWidth,Net4_Subnet0_DR_AIL2_VerMinSpacing,Net4_Subnet0_DR_VerAIL2_HorMinSpacing,Net4_Subnet0_DR_MINT1AB_HorMinWidth,Net4_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net4_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net4_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net4_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net4_Subnet0_DR_M1AB_MinWidth,Net4_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net4_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net4_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net4_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net4_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net4_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net4_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net4_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net4_Subnet0_DR_V0_HorMinSpacing,Net4_Subnet0_DR_V1_HorMinSpacing,Net4_Subnet0_DR_V0_VerMinSpacing,Net4_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net4_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet4,[12,0,0,0, 12,1,0,0, 12,2,0,0, 12,3,0,0, 12,4,0,0, 12,5,0,0, 12,6,0,0, 12,7,0,0, 12,8,0,0, 12,9,0,0, 12,10,0,0, 12,11,0,0, 12,12,0,0, 12,13,0,0, 12,14,0,0, 12,15,0,0, 12,16,0,0, 12,17,0,0, 12,18,0,0, 12,19,0,0, 12,20,0,0, 12,21,0,0, 12,22,0,0, 12,23,0,0, 12,24,0,0, 12,25,0,0, 12,26,0,0, 12,27,0,0, 12,28,0,0, 12,29,0,0, 12,30,0,0, 12,31,0,0, 12,32,0,0, 12,33,0,0, 12,34,0,0, 12,35,0,0, ],36,0,0,1,16,35,3,0),
	RConstraints.R1(Edge_Net_Subnet4,[4,0,0,0, 4,1,0,0, 4,2,0,0, 4,3,0,0, 4,4,0,0, 4,5,0,0, 4,6,0,0, 4,7,0,0, 4,8,0,0, 4,9,0,0, 4,10,0,0, 4,11,0,0, 4,12,0,0, 4,13,0,0, 4,14,0,0, 4,15,0,0, 4,16,0,0, 4,17,0,0, 4,18,0,0, 4,19,0,0, 4,20,0,0, 4,21,0,0, 4,22,0,0, 4,23,0,0, 4,24,0,0, 4,25,0,0, 4,26,0,0, 4,27,0,0, 4,28,0,0, 4,29,0,0, 4,30,0,0, 4,31,0,0, 4,32,0,0, 4,33,0,0, 4,34,0,0, 4,35,0,0, ],36,0,0,1,16,35,3,0),
	).to_cnf()
Net4_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet4,Edge,Edge_Net,[12,0,0, 12,1,0, 12,2,0, 12,3,0, 12,4,0, 12,5,0, 12,6,0, 12,7,0, 12,8,0, 12,9,0, 12,10,0, 12,11,0, 12,12,0, 12,13,0, 12,14,0, 12,15,0, 12,16,0, 12,17,0, 12,18,0, 12,19,0, 12,20,0, 12,21,0, 12,22,0, 12,23,0, 12,24,0, 12,25,0, 12,26,0, 12,27,0, 12,28,0, 12,29,0, 12,30,0, 12,31,0, 12,32,0, 12,33,0, 12,34,0, 12,35,0, 4,0,0, 4,1,0, 4,2,0, 4,3,0, 4,4,0, 4,5,0, 4,6,0, 4,7,0, 4,8,0, 4,9,0, 4,10,0, 4,11,0, 4,12,0, 4,13,0, 4,14,0, 4,15,0, 4,16,0, 4,17,0, 4,18,0, 4,19,0, 4,20,0, 4,21,0, 4,22,0, 4,23,0, 4,24,0, 4,25,0, 4,26,0, 4,27,0, 4,28,0, 4,29,0, 4,30,0, 4,31,0, 4,32,0, 4,33,0, 4,34,0, 4,35,0, ],72,0,0,0,16,35,3,0,3),
	)
Net4_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,3],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,3],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(4,12+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net4_Subnet0_R = And(Net4_Subnet0_R1,Net4_Subnet0_R2,Net4_Subnet0_R3,)
Net4_Subnet0_Formula = And(Net4_Subnet0_C,Net4_Subnet0_DR,Net4_Subnet0_R)
# Net = 4 Subnet = 1 | Left -> Right [8,42] Top -> Bottom [0,35]
# Range R1(12,12,0,35)
# Range R2(38,38,1,6)
### Disable edges outside window
Edge_Net_Subnet4[0:8,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(10368)
Edge_Net_Subnet4[42:77+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(46656)

### Consistency Constraints
Net4_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,3]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(8,42+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net4_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet4[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,3])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(8,42+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net4_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet4[x,y,2,trend,0,1],Xor(Edge_Net_Subnet4[x,y,2,trend,1,1],Edge_Net_Subnet4[x,y,2,trend,2,1])),And(~Edge_Net_Subnet4[x,y,2,trend,0,1],~Edge_Net_Subnet4[x,y,2,trend,1,1],~Edge_Net_Subnet4[x,y,2,trend,2,1]))for x in range(8,42+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net4_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet4[x,y,3,1,0,1],Xor(Edge_Net_Subnet4[x,y,3,1,1,1],Edge_Net_Subnet4[x,y,3,1,2,1])),And(~Edge_Net_Subnet4[x,y,3,1,0,1],~Edge_Net_Subnet4[x,y,3,1,1,1],~Edge_Net_Subnet4[x,y,3,1,2,1]))for x in range(8,42+1)])for y in range(0,35+1)]).to_cnf()
Net4_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet4[x,y,1,trend,2,1],Xor(Edge_Net_Subnet4[x,y,1,trend,0,1],Edge_Net_Subnet4[x,y,1,trend,1,1])),And(~Edge_Net_Subnet4[x,y,1,trend,2,1],~Edge_Net_Subnet4[x,y,1,trend,0,1],~Edge_Net_Subnet4[x,y,1,trend,1,1]))for x in range(8,42+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net4_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet4[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(8,42+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet4[x,y,z,trend,2,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(8,42+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet4[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(8,42+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet4[x,y,z,trend,1,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(8,42+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net4_Subnet1_C = And(Net4_Subnet1_C1, Net4_Subnet1_C2,Net4_Subnet1_C3_ME1_Mask,Net4_Subnet1_C4_MINT1_Mask,Net4_Subnet1_C5_AIL2GIL_Mask,Net4_Subnet1_C6,)
### Design Rules
Net4_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(8,42+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net4_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,1,1,1,1], ~Edge_Net_Subnet4[x-1,y,1,1,1,1]), And(Edge_Net_Subnet4[x+1,y,1,1,1,1], Edge_Net_Subnet4[x+2,y,1,1,1,1], Edge_Net_Subnet4[x+3,y,1,1,1,1], ))for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,1,1,1,1], ~Edge_Net_Subnet4[x+1,y,1,1,1,1]), And(Edge_Net_Subnet4[x-1,y,1,1,1,1], Edge_Net_Subnet4[x-2,y,1,1,1,1], Edge_Net_Subnet4[x-3,y,1,1,1,1], ))for x in range(8,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(8,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(8,42+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(8,42+1)])for y in range(3,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1]), And(Edge_Net_Subnet4[x,y+1,1,0,0,1], Edge_Net_Subnet4[x,y+2,1,0,0,1], Edge_Net_Subnet4[x,y+3,1,0,0,1], ))for x in range(8,42+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1]), And(Edge_Net_Subnet4[x,y-1,1,0,0,1], Edge_Net_Subnet4[x,y-2,1,0,0,1], Edge_Net_Subnet4[x,y-3,1,0,0,1], ))for x in range(8,42+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge_Net_Subnet4[x,y-1,1,0,0,1]), And(Edge_Net_Subnet4[x,y+1,1,0,0,1], Edge_Net_Subnet4[x,y+2,1,0,0,1], Edge_Net_Subnet4[x,y+3,1,0,0,1], ))for x in range(8,42+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge_Net_Subnet4[x,y+1,1,0,0,1]), And(Edge_Net_Subnet4[x,y-1,1,0,0,1], Edge_Net_Subnet4[x,y-2,1,0,0,1], Edge_Net_Subnet4[x,y-3,1,0,0,1], ))for x in range(8,42+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net4_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(8,42+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(8,42+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(8,42+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(8,42+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(8,42+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(8,42+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net4_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(8,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,3,1,mask,1], ~Edge_Net_Subnet4[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet4[x+1,y,3,1,mask,1], Edge_Net_Subnet4[x+2,y,3,1,mask,1], Edge_Net_Subnet4[x+3,y,3,1,mask,1], Edge_Net_Subnet4[x+4,y,3,1,mask,1], Edge_Net_Subnet4[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,3,1,mask,1], ~Edge_Net_Subnet4[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet4[x-1,y,3,1,mask,1], Edge_Net_Subnet4[x-2,y,3,1,mask,1], Edge_Net_Subnet4[x-3,y,3,1,mask,1], Edge_Net_Subnet4[x-4,y,3,1,mask,1], Edge_Net_Subnet4[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(3,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(8,42+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(8,42+1)])for y in range(2,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(8,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,2,1,mask,1], ~Edge_Net_Subnet4[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet4[x+1,y,2,1,mask,1], Edge_Net_Subnet4[x+2,y,2,1,mask,1], Edge_Net_Subnet4[x+3,y,2,1,mask,1], Edge_Net_Subnet4[x+4,y,2,1,mask,1], Edge_Net_Subnet4[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,2,1,mask,1], ~Edge_Net_Subnet4[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet4[x-1,y,2,1,mask,1], Edge_Net_Subnet4[x-2,y,2,1,mask,1], Edge_Net_Subnet4[x-3,y,2,1,mask,1], Edge_Net_Subnet4[x-4,y,2,1,mask,1], Edge_Net_Subnet4[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,1], And(Edge_Net_Subnet4[x-1,y,2,1,mask,1], Edge_Net_Subnet4[x-2,y,2,1,mask,1], Edge_Net_Subnet4[x-3,y,2,1,mask,1], Edge_Net_Subnet4[x-4,y,2,1,mask,1], Edge_Net_Subnet4[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(8,8+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,1], And(Edge_Net_Subnet4[x+1,y,2,1,mask,1], Edge_Net_Subnet4[x+2,y,2,1,mask,1], Edge_Net_Subnet4[x+3,y,2,1,mask,1], Edge_Net_Subnet4[x+4,y,2,1,mask,1], Edge_Net_Subnet4[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(42-1,8)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,1], ~Edge_Net_Subnet4[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet4[x,y+1,2,0,mask,1], Edge_Net_Subnet4[x,y+2,2,0,mask,1], Edge_Net_Subnet4[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,1], ~Edge_Net_Subnet4[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet4[x,y-1,2,0,mask,1], Edge_Net_Subnet4[x,y-2,2,0,mask,1], Edge_Net_Subnet4[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet4[x,y,2,0,mask,1], And(Edge_Net_Subnet4[x,y+1,2,0,mask,1], Edge_Net_Subnet4[x,y+2,2,0,mask,1], Edge_Net_Subnet4[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet4[x,y,2,0,mask,1], And(Edge_Net_Subnet4[x,y-1,2,0,mask,1], Edge_Net_Subnet4[x,y-2,2,0,mask,1], Edge_Net_Subnet4[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(35,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(8,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(8,42+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(8,42+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net4_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net4_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(8,42+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(8,42+1)])for y in range(3,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(4,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(8,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(8,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(8,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(8,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(8,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(8,42+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(8,42+1)])for y in range(2,35+1)]),
	).to_cnf()
Net4_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(8,42+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(8,42+1)])for y in range(2,35+1)]),
	).to_cnf()
Net4_Subnet1_DR = And(Net4_Subnet1_DR_Trend, Net4_Subnet1_DR_GIL_HorMinWidth,Net4_Subnet1_DR_GIL_HorMinSpacing,Net4_Subnet1_DR_GIL_VerMinSpacing,Net4_Subnet1_DR_AIL2_VerMinWidth,Net4_Subnet1_DR_AIL2_VerMinSpacing,Net4_Subnet1_DR_VerAIL2_HorMinSpacing,Net4_Subnet1_DR_MINT1AB_HorMinWidth,Net4_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net4_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net4_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net4_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net4_Subnet1_DR_M1AB_MinWidth,Net4_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net4_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net4_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net4_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net4_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net4_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net4_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net4_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net4_Subnet1_DR_V0_HorMinSpacing,Net4_Subnet1_DR_V1_HorMinSpacing,Net4_Subnet1_DR_V0_VerMinSpacing,Net4_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net4_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet4,[12,0,0,0, 12,1,0,0, 12,2,0,0, 12,3,0,0, 12,4,0,0, 12,5,0,0, 12,6,0,0, 12,7,0,0, 12,8,0,0, 12,9,0,0, 12,10,0,0, 12,11,0,0, 12,12,0,0, 12,13,0,0, 12,14,0,0, 12,15,0,0, 12,16,0,0, 12,17,0,0, 12,18,0,0, 12,19,0,0, 12,20,0,0, 12,21,0,0, 12,22,0,0, 12,23,0,0, 12,24,0,0, 12,25,0,0, 12,26,0,0, 12,27,0,0, 12,28,0,0, 12,29,0,0, 12,30,0,0, 12,31,0,0, 12,32,0,0, 12,33,0,0, 12,34,0,0, 12,35,0,0, ],36,8,0,1,42,35,3,1),
	RConstraints.R1(Edge_Net_Subnet4,[38,1,0,0, 38,2,0,0, 38,3,0,0, 38,4,0,0, 38,5,0,0, 38,6,0,0, ],6,8,0,1,42,35,3,1),
	).to_cnf()
Net4_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet4,Edge,Edge_Net,[12,0,0, 12,1,0, 12,2,0, 12,3,0, 12,4,0, 12,5,0, 12,6,0, 12,7,0, 12,8,0, 12,9,0, 12,10,0, 12,11,0, 12,12,0, 12,13,0, 12,14,0, 12,15,0, 12,16,0, 12,17,0, 12,18,0, 12,19,0, 12,20,0, 12,21,0, 12,22,0, 12,23,0, 12,24,0, 12,25,0, 12,26,0, 12,27,0, 12,28,0, 12,29,0, 12,30,0, 12,31,0, 12,32,0, 12,33,0, 12,34,0, 12,35,0, 38,1,0, 38,2,0, 38,3,0, 38,4,0, 38,5,0, 38,6,0, 38,7,0, ],43,8,0,0,42,35,3,1,3),
	)
Net4_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,3],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,2+1)])for x in range(8,42+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,3],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(4,12+1)])for x in range(8,42+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net4_Subnet1_R = And(Net4_Subnet1_R1,Net4_Subnet1_R2,Net4_Subnet1_R3,)
Net4_Subnet1_Formula = And(Net4_Subnet1_C,Net4_Subnet1_DR,Net4_Subnet1_R)
# Net = 4 Subnet = 2 | Left -> Right [34,42] Top -> Bottom [0,35]
# Range R1(38,38,1,6)
# Range R2(38,38,28,33)
### Disable edges outside window
Edge_Net_Subnet4[0:34,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(44064)
Edge_Net_Subnet4[42:77+1,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(46656)

### Consistency Constraints
Net4_Subnet2_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,3]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net4_Subnet2_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet4[x,y,z,trend,mask,2]), Edge_Net[x,y,z,trend,mask,3])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net4_Subnet2_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet4[x,y,2,trend,0,2],Xor(Edge_Net_Subnet4[x,y,2,trend,1,2],Edge_Net_Subnet4[x,y,2,trend,2,2])),And(~Edge_Net_Subnet4[x,y,2,trend,0,2],~Edge_Net_Subnet4[x,y,2,trend,1,2],~Edge_Net_Subnet4[x,y,2,trend,2,2]))for x in range(34,42+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net4_Subnet2_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet4[x,y,3,1,0,2],Xor(Edge_Net_Subnet4[x,y,3,1,1,2],Edge_Net_Subnet4[x,y,3,1,2,2])),And(~Edge_Net_Subnet4[x,y,3,1,0,2],~Edge_Net_Subnet4[x,y,3,1,1,2],~Edge_Net_Subnet4[x,y,3,1,2,2]))for x in range(34,42+1)])for y in range(0,35+1)]).to_cnf()
Net4_Subnet2_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet4[x,y,1,trend,2,2],Xor(Edge_Net_Subnet4[x,y,1,trend,0,2],Edge_Net_Subnet4[x,y,1,trend,1,2])),And(~Edge_Net_Subnet4[x,y,1,trend,2,2],~Edge_Net_Subnet4[x,y,1,trend,0,2],~Edge_Net_Subnet4[x,y,1,trend,1,2]))for x in range(34,42+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net4_Subnet2_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet4[x,y,z,trend,2,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(34,42+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet4[x,y,z,trend,1,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(34,42+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net4_Subnet2_C = And(Net4_Subnet2_C1, Net4_Subnet2_C2,Net4_Subnet2_C3_ME1_Mask,Net4_Subnet2_C4_MINT1_Mask,Net4_Subnet2_C5_AIL2GIL_Mask,Net4_Subnet2_C6,)
### Design Rules
Net4_Subnet2_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(34,42+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net4_Subnet2_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,1,1,1,2], ~Edge_Net_Subnet4[x-1,y,1,1,1,2]), And(Edge_Net_Subnet4[x+1,y,1,1,1,2], Edge_Net_Subnet4[x+2,y,1,1,1,2], Edge_Net_Subnet4[x+3,y,1,1,1,2], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,1,1,1,2], ~Edge_Net_Subnet4[x+1,y,1,1,1,2]), And(Edge_Net_Subnet4[x-1,y,1,1,1,2], Edge_Net_Subnet4[x-2,y,1,1,1,2], Edge_Net_Subnet4[x-3,y,1,1,1,2], ))for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet2_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,1,1,2], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,1,1,2], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet2_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,1,1,2], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(34,42+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,1,1,2], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(34,42+1)])for y in range(3,35+1)]),
	).to_cnf()
Net4_Subnet2_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,2]), And(Edge_Net_Subnet4[x,y+1,1,0,0,2], Edge_Net_Subnet4[x,y+2,1,0,0,2], Edge_Net_Subnet4[x,y+3,1,0,0,2], ))for x in range(34,42+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,2]), And(Edge_Net_Subnet4[x,y-1,1,0,0,2], Edge_Net_Subnet4[x,y-2,1,0,0,2], Edge_Net_Subnet4[x,y-3,1,0,0,2], ))for x in range(34,42+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,2], ~Edge_Net_Subnet4[x,y-1,1,0,0,2]), And(Edge_Net_Subnet4[x,y+1,1,0,0,2], Edge_Net_Subnet4[x,y+2,1,0,0,2], Edge_Net_Subnet4[x,y+3,1,0,0,2], ))for x in range(34,42+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,2], ~Edge_Net_Subnet4[x,y+1,1,0,0,2]), And(Edge_Net_Subnet4[x,y-1,1,0,0,2], Edge_Net_Subnet4[x,y-2,1,0,0,2], Edge_Net_Subnet4[x,y-3,1,0,0,2], ))for x in range(34,42+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net4_Subnet2_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(34,42+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(34,42+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(34,42+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(34,42+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(34,42+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(34,42+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net4_Subnet2_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,0,0,2], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,0,0,2], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet2_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,3,1,mask,2], ~Edge_Net_Subnet4[x-1,y,3,1,mask,2]), And(Edge_Net_Subnet4[x+1,y,3,1,mask,2], Edge_Net_Subnet4[x+2,y,3,1,mask,2], Edge_Net_Subnet4[x+3,y,3,1,mask,2], Edge_Net_Subnet4[x+4,y,3,1,mask,2], Edge_Net_Subnet4[x+5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,3,1,mask,2], ~Edge_Net_Subnet4[x+1,y,3,1,mask,2]), And(Edge_Net_Subnet4[x-1,y,3,1,mask,2], Edge_Net_Subnet4[x-2,y,3,1,mask,2], Edge_Net_Subnet4[x-3,y,3,1,mask,2], Edge_Net_Subnet4[x-4,y,3,1,mask,2], Edge_Net_Subnet4[x-5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet2_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,mask,2], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,mask,2], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(3,35+1)]),
	).to_cnf()
Net4_Subnet2_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,mask,2], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,mask,2], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet2_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,1,2], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(34,42+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,3,1,1,2], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(34,42+1)])for y in range(2,35+1)]),
	).to_cnf()
Net4_Subnet2_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,1,2], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,3,1,1,2], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet2_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,2,1,mask,2], ~Edge_Net_Subnet4[x-1,y,2,1,mask,2]), And(Edge_Net_Subnet4[x+1,y,2,1,mask,2], Edge_Net_Subnet4[x+2,y,2,1,mask,2], Edge_Net_Subnet4[x+3,y,2,1,mask,2], Edge_Net_Subnet4[x+4,y,2,1,mask,2], Edge_Net_Subnet4[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet4[x,y,2,1,mask,2], ~Edge_Net_Subnet4[x+1,y,2,1,mask,2]), And(Edge_Net_Subnet4[x-1,y,2,1,mask,2], Edge_Net_Subnet4[x-2,y,2,1,mask,2], Edge_Net_Subnet4[x-3,y,2,1,mask,2], Edge_Net_Subnet4[x-4,y,2,1,mask,2], Edge_Net_Subnet4[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,2], And(Edge_Net_Subnet4[x-1,y,2,1,mask,2], Edge_Net_Subnet4[x-2,y,2,1,mask,2], Edge_Net_Subnet4[x-3,y,2,1,mask,2], Edge_Net_Subnet4[x-4,y,2,1,mask,2], Edge_Net_Subnet4[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(34,34+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,2], And(Edge_Net_Subnet4[x+1,y,2,1,mask,2], Edge_Net_Subnet4[x+2,y,2,1,mask,2], Edge_Net_Subnet4[x+3,y,2,1,mask,2], Edge_Net_Subnet4[x+4,y,2,1,mask,2], Edge_Net_Subnet4[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(42-1,34)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,2], ~Edge_Net_Subnet4[x,y-1,2,0,mask,2]), And(Edge_Net_Subnet4[x,y+1,2,0,mask,2], Edge_Net_Subnet4[x,y+2,2,0,mask,2], Edge_Net_Subnet4[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,2], ~Edge_Net_Subnet4[x,y+1,2,0,mask,2]), And(Edge_Net_Subnet4[x,y-1,2,0,mask,2], Edge_Net_Subnet4[x,y-2,2,0,mask,2], Edge_Net_Subnet4[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet4[x,y,2,0,mask,2], And(Edge_Net_Subnet4[x,y+1,2,0,mask,2], Edge_Net_Subnet4[x,y+2,2,0,mask,2], Edge_Net_Subnet4[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet4[x,y,2,0,mask,2], And(Edge_Net_Subnet4[x,y-1,2,0,mask,2], Edge_Net_Subnet4[x,y-2,2,0,mask,2], Edge_Net_Subnet4[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(35,35+1)]),
	).to_cnf()
Net4_Subnet2_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,1,2], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,1,2], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet2_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,mask,2], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,1,mask,2], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet2_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,1,2], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(34,42+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,1,2], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(34,42+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net4_Subnet2_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,2], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet4[x,y,2,0,mask,2], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net4_Subnet2_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,1,2], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(34,42+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,1,2], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(34,42+1)])for y in range(3,35+1)]),
	).to_cnf()
Net4_Subnet2_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,2], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,1,mask,2], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(4,35+1)]),
	).to_cnf()
Net4_Subnet2_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,1,2], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,1,2], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(34,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet2_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,mask,2], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,0,mask,2], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	).to_cnf()
Net4_Subnet2_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,1,2,mask,2], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,1,2,mask,2], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet2_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,2,2,mask,2], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet4[x,y,2,2,mask,2], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])
	).to_cnf()
Net4_Subnet2_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,2,mask,2], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,1,2,mask,2], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(2,35+1)]),
	).to_cnf()
Net4_Subnet2_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,2,mask,2], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet4[x,y,2,2,mask,2], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(34,42+1)])for y in range(2,35+1)]),
	).to_cnf()
Net4_Subnet2_DR = And(Net4_Subnet2_DR_Trend, Net4_Subnet2_DR_GIL_HorMinWidth,Net4_Subnet2_DR_GIL_HorMinSpacing,Net4_Subnet2_DR_GIL_VerMinSpacing,Net4_Subnet2_DR_AIL2_VerMinWidth,Net4_Subnet2_DR_AIL2_VerMinSpacing,Net4_Subnet2_DR_VerAIL2_HorMinSpacing,Net4_Subnet2_DR_MINT1AB_HorMinWidth,Net4_Subnet2_DR_MINT1_SameMask_VerMinSpacing,Net4_Subnet2_DR_MINT1_SameMask_HorMinSpacing,Net4_Subnet2_DR_MINT1_DiffMask_VerMinSpacing,Net4_Subnet2_DR_MINT1_DiffMask_HorMinSpacing,Net4_Subnet2_DR_M1AB_MinWidth,Net4_Subnet2_DR_HorM1_DiffMask_HorMinSpacing,Net4_Subnet2_DR_HorM1_SameMask_HorMinSpacing,Net4_Subnet2_DR_VerM1_DiffMask_VerMinSpacing,Net4_Subnet2_DR_VerM1_SameMask_VerMinSpacing,Net4_Subnet2_DR_HorM1_DiffMask_VerMinSpacing,Net4_Subnet2_DR_HorM1_SameMask_VerMinSpacing,Net4_Subnet2_DR_VerM1_DiffMask_HorMinSpacing,Net4_Subnet2_DR_VerM1_SameMask_HorMinSpacing,Net4_Subnet2_DR_V0_HorMinSpacing,Net4_Subnet2_DR_V1_HorMinSpacing,Net4_Subnet2_DR_V0_VerMinSpacing,Net4_Subnet2_DR_V1_VerMinSpacing,)
### Routability Constraints
Net4_Subnet2_R1 = And(
	RConstraints.R1(Edge_Net_Subnet4,[38,1,0,0, 38,2,0,0, 38,3,0,0, 38,4,0,0, 38,5,0,0, 38,6,0,0, ],6,34,0,1,42,35,3,2),
	RConstraints.R1(Edge_Net_Subnet4,[38,28,0,0, 38,29,0,0, 38,30,0,0, 38,31,0,0, 38,32,0,0, 38,33,0,0, ],6,34,0,1,42,35,3,2),
	).to_cnf()
Net4_Subnet2_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet4,Edge,Edge_Net,[38,1,0, 38,2,0, 38,3,0, 38,4,0, 38,5,0, 38,6,0, 38,7,0, 38,28,0, 38,29,0, 38,30,0, 38,31,0, 38,32,0, 38,33,0, 38,34,0, ],14,34,0,0,42,35,3,2,3),
	)
Net4_Subnet2_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,3],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,2+1)])for x in range(34,42+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,3],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(4,12+1)])for x in range(34,42+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net4_Subnet2_R = And(Net4_Subnet2_R1,Net4_Subnet2_R2,Net4_Subnet2_R3,)
Net4_Subnet2_Formula = And(Net4_Subnet2_C,Net4_Subnet2_DR,Net4_Subnet2_R)
# Net = 5 Subnet = 1 | Left -> Right [12,38] Top -> Bottom [0,35]
# Range R1(16,16,0,35)
# Range R2(34,34,1,6)
### Disable edges outside window
Edge_Net_Subnet5[0:12,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(15552)
Edge_Net_Subnet5[38:77+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(51840)

### Consistency Constraints
Net5_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,4]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(12,38+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net5_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet5[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,4])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(12,38+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net5_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet5[x,y,2,trend,0,1],Xor(Edge_Net_Subnet5[x,y,2,trend,1,1],Edge_Net_Subnet5[x,y,2,trend,2,1])),And(~Edge_Net_Subnet5[x,y,2,trend,0,1],~Edge_Net_Subnet5[x,y,2,trend,1,1],~Edge_Net_Subnet5[x,y,2,trend,2,1]))for x in range(12,38+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net5_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet5[x,y,3,1,0,1],Xor(Edge_Net_Subnet5[x,y,3,1,1,1],Edge_Net_Subnet5[x,y,3,1,2,1])),And(~Edge_Net_Subnet5[x,y,3,1,0,1],~Edge_Net_Subnet5[x,y,3,1,1,1],~Edge_Net_Subnet5[x,y,3,1,2,1]))for x in range(12,38+1)])for y in range(0,35+1)]).to_cnf()
Net5_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet5[x,y,1,trend,2,1],Xor(Edge_Net_Subnet5[x,y,1,trend,0,1],Edge_Net_Subnet5[x,y,1,trend,1,1])),And(~Edge_Net_Subnet5[x,y,1,trend,2,1],~Edge_Net_Subnet5[x,y,1,trend,0,1],~Edge_Net_Subnet5[x,y,1,trend,1,1]))for x in range(12,38+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net5_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet5[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(12,38+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet5[x,y,z,trend,2,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(12,38+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet5[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(12,38+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet5[x,y,z,trend,1,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(12,38+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net5_Subnet1_C = And(Net5_Subnet1_C1, Net5_Subnet1_C2,Net5_Subnet1_C3_ME1_Mask,Net5_Subnet1_C4_MINT1_Mask,Net5_Subnet1_C5_AIL2GIL_Mask,Net5_Subnet1_C6,)
### Design Rules
Net5_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(12,38+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net5_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,1,1,1,1], ~Edge_Net_Subnet5[x-1,y,1,1,1,1]), And(Edge_Net_Subnet5[x+1,y,1,1,1,1], Edge_Net_Subnet5[x+2,y,1,1,1,1], Edge_Net_Subnet5[x+3,y,1,1,1,1], ))for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,1,1,1,1], ~Edge_Net_Subnet5[x+1,y,1,1,1,1]), And(Edge_Net_Subnet5[x-1,y,1,1,1,1], Edge_Net_Subnet5[x-2,y,1,1,1,1], Edge_Net_Subnet5[x-3,y,1,1,1,1], ))for x in range(12,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(12,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(12,38+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(12,38+1)])for y in range(3,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1]), And(Edge_Net_Subnet5[x,y+1,1,0,0,1], Edge_Net_Subnet5[x,y+2,1,0,0,1], Edge_Net_Subnet5[x,y+3,1,0,0,1], ))for x in range(12,38+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1]), And(Edge_Net_Subnet5[x,y-1,1,0,0,1], Edge_Net_Subnet5[x,y-2,1,0,0,1], Edge_Net_Subnet5[x,y-3,1,0,0,1], ))for x in range(12,38+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge_Net_Subnet5[x,y-1,1,0,0,1]), And(Edge_Net_Subnet5[x,y+1,1,0,0,1], Edge_Net_Subnet5[x,y+2,1,0,0,1], Edge_Net_Subnet5[x,y+3,1,0,0,1], ))for x in range(12,38+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge_Net_Subnet5[x,y+1,1,0,0,1]), And(Edge_Net_Subnet5[x,y-1,1,0,0,1], Edge_Net_Subnet5[x,y-2,1,0,0,1], Edge_Net_Subnet5[x,y-3,1,0,0,1], ))for x in range(12,38+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net5_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(12,38+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(12,38+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(12,38+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(12,38+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(12,38+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(12,38+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net5_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(12,38+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,3,1,mask,1], ~Edge_Net_Subnet5[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet5[x+1,y,3,1,mask,1], Edge_Net_Subnet5[x+2,y,3,1,mask,1], Edge_Net_Subnet5[x+3,y,3,1,mask,1], Edge_Net_Subnet5[x+4,y,3,1,mask,1], Edge_Net_Subnet5[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,3,1,mask,1], ~Edge_Net_Subnet5[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet5[x-1,y,3,1,mask,1], Edge_Net_Subnet5[x-2,y,3,1,mask,1], Edge_Net_Subnet5[x-3,y,3,1,mask,1], Edge_Net_Subnet5[x-4,y,3,1,mask,1], Edge_Net_Subnet5[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(3,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(12,38+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(12,38+1)])for y in range(2,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(12,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,2,1,mask,1], ~Edge_Net_Subnet5[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet5[x+1,y,2,1,mask,1], Edge_Net_Subnet5[x+2,y,2,1,mask,1], Edge_Net_Subnet5[x+3,y,2,1,mask,1], Edge_Net_Subnet5[x+4,y,2,1,mask,1], Edge_Net_Subnet5[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,2,1,mask,1], ~Edge_Net_Subnet5[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet5[x-1,y,2,1,mask,1], Edge_Net_Subnet5[x-2,y,2,1,mask,1], Edge_Net_Subnet5[x-3,y,2,1,mask,1], Edge_Net_Subnet5[x-4,y,2,1,mask,1], Edge_Net_Subnet5[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,1], And(Edge_Net_Subnet5[x-1,y,2,1,mask,1], Edge_Net_Subnet5[x-2,y,2,1,mask,1], Edge_Net_Subnet5[x-3,y,2,1,mask,1], Edge_Net_Subnet5[x-4,y,2,1,mask,1], Edge_Net_Subnet5[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(12,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,1], And(Edge_Net_Subnet5[x+1,y,2,1,mask,1], Edge_Net_Subnet5[x+2,y,2,1,mask,1], Edge_Net_Subnet5[x+3,y,2,1,mask,1], Edge_Net_Subnet5[x+4,y,2,1,mask,1], Edge_Net_Subnet5[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(38-1,12)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,1], ~Edge_Net_Subnet5[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet5[x,y+1,2,0,mask,1], Edge_Net_Subnet5[x,y+2,2,0,mask,1], Edge_Net_Subnet5[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,1], ~Edge_Net_Subnet5[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet5[x,y-1,2,0,mask,1], Edge_Net_Subnet5[x,y-2,2,0,mask,1], Edge_Net_Subnet5[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet5[x,y,2,0,mask,1], And(Edge_Net_Subnet5[x,y+1,2,0,mask,1], Edge_Net_Subnet5[x,y+2,2,0,mask,1], Edge_Net_Subnet5[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet5[x,y,2,0,mask,1], And(Edge_Net_Subnet5[x,y-1,2,0,mask,1], Edge_Net_Subnet5[x,y-2,2,0,mask,1], Edge_Net_Subnet5[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(35,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(12,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(12,38+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(12,38+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net5_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net5_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(12,38+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(12,38+1)])for y in range(3,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(4,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(12,38+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,38+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,38+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,38+1)])for y in range(2,35+1)]),
	).to_cnf()
Net5_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,38+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,38+1)])for y in range(2,35+1)]),
	).to_cnf()
Net5_Subnet1_DR = And(Net5_Subnet1_DR_Trend, Net5_Subnet1_DR_GIL_HorMinWidth,Net5_Subnet1_DR_GIL_HorMinSpacing,Net5_Subnet1_DR_GIL_VerMinSpacing,Net5_Subnet1_DR_AIL2_VerMinWidth,Net5_Subnet1_DR_AIL2_VerMinSpacing,Net5_Subnet1_DR_VerAIL2_HorMinSpacing,Net5_Subnet1_DR_MINT1AB_HorMinWidth,Net5_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net5_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net5_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net5_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net5_Subnet1_DR_M1AB_MinWidth,Net5_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net5_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net5_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net5_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net5_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net5_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net5_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net5_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net5_Subnet1_DR_V0_HorMinSpacing,Net5_Subnet1_DR_V1_HorMinSpacing,Net5_Subnet1_DR_V0_VerMinSpacing,Net5_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net5_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet5,[16,0,0,0, 16,1,0,0, 16,2,0,0, 16,3,0,0, 16,4,0,0, 16,5,0,0, 16,6,0,0, 16,7,0,0, 16,8,0,0, 16,9,0,0, 16,10,0,0, 16,11,0,0, 16,12,0,0, 16,13,0,0, 16,14,0,0, 16,15,0,0, 16,16,0,0, 16,17,0,0, 16,18,0,0, 16,19,0,0, 16,20,0,0, 16,21,0,0, 16,22,0,0, 16,23,0,0, 16,24,0,0, 16,25,0,0, 16,26,0,0, 16,27,0,0, 16,28,0,0, 16,29,0,0, 16,30,0,0, 16,31,0,0, 16,32,0,0, 16,33,0,0, 16,34,0,0, 16,35,0,0, ],36,12,0,1,38,35,3,1),
	RConstraints.R1(Edge_Net_Subnet5,[34,1,0,0, 34,2,0,0, 34,3,0,0, 34,4,0,0, 34,5,0,0, 34,6,0,0, ],6,12,0,1,38,35,3,1),
	).to_cnf()
Net5_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet5,Edge,Edge_Net,[16,0,0, 16,1,0, 16,2,0, 16,3,0, 16,4,0, 16,5,0, 16,6,0, 16,7,0, 16,8,0, 16,9,0, 16,10,0, 16,11,0, 16,12,0, 16,13,0, 16,14,0, 16,15,0, 16,16,0, 16,17,0, 16,18,0, 16,19,0, 16,20,0, 16,21,0, 16,22,0, 16,23,0, 16,24,0, 16,25,0, 16,26,0, 16,27,0, 16,28,0, 16,29,0, 16,30,0, 16,31,0, 16,32,0, 16,33,0, 16,34,0, 16,35,0, 34,1,0, 34,2,0, 34,3,0, 34,4,0, 34,5,0, 34,6,0, 34,7,0, ],43,12,0,0,38,35,3,1,4),
	)
Net5_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,4],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,3+1)])for x in range(12,38+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,4],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(5,12+1)])for x in range(12,38+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net5_Subnet1_R = And(Net5_Subnet1_R1,Net5_Subnet1_R2,Net5_Subnet1_R3,)
Net5_Subnet1_Formula = And(Net5_Subnet1_C,Net5_Subnet1_DR,Net5_Subnet1_R)
# Net = 5 Subnet = 2 | Left -> Right [30,38] Top -> Bottom [0,35]
# Range R1(34,34,1,6)
# Range R2(34,34,28,33)
### Disable edges outside window
Edge_Net_Subnet5[0:30,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(38880)
Edge_Net_Subnet5[38:77+1,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(51840)

### Consistency Constraints
Net5_Subnet2_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,4]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(30,38+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net5_Subnet2_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet5[x,y,z,trend,mask,2]), Edge_Net[x,y,z,trend,mask,4])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(30,38+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net5_Subnet2_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet5[x,y,2,trend,0,2],Xor(Edge_Net_Subnet5[x,y,2,trend,1,2],Edge_Net_Subnet5[x,y,2,trend,2,2])),And(~Edge_Net_Subnet5[x,y,2,trend,0,2],~Edge_Net_Subnet5[x,y,2,trend,1,2],~Edge_Net_Subnet5[x,y,2,trend,2,2]))for x in range(30,38+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net5_Subnet2_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet5[x,y,3,1,0,2],Xor(Edge_Net_Subnet5[x,y,3,1,1,2],Edge_Net_Subnet5[x,y,3,1,2,2])),And(~Edge_Net_Subnet5[x,y,3,1,0,2],~Edge_Net_Subnet5[x,y,3,1,1,2],~Edge_Net_Subnet5[x,y,3,1,2,2]))for x in range(30,38+1)])for y in range(0,35+1)]).to_cnf()
Net5_Subnet2_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet5[x,y,1,trend,2,2],Xor(Edge_Net_Subnet5[x,y,1,trend,0,2],Edge_Net_Subnet5[x,y,1,trend,1,2])),And(~Edge_Net_Subnet5[x,y,1,trend,2,2],~Edge_Net_Subnet5[x,y,1,trend,0,2],~Edge_Net_Subnet5[x,y,1,trend,1,2]))for x in range(30,38+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net5_Subnet2_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet5[x,y,z,trend,2,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(30,38+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet5[x,y,z,trend,1,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(30,38+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net5_Subnet2_C = And(Net5_Subnet2_C1, Net5_Subnet2_C2,Net5_Subnet2_C3_ME1_Mask,Net5_Subnet2_C4_MINT1_Mask,Net5_Subnet2_C5_AIL2GIL_Mask,Net5_Subnet2_C6,)
### Design Rules
Net5_Subnet2_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(30,38+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net5_Subnet2_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,1,1,1,2], ~Edge_Net_Subnet5[x-1,y,1,1,1,2]), And(Edge_Net_Subnet5[x+1,y,1,1,1,2], Edge_Net_Subnet5[x+2,y,1,1,1,2], Edge_Net_Subnet5[x+3,y,1,1,1,2], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,1,1,1,2], ~Edge_Net_Subnet5[x+1,y,1,1,1,2]), And(Edge_Net_Subnet5[x-1,y,1,1,1,2], Edge_Net_Subnet5[x-2,y,1,1,1,2], Edge_Net_Subnet5[x-3,y,1,1,1,2], ))for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet2_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,1,1,2], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,1,1,2], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet2_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,1,1,2], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(30,38+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,1,1,2], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(30,38+1)])for y in range(3,35+1)]),
	).to_cnf()
Net5_Subnet2_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,2]), And(Edge_Net_Subnet5[x,y+1,1,0,0,2], Edge_Net_Subnet5[x,y+2,1,0,0,2], Edge_Net_Subnet5[x,y+3,1,0,0,2], ))for x in range(30,38+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,2]), And(Edge_Net_Subnet5[x,y-1,1,0,0,2], Edge_Net_Subnet5[x,y-2,1,0,0,2], Edge_Net_Subnet5[x,y-3,1,0,0,2], ))for x in range(30,38+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,2], ~Edge_Net_Subnet5[x,y-1,1,0,0,2]), And(Edge_Net_Subnet5[x,y+1,1,0,0,2], Edge_Net_Subnet5[x,y+2,1,0,0,2], Edge_Net_Subnet5[x,y+3,1,0,0,2], ))for x in range(30,38+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,2], ~Edge_Net_Subnet5[x,y+1,1,0,0,2]), And(Edge_Net_Subnet5[x,y-1,1,0,0,2], Edge_Net_Subnet5[x,y-2,1,0,0,2], Edge_Net_Subnet5[x,y-3,1,0,0,2], ))for x in range(30,38+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net5_Subnet2_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(30,38+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(30,38+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(30,38+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(30,38+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(30,38+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(30,38+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net5_Subnet2_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,0,0,2], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,0,0,2], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet2_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,3,1,mask,2], ~Edge_Net_Subnet5[x-1,y,3,1,mask,2]), And(Edge_Net_Subnet5[x+1,y,3,1,mask,2], Edge_Net_Subnet5[x+2,y,3,1,mask,2], Edge_Net_Subnet5[x+3,y,3,1,mask,2], Edge_Net_Subnet5[x+4,y,3,1,mask,2], Edge_Net_Subnet5[x+5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,3,1,mask,2], ~Edge_Net_Subnet5[x+1,y,3,1,mask,2]), And(Edge_Net_Subnet5[x-1,y,3,1,mask,2], Edge_Net_Subnet5[x-2,y,3,1,mask,2], Edge_Net_Subnet5[x-3,y,3,1,mask,2], Edge_Net_Subnet5[x-4,y,3,1,mask,2], Edge_Net_Subnet5[x-5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet2_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,mask,2], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,mask,2], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(3,35+1)]),
	).to_cnf()
Net5_Subnet2_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,mask,2], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,mask,2], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet2_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,1,2], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(30,38+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,3,1,1,2], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(30,38+1)])for y in range(2,35+1)]),
	).to_cnf()
Net5_Subnet2_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,1,2], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,3,1,1,2], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet2_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,2,1,mask,2], ~Edge_Net_Subnet5[x-1,y,2,1,mask,2]), And(Edge_Net_Subnet5[x+1,y,2,1,mask,2], Edge_Net_Subnet5[x+2,y,2,1,mask,2], Edge_Net_Subnet5[x+3,y,2,1,mask,2], Edge_Net_Subnet5[x+4,y,2,1,mask,2], Edge_Net_Subnet5[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet5[x,y,2,1,mask,2], ~Edge_Net_Subnet5[x+1,y,2,1,mask,2]), And(Edge_Net_Subnet5[x-1,y,2,1,mask,2], Edge_Net_Subnet5[x-2,y,2,1,mask,2], Edge_Net_Subnet5[x-3,y,2,1,mask,2], Edge_Net_Subnet5[x-4,y,2,1,mask,2], Edge_Net_Subnet5[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,2], And(Edge_Net_Subnet5[x-1,y,2,1,mask,2], Edge_Net_Subnet5[x-2,y,2,1,mask,2], Edge_Net_Subnet5[x-3,y,2,1,mask,2], Edge_Net_Subnet5[x-4,y,2,1,mask,2], Edge_Net_Subnet5[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(30,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,2], And(Edge_Net_Subnet5[x+1,y,2,1,mask,2], Edge_Net_Subnet5[x+2,y,2,1,mask,2], Edge_Net_Subnet5[x+3,y,2,1,mask,2], Edge_Net_Subnet5[x+4,y,2,1,mask,2], Edge_Net_Subnet5[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(38-1,30)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,2], ~Edge_Net_Subnet5[x,y-1,2,0,mask,2]), And(Edge_Net_Subnet5[x,y+1,2,0,mask,2], Edge_Net_Subnet5[x,y+2,2,0,mask,2], Edge_Net_Subnet5[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,2], ~Edge_Net_Subnet5[x,y+1,2,0,mask,2]), And(Edge_Net_Subnet5[x,y-1,2,0,mask,2], Edge_Net_Subnet5[x,y-2,2,0,mask,2], Edge_Net_Subnet5[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet5[x,y,2,0,mask,2], And(Edge_Net_Subnet5[x,y+1,2,0,mask,2], Edge_Net_Subnet5[x,y+2,2,0,mask,2], Edge_Net_Subnet5[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet5[x,y,2,0,mask,2], And(Edge_Net_Subnet5[x,y-1,2,0,mask,2], Edge_Net_Subnet5[x,y-2,2,0,mask,2], Edge_Net_Subnet5[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(35,35+1)]),
	).to_cnf()
Net5_Subnet2_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,1,2], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,1,2], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet2_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,mask,2], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,1,mask,2], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet2_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,1,2], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(30,38+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,1,2], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(30,38+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net5_Subnet2_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,2], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet5[x,y,2,0,mask,2], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net5_Subnet2_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,1,2], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(30,38+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,1,2], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(30,38+1)])for y in range(3,35+1)]),
	).to_cnf()
Net5_Subnet2_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,2], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,1,mask,2], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(4,35+1)]),
	).to_cnf()
Net5_Subnet2_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,1,2], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,1,2], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(30,38+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet2_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,mask,2], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,0,mask,2], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	).to_cnf()
Net5_Subnet2_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,1,2,mask,2], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,1,2,mask,2], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet2_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,2,2,mask,2], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet5[x,y,2,2,mask,2], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(0,35+1)])
	).to_cnf()
Net5_Subnet2_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,2,mask,2], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,1,2,mask,2], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(2,35+1)]),
	).to_cnf()
Net5_Subnet2_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,2,mask,2], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet5[x,y,2,2,mask,2], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(30,38+1)])for y in range(2,35+1)]),
	).to_cnf()
Net5_Subnet2_DR = And(Net5_Subnet2_DR_Trend, Net5_Subnet2_DR_GIL_HorMinWidth,Net5_Subnet2_DR_GIL_HorMinSpacing,Net5_Subnet2_DR_GIL_VerMinSpacing,Net5_Subnet2_DR_AIL2_VerMinWidth,Net5_Subnet2_DR_AIL2_VerMinSpacing,Net5_Subnet2_DR_VerAIL2_HorMinSpacing,Net5_Subnet2_DR_MINT1AB_HorMinWidth,Net5_Subnet2_DR_MINT1_SameMask_VerMinSpacing,Net5_Subnet2_DR_MINT1_SameMask_HorMinSpacing,Net5_Subnet2_DR_MINT1_DiffMask_VerMinSpacing,Net5_Subnet2_DR_MINT1_DiffMask_HorMinSpacing,Net5_Subnet2_DR_M1AB_MinWidth,Net5_Subnet2_DR_HorM1_DiffMask_HorMinSpacing,Net5_Subnet2_DR_HorM1_SameMask_HorMinSpacing,Net5_Subnet2_DR_VerM1_DiffMask_VerMinSpacing,Net5_Subnet2_DR_VerM1_SameMask_VerMinSpacing,Net5_Subnet2_DR_HorM1_DiffMask_VerMinSpacing,Net5_Subnet2_DR_HorM1_SameMask_VerMinSpacing,Net5_Subnet2_DR_VerM1_DiffMask_HorMinSpacing,Net5_Subnet2_DR_VerM1_SameMask_HorMinSpacing,Net5_Subnet2_DR_V0_HorMinSpacing,Net5_Subnet2_DR_V1_HorMinSpacing,Net5_Subnet2_DR_V0_VerMinSpacing,Net5_Subnet2_DR_V1_VerMinSpacing,)
### Routability Constraints
Net5_Subnet2_R1 = And(
	RConstraints.R1(Edge_Net_Subnet5,[34,1,0,0, 34,2,0,0, 34,3,0,0, 34,4,0,0, 34,5,0,0, 34,6,0,0, ],6,30,0,1,38,35,3,2),
	RConstraints.R1(Edge_Net_Subnet5,[34,28,0,0, 34,29,0,0, 34,30,0,0, 34,31,0,0, 34,32,0,0, 34,33,0,0, ],6,30,0,1,38,35,3,2),
	).to_cnf()
Net5_Subnet2_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet5,Edge,Edge_Net,[34,1,0, 34,2,0, 34,3,0, 34,4,0, 34,5,0, 34,6,0, 34,7,0, 34,28,0, 34,29,0, 34,30,0, 34,31,0, 34,32,0, 34,33,0, 34,34,0, ],14,30,0,0,38,35,3,2,4),
	)
Net5_Subnet2_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,4],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,3+1)])for x in range(30,38+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,4],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(5,12+1)])for x in range(30,38+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net5_Subnet2_R = And(Net5_Subnet2_R1,Net5_Subnet2_R2,Net5_Subnet2_R3,)
Net5_Subnet2_Formula = And(Net5_Subnet2_C,Net5_Subnet2_DR,Net5_Subnet2_R)
# Net = 6 Subnet = 0 | Left -> Right [16,28] Top -> Bottom [0,35]
# Range R1(20,20,0,35)
# Range R2(24,24,0,35)
### Disable edges outside window
Edge_Net_Subnet6[0:16,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(20736)
Edge_Net_Subnet6[28:77+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(64800)

### Consistency Constraints
Net6_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,5]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net6_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet6[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,5])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net6_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,2,trend,0,0],Xor(Edge_Net_Subnet6[x,y,2,trend,1,0],Edge_Net_Subnet6[x,y,2,trend,2,0])),And(~Edge_Net_Subnet6[x,y,2,trend,0,0],~Edge_Net_Subnet6[x,y,2,trend,1,0],~Edge_Net_Subnet6[x,y,2,trend,2,0]))for x in range(16,28+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net6_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,3,1,0,0],Xor(Edge_Net_Subnet6[x,y,3,1,1,0],Edge_Net_Subnet6[x,y,3,1,2,0])),And(~Edge_Net_Subnet6[x,y,3,1,0,0],~Edge_Net_Subnet6[x,y,3,1,1,0],~Edge_Net_Subnet6[x,y,3,1,2,0]))for x in range(16,28+1)])for y in range(0,35+1)]).to_cnf()
Net6_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,1,trend,2,0],Xor(Edge_Net_Subnet6[x,y,1,trend,0,0],Edge_Net_Subnet6[x,y,1,trend,1,0])),And(~Edge_Net_Subnet6[x,y,1,trend,2,0],~Edge_Net_Subnet6[x,y,1,trend,0,0],~Edge_Net_Subnet6[x,y,1,trend,1,0]))for x in range(16,28+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net6_Subnet0_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,1,0], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,2,s2])for s2 in range(0+1,7)]))for trend in range(0,1+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,2,0], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,1,s2])for s2 in range(0+1,7)]))for trend in range(0,1+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net6_Subnet0_C = And(Net6_Subnet0_C1, Net6_Subnet0_C2,Net6_Subnet0_C3_ME1_Mask,Net6_Subnet0_C4_MINT1_Mask,Net6_Subnet0_C5_AIL2GIL_Mask,Net6_Subnet0_C6,)
### Design Rules
Net6_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(16,28+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net6_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,1,1,1,0], ~Edge_Net_Subnet6[x-1,y,1,1,1,0]), And(Edge_Net_Subnet6[x+1,y,1,1,1,0], Edge_Net_Subnet6[x+2,y,1,1,1,0], Edge_Net_Subnet6[x+3,y,1,1,1,0], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,1,1,1,0], ~Edge_Net_Subnet6[x+1,y,1,1,1,0]), And(Edge_Net_Subnet6[x-1,y,1,1,1,0], Edge_Net_Subnet6[x-2,y,1,1,1,0], Edge_Net_Subnet6[x-3,y,1,1,1,0], ))for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(16,28+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(16,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,0]), And(Edge_Net_Subnet6[x,y+1,1,0,0,0], Edge_Net_Subnet6[x,y+2,1,0,0,0], Edge_Net_Subnet6[x,y+3,1,0,0,0], ))for x in range(16,28+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,0]), And(Edge_Net_Subnet6[x,y-1,1,0,0,0], Edge_Net_Subnet6[x,y-2,1,0,0,0], Edge_Net_Subnet6[x,y-3,1,0,0,0], ))for x in range(16,28+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,0], ~Edge_Net_Subnet6[x,y-1,1,0,0,0]), And(Edge_Net_Subnet6[x,y+1,1,0,0,0], Edge_Net_Subnet6[x,y+2,1,0,0,0], Edge_Net_Subnet6[x,y+3,1,0,0,0], ))for x in range(16,28+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,0], ~Edge_Net_Subnet6[x,y+1,1,0,0,0]), And(Edge_Net_Subnet6[x,y-1,1,0,0,0], Edge_Net_Subnet6[x,y-2,1,0,0,0], Edge_Net_Subnet6[x,y-3,1,0,0,0], ))for x in range(16,28+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net6_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(16,28+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(16,28+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(16,28+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(16,28+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(16,28+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(16,28+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net6_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,3,1,mask,0], ~Edge_Net_Subnet6[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet6[x+1,y,3,1,mask,0], Edge_Net_Subnet6[x+2,y,3,1,mask,0], Edge_Net_Subnet6[x+3,y,3,1,mask,0], Edge_Net_Subnet6[x+4,y,3,1,mask,0], Edge_Net_Subnet6[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,3,1,mask,0], ~Edge_Net_Subnet6[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet6[x-1,y,3,1,mask,0], Edge_Net_Subnet6[x-2,y,3,1,mask,0], Edge_Net_Subnet6[x-3,y,3,1,mask,0], Edge_Net_Subnet6[x-4,y,3,1,mask,0], Edge_Net_Subnet6[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(16,28+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(16,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,2,1,mask,0], ~Edge_Net_Subnet6[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet6[x+1,y,2,1,mask,0], Edge_Net_Subnet6[x+2,y,2,1,mask,0], Edge_Net_Subnet6[x+3,y,2,1,mask,0], Edge_Net_Subnet6[x+4,y,2,1,mask,0], Edge_Net_Subnet6[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,2,1,mask,0], ~Edge_Net_Subnet6[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet6[x-1,y,2,1,mask,0], Edge_Net_Subnet6[x-2,y,2,1,mask,0], Edge_Net_Subnet6[x-3,y,2,1,mask,0], Edge_Net_Subnet6[x-4,y,2,1,mask,0], Edge_Net_Subnet6[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,0], And(Edge_Net_Subnet6[x-1,y,2,1,mask,0], Edge_Net_Subnet6[x-2,y,2,1,mask,0], Edge_Net_Subnet6[x-3,y,2,1,mask,0], Edge_Net_Subnet6[x-4,y,2,1,mask,0], Edge_Net_Subnet6[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(16,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,0], And(Edge_Net_Subnet6[x+1,y,2,1,mask,0], Edge_Net_Subnet6[x+2,y,2,1,mask,0], Edge_Net_Subnet6[x+3,y,2,1,mask,0], Edge_Net_Subnet6[x+4,y,2,1,mask,0], Edge_Net_Subnet6[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(28-1,16)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,0], ~Edge_Net_Subnet6[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet6[x,y+1,2,0,mask,0], Edge_Net_Subnet6[x,y+2,2,0,mask,0], Edge_Net_Subnet6[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,0], ~Edge_Net_Subnet6[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet6[x,y-1,2,0,mask,0], Edge_Net_Subnet6[x,y-2,2,0,mask,0], Edge_Net_Subnet6[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet6[x,y,2,0,mask,0], And(Edge_Net_Subnet6[x,y+1,2,0,mask,0], Edge_Net_Subnet6[x,y+2,2,0,mask,0], Edge_Net_Subnet6[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet6[x,y,2,0,mask,0], And(Edge_Net_Subnet6[x,y-1,2,0,mask,0], Edge_Net_Subnet6[x,y-2,2,0,mask,0], Edge_Net_Subnet6[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(35,35+1)]),
	).to_cnf()
Net6_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(16,28+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(16,28+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net6_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net6_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(16,28+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(16,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(4,35+1)]),
	).to_cnf()
Net6_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet0_DR = And(Net6_Subnet0_DR_Trend, Net6_Subnet0_DR_GIL_HorMinWidth,Net6_Subnet0_DR_GIL_HorMinSpacing,Net6_Subnet0_DR_GIL_VerMinSpacing,Net6_Subnet0_DR_AIL2_VerMinWidth,Net6_Subnet0_DR_AIL2_VerMinSpacing,Net6_Subnet0_DR_VerAIL2_HorMinSpacing,Net6_Subnet0_DR_MINT1AB_HorMinWidth,Net6_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net6_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net6_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net6_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net6_Subnet0_DR_M1AB_MinWidth,Net6_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net6_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net6_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net6_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net6_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net6_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net6_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net6_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net6_Subnet0_DR_V0_HorMinSpacing,Net6_Subnet0_DR_V1_HorMinSpacing,Net6_Subnet0_DR_V0_VerMinSpacing,Net6_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net6_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet6,[20,0,0,0, 20,1,0,0, 20,2,0,0, 20,3,0,0, 20,4,0,0, 20,5,0,0, 20,6,0,0, 20,7,0,0, 20,8,0,0, 20,9,0,0, 20,10,0,0, 20,11,0,0, 20,12,0,0, 20,13,0,0, 20,14,0,0, 20,15,0,0, 20,16,0,0, 20,17,0,0, 20,18,0,0, 20,19,0,0, 20,20,0,0, 20,21,0,0, 20,22,0,0, 20,23,0,0, 20,24,0,0, 20,25,0,0, 20,26,0,0, 20,27,0,0, 20,28,0,0, 20,29,0,0, 20,30,0,0, 20,31,0,0, 20,32,0,0, 20,33,0,0, 20,34,0,0, 20,35,0,0, ],36,16,0,1,28,35,3,0),
	RConstraints.R1(Edge_Net_Subnet6,[24,0,0,0, 24,1,0,0, 24,2,0,0, 24,3,0,0, 24,4,0,0, 24,5,0,0, 24,6,0,0, 24,7,0,0, 24,8,0,0, 24,9,0,0, 24,10,0,0, 24,11,0,0, 24,12,0,0, 24,13,0,0, 24,14,0,0, 24,15,0,0, 24,16,0,0, 24,17,0,0, 24,18,0,0, 24,19,0,0, 24,20,0,0, 24,21,0,0, 24,22,0,0, 24,23,0,0, 24,24,0,0, 24,25,0,0, 24,26,0,0, 24,27,0,0, 24,28,0,0, 24,29,0,0, 24,30,0,0, 24,31,0,0, 24,32,0,0, 24,33,0,0, 24,34,0,0, 24,35,0,0, ],36,16,0,1,28,35,3,0),
	).to_cnf()
Net6_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet6,Edge,Edge_Net,[20,0,0, 20,1,0, 20,2,0, 20,3,0, 20,4,0, 20,5,0, 20,6,0, 20,7,0, 20,8,0, 20,9,0, 20,10,0, 20,11,0, 20,12,0, 20,13,0, 20,14,0, 20,15,0, 20,16,0, 20,17,0, 20,18,0, 20,19,0, 20,20,0, 20,21,0, 20,22,0, 20,23,0, 20,24,0, 20,25,0, 20,26,0, 20,27,0, 20,28,0, 20,29,0, 20,30,0, 20,31,0, 20,32,0, 20,33,0, 20,34,0, 20,35,0, 24,0,0, 24,1,0, 24,2,0, 24,3,0, 24,4,0, 24,5,0, 24,6,0, 24,7,0, 24,8,0, 24,9,0, 24,10,0, 24,11,0, 24,12,0, 24,13,0, 24,14,0, 24,15,0, 24,16,0, 24,17,0, 24,18,0, 24,19,0, 24,20,0, 24,21,0, 24,22,0, 24,23,0, 24,24,0, 24,25,0, 24,26,0, 24,27,0, 24,28,0, 24,29,0, 24,30,0, 24,31,0, 24,32,0, 24,33,0, 24,34,0, 24,35,0, ],72,16,0,0,28,35,3,0,5),
	)
Net6_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,5],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,4+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,5],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(6,12+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net6_Subnet0_R = And(Net6_Subnet0_R1,Net6_Subnet0_R2,Net6_Subnet0_R3,)
Net6_Subnet0_Formula = And(Net6_Subnet0_C,Net6_Subnet0_DR,Net6_Subnet0_R)
# Net = 6 Subnet = 1 | Left -> Right [20,40] Top -> Bottom [0,35]
# Range R1(24,24,0,35)
# Range R2(36,36,0,35)
### Disable edges outside window
Edge_Net_Subnet6[0:20,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(25920)
Edge_Net_Subnet6[40:77+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(49248)

### Consistency Constraints
Net6_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,5]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net6_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet6[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,5])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net6_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,2,trend,0,1],Xor(Edge_Net_Subnet6[x,y,2,trend,1,1],Edge_Net_Subnet6[x,y,2,trend,2,1])),And(~Edge_Net_Subnet6[x,y,2,trend,0,1],~Edge_Net_Subnet6[x,y,2,trend,1,1],~Edge_Net_Subnet6[x,y,2,trend,2,1]))for x in range(20,40+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net6_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,3,1,0,1],Xor(Edge_Net_Subnet6[x,y,3,1,1,1],Edge_Net_Subnet6[x,y,3,1,2,1])),And(~Edge_Net_Subnet6[x,y,3,1,0,1],~Edge_Net_Subnet6[x,y,3,1,1,1],~Edge_Net_Subnet6[x,y,3,1,2,1]))for x in range(20,40+1)])for y in range(0,35+1)]).to_cnf()
Net6_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,1,trend,2,1],Xor(Edge_Net_Subnet6[x,y,1,trend,0,1],Edge_Net_Subnet6[x,y,1,trend,1,1])),And(~Edge_Net_Subnet6[x,y,1,trend,2,1],~Edge_Net_Subnet6[x,y,1,trend,0,1],~Edge_Net_Subnet6[x,y,1,trend,1,1]))for x in range(20,40+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net6_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,2,s2])for s2 in range(1+1,7)]))for trend in range(0,1+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,1,s2])for s2 in range(1+1,7)]))for trend in range(0,1+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net6_Subnet1_C = And(Net6_Subnet1_C1, Net6_Subnet1_C2,Net6_Subnet1_C3_ME1_Mask,Net6_Subnet1_C4_MINT1_Mask,Net6_Subnet1_C5_AIL2GIL_Mask,Net6_Subnet1_C6,)
### Design Rules
Net6_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(20,40+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net6_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,1,1,1,1], ~Edge_Net_Subnet6[x-1,y,1,1,1,1]), And(Edge_Net_Subnet6[x+1,y,1,1,1,1], Edge_Net_Subnet6[x+2,y,1,1,1,1], Edge_Net_Subnet6[x+3,y,1,1,1,1], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,1,1,1,1], ~Edge_Net_Subnet6[x+1,y,1,1,1,1]), And(Edge_Net_Subnet6[x-1,y,1,1,1,1], Edge_Net_Subnet6[x-2,y,1,1,1,1], Edge_Net_Subnet6[x-3,y,1,1,1,1], ))for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(20,40+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(20,40+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,1]), And(Edge_Net_Subnet6[x,y+1,1,0,0,1], Edge_Net_Subnet6[x,y+2,1,0,0,1], Edge_Net_Subnet6[x,y+3,1,0,0,1], ))for x in range(20,40+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,1]), And(Edge_Net_Subnet6[x,y-1,1,0,0,1], Edge_Net_Subnet6[x,y-2,1,0,0,1], Edge_Net_Subnet6[x,y-3,1,0,0,1], ))for x in range(20,40+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,1], ~Edge_Net_Subnet6[x,y-1,1,0,0,1]), And(Edge_Net_Subnet6[x,y+1,1,0,0,1], Edge_Net_Subnet6[x,y+2,1,0,0,1], Edge_Net_Subnet6[x,y+3,1,0,0,1], ))for x in range(20,40+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,1], ~Edge_Net_Subnet6[x,y+1,1,0,0,1]), And(Edge_Net_Subnet6[x,y-1,1,0,0,1], Edge_Net_Subnet6[x,y-2,1,0,0,1], Edge_Net_Subnet6[x,y-3,1,0,0,1], ))for x in range(20,40+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net6_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(20,40+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(20,40+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(20,40+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(20,40+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(20,40+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(20,40+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net6_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,3,1,mask,1], ~Edge_Net_Subnet6[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet6[x+1,y,3,1,mask,1], Edge_Net_Subnet6[x+2,y,3,1,mask,1], Edge_Net_Subnet6[x+3,y,3,1,mask,1], Edge_Net_Subnet6[x+4,y,3,1,mask,1], Edge_Net_Subnet6[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,3,1,mask,1], ~Edge_Net_Subnet6[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet6[x-1,y,3,1,mask,1], Edge_Net_Subnet6[x-2,y,3,1,mask,1], Edge_Net_Subnet6[x-3,y,3,1,mask,1], Edge_Net_Subnet6[x-4,y,3,1,mask,1], Edge_Net_Subnet6[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(20,40+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(20,40+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,2,1,mask,1], ~Edge_Net_Subnet6[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet6[x+1,y,2,1,mask,1], Edge_Net_Subnet6[x+2,y,2,1,mask,1], Edge_Net_Subnet6[x+3,y,2,1,mask,1], Edge_Net_Subnet6[x+4,y,2,1,mask,1], Edge_Net_Subnet6[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,2,1,mask,1], ~Edge_Net_Subnet6[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet6[x-1,y,2,1,mask,1], Edge_Net_Subnet6[x-2,y,2,1,mask,1], Edge_Net_Subnet6[x-3,y,2,1,mask,1], Edge_Net_Subnet6[x-4,y,2,1,mask,1], Edge_Net_Subnet6[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,1], And(Edge_Net_Subnet6[x-1,y,2,1,mask,1], Edge_Net_Subnet6[x-2,y,2,1,mask,1], Edge_Net_Subnet6[x-3,y,2,1,mask,1], Edge_Net_Subnet6[x-4,y,2,1,mask,1], Edge_Net_Subnet6[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(20,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,1], And(Edge_Net_Subnet6[x+1,y,2,1,mask,1], Edge_Net_Subnet6[x+2,y,2,1,mask,1], Edge_Net_Subnet6[x+3,y,2,1,mask,1], Edge_Net_Subnet6[x+4,y,2,1,mask,1], Edge_Net_Subnet6[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(40-1,20)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,1], ~Edge_Net_Subnet6[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet6[x,y+1,2,0,mask,1], Edge_Net_Subnet6[x,y+2,2,0,mask,1], Edge_Net_Subnet6[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,1], ~Edge_Net_Subnet6[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet6[x,y-1,2,0,mask,1], Edge_Net_Subnet6[x,y-2,2,0,mask,1], Edge_Net_Subnet6[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet6[x,y,2,0,mask,1], And(Edge_Net_Subnet6[x,y+1,2,0,mask,1], Edge_Net_Subnet6[x,y+2,2,0,mask,1], Edge_Net_Subnet6[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet6[x,y,2,0,mask,1], And(Edge_Net_Subnet6[x,y-1,2,0,mask,1], Edge_Net_Subnet6[x,y-2,2,0,mask,1], Edge_Net_Subnet6[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(35,35+1)]),
	).to_cnf()
Net6_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(20,40+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(20,40+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net6_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net6_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(20,40+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(20,40+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(4,35+1)]),
	).to_cnf()
Net6_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet1_DR = And(Net6_Subnet1_DR_Trend, Net6_Subnet1_DR_GIL_HorMinWidth,Net6_Subnet1_DR_GIL_HorMinSpacing,Net6_Subnet1_DR_GIL_VerMinSpacing,Net6_Subnet1_DR_AIL2_VerMinWidth,Net6_Subnet1_DR_AIL2_VerMinSpacing,Net6_Subnet1_DR_VerAIL2_HorMinSpacing,Net6_Subnet1_DR_MINT1AB_HorMinWidth,Net6_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net6_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net6_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net6_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net6_Subnet1_DR_M1AB_MinWidth,Net6_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net6_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net6_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net6_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net6_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net6_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net6_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net6_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net6_Subnet1_DR_V0_HorMinSpacing,Net6_Subnet1_DR_V1_HorMinSpacing,Net6_Subnet1_DR_V0_VerMinSpacing,Net6_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net6_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet6,[24,0,0,0, 24,1,0,0, 24,2,0,0, 24,3,0,0, 24,4,0,0, 24,5,0,0, 24,6,0,0, 24,7,0,0, 24,8,0,0, 24,9,0,0, 24,10,0,0, 24,11,0,0, 24,12,0,0, 24,13,0,0, 24,14,0,0, 24,15,0,0, 24,16,0,0, 24,17,0,0, 24,18,0,0, 24,19,0,0, 24,20,0,0, 24,21,0,0, 24,22,0,0, 24,23,0,0, 24,24,0,0, 24,25,0,0, 24,26,0,0, 24,27,0,0, 24,28,0,0, 24,29,0,0, 24,30,0,0, 24,31,0,0, 24,32,0,0, 24,33,0,0, 24,34,0,0, 24,35,0,0, ],36,20,0,1,40,35,3,1),
	RConstraints.R1(Edge_Net_Subnet6,[36,0,0,0, 36,1,0,0, 36,2,0,0, 36,3,0,0, 36,4,0,0, 36,5,0,0, 36,6,0,0, 36,7,0,0, 36,8,0,0, 36,9,0,0, 36,10,0,0, 36,11,0,0, 36,12,0,0, 36,13,0,0, 36,14,0,0, 36,15,0,0, 36,16,0,0, 36,17,0,0, 36,18,0,0, 36,19,0,0, 36,20,0,0, 36,21,0,0, 36,22,0,0, 36,23,0,0, 36,24,0,0, 36,25,0,0, 36,26,0,0, 36,27,0,0, 36,28,0,0, 36,29,0,0, 36,30,0,0, 36,31,0,0, 36,32,0,0, 36,33,0,0, 36,34,0,0, 36,35,0,0, ],36,20,0,1,40,35,3,1),
	).to_cnf()
Net6_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet6,Edge,Edge_Net,[24,0,0, 24,1,0, 24,2,0, 24,3,0, 24,4,0, 24,5,0, 24,6,0, 24,7,0, 24,8,0, 24,9,0, 24,10,0, 24,11,0, 24,12,0, 24,13,0, 24,14,0, 24,15,0, 24,16,0, 24,17,0, 24,18,0, 24,19,0, 24,20,0, 24,21,0, 24,22,0, 24,23,0, 24,24,0, 24,25,0, 24,26,0, 24,27,0, 24,28,0, 24,29,0, 24,30,0, 24,31,0, 24,32,0, 24,33,0, 24,34,0, 24,35,0, 36,0,0, 36,1,0, 36,2,0, 36,3,0, 36,4,0, 36,5,0, 36,6,0, 36,7,0, 36,8,0, 36,9,0, 36,10,0, 36,11,0, 36,12,0, 36,13,0, 36,14,0, 36,15,0, 36,16,0, 36,17,0, 36,18,0, 36,19,0, 36,20,0, 36,21,0, 36,22,0, 36,23,0, 36,24,0, 36,25,0, 36,26,0, 36,27,0, 36,28,0, 36,29,0, 36,30,0, 36,31,0, 36,32,0, 36,33,0, 36,34,0, 36,35,0, ],72,20,0,0,40,35,3,1,5),
	)
Net6_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,5],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,4+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,5],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(6,12+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net6_Subnet1_R = And(Net6_Subnet1_R1,Net6_Subnet1_R2,Net6_Subnet1_R3,)
Net6_Subnet1_Formula = And(Net6_Subnet1_C,Net6_Subnet1_DR,Net6_Subnet1_R)
# Net = 6 Subnet = 2 | Left -> Right [32,44] Top -> Bottom [0,35]
# Range R1(36,36,0,35)
# Range R2(40,40,0,35)
### Disable edges outside window
Edge_Net_Subnet6[0:32,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(41472)
Edge_Net_Subnet6[44:77+1,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(44064)

### Consistency Constraints
Net6_Subnet2_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,5]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net6_Subnet2_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet6[x,y,z,trend,mask,2]), Edge_Net[x,y,z,trend,mask,5])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net6_Subnet2_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,2,trend,0,2],Xor(Edge_Net_Subnet6[x,y,2,trend,1,2],Edge_Net_Subnet6[x,y,2,trend,2,2])),And(~Edge_Net_Subnet6[x,y,2,trend,0,2],~Edge_Net_Subnet6[x,y,2,trend,1,2],~Edge_Net_Subnet6[x,y,2,trend,2,2]))for x in range(32,44+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net6_Subnet2_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,3,1,0,2],Xor(Edge_Net_Subnet6[x,y,3,1,1,2],Edge_Net_Subnet6[x,y,3,1,2,2])),And(~Edge_Net_Subnet6[x,y,3,1,0,2],~Edge_Net_Subnet6[x,y,3,1,1,2],~Edge_Net_Subnet6[x,y,3,1,2,2]))for x in range(32,44+1)])for y in range(0,35+1)]).to_cnf()
Net6_Subnet2_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,1,trend,2,2],Xor(Edge_Net_Subnet6[x,y,1,trend,0,2],Edge_Net_Subnet6[x,y,1,trend,1,2])),And(~Edge_Net_Subnet6[x,y,1,trend,2,2],~Edge_Net_Subnet6[x,y,1,trend,0,2],~Edge_Net_Subnet6[x,y,1,trend,1,2]))for x in range(32,44+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net6_Subnet2_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,2,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,2,s2])for s2 in range(2+1,7)]))for trend in range(0,1+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,1,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,1,s2])for s2 in range(2+1,7)]))for trend in range(0,1+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net6_Subnet2_C = And(Net6_Subnet2_C1, Net6_Subnet2_C2,Net6_Subnet2_C3_ME1_Mask,Net6_Subnet2_C4_MINT1_Mask,Net6_Subnet2_C5_AIL2GIL_Mask,Net6_Subnet2_C6,)
### Design Rules
Net6_Subnet2_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(32,44+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net6_Subnet2_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,1,1,1,2], ~Edge_Net_Subnet6[x-1,y,1,1,1,2]), And(Edge_Net_Subnet6[x+1,y,1,1,1,2], Edge_Net_Subnet6[x+2,y,1,1,1,2], Edge_Net_Subnet6[x+3,y,1,1,1,2], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,1,1,1,2], ~Edge_Net_Subnet6[x+1,y,1,1,1,2]), And(Edge_Net_Subnet6[x-1,y,1,1,1,2], Edge_Net_Subnet6[x-2,y,1,1,1,2], Edge_Net_Subnet6[x-3,y,1,1,1,2], ))for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet2_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,1,1,2], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,1,1,2], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet2_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,1,1,2], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(32,44+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,1,1,2], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(32,44+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet2_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,2]), And(Edge_Net_Subnet6[x,y+1,1,0,0,2], Edge_Net_Subnet6[x,y+2,1,0,0,2], Edge_Net_Subnet6[x,y+3,1,0,0,2], ))for x in range(32,44+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,2]), And(Edge_Net_Subnet6[x,y-1,1,0,0,2], Edge_Net_Subnet6[x,y-2,1,0,0,2], Edge_Net_Subnet6[x,y-3,1,0,0,2], ))for x in range(32,44+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,2], ~Edge_Net_Subnet6[x,y-1,1,0,0,2]), And(Edge_Net_Subnet6[x,y+1,1,0,0,2], Edge_Net_Subnet6[x,y+2,1,0,0,2], Edge_Net_Subnet6[x,y+3,1,0,0,2], ))for x in range(32,44+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,2], ~Edge_Net_Subnet6[x,y+1,1,0,0,2]), And(Edge_Net_Subnet6[x,y-1,1,0,0,2], Edge_Net_Subnet6[x,y-2,1,0,0,2], Edge_Net_Subnet6[x,y-3,1,0,0,2], ))for x in range(32,44+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net6_Subnet2_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(32,44+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(32,44+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(32,44+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(32,44+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(32,44+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(32,44+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net6_Subnet2_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,0,0,2], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,0,0,2], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet2_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,3,1,mask,2], ~Edge_Net_Subnet6[x-1,y,3,1,mask,2]), And(Edge_Net_Subnet6[x+1,y,3,1,mask,2], Edge_Net_Subnet6[x+2,y,3,1,mask,2], Edge_Net_Subnet6[x+3,y,3,1,mask,2], Edge_Net_Subnet6[x+4,y,3,1,mask,2], Edge_Net_Subnet6[x+5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,3,1,mask,2], ~Edge_Net_Subnet6[x+1,y,3,1,mask,2]), And(Edge_Net_Subnet6[x-1,y,3,1,mask,2], Edge_Net_Subnet6[x-2,y,3,1,mask,2], Edge_Net_Subnet6[x-3,y,3,1,mask,2], Edge_Net_Subnet6[x-4,y,3,1,mask,2], Edge_Net_Subnet6[x-5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet2_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,mask,2], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,mask,2], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet2_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,mask,2], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,mask,2], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet2_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,1,2], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(32,44+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,1,2], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(32,44+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet2_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,1,2], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,1,2], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet2_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,2,1,mask,2], ~Edge_Net_Subnet6[x-1,y,2,1,mask,2]), And(Edge_Net_Subnet6[x+1,y,2,1,mask,2], Edge_Net_Subnet6[x+2,y,2,1,mask,2], Edge_Net_Subnet6[x+3,y,2,1,mask,2], Edge_Net_Subnet6[x+4,y,2,1,mask,2], Edge_Net_Subnet6[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,2,1,mask,2], ~Edge_Net_Subnet6[x+1,y,2,1,mask,2]), And(Edge_Net_Subnet6[x-1,y,2,1,mask,2], Edge_Net_Subnet6[x-2,y,2,1,mask,2], Edge_Net_Subnet6[x-3,y,2,1,mask,2], Edge_Net_Subnet6[x-4,y,2,1,mask,2], Edge_Net_Subnet6[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,2], And(Edge_Net_Subnet6[x-1,y,2,1,mask,2], Edge_Net_Subnet6[x-2,y,2,1,mask,2], Edge_Net_Subnet6[x-3,y,2,1,mask,2], Edge_Net_Subnet6[x-4,y,2,1,mask,2], Edge_Net_Subnet6[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(32,32+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,2], And(Edge_Net_Subnet6[x+1,y,2,1,mask,2], Edge_Net_Subnet6[x+2,y,2,1,mask,2], Edge_Net_Subnet6[x+3,y,2,1,mask,2], Edge_Net_Subnet6[x+4,y,2,1,mask,2], Edge_Net_Subnet6[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(44-1,32)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,2], ~Edge_Net_Subnet6[x,y-1,2,0,mask,2]), And(Edge_Net_Subnet6[x,y+1,2,0,mask,2], Edge_Net_Subnet6[x,y+2,2,0,mask,2], Edge_Net_Subnet6[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,2], ~Edge_Net_Subnet6[x,y+1,2,0,mask,2]), And(Edge_Net_Subnet6[x,y-1,2,0,mask,2], Edge_Net_Subnet6[x,y-2,2,0,mask,2], Edge_Net_Subnet6[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet6[x,y,2,0,mask,2], And(Edge_Net_Subnet6[x,y+1,2,0,mask,2], Edge_Net_Subnet6[x,y+2,2,0,mask,2], Edge_Net_Subnet6[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet6[x,y,2,0,mask,2], And(Edge_Net_Subnet6[x,y-1,2,0,mask,2], Edge_Net_Subnet6[x,y-2,2,0,mask,2], Edge_Net_Subnet6[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(35,35+1)]),
	).to_cnf()
Net6_Subnet2_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,1,2], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,1,2], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet2_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,mask,2], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,mask,2], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet2_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,1,2], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(32,44+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,1,2], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(32,44+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net6_Subnet2_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,2], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,2], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net6_Subnet2_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,1,2], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(32,44+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,1,2], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(32,44+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet2_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,2], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,2], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(4,35+1)]),
	).to_cnf()
Net6_Subnet2_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,1,2], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,1,2], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet2_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,mask,2], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,mask,2], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet2_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,1,2,mask,2], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,1,2,mask,2], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet2_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,2,2,mask,2], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,2,2,mask,2], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet2_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,2,mask,2], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,2,mask,2], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet2_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,2,mask,2], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,2,mask,2], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet2_DR = And(Net6_Subnet2_DR_Trend, Net6_Subnet2_DR_GIL_HorMinWidth,Net6_Subnet2_DR_GIL_HorMinSpacing,Net6_Subnet2_DR_GIL_VerMinSpacing,Net6_Subnet2_DR_AIL2_VerMinWidth,Net6_Subnet2_DR_AIL2_VerMinSpacing,Net6_Subnet2_DR_VerAIL2_HorMinSpacing,Net6_Subnet2_DR_MINT1AB_HorMinWidth,Net6_Subnet2_DR_MINT1_SameMask_VerMinSpacing,Net6_Subnet2_DR_MINT1_SameMask_HorMinSpacing,Net6_Subnet2_DR_MINT1_DiffMask_VerMinSpacing,Net6_Subnet2_DR_MINT1_DiffMask_HorMinSpacing,Net6_Subnet2_DR_M1AB_MinWidth,Net6_Subnet2_DR_HorM1_DiffMask_HorMinSpacing,Net6_Subnet2_DR_HorM1_SameMask_HorMinSpacing,Net6_Subnet2_DR_VerM1_DiffMask_VerMinSpacing,Net6_Subnet2_DR_VerM1_SameMask_VerMinSpacing,Net6_Subnet2_DR_HorM1_DiffMask_VerMinSpacing,Net6_Subnet2_DR_HorM1_SameMask_VerMinSpacing,Net6_Subnet2_DR_VerM1_DiffMask_HorMinSpacing,Net6_Subnet2_DR_VerM1_SameMask_HorMinSpacing,Net6_Subnet2_DR_V0_HorMinSpacing,Net6_Subnet2_DR_V1_HorMinSpacing,Net6_Subnet2_DR_V0_VerMinSpacing,Net6_Subnet2_DR_V1_VerMinSpacing,)
### Routability Constraints
Net6_Subnet2_R1 = And(
	RConstraints.R1(Edge_Net_Subnet6,[36,0,0,0, 36,1,0,0, 36,2,0,0, 36,3,0,0, 36,4,0,0, 36,5,0,0, 36,6,0,0, 36,7,0,0, 36,8,0,0, 36,9,0,0, 36,10,0,0, 36,11,0,0, 36,12,0,0, 36,13,0,0, 36,14,0,0, 36,15,0,0, 36,16,0,0, 36,17,0,0, 36,18,0,0, 36,19,0,0, 36,20,0,0, 36,21,0,0, 36,22,0,0, 36,23,0,0, 36,24,0,0, 36,25,0,0, 36,26,0,0, 36,27,0,0, 36,28,0,0, 36,29,0,0, 36,30,0,0, 36,31,0,0, 36,32,0,0, 36,33,0,0, 36,34,0,0, 36,35,0,0, ],36,32,0,1,44,35,3,2),
	RConstraints.R1(Edge_Net_Subnet6,[40,0,0,0, 40,1,0,0, 40,2,0,0, 40,3,0,0, 40,4,0,0, 40,5,0,0, 40,6,0,0, 40,7,0,0, 40,8,0,0, 40,9,0,0, 40,10,0,0, 40,11,0,0, 40,12,0,0, 40,13,0,0, 40,14,0,0, 40,15,0,0, 40,16,0,0, 40,17,0,0, 40,18,0,0, 40,19,0,0, 40,20,0,0, 40,21,0,0, 40,22,0,0, 40,23,0,0, 40,24,0,0, 40,25,0,0, 40,26,0,0, 40,27,0,0, 40,28,0,0, 40,29,0,0, 40,30,0,0, 40,31,0,0, 40,32,0,0, 40,33,0,0, 40,34,0,0, 40,35,0,0, ],36,32,0,1,44,35,3,2),
	).to_cnf()
Net6_Subnet2_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet6,Edge,Edge_Net,[36,0,0, 36,1,0, 36,2,0, 36,3,0, 36,4,0, 36,5,0, 36,6,0, 36,7,0, 36,8,0, 36,9,0, 36,10,0, 36,11,0, 36,12,0, 36,13,0, 36,14,0, 36,15,0, 36,16,0, 36,17,0, 36,18,0, 36,19,0, 36,20,0, 36,21,0, 36,22,0, 36,23,0, 36,24,0, 36,25,0, 36,26,0, 36,27,0, 36,28,0, 36,29,0, 36,30,0, 36,31,0, 36,32,0, 36,33,0, 36,34,0, 36,35,0, 40,0,0, 40,1,0, 40,2,0, 40,3,0, 40,4,0, 40,5,0, 40,6,0, 40,7,0, 40,8,0, 40,9,0, 40,10,0, 40,11,0, 40,12,0, 40,13,0, 40,14,0, 40,15,0, 40,16,0, 40,17,0, 40,18,0, 40,19,0, 40,20,0, 40,21,0, 40,22,0, 40,23,0, 40,24,0, 40,25,0, 40,26,0, 40,27,0, 40,28,0, 40,29,0, 40,30,0, 40,31,0, 40,32,0, 40,33,0, 40,34,0, 40,35,0, ],72,32,0,0,44,35,3,2,5),
	)
Net6_Subnet2_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,5],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,4+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,5],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(6,12+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net6_Subnet2_R = And(Net6_Subnet2_R1,Net6_Subnet2_R2,Net6_Subnet2_R3,)
Net6_Subnet2_Formula = And(Net6_Subnet2_C,Net6_Subnet2_DR,Net6_Subnet2_R)
# Net = 6 Subnet = 3 | Left -> Right [16,40] Top -> Bottom [0,35]
# Range R1(36,36,0,35)
# Range R2(20,20,0,35)
### Disable edges outside window
Edge_Net_Subnet6[0:16,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(20736)
Edge_Net_Subnet6[40:77+1,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(49248)

### Consistency Constraints
Net6_Subnet3_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,5]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(16,40+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net6_Subnet3_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet6[x,y,z,trend,mask,3]), Edge_Net[x,y,z,trend,mask,5])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(16,40+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net6_Subnet3_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,2,trend,0,3],Xor(Edge_Net_Subnet6[x,y,2,trend,1,3],Edge_Net_Subnet6[x,y,2,trend,2,3])),And(~Edge_Net_Subnet6[x,y,2,trend,0,3],~Edge_Net_Subnet6[x,y,2,trend,1,3],~Edge_Net_Subnet6[x,y,2,trend,2,3]))for x in range(16,40+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net6_Subnet3_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,3,1,0,3],Xor(Edge_Net_Subnet6[x,y,3,1,1,3],Edge_Net_Subnet6[x,y,3,1,2,3])),And(~Edge_Net_Subnet6[x,y,3,1,0,3],~Edge_Net_Subnet6[x,y,3,1,1,3],~Edge_Net_Subnet6[x,y,3,1,2,3]))for x in range(16,40+1)])for y in range(0,35+1)]).to_cnf()
Net6_Subnet3_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,1,trend,2,3],Xor(Edge_Net_Subnet6[x,y,1,trend,0,3],Edge_Net_Subnet6[x,y,1,trend,1,3])),And(~Edge_Net_Subnet6[x,y,1,trend,2,3],~Edge_Net_Subnet6[x,y,1,trend,0,3],~Edge_Net_Subnet6[x,y,1,trend,1,3]))for x in range(16,40+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net6_Subnet3_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,2,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(16,40+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,2,s2])for s2 in range(3+1,7)]))for trend in range(0,1+1)])for x in range(16,40+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,1,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(16,40+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,1,s2])for s2 in range(3+1,7)]))for trend in range(0,1+1)])for x in range(16,40+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net6_Subnet3_C = And(Net6_Subnet3_C1, Net6_Subnet3_C2,Net6_Subnet3_C3_ME1_Mask,Net6_Subnet3_C4_MINT1_Mask,Net6_Subnet3_C5_AIL2GIL_Mask,Net6_Subnet3_C6,)
### Design Rules
Net6_Subnet3_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(16,40+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net6_Subnet3_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,1,1,1,3], ~Edge_Net_Subnet6[x-1,y,1,1,1,3]), And(Edge_Net_Subnet6[x+1,y,1,1,1,3], Edge_Net_Subnet6[x+2,y,1,1,1,3], Edge_Net_Subnet6[x+3,y,1,1,1,3], ))for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,1,1,1,3], ~Edge_Net_Subnet6[x+1,y,1,1,1,3]), And(Edge_Net_Subnet6[x-1,y,1,1,1,3], Edge_Net_Subnet6[x-2,y,1,1,1,3], Edge_Net_Subnet6[x-3,y,1,1,1,3], ))for x in range(16,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet3_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,1,1,3], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,1,1,3], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(16,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet3_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,1,1,3], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(16,40+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,1,1,3], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(16,40+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet3_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,3]), And(Edge_Net_Subnet6[x,y+1,1,0,0,3], Edge_Net_Subnet6[x,y+2,1,0,0,3], Edge_Net_Subnet6[x,y+3,1,0,0,3], ))for x in range(16,40+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,3]), And(Edge_Net_Subnet6[x,y-1,1,0,0,3], Edge_Net_Subnet6[x,y-2,1,0,0,3], Edge_Net_Subnet6[x,y-3,1,0,0,3], ))for x in range(16,40+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,3], ~Edge_Net_Subnet6[x,y-1,1,0,0,3]), And(Edge_Net_Subnet6[x,y+1,1,0,0,3], Edge_Net_Subnet6[x,y+2,1,0,0,3], Edge_Net_Subnet6[x,y+3,1,0,0,3], ))for x in range(16,40+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,3], ~Edge_Net_Subnet6[x,y+1,1,0,0,3]), And(Edge_Net_Subnet6[x,y-1,1,0,0,3], Edge_Net_Subnet6[x,y-2,1,0,0,3], Edge_Net_Subnet6[x,y-3,1,0,0,3], ))for x in range(16,40+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net6_Subnet3_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(16,40+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(16,40+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(16,40+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(16,40+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(16,40+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(16,40+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net6_Subnet3_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,0,0,3], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,0,0,3], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(16,40+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet3_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,3,1,mask,3], ~Edge_Net_Subnet6[x-1,y,3,1,mask,3]), And(Edge_Net_Subnet6[x+1,y,3,1,mask,3], Edge_Net_Subnet6[x+2,y,3,1,mask,3], Edge_Net_Subnet6[x+3,y,3,1,mask,3], Edge_Net_Subnet6[x+4,y,3,1,mask,3], Edge_Net_Subnet6[x+5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,3,1,mask,3], ~Edge_Net_Subnet6[x+1,y,3,1,mask,3]), And(Edge_Net_Subnet6[x-1,y,3,1,mask,3], Edge_Net_Subnet6[x-2,y,3,1,mask,3], Edge_Net_Subnet6[x-3,y,3,1,mask,3], Edge_Net_Subnet6[x-4,y,3,1,mask,3], Edge_Net_Subnet6[x-5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet3_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,mask,3], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,mask,3], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet3_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,mask,3], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,mask,3], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet3_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,1,3], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(16,40+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,1,3], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(16,40+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet3_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,1,3], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,1,3], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(16,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet3_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,2,1,mask,3], ~Edge_Net_Subnet6[x-1,y,2,1,mask,3]), And(Edge_Net_Subnet6[x+1,y,2,1,mask,3], Edge_Net_Subnet6[x+2,y,2,1,mask,3], Edge_Net_Subnet6[x+3,y,2,1,mask,3], Edge_Net_Subnet6[x+4,y,2,1,mask,3], Edge_Net_Subnet6[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,2,1,mask,3], ~Edge_Net_Subnet6[x+1,y,2,1,mask,3]), And(Edge_Net_Subnet6[x-1,y,2,1,mask,3], Edge_Net_Subnet6[x-2,y,2,1,mask,3], Edge_Net_Subnet6[x-3,y,2,1,mask,3], Edge_Net_Subnet6[x-4,y,2,1,mask,3], Edge_Net_Subnet6[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,3], And(Edge_Net_Subnet6[x-1,y,2,1,mask,3], Edge_Net_Subnet6[x-2,y,2,1,mask,3], Edge_Net_Subnet6[x-3,y,2,1,mask,3], Edge_Net_Subnet6[x-4,y,2,1,mask,3], Edge_Net_Subnet6[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(16,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,3], And(Edge_Net_Subnet6[x+1,y,2,1,mask,3], Edge_Net_Subnet6[x+2,y,2,1,mask,3], Edge_Net_Subnet6[x+3,y,2,1,mask,3], Edge_Net_Subnet6[x+4,y,2,1,mask,3], Edge_Net_Subnet6[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(40-1,16)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,3], ~Edge_Net_Subnet6[x,y-1,2,0,mask,3]), And(Edge_Net_Subnet6[x,y+1,2,0,mask,3], Edge_Net_Subnet6[x,y+2,2,0,mask,3], Edge_Net_Subnet6[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,3], ~Edge_Net_Subnet6[x,y+1,2,0,mask,3]), And(Edge_Net_Subnet6[x,y-1,2,0,mask,3], Edge_Net_Subnet6[x,y-2,2,0,mask,3], Edge_Net_Subnet6[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet6[x,y,2,0,mask,3], And(Edge_Net_Subnet6[x,y+1,2,0,mask,3], Edge_Net_Subnet6[x,y+2,2,0,mask,3], Edge_Net_Subnet6[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet6[x,y,2,0,mask,3], And(Edge_Net_Subnet6[x,y-1,2,0,mask,3], Edge_Net_Subnet6[x,y-2,2,0,mask,3], Edge_Net_Subnet6[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(35,35+1)]),
	).to_cnf()
Net6_Subnet3_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,1,3], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,1,3], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(16,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet3_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,mask,3], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,mask,3], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet3_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,1,3], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(16,40+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,1,3], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(16,40+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net6_Subnet3_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,3], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,3], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net6_Subnet3_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,1,3], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(16,40+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,1,3], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(16,40+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet3_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,3], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,3], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(4,35+1)]),
	).to_cnf()
Net6_Subnet3_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,1,3], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,1,3], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(16,40+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet3_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,mask,3], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,mask,3], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,40+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet3_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,1,2,mask,3], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,1,2,mask,3], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet3_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,2,2,mask,3], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,2,2,mask,3], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet3_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,2,mask,3], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,40+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,2,mask,3], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,40+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet3_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,2,mask,3], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,40+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,2,mask,3], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,40+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet3_DR = And(Net6_Subnet3_DR_Trend, Net6_Subnet3_DR_GIL_HorMinWidth,Net6_Subnet3_DR_GIL_HorMinSpacing,Net6_Subnet3_DR_GIL_VerMinSpacing,Net6_Subnet3_DR_AIL2_VerMinWidth,Net6_Subnet3_DR_AIL2_VerMinSpacing,Net6_Subnet3_DR_VerAIL2_HorMinSpacing,Net6_Subnet3_DR_MINT1AB_HorMinWidth,Net6_Subnet3_DR_MINT1_SameMask_VerMinSpacing,Net6_Subnet3_DR_MINT1_SameMask_HorMinSpacing,Net6_Subnet3_DR_MINT1_DiffMask_VerMinSpacing,Net6_Subnet3_DR_MINT1_DiffMask_HorMinSpacing,Net6_Subnet3_DR_M1AB_MinWidth,Net6_Subnet3_DR_HorM1_DiffMask_HorMinSpacing,Net6_Subnet3_DR_HorM1_SameMask_HorMinSpacing,Net6_Subnet3_DR_VerM1_DiffMask_VerMinSpacing,Net6_Subnet3_DR_VerM1_SameMask_VerMinSpacing,Net6_Subnet3_DR_HorM1_DiffMask_VerMinSpacing,Net6_Subnet3_DR_HorM1_SameMask_VerMinSpacing,Net6_Subnet3_DR_VerM1_DiffMask_HorMinSpacing,Net6_Subnet3_DR_VerM1_SameMask_HorMinSpacing,Net6_Subnet3_DR_V0_HorMinSpacing,Net6_Subnet3_DR_V1_HorMinSpacing,Net6_Subnet3_DR_V0_VerMinSpacing,Net6_Subnet3_DR_V1_VerMinSpacing,)
### Routability Constraints
Net6_Subnet3_R1 = And(
	RConstraints.R1(Edge_Net_Subnet6,[36,0,0,0, 36,1,0,0, 36,2,0,0, 36,3,0,0, 36,4,0,0, 36,5,0,0, 36,6,0,0, 36,7,0,0, 36,8,0,0, 36,9,0,0, 36,10,0,0, 36,11,0,0, 36,12,0,0, 36,13,0,0, 36,14,0,0, 36,15,0,0, 36,16,0,0, 36,17,0,0, 36,18,0,0, 36,19,0,0, 36,20,0,0, 36,21,0,0, 36,22,0,0, 36,23,0,0, 36,24,0,0, 36,25,0,0, 36,26,0,0, 36,27,0,0, 36,28,0,0, 36,29,0,0, 36,30,0,0, 36,31,0,0, 36,32,0,0, 36,33,0,0, 36,34,0,0, 36,35,0,0, ],36,16,0,1,40,35,3,3),
	RConstraints.R1(Edge_Net_Subnet6,[20,0,0,0, 20,1,0,0, 20,2,0,0, 20,3,0,0, 20,4,0,0, 20,5,0,0, 20,6,0,0, 20,7,0,0, 20,8,0,0, 20,9,0,0, 20,10,0,0, 20,11,0,0, 20,12,0,0, 20,13,0,0, 20,14,0,0, 20,15,0,0, 20,16,0,0, 20,17,0,0, 20,18,0,0, 20,19,0,0, 20,20,0,0, 20,21,0,0, 20,22,0,0, 20,23,0,0, 20,24,0,0, 20,25,0,0, 20,26,0,0, 20,27,0,0, 20,28,0,0, 20,29,0,0, 20,30,0,0, 20,31,0,0, 20,32,0,0, 20,33,0,0, 20,34,0,0, 20,35,0,0, ],36,16,0,1,40,35,3,3),
	).to_cnf()
Net6_Subnet3_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet6,Edge,Edge_Net,[36,0,0, 36,1,0, 36,2,0, 36,3,0, 36,4,0, 36,5,0, 36,6,0, 36,7,0, 36,8,0, 36,9,0, 36,10,0, 36,11,0, 36,12,0, 36,13,0, 36,14,0, 36,15,0, 36,16,0, 36,17,0, 36,18,0, 36,19,0, 36,20,0, 36,21,0, 36,22,0, 36,23,0, 36,24,0, 36,25,0, 36,26,0, 36,27,0, 36,28,0, 36,29,0, 36,30,0, 36,31,0, 36,32,0, 36,33,0, 36,34,0, 36,35,0, 20,0,0, 20,1,0, 20,2,0, 20,3,0, 20,4,0, 20,5,0, 20,6,0, 20,7,0, 20,8,0, 20,9,0, 20,10,0, 20,11,0, 20,12,0, 20,13,0, 20,14,0, 20,15,0, 20,16,0, 20,17,0, 20,18,0, 20,19,0, 20,20,0, 20,21,0, 20,22,0, 20,23,0, 20,24,0, 20,25,0, 20,26,0, 20,27,0, 20,28,0, 20,29,0, 20,30,0, 20,31,0, 20,32,0, 20,33,0, 20,34,0, 20,35,0, ],72,16,0,0,40,35,3,3,5),
	)
Net6_Subnet3_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,5],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,4+1)])for x in range(16,40+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,5],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(6,12+1)])for x in range(16,40+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net6_Subnet3_R = And(Net6_Subnet3_R1,Net6_Subnet3_R2,Net6_Subnet3_R3,)
Net6_Subnet3_Formula = And(Net6_Subnet3_C,Net6_Subnet3_DR,Net6_Subnet3_R)
# Net = 6 Subnet = 4 | Left -> Right [36,64] Top -> Bottom [0,35]
# Range R1(40,40,0,35)
# Range R2(60,60,0,35)
### Disable edges outside window
Edge_Net_Subnet6[0:36,0:35+1,0:3+1,0:2+1,0:2+1,4]=exprzeros(46656)
Edge_Net_Subnet6[64:77+1,0:35+1,0:3+1,0:2+1,0:2+1,4]=exprzeros(18144)

### Consistency Constraints
Net6_Subnet4_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,5]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(36,64+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net6_Subnet4_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet6[x,y,z,trend,mask,4]), Edge_Net[x,y,z,trend,mask,5])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(36,64+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net6_Subnet4_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,2,trend,0,4],Xor(Edge_Net_Subnet6[x,y,2,trend,1,4],Edge_Net_Subnet6[x,y,2,trend,2,4])),And(~Edge_Net_Subnet6[x,y,2,trend,0,4],~Edge_Net_Subnet6[x,y,2,trend,1,4],~Edge_Net_Subnet6[x,y,2,trend,2,4]))for x in range(36,64+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net6_Subnet4_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,3,1,0,4],Xor(Edge_Net_Subnet6[x,y,3,1,1,4],Edge_Net_Subnet6[x,y,3,1,2,4])),And(~Edge_Net_Subnet6[x,y,3,1,0,4],~Edge_Net_Subnet6[x,y,3,1,1,4],~Edge_Net_Subnet6[x,y,3,1,2,4]))for x in range(36,64+1)])for y in range(0,35+1)]).to_cnf()
Net6_Subnet4_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,1,trend,2,4],Xor(Edge_Net_Subnet6[x,y,1,trend,0,4],Edge_Net_Subnet6[x,y,1,trend,1,4])),And(~Edge_Net_Subnet6[x,y,1,trend,2,4],~Edge_Net_Subnet6[x,y,1,trend,0,4],~Edge_Net_Subnet6[x,y,1,trend,1,4]))for x in range(36,64+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net6_Subnet4_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,1,4], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,2,s2])for s2 in range(0,4)]))for trend in range(0,1+1)])for x in range(36,64+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,1,4], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,2,s2])for s2 in range(4+1,7)]))for trend in range(0,1+1)])for x in range(36,64+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,2,4], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,1,s2])for s2 in range(0,4)]))for trend in range(0,1+1)])for x in range(36,64+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,2,4], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,1,s2])for s2 in range(4+1,7)]))for trend in range(0,1+1)])for x in range(36,64+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net6_Subnet4_C = And(Net6_Subnet4_C1, Net6_Subnet4_C2,Net6_Subnet4_C3_ME1_Mask,Net6_Subnet4_C4_MINT1_Mask,Net6_Subnet4_C5_AIL2GIL_Mask,Net6_Subnet4_C6,)
### Design Rules
Net6_Subnet4_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(36,64+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net6_Subnet4_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,1,1,1,4], ~Edge_Net_Subnet6[x-1,y,1,1,1,4]), And(Edge_Net_Subnet6[x+1,y,1,1,1,4], Edge_Net_Subnet6[x+2,y,1,1,1,4], Edge_Net_Subnet6[x+3,y,1,1,1,4], ))for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,1,1,1,4], ~Edge_Net_Subnet6[x+1,y,1,1,1,4]), And(Edge_Net_Subnet6[x-1,y,1,1,1,4], Edge_Net_Subnet6[x-2,y,1,1,1,4], Edge_Net_Subnet6[x-3,y,1,1,1,4], ))for x in range(36,64+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet4_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,1,1,4], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,1,1,4], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(36,64+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet4_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,1,1,4], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(36,64+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,1,1,4], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(36,64+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet4_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,4]), And(Edge_Net_Subnet6[x,y+1,1,0,0,4], Edge_Net_Subnet6[x,y+2,1,0,0,4], Edge_Net_Subnet6[x,y+3,1,0,0,4], ))for x in range(36,64+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,4]), And(Edge_Net_Subnet6[x,y-1,1,0,0,4], Edge_Net_Subnet6[x,y-2,1,0,0,4], Edge_Net_Subnet6[x,y-3,1,0,0,4], ))for x in range(36,64+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,4], ~Edge_Net_Subnet6[x,y-1,1,0,0,4]), And(Edge_Net_Subnet6[x,y+1,1,0,0,4], Edge_Net_Subnet6[x,y+2,1,0,0,4], Edge_Net_Subnet6[x,y+3,1,0,0,4], ))for x in range(36,64+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,4], ~Edge_Net_Subnet6[x,y+1,1,0,0,4]), And(Edge_Net_Subnet6[x,y-1,1,0,0,4], Edge_Net_Subnet6[x,y-2,1,0,0,4], Edge_Net_Subnet6[x,y-3,1,0,0,4], ))for x in range(36,64+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net6_Subnet4_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(36,64+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(36,64+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(36,64+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(36,64+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(36,64+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(36,64+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net6_Subnet4_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,0,0,4], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,0,0,4], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(36,64+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet4_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,3,1,mask,4], ~Edge_Net_Subnet6[x-1,y,3,1,mask,4]), And(Edge_Net_Subnet6[x+1,y,3,1,mask,4], Edge_Net_Subnet6[x+2,y,3,1,mask,4], Edge_Net_Subnet6[x+3,y,3,1,mask,4], Edge_Net_Subnet6[x+4,y,3,1,mask,4], Edge_Net_Subnet6[x+5,y,3,1,mask,4], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,3,1,mask,4], ~Edge_Net_Subnet6[x+1,y,3,1,mask,4]), And(Edge_Net_Subnet6[x-1,y,3,1,mask,4], Edge_Net_Subnet6[x-2,y,3,1,mask,4], Edge_Net_Subnet6[x-3,y,3,1,mask,4], Edge_Net_Subnet6[x-4,y,3,1,mask,4], Edge_Net_Subnet6[x-5,y,3,1,mask,4], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet4_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,mask,4], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,mask,4], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet4_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,mask,4], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,mask,4], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet4_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,1,4], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(36,64+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,1,4], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(36,64+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet4_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,1,4], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,1,4], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(36,64+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet4_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,2,1,mask,4], ~Edge_Net_Subnet6[x-1,y,2,1,mask,4]), And(Edge_Net_Subnet6[x+1,y,2,1,mask,4], Edge_Net_Subnet6[x+2,y,2,1,mask,4], Edge_Net_Subnet6[x+3,y,2,1,mask,4], Edge_Net_Subnet6[x+4,y,2,1,mask,4], Edge_Net_Subnet6[x+5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,2,1,mask,4], ~Edge_Net_Subnet6[x+1,y,2,1,mask,4]), And(Edge_Net_Subnet6[x-1,y,2,1,mask,4], Edge_Net_Subnet6[x-2,y,2,1,mask,4], Edge_Net_Subnet6[x-3,y,2,1,mask,4], Edge_Net_Subnet6[x-4,y,2,1,mask,4], Edge_Net_Subnet6[x-5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,4], And(Edge_Net_Subnet6[x-1,y,2,1,mask,4], Edge_Net_Subnet6[x-2,y,2,1,mask,4], Edge_Net_Subnet6[x-3,y,2,1,mask,4], Edge_Net_Subnet6[x-4,y,2,1,mask,4], Edge_Net_Subnet6[x-5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(36,36+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,4], And(Edge_Net_Subnet6[x+1,y,2,1,mask,4], Edge_Net_Subnet6[x+2,y,2,1,mask,4], Edge_Net_Subnet6[x+3,y,2,1,mask,4], Edge_Net_Subnet6[x+4,y,2,1,mask,4], Edge_Net_Subnet6[x+5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(64-1,36)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,4], ~Edge_Net_Subnet6[x,y-1,2,0,mask,4]), And(Edge_Net_Subnet6[x,y+1,2,0,mask,4], Edge_Net_Subnet6[x,y+2,2,0,mask,4], Edge_Net_Subnet6[x,y+3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,4], ~Edge_Net_Subnet6[x,y+1,2,0,mask,4]), And(Edge_Net_Subnet6[x,y-1,2,0,mask,4], Edge_Net_Subnet6[x,y-2,2,0,mask,4], Edge_Net_Subnet6[x,y-3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet6[x,y,2,0,mask,4], And(Edge_Net_Subnet6[x,y+1,2,0,mask,4], Edge_Net_Subnet6[x,y+2,2,0,mask,4], Edge_Net_Subnet6[x,y+3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet6[x,y,2,0,mask,4], And(Edge_Net_Subnet6[x,y-1,2,0,mask,4], Edge_Net_Subnet6[x,y-2,2,0,mask,4], Edge_Net_Subnet6[x,y-3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(35,35+1)]),
	).to_cnf()
Net6_Subnet4_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,1,4], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,1,4], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(36,64+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet4_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,mask,4], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,mask,4], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet4_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,1,4], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(36,64+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,1,4], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(36,64+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net6_Subnet4_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,4], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,4], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net6_Subnet4_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,1,4], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(36,64+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,1,4], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(36,64+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet4_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,4], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,4], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(4,35+1)]),
	).to_cnf()
Net6_Subnet4_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,1,4], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,1,4], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(36,64+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet4_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,mask,4], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,mask,4], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(36,64+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet4_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,1,2,mask,4], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,1,2,mask,4], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(36,64+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet4_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,2,2,mask,4], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(36,64+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,2,2,mask,4], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(36,64+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet4_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,2,mask,4], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(36,64+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,2,mask,4], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(36,64+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet4_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,2,mask,4], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(36,64+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,2,mask,4], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(36,64+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet4_DR = And(Net6_Subnet4_DR_Trend, Net6_Subnet4_DR_GIL_HorMinWidth,Net6_Subnet4_DR_GIL_HorMinSpacing,Net6_Subnet4_DR_GIL_VerMinSpacing,Net6_Subnet4_DR_AIL2_VerMinWidth,Net6_Subnet4_DR_AIL2_VerMinSpacing,Net6_Subnet4_DR_VerAIL2_HorMinSpacing,Net6_Subnet4_DR_MINT1AB_HorMinWidth,Net6_Subnet4_DR_MINT1_SameMask_VerMinSpacing,Net6_Subnet4_DR_MINT1_SameMask_HorMinSpacing,Net6_Subnet4_DR_MINT1_DiffMask_VerMinSpacing,Net6_Subnet4_DR_MINT1_DiffMask_HorMinSpacing,Net6_Subnet4_DR_M1AB_MinWidth,Net6_Subnet4_DR_HorM1_DiffMask_HorMinSpacing,Net6_Subnet4_DR_HorM1_SameMask_HorMinSpacing,Net6_Subnet4_DR_VerM1_DiffMask_VerMinSpacing,Net6_Subnet4_DR_VerM1_SameMask_VerMinSpacing,Net6_Subnet4_DR_HorM1_DiffMask_VerMinSpacing,Net6_Subnet4_DR_HorM1_SameMask_VerMinSpacing,Net6_Subnet4_DR_VerM1_DiffMask_HorMinSpacing,Net6_Subnet4_DR_VerM1_SameMask_HorMinSpacing,Net6_Subnet4_DR_V0_HorMinSpacing,Net6_Subnet4_DR_V1_HorMinSpacing,Net6_Subnet4_DR_V0_VerMinSpacing,Net6_Subnet4_DR_V1_VerMinSpacing,)
### Routability Constraints
Net6_Subnet4_R1 = And(
	RConstraints.R1(Edge_Net_Subnet6,[40,0,0,0, 40,1,0,0, 40,2,0,0, 40,3,0,0, 40,4,0,0, 40,5,0,0, 40,6,0,0, 40,7,0,0, 40,8,0,0, 40,9,0,0, 40,10,0,0, 40,11,0,0, 40,12,0,0, 40,13,0,0, 40,14,0,0, 40,15,0,0, 40,16,0,0, 40,17,0,0, 40,18,0,0, 40,19,0,0, 40,20,0,0, 40,21,0,0, 40,22,0,0, 40,23,0,0, 40,24,0,0, 40,25,0,0, 40,26,0,0, 40,27,0,0, 40,28,0,0, 40,29,0,0, 40,30,0,0, 40,31,0,0, 40,32,0,0, 40,33,0,0, 40,34,0,0, 40,35,0,0, ],36,36,0,1,64,35,3,4),
	RConstraints.R1(Edge_Net_Subnet6,[60,0,0,0, 60,1,0,0, 60,2,0,0, 60,3,0,0, 60,4,0,0, 60,5,0,0, 60,6,0,0, 60,7,0,0, 60,8,0,0, 60,9,0,0, 60,10,0,0, 60,11,0,0, 60,12,0,0, 60,13,0,0, 60,14,0,0, 60,15,0,0, 60,16,0,0, 60,17,0,0, 60,18,0,0, 60,19,0,0, 60,20,0,0, 60,21,0,0, 60,22,0,0, 60,23,0,0, 60,24,0,0, 60,25,0,0, 60,26,0,0, 60,27,0,0, 60,28,0,0, 60,29,0,0, 60,30,0,0, 60,31,0,0, 60,32,0,0, 60,33,0,0, 60,34,0,0, 60,35,0,0, ],36,36,0,1,64,35,3,4),
	).to_cnf()
Net6_Subnet4_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet6,Edge,Edge_Net,[40,0,0, 40,1,0, 40,2,0, 40,3,0, 40,4,0, 40,5,0, 40,6,0, 40,7,0, 40,8,0, 40,9,0, 40,10,0, 40,11,0, 40,12,0, 40,13,0, 40,14,0, 40,15,0, 40,16,0, 40,17,0, 40,18,0, 40,19,0, 40,20,0, 40,21,0, 40,22,0, 40,23,0, 40,24,0, 40,25,0, 40,26,0, 40,27,0, 40,28,0, 40,29,0, 40,30,0, 40,31,0, 40,32,0, 40,33,0, 40,34,0, 40,35,0, 60,0,0, 60,1,0, 60,2,0, 60,3,0, 60,4,0, 60,5,0, 60,6,0, 60,7,0, 60,8,0, 60,9,0, 60,10,0, 60,11,0, 60,12,0, 60,13,0, 60,14,0, 60,15,0, 60,16,0, 60,17,0, 60,18,0, 60,19,0, 60,20,0, 60,21,0, 60,22,0, 60,23,0, 60,24,0, 60,25,0, 60,26,0, 60,27,0, 60,28,0, 60,29,0, 60,30,0, 60,31,0, 60,32,0, 60,33,0, 60,34,0, 60,35,0, ],72,36,0,0,64,35,3,4,5),
	)
Net6_Subnet4_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,5],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,4+1)])for x in range(36,64+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,5],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(6,12+1)])for x in range(36,64+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net6_Subnet4_R = And(Net6_Subnet4_R1,Net6_Subnet4_R2,Net6_Subnet4_R3,)
Net6_Subnet4_Formula = And(Net6_Subnet4_C,Net6_Subnet4_DR,Net6_Subnet4_R)
# Net = 6 Subnet = 6 | Left -> Right [56,70] Top -> Bottom [0,35]
# Range R1(60,60,0,35)
# Range R2(66,66,26,33)
### Disable edges outside window
Edge_Net_Subnet6[0:56,0:35+1,0:3+1,0:2+1,0:2+1,6]=exprzeros(72576)
Edge_Net_Subnet6[70:77+1,0:35+1,0:3+1,0:2+1,0:2+1,6]=exprzeros(10368)

### Consistency Constraints
Net6_Subnet6_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,5]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(56,70+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net6_Subnet6_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet6[x,y,z,trend,mask,6]), Edge_Net[x,y,z,trend,mask,5])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(56,70+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net6_Subnet6_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,2,trend,0,6],Xor(Edge_Net_Subnet6[x,y,2,trend,1,6],Edge_Net_Subnet6[x,y,2,trend,2,6])),And(~Edge_Net_Subnet6[x,y,2,trend,0,6],~Edge_Net_Subnet6[x,y,2,trend,1,6],~Edge_Net_Subnet6[x,y,2,trend,2,6]))for x in range(56,70+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net6_Subnet6_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,3,1,0,6],Xor(Edge_Net_Subnet6[x,y,3,1,1,6],Edge_Net_Subnet6[x,y,3,1,2,6])),And(~Edge_Net_Subnet6[x,y,3,1,0,6],~Edge_Net_Subnet6[x,y,3,1,1,6],~Edge_Net_Subnet6[x,y,3,1,2,6]))for x in range(56,70+1)])for y in range(0,35+1)]).to_cnf()
Net6_Subnet6_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet6[x,y,1,trend,2,6],Xor(Edge_Net_Subnet6[x,y,1,trend,0,6],Edge_Net_Subnet6[x,y,1,trend,1,6])),And(~Edge_Net_Subnet6[x,y,1,trend,2,6],~Edge_Net_Subnet6[x,y,1,trend,0,6],~Edge_Net_Subnet6[x,y,1,trend,1,6]))for x in range(56,70+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net6_Subnet6_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,1,6], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,2,s2])for s2 in range(0,6)]))for trend in range(0,1+1)])for x in range(56,70+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,z,trend,2,6], And(*[And(~Edge_Net_Subnet6[x,y,z,trend,1,s2])for s2 in range(0,6)]))for trend in range(0,1+1)])for x in range(56,70+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net6_Subnet6_C = And(Net6_Subnet6_C1, Net6_Subnet6_C2,Net6_Subnet6_C3_ME1_Mask,Net6_Subnet6_C4_MINT1_Mask,Net6_Subnet6_C5_AIL2GIL_Mask,Net6_Subnet6_C6,)
### Design Rules
Net6_Subnet6_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(56,70+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net6_Subnet6_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,1,1,1,6], ~Edge_Net_Subnet6[x-1,y,1,1,1,6]), And(Edge_Net_Subnet6[x+1,y,1,1,1,6], Edge_Net_Subnet6[x+2,y,1,1,1,6], Edge_Net_Subnet6[x+3,y,1,1,1,6], ))for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,1,1,1,6], ~Edge_Net_Subnet6[x+1,y,1,1,1,6]), And(Edge_Net_Subnet6[x-1,y,1,1,1,6], Edge_Net_Subnet6[x-2,y,1,1,1,6], Edge_Net_Subnet6[x-3,y,1,1,1,6], ))for x in range(56,70+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet6_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,1,1,6], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,1,1,6], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(56,70+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet6_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,1,1,6], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(56,70+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,1,1,6], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(56,70+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet6_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,6]), And(Edge_Net_Subnet6[x,y+1,1,0,0,6], Edge_Net_Subnet6[x,y+2,1,0,0,6], Edge_Net_Subnet6[x,y+3,1,0,0,6], ))for x in range(56,70+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,6]), And(Edge_Net_Subnet6[x,y-1,1,0,0,6], Edge_Net_Subnet6[x,y-2,1,0,0,6], Edge_Net_Subnet6[x,y-3,1,0,0,6], ))for x in range(56,70+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,6], ~Edge_Net_Subnet6[x,y-1,1,0,0,6]), And(Edge_Net_Subnet6[x,y+1,1,0,0,6], Edge_Net_Subnet6[x,y+2,1,0,0,6], Edge_Net_Subnet6[x,y+3,1,0,0,6], ))for x in range(56,70+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,6], ~Edge_Net_Subnet6[x,y+1,1,0,0,6]), And(Edge_Net_Subnet6[x,y-1,1,0,0,6], Edge_Net_Subnet6[x,y-2,1,0,0,6], Edge_Net_Subnet6[x,y-3,1,0,0,6], ))for x in range(56,70+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net6_Subnet6_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,6], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(56,70+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,6], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(56,70+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,6], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(56,70+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,6], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(56,70+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,6], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(56,70+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,1,0,0,6], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(56,70+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net6_Subnet6_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,0,0,6], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,0,0,6], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(56,70+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet6_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,3,1,mask,6], ~Edge_Net_Subnet6[x-1,y,3,1,mask,6]), And(Edge_Net_Subnet6[x+1,y,3,1,mask,6], Edge_Net_Subnet6[x+2,y,3,1,mask,6], Edge_Net_Subnet6[x+3,y,3,1,mask,6], Edge_Net_Subnet6[x+4,y,3,1,mask,6], Edge_Net_Subnet6[x+5,y,3,1,mask,6], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,3,1,mask,6], ~Edge_Net_Subnet6[x+1,y,3,1,mask,6]), And(Edge_Net_Subnet6[x-1,y,3,1,mask,6], Edge_Net_Subnet6[x-2,y,3,1,mask,6], Edge_Net_Subnet6[x-3,y,3,1,mask,6], Edge_Net_Subnet6[x-4,y,3,1,mask,6], Edge_Net_Subnet6[x-5,y,3,1,mask,6], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet6_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,mask,6], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,mask,6], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet6_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,mask,6], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,mask,6], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet6_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,1,6], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(56,70+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,3,1,1,6], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(56,70+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet6_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,1,6], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,3,1,1,6], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(56,70+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet6_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,2,1,mask,6], ~Edge_Net_Subnet6[x-1,y,2,1,mask,6]), And(Edge_Net_Subnet6[x+1,y,2,1,mask,6], Edge_Net_Subnet6[x+2,y,2,1,mask,6], Edge_Net_Subnet6[x+3,y,2,1,mask,6], Edge_Net_Subnet6[x+4,y,2,1,mask,6], Edge_Net_Subnet6[x+5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet6[x,y,2,1,mask,6], ~Edge_Net_Subnet6[x+1,y,2,1,mask,6]), And(Edge_Net_Subnet6[x-1,y,2,1,mask,6], Edge_Net_Subnet6[x-2,y,2,1,mask,6], Edge_Net_Subnet6[x-3,y,2,1,mask,6], Edge_Net_Subnet6[x-4,y,2,1,mask,6], Edge_Net_Subnet6[x-5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,6], And(Edge_Net_Subnet6[x-1,y,2,1,mask,6], Edge_Net_Subnet6[x-2,y,2,1,mask,6], Edge_Net_Subnet6[x-3,y,2,1,mask,6], Edge_Net_Subnet6[x-4,y,2,1,mask,6], Edge_Net_Subnet6[x-5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(56,56+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,6], And(Edge_Net_Subnet6[x+1,y,2,1,mask,6], Edge_Net_Subnet6[x+2,y,2,1,mask,6], Edge_Net_Subnet6[x+3,y,2,1,mask,6], Edge_Net_Subnet6[x+4,y,2,1,mask,6], Edge_Net_Subnet6[x+5,y,2,1,mask,6], ))for mask in range(1,2+1)])for x in range(70-1,56)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,6], ~Edge_Net_Subnet6[x,y-1,2,0,mask,6]), And(Edge_Net_Subnet6[x,y+1,2,0,mask,6], Edge_Net_Subnet6[x,y+2,2,0,mask,6], Edge_Net_Subnet6[x,y+3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,6], ~Edge_Net_Subnet6[x,y+1,2,0,mask,6]), And(Edge_Net_Subnet6[x,y-1,2,0,mask,6], Edge_Net_Subnet6[x,y-2,2,0,mask,6], Edge_Net_Subnet6[x,y-3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet6[x,y,2,0,mask,6], And(Edge_Net_Subnet6[x,y+1,2,0,mask,6], Edge_Net_Subnet6[x,y+2,2,0,mask,6], Edge_Net_Subnet6[x,y+3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet6[x,y,2,0,mask,6], And(Edge_Net_Subnet6[x,y-1,2,0,mask,6], Edge_Net_Subnet6[x,y-2,2,0,mask,6], Edge_Net_Subnet6[x,y-3,2,0,mask,6], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(35,35+1)]),
	).to_cnf()
Net6_Subnet6_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,1,6], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,1,6], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(56,70+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet6_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,mask,6], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,1,mask,6], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet6_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,1,6], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(56,70+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,1,6], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(56,70+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net6_Subnet6_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,6], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet6[x,y,2,0,mask,6], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net6_Subnet6_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,1,6], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(56,70+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,1,6], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(56,70+1)])for y in range(3,35+1)]),
	).to_cnf()
Net6_Subnet6_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,6], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,1,mask,6], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(4,35+1)]),
	).to_cnf()
Net6_Subnet6_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,1,6], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,1,6], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(56,70+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet6_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,mask,6], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,0,mask,6], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(56,70+1)])for y in range(0,35+1)]),
	).to_cnf()
Net6_Subnet6_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,1,2,mask,6], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,1,2,mask,6], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(56,70+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet6_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,2,2,mask,6], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(56,70+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet6[x,y,2,2,mask,6], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(56,70+1)])for y in range(0,35+1)])
	).to_cnf()
Net6_Subnet6_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,2,mask,6], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(56,70+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,1,2,mask,6], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(56,70+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet6_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,2,mask,6], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(56,70+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet6[x,y,2,2,mask,6], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(56,70+1)])for y in range(2,35+1)]),
	).to_cnf()
Net6_Subnet6_DR = And(Net6_Subnet6_DR_Trend, Net6_Subnet6_DR_GIL_HorMinWidth,Net6_Subnet6_DR_GIL_HorMinSpacing,Net6_Subnet6_DR_GIL_VerMinSpacing,Net6_Subnet6_DR_AIL2_VerMinWidth,Net6_Subnet6_DR_AIL2_VerMinSpacing,Net6_Subnet6_DR_VerAIL2_HorMinSpacing,Net6_Subnet6_DR_MINT1AB_HorMinWidth,Net6_Subnet6_DR_MINT1_SameMask_VerMinSpacing,Net6_Subnet6_DR_MINT1_SameMask_HorMinSpacing,Net6_Subnet6_DR_MINT1_DiffMask_VerMinSpacing,Net6_Subnet6_DR_MINT1_DiffMask_HorMinSpacing,Net6_Subnet6_DR_M1AB_MinWidth,Net6_Subnet6_DR_HorM1_DiffMask_HorMinSpacing,Net6_Subnet6_DR_HorM1_SameMask_HorMinSpacing,Net6_Subnet6_DR_VerM1_DiffMask_VerMinSpacing,Net6_Subnet6_DR_VerM1_SameMask_VerMinSpacing,Net6_Subnet6_DR_HorM1_DiffMask_VerMinSpacing,Net6_Subnet6_DR_HorM1_SameMask_VerMinSpacing,Net6_Subnet6_DR_VerM1_DiffMask_HorMinSpacing,Net6_Subnet6_DR_VerM1_SameMask_HorMinSpacing,Net6_Subnet6_DR_V0_HorMinSpacing,Net6_Subnet6_DR_V1_HorMinSpacing,Net6_Subnet6_DR_V0_VerMinSpacing,Net6_Subnet6_DR_V1_VerMinSpacing,)
### Routability Constraints
Net6_Subnet6_R1 = And(
	RConstraints.R1(Edge_Net_Subnet6,[60,0,0,0, 60,1,0,0, 60,2,0,0, 60,3,0,0, 60,4,0,0, 60,5,0,0, 60,6,0,0, 60,7,0,0, 60,8,0,0, 60,9,0,0, 60,10,0,0, 60,11,0,0, 60,12,0,0, 60,13,0,0, 60,14,0,0, 60,15,0,0, 60,16,0,0, 60,17,0,0, 60,18,0,0, 60,19,0,0, 60,20,0,0, 60,21,0,0, 60,22,0,0, 60,23,0,0, 60,24,0,0, 60,25,0,0, 60,26,0,0, 60,27,0,0, 60,28,0,0, 60,29,0,0, 60,30,0,0, 60,31,0,0, 60,32,0,0, 60,33,0,0, 60,34,0,0, 60,35,0,0, ],36,56,0,1,70,35,3,6),
	RConstraints.R1(Edge_Net_Subnet6,[66,26,0,0, 66,27,0,0, 66,28,0,0, 66,29,0,0, 66,30,0,0, 66,31,0,0, 66,32,0,0, 66,33,0,0, ],8,56,0,1,70,35,3,6),
	).to_cnf()
Net6_Subnet6_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet6,Edge,Edge_Net,[60,0,0, 60,1,0, 60,2,0, 60,3,0, 60,4,0, 60,5,0, 60,6,0, 60,7,0, 60,8,0, 60,9,0, 60,10,0, 60,11,0, 60,12,0, 60,13,0, 60,14,0, 60,15,0, 60,16,0, 60,17,0, 60,18,0, 60,19,0, 60,20,0, 60,21,0, 60,22,0, 60,23,0, 60,24,0, 60,25,0, 60,26,0, 60,27,0, 60,28,0, 60,29,0, 60,30,0, 60,31,0, 60,32,0, 60,33,0, 60,34,0, 60,35,0, 66,26,0, 66,27,0, 66,28,0, 66,29,0, 66,30,0, 66,31,0, 66,32,0, 66,33,0, 66,34,0, ],45,56,0,0,70,35,3,6,5),
	)
Net6_Subnet6_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,5],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,4+1)])for x in range(56,70+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,5],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(6,12+1)])for x in range(56,70+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net6_Subnet6_R = And(Net6_Subnet6_R1,Net6_Subnet6_R2,Net6_Subnet6_R3,)
Net6_Subnet6_Formula = And(Net6_Subnet6_C,Net6_Subnet6_DR,Net6_Subnet6_R)
# Net = 8 Subnet = 0 | Left -> Right [18,26] Top -> Bottom [0,35]
# Range R1(22,22,1,6)
# Range R2(22,22,28,33)
### Disable edges outside window
Edge_Net_Subnet8[0:18,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(23328)
Edge_Net_Subnet8[26:77+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(67392)

### Consistency Constraints
Net8_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,7]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(18,26+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net8_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet8[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,7])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(18,26+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net8_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet8[x,y,2,trend,0,0],Xor(Edge_Net_Subnet8[x,y,2,trend,1,0],Edge_Net_Subnet8[x,y,2,trend,2,0])),And(~Edge_Net_Subnet8[x,y,2,trend,0,0],~Edge_Net_Subnet8[x,y,2,trend,1,0],~Edge_Net_Subnet8[x,y,2,trend,2,0]))for x in range(18,26+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net8_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet8[x,y,3,1,0,0],Xor(Edge_Net_Subnet8[x,y,3,1,1,0],Edge_Net_Subnet8[x,y,3,1,2,0])),And(~Edge_Net_Subnet8[x,y,3,1,0,0],~Edge_Net_Subnet8[x,y,3,1,1,0],~Edge_Net_Subnet8[x,y,3,1,2,0]))for x in range(18,26+1)])for y in range(0,35+1)]).to_cnf()
Net8_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet8[x,y,1,trend,2,0],Xor(Edge_Net_Subnet8[x,y,1,trend,0,0],Edge_Net_Subnet8[x,y,1,trend,1,0])),And(~Edge_Net_Subnet8[x,y,1,trend,2,0],~Edge_Net_Subnet8[x,y,1,trend,0,0],~Edge_Net_Subnet8[x,y,1,trend,1,0]))for x in range(18,26+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net8_Subnet0_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,1,0], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,2,s2])for s2 in range(0+1,3)]))for trend in range(0,1+1)])for x in range(18,26+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,2,0], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,1,s2])for s2 in range(0+1,3)]))for trend in range(0,1+1)])for x in range(18,26+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net8_Subnet0_C = And(Net8_Subnet0_C1, Net8_Subnet0_C2,Net8_Subnet0_C3_ME1_Mask,Net8_Subnet0_C4_MINT1_Mask,Net8_Subnet0_C5_AIL2GIL_Mask,Net8_Subnet0_C6,)
### Design Rules
Net8_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(18,26+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net8_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,1,1,1,0], ~Edge_Net_Subnet8[x-1,y,1,1,1,0]), And(Edge_Net_Subnet8[x+1,y,1,1,1,0], Edge_Net_Subnet8[x+2,y,1,1,1,0], Edge_Net_Subnet8[x+3,y,1,1,1,0], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,1,1,1,0], ~Edge_Net_Subnet8[x+1,y,1,1,1,0]), And(Edge_Net_Subnet8[x-1,y,1,1,1,0], Edge_Net_Subnet8[x-2,y,1,1,1,0], Edge_Net_Subnet8[x-3,y,1,1,1,0], ))for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(18,26+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(18,26+1)])for y in range(3,35+1)]),
	).to_cnf()
Net8_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,0]), And(Edge_Net_Subnet8[x,y+1,1,0,0,0], Edge_Net_Subnet8[x,y+2,1,0,0,0], Edge_Net_Subnet8[x,y+3,1,0,0,0], ))for x in range(18,26+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,0]), And(Edge_Net_Subnet8[x,y-1,1,0,0,0], Edge_Net_Subnet8[x,y-2,1,0,0,0], Edge_Net_Subnet8[x,y-3,1,0,0,0], ))for x in range(18,26+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,0], ~Edge_Net_Subnet8[x,y-1,1,0,0,0]), And(Edge_Net_Subnet8[x,y+1,1,0,0,0], Edge_Net_Subnet8[x,y+2,1,0,0,0], Edge_Net_Subnet8[x,y+3,1,0,0,0], ))for x in range(18,26+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,0], ~Edge_Net_Subnet8[x,y+1,1,0,0,0]), And(Edge_Net_Subnet8[x,y-1,1,0,0,0], Edge_Net_Subnet8[x,y-2,1,0,0,0], Edge_Net_Subnet8[x,y-3,1,0,0,0], ))for x in range(18,26+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net8_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(18,26+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(18,26+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(18,26+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(18,26+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(18,26+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(18,26+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net8_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,3,1,mask,0], ~Edge_Net_Subnet8[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet8[x+1,y,3,1,mask,0], Edge_Net_Subnet8[x+2,y,3,1,mask,0], Edge_Net_Subnet8[x+3,y,3,1,mask,0], Edge_Net_Subnet8[x+4,y,3,1,mask,0], Edge_Net_Subnet8[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,3,1,mask,0], ~Edge_Net_Subnet8[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet8[x-1,y,3,1,mask,0], Edge_Net_Subnet8[x-2,y,3,1,mask,0], Edge_Net_Subnet8[x-3,y,3,1,mask,0], Edge_Net_Subnet8[x-4,y,3,1,mask,0], Edge_Net_Subnet8[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(3,35+1)]),
	).to_cnf()
Net8_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(18,26+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(18,26+1)])for y in range(2,35+1)]),
	).to_cnf()
Net8_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,2,1,mask,0], ~Edge_Net_Subnet8[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet8[x+1,y,2,1,mask,0], Edge_Net_Subnet8[x+2,y,2,1,mask,0], Edge_Net_Subnet8[x+3,y,2,1,mask,0], Edge_Net_Subnet8[x+4,y,2,1,mask,0], Edge_Net_Subnet8[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,2,1,mask,0], ~Edge_Net_Subnet8[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet8[x-1,y,2,1,mask,0], Edge_Net_Subnet8[x-2,y,2,1,mask,0], Edge_Net_Subnet8[x-3,y,2,1,mask,0], Edge_Net_Subnet8[x-4,y,2,1,mask,0], Edge_Net_Subnet8[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,0], And(Edge_Net_Subnet8[x-1,y,2,1,mask,0], Edge_Net_Subnet8[x-2,y,2,1,mask,0], Edge_Net_Subnet8[x-3,y,2,1,mask,0], Edge_Net_Subnet8[x-4,y,2,1,mask,0], Edge_Net_Subnet8[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(18,18+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,0], And(Edge_Net_Subnet8[x+1,y,2,1,mask,0], Edge_Net_Subnet8[x+2,y,2,1,mask,0], Edge_Net_Subnet8[x+3,y,2,1,mask,0], Edge_Net_Subnet8[x+4,y,2,1,mask,0], Edge_Net_Subnet8[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(26-1,18)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,0], ~Edge_Net_Subnet8[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet8[x,y+1,2,0,mask,0], Edge_Net_Subnet8[x,y+2,2,0,mask,0], Edge_Net_Subnet8[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,0], ~Edge_Net_Subnet8[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet8[x,y-1,2,0,mask,0], Edge_Net_Subnet8[x,y-2,2,0,mask,0], Edge_Net_Subnet8[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet8[x,y,2,0,mask,0], And(Edge_Net_Subnet8[x,y+1,2,0,mask,0], Edge_Net_Subnet8[x,y+2,2,0,mask,0], Edge_Net_Subnet8[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet8[x,y,2,0,mask,0], And(Edge_Net_Subnet8[x,y-1,2,0,mask,0], Edge_Net_Subnet8[x,y-2,2,0,mask,0], Edge_Net_Subnet8[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(35,35+1)]),
	).to_cnf()
Net8_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(18,26+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(18,26+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net8_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net8_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(18,26+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(18,26+1)])for y in range(3,35+1)]),
	).to_cnf()
Net8_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(4,35+1)]),
	).to_cnf()
Net8_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(18,26+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(2,35+1)]),
	).to_cnf()
Net8_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(18,26+1)])for y in range(2,35+1)]),
	).to_cnf()
Net8_Subnet0_DR = And(Net8_Subnet0_DR_Trend, Net8_Subnet0_DR_GIL_HorMinWidth,Net8_Subnet0_DR_GIL_HorMinSpacing,Net8_Subnet0_DR_GIL_VerMinSpacing,Net8_Subnet0_DR_AIL2_VerMinWidth,Net8_Subnet0_DR_AIL2_VerMinSpacing,Net8_Subnet0_DR_VerAIL2_HorMinSpacing,Net8_Subnet0_DR_MINT1AB_HorMinWidth,Net8_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net8_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net8_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net8_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net8_Subnet0_DR_M1AB_MinWidth,Net8_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net8_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net8_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net8_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net8_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net8_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net8_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net8_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net8_Subnet0_DR_V0_HorMinSpacing,Net8_Subnet0_DR_V1_HorMinSpacing,Net8_Subnet0_DR_V0_VerMinSpacing,Net8_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net8_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet8,[22,1,0,0, 22,2,0,0, 22,3,0,0, 22,4,0,0, 22,5,0,0, 22,6,0,0, ],6,18,0,1,26,35,3,0),
	RConstraints.R1(Edge_Net_Subnet8,[22,28,0,0, 22,29,0,0, 22,30,0,0, 22,31,0,0, 22,32,0,0, 22,33,0,0, ],6,18,0,1,26,35,3,0),
	).to_cnf()
Net8_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet8,Edge,Edge_Net,[22,1,0, 22,2,0, 22,3,0, 22,4,0, 22,5,0, 22,6,0, 22,7,0, 22,28,0, 22,29,0, 22,30,0, 22,31,0, 22,32,0, 22,33,0, 22,34,0, ],14,18,0,0,26,35,3,0,7),
	)
Net8_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,7],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,6+1)])for x in range(18,26+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,7],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(8,12+1)])for x in range(18,26+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net8_Subnet0_R = And(Net8_Subnet0_R1,Net8_Subnet0_R2,Net8_Subnet0_R3,)
Net8_Subnet0_Formula = And(Net8_Subnet0_C,Net8_Subnet0_DR,Net8_Subnet0_R)
# Net = 8 Subnet = 1 | Left -> Right [18,36] Top -> Bottom [0,35]
# Range R1(22,22,1,6)
# Range R2(32,32,0,35)
### Disable edges outside window
Edge_Net_Subnet8[0:18,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(23328)
Edge_Net_Subnet8[36:77+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(54432)

### Consistency Constraints
Net8_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,7]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(18,36+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net8_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet8[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,7])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(18,36+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net8_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet8[x,y,2,trend,0,1],Xor(Edge_Net_Subnet8[x,y,2,trend,1,1],Edge_Net_Subnet8[x,y,2,trend,2,1])),And(~Edge_Net_Subnet8[x,y,2,trend,0,1],~Edge_Net_Subnet8[x,y,2,trend,1,1],~Edge_Net_Subnet8[x,y,2,trend,2,1]))for x in range(18,36+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net8_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet8[x,y,3,1,0,1],Xor(Edge_Net_Subnet8[x,y,3,1,1,1],Edge_Net_Subnet8[x,y,3,1,2,1])),And(~Edge_Net_Subnet8[x,y,3,1,0,1],~Edge_Net_Subnet8[x,y,3,1,1,1],~Edge_Net_Subnet8[x,y,3,1,2,1]))for x in range(18,36+1)])for y in range(0,35+1)]).to_cnf()
Net8_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet8[x,y,1,trend,2,1],Xor(Edge_Net_Subnet8[x,y,1,trend,0,1],Edge_Net_Subnet8[x,y,1,trend,1,1])),And(~Edge_Net_Subnet8[x,y,1,trend,2,1],~Edge_Net_Subnet8[x,y,1,trend,0,1],~Edge_Net_Subnet8[x,y,1,trend,1,1]))for x in range(18,36+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net8_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(18,36+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,2,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(18,36+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(18,36+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet8[x,y,z,trend,1,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(18,36+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net8_Subnet1_C = And(Net8_Subnet1_C1, Net8_Subnet1_C2,Net8_Subnet1_C3_ME1_Mask,Net8_Subnet1_C4_MINT1_Mask,Net8_Subnet1_C5_AIL2GIL_Mask,Net8_Subnet1_C6,)
### Design Rules
Net8_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(18,36+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net8_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,1,1,1,1], ~Edge_Net_Subnet8[x-1,y,1,1,1,1]), And(Edge_Net_Subnet8[x+1,y,1,1,1,1], Edge_Net_Subnet8[x+2,y,1,1,1,1], Edge_Net_Subnet8[x+3,y,1,1,1,1], ))for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,1,1,1,1], ~Edge_Net_Subnet8[x+1,y,1,1,1,1]), And(Edge_Net_Subnet8[x-1,y,1,1,1,1], Edge_Net_Subnet8[x-2,y,1,1,1,1], Edge_Net_Subnet8[x-3,y,1,1,1,1], ))for x in range(18,36+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(18,36+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(18,36+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(18,36+1)])for y in range(3,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1]), And(Edge_Net_Subnet8[x,y+1,1,0,0,1], Edge_Net_Subnet8[x,y+2,1,0,0,1], Edge_Net_Subnet8[x,y+3,1,0,0,1], ))for x in range(18,36+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1]), And(Edge_Net_Subnet8[x,y-1,1,0,0,1], Edge_Net_Subnet8[x,y-2,1,0,0,1], Edge_Net_Subnet8[x,y-3,1,0,0,1], ))for x in range(18,36+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge_Net_Subnet8[x,y-1,1,0,0,1]), And(Edge_Net_Subnet8[x,y+1,1,0,0,1], Edge_Net_Subnet8[x,y+2,1,0,0,1], Edge_Net_Subnet8[x,y+3,1,0,0,1], ))for x in range(18,36+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge_Net_Subnet8[x,y+1,1,0,0,1]), And(Edge_Net_Subnet8[x,y-1,1,0,0,1], Edge_Net_Subnet8[x,y-2,1,0,0,1], Edge_Net_Subnet8[x,y-3,1,0,0,1], ))for x in range(18,36+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net8_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(18,36+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(18,36+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(18,36+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(18,36+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(18,36+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(18,36+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net8_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(18,36+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,3,1,mask,1], ~Edge_Net_Subnet8[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet8[x+1,y,3,1,mask,1], Edge_Net_Subnet8[x+2,y,3,1,mask,1], Edge_Net_Subnet8[x+3,y,3,1,mask,1], Edge_Net_Subnet8[x+4,y,3,1,mask,1], Edge_Net_Subnet8[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,3,1,mask,1], ~Edge_Net_Subnet8[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet8[x-1,y,3,1,mask,1], Edge_Net_Subnet8[x-2,y,3,1,mask,1], Edge_Net_Subnet8[x-3,y,3,1,mask,1], Edge_Net_Subnet8[x-4,y,3,1,mask,1], Edge_Net_Subnet8[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(3,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(18,36+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(18,36+1)])for y in range(2,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(18,36+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,2,1,mask,1], ~Edge_Net_Subnet8[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet8[x+1,y,2,1,mask,1], Edge_Net_Subnet8[x+2,y,2,1,mask,1], Edge_Net_Subnet8[x+3,y,2,1,mask,1], Edge_Net_Subnet8[x+4,y,2,1,mask,1], Edge_Net_Subnet8[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet8[x,y,2,1,mask,1], ~Edge_Net_Subnet8[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet8[x-1,y,2,1,mask,1], Edge_Net_Subnet8[x-2,y,2,1,mask,1], Edge_Net_Subnet8[x-3,y,2,1,mask,1], Edge_Net_Subnet8[x-4,y,2,1,mask,1], Edge_Net_Subnet8[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,1], And(Edge_Net_Subnet8[x-1,y,2,1,mask,1], Edge_Net_Subnet8[x-2,y,2,1,mask,1], Edge_Net_Subnet8[x-3,y,2,1,mask,1], Edge_Net_Subnet8[x-4,y,2,1,mask,1], Edge_Net_Subnet8[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(18,18+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,1], And(Edge_Net_Subnet8[x+1,y,2,1,mask,1], Edge_Net_Subnet8[x+2,y,2,1,mask,1], Edge_Net_Subnet8[x+3,y,2,1,mask,1], Edge_Net_Subnet8[x+4,y,2,1,mask,1], Edge_Net_Subnet8[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(36-1,18)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,1], ~Edge_Net_Subnet8[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet8[x,y+1,2,0,mask,1], Edge_Net_Subnet8[x,y+2,2,0,mask,1], Edge_Net_Subnet8[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,1], ~Edge_Net_Subnet8[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet8[x,y-1,2,0,mask,1], Edge_Net_Subnet8[x,y-2,2,0,mask,1], Edge_Net_Subnet8[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet8[x,y,2,0,mask,1], And(Edge_Net_Subnet8[x,y+1,2,0,mask,1], Edge_Net_Subnet8[x,y+2,2,0,mask,1], Edge_Net_Subnet8[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet8[x,y,2,0,mask,1], And(Edge_Net_Subnet8[x,y-1,2,0,mask,1], Edge_Net_Subnet8[x,y-2,2,0,mask,1], Edge_Net_Subnet8[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(35,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(18,36+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(18,36+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(18,36+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net8_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet8[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net8_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(18,36+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(18,36+1)])for y in range(3,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(4,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(18,36+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(18,36+1)])for y in range(0,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(18,36+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(18,36+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet8[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(18,36+1)])for y in range(0,35+1)])
	).to_cnf()
Net8_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(18,36+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(18,36+1)])for y in range(2,35+1)]),
	).to_cnf()
Net8_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(18,36+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet8[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(18,36+1)])for y in range(2,35+1)]),
	).to_cnf()
Net8_Subnet1_DR = And(Net8_Subnet1_DR_Trend, Net8_Subnet1_DR_GIL_HorMinWidth,Net8_Subnet1_DR_GIL_HorMinSpacing,Net8_Subnet1_DR_GIL_VerMinSpacing,Net8_Subnet1_DR_AIL2_VerMinWidth,Net8_Subnet1_DR_AIL2_VerMinSpacing,Net8_Subnet1_DR_VerAIL2_HorMinSpacing,Net8_Subnet1_DR_MINT1AB_HorMinWidth,Net8_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net8_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net8_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net8_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net8_Subnet1_DR_M1AB_MinWidth,Net8_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net8_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net8_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net8_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net8_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net8_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net8_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net8_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net8_Subnet1_DR_V0_HorMinSpacing,Net8_Subnet1_DR_V1_HorMinSpacing,Net8_Subnet1_DR_V0_VerMinSpacing,Net8_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net8_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet8,[22,1,0,0, 22,2,0,0, 22,3,0,0, 22,4,0,0, 22,5,0,0, 22,6,0,0, ],6,18,0,1,36,35,3,1),
	RConstraints.R1(Edge_Net_Subnet8,[32,0,0,0, 32,1,0,0, 32,2,0,0, 32,3,0,0, 32,4,0,0, 32,5,0,0, 32,6,0,0, 32,7,0,0, 32,8,0,0, 32,9,0,0, 32,10,0,0, 32,11,0,0, 32,12,0,0, 32,13,0,0, 32,14,0,0, 32,15,0,0, 32,16,0,0, 32,17,0,0, 32,18,0,0, 32,19,0,0, 32,20,0,0, 32,21,0,0, 32,22,0,0, 32,23,0,0, 32,24,0,0, 32,25,0,0, 32,26,0,0, 32,27,0,0, 32,28,0,0, 32,29,0,0, 32,30,0,0, 32,31,0,0, 32,32,0,0, 32,33,0,0, 32,34,0,0, 32,35,0,0, ],36,18,0,1,36,35,3,1),
	).to_cnf()
Net8_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet8,Edge,Edge_Net,[22,1,0, 22,2,0, 22,3,0, 22,4,0, 22,5,0, 22,6,0, 22,7,0, 32,0,0, 32,1,0, 32,2,0, 32,3,0, 32,4,0, 32,5,0, 32,6,0, 32,7,0, 32,8,0, 32,9,0, 32,10,0, 32,11,0, 32,12,0, 32,13,0, 32,14,0, 32,15,0, 32,16,0, 32,17,0, 32,18,0, 32,19,0, 32,20,0, 32,21,0, 32,22,0, 32,23,0, 32,24,0, 32,25,0, 32,26,0, 32,27,0, 32,28,0, 32,29,0, 32,30,0, 32,31,0, 32,32,0, 32,33,0, 32,34,0, 32,35,0, ],43,18,0,0,36,35,3,1,7),
	)
Net8_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,7],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,6+1)])for x in range(18,36+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,7],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(8,12+1)])for x in range(18,36+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net8_Subnet1_R = And(Net8_Subnet1_R1,Net8_Subnet1_R2,Net8_Subnet1_R3,)
Net8_Subnet1_Formula = And(Net8_Subnet1_C,Net8_Subnet1_DR,Net8_Subnet1_R)
# Net = 7 Subnet = 0 | Left -> Right [16,28] Top -> Bottom [0,35]
# Range R1(24,24,0,35)
# Range R2(20,20,0,35)
### Disable edges outside window
Edge_Net_Subnet7[0:16,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(20736)
Edge_Net_Subnet7[28:77+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(64800)

### Consistency Constraints
Net7_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,6]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net7_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet7[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,6])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net7_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,2,trend,0,0],Xor(Edge_Net_Subnet7[x,y,2,trend,1,0],Edge_Net_Subnet7[x,y,2,trend,2,0])),And(~Edge_Net_Subnet7[x,y,2,trend,0,0],~Edge_Net_Subnet7[x,y,2,trend,1,0],~Edge_Net_Subnet7[x,y,2,trend,2,0]))for x in range(16,28+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net7_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,3,1,0,0],Xor(Edge_Net_Subnet7[x,y,3,1,1,0],Edge_Net_Subnet7[x,y,3,1,2,0])),And(~Edge_Net_Subnet7[x,y,3,1,0,0],~Edge_Net_Subnet7[x,y,3,1,1,0],~Edge_Net_Subnet7[x,y,3,1,2,0]))for x in range(16,28+1)])for y in range(0,35+1)]).to_cnf()
Net7_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,1,trend,2,0],Xor(Edge_Net_Subnet7[x,y,1,trend,0,0],Edge_Net_Subnet7[x,y,1,trend,1,0])),And(~Edge_Net_Subnet7[x,y,1,trend,2,0],~Edge_Net_Subnet7[x,y,1,trend,0,0],~Edge_Net_Subnet7[x,y,1,trend,1,0]))for x in range(16,28+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net7_Subnet0_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,1,0], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,2,s2])for s2 in range(0+1,5)]))for trend in range(0,1+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,2,0], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,1,s2])for s2 in range(0+1,5)]))for trend in range(0,1+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net7_Subnet0_C = And(Net7_Subnet0_C1, Net7_Subnet0_C2,Net7_Subnet0_C3_ME1_Mask,Net7_Subnet0_C4_MINT1_Mask,Net7_Subnet0_C5_AIL2GIL_Mask,Net7_Subnet0_C6,)
### Design Rules
Net7_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(16,28+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net7_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,1,1,1,0], ~Edge_Net_Subnet7[x-1,y,1,1,1,0]), And(Edge_Net_Subnet7[x+1,y,1,1,1,0], Edge_Net_Subnet7[x+2,y,1,1,1,0], Edge_Net_Subnet7[x+3,y,1,1,1,0], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,1,1,1,0], ~Edge_Net_Subnet7[x+1,y,1,1,1,0]), And(Edge_Net_Subnet7[x-1,y,1,1,1,0], Edge_Net_Subnet7[x-2,y,1,1,1,0], Edge_Net_Subnet7[x-3,y,1,1,1,0], ))for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(16,28+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(16,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,0]), And(Edge_Net_Subnet7[x,y+1,1,0,0,0], Edge_Net_Subnet7[x,y+2,1,0,0,0], Edge_Net_Subnet7[x,y+3,1,0,0,0], ))for x in range(16,28+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,0]), And(Edge_Net_Subnet7[x,y-1,1,0,0,0], Edge_Net_Subnet7[x,y-2,1,0,0,0], Edge_Net_Subnet7[x,y-3,1,0,0,0], ))for x in range(16,28+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,0], ~Edge_Net_Subnet7[x,y-1,1,0,0,0]), And(Edge_Net_Subnet7[x,y+1,1,0,0,0], Edge_Net_Subnet7[x,y+2,1,0,0,0], Edge_Net_Subnet7[x,y+3,1,0,0,0], ))for x in range(16,28+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,0], ~Edge_Net_Subnet7[x,y+1,1,0,0,0]), And(Edge_Net_Subnet7[x,y-1,1,0,0,0], Edge_Net_Subnet7[x,y-2,1,0,0,0], Edge_Net_Subnet7[x,y-3,1,0,0,0], ))for x in range(16,28+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net7_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(16,28+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(16,28+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(16,28+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(16,28+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(16,28+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(16,28+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net7_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,3,1,mask,0], ~Edge_Net_Subnet7[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet7[x+1,y,3,1,mask,0], Edge_Net_Subnet7[x+2,y,3,1,mask,0], Edge_Net_Subnet7[x+3,y,3,1,mask,0], Edge_Net_Subnet7[x+4,y,3,1,mask,0], Edge_Net_Subnet7[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,3,1,mask,0], ~Edge_Net_Subnet7[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet7[x-1,y,3,1,mask,0], Edge_Net_Subnet7[x-2,y,3,1,mask,0], Edge_Net_Subnet7[x-3,y,3,1,mask,0], Edge_Net_Subnet7[x-4,y,3,1,mask,0], Edge_Net_Subnet7[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(16,28+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(16,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,2,1,mask,0], ~Edge_Net_Subnet7[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet7[x+1,y,2,1,mask,0], Edge_Net_Subnet7[x+2,y,2,1,mask,0], Edge_Net_Subnet7[x+3,y,2,1,mask,0], Edge_Net_Subnet7[x+4,y,2,1,mask,0], Edge_Net_Subnet7[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,2,1,mask,0], ~Edge_Net_Subnet7[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet7[x-1,y,2,1,mask,0], Edge_Net_Subnet7[x-2,y,2,1,mask,0], Edge_Net_Subnet7[x-3,y,2,1,mask,0], Edge_Net_Subnet7[x-4,y,2,1,mask,0], Edge_Net_Subnet7[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,0], And(Edge_Net_Subnet7[x-1,y,2,1,mask,0], Edge_Net_Subnet7[x-2,y,2,1,mask,0], Edge_Net_Subnet7[x-3,y,2,1,mask,0], Edge_Net_Subnet7[x-4,y,2,1,mask,0], Edge_Net_Subnet7[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(16,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,0], And(Edge_Net_Subnet7[x+1,y,2,1,mask,0], Edge_Net_Subnet7[x+2,y,2,1,mask,0], Edge_Net_Subnet7[x+3,y,2,1,mask,0], Edge_Net_Subnet7[x+4,y,2,1,mask,0], Edge_Net_Subnet7[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(28-1,16)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,0], ~Edge_Net_Subnet7[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet7[x,y+1,2,0,mask,0], Edge_Net_Subnet7[x,y+2,2,0,mask,0], Edge_Net_Subnet7[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,0], ~Edge_Net_Subnet7[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet7[x,y-1,2,0,mask,0], Edge_Net_Subnet7[x,y-2,2,0,mask,0], Edge_Net_Subnet7[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet7[x,y,2,0,mask,0], And(Edge_Net_Subnet7[x,y+1,2,0,mask,0], Edge_Net_Subnet7[x,y+2,2,0,mask,0], Edge_Net_Subnet7[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet7[x,y,2,0,mask,0], And(Edge_Net_Subnet7[x,y-1,2,0,mask,0], Edge_Net_Subnet7[x,y-2,2,0,mask,0], Edge_Net_Subnet7[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(35,35+1)]),
	).to_cnf()
Net7_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(16,28+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(16,28+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net7_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net7_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(16,28+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(16,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(4,35+1)]),
	).to_cnf()
Net7_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet0_DR = And(Net7_Subnet0_DR_Trend, Net7_Subnet0_DR_GIL_HorMinWidth,Net7_Subnet0_DR_GIL_HorMinSpacing,Net7_Subnet0_DR_GIL_VerMinSpacing,Net7_Subnet0_DR_AIL2_VerMinWidth,Net7_Subnet0_DR_AIL2_VerMinSpacing,Net7_Subnet0_DR_VerAIL2_HorMinSpacing,Net7_Subnet0_DR_MINT1AB_HorMinWidth,Net7_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net7_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net7_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net7_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net7_Subnet0_DR_M1AB_MinWidth,Net7_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net7_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net7_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net7_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net7_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net7_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net7_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net7_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net7_Subnet0_DR_V0_HorMinSpacing,Net7_Subnet0_DR_V1_HorMinSpacing,Net7_Subnet0_DR_V0_VerMinSpacing,Net7_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net7_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet7,[24,0,0,0, 24,1,0,0, 24,2,0,0, 24,3,0,0, 24,4,0,0, 24,5,0,0, 24,6,0,0, 24,7,0,0, 24,8,0,0, 24,9,0,0, 24,10,0,0, 24,11,0,0, 24,12,0,0, 24,13,0,0, 24,14,0,0, 24,15,0,0, 24,16,0,0, 24,17,0,0, 24,18,0,0, 24,19,0,0, 24,20,0,0, 24,21,0,0, 24,22,0,0, 24,23,0,0, 24,24,0,0, 24,25,0,0, 24,26,0,0, 24,27,0,0, 24,28,0,0, 24,29,0,0, 24,30,0,0, 24,31,0,0, 24,32,0,0, 24,33,0,0, 24,34,0,0, 24,35,0,0, ],36,16,0,1,28,35,3,0),
	RConstraints.R1(Edge_Net_Subnet7,[20,0,0,0, 20,1,0,0, 20,2,0,0, 20,3,0,0, 20,4,0,0, 20,5,0,0, 20,6,0,0, 20,7,0,0, 20,8,0,0, 20,9,0,0, 20,10,0,0, 20,11,0,0, 20,12,0,0, 20,13,0,0, 20,14,0,0, 20,15,0,0, 20,16,0,0, 20,17,0,0, 20,18,0,0, 20,19,0,0, 20,20,0,0, 20,21,0,0, 20,22,0,0, 20,23,0,0, 20,24,0,0, 20,25,0,0, 20,26,0,0, 20,27,0,0, 20,28,0,0, 20,29,0,0, 20,30,0,0, 20,31,0,0, 20,32,0,0, 20,33,0,0, 20,34,0,0, 20,35,0,0, ],36,16,0,1,28,35,3,0),
	).to_cnf()
Net7_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet7,Edge,Edge_Net,[24,0,0, 24,1,0, 24,2,0, 24,3,0, 24,4,0, 24,5,0, 24,6,0, 24,7,0, 24,8,0, 24,9,0, 24,10,0, 24,11,0, 24,12,0, 24,13,0, 24,14,0, 24,15,0, 24,16,0, 24,17,0, 24,18,0, 24,19,0, 24,20,0, 24,21,0, 24,22,0, 24,23,0, 24,24,0, 24,25,0, 24,26,0, 24,27,0, 24,28,0, 24,29,0, 24,30,0, 24,31,0, 24,32,0, 24,33,0, 24,34,0, 24,35,0, 20,0,0, 20,1,0, 20,2,0, 20,3,0, 20,4,0, 20,5,0, 20,6,0, 20,7,0, 20,8,0, 20,9,0, 20,10,0, 20,11,0, 20,12,0, 20,13,0, 20,14,0, 20,15,0, 20,16,0, 20,17,0, 20,18,0, 20,19,0, 20,20,0, 20,21,0, 20,22,0, 20,23,0, 20,24,0, 20,25,0, 20,26,0, 20,27,0, 20,28,0, 20,29,0, 20,30,0, 20,31,0, 20,32,0, 20,33,0, 20,34,0, 20,35,0, ],72,16,0,0,28,35,3,0,6),
	)
Net7_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,6],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,5+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,6],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(7,12+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net7_Subnet0_R = And(Net7_Subnet0_R1,Net7_Subnet0_R2,Net7_Subnet0_R3,)
Net7_Subnet0_Formula = And(Net7_Subnet0_C,Net7_Subnet0_DR,Net7_Subnet0_R)
# Net = 7 Subnet = 1 | Left -> Right [20,40] Top -> Bottom [0,35]
# Range R1(24,24,0,35)
# Range R2(36,36,0,35)
### Disable edges outside window
Edge_Net_Subnet7[0:20,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(25920)
Edge_Net_Subnet7[40:77+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(49248)

### Consistency Constraints
Net7_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,6]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net7_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet7[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,6])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net7_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,2,trend,0,1],Xor(Edge_Net_Subnet7[x,y,2,trend,1,1],Edge_Net_Subnet7[x,y,2,trend,2,1])),And(~Edge_Net_Subnet7[x,y,2,trend,0,1],~Edge_Net_Subnet7[x,y,2,trend,1,1],~Edge_Net_Subnet7[x,y,2,trend,2,1]))for x in range(20,40+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net7_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,3,1,0,1],Xor(Edge_Net_Subnet7[x,y,3,1,1,1],Edge_Net_Subnet7[x,y,3,1,2,1])),And(~Edge_Net_Subnet7[x,y,3,1,0,1],~Edge_Net_Subnet7[x,y,3,1,1,1],~Edge_Net_Subnet7[x,y,3,1,2,1]))for x in range(20,40+1)])for y in range(0,35+1)]).to_cnf()
Net7_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,1,trend,2,1],Xor(Edge_Net_Subnet7[x,y,1,trend,0,1],Edge_Net_Subnet7[x,y,1,trend,1,1])),And(~Edge_Net_Subnet7[x,y,1,trend,2,1],~Edge_Net_Subnet7[x,y,1,trend,0,1],~Edge_Net_Subnet7[x,y,1,trend,1,1]))for x in range(20,40+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net7_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,2,s2])for s2 in range(1+1,5)]))for trend in range(0,1+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,1,s2])for s2 in range(1+1,5)]))for trend in range(0,1+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net7_Subnet1_C = And(Net7_Subnet1_C1, Net7_Subnet1_C2,Net7_Subnet1_C3_ME1_Mask,Net7_Subnet1_C4_MINT1_Mask,Net7_Subnet1_C5_AIL2GIL_Mask,Net7_Subnet1_C6,)
### Design Rules
Net7_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(20,40+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net7_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,1,1,1,1], ~Edge_Net_Subnet7[x-1,y,1,1,1,1]), And(Edge_Net_Subnet7[x+1,y,1,1,1,1], Edge_Net_Subnet7[x+2,y,1,1,1,1], Edge_Net_Subnet7[x+3,y,1,1,1,1], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,1,1,1,1], ~Edge_Net_Subnet7[x+1,y,1,1,1,1]), And(Edge_Net_Subnet7[x-1,y,1,1,1,1], Edge_Net_Subnet7[x-2,y,1,1,1,1], Edge_Net_Subnet7[x-3,y,1,1,1,1], ))for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(20,40+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(20,40+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,1]), And(Edge_Net_Subnet7[x,y+1,1,0,0,1], Edge_Net_Subnet7[x,y+2,1,0,0,1], Edge_Net_Subnet7[x,y+3,1,0,0,1], ))for x in range(20,40+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,1]), And(Edge_Net_Subnet7[x,y-1,1,0,0,1], Edge_Net_Subnet7[x,y-2,1,0,0,1], Edge_Net_Subnet7[x,y-3,1,0,0,1], ))for x in range(20,40+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,1], ~Edge_Net_Subnet7[x,y-1,1,0,0,1]), And(Edge_Net_Subnet7[x,y+1,1,0,0,1], Edge_Net_Subnet7[x,y+2,1,0,0,1], Edge_Net_Subnet7[x,y+3,1,0,0,1], ))for x in range(20,40+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,1], ~Edge_Net_Subnet7[x,y+1,1,0,0,1]), And(Edge_Net_Subnet7[x,y-1,1,0,0,1], Edge_Net_Subnet7[x,y-2,1,0,0,1], Edge_Net_Subnet7[x,y-3,1,0,0,1], ))for x in range(20,40+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net7_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(20,40+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(20,40+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(20,40+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(20,40+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(20,40+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(20,40+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net7_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,3,1,mask,1], ~Edge_Net_Subnet7[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet7[x+1,y,3,1,mask,1], Edge_Net_Subnet7[x+2,y,3,1,mask,1], Edge_Net_Subnet7[x+3,y,3,1,mask,1], Edge_Net_Subnet7[x+4,y,3,1,mask,1], Edge_Net_Subnet7[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,3,1,mask,1], ~Edge_Net_Subnet7[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet7[x-1,y,3,1,mask,1], Edge_Net_Subnet7[x-2,y,3,1,mask,1], Edge_Net_Subnet7[x-3,y,3,1,mask,1], Edge_Net_Subnet7[x-4,y,3,1,mask,1], Edge_Net_Subnet7[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(20,40+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(20,40+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,2,1,mask,1], ~Edge_Net_Subnet7[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet7[x+1,y,2,1,mask,1], Edge_Net_Subnet7[x+2,y,2,1,mask,1], Edge_Net_Subnet7[x+3,y,2,1,mask,1], Edge_Net_Subnet7[x+4,y,2,1,mask,1], Edge_Net_Subnet7[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,2,1,mask,1], ~Edge_Net_Subnet7[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet7[x-1,y,2,1,mask,1], Edge_Net_Subnet7[x-2,y,2,1,mask,1], Edge_Net_Subnet7[x-3,y,2,1,mask,1], Edge_Net_Subnet7[x-4,y,2,1,mask,1], Edge_Net_Subnet7[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,1], And(Edge_Net_Subnet7[x-1,y,2,1,mask,1], Edge_Net_Subnet7[x-2,y,2,1,mask,1], Edge_Net_Subnet7[x-3,y,2,1,mask,1], Edge_Net_Subnet7[x-4,y,2,1,mask,1], Edge_Net_Subnet7[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(20,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,1], And(Edge_Net_Subnet7[x+1,y,2,1,mask,1], Edge_Net_Subnet7[x+2,y,2,1,mask,1], Edge_Net_Subnet7[x+3,y,2,1,mask,1], Edge_Net_Subnet7[x+4,y,2,1,mask,1], Edge_Net_Subnet7[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(40-1,20)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,1], ~Edge_Net_Subnet7[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet7[x,y+1,2,0,mask,1], Edge_Net_Subnet7[x,y+2,2,0,mask,1], Edge_Net_Subnet7[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,1], ~Edge_Net_Subnet7[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet7[x,y-1,2,0,mask,1], Edge_Net_Subnet7[x,y-2,2,0,mask,1], Edge_Net_Subnet7[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet7[x,y,2,0,mask,1], And(Edge_Net_Subnet7[x,y+1,2,0,mask,1], Edge_Net_Subnet7[x,y+2,2,0,mask,1], Edge_Net_Subnet7[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet7[x,y,2,0,mask,1], And(Edge_Net_Subnet7[x,y-1,2,0,mask,1], Edge_Net_Subnet7[x,y-2,2,0,mask,1], Edge_Net_Subnet7[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(35,35+1)]),
	).to_cnf()
Net7_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(20,40+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(20,40+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net7_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net7_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(20,40+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(20,40+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(4,35+1)]),
	).to_cnf()
Net7_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(20,40+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,40+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet1_DR = And(Net7_Subnet1_DR_Trend, Net7_Subnet1_DR_GIL_HorMinWidth,Net7_Subnet1_DR_GIL_HorMinSpacing,Net7_Subnet1_DR_GIL_VerMinSpacing,Net7_Subnet1_DR_AIL2_VerMinWidth,Net7_Subnet1_DR_AIL2_VerMinSpacing,Net7_Subnet1_DR_VerAIL2_HorMinSpacing,Net7_Subnet1_DR_MINT1AB_HorMinWidth,Net7_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net7_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net7_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net7_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net7_Subnet1_DR_M1AB_MinWidth,Net7_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net7_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net7_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net7_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net7_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net7_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net7_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net7_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net7_Subnet1_DR_V0_HorMinSpacing,Net7_Subnet1_DR_V1_HorMinSpacing,Net7_Subnet1_DR_V0_VerMinSpacing,Net7_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net7_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet7,[24,0,0,0, 24,1,0,0, 24,2,0,0, 24,3,0,0, 24,4,0,0, 24,5,0,0, 24,6,0,0, 24,7,0,0, 24,8,0,0, 24,9,0,0, 24,10,0,0, 24,11,0,0, 24,12,0,0, 24,13,0,0, 24,14,0,0, 24,15,0,0, 24,16,0,0, 24,17,0,0, 24,18,0,0, 24,19,0,0, 24,20,0,0, 24,21,0,0, 24,22,0,0, 24,23,0,0, 24,24,0,0, 24,25,0,0, 24,26,0,0, 24,27,0,0, 24,28,0,0, 24,29,0,0, 24,30,0,0, 24,31,0,0, 24,32,0,0, 24,33,0,0, 24,34,0,0, 24,35,0,0, ],36,20,0,1,40,35,3,1),
	RConstraints.R1(Edge_Net_Subnet7,[36,0,0,0, 36,1,0,0, 36,2,0,0, 36,3,0,0, 36,4,0,0, 36,5,0,0, 36,6,0,0, 36,7,0,0, 36,8,0,0, 36,9,0,0, 36,10,0,0, 36,11,0,0, 36,12,0,0, 36,13,0,0, 36,14,0,0, 36,15,0,0, 36,16,0,0, 36,17,0,0, 36,18,0,0, 36,19,0,0, 36,20,0,0, 36,21,0,0, 36,22,0,0, 36,23,0,0, 36,24,0,0, 36,25,0,0, 36,26,0,0, 36,27,0,0, 36,28,0,0, 36,29,0,0, 36,30,0,0, 36,31,0,0, 36,32,0,0, 36,33,0,0, 36,34,0,0, 36,35,0,0, ],36,20,0,1,40,35,3,1),
	).to_cnf()
Net7_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet7,Edge,Edge_Net,[24,0,0, 24,1,0, 24,2,0, 24,3,0, 24,4,0, 24,5,0, 24,6,0, 24,7,0, 24,8,0, 24,9,0, 24,10,0, 24,11,0, 24,12,0, 24,13,0, 24,14,0, 24,15,0, 24,16,0, 24,17,0, 24,18,0, 24,19,0, 24,20,0, 24,21,0, 24,22,0, 24,23,0, 24,24,0, 24,25,0, 24,26,0, 24,27,0, 24,28,0, 24,29,0, 24,30,0, 24,31,0, 24,32,0, 24,33,0, 24,34,0, 24,35,0, 36,0,0, 36,1,0, 36,2,0, 36,3,0, 36,4,0, 36,5,0, 36,6,0, 36,7,0, 36,8,0, 36,9,0, 36,10,0, 36,11,0, 36,12,0, 36,13,0, 36,14,0, 36,15,0, 36,16,0, 36,17,0, 36,18,0, 36,19,0, 36,20,0, 36,21,0, 36,22,0, 36,23,0, 36,24,0, 36,25,0, 36,26,0, 36,27,0, 36,28,0, 36,29,0, 36,30,0, 36,31,0, 36,32,0, 36,33,0, 36,34,0, 36,35,0, ],72,20,0,0,40,35,3,1,6),
	)
Net7_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,6],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,5+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,6],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(7,12+1)])for x in range(20,40+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net7_Subnet1_R = And(Net7_Subnet1_R1,Net7_Subnet1_R2,Net7_Subnet1_R3,)
Net7_Subnet1_Formula = And(Net7_Subnet1_C,Net7_Subnet1_DR,Net7_Subnet1_R)
# Net = 7 Subnet = 2 | Left -> Right [32,44] Top -> Bottom [0,35]
# Range R1(36,36,0,35)
# Range R2(40,40,0,35)
### Disable edges outside window
Edge_Net_Subnet7[0:32,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(41472)
Edge_Net_Subnet7[44:77+1,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(44064)

### Consistency Constraints
Net7_Subnet2_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,6]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net7_Subnet2_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet7[x,y,z,trend,mask,2]), Edge_Net[x,y,z,trend,mask,6])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net7_Subnet2_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,2,trend,0,2],Xor(Edge_Net_Subnet7[x,y,2,trend,1,2],Edge_Net_Subnet7[x,y,2,trend,2,2])),And(~Edge_Net_Subnet7[x,y,2,trend,0,2],~Edge_Net_Subnet7[x,y,2,trend,1,2],~Edge_Net_Subnet7[x,y,2,trend,2,2]))for x in range(32,44+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net7_Subnet2_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,3,1,0,2],Xor(Edge_Net_Subnet7[x,y,3,1,1,2],Edge_Net_Subnet7[x,y,3,1,2,2])),And(~Edge_Net_Subnet7[x,y,3,1,0,2],~Edge_Net_Subnet7[x,y,3,1,1,2],~Edge_Net_Subnet7[x,y,3,1,2,2]))for x in range(32,44+1)])for y in range(0,35+1)]).to_cnf()
Net7_Subnet2_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,1,trend,2,2],Xor(Edge_Net_Subnet7[x,y,1,trend,0,2],Edge_Net_Subnet7[x,y,1,trend,1,2])),And(~Edge_Net_Subnet7[x,y,1,trend,2,2],~Edge_Net_Subnet7[x,y,1,trend,0,2],~Edge_Net_Subnet7[x,y,1,trend,1,2]))for x in range(32,44+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net7_Subnet2_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,2,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,2,s2])for s2 in range(2+1,5)]))for trend in range(0,1+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,1,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,1,s2])for s2 in range(2+1,5)]))for trend in range(0,1+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net7_Subnet2_C = And(Net7_Subnet2_C1, Net7_Subnet2_C2,Net7_Subnet2_C3_ME1_Mask,Net7_Subnet2_C4_MINT1_Mask,Net7_Subnet2_C5_AIL2GIL_Mask,Net7_Subnet2_C6,)
### Design Rules
Net7_Subnet2_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(32,44+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net7_Subnet2_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,1,1,1,2], ~Edge_Net_Subnet7[x-1,y,1,1,1,2]), And(Edge_Net_Subnet7[x+1,y,1,1,1,2], Edge_Net_Subnet7[x+2,y,1,1,1,2], Edge_Net_Subnet7[x+3,y,1,1,1,2], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,1,1,1,2], ~Edge_Net_Subnet7[x+1,y,1,1,1,2]), And(Edge_Net_Subnet7[x-1,y,1,1,1,2], Edge_Net_Subnet7[x-2,y,1,1,1,2], Edge_Net_Subnet7[x-3,y,1,1,1,2], ))for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet2_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,1,1,2], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,1,1,2], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet2_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,1,1,2], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(32,44+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,1,1,2], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(32,44+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet2_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,2]), And(Edge_Net_Subnet7[x,y+1,1,0,0,2], Edge_Net_Subnet7[x,y+2,1,0,0,2], Edge_Net_Subnet7[x,y+3,1,0,0,2], ))for x in range(32,44+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,2]), And(Edge_Net_Subnet7[x,y-1,1,0,0,2], Edge_Net_Subnet7[x,y-2,1,0,0,2], Edge_Net_Subnet7[x,y-3,1,0,0,2], ))for x in range(32,44+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,2], ~Edge_Net_Subnet7[x,y-1,1,0,0,2]), And(Edge_Net_Subnet7[x,y+1,1,0,0,2], Edge_Net_Subnet7[x,y+2,1,0,0,2], Edge_Net_Subnet7[x,y+3,1,0,0,2], ))for x in range(32,44+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,2], ~Edge_Net_Subnet7[x,y+1,1,0,0,2]), And(Edge_Net_Subnet7[x,y-1,1,0,0,2], Edge_Net_Subnet7[x,y-2,1,0,0,2], Edge_Net_Subnet7[x,y-3,1,0,0,2], ))for x in range(32,44+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net7_Subnet2_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(32,44+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(32,44+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(32,44+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(32,44+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(32,44+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(32,44+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net7_Subnet2_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,0,0,2], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,0,0,2], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet2_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,3,1,mask,2], ~Edge_Net_Subnet7[x-1,y,3,1,mask,2]), And(Edge_Net_Subnet7[x+1,y,3,1,mask,2], Edge_Net_Subnet7[x+2,y,3,1,mask,2], Edge_Net_Subnet7[x+3,y,3,1,mask,2], Edge_Net_Subnet7[x+4,y,3,1,mask,2], Edge_Net_Subnet7[x+5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,3,1,mask,2], ~Edge_Net_Subnet7[x+1,y,3,1,mask,2]), And(Edge_Net_Subnet7[x-1,y,3,1,mask,2], Edge_Net_Subnet7[x-2,y,3,1,mask,2], Edge_Net_Subnet7[x-3,y,3,1,mask,2], Edge_Net_Subnet7[x-4,y,3,1,mask,2], Edge_Net_Subnet7[x-5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet2_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,mask,2], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,mask,2], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet2_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,mask,2], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,mask,2], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet2_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,1,2], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(32,44+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,1,2], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(32,44+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet2_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,1,2], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,1,2], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet2_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,2,1,mask,2], ~Edge_Net_Subnet7[x-1,y,2,1,mask,2]), And(Edge_Net_Subnet7[x+1,y,2,1,mask,2], Edge_Net_Subnet7[x+2,y,2,1,mask,2], Edge_Net_Subnet7[x+3,y,2,1,mask,2], Edge_Net_Subnet7[x+4,y,2,1,mask,2], Edge_Net_Subnet7[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,2,1,mask,2], ~Edge_Net_Subnet7[x+1,y,2,1,mask,2]), And(Edge_Net_Subnet7[x-1,y,2,1,mask,2], Edge_Net_Subnet7[x-2,y,2,1,mask,2], Edge_Net_Subnet7[x-3,y,2,1,mask,2], Edge_Net_Subnet7[x-4,y,2,1,mask,2], Edge_Net_Subnet7[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,2], And(Edge_Net_Subnet7[x-1,y,2,1,mask,2], Edge_Net_Subnet7[x-2,y,2,1,mask,2], Edge_Net_Subnet7[x-3,y,2,1,mask,2], Edge_Net_Subnet7[x-4,y,2,1,mask,2], Edge_Net_Subnet7[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(32,32+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,2], And(Edge_Net_Subnet7[x+1,y,2,1,mask,2], Edge_Net_Subnet7[x+2,y,2,1,mask,2], Edge_Net_Subnet7[x+3,y,2,1,mask,2], Edge_Net_Subnet7[x+4,y,2,1,mask,2], Edge_Net_Subnet7[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(44-1,32)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,2], ~Edge_Net_Subnet7[x,y-1,2,0,mask,2]), And(Edge_Net_Subnet7[x,y+1,2,0,mask,2], Edge_Net_Subnet7[x,y+2,2,0,mask,2], Edge_Net_Subnet7[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,2], ~Edge_Net_Subnet7[x,y+1,2,0,mask,2]), And(Edge_Net_Subnet7[x,y-1,2,0,mask,2], Edge_Net_Subnet7[x,y-2,2,0,mask,2], Edge_Net_Subnet7[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet7[x,y,2,0,mask,2], And(Edge_Net_Subnet7[x,y+1,2,0,mask,2], Edge_Net_Subnet7[x,y+2,2,0,mask,2], Edge_Net_Subnet7[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet7[x,y,2,0,mask,2], And(Edge_Net_Subnet7[x,y-1,2,0,mask,2], Edge_Net_Subnet7[x,y-2,2,0,mask,2], Edge_Net_Subnet7[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(35,35+1)]),
	).to_cnf()
Net7_Subnet2_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,1,2], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,1,2], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet2_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,mask,2], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,mask,2], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet2_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,1,2], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(32,44+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,1,2], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(32,44+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net7_Subnet2_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,2], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,2], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net7_Subnet2_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,1,2], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(32,44+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,1,2], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(32,44+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet2_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,2], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,2], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(4,35+1)]),
	).to_cnf()
Net7_Subnet2_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,1,2], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,1,2], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(32,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet2_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,mask,2], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,mask,2], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet2_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,1,2,mask,2], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,1,2,mask,2], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet2_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,2,2,mask,2], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,2,2,mask,2], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet2_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,2,mask,2], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,2,mask,2], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet2_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,2,mask,2], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,2,mask,2], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(32,44+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet2_DR = And(Net7_Subnet2_DR_Trend, Net7_Subnet2_DR_GIL_HorMinWidth,Net7_Subnet2_DR_GIL_HorMinSpacing,Net7_Subnet2_DR_GIL_VerMinSpacing,Net7_Subnet2_DR_AIL2_VerMinWidth,Net7_Subnet2_DR_AIL2_VerMinSpacing,Net7_Subnet2_DR_VerAIL2_HorMinSpacing,Net7_Subnet2_DR_MINT1AB_HorMinWidth,Net7_Subnet2_DR_MINT1_SameMask_VerMinSpacing,Net7_Subnet2_DR_MINT1_SameMask_HorMinSpacing,Net7_Subnet2_DR_MINT1_DiffMask_VerMinSpacing,Net7_Subnet2_DR_MINT1_DiffMask_HorMinSpacing,Net7_Subnet2_DR_M1AB_MinWidth,Net7_Subnet2_DR_HorM1_DiffMask_HorMinSpacing,Net7_Subnet2_DR_HorM1_SameMask_HorMinSpacing,Net7_Subnet2_DR_VerM1_DiffMask_VerMinSpacing,Net7_Subnet2_DR_VerM1_SameMask_VerMinSpacing,Net7_Subnet2_DR_HorM1_DiffMask_VerMinSpacing,Net7_Subnet2_DR_HorM1_SameMask_VerMinSpacing,Net7_Subnet2_DR_VerM1_DiffMask_HorMinSpacing,Net7_Subnet2_DR_VerM1_SameMask_HorMinSpacing,Net7_Subnet2_DR_V0_HorMinSpacing,Net7_Subnet2_DR_V1_HorMinSpacing,Net7_Subnet2_DR_V0_VerMinSpacing,Net7_Subnet2_DR_V1_VerMinSpacing,)
### Routability Constraints
Net7_Subnet2_R1 = And(
	RConstraints.R1(Edge_Net_Subnet7,[36,0,0,0, 36,1,0,0, 36,2,0,0, 36,3,0,0, 36,4,0,0, 36,5,0,0, 36,6,0,0, 36,7,0,0, 36,8,0,0, 36,9,0,0, 36,10,0,0, 36,11,0,0, 36,12,0,0, 36,13,0,0, 36,14,0,0, 36,15,0,0, 36,16,0,0, 36,17,0,0, 36,18,0,0, 36,19,0,0, 36,20,0,0, 36,21,0,0, 36,22,0,0, 36,23,0,0, 36,24,0,0, 36,25,0,0, 36,26,0,0, 36,27,0,0, 36,28,0,0, 36,29,0,0, 36,30,0,0, 36,31,0,0, 36,32,0,0, 36,33,0,0, 36,34,0,0, 36,35,0,0, ],36,32,0,1,44,35,3,2),
	RConstraints.R1(Edge_Net_Subnet7,[40,0,0,0, 40,1,0,0, 40,2,0,0, 40,3,0,0, 40,4,0,0, 40,5,0,0, 40,6,0,0, 40,7,0,0, 40,8,0,0, 40,9,0,0, 40,10,0,0, 40,11,0,0, 40,12,0,0, 40,13,0,0, 40,14,0,0, 40,15,0,0, 40,16,0,0, 40,17,0,0, 40,18,0,0, 40,19,0,0, 40,20,0,0, 40,21,0,0, 40,22,0,0, 40,23,0,0, 40,24,0,0, 40,25,0,0, 40,26,0,0, 40,27,0,0, 40,28,0,0, 40,29,0,0, 40,30,0,0, 40,31,0,0, 40,32,0,0, 40,33,0,0, 40,34,0,0, 40,35,0,0, ],36,32,0,1,44,35,3,2),
	).to_cnf()
Net7_Subnet2_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet7,Edge,Edge_Net,[36,0,0, 36,1,0, 36,2,0, 36,3,0, 36,4,0, 36,5,0, 36,6,0, 36,7,0, 36,8,0, 36,9,0, 36,10,0, 36,11,0, 36,12,0, 36,13,0, 36,14,0, 36,15,0, 36,16,0, 36,17,0, 36,18,0, 36,19,0, 36,20,0, 36,21,0, 36,22,0, 36,23,0, 36,24,0, 36,25,0, 36,26,0, 36,27,0, 36,28,0, 36,29,0, 36,30,0, 36,31,0, 36,32,0, 36,33,0, 36,34,0, 36,35,0, 40,0,0, 40,1,0, 40,2,0, 40,3,0, 40,4,0, 40,5,0, 40,6,0, 40,7,0, 40,8,0, 40,9,0, 40,10,0, 40,11,0, 40,12,0, 40,13,0, 40,14,0, 40,15,0, 40,16,0, 40,17,0, 40,18,0, 40,19,0, 40,20,0, 40,21,0, 40,22,0, 40,23,0, 40,24,0, 40,25,0, 40,26,0, 40,27,0, 40,28,0, 40,29,0, 40,30,0, 40,31,0, 40,32,0, 40,33,0, 40,34,0, 40,35,0, ],72,32,0,0,44,35,3,2,6),
	)
Net7_Subnet2_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,6],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,5+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,6],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(7,12+1)])for x in range(32,44+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net7_Subnet2_R = And(Net7_Subnet2_R1,Net7_Subnet2_R2,Net7_Subnet2_R3,)
Net7_Subnet2_Formula = And(Net7_Subnet2_C,Net7_Subnet2_DR,Net7_Subnet2_R)
# Net = 7 Subnet = 3 | Left -> Right [20,44] Top -> Bottom [0,35]
# Range R1(40,40,0,35)
# Range R2(24,24,0,35)
### Disable edges outside window
Edge_Net_Subnet7[0:20,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(25920)
Edge_Net_Subnet7[44:77+1,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(44064)

### Consistency Constraints
Net7_Subnet3_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,6]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(20,44+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net7_Subnet3_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet7[x,y,z,trend,mask,3]), Edge_Net[x,y,z,trend,mask,6])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(20,44+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net7_Subnet3_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,2,trend,0,3],Xor(Edge_Net_Subnet7[x,y,2,trend,1,3],Edge_Net_Subnet7[x,y,2,trend,2,3])),And(~Edge_Net_Subnet7[x,y,2,trend,0,3],~Edge_Net_Subnet7[x,y,2,trend,1,3],~Edge_Net_Subnet7[x,y,2,trend,2,3]))for x in range(20,44+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net7_Subnet3_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,3,1,0,3],Xor(Edge_Net_Subnet7[x,y,3,1,1,3],Edge_Net_Subnet7[x,y,3,1,2,3])),And(~Edge_Net_Subnet7[x,y,3,1,0,3],~Edge_Net_Subnet7[x,y,3,1,1,3],~Edge_Net_Subnet7[x,y,3,1,2,3]))for x in range(20,44+1)])for y in range(0,35+1)]).to_cnf()
Net7_Subnet3_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,1,trend,2,3],Xor(Edge_Net_Subnet7[x,y,1,trend,0,3],Edge_Net_Subnet7[x,y,1,trend,1,3])),And(~Edge_Net_Subnet7[x,y,1,trend,2,3],~Edge_Net_Subnet7[x,y,1,trend,0,3],~Edge_Net_Subnet7[x,y,1,trend,1,3]))for x in range(20,44+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net7_Subnet3_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,2,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(20,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,2,s2])for s2 in range(3+1,5)]))for trend in range(0,1+1)])for x in range(20,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,1,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(20,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,1,s2])for s2 in range(3+1,5)]))for trend in range(0,1+1)])for x in range(20,44+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net7_Subnet3_C = And(Net7_Subnet3_C1, Net7_Subnet3_C2,Net7_Subnet3_C3_ME1_Mask,Net7_Subnet3_C4_MINT1_Mask,Net7_Subnet3_C5_AIL2GIL_Mask,Net7_Subnet3_C6,)
### Design Rules
Net7_Subnet3_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(20,44+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net7_Subnet3_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,1,1,1,3], ~Edge_Net_Subnet7[x-1,y,1,1,1,3]), And(Edge_Net_Subnet7[x+1,y,1,1,1,3], Edge_Net_Subnet7[x+2,y,1,1,1,3], Edge_Net_Subnet7[x+3,y,1,1,1,3], ))for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,1,1,1,3], ~Edge_Net_Subnet7[x+1,y,1,1,1,3]), And(Edge_Net_Subnet7[x-1,y,1,1,1,3], Edge_Net_Subnet7[x-2,y,1,1,1,3], Edge_Net_Subnet7[x-3,y,1,1,1,3], ))for x in range(20,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet3_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,1,1,3], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,1,1,3], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(20,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet3_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,1,1,3], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(20,44+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,1,1,3], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(20,44+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet3_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,3]), And(Edge_Net_Subnet7[x,y+1,1,0,0,3], Edge_Net_Subnet7[x,y+2,1,0,0,3], Edge_Net_Subnet7[x,y+3,1,0,0,3], ))for x in range(20,44+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,3]), And(Edge_Net_Subnet7[x,y-1,1,0,0,3], Edge_Net_Subnet7[x,y-2,1,0,0,3], Edge_Net_Subnet7[x,y-3,1,0,0,3], ))for x in range(20,44+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,3], ~Edge_Net_Subnet7[x,y-1,1,0,0,3]), And(Edge_Net_Subnet7[x,y+1,1,0,0,3], Edge_Net_Subnet7[x,y+2,1,0,0,3], Edge_Net_Subnet7[x,y+3,1,0,0,3], ))for x in range(20,44+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,3], ~Edge_Net_Subnet7[x,y+1,1,0,0,3]), And(Edge_Net_Subnet7[x,y-1,1,0,0,3], Edge_Net_Subnet7[x,y-2,1,0,0,3], Edge_Net_Subnet7[x,y-3,1,0,0,3], ))for x in range(20,44+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net7_Subnet3_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(20,44+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(20,44+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(20,44+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(20,44+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(20,44+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(20,44+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net7_Subnet3_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,0,0,3], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,0,0,3], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(20,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet3_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,3,1,mask,3], ~Edge_Net_Subnet7[x-1,y,3,1,mask,3]), And(Edge_Net_Subnet7[x+1,y,3,1,mask,3], Edge_Net_Subnet7[x+2,y,3,1,mask,3], Edge_Net_Subnet7[x+3,y,3,1,mask,3], Edge_Net_Subnet7[x+4,y,3,1,mask,3], Edge_Net_Subnet7[x+5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,3,1,mask,3], ~Edge_Net_Subnet7[x+1,y,3,1,mask,3]), And(Edge_Net_Subnet7[x-1,y,3,1,mask,3], Edge_Net_Subnet7[x-2,y,3,1,mask,3], Edge_Net_Subnet7[x-3,y,3,1,mask,3], Edge_Net_Subnet7[x-4,y,3,1,mask,3], Edge_Net_Subnet7[x-5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet3_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,mask,3], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,mask,3], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet3_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,mask,3], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,mask,3], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet3_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,1,3], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(20,44+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,1,3], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(20,44+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet3_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,1,3], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,1,3], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(20,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet3_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,2,1,mask,3], ~Edge_Net_Subnet7[x-1,y,2,1,mask,3]), And(Edge_Net_Subnet7[x+1,y,2,1,mask,3], Edge_Net_Subnet7[x+2,y,2,1,mask,3], Edge_Net_Subnet7[x+3,y,2,1,mask,3], Edge_Net_Subnet7[x+4,y,2,1,mask,3], Edge_Net_Subnet7[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,2,1,mask,3], ~Edge_Net_Subnet7[x+1,y,2,1,mask,3]), And(Edge_Net_Subnet7[x-1,y,2,1,mask,3], Edge_Net_Subnet7[x-2,y,2,1,mask,3], Edge_Net_Subnet7[x-3,y,2,1,mask,3], Edge_Net_Subnet7[x-4,y,2,1,mask,3], Edge_Net_Subnet7[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,3], And(Edge_Net_Subnet7[x-1,y,2,1,mask,3], Edge_Net_Subnet7[x-2,y,2,1,mask,3], Edge_Net_Subnet7[x-3,y,2,1,mask,3], Edge_Net_Subnet7[x-4,y,2,1,mask,3], Edge_Net_Subnet7[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(20,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,3], And(Edge_Net_Subnet7[x+1,y,2,1,mask,3], Edge_Net_Subnet7[x+2,y,2,1,mask,3], Edge_Net_Subnet7[x+3,y,2,1,mask,3], Edge_Net_Subnet7[x+4,y,2,1,mask,3], Edge_Net_Subnet7[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(44-1,20)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,3], ~Edge_Net_Subnet7[x,y-1,2,0,mask,3]), And(Edge_Net_Subnet7[x,y+1,2,0,mask,3], Edge_Net_Subnet7[x,y+2,2,0,mask,3], Edge_Net_Subnet7[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,3], ~Edge_Net_Subnet7[x,y+1,2,0,mask,3]), And(Edge_Net_Subnet7[x,y-1,2,0,mask,3], Edge_Net_Subnet7[x,y-2,2,0,mask,3], Edge_Net_Subnet7[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet7[x,y,2,0,mask,3], And(Edge_Net_Subnet7[x,y+1,2,0,mask,3], Edge_Net_Subnet7[x,y+2,2,0,mask,3], Edge_Net_Subnet7[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet7[x,y,2,0,mask,3], And(Edge_Net_Subnet7[x,y-1,2,0,mask,3], Edge_Net_Subnet7[x,y-2,2,0,mask,3], Edge_Net_Subnet7[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(35,35+1)]),
	).to_cnf()
Net7_Subnet3_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,1,3], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,1,3], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(20,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet3_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,mask,3], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,mask,3], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet3_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,1,3], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(20,44+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,1,3], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(20,44+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net7_Subnet3_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,3], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,3], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net7_Subnet3_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,1,3], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(20,44+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,1,3], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(20,44+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet3_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,3], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,3], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(4,35+1)]),
	).to_cnf()
Net7_Subnet3_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,1,3], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,1,3], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(20,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet3_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,mask,3], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,mask,3], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,44+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet3_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,1,2,mask,3], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,1,2,mask,3], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet3_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,2,2,mask,3], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,44+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,2,2,mask,3], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,44+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet3_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,2,mask,3], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,44+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,2,mask,3], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,44+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet3_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,2,mask,3], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,44+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,2,mask,3], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,44+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet3_DR = And(Net7_Subnet3_DR_Trend, Net7_Subnet3_DR_GIL_HorMinWidth,Net7_Subnet3_DR_GIL_HorMinSpacing,Net7_Subnet3_DR_GIL_VerMinSpacing,Net7_Subnet3_DR_AIL2_VerMinWidth,Net7_Subnet3_DR_AIL2_VerMinSpacing,Net7_Subnet3_DR_VerAIL2_HorMinSpacing,Net7_Subnet3_DR_MINT1AB_HorMinWidth,Net7_Subnet3_DR_MINT1_SameMask_VerMinSpacing,Net7_Subnet3_DR_MINT1_SameMask_HorMinSpacing,Net7_Subnet3_DR_MINT1_DiffMask_VerMinSpacing,Net7_Subnet3_DR_MINT1_DiffMask_HorMinSpacing,Net7_Subnet3_DR_M1AB_MinWidth,Net7_Subnet3_DR_HorM1_DiffMask_HorMinSpacing,Net7_Subnet3_DR_HorM1_SameMask_HorMinSpacing,Net7_Subnet3_DR_VerM1_DiffMask_VerMinSpacing,Net7_Subnet3_DR_VerM1_SameMask_VerMinSpacing,Net7_Subnet3_DR_HorM1_DiffMask_VerMinSpacing,Net7_Subnet3_DR_HorM1_SameMask_VerMinSpacing,Net7_Subnet3_DR_VerM1_DiffMask_HorMinSpacing,Net7_Subnet3_DR_VerM1_SameMask_HorMinSpacing,Net7_Subnet3_DR_V0_HorMinSpacing,Net7_Subnet3_DR_V1_HorMinSpacing,Net7_Subnet3_DR_V0_VerMinSpacing,Net7_Subnet3_DR_V1_VerMinSpacing,)
### Routability Constraints
Net7_Subnet3_R1 = And(
	RConstraints.R1(Edge_Net_Subnet7,[40,0,0,0, 40,1,0,0, 40,2,0,0, 40,3,0,0, 40,4,0,0, 40,5,0,0, 40,6,0,0, 40,7,0,0, 40,8,0,0, 40,9,0,0, 40,10,0,0, 40,11,0,0, 40,12,0,0, 40,13,0,0, 40,14,0,0, 40,15,0,0, 40,16,0,0, 40,17,0,0, 40,18,0,0, 40,19,0,0, 40,20,0,0, 40,21,0,0, 40,22,0,0, 40,23,0,0, 40,24,0,0, 40,25,0,0, 40,26,0,0, 40,27,0,0, 40,28,0,0, 40,29,0,0, 40,30,0,0, 40,31,0,0, 40,32,0,0, 40,33,0,0, 40,34,0,0, 40,35,0,0, ],36,20,0,1,44,35,3,3),
	RConstraints.R1(Edge_Net_Subnet7,[24,0,0,0, 24,1,0,0, 24,2,0,0, 24,3,0,0, 24,4,0,0, 24,5,0,0, 24,6,0,0, 24,7,0,0, 24,8,0,0, 24,9,0,0, 24,10,0,0, 24,11,0,0, 24,12,0,0, 24,13,0,0, 24,14,0,0, 24,15,0,0, 24,16,0,0, 24,17,0,0, 24,18,0,0, 24,19,0,0, 24,20,0,0, 24,21,0,0, 24,22,0,0, 24,23,0,0, 24,24,0,0, 24,25,0,0, 24,26,0,0, 24,27,0,0, 24,28,0,0, 24,29,0,0, 24,30,0,0, 24,31,0,0, 24,32,0,0, 24,33,0,0, 24,34,0,0, 24,35,0,0, ],36,20,0,1,44,35,3,3),
	).to_cnf()
Net7_Subnet3_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet7,Edge,Edge_Net,[40,0,0, 40,1,0, 40,2,0, 40,3,0, 40,4,0, 40,5,0, 40,6,0, 40,7,0, 40,8,0, 40,9,0, 40,10,0, 40,11,0, 40,12,0, 40,13,0, 40,14,0, 40,15,0, 40,16,0, 40,17,0, 40,18,0, 40,19,0, 40,20,0, 40,21,0, 40,22,0, 40,23,0, 40,24,0, 40,25,0, 40,26,0, 40,27,0, 40,28,0, 40,29,0, 40,30,0, 40,31,0, 40,32,0, 40,33,0, 40,34,0, 40,35,0, 24,0,0, 24,1,0, 24,2,0, 24,3,0, 24,4,0, 24,5,0, 24,6,0, 24,7,0, 24,8,0, 24,9,0, 24,10,0, 24,11,0, 24,12,0, 24,13,0, 24,14,0, 24,15,0, 24,16,0, 24,17,0, 24,18,0, 24,19,0, 24,20,0, 24,21,0, 24,22,0, 24,23,0, 24,24,0, 24,25,0, 24,26,0, 24,27,0, 24,28,0, 24,29,0, 24,30,0, 24,31,0, 24,32,0, 24,33,0, 24,34,0, 24,35,0, ],72,20,0,0,44,35,3,3,6),
	)
Net7_Subnet3_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,6],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,5+1)])for x in range(20,44+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,6],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(7,12+1)])for x in range(20,44+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net7_Subnet3_R = And(Net7_Subnet3_R1,Net7_Subnet3_R2,Net7_Subnet3_R3,)
Net7_Subnet3_Formula = And(Net7_Subnet3_C,Net7_Subnet3_DR,Net7_Subnet3_R)
# Net = 7 Subnet = 4 | Left -> Right [36,62] Top -> Bottom [0,35]
# Range R1(40,40,0,35)
# Range R2(58,58,1,10)
### Disable edges outside window
Edge_Net_Subnet7[0:36,0:35+1,0:3+1,0:2+1,0:2+1,4]=exprzeros(46656)
Edge_Net_Subnet7[62:77+1,0:35+1,0:3+1,0:2+1,0:2+1,4]=exprzeros(20736)

### Consistency Constraints
Net7_Subnet4_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,6]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(36,62+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net7_Subnet4_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet7[x,y,z,trend,mask,4]), Edge_Net[x,y,z,trend,mask,6])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(36,62+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net7_Subnet4_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,2,trend,0,4],Xor(Edge_Net_Subnet7[x,y,2,trend,1,4],Edge_Net_Subnet7[x,y,2,trend,2,4])),And(~Edge_Net_Subnet7[x,y,2,trend,0,4],~Edge_Net_Subnet7[x,y,2,trend,1,4],~Edge_Net_Subnet7[x,y,2,trend,2,4]))for x in range(36,62+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net7_Subnet4_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,3,1,0,4],Xor(Edge_Net_Subnet7[x,y,3,1,1,4],Edge_Net_Subnet7[x,y,3,1,2,4])),And(~Edge_Net_Subnet7[x,y,3,1,0,4],~Edge_Net_Subnet7[x,y,3,1,1,4],~Edge_Net_Subnet7[x,y,3,1,2,4]))for x in range(36,62+1)])for y in range(0,35+1)]).to_cnf()
Net7_Subnet4_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet7[x,y,1,trend,2,4],Xor(Edge_Net_Subnet7[x,y,1,trend,0,4],Edge_Net_Subnet7[x,y,1,trend,1,4])),And(~Edge_Net_Subnet7[x,y,1,trend,2,4],~Edge_Net_Subnet7[x,y,1,trend,0,4],~Edge_Net_Subnet7[x,y,1,trend,1,4]))for x in range(36,62+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net7_Subnet4_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,1,4], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,2,s2])for s2 in range(0,4)]))for trend in range(0,1+1)])for x in range(36,62+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,z,trend,2,4], And(*[And(~Edge_Net_Subnet7[x,y,z,trend,1,s2])for s2 in range(0,4)]))for trend in range(0,1+1)])for x in range(36,62+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net7_Subnet4_C = And(Net7_Subnet4_C1, Net7_Subnet4_C2,Net7_Subnet4_C3_ME1_Mask,Net7_Subnet4_C4_MINT1_Mask,Net7_Subnet4_C5_AIL2GIL_Mask,Net7_Subnet4_C6,)
### Design Rules
Net7_Subnet4_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(36,62+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net7_Subnet4_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,1,1,1,4], ~Edge_Net_Subnet7[x-1,y,1,1,1,4]), And(Edge_Net_Subnet7[x+1,y,1,1,1,4], Edge_Net_Subnet7[x+2,y,1,1,1,4], Edge_Net_Subnet7[x+3,y,1,1,1,4], ))for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,1,1,1,4], ~Edge_Net_Subnet7[x+1,y,1,1,1,4]), And(Edge_Net_Subnet7[x-1,y,1,1,1,4], Edge_Net_Subnet7[x-2,y,1,1,1,4], Edge_Net_Subnet7[x-3,y,1,1,1,4], ))for x in range(36,62+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet4_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,1,1,4], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,1,1,4], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(36,62+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet4_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,1,1,4], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(36,62+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,1,1,4], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(36,62+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet4_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,4]), And(Edge_Net_Subnet7[x,y+1,1,0,0,4], Edge_Net_Subnet7[x,y+2,1,0,0,4], Edge_Net_Subnet7[x,y+3,1,0,0,4], ))for x in range(36,62+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,4]), And(Edge_Net_Subnet7[x,y-1,1,0,0,4], Edge_Net_Subnet7[x,y-2,1,0,0,4], Edge_Net_Subnet7[x,y-3,1,0,0,4], ))for x in range(36,62+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,4], ~Edge_Net_Subnet7[x,y-1,1,0,0,4]), And(Edge_Net_Subnet7[x,y+1,1,0,0,4], Edge_Net_Subnet7[x,y+2,1,0,0,4], Edge_Net_Subnet7[x,y+3,1,0,0,4], ))for x in range(36,62+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,4], ~Edge_Net_Subnet7[x,y+1,1,0,0,4]), And(Edge_Net_Subnet7[x,y-1,1,0,0,4], Edge_Net_Subnet7[x,y-2,1,0,0,4], Edge_Net_Subnet7[x,y-3,1,0,0,4], ))for x in range(36,62+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net7_Subnet4_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(36,62+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(36,62+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(36,62+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(36,62+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,4], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(36,62+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,1,0,0,4], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(36,62+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net7_Subnet4_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,0,0,4], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,0,0,4], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(36,62+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet4_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,3,1,mask,4], ~Edge_Net_Subnet7[x-1,y,3,1,mask,4]), And(Edge_Net_Subnet7[x+1,y,3,1,mask,4], Edge_Net_Subnet7[x+2,y,3,1,mask,4], Edge_Net_Subnet7[x+3,y,3,1,mask,4], Edge_Net_Subnet7[x+4,y,3,1,mask,4], Edge_Net_Subnet7[x+5,y,3,1,mask,4], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,3,1,mask,4], ~Edge_Net_Subnet7[x+1,y,3,1,mask,4]), And(Edge_Net_Subnet7[x-1,y,3,1,mask,4], Edge_Net_Subnet7[x-2,y,3,1,mask,4], Edge_Net_Subnet7[x-3,y,3,1,mask,4], Edge_Net_Subnet7[x-4,y,3,1,mask,4], Edge_Net_Subnet7[x-5,y,3,1,mask,4], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet4_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,mask,4], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,mask,4], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet4_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,mask,4], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,mask,4], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet4_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,1,4], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(36,62+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,3,1,1,4], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(36,62+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet4_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,1,4], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,3,1,1,4], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(36,62+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet4_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,2,1,mask,4], ~Edge_Net_Subnet7[x-1,y,2,1,mask,4]), And(Edge_Net_Subnet7[x+1,y,2,1,mask,4], Edge_Net_Subnet7[x+2,y,2,1,mask,4], Edge_Net_Subnet7[x+3,y,2,1,mask,4], Edge_Net_Subnet7[x+4,y,2,1,mask,4], Edge_Net_Subnet7[x+5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet7[x,y,2,1,mask,4], ~Edge_Net_Subnet7[x+1,y,2,1,mask,4]), And(Edge_Net_Subnet7[x-1,y,2,1,mask,4], Edge_Net_Subnet7[x-2,y,2,1,mask,4], Edge_Net_Subnet7[x-3,y,2,1,mask,4], Edge_Net_Subnet7[x-4,y,2,1,mask,4], Edge_Net_Subnet7[x-5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,4], And(Edge_Net_Subnet7[x-1,y,2,1,mask,4], Edge_Net_Subnet7[x-2,y,2,1,mask,4], Edge_Net_Subnet7[x-3,y,2,1,mask,4], Edge_Net_Subnet7[x-4,y,2,1,mask,4], Edge_Net_Subnet7[x-5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(36,36+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,4], And(Edge_Net_Subnet7[x+1,y,2,1,mask,4], Edge_Net_Subnet7[x+2,y,2,1,mask,4], Edge_Net_Subnet7[x+3,y,2,1,mask,4], Edge_Net_Subnet7[x+4,y,2,1,mask,4], Edge_Net_Subnet7[x+5,y,2,1,mask,4], ))for mask in range(1,2+1)])for x in range(62-1,36)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,4], ~Edge_Net_Subnet7[x,y-1,2,0,mask,4]), And(Edge_Net_Subnet7[x,y+1,2,0,mask,4], Edge_Net_Subnet7[x,y+2,2,0,mask,4], Edge_Net_Subnet7[x,y+3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,4], ~Edge_Net_Subnet7[x,y+1,2,0,mask,4]), And(Edge_Net_Subnet7[x,y-1,2,0,mask,4], Edge_Net_Subnet7[x,y-2,2,0,mask,4], Edge_Net_Subnet7[x,y-3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet7[x,y,2,0,mask,4], And(Edge_Net_Subnet7[x,y+1,2,0,mask,4], Edge_Net_Subnet7[x,y+2,2,0,mask,4], Edge_Net_Subnet7[x,y+3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet7[x,y,2,0,mask,4], And(Edge_Net_Subnet7[x,y-1,2,0,mask,4], Edge_Net_Subnet7[x,y-2,2,0,mask,4], Edge_Net_Subnet7[x,y-3,2,0,mask,4], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(35,35+1)]),
	).to_cnf()
Net7_Subnet4_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,1,4], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,1,4], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(36,62+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet4_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,mask,4], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,1,mask,4], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet4_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,1,4], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(36,62+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,1,4], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(36,62+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net7_Subnet4_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,4], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet7[x,y,2,0,mask,4], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net7_Subnet4_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,1,4], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(36,62+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,1,4], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(36,62+1)])for y in range(3,35+1)]),
	).to_cnf()
Net7_Subnet4_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,4], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,1,mask,4], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(4,35+1)]),
	).to_cnf()
Net7_Subnet4_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,1,4], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,1,4], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(36,62+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet4_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,mask,4], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,0,mask,4], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(36,62+1)])for y in range(0,35+1)]),
	).to_cnf()
Net7_Subnet4_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,1,2,mask,4], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,1,2,mask,4], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(36,62+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet4_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,2,2,mask,4], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(36,62+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet7[x,y,2,2,mask,4], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(36,62+1)])for y in range(0,35+1)])
	).to_cnf()
Net7_Subnet4_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,2,mask,4], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(36,62+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,1,2,mask,4], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(36,62+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet4_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,2,mask,4], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(36,62+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet7[x,y,2,2,mask,4], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(36,62+1)])for y in range(2,35+1)]),
	).to_cnf()
Net7_Subnet4_DR = And(Net7_Subnet4_DR_Trend, Net7_Subnet4_DR_GIL_HorMinWidth,Net7_Subnet4_DR_GIL_HorMinSpacing,Net7_Subnet4_DR_GIL_VerMinSpacing,Net7_Subnet4_DR_AIL2_VerMinWidth,Net7_Subnet4_DR_AIL2_VerMinSpacing,Net7_Subnet4_DR_VerAIL2_HorMinSpacing,Net7_Subnet4_DR_MINT1AB_HorMinWidth,Net7_Subnet4_DR_MINT1_SameMask_VerMinSpacing,Net7_Subnet4_DR_MINT1_SameMask_HorMinSpacing,Net7_Subnet4_DR_MINT1_DiffMask_VerMinSpacing,Net7_Subnet4_DR_MINT1_DiffMask_HorMinSpacing,Net7_Subnet4_DR_M1AB_MinWidth,Net7_Subnet4_DR_HorM1_DiffMask_HorMinSpacing,Net7_Subnet4_DR_HorM1_SameMask_HorMinSpacing,Net7_Subnet4_DR_VerM1_DiffMask_VerMinSpacing,Net7_Subnet4_DR_VerM1_SameMask_VerMinSpacing,Net7_Subnet4_DR_HorM1_DiffMask_VerMinSpacing,Net7_Subnet4_DR_HorM1_SameMask_VerMinSpacing,Net7_Subnet4_DR_VerM1_DiffMask_HorMinSpacing,Net7_Subnet4_DR_VerM1_SameMask_HorMinSpacing,Net7_Subnet4_DR_V0_HorMinSpacing,Net7_Subnet4_DR_V1_HorMinSpacing,Net7_Subnet4_DR_V0_VerMinSpacing,Net7_Subnet4_DR_V1_VerMinSpacing,)
### Routability Constraints
Net7_Subnet4_R1 = And(
	RConstraints.R1(Edge_Net_Subnet7,[40,0,0,0, 40,1,0,0, 40,2,0,0, 40,3,0,0, 40,4,0,0, 40,5,0,0, 40,6,0,0, 40,7,0,0, 40,8,0,0, 40,9,0,0, 40,10,0,0, 40,11,0,0, 40,12,0,0, 40,13,0,0, 40,14,0,0, 40,15,0,0, 40,16,0,0, 40,17,0,0, 40,18,0,0, 40,19,0,0, 40,20,0,0, 40,21,0,0, 40,22,0,0, 40,23,0,0, 40,24,0,0, 40,25,0,0, 40,26,0,0, 40,27,0,0, 40,28,0,0, 40,29,0,0, 40,30,0,0, 40,31,0,0, 40,32,0,0, 40,33,0,0, 40,34,0,0, 40,35,0,0, ],36,36,0,1,62,35,3,4),
	RConstraints.R1(Edge_Net_Subnet7,[58,1,0,0, 58,2,0,0, 58,3,0,0, 58,4,0,0, 58,5,0,0, 58,6,0,0, 58,7,0,0, 58,8,0,0, 58,9,0,0, 58,10,0,0, ],10,36,0,1,62,35,3,4),
	).to_cnf()
Net7_Subnet4_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet7,Edge,Edge_Net,[40,0,0, 40,1,0, 40,2,0, 40,3,0, 40,4,0, 40,5,0, 40,6,0, 40,7,0, 40,8,0, 40,9,0, 40,10,0, 40,11,0, 40,12,0, 40,13,0, 40,14,0, 40,15,0, 40,16,0, 40,17,0, 40,18,0, 40,19,0, 40,20,0, 40,21,0, 40,22,0, 40,23,0, 40,24,0, 40,25,0, 40,26,0, 40,27,0, 40,28,0, 40,29,0, 40,30,0, 40,31,0, 40,32,0, 40,33,0, 40,34,0, 40,35,0, 58,1,0, 58,2,0, 58,3,0, 58,4,0, 58,5,0, 58,6,0, 58,7,0, 58,8,0, 58,9,0, 58,10,0, 58,11,0, ],47,36,0,0,62,35,3,4,6),
	)
Net7_Subnet4_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,6],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,5+1)])for x in range(36,62+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,6],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(7,12+1)])for x in range(36,62+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net7_Subnet4_R = And(Net7_Subnet4_R1,Net7_Subnet4_R2,Net7_Subnet4_R3,)
Net7_Subnet4_Formula = And(Net7_Subnet4_C,Net7_Subnet4_DR,Net7_Subnet4_R)
FORMULA = And(Net9_Subnet0_Formula, Net11_Subnet0_Formula, Net12_Subnet0_Formula, Net1_Subnet0_Formula, Net3_Subnet0_Formula, Net3_Subnet2_Formula, Net2_Subnet0_Formula, Net2_Subnet1_Formula, Net2_Subnet3_Formula, Net4_Subnet0_Formula, Net4_Subnet1_Formula, Net4_Subnet2_Formula, Net5_Subnet1_Formula, Net5_Subnet2_Formula, Net6_Subnet0_Formula, Net6_Subnet1_Formula, Net6_Subnet2_Formula, Net6_Subnet3_Formula, Net6_Subnet4_Formula, Net6_Subnet6_Formula, Net8_Subnet0_Formula, Net8_Subnet1_Formula, Net7_Subnet0_Formula, Net7_Subnet1_Formula, Net7_Subnet2_Formula, Net7_Subnet3_Formula, Net7_Subnet4_Formula, )
endTime = time.time()
print('Total Time = ', endTime-startTime)
setOut.clauseDistribution(FORMULA)
setOut.setUpLayoutViaFromResult(FORMULA.satisfy_one(),outLayout,subnetRec,13)
print('#edge = 29645')