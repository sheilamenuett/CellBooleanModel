from pyeda.inter import *
import RConstraints
import time
import setOut
startTime = time.time()
# ===> Instruction(Create)  2D Routing Style p(e) <===
# ===> Edges[X, Y, Z, Trends, Masks]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge = exprvars('edge', 42, 36, 4, 3, 3)

# ===> Instruction(Create)  2D Routing Style p(e,n) <===
# ===> Edge_Net[X, Y, Z, Trends, Masks, Nets]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge_Net = exprvars('edge_net', 42, 36, 4, 3, 3, 3)

# ===> Instruction(Create)  2D Routing Style p(e,n,s) <===
# ===> Edge_Net_Subnet_NetID[X, Y, Z, Trends, Masks, Subnets]
# Trends Index => 0: Vertical | 1: Horizontal | 2: Orthogonal
Edge_Net_Subnet1 = exprvars('edge_net_subnet1', 42, 36, 4, 3, 3, 3)
Edge_Net_Subnet2 = exprvars('edge_net_subnet2', 42, 36, 4, 3, 3, 10)
Edge_Net_Subnet3 = exprvars('edge_net_subnet3', 42, 36, 4, 3, 3, 3)

outLayout=[[[[0 for trend in range(3)] for z in range(4)] for y in range(36)] for x in range(42)]

subnetRec=[[[[0 for trend in range(3)] for z in range(4)] for y in range(36)] for x in range(42)]

MaxX = 41
MaxY = 35
MaxZ = 3
#Net = 3
#cellName = CLKBUF_X4_DFINH_combined
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
Edge_Net[0,0,0,0,0,0:] = exprzeros(3)
Edge_Net[0,1,0,0,0,0:] = exprzeros(3)
Edge_Net[0,2,0,0,0,0:] = exprzeros(3)
Edge_Net[0,3,0,0,0,0:] = exprzeros(3)
Edge_Net[0,4,0,0,0,0:] = exprzeros(3)
Edge_Net[0,5,0,0,0,0:] = exprzeros(3)
Edge_Net[0,6,0,0,0,0:] = exprzeros(3)
Edge_Net[0,7,0,0,0,0:] = exprzeros(3)
Edge_Net[0,8,0,0,0,0:] = exprzeros(3)
Edge_Net[0,9,0,0,0,0:] = exprzeros(3)
Edge_Net[0,10,0,0,0,0:] = exprzeros(3)
Edge_Net[0,11,0,0,0,0:] = exprzeros(3)
Edge_Net[0,12,0,0,0,0:] = exprzeros(3)
Edge_Net[0,13,0,0,0,0:] = exprzeros(3)
Edge_Net[0,14,0,0,0,0:] = exprzeros(3)
Edge_Net[0,15,0,0,0,0:] = exprzeros(3)
Edge_Net[0,16,0,0,0,0:] = exprzeros(3)
Edge_Net[0,17,0,0,0,0:] = exprzeros(3)
Edge_Net[0,18,0,0,0,0:] = exprzeros(3)
Edge_Net[0,19,0,0,0,0:] = exprzeros(3)
Edge_Net[0,20,0,0,0,0:] = exprzeros(3)
Edge_Net[0,21,0,0,0,0:] = exprzeros(3)
Edge_Net[0,22,0,0,0,0:] = exprzeros(3)
Edge_Net[0,23,0,0,0,0:] = exprzeros(3)
Edge_Net[0,24,0,0,0,0:] = exprzeros(3)
Edge_Net[0,25,0,0,0,0:] = exprzeros(3)
Edge_Net[0,26,0,0,0,0:] = exprzeros(3)
Edge_Net[0,27,0,0,0,0:] = exprzeros(3)
Edge_Net[0,28,0,0,0,0:] = exprzeros(3)
Edge_Net[0,29,0,0,0,0:] = exprzeros(3)
Edge_Net[0,30,0,0,0,0:] = exprzeros(3)
Edge_Net[0,31,0,0,0,0:] = exprzeros(3)
Edge_Net[0,32,0,0,0,0:] = exprzeros(3)
Edge_Net[0,33,0,0,0,0:] = exprzeros(3)
Edge_Net[0,34,0,0,0,0:] = exprzeros(3)
Edge_Net[0,35,0,0,0,0:] = exprzeros(3)
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
Edge_Net[4,0,0,0,0,0:] = exprzeros(3)
Edge_Net[4,1,0,0,0,0:] = exprzeros(3)
Edge_Net[4,2,0,0,0,0:] = exprzeros(3)
Edge_Net[4,3,0,0,0,0:] = exprzeros(3)
Edge_Net[4,4,0,0,0,0:] = exprzeros(3)
Edge_Net[4,5,0,0,0,0:] = exprzeros(3)
Edge_Net[4,6,0,0,0,0:] = exprzeros(3)
Edge_Net[4,7,0,0,0,0:] = exprzeros(3)
Edge_Net[4,8,0,0,0,0:] = exprzeros(3)
Edge_Net[4,9,0,0,0,0:] = exprzeros(3)
Edge_Net[4,10,0,0,0,0:] = exprzeros(3)
Edge_Net[4,11,0,0,0,0:] = exprzeros(3)
Edge_Net[4,12,0,0,0,0:] = exprzeros(3)
Edge_Net[4,13,0,0,0,0:] = exprzeros(3)
Edge_Net[4,14,0,0,0,0:] = exprzeros(3)
Edge_Net[4,15,0,0,0,0:] = exprzeros(3)
Edge_Net[4,16,0,0,0,0:] = exprzeros(3)
Edge_Net[4,17,0,0,0,0:] = exprzeros(3)
Edge_Net[4,18,0,0,0,0:] = exprzeros(3)
Edge_Net[4,19,0,0,0,0:] = exprzeros(3)
Edge_Net[4,20,0,0,0,0:] = exprzeros(3)
Edge_Net[4,21,0,0,0,0:] = exprzeros(3)
Edge_Net[4,22,0,0,0,0:] = exprzeros(3)
Edge_Net[4,23,0,0,0,0:] = exprzeros(3)
Edge_Net[4,24,0,0,0,0:] = exprzeros(3)
Edge_Net[4,25,0,0,0,0:] = exprzeros(3)
Edge_Net[4,26,0,0,0,0:] = exprzeros(3)
Edge_Net[4,27,0,0,0,0:] = exprzeros(3)
Edge_Net[4,28,0,0,0,0:] = exprzeros(3)
Edge_Net[4,29,0,0,0,0:] = exprzeros(3)
Edge_Net[4,30,0,0,0,0:] = exprzeros(3)
Edge_Net[4,31,0,0,0,0:] = exprzeros(3)
Edge_Net[4,32,0,0,0,0:] = exprzeros(3)
Edge_Net[4,33,0,0,0,0:] = exprzeros(3)
Edge_Net[4,34,0,0,0,0:] = exprzeros(3)
Edge_Net[4,35,0,0,0,0:] = exprzeros(3)
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
Edge_Net[8,0,0,0,0,0:] = exprzeros(3)
Edge_Net[8,1,0,0,0,0:] = exprzeros(3)
Edge_Net[8,2,0,0,0,0:] = exprzeros(3)
Edge_Net[8,3,0,0,0,0:] = exprzeros(3)
Edge_Net[8,4,0,0,0,0:] = exprzeros(3)
Edge_Net[8,5,0,0,0,0:] = exprzeros(3)
Edge_Net[8,6,0,0,0,0:] = exprzeros(3)
Edge_Net[8,7,0,0,0,0:] = exprzeros(3)
Edge_Net[8,8,0,0,0,0:] = exprzeros(3)
Edge_Net[8,9,0,0,0,0:] = exprzeros(3)
Edge_Net[8,10,0,0,0,0:] = exprzeros(3)
Edge_Net[8,11,0,0,0,0:] = exprzeros(3)
Edge_Net[8,12,0,0,0,0:] = exprzeros(3)
Edge_Net[8,13,0,0,0,0:] = exprzeros(3)
Edge_Net[8,14,0,0,0,0:] = exprzeros(3)
Edge_Net[8,15,0,0,0,0:] = exprzeros(3)
Edge_Net[8,16,0,0,0,0:] = exprzeros(3)
Edge_Net[8,17,0,0,0,0:] = exprzeros(3)
Edge_Net[8,18,0,0,0,0:] = exprzeros(3)
Edge_Net[8,19,0,0,0,0:] = exprzeros(3)
Edge_Net[8,20,0,0,0,0:] = exprzeros(3)
Edge_Net[8,21,0,0,0,0:] = exprzeros(3)
Edge_Net[8,22,0,0,0,0:] = exprzeros(3)
Edge_Net[8,23,0,0,0,0:] = exprzeros(3)
Edge_Net[8,24,0,0,0,0:] = exprzeros(3)
Edge_Net[8,25,0,0,0,0:] = exprzeros(3)
Edge_Net[8,26,0,0,0,0:] = exprzeros(3)
Edge_Net[8,27,0,0,0,0:] = exprzeros(3)
Edge_Net[8,28,0,0,0,0:] = exprzeros(3)
Edge_Net[8,29,0,0,0,0:] = exprzeros(3)
Edge_Net[8,30,0,0,0,0:] = exprzeros(3)
Edge_Net[8,31,0,0,0,0:] = exprzeros(3)
Edge_Net[8,32,0,0,0,0:] = exprzeros(3)
Edge_Net[8,33,0,0,0,0:] = exprzeros(3)
Edge_Net[8,34,0,0,0,0:] = exprzeros(3)
Edge_Net[8,35,0,0,0,0:] = exprzeros(3)
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
Edge_Net[12,0,0,0,0,0:] = exprzeros(3)
Edge_Net[12,1,0,0,0,0:] = exprzeros(3)
Edge_Net[12,2,0,0,0,0:] = exprzeros(3)
Edge_Net[12,3,0,0,0,0:] = exprzeros(3)
Edge_Net[12,4,0,0,0,0:] = exprzeros(3)
Edge_Net[12,5,0,0,0,0:] = exprzeros(3)
Edge_Net[12,6,0,0,0,0:] = exprzeros(3)
Edge_Net[12,7,0,0,0,0:] = exprzeros(3)
Edge_Net[12,8,0,0,0,0:] = exprzeros(3)
Edge_Net[12,9,0,0,0,0:] = exprzeros(3)
Edge_Net[12,10,0,0,0,0:] = exprzeros(3)
Edge_Net[12,11,0,0,0,0:] = exprzeros(3)
Edge_Net[12,12,0,0,0,0:] = exprzeros(3)
Edge_Net[12,13,0,0,0,0:] = exprzeros(3)
Edge_Net[12,14,0,0,0,0:] = exprzeros(3)
Edge_Net[12,15,0,0,0,0:] = exprzeros(3)
Edge_Net[12,16,0,0,0,0:] = exprzeros(3)
Edge_Net[12,17,0,0,0,0:] = exprzeros(3)
Edge_Net[12,18,0,0,0,0:] = exprzeros(3)
Edge_Net[12,19,0,0,0,0:] = exprzeros(3)
Edge_Net[12,20,0,0,0,0:] = exprzeros(3)
Edge_Net[12,21,0,0,0,0:] = exprzeros(3)
Edge_Net[12,22,0,0,0,0:] = exprzeros(3)
Edge_Net[12,23,0,0,0,0:] = exprzeros(3)
Edge_Net[12,24,0,0,0,0:] = exprzeros(3)
Edge_Net[12,25,0,0,0,0:] = exprzeros(3)
Edge_Net[12,26,0,0,0,0:] = exprzeros(3)
Edge_Net[12,27,0,0,0,0:] = exprzeros(3)
Edge_Net[12,28,0,0,0,0:] = exprzeros(3)
Edge_Net[12,29,0,0,0,0:] = exprzeros(3)
Edge_Net[12,30,0,0,0,0:] = exprzeros(3)
Edge_Net[12,31,0,0,0,0:] = exprzeros(3)
Edge_Net[12,32,0,0,0,0:] = exprzeros(3)
Edge_Net[12,33,0,0,0,0:] = exprzeros(3)
Edge_Net[12,34,0,0,0,0:] = exprzeros(3)
Edge_Net[12,35,0,0,0,0:] = exprzeros(3)
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
Edge_Net[16,0,0,0,0,0:] = exprzeros(3)
Edge_Net[16,1,0,0,0,0:] = exprzeros(3)
Edge_Net[16,2,0,0,0,0:] = exprzeros(3)
Edge_Net[16,3,0,0,0,0:] = exprzeros(3)
Edge_Net[16,4,0,0,0,0:] = exprzeros(3)
Edge_Net[16,5,0,0,0,0:] = exprzeros(3)
Edge_Net[16,6,0,0,0,0:] = exprzeros(3)
Edge_Net[16,7,0,0,0,0:] = exprzeros(3)
Edge_Net[16,8,0,0,0,0:] = exprzeros(3)
Edge_Net[16,9,0,0,0,0:] = exprzeros(3)
Edge_Net[16,10,0,0,0,0:] = exprzeros(3)
Edge_Net[16,11,0,0,0,0:] = exprzeros(3)
Edge_Net[16,12,0,0,0,0:] = exprzeros(3)
Edge_Net[16,13,0,0,0,0:] = exprzeros(3)
Edge_Net[16,14,0,0,0,0:] = exprzeros(3)
Edge_Net[16,15,0,0,0,0:] = exprzeros(3)
Edge_Net[16,16,0,0,0,0:] = exprzeros(3)
Edge_Net[16,17,0,0,0,0:] = exprzeros(3)
Edge_Net[16,18,0,0,0,0:] = exprzeros(3)
Edge_Net[16,19,0,0,0,0:] = exprzeros(3)
Edge_Net[16,20,0,0,0,0:] = exprzeros(3)
Edge_Net[16,21,0,0,0,0:] = exprzeros(3)
Edge_Net[16,22,0,0,0,0:] = exprzeros(3)
Edge_Net[16,23,0,0,0,0:] = exprzeros(3)
Edge_Net[16,24,0,0,0,0:] = exprzeros(3)
Edge_Net[16,25,0,0,0,0:] = exprzeros(3)
Edge_Net[16,26,0,0,0,0:] = exprzeros(3)
Edge_Net[16,27,0,0,0,0:] = exprzeros(3)
Edge_Net[16,28,0,0,0,0:] = exprzeros(3)
Edge_Net[16,29,0,0,0,0:] = exprzeros(3)
Edge_Net[16,30,0,0,0,0:] = exprzeros(3)
Edge_Net[16,31,0,0,0,0:] = exprzeros(3)
Edge_Net[16,32,0,0,0,0:] = exprzeros(3)
Edge_Net[16,33,0,0,0,0:] = exprzeros(3)
Edge_Net[16,34,0,0,0,0:] = exprzeros(3)
Edge_Net[16,35,0,0,0,0:] = exprzeros(3)
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
Edge_Net[20,0,0,0,0,0:] = exprzeros(3)
Edge_Net[20,1,0,0,0,0:] = exprzeros(3)
Edge_Net[20,2,0,0,0,0:] = exprzeros(3)
Edge_Net[20,3,0,0,0,0:] = exprzeros(3)
Edge_Net[20,4,0,0,0,0:] = exprzeros(3)
Edge_Net[20,5,0,0,0,0:] = exprzeros(3)
Edge_Net[20,6,0,0,0,0:] = exprzeros(3)
Edge_Net[20,7,0,0,0,0:] = exprzeros(3)
Edge_Net[20,8,0,0,0,0:] = exprzeros(3)
Edge_Net[20,9,0,0,0,0:] = exprzeros(3)
Edge_Net[20,10,0,0,0,0:] = exprzeros(3)
Edge_Net[20,11,0,0,0,0:] = exprzeros(3)
Edge_Net[20,12,0,0,0,0:] = exprzeros(3)
Edge_Net[20,13,0,0,0,0:] = exprzeros(3)
Edge_Net[20,14,0,0,0,0:] = exprzeros(3)
Edge_Net[20,15,0,0,0,0:] = exprzeros(3)
Edge_Net[20,16,0,0,0,0:] = exprzeros(3)
Edge_Net[20,17,0,0,0,0:] = exprzeros(3)
Edge_Net[20,18,0,0,0,0:] = exprzeros(3)
Edge_Net[20,19,0,0,0,0:] = exprzeros(3)
Edge_Net[20,20,0,0,0,0:] = exprzeros(3)
Edge_Net[20,21,0,0,0,0:] = exprzeros(3)
Edge_Net[20,22,0,0,0,0:] = exprzeros(3)
Edge_Net[20,23,0,0,0,0:] = exprzeros(3)
Edge_Net[20,24,0,0,0,0:] = exprzeros(3)
Edge_Net[20,25,0,0,0,0:] = exprzeros(3)
Edge_Net[20,26,0,0,0,0:] = exprzeros(3)
Edge_Net[20,27,0,0,0,0:] = exprzeros(3)
Edge_Net[20,28,0,0,0,0:] = exprzeros(3)
Edge_Net[20,29,0,0,0,0:] = exprzeros(3)
Edge_Net[20,30,0,0,0,0:] = exprzeros(3)
Edge_Net[20,31,0,0,0,0:] = exprzeros(3)
Edge_Net[20,32,0,0,0,0:] = exprzeros(3)
Edge_Net[20,33,0,0,0,0:] = exprzeros(3)
Edge_Net[20,34,0,0,0,0:] = exprzeros(3)
Edge_Net[20,35,0,0,0,0:] = exprzeros(3)
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
Edge_Net[24,0,0,0,0,0:] = exprzeros(3)
Edge_Net[24,1,0,0,0,0:] = exprzeros(3)
Edge_Net[24,2,0,0,0,0:] = exprzeros(3)
Edge_Net[24,3,0,0,0,0:] = exprzeros(3)
Edge_Net[24,4,0,0,0,0:] = exprzeros(3)
Edge_Net[24,5,0,0,0,0:] = exprzeros(3)
Edge_Net[24,6,0,0,0,0:] = exprzeros(3)
Edge_Net[24,7,0,0,0,0:] = exprzeros(3)
Edge_Net[24,8,0,0,0,0:] = exprzeros(3)
Edge_Net[24,9,0,0,0,0:] = exprzeros(3)
Edge_Net[24,10,0,0,0,0:] = exprzeros(3)
Edge_Net[24,11,0,0,0,0:] = exprzeros(3)
Edge_Net[24,12,0,0,0,0:] = exprzeros(3)
Edge_Net[24,13,0,0,0,0:] = exprzeros(3)
Edge_Net[24,14,0,0,0,0:] = exprzeros(3)
Edge_Net[24,15,0,0,0,0:] = exprzeros(3)
Edge_Net[24,16,0,0,0,0:] = exprzeros(3)
Edge_Net[24,17,0,0,0,0:] = exprzeros(3)
Edge_Net[24,18,0,0,0,0:] = exprzeros(3)
Edge_Net[24,19,0,0,0,0:] = exprzeros(3)
Edge_Net[24,20,0,0,0,0:] = exprzeros(3)
Edge_Net[24,21,0,0,0,0:] = exprzeros(3)
Edge_Net[24,22,0,0,0,0:] = exprzeros(3)
Edge_Net[24,23,0,0,0,0:] = exprzeros(3)
Edge_Net[24,24,0,0,0,0:] = exprzeros(3)
Edge_Net[24,25,0,0,0,0:] = exprzeros(3)
Edge_Net[24,26,0,0,0,0:] = exprzeros(3)
Edge_Net[24,27,0,0,0,0:] = exprzeros(3)
Edge_Net[24,28,0,0,0,0:] = exprzeros(3)
Edge_Net[24,29,0,0,0,0:] = exprzeros(3)
Edge_Net[24,30,0,0,0,0:] = exprzeros(3)
Edge_Net[24,31,0,0,0,0:] = exprzeros(3)
Edge_Net[24,32,0,0,0,0:] = exprzeros(3)
Edge_Net[24,33,0,0,0,0:] = exprzeros(3)
Edge_Net[24,34,0,0,0,0:] = exprzeros(3)
Edge_Net[24,35,0,0,0,0:] = exprzeros(3)
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
Edge_Net[28,0,0,0,0,0:] = exprzeros(3)
Edge_Net[28,1,0,0,0,0:] = exprzeros(3)
Edge_Net[28,2,0,0,0,0:] = exprzeros(3)
Edge_Net[28,3,0,0,0,0:] = exprzeros(3)
Edge_Net[28,4,0,0,0,0:] = exprzeros(3)
Edge_Net[28,5,0,0,0,0:] = exprzeros(3)
Edge_Net[28,6,0,0,0,0:] = exprzeros(3)
Edge_Net[28,7,0,0,0,0:] = exprzeros(3)
Edge_Net[28,8,0,0,0,0:] = exprzeros(3)
Edge_Net[28,9,0,0,0,0:] = exprzeros(3)
Edge_Net[28,10,0,0,0,0:] = exprzeros(3)
Edge_Net[28,11,0,0,0,0:] = exprzeros(3)
Edge_Net[28,12,0,0,0,0:] = exprzeros(3)
Edge_Net[28,13,0,0,0,0:] = exprzeros(3)
Edge_Net[28,14,0,0,0,0:] = exprzeros(3)
Edge_Net[28,15,0,0,0,0:] = exprzeros(3)
Edge_Net[28,16,0,0,0,0:] = exprzeros(3)
Edge_Net[28,17,0,0,0,0:] = exprzeros(3)
Edge_Net[28,18,0,0,0,0:] = exprzeros(3)
Edge_Net[28,19,0,0,0,0:] = exprzeros(3)
Edge_Net[28,20,0,0,0,0:] = exprzeros(3)
Edge_Net[28,21,0,0,0,0:] = exprzeros(3)
Edge_Net[28,22,0,0,0,0:] = exprzeros(3)
Edge_Net[28,23,0,0,0,0:] = exprzeros(3)
Edge_Net[28,24,0,0,0,0:] = exprzeros(3)
Edge_Net[28,25,0,0,0,0:] = exprzeros(3)
Edge_Net[28,26,0,0,0,0:] = exprzeros(3)
Edge_Net[28,27,0,0,0,0:] = exprzeros(3)
Edge_Net[28,28,0,0,0,0:] = exprzeros(3)
Edge_Net[28,29,0,0,0,0:] = exprzeros(3)
Edge_Net[28,30,0,0,0,0:] = exprzeros(3)
Edge_Net[28,31,0,0,0,0:] = exprzeros(3)
Edge_Net[28,32,0,0,0,0:] = exprzeros(3)
Edge_Net[28,33,0,0,0,0:] = exprzeros(3)
Edge_Net[28,34,0,0,0,0:] = exprzeros(3)
Edge_Net[28,35,0,0,0,0:] = exprzeros(3)
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
Edge_Net[32,0,0,0,0,0:] = exprzeros(3)
Edge_Net[32,1,0,0,0,0:] = exprzeros(3)
Edge_Net[32,2,0,0,0,0:] = exprzeros(3)
Edge_Net[32,3,0,0,0,0:] = exprzeros(3)
Edge_Net[32,4,0,0,0,0:] = exprzeros(3)
Edge_Net[32,5,0,0,0,0:] = exprzeros(3)
Edge_Net[32,6,0,0,0,0:] = exprzeros(3)
Edge_Net[32,7,0,0,0,0:] = exprzeros(3)
Edge_Net[32,8,0,0,0,0:] = exprzeros(3)
Edge_Net[32,9,0,0,0,0:] = exprzeros(3)
Edge_Net[32,10,0,0,0,0:] = exprzeros(3)
Edge_Net[32,11,0,0,0,0:] = exprzeros(3)
Edge_Net[32,12,0,0,0,0:] = exprzeros(3)
Edge_Net[32,13,0,0,0,0:] = exprzeros(3)
Edge_Net[32,14,0,0,0,0:] = exprzeros(3)
Edge_Net[32,15,0,0,0,0:] = exprzeros(3)
Edge_Net[32,16,0,0,0,0:] = exprzeros(3)
Edge_Net[32,17,0,0,0,0:] = exprzeros(3)
Edge_Net[32,18,0,0,0,0:] = exprzeros(3)
Edge_Net[32,19,0,0,0,0:] = exprzeros(3)
Edge_Net[32,20,0,0,0,0:] = exprzeros(3)
Edge_Net[32,21,0,0,0,0:] = exprzeros(3)
Edge_Net[32,22,0,0,0,0:] = exprzeros(3)
Edge_Net[32,23,0,0,0,0:] = exprzeros(3)
Edge_Net[32,24,0,0,0,0:] = exprzeros(3)
Edge_Net[32,25,0,0,0,0:] = exprzeros(3)
Edge_Net[32,26,0,0,0,0:] = exprzeros(3)
Edge_Net[32,27,0,0,0,0:] = exprzeros(3)
Edge_Net[32,28,0,0,0,0:] = exprzeros(3)
Edge_Net[32,29,0,0,0,0:] = exprzeros(3)
Edge_Net[32,30,0,0,0,0:] = exprzeros(3)
Edge_Net[32,31,0,0,0,0:] = exprzeros(3)
Edge_Net[32,32,0,0,0,0:] = exprzeros(3)
Edge_Net[32,33,0,0,0,0:] = exprzeros(3)
Edge_Net[32,34,0,0,0,0:] = exprzeros(3)
Edge_Net[32,35,0,0,0,0:] = exprzeros(3)

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
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[2,1,0,0,1,0:] = exprzeros(3)
Edge_Net[2,2,0,0,1,0:] = exprzeros(3)
Edge_Net[2,3,0,0,1,0:] = exprzeros(3)
Edge_Net[2,4,0,0,1,0:] = exprzeros(3)
Edge_Net[2,5,0,0,1,0:] = exprzeros(3)
Edge_Net[2,6,0,0,1,0:] = exprzeros(3)
Edge_Net[2,7,0,0,1,0:] = exprzeros(3)
Edge_Net[2,8,0,0,1,0:] = exprzeros(3)
Edge_Net[2,9,0,0,1,0:] = exprzeros(3)
Edge_Net[2,10,0,0,1,0:] = exprzeros(3)
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
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[6,1,0,0,1,0:] = exprzeros(3)
Edge_Net[6,2,0,0,1,0:] = exprzeros(3)
Edge_Net[6,3,0,0,1,0:] = exprzeros(3)
Edge_Net[6,4,0,0,1,0:] = exprzeros(3)
Edge_Net[6,5,0,0,1,0:] = exprzeros(3)
Edge_Net[6,6,0,0,1,0:] = exprzeros(3)
Edge_Net[6,7,0,0,1,0:] = exprzeros(3)
Edge_Net[6,8,0,0,1,0:] = exprzeros(3)
Edge_Net[6,9,0,0,1,0:] = exprzeros(3)
Edge_Net[6,10,0,0,1,0:] = exprzeros(3)
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
Edge_Net[10,1,0,0,1,0:] = exprzeros(3)
Edge_Net[10,2,0,0,1,0:] = exprzeros(3)
Edge_Net[10,3,0,0,1,0:] = exprzeros(3)
Edge_Net[10,4,0,0,1,0:] = exprzeros(3)
Edge_Net[10,5,0,0,1,0:] = exprzeros(3)
Edge_Net[10,6,0,0,1,0:] = exprzeros(3)
Edge_Net[10,7,0,0,1,0:] = exprzeros(3)
Edge_Net[10,8,0,0,1,0:] = exprzeros(3)
Edge_Net[10,9,0,0,1,0:] = exprzeros(3)
Edge_Net[10,10,0,0,1,0:] = exprzeros(3)
Edge_Net[10,11,0,0,1,0:] = exprzeros(3)
Edge_Net[10,12,0,0,1,0:] = exprzeros(3)
Edge_Net[10,13,0,0,1,0:] = exprzeros(3)
Edge_Net[10,14,0,0,1,0:] = exprzeros(3)
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
Edge_Net[14,1,0,0,1,0:] = exprzeros(3)
Edge_Net[14,2,0,0,1,0:] = exprzeros(3)
Edge_Net[14,3,0,0,1,0:] = exprzeros(3)
Edge_Net[14,4,0,0,1,0:] = exprzeros(3)
Edge_Net[14,5,0,0,1,0:] = exprzeros(3)
Edge_Net[14,6,0,0,1,0:] = exprzeros(3)
Edge_Net[14,7,0,0,1,0:] = exprzeros(3)
Edge_Net[14,8,0,0,1,0:] = exprzeros(3)
Edge_Net[14,9,0,0,1,0:] = exprzeros(3)
Edge_Net[14,10,0,0,1,0:] = exprzeros(3)
Edge_Net[14,11,0,0,1,0:] = exprzeros(3)
Edge_Net[14,12,0,0,1,0:] = exprzeros(3)
Edge_Net[14,13,0,0,1,0:] = exprzeros(3)
Edge_Net[14,14,0,0,1,0:] = exprzeros(3)
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
Edge_Net[14,1,0,0,1,0:] = exprzeros(3)
Edge_Net[14,2,0,0,1,0:] = exprzeros(3)
Edge_Net[14,3,0,0,1,0:] = exprzeros(3)
Edge_Net[14,4,0,0,1,0:] = exprzeros(3)
Edge_Net[14,5,0,0,1,0:] = exprzeros(3)
Edge_Net[14,6,0,0,1,0:] = exprzeros(3)
Edge_Net[14,7,0,0,1,0:] = exprzeros(3)
Edge_Net[14,8,0,0,1,0:] = exprzeros(3)
Edge_Net[14,9,0,0,1,0:] = exprzeros(3)
Edge_Net[14,10,0,0,1,0:] = exprzeros(3)
Edge_Net[14,11,0,0,1,0:] = exprzeros(3)
Edge_Net[14,12,0,0,1,0:] = exprzeros(3)
Edge_Net[14,13,0,0,1,0:] = exprzeros(3)
Edge_Net[14,14,0,0,1,0:] = exprzeros(3)
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
Edge_Net[18,1,0,0,1,0:] = exprzeros(3)
Edge_Net[18,2,0,0,1,0:] = exprzeros(3)
Edge_Net[18,3,0,0,1,0:] = exprzeros(3)
Edge_Net[18,4,0,0,1,0:] = exprzeros(3)
Edge_Net[18,5,0,0,1,0:] = exprzeros(3)
Edge_Net[18,6,0,0,1,0:] = exprzeros(3)
Edge_Net[18,7,0,0,1,0:] = exprzeros(3)
Edge_Net[18,8,0,0,1,0:] = exprzeros(3)
Edge_Net[18,9,0,0,1,0:] = exprzeros(3)
Edge_Net[18,10,0,0,1,0:] = exprzeros(3)
Edge_Net[18,11,0,0,1,0:] = exprzeros(3)
Edge_Net[18,12,0,0,1,0:] = exprzeros(3)
Edge_Net[18,13,0,0,1,0:] = exprzeros(3)
Edge_Net[18,14,0,0,1,0:] = exprzeros(3)
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
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[18,1,0,0,1,0:] = exprzeros(3)
Edge_Net[18,2,0,0,1,0:] = exprzeros(3)
Edge_Net[18,3,0,0,1,0:] = exprzeros(3)
Edge_Net[18,4,0,0,1,0:] = exprzeros(3)
Edge_Net[18,5,0,0,1,0:] = exprzeros(3)
Edge_Net[18,6,0,0,1,0:] = exprzeros(3)
Edge_Net[18,7,0,0,1,0:] = exprzeros(3)
Edge_Net[18,8,0,0,1,0:] = exprzeros(3)
Edge_Net[18,9,0,0,1,0:] = exprzeros(3)
Edge_Net[18,10,0,0,1,0:] = exprzeros(3)
Edge_Net[18,11,0,0,1,0:] = exprzeros(3)
Edge_Net[18,12,0,0,1,0:] = exprzeros(3)
Edge_Net[18,13,0,0,1,0:] = exprzeros(3)
Edge_Net[18,14,0,0,1,0:] = exprzeros(3)
#(L)End initialize EdgeNet
#(R)Initialize Edge
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
Edge[22,11,0,0,1] = expr(1)
Edge[22,12,0,0,1] = expr(1)
Edge[22,13,0,0,1] = expr(1)
Edge[22,14,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[22,1,0,0,1,0:] = exprzeros(3)
Edge_Net[22,2,0,0,1,0:] = exprzeros(3)
Edge_Net[22,3,0,0,1,0:] = exprzeros(3)
Edge_Net[22,4,0,0,1,0:] = exprzeros(3)
Edge_Net[22,5,0,0,1,0:] = exprzeros(3)
Edge_Net[22,6,0,0,1,0:] = exprzeros(3)
Edge_Net[22,7,0,0,1,0:] = exprzeros(3)
Edge_Net[22,8,0,0,1,0:] = exprzeros(3)
Edge_Net[22,9,0,0,1,0:] = exprzeros(3)
Edge_Net[22,10,0,0,1,0:] = exprzeros(3)
Edge_Net[22,11,0,0,1,0:] = exprzeros(3)
Edge_Net[22,12,0,0,1,0:] = exprzeros(3)
Edge_Net[22,13,0,0,1,0:] = exprzeros(3)
Edge_Net[22,14,0,0,1,0:] = exprzeros(3)
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
Edge[22,8,1,1,1] = expr(0)
Edge[22,9,1,1,1] = expr(0)
Edge[22,10,1,1,1] = expr(0)
Edge[22,11,1,1,1] = expr(0)
Edge[22,12,1,1,1] = expr(0)
Edge[22,13,1,1,1] = expr(0)
Edge[22,14,1,1,1] = expr(0)
Edge[22,15,1,1,1] = expr(0)
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
Edge[22,12,1,1,1] = expr(0)
Edge[22,13,1,1,1] = expr(0)
Edge[22,14,1,1,1] = expr(0)
Edge[22,15,1,1,1] = expr(0)
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
Edge[22,11,0,0,1] = expr(1)
Edge[22,12,0,0,1] = expr(1)
Edge[22,13,0,0,1] = expr(1)
Edge[22,14,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[22,1,0,0,1,0:] = exprzeros(3)
Edge_Net[22,2,0,0,1,0:] = exprzeros(3)
Edge_Net[22,3,0,0,1,0:] = exprzeros(3)
Edge_Net[22,4,0,0,1,0:] = exprzeros(3)
Edge_Net[22,5,0,0,1,0:] = exprzeros(3)
Edge_Net[22,6,0,0,1,0:] = exprzeros(3)
Edge_Net[22,7,0,0,1,0:] = exprzeros(3)
Edge_Net[22,8,0,0,1,0:] = exprzeros(3)
Edge_Net[22,9,0,0,1,0:] = exprzeros(3)
Edge_Net[22,10,0,0,1,0:] = exprzeros(3)
Edge_Net[22,11,0,0,1,0:] = exprzeros(3)
Edge_Net[22,12,0,0,1,0:] = exprzeros(3)
Edge_Net[22,13,0,0,1,0:] = exprzeros(3)
Edge_Net[22,14,0,0,1,0:] = exprzeros(3)
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
Edge[26,11,0,0,1] = expr(1)
Edge[26,12,0,0,1] = expr(1)
Edge[26,13,0,0,1] = expr(1)
Edge[26,14,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[26,1,0,0,1,0:] = exprzeros(3)
Edge_Net[26,2,0,0,1,0:] = exprzeros(3)
Edge_Net[26,3,0,0,1,0:] = exprzeros(3)
Edge_Net[26,4,0,0,1,0:] = exprzeros(3)
Edge_Net[26,5,0,0,1,0:] = exprzeros(3)
Edge_Net[26,6,0,0,1,0:] = exprzeros(3)
Edge_Net[26,7,0,0,1,0:] = exprzeros(3)
Edge_Net[26,8,0,0,1,0:] = exprzeros(3)
Edge_Net[26,9,0,0,1,0:] = exprzeros(3)
Edge_Net[26,10,0,0,1,0:] = exprzeros(3)
Edge_Net[26,11,0,0,1,0:] = exprzeros(3)
Edge_Net[26,12,0,0,1,0:] = exprzeros(3)
Edge_Net[26,13,0,0,1,0:] = exprzeros(3)
Edge_Net[26,14,0,0,1,0:] = exprzeros(3)
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
Edge[22,12,1,1,1] = expr(0)
Edge[22,13,1,1,1] = expr(0)
Edge[22,14,1,1,1] = expr(0)
Edge[22,15,1,1,1] = expr(0)
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
Edge[22,12,1,1,1] = expr(0)
Edge[22,13,1,1,1] = expr(0)
Edge[22,14,1,1,1] = expr(0)
Edge[22,15,1,1,1] = expr(0)
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
Edge[26,12,1,1,1] = expr(0)
Edge[26,13,1,1,1] = expr(0)
Edge[26,14,1,1,1] = expr(0)
Edge[26,15,1,1,1] = expr(0)
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
Edge[26,12,1,1,1] = expr(0)
Edge[26,13,1,1,1] = expr(0)
Edge[26,14,1,1,1] = expr(0)
Edge[26,15,1,1,1] = expr(0)
#(R)End disable GIL
#store in
#(L)Initialize Edge
Edge[26,1,0,0,1] = expr(1)
Edge[26,2,0,0,1] = expr(1)
Edge[26,3,0,0,1] = expr(1)
Edge[26,4,0,0,1] = expr(1)
#(L)End initialize Edge
#(L)Initialize EdgeNet
Edge_Net[26,1,0,0,1,0:] = exprzeros(3)
Edge_Net[26,2,0,0,1,0:] = exprzeros(3)
Edge_Net[26,3,0,0,1,0:] = exprzeros(3)
Edge_Net[26,4,0,0,1,0:] = exprzeros(3)
#(L)End initialize EdgeNet
#(R)Initialize Edge
Edge[30,1,0,0,1] = expr(1)
Edge[30,2,0,0,1] = expr(1)
Edge[30,3,0,0,1] = expr(1)
Edge[30,4,0,0,1] = expr(1)
#(R)End initialize Edge
#(R)Initialize EdgeNet
Edge_Net[30,1,0,0,1,0:] = exprzeros(3)
Edge_Net[30,2,0,0,1,0:] = exprzeros(3)
Edge_Net[30,3,0,0,1,0:] = exprzeros(3)
Edge_Net[30,4,0,0,1,0:] = exprzeros(3)
#(R)End initialize EdgeNet
#(L)Disable GIL
Edge[26,0,1,1,1] = expr(0)
Edge[26,1,1,1,1] = expr(0)
Edge[26,2,1,1,1] = expr(0)
Edge[26,3,1,1,1] = expr(0)
Edge[26,4,1,1,1] = expr(0)
Edge[26,5,1,1,1] = expr(0)
Edge[26,0,1,1,1] = expr(0)
Edge[26,1,1,1,1] = expr(0)
Edge[26,2,1,1,1] = expr(0)
Edge[26,3,1,1,1] = expr(0)
Edge[26,4,1,1,1] = expr(0)
Edge[26,5,1,1,1] = expr(0)
#(L)End disable GIL
#(R)Disable GIL
Edge[30,0,1,1,1] = expr(0)
Edge[30,1,1,1,1] = expr(0)
Edge[30,2,1,1,1] = expr(0)
Edge[30,3,1,1,1] = expr(0)
Edge[30,4,1,1,1] = expr(0)
Edge[30,5,1,1,1] = expr(0)
Edge[30,0,1,1,1] = expr(0)
Edge[30,1,1,1,1] = expr(0)
Edge[30,2,1,1,1] = expr(0)
Edge[30,3,1,1,1] = expr(0)
Edge[30,4,1,1,1] = expr(0)
Edge[30,5,1,1,1] = expr(0)
#(R)End disable GIL

#Initialize N AIL1
Edge[2,28,0,0,1] = expr(1)
Edge[2,29,0,0,1] = expr(1)
Edge[2,30,0,0,1] = expr(1)
Edge[2,31,0,0,1] = expr(1)
Edge[2,32,0,0,1] = expr(1)
Edge[2,33,0,0,1] = expr(1)
Edge_Net[2,28,0,0,1,0:] = exprzeros(3)
Edge_Net[2,29,0,0,1,0:] = exprzeros(3)
Edge_Net[2,30,0,0,1,0:] = exprzeros(3)
Edge_Net[2,31,0,0,1,0:] = exprzeros(3)
Edge_Net[2,32,0,0,1,0:] = exprzeros(3)
Edge_Net[2,33,0,0,1,0:] = exprzeros(3)
Edge[6,28,0,0,1] = expr(1)
Edge[6,29,0,0,1] = expr(1)
Edge[6,30,0,0,1] = expr(1)
Edge[6,31,0,0,1] = expr(1)
Edge[6,32,0,0,1] = expr(1)
Edge[6,33,0,0,1] = expr(1)
Edge_Net[6,28,0,0,1,0:] = exprzeros(3)
Edge_Net[6,29,0,0,1,0:] = exprzeros(3)
Edge_Net[6,30,0,0,1,0:] = exprzeros(3)
Edge_Net[6,31,0,0,1,0:] = exprzeros(3)
Edge_Net[6,32,0,0,1,0:] = exprzeros(3)
Edge_Net[6,33,0,0,1,0:] = exprzeros(3)
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
Edge_Net[10,20,0,0,1,0:] = exprzeros(3)
Edge_Net[10,21,0,0,1,0:] = exprzeros(3)
Edge_Net[10,22,0,0,1,0:] = exprzeros(3)
Edge_Net[10,23,0,0,1,0:] = exprzeros(3)
Edge_Net[10,24,0,0,1,0:] = exprzeros(3)
Edge_Net[10,25,0,0,1,0:] = exprzeros(3)
Edge_Net[10,26,0,0,1,0:] = exprzeros(3)
Edge_Net[10,27,0,0,1,0:] = exprzeros(3)
Edge_Net[10,28,0,0,1,0:] = exprzeros(3)
Edge_Net[10,29,0,0,1,0:] = exprzeros(3)
Edge_Net[10,30,0,0,1,0:] = exprzeros(3)
Edge_Net[10,31,0,0,1,0:] = exprzeros(3)
Edge_Net[10,32,0,0,1,0:] = exprzeros(3)
Edge_Net[10,33,0,0,1,0:] = exprzeros(3)
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
Edge_Net[14,20,0,0,1,0:] = exprzeros(3)
Edge_Net[14,21,0,0,1,0:] = exprzeros(3)
Edge_Net[14,22,0,0,1,0:] = exprzeros(3)
Edge_Net[14,23,0,0,1,0:] = exprzeros(3)
Edge_Net[14,24,0,0,1,0:] = exprzeros(3)
Edge_Net[14,25,0,0,1,0:] = exprzeros(3)
Edge_Net[14,26,0,0,1,0:] = exprzeros(3)
Edge_Net[14,27,0,0,1,0:] = exprzeros(3)
Edge_Net[14,28,0,0,1,0:] = exprzeros(3)
Edge_Net[14,29,0,0,1,0:] = exprzeros(3)
Edge_Net[14,30,0,0,1,0:] = exprzeros(3)
Edge_Net[14,31,0,0,1,0:] = exprzeros(3)
Edge_Net[14,32,0,0,1,0:] = exprzeros(3)
Edge_Net[14,33,0,0,1,0:] = exprzeros(3)
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
Edge_Net[14,20,0,0,1,0:] = exprzeros(3)
Edge_Net[14,21,0,0,1,0:] = exprzeros(3)
Edge_Net[14,22,0,0,1,0:] = exprzeros(3)
Edge_Net[14,23,0,0,1,0:] = exprzeros(3)
Edge_Net[14,24,0,0,1,0:] = exprzeros(3)
Edge_Net[14,25,0,0,1,0:] = exprzeros(3)
Edge_Net[14,26,0,0,1,0:] = exprzeros(3)
Edge_Net[14,27,0,0,1,0:] = exprzeros(3)
Edge_Net[14,28,0,0,1,0:] = exprzeros(3)
Edge_Net[14,29,0,0,1,0:] = exprzeros(3)
Edge_Net[14,30,0,0,1,0:] = exprzeros(3)
Edge_Net[14,31,0,0,1,0:] = exprzeros(3)
Edge_Net[14,32,0,0,1,0:] = exprzeros(3)
Edge_Net[14,33,0,0,1,0:] = exprzeros(3)
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
Edge_Net[18,20,0,0,1,0:] = exprzeros(3)
Edge_Net[18,21,0,0,1,0:] = exprzeros(3)
Edge_Net[18,22,0,0,1,0:] = exprzeros(3)
Edge_Net[18,23,0,0,1,0:] = exprzeros(3)
Edge_Net[18,24,0,0,1,0:] = exprzeros(3)
Edge_Net[18,25,0,0,1,0:] = exprzeros(3)
Edge_Net[18,26,0,0,1,0:] = exprzeros(3)
Edge_Net[18,27,0,0,1,0:] = exprzeros(3)
Edge_Net[18,28,0,0,1,0:] = exprzeros(3)
Edge_Net[18,29,0,0,1,0:] = exprzeros(3)
Edge_Net[18,30,0,0,1,0:] = exprzeros(3)
Edge_Net[18,31,0,0,1,0:] = exprzeros(3)
Edge_Net[18,32,0,0,1,0:] = exprzeros(3)
Edge_Net[18,33,0,0,1,0:] = exprzeros(3)
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
Edge_Net[18,20,0,0,1,0:] = exprzeros(3)
Edge_Net[18,21,0,0,1,0:] = exprzeros(3)
Edge_Net[18,22,0,0,1,0:] = exprzeros(3)
Edge_Net[18,23,0,0,1,0:] = exprzeros(3)
Edge_Net[18,24,0,0,1,0:] = exprzeros(3)
Edge_Net[18,25,0,0,1,0:] = exprzeros(3)
Edge_Net[18,26,0,0,1,0:] = exprzeros(3)
Edge_Net[18,27,0,0,1,0:] = exprzeros(3)
Edge_Net[18,28,0,0,1,0:] = exprzeros(3)
Edge_Net[18,29,0,0,1,0:] = exprzeros(3)
Edge_Net[18,30,0,0,1,0:] = exprzeros(3)
Edge_Net[18,31,0,0,1,0:] = exprzeros(3)
Edge_Net[18,32,0,0,1,0:] = exprzeros(3)
Edge_Net[18,33,0,0,1,0:] = exprzeros(3)
Edge[22,20,0,0,1] = expr(1)
Edge[22,21,0,0,1] = expr(1)
Edge[22,22,0,0,1] = expr(1)
Edge[22,23,0,0,1] = expr(1)
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
Edge_Net[22,20,0,0,1,0:] = exprzeros(3)
Edge_Net[22,21,0,0,1,0:] = exprzeros(3)
Edge_Net[22,22,0,0,1,0:] = exprzeros(3)
Edge_Net[22,23,0,0,1,0:] = exprzeros(3)
Edge_Net[22,24,0,0,1,0:] = exprzeros(3)
Edge_Net[22,25,0,0,1,0:] = exprzeros(3)
Edge_Net[22,26,0,0,1,0:] = exprzeros(3)
Edge_Net[22,27,0,0,1,0:] = exprzeros(3)
Edge_Net[22,28,0,0,1,0:] = exprzeros(3)
Edge_Net[22,29,0,0,1,0:] = exprzeros(3)
Edge_Net[22,30,0,0,1,0:] = exprzeros(3)
Edge_Net[22,31,0,0,1,0:] = exprzeros(3)
Edge_Net[22,32,0,0,1,0:] = exprzeros(3)
Edge_Net[22,33,0,0,1,0:] = exprzeros(3)
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
Edge[22,19,1,1,1] = expr(0)
Edge[22,20,1,1,1] = expr(0)
Edge[22,21,1,1,1] = expr(0)
Edge[22,22,1,1,1] = expr(0)
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
Edge[26,22,0,0,1] = expr(1)
Edge[26,23,0,0,1] = expr(1)
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
Edge_Net[26,22,0,0,1,0:] = exprzeros(3)
Edge_Net[26,23,0,0,1,0:] = exprzeros(3)
Edge_Net[26,24,0,0,1,0:] = exprzeros(3)
Edge_Net[26,25,0,0,1,0:] = exprzeros(3)
Edge_Net[26,26,0,0,1,0:] = exprzeros(3)
Edge_Net[26,27,0,0,1,0:] = exprzeros(3)
Edge_Net[26,28,0,0,1,0:] = exprzeros(3)
Edge_Net[26,29,0,0,1,0:] = exprzeros(3)
Edge_Net[26,30,0,0,1,0:] = exprzeros(3)
Edge_Net[26,31,0,0,1,0:] = exprzeros(3)
Edge_Net[26,32,0,0,1,0:] = exprzeros(3)
Edge_Net[26,33,0,0,1,0:] = exprzeros(3)
Edge[30,22,0,0,1] = expr(1)
Edge[30,23,0,0,1] = expr(1)
Edge[30,24,0,0,1] = expr(1)
Edge[30,25,0,0,1] = expr(1)
Edge[30,26,0,0,1] = expr(1)
Edge[30,27,0,0,1] = expr(1)
Edge[30,28,0,0,1] = expr(1)
Edge[30,29,0,0,1] = expr(1)
Edge[30,30,0,0,1] = expr(1)
Edge[30,31,0,0,1] = expr(1)
Edge[30,32,0,0,1] = expr(1)
Edge[30,33,0,0,1] = expr(1)
Edge_Net[30,22,0,0,1,0:] = exprzeros(3)
Edge_Net[30,23,0,0,1,0:] = exprzeros(3)
Edge_Net[30,24,0,0,1,0:] = exprzeros(3)
Edge_Net[30,25,0,0,1,0:] = exprzeros(3)
Edge_Net[30,26,0,0,1,0:] = exprzeros(3)
Edge_Net[30,27,0,0,1,0:] = exprzeros(3)
Edge_Net[30,28,0,0,1,0:] = exprzeros(3)
Edge_Net[30,29,0,0,1,0:] = exprzeros(3)
Edge_Net[30,30,0,0,1,0:] = exprzeros(3)
Edge_Net[30,31,0,0,1,0:] = exprzeros(3)
Edge_Net[30,32,0,0,1,0:] = exprzeros(3)
Edge_Net[30,33,0,0,1,0:] = exprzeros(3)
Edge[26,21,1,1,1] = expr(0)
Edge[26,22,1,1,1] = expr(0)
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
Edge[30,21,1,1,1] = expr(0)
Edge[30,22,1,1,1] = expr(0)
Edge[30,23,1,1,1] = expr(0)
Edge[30,24,1,1,1] = expr(0)
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

# Net-1 subNet-0 Terminal[0] to Terminal[2]
# Poly(4,4,0,35) ==> Poly(4,4,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet1[4,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet1[4,0:36,0,0,2,0] = exprones(36)
Edge_Net[4,0:36,0,0,0,0] = exprones(36)
for x in range(4,4+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 1
Edge_Net_Subnet1[4,0:36,0,0,0,0] = exprones(36)
Edge_Net_Subnet1[4,0:36,0,0,2,0] = exprones(36)
Edge_Net[4,0:36,0,0,0,0] = exprones(36)
for x in range(4,4+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 1
# Net-1 subNet-1 Terminal[0] to Terminal[1]
# Poly(4,4,0,35) ==> Poly(12,12,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet1[4,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet1[4,0:36,0,0,2,1] = exprones(36)
Edge_Net[4,0:36,0,0,0,0] = exprones(36)
for x in range(4,4+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 1
Edge_Net_Subnet1[12,0:36,0,0,0,1] = exprones(36)
Edge_Net_Subnet1[12,0:36,0,0,2,1] = exprones(36)
Edge_Net[12,0:36,0,0,0,0] = exprones(36)
for x in range(12,12+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 1
# Net-1 subNet-2 Terminal[1] to Terminal[3]
# Poly(12,12,0,35) ==> Poly(12,12,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet1[12,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet1[12,0:36,0,0,2,2] = exprones(36)
Edge_Net[12,0:36,0,0,0,0] = exprones(36)
for x in range(12,12+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 1
Edge_Net_Subnet1[12,0:36,0,0,0,2] = exprones(36)
Edge_Net_Subnet1[12,0:36,0,0,2,2] = exprones(36)
Edge_Net[12,0:36,0,0,0,0] = exprones(36)
for x in range(12,12+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 1
# Net-2 subNet-0 Terminal[0] to Terminal[6]
# AIL1(6,6,1,10) ==> AIL1(6,6,28,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[6,1:11,0,0,1,0] = exprones(10)
Edge_Net_Subnet2[6,1:11,0,0,2,0] = exprones(10)
Edge_Net[6,1:11,0,0,1,1] = exprones(10)
for x in range(6,6+1):
  for y in range(1,10+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[6,28:34,0,0,1,0] = exprones(6)
Edge_Net_Subnet2[6,28:34,0,0,2,0] = exprones(6)
Edge_Net[6,28:34,0,0,1,1] = exprones(6)
for x in range(6,6+1):
  for y in range(28,33+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-1 Terminal[0] to Terminal[1]
# AIL1(6,6,1,10) ==> AIL1(10,10,1,14)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[6,1:11,0,0,1,1] = exprones(10)
Edge_Net_Subnet2[6,1:11,0,0,2,1] = exprones(10)
Edge_Net[6,1:11,0,0,1,1] = exprones(10)
for x in range(6,6+1):
  for y in range(1,10+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[10,1:15,0,0,1,1] = exprones(14)
Edge_Net_Subnet2[10,1:15,0,0,2,1] = exprones(14)
Edge_Net[10,1:15,0,0,1,1] = exprones(14)
for x in range(10,10+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-2 Terminal[1] to Terminal[7]
# AIL1(10,10,1,14) ==> AIL1(10,10,20,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[10,1:15,0,0,1,2] = exprones(14)
Edge_Net_Subnet2[10,1:15,0,0,2,2] = exprones(14)
Edge_Net[10,1:15,0,0,1,1] = exprones(14)
for x in range(10,10+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[10,20:34,0,0,1,2] = exprones(14)
Edge_Net_Subnet2[10,20:34,0,0,2,2] = exprones(14)
Edge_Net[10,20:34,0,0,1,1] = exprones(14)
for x in range(10,10+1):
  for y in range(20,33+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-3 Terminal[1] to Terminal[2]
# AIL1(10,10,1,14) ==> Poly(16,16,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[10,1:15,0,0,1,3] = exprones(14)
Edge_Net_Subnet2[10,1:15,0,0,2,3] = exprones(14)
Edge_Net[10,1:15,0,0,1,1] = exprones(14)
for x in range(10,10+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[16,0:36,0,0,0,3] = exprones(36)
Edge_Net_Subnet2[16,0:36,0,0,2,3] = exprones(36)
Edge_Net[16,0:36,0,0,0,1] = exprones(36)
for x in range(16,16+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-4 Terminal[2] to Terminal[8]
# Poly(16,16,0,35) ==> Poly(16,16,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[16,0:36,0,0,0,4] = exprones(36)
Edge_Net_Subnet2[16,0:36,0,0,2,4] = exprones(36)
Edge_Net[16,0:36,0,0,0,1] = exprones(36)
for x in range(16,16+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[16,0:36,0,0,0,4] = exprones(36)
Edge_Net_Subnet2[16,0:36,0,0,2,4] = exprones(36)
Edge_Net[16,0:36,0,0,0,1] = exprones(36)
for x in range(16,16+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-5 Terminal[2] to Terminal[3]
# Poly(16,16,0,35) ==> Poly(20,20,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[16,0:36,0,0,0,5] = exprones(36)
Edge_Net_Subnet2[16,0:36,0,0,2,5] = exprones(36)
Edge_Net[16,0:36,0,0,0,1] = exprones(36)
for x in range(16,16+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[20,0:36,0,0,0,5] = exprones(36)
Edge_Net_Subnet2[20,0:36,0,0,2,5] = exprones(36)
Edge_Net[20,0:36,0,0,0,1] = exprones(36)
for x in range(20,20+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-6 Terminal[3] to Terminal[9]
# Poly(20,20,0,35) ==> Poly(20,20,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[20,0:36,0,0,0,6] = exprones(36)
Edge_Net_Subnet2[20,0:36,0,0,2,6] = exprones(36)
Edge_Net[20,0:36,0,0,0,1] = exprones(36)
for x in range(20,20+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[20,0:36,0,0,0,6] = exprones(36)
Edge_Net_Subnet2[20,0:36,0,0,2,6] = exprones(36)
Edge_Net[20,0:36,0,0,0,1] = exprones(36)
for x in range(20,20+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-7 Terminal[3] to Terminal[4]
# Poly(20,20,0,35) ==> Poly(24,24,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[20,0:36,0,0,0,7] = exprones(36)
Edge_Net_Subnet2[20,0:36,0,0,2,7] = exprones(36)
Edge_Net[20,0:36,0,0,0,1] = exprones(36)
for x in range(20,20+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[24,0:36,0,0,0,7] = exprones(36)
Edge_Net_Subnet2[24,0:36,0,0,2,7] = exprones(36)
Edge_Net[24,0:36,0,0,0,1] = exprones(36)
for x in range(24,24+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-8 Terminal[4] to Terminal[5]
# Poly(24,24,0,35) ==> Poly(28,28,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[24,0:36,0,0,0,8] = exprones(36)
Edge_Net_Subnet2[24,0:36,0,0,2,8] = exprones(36)
Edge_Net[24,0:36,0,0,0,1] = exprones(36)
for x in range(24,24+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[28,0:36,0,0,0,8] = exprones(36)
Edge_Net_Subnet2[28,0:36,0,0,2,8] = exprones(36)
Edge_Net[28,0:36,0,0,0,1] = exprones(36)
for x in range(28,28+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-2 subNet-9 Terminal[5] to Terminal[10]
# Poly(28,28,0,35) ==> Poly(28,28,0,35)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet2[28,0:36,0,0,0,9] = exprones(36)
Edge_Net_Subnet2[28,0:36,0,0,2,9] = exprones(36)
Edge_Net[28,0:36,0,0,0,1] = exprones(36)
for x in range(28,28+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
Edge_Net_Subnet2[28,0:36,0,0,0,9] = exprones(36)
Edge_Net_Subnet2[28,0:36,0,0,2,9] = exprones(36)
Edge_Net[28,0:36,0,0,0,1] = exprones(36)
for x in range(28,28+1):
  for y in range(0,35+1) :
    outLayout[x][y][0][0] = 2
# Net-3 subNet-0 Terminal[0] to Terminal[2]
# AIL1(18,18,1,14) ==> AIL1(18,18,20,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[18,1:15,0,0,1,0] = exprones(14)
Edge_Net_Subnet3[18,1:15,0,0,2,0] = exprones(14)
Edge_Net[18,1:15,0,0,1,2] = exprones(14)
for x in range(18,18+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[18,20:34,0,0,1,0] = exprones(14)
Edge_Net_Subnet3[18,20:34,0,0,2,0] = exprones(14)
Edge_Net[18,20:34,0,0,1,2] = exprones(14)
for x in range(18,18+1):
  for y in range(20,33+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-1 Terminal[0] to Terminal[1]
# AIL1(18,18,1,14) ==> AIL1(26,26,1,14)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[18,1:15,0,0,1,1] = exprones(14)
Edge_Net_Subnet3[18,1:15,0,0,2,1] = exprones(14)
Edge_Net[18,1:15,0,0,1,2] = exprones(14)
for x in range(18,18+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[26,1:15,0,0,1,1] = exprones(14)
Edge_Net_Subnet3[26,1:15,0,0,2,1] = exprones(14)
Edge_Net[26,1:15,0,0,1,2] = exprones(14)
for x in range(26,26+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 3
# Net-3 subNet-2 Terminal[1] to Terminal[3]
# AIL1(26,26,1,14) ==> AIL1(26,26,22,33)   Form(minX, maxX, minY, maxY)
Edge_Net_Subnet3[26,1:15,0,0,1,2] = exprones(14)
Edge_Net_Subnet3[26,1:15,0,0,2,2] = exprones(14)
Edge_Net[26,1:15,0,0,1,2] = exprones(14)
for x in range(26,26+1):
  for y in range(1,14+1) :
    outLayout[x][y][0][0] = 3
Edge_Net_Subnet3[26,22:34,0,0,1,2] = exprones(12)
Edge_Net_Subnet3[26,22:34,0,0,2,2] = exprones(12)
Edge_Net[26,22:34,0,0,1,2] = exprones(12)
for x in range(26,26+1):
  for y in range(22,33+1) :
    outLayout[x][y][0][0] = 3
# Net = 1 Subnet = 1 | Left -> Right [0,16] Top -> Bottom [0,35]
# Range R1(4,4,0,35)
# Range R2(12,12,0,35)
### Disable edges outside window
Edge_Net_Subnet1[16:41+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(33696)

### Consistency Constraints
Net1_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,0]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet1[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,0])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net1_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,2,trend,0,1],Xor(Edge_Net_Subnet1[x,y,2,trend,1,1],Edge_Net_Subnet1[x,y,2,trend,2,1])),And(~Edge_Net_Subnet1[x,y,2,trend,0,1],~Edge_Net_Subnet1[x,y,2,trend,1,1],~Edge_Net_Subnet1[x,y,2,trend,2,1]))for x in range(0,16+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,3,1,0,1],Xor(Edge_Net_Subnet1[x,y,3,1,1,1],Edge_Net_Subnet1[x,y,3,1,2,1])),And(~Edge_Net_Subnet1[x,y,3,1,0,1],~Edge_Net_Subnet1[x,y,3,1,1,1],~Edge_Net_Subnet1[x,y,3,1,2,1]))for x in range(0,16+1)])for y in range(0,35+1)]).to_cnf()
Net1_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet1[x,y,1,trend,2,1],Xor(Edge_Net_Subnet1[x,y,1,trend,0,1],Edge_Net_Subnet1[x,y,1,trend,1,1])),And(~Edge_Net_Subnet1[x,y,1,trend,2,1],~Edge_Net_Subnet1[x,y,1,trend,0,1],~Edge_Net_Subnet1[x,y,1,trend,1,1]))for x in range(0,16+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net1_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,2,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet1[x,y,z,trend,1,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net1_Subnet1_C = And(Net1_Subnet1_C1, Net1_Subnet1_C2,Net1_Subnet1_C3_ME1_Mask,Net1_Subnet1_C4_MINT1_Mask,Net1_Subnet1_C5_AIL2GIL_Mask,Net1_Subnet1_C6,)
### Design Rules
Net1_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(0,16+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net1_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,1], ~Edge_Net_Subnet1[x-1,y,1,1,1,1]), And(Edge_Net_Subnet1[x+1,y,1,1,1,1], Edge_Net_Subnet1[x+2,y,1,1,1,1], Edge_Net_Subnet1[x+3,y,1,1,1,1], ))for x in range(1,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,1,1,1,1], ~Edge_Net_Subnet1[x+1,y,1,1,1,1]), And(Edge_Net_Subnet1[x-1,y,1,1,1,1], Edge_Net_Subnet1[x-2,y,1,1,1,1], Edge_Net_Subnet1[x-3,y,1,1,1,1], ))for x in range(3,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(0,16+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(0,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1]), And(Edge_Net_Subnet1[x,y+1,1,0,0,1], Edge_Net_Subnet1[x,y+2,1,0,0,1], Edge_Net_Subnet1[x,y+3,1,0,0,1], ))for x in range(0,16+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1]), And(Edge_Net_Subnet1[x,y-1,1,0,0,1], Edge_Net_Subnet1[x,y-2,1,0,0,1], Edge_Net_Subnet1[x,y-3,1,0,0,1], ))for x in range(0,16+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge_Net_Subnet1[x,y-1,1,0,0,1]), And(Edge_Net_Subnet1[x,y+1,1,0,0,1], Edge_Net_Subnet1[x,y+2,1,0,0,1], Edge_Net_Subnet1[x,y+3,1,0,0,1], ))for x in range(0,16+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge_Net_Subnet1[x,y+1,1,0,0,1]), And(Edge_Net_Subnet1[x,y-1,1,0,0,1], Edge_Net_Subnet1[x,y-2,1,0,0,1], Edge_Net_Subnet1[x,y-3,1,0,0,1], ))for x in range(0,16+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net1_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(0,16+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(0,16+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(0,16+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(0,16+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(0,16+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(0,16+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net1_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,1], ~Edge_Net_Subnet1[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet1[x+1,y,3,1,mask,1], Edge_Net_Subnet1[x+2,y,3,1,mask,1], Edge_Net_Subnet1[x+3,y,3,1,mask,1], Edge_Net_Subnet1[x+4,y,3,1,mask,1], Edge_Net_Subnet1[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(1,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,3,1,mask,1], ~Edge_Net_Subnet1[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet1[x-1,y,3,1,mask,1], Edge_Net_Subnet1[x-2,y,3,1,mask,1], Edge_Net_Subnet1[x-3,y,3,1,mask,1], Edge_Net_Subnet1[x-4,y,3,1,mask,1], Edge_Net_Subnet1[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,1], And(Edge_Net_Subnet1[x+1,y,3,1,mask,1], Edge_Net_Subnet1[x+2,y,3,1,mask,1], Edge_Net_Subnet1[x+3,y,3,1,mask,1], Edge_Net_Subnet1[x+4,y,3,1,mask,1], Edge_Net_Subnet1[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(0, 0+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(0,16+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(0,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,1], ~Edge_Net_Subnet1[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet1[x+1,y,2,1,mask,1], Edge_Net_Subnet1[x+2,y,2,1,mask,1], Edge_Net_Subnet1[x+3,y,2,1,mask,1], Edge_Net_Subnet1[x+4,y,2,1,mask,1], Edge_Net_Subnet1[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(1,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet1[x,y,2,1,mask,1], ~Edge_Net_Subnet1[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet1[x-1,y,2,1,mask,1], Edge_Net_Subnet1[x-2,y,2,1,mask,1], Edge_Net_Subnet1[x-3,y,2,1,mask,1], Edge_Net_Subnet1[x-4,y,2,1,mask,1], Edge_Net_Subnet1[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,1], And(Edge_Net_Subnet1[x-1,y,2,1,mask,1], Edge_Net_Subnet1[x-2,y,2,1,mask,1], Edge_Net_Subnet1[x-3,y,2,1,mask,1], Edge_Net_Subnet1[x-4,y,2,1,mask,1], Edge_Net_Subnet1[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(0,0+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,1], And(Edge_Net_Subnet1[x+1,y,2,1,mask,1], Edge_Net_Subnet1[x+2,y,2,1,mask,1], Edge_Net_Subnet1[x+3,y,2,1,mask,1], Edge_Net_Subnet1[x+4,y,2,1,mask,1], Edge_Net_Subnet1[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(16-1,0)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,1], ~Edge_Net_Subnet1[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet1[x,y+1,2,0,mask,1], Edge_Net_Subnet1[x,y+2,2,0,mask,1], Edge_Net_Subnet1[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,1], ~Edge_Net_Subnet1[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet1[x,y-1,2,0,mask,1], Edge_Net_Subnet1[x,y-2,2,0,mask,1], Edge_Net_Subnet1[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,1], And(Edge_Net_Subnet1[x,y+1,2,0,mask,1], Edge_Net_Subnet1[x,y+2,2,0,mask,1], Edge_Net_Subnet1[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet1[x,y,2,0,mask,1], And(Edge_Net_Subnet1[x,y-1,2,0,mask,1], Edge_Net_Subnet1[x,y-2,2,0,mask,1], Edge_Net_Subnet1[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(35,35+1)]),
	).to_cnf()
Net1_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(0,16+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(0,16+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net1_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet1[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net1_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(0,16+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(0,16+1)])for y in range(3,35+1)]),
	).to_cnf()
Net1_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(4,35+1)]),
	).to_cnf()
Net1_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,16+1)])for y in range(0,35+1)]),
	).to_cnf()
Net1_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet1[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])
	).to_cnf()
Net1_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet1[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(0,16+1)])for y in range(2,35+1)]),
	).to_cnf()
Net1_Subnet1_DR = And(Net1_Subnet1_DR_Trend, Net1_Subnet1_DR_GIL_HorMinWidth,Net1_Subnet1_DR_GIL_HorMinSpacing,Net1_Subnet1_DR_GIL_VerMinSpacing,Net1_Subnet1_DR_AIL2_VerMinWidth,Net1_Subnet1_DR_AIL2_VerMinSpacing,Net1_Subnet1_DR_VerAIL2_HorMinSpacing,Net1_Subnet1_DR_MINT1AB_HorMinWidth,Net1_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net1_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net1_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net1_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net1_Subnet1_DR_M1AB_MinWidth,Net1_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net1_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net1_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net1_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net1_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net1_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net1_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net1_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net1_Subnet1_DR_V0_HorMinSpacing,Net1_Subnet1_DR_V1_HorMinSpacing,Net1_Subnet1_DR_V0_VerMinSpacing,Net1_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net1_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet1,[4,0,0,0, 4,1,0,0, 4,2,0,0, 4,3,0,0, 4,4,0,0, 4,5,0,0, 4,6,0,0, 4,7,0,0, 4,8,0,0, 4,9,0,0, 4,10,0,0, 4,11,0,0, 4,12,0,0, 4,13,0,0, 4,14,0,0, 4,15,0,0, 4,16,0,0, 4,17,0,0, 4,18,0,0, 4,19,0,0, 4,20,0,0, 4,21,0,0, 4,22,0,0, 4,23,0,0, 4,24,0,0, 4,25,0,0, 4,26,0,0, 4,27,0,0, 4,28,0,0, 4,29,0,0, 4,30,0,0, 4,31,0,0, 4,32,0,0, 4,33,0,0, 4,34,0,0, 4,35,0,0, ],36,0,0,1,16,35,3,1),
	RConstraints.R1(Edge_Net_Subnet1,[12,0,0,0, 12,1,0,0, 12,2,0,0, 12,3,0,0, 12,4,0,0, 12,5,0,0, 12,6,0,0, 12,7,0,0, 12,8,0,0, 12,9,0,0, 12,10,0,0, 12,11,0,0, 12,12,0,0, 12,13,0,0, 12,14,0,0, 12,15,0,0, 12,16,0,0, 12,17,0,0, 12,18,0,0, 12,19,0,0, 12,20,0,0, 12,21,0,0, 12,22,0,0, 12,23,0,0, 12,24,0,0, 12,25,0,0, 12,26,0,0, 12,27,0,0, 12,28,0,0, 12,29,0,0, 12,30,0,0, 12,31,0,0, 12,32,0,0, 12,33,0,0, 12,34,0,0, 12,35,0,0, ],36,0,0,1,16,35,3,1),
	).to_cnf()
Net1_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet1,Edge,Edge_Net,[4,0,0, 4,1,0, 4,2,0, 4,3,0, 4,4,0, 4,5,0, 4,6,0, 4,7,0, 4,8,0, 4,9,0, 4,10,0, 4,11,0, 4,12,0, 4,13,0, 4,14,0, 4,15,0, 4,16,0, 4,17,0, 4,18,0, 4,19,0, 4,20,0, 4,21,0, 4,22,0, 4,23,0, 4,24,0, 4,25,0, 4,26,0, 4,27,0, 4,28,0, 4,29,0, 4,30,0, 4,31,0, 4,32,0, 4,33,0, 4,34,0, 4,35,0, 12,0,0, 12,1,0, 12,2,0, 12,3,0, 12,4,0, 12,5,0, 12,6,0, 12,7,0, 12,8,0, 12,9,0, 12,10,0, 12,11,0, 12,12,0, 12,13,0, 12,14,0, 12,15,0, 12,16,0, 12,17,0, 12,18,0, 12,19,0, 12,20,0, 12,21,0, 12,22,0, 12,23,0, 12,24,0, 12,25,0, 12,26,0, 12,27,0, 12,28,0, 12,29,0, 12,30,0, 12,31,0, 12,32,0, 12,33,0, 12,34,0, 12,35,0, ],72,0,0,0,16,35,3,1,0),
	)
Net1_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,0],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(1,2+1)])for x in range(0,16+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	).to_cnf()
Net1_Subnet1_R = And(Net1_Subnet1_R1,Net1_Subnet1_R2,Net1_Subnet1_R3,)
Net1_Subnet1_Formula = And(Net1_Subnet1_C,Net1_Subnet1_DR,Net1_Subnet1_R)
# Net = 2 Subnet = 0 | Left -> Right [2,10] Top -> Bottom [0,35]
# Range R1(6,6,1,10)
# Range R2(6,6,28,33)
### Disable edges outside window
Edge_Net_Subnet2[0:2,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(2592)
Edge_Net_Subnet2[10:41+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(41472)

### Consistency Constraints
Net2_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(2,10+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(2,10+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,0],Xor(Edge_Net_Subnet2[x,y,2,trend,1,0],Edge_Net_Subnet2[x,y,2,trend,2,0])),And(~Edge_Net_Subnet2[x,y,2,trend,0,0],~Edge_Net_Subnet2[x,y,2,trend,1,0],~Edge_Net_Subnet2[x,y,2,trend,2,0]))for x in range(2,10+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,0],Xor(Edge_Net_Subnet2[x,y,3,1,1,0],Edge_Net_Subnet2[x,y,3,1,2,0])),And(~Edge_Net_Subnet2[x,y,3,1,0,0],~Edge_Net_Subnet2[x,y,3,1,1,0],~Edge_Net_Subnet2[x,y,3,1,2,0]))for x in range(2,10+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,0],Xor(Edge_Net_Subnet2[x,y,1,trend,0,0],Edge_Net_Subnet2[x,y,1,trend,1,0])),And(~Edge_Net_Subnet2[x,y,1,trend,2,0],~Edge_Net_Subnet2[x,y,1,trend,0,0],~Edge_Net_Subnet2[x,y,1,trend,1,0]))for x in range(2,10+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet0_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,0], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0+1,10)]))for trend in range(0,1+1)])for x in range(2,10+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,0], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0+1,10)]))for trend in range(0,1+1)])for x in range(2,10+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet0_C = And(Net2_Subnet0_C1, Net2_Subnet0_C2,Net2_Subnet0_C3_ME1_Mask,Net2_Subnet0_C4_MINT1_Mask,Net2_Subnet0_C5_AIL2GIL_Mask,Net2_Subnet0_C6,)
### Design Rules
Net2_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(2,10+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(2,10+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(2,10+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge_Net_Subnet2[x-1,y,1,1,1,0]), And(Edge_Net_Subnet2[x+1,y,1,1,1,0], Edge_Net_Subnet2[x+2,y,1,1,1,0], Edge_Net_Subnet2[x+3,y,1,1,1,0], ))for x in range(2,10+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge_Net_Subnet2[x+1,y,1,1,1,0]), And(Edge_Net_Subnet2[x-1,y,1,1,1,0], Edge_Net_Subnet2[x-2,y,1,1,1,0], Edge_Net_Subnet2[x-3,y,1,1,1,0], ))for x in range(3,10+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,10+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(2,10+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(2,10+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(2,10+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0]), And(Edge_Net_Subnet2[x,y+1,1,0,0,0], Edge_Net_Subnet2[x,y+2,1,0,0,0], Edge_Net_Subnet2[x,y+3,1,0,0,0], ))for x in range(2,10+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0]), And(Edge_Net_Subnet2[x,y-1,1,0,0,0], Edge_Net_Subnet2[x,y-2,1,0,0,0], Edge_Net_Subnet2[x,y-3,1,0,0,0], ))for x in range(2,10+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge_Net_Subnet2[x,y-1,1,0,0,0]), And(Edge_Net_Subnet2[x,y+1,1,0,0,0], Edge_Net_Subnet2[x,y+2,1,0,0,0], Edge_Net_Subnet2[x,y+3,1,0,0,0], ))for x in range(2,10+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge_Net_Subnet2[x,y+1,1,0,0,0]), And(Edge_Net_Subnet2[x,y-1,1,0,0,0], Edge_Net_Subnet2[x,y-2,1,0,0,0], Edge_Net_Subnet2[x,y-3,1,0,0,0], ))for x in range(2,10+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(2,10+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(2,10+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(2,10+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(2,10+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(2,10+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(2,10+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(2,10+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,10+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge_Net_Subnet2[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,0], Edge_Net_Subnet2[x+2,y,3,1,mask,0], Edge_Net_Subnet2[x+3,y,3,1,mask,0], Edge_Net_Subnet2[x+4,y,3,1,mask,0], Edge_Net_Subnet2[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge_Net_Subnet2[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,0], Edge_Net_Subnet2[x-2,y,3,1,mask,0], Edge_Net_Subnet2[x-3,y,3,1,mask,0], Edge_Net_Subnet2[x-4,y,3,1,mask,0], Edge_Net_Subnet2[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,10+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,10+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(2,10+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(2,10+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,10+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(2,10+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge_Net_Subnet2[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,0], Edge_Net_Subnet2[x+2,y,2,1,mask,0], Edge_Net_Subnet2[x+3,y,2,1,mask,0], Edge_Net_Subnet2[x+4,y,2,1,mask,0], Edge_Net_Subnet2[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge_Net_Subnet2[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,0], Edge_Net_Subnet2[x-2,y,2,1,mask,0], Edge_Net_Subnet2[x-3,y,2,1,mask,0], Edge_Net_Subnet2[x-4,y,2,1,mask,0], Edge_Net_Subnet2[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(5,10+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(Edge_Net_Subnet2[x-1,y,2,1,mask,0], Edge_Net_Subnet2[x-2,y,2,1,mask,0], Edge_Net_Subnet2[x-3,y,2,1,mask,0], Edge_Net_Subnet2[x-4,y,2,1,mask,0], Edge_Net_Subnet2[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(2,2+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(Edge_Net_Subnet2[x+1,y,2,1,mask,0], Edge_Net_Subnet2[x+2,y,2,1,mask,0], Edge_Net_Subnet2[x+3,y,2,1,mask,0], Edge_Net_Subnet2[x+4,y,2,1,mask,0], Edge_Net_Subnet2[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(10-1,2)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge_Net_Subnet2[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,0], Edge_Net_Subnet2[x,y+2,2,0,mask,0], Edge_Net_Subnet2[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge_Net_Subnet2[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,0], Edge_Net_Subnet2[x,y-2,2,0,mask,0], Edge_Net_Subnet2[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,0], And(Edge_Net_Subnet2[x,y+1,2,0,mask,0], Edge_Net_Subnet2[x,y+2,2,0,mask,0], Edge_Net_Subnet2[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,0], And(Edge_Net_Subnet2[x,y-1,2,0,mask,0], Edge_Net_Subnet2[x,y-2,2,0,mask,0], Edge_Net_Subnet2[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,10+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(2,10+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,10+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(2,10+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(2,10+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(2,10+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(2,10+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(2,10+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,10+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(2,10+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,10+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,10+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(2,10+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,10+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(2,10+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(2,10+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(2,10+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(2,10+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(2,10+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet0_DR = And(Net2_Subnet0_DR_Trend, Net2_Subnet0_DR_GIL_HorMinWidth,Net2_Subnet0_DR_GIL_HorMinSpacing,Net2_Subnet0_DR_GIL_VerMinSpacing,Net2_Subnet0_DR_AIL2_VerMinWidth,Net2_Subnet0_DR_AIL2_VerMinSpacing,Net2_Subnet0_DR_VerAIL2_HorMinSpacing,Net2_Subnet0_DR_MINT1AB_HorMinWidth,Net2_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet0_DR_M1AB_MinWidth,Net2_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet0_DR_V0_HorMinSpacing,Net2_Subnet0_DR_V1_HorMinSpacing,Net2_Subnet0_DR_V0_VerMinSpacing,Net2_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[6,1,0,0, 6,2,0,0, 6,3,0,0, 6,4,0,0, 6,5,0,0, 6,6,0,0, 6,7,0,0, 6,8,0,0, 6,9,0,0, 6,10,0,0, ],10,2,0,1,10,35,3,0),
	RConstraints.R1(Edge_Net_Subnet2,[6,28,0,0, 6,29,0,0, 6,30,0,0, 6,31,0,0, 6,32,0,0, 6,33,0,0, ],6,2,0,1,10,35,3,0),
	).to_cnf()
Net2_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[6,1,0, 6,2,0, 6,3,0, 6,4,0, 6,5,0, 6,6,0, 6,7,0, 6,8,0, 6,9,0, 6,10,0, 6,11,0, 6,28,0, 6,29,0, 6,30,0, 6,31,0, 6,32,0, 6,33,0, 6,34,0, ],18,2,0,0,10,35,3,0,1),
	)
Net2_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(2,10+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,2+1)])for x in range(2,10+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet0_R = And(Net2_Subnet0_R1,Net2_Subnet0_R2,Net2_Subnet0_R3,)
Net2_Subnet0_Formula = And(Net2_Subnet0_C,Net2_Subnet0_DR,Net2_Subnet0_R)
# Net = 2 Subnet = 1 | Left -> Right [2,14] Top -> Bottom [0,18]
# Range R1(6,6,1,10)
# Range R2(10,10,1,14)
### Disable edges outside window
Edge_Net_Subnet2[0:2,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(2592)
Edge_Net_Subnet2[2:14,18:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(7776)
Edge_Net_Subnet2[14:41+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(36288)

### Consistency Constraints
Net2_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(2,14+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(2,14+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,1],Xor(Edge_Net_Subnet2[x,y,2,trend,1,1],Edge_Net_Subnet2[x,y,2,trend,2,1])),And(~Edge_Net_Subnet2[x,y,2,trend,0,1],~Edge_Net_Subnet2[x,y,2,trend,1,1],~Edge_Net_Subnet2[x,y,2,trend,2,1]))for x in range(2,14+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,1],Xor(Edge_Net_Subnet2[x,y,3,1,1,1],Edge_Net_Subnet2[x,y,3,1,2,1])),And(~Edge_Net_Subnet2[x,y,3,1,0,1],~Edge_Net_Subnet2[x,y,3,1,1,1],~Edge_Net_Subnet2[x,y,3,1,2,1]))for x in range(2,14+1)])for y in range(0,18+1)]).to_cnf()
Net2_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,1],Xor(Edge_Net_Subnet2[x,y,1,trend,0,1],Edge_Net_Subnet2[x,y,1,trend,1,1])),And(~Edge_Net_Subnet2[x,y,1,trend,2,1],~Edge_Net_Subnet2[x,y,1,trend,0,1],~Edge_Net_Subnet2[x,y,1,trend,1,1]))for x in range(2,14+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(2,14+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(1+1,10)]))for trend in range(0,1+1)])for x in range(2,14+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(2,14+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(1+1,10)]))for trend in range(0,1+1)])for x in range(2,14+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet1_C = And(Net2_Subnet1_C1, Net2_Subnet1_C2,Net2_Subnet1_C3_ME1_Mask,Net2_Subnet1_C4_MINT1_Mask,Net2_Subnet1_C5_AIL2GIL_Mask,Net2_Subnet1_C6,)
### Design Rules
Net2_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(2,14+1)])for y in range(0,18+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,1], ~Edge_Net_Subnet2[x-1,y,1,1,1,1]), And(Edge_Net_Subnet2[x+1,y,1,1,1,1], Edge_Net_Subnet2[x+2,y,1,1,1,1], Edge_Net_Subnet2[x+3,y,1,1,1,1], ))for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,1], ~Edge_Net_Subnet2[x+1,y,1,1,1,1]), And(Edge_Net_Subnet2[x-1,y,1,1,1,1], Edge_Net_Subnet2[x-2,y,1,1,1,1], Edge_Net_Subnet2[x-3,y,1,1,1,1], ))for x in range(3,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(3,14+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(2,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(2,14+1)])for y in range(3,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1]), And(Edge_Net_Subnet2[x,y+1,1,0,0,1], Edge_Net_Subnet2[x,y+2,1,0,0,1], Edge_Net_Subnet2[x,y+3,1,0,0,1], ))for x in range(2,14+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge_Net_Subnet2[x,y-1,1,0,0,1]), And(Edge_Net_Subnet2[x,y+1,1,0,0,1], Edge_Net_Subnet2[x,y+2,1,0,0,1], Edge_Net_Subnet2[x,y+3,1,0,0,1], ))for x in range(2,14+1)])for y in range(0+1,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge_Net_Subnet2[x,y+1,1,0,0,1]), And(Edge_Net_Subnet2[x,y-1,1,0,0,1], Edge_Net_Subnet2[x,y-2,1,0,0,1], Edge_Net_Subnet2[x,y-3,1,0,0,1], ))for x in range(2,14+1)])for y in range(0+3,18+1)])
	).to_cnf()
Net2_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(2,14+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(2,14+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(2,14+1)])for y in range(0+3,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(2,14+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(3,14+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,1], ~Edge_Net_Subnet2[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,1], Edge_Net_Subnet2[x+2,y,3,1,mask,1], Edge_Net_Subnet2[x+3,y,3,1,mask,1], Edge_Net_Subnet2[x+4,y,3,1,mask,1], Edge_Net_Subnet2[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,1], ~Edge_Net_Subnet2[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,1], Edge_Net_Subnet2[x-2,y,3,1,mask,1], Edge_Net_Subnet2[x-3,y,3,1,mask,1], Edge_Net_Subnet2[x-4,y,3,1,mask,1], Edge_Net_Subnet2[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(3,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(2,14+1)])for y in range(2,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(3,14+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(2,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,1], ~Edge_Net_Subnet2[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,1], Edge_Net_Subnet2[x+2,y,2,1,mask,1], Edge_Net_Subnet2[x+3,y,2,1,mask,1], Edge_Net_Subnet2[x+4,y,2,1,mask,1], Edge_Net_Subnet2[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,1], ~Edge_Net_Subnet2[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,1], Edge_Net_Subnet2[x-2,y,2,1,mask,1], Edge_Net_Subnet2[x-3,y,2,1,mask,1], Edge_Net_Subnet2[x-4,y,2,1,mask,1], Edge_Net_Subnet2[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,1], And(Edge_Net_Subnet2[x-1,y,2,1,mask,1], Edge_Net_Subnet2[x-2,y,2,1,mask,1], Edge_Net_Subnet2[x-3,y,2,1,mask,1], Edge_Net_Subnet2[x-4,y,2,1,mask,1], Edge_Net_Subnet2[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(2,2+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,1], And(Edge_Net_Subnet2[x+1,y,2,1,mask,1], Edge_Net_Subnet2[x+2,y,2,1,mask,1], Edge_Net_Subnet2[x+3,y,2,1,mask,1], Edge_Net_Subnet2[x+4,y,2,1,mask,1], Edge_Net_Subnet2[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(14-1,2)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,1], ~Edge_Net_Subnet2[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,1], Edge_Net_Subnet2[x,y+2,2,0,mask,1], Edge_Net_Subnet2[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0+1,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,1], ~Edge_Net_Subnet2[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,1], Edge_Net_Subnet2[x,y-2,2,0,mask,1], Edge_Net_Subnet2[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0+3,18+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,1], And(Edge_Net_Subnet2[x,y+1,2,0,mask,1], Edge_Net_Subnet2[x,y+2,2,0,mask,1], Edge_Net_Subnet2[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,1], And(Edge_Net_Subnet2[x,y-1,2,0,mask,1], Edge_Net_Subnet2[x,y-2,2,0,mask,1], Edge_Net_Subnet2[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(18,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(3,14+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(2,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(5,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(2,14+1)])for y in range(2,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(2,14+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(4,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(2,14+1)])for y in range(3,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(4,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(3,14+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(4,14+1)])for y in range(0,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(3,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(2,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(3,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(2,14+1)])for y in range(0,18+1)])
	).to_cnf()
Net2_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(2,14+1)])for y in range(2,18+1)]),
	).to_cnf()
Net2_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(2,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(2,14+1)])for y in range(2,18+1)]),
	).to_cnf()
Net2_Subnet1_DR = And(Net2_Subnet1_DR_Trend, Net2_Subnet1_DR_GIL_HorMinWidth,Net2_Subnet1_DR_GIL_HorMinSpacing,Net2_Subnet1_DR_GIL_VerMinSpacing,Net2_Subnet1_DR_AIL2_VerMinWidth,Net2_Subnet1_DR_AIL2_VerMinSpacing,Net2_Subnet1_DR_VerAIL2_HorMinSpacing,Net2_Subnet1_DR_MINT1AB_HorMinWidth,Net2_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet1_DR_M1AB_MinWidth,Net2_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet1_DR_V0_HorMinSpacing,Net2_Subnet1_DR_V1_HorMinSpacing,Net2_Subnet1_DR_V0_VerMinSpacing,Net2_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[6,1,0,0, 6,2,0,0, 6,3,0,0, 6,4,0,0, 6,5,0,0, 6,6,0,0, 6,7,0,0, 6,8,0,0, 6,9,0,0, 6,10,0,0, ],10,2,0,1,14,18,3,1),
	RConstraints.R1(Edge_Net_Subnet2,[10,1,0,0, 10,2,0,0, 10,3,0,0, 10,4,0,0, 10,5,0,0, 10,6,0,0, 10,7,0,0, 10,8,0,0, 10,9,0,0, 10,10,0,0, 10,11,0,0, 10,12,0,0, 10,13,0,0, 10,14,0,0, ],14,2,0,1,14,18,3,1),
	).to_cnf()
Net2_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[6,1,0, 6,2,0, 6,3,0, 6,4,0, 6,5,0, 6,6,0, 6,7,0, 6,8,0, 6,9,0, 6,10,0, 6,11,0, 10,1,0, 10,2,0, 10,3,0, 10,4,0, 10,5,0, 10,6,0, 10,7,0, 10,8,0, 10,9,0, 10,10,0, 10,11,0, 10,12,0, 10,13,0, 10,14,0, 10,15,0, ],26,2,0,0,14,18,3,1,1),
	)
Net2_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(2,14+1)])for y in range(0,18+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,2+1)])for x in range(2,14+1)])for y in range(0,18+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet1_R = And(Net2_Subnet1_R1,Net2_Subnet1_R2,Net2_Subnet1_R3,)
Net2_Subnet1_Formula = And(Net2_Subnet1_C,Net2_Subnet1_DR,Net2_Subnet1_R)
# Net = 2 Subnet = 2 | Left -> Right [6,14] Top -> Bottom [0,35]
# Range R1(10,10,1,14)
# Range R2(10,10,20,33)
### Disable edges outside window
Edge_Net_Subnet2[0:6,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(7776)
Edge_Net_Subnet2[14:41+1,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(36288)

### Consistency Constraints
Net2_Subnet2_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet2_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,2]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet2_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,2],Xor(Edge_Net_Subnet2[x,y,2,trend,1,2],Edge_Net_Subnet2[x,y,2,trend,2,2])),And(~Edge_Net_Subnet2[x,y,2,trend,0,2],~Edge_Net_Subnet2[x,y,2,trend,1,2],~Edge_Net_Subnet2[x,y,2,trend,2,2]))for x in range(6,14+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet2_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,2],Xor(Edge_Net_Subnet2[x,y,3,1,1,2],Edge_Net_Subnet2[x,y,3,1,2,2])),And(~Edge_Net_Subnet2[x,y,3,1,0,2],~Edge_Net_Subnet2[x,y,3,1,1,2],~Edge_Net_Subnet2[x,y,3,1,2,2]))for x in range(6,14+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet2_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,2],Xor(Edge_Net_Subnet2[x,y,1,trend,0,2],Edge_Net_Subnet2[x,y,1,trend,1,2])),And(~Edge_Net_Subnet2[x,y,1,trend,2,2],~Edge_Net_Subnet2[x,y,1,trend,0,2],~Edge_Net_Subnet2[x,y,1,trend,1,2]))for x in range(6,14+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet2_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(2+1,10)]))for trend in range(0,1+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(2+1,10)]))for trend in range(0,1+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet2_C = And(Net2_Subnet2_C1, Net2_Subnet2_C2,Net2_Subnet2_C3_ME1_Mask,Net2_Subnet2_C4_MINT1_Mask,Net2_Subnet2_C5_AIL2GIL_Mask,Net2_Subnet2_C6,)
### Design Rules
Net2_Subnet2_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(6,14+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet2_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,2], ~Edge_Net_Subnet2[x-1,y,1,1,1,2]), And(Edge_Net_Subnet2[x+1,y,1,1,1,2], Edge_Net_Subnet2[x+2,y,1,1,1,2], Edge_Net_Subnet2[x+3,y,1,1,1,2], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,2], ~Edge_Net_Subnet2[x+1,y,1,1,1,2]), And(Edge_Net_Subnet2[x-1,y,1,1,1,2], Edge_Net_Subnet2[x-2,y,1,1,1,2], Edge_Net_Subnet2[x-3,y,1,1,1,2], ))for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,2], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,2], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,2], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(6,14+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,2], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(6,14+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2]), And(Edge_Net_Subnet2[x,y+1,1,0,0,2], Edge_Net_Subnet2[x,y+2,1,0,0,2], Edge_Net_Subnet2[x,y+3,1,0,0,2], ))for x in range(6,14+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2]), And(Edge_Net_Subnet2[x,y-1,1,0,0,2], Edge_Net_Subnet2[x,y-2,1,0,0,2], Edge_Net_Subnet2[x,y-3,1,0,0,2], ))for x in range(6,14+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge_Net_Subnet2[x,y-1,1,0,0,2]), And(Edge_Net_Subnet2[x,y+1,1,0,0,2], Edge_Net_Subnet2[x,y+2,1,0,0,2], Edge_Net_Subnet2[x,y+3,1,0,0,2], ))for x in range(6,14+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge_Net_Subnet2[x,y+1,1,0,0,2]), And(Edge_Net_Subnet2[x,y-1,1,0,0,2], Edge_Net_Subnet2[x,y-2,1,0,0,2], Edge_Net_Subnet2[x,y-3,1,0,0,2], ))for x in range(6,14+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet2_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(6,14+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(6,14+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(6,14+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(6,14+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(6,14+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(6,14+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet2_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,2], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,2], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,2], ~Edge_Net_Subnet2[x-1,y,3,1,mask,2]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,2], Edge_Net_Subnet2[x+2,y,3,1,mask,2], Edge_Net_Subnet2[x+3,y,3,1,mask,2], Edge_Net_Subnet2[x+4,y,3,1,mask,2], Edge_Net_Subnet2[x+5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,2], ~Edge_Net_Subnet2[x+1,y,3,1,mask,2]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,2], Edge_Net_Subnet2[x-2,y,3,1,mask,2], Edge_Net_Subnet2[x-3,y,3,1,mask,2], Edge_Net_Subnet2[x-4,y,3,1,mask,2], Edge_Net_Subnet2[x-5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,2], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,2], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,2], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,2], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,2], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(6,14+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,2], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(6,14+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,2], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,2], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,2], ~Edge_Net_Subnet2[x-1,y,2,1,mask,2]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,2], Edge_Net_Subnet2[x+2,y,2,1,mask,2], Edge_Net_Subnet2[x+3,y,2,1,mask,2], Edge_Net_Subnet2[x+4,y,2,1,mask,2], Edge_Net_Subnet2[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,2], ~Edge_Net_Subnet2[x+1,y,2,1,mask,2]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,2], Edge_Net_Subnet2[x-2,y,2,1,mask,2], Edge_Net_Subnet2[x-3,y,2,1,mask,2], Edge_Net_Subnet2[x-4,y,2,1,mask,2], Edge_Net_Subnet2[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,2], And(Edge_Net_Subnet2[x-1,y,2,1,mask,2], Edge_Net_Subnet2[x-2,y,2,1,mask,2], Edge_Net_Subnet2[x-3,y,2,1,mask,2], Edge_Net_Subnet2[x-4,y,2,1,mask,2], Edge_Net_Subnet2[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(6,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,2], And(Edge_Net_Subnet2[x+1,y,2,1,mask,2], Edge_Net_Subnet2[x+2,y,2,1,mask,2], Edge_Net_Subnet2[x+3,y,2,1,mask,2], Edge_Net_Subnet2[x+4,y,2,1,mask,2], Edge_Net_Subnet2[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(14-1,6)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,2], ~Edge_Net_Subnet2[x,y-1,2,0,mask,2]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,2], Edge_Net_Subnet2[x,y+2,2,0,mask,2], Edge_Net_Subnet2[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,2], ~Edge_Net_Subnet2[x,y+1,2,0,mask,2]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,2], Edge_Net_Subnet2[x,y-2,2,0,mask,2], Edge_Net_Subnet2[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,2], And(Edge_Net_Subnet2[x,y+1,2,0,mask,2], Edge_Net_Subnet2[x,y+2,2,0,mask,2], Edge_Net_Subnet2[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,2], And(Edge_Net_Subnet2[x,y-1,2,0,mask,2], Edge_Net_Subnet2[x,y-2,2,0,mask,2], Edge_Net_Subnet2[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,2], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,2], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,2], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,2], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,2], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(6,14+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,2], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(6,14+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet2_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,2], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,2], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet2_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,2], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(6,14+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,2], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(6,14+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,2], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,2], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,2], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,2], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(6,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,2], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,2], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,2], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,2], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,2], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,2], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet2_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,2], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,2], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet2_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,2], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,2], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,14+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet2_DR = And(Net2_Subnet2_DR_Trend, Net2_Subnet2_DR_GIL_HorMinWidth,Net2_Subnet2_DR_GIL_HorMinSpacing,Net2_Subnet2_DR_GIL_VerMinSpacing,Net2_Subnet2_DR_AIL2_VerMinWidth,Net2_Subnet2_DR_AIL2_VerMinSpacing,Net2_Subnet2_DR_VerAIL2_HorMinSpacing,Net2_Subnet2_DR_MINT1AB_HorMinWidth,Net2_Subnet2_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet2_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet2_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet2_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet2_DR_M1AB_MinWidth,Net2_Subnet2_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet2_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet2_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet2_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet2_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet2_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet2_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet2_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet2_DR_V0_HorMinSpacing,Net2_Subnet2_DR_V1_HorMinSpacing,Net2_Subnet2_DR_V0_VerMinSpacing,Net2_Subnet2_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet2_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[10,1,0,0, 10,2,0,0, 10,3,0,0, 10,4,0,0, 10,5,0,0, 10,6,0,0, 10,7,0,0, 10,8,0,0, 10,9,0,0, 10,10,0,0, 10,11,0,0, 10,12,0,0, 10,13,0,0, 10,14,0,0, ],14,6,0,1,14,35,3,2),
	RConstraints.R1(Edge_Net_Subnet2,[10,20,0,0, 10,21,0,0, 10,22,0,0, 10,23,0,0, 10,24,0,0, 10,25,0,0, 10,26,0,0, 10,27,0,0, 10,28,0,0, 10,29,0,0, 10,30,0,0, 10,31,0,0, 10,32,0,0, 10,33,0,0, ],14,6,0,1,14,35,3,2),
	).to_cnf()
Net2_Subnet2_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[10,1,0, 10,2,0, 10,3,0, 10,4,0, 10,5,0, 10,6,0, 10,7,0, 10,8,0, 10,9,0, 10,10,0, 10,11,0, 10,12,0, 10,13,0, 10,14,0, 10,15,0, 10,20,0, 10,21,0, 10,22,0, 10,23,0, 10,24,0, 10,25,0, 10,26,0, 10,27,0, 10,28,0, 10,29,0, 10,30,0, 10,31,0, 10,32,0, 10,33,0, 10,34,0, ],30,6,0,0,14,35,3,2,1),
	)
Net2_Subnet2_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,2+1)])for x in range(6,14+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet2_R = And(Net2_Subnet2_R1,Net2_Subnet2_R2,Net2_Subnet2_R3,)
Net2_Subnet2_Formula = And(Net2_Subnet2_C,Net2_Subnet2_DR,Net2_Subnet2_R)
# Net = 2 Subnet = 3 | Left -> Right [6,20] Top -> Bottom [0,35]
# Range R1(10,10,1,14)
# Range R2(16,16,0,35)
### Disable edges outside window
Edge_Net_Subnet2[0:6,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(7776)
Edge_Net_Subnet2[20:41+1,0:35+1,0:3+1,0:2+1,0:2+1,3]=exprzeros(28512)

### Consistency Constraints
Net2_Subnet3_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(6,20+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet3_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,3]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(6,20+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet3_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,3],Xor(Edge_Net_Subnet2[x,y,2,trend,1,3],Edge_Net_Subnet2[x,y,2,trend,2,3])),And(~Edge_Net_Subnet2[x,y,2,trend,0,3],~Edge_Net_Subnet2[x,y,2,trend,1,3],~Edge_Net_Subnet2[x,y,2,trend,2,3]))for x in range(6,20+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet3_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,3],Xor(Edge_Net_Subnet2[x,y,3,1,1,3],Edge_Net_Subnet2[x,y,3,1,2,3])),And(~Edge_Net_Subnet2[x,y,3,1,0,3],~Edge_Net_Subnet2[x,y,3,1,1,3],~Edge_Net_Subnet2[x,y,3,1,2,3]))for x in range(6,20+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet3_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,3],Xor(Edge_Net_Subnet2[x,y,1,trend,0,3],Edge_Net_Subnet2[x,y,1,trend,1,3])),And(~Edge_Net_Subnet2[x,y,1,trend,2,3],~Edge_Net_Subnet2[x,y,1,trend,0,3],~Edge_Net_Subnet2[x,y,1,trend,1,3]))for x in range(6,20+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet3_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(6,20+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,3], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(3+1,10)]))for trend in range(0,1+1)])for x in range(6,20+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,3)]))for trend in range(0,1+1)])for x in range(6,20+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,3], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(3+1,10)]))for trend in range(0,1+1)])for x in range(6,20+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet3_C = And(Net2_Subnet3_C1, Net2_Subnet3_C2,Net2_Subnet3_C3_ME1_Mask,Net2_Subnet3_C4_MINT1_Mask,Net2_Subnet3_C5_AIL2GIL_Mask,Net2_Subnet3_C6,)
### Design Rules
Net2_Subnet3_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(6,20+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet3_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,3], ~Edge_Net_Subnet2[x-1,y,1,1,1,3]), And(Edge_Net_Subnet2[x+1,y,1,1,1,3], Edge_Net_Subnet2[x+2,y,1,1,1,3], Edge_Net_Subnet2[x+3,y,1,1,1,3], ))for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,3], ~Edge_Net_Subnet2[x+1,y,1,1,1,3]), And(Edge_Net_Subnet2[x-1,y,1,1,1,3], Edge_Net_Subnet2[x-2,y,1,1,1,3], Edge_Net_Subnet2[x-3,y,1,1,1,3], ))for x in range(6,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,3], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,3], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(6,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,3], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(6,20+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,3], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(6,20+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3]), And(Edge_Net_Subnet2[x,y+1,1,0,0,3], Edge_Net_Subnet2[x,y+2,1,0,0,3], Edge_Net_Subnet2[x,y+3,1,0,0,3], ))for x in range(6,20+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3]), And(Edge_Net_Subnet2[x,y-1,1,0,0,3], Edge_Net_Subnet2[x,y-2,1,0,0,3], Edge_Net_Subnet2[x,y-3,1,0,0,3], ))for x in range(6,20+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge_Net_Subnet2[x,y-1,1,0,0,3]), And(Edge_Net_Subnet2[x,y+1,1,0,0,3], Edge_Net_Subnet2[x,y+2,1,0,0,3], Edge_Net_Subnet2[x,y+3,1,0,0,3], ))for x in range(6,20+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge_Net_Subnet2[x,y+1,1,0,0,3]), And(Edge_Net_Subnet2[x,y-1,1,0,0,3], Edge_Net_Subnet2[x,y-2,1,0,0,3], Edge_Net_Subnet2[x,y-3,1,0,0,3], ))for x in range(6,20+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet3_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(6,20+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(6,20+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(6,20+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(6,20+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(6,20+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,3], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(6,20+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet3_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,3], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,3], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(6,20+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,3], ~Edge_Net_Subnet2[x-1,y,3,1,mask,3]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,3], Edge_Net_Subnet2[x+2,y,3,1,mask,3], Edge_Net_Subnet2[x+3,y,3,1,mask,3], Edge_Net_Subnet2[x+4,y,3,1,mask,3], Edge_Net_Subnet2[x+5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,3], ~Edge_Net_Subnet2[x+1,y,3,1,mask,3]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,3], Edge_Net_Subnet2[x-2,y,3,1,mask,3], Edge_Net_Subnet2[x-3,y,3,1,mask,3], Edge_Net_Subnet2[x-4,y,3,1,mask,3], Edge_Net_Subnet2[x-5,y,3,1,mask,3], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,3], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,3], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,3], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,3], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,3], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(6,20+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,3], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(6,20+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,3], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,3], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(6,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,3], ~Edge_Net_Subnet2[x-1,y,2,1,mask,3]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,3], Edge_Net_Subnet2[x+2,y,2,1,mask,3], Edge_Net_Subnet2[x+3,y,2,1,mask,3], Edge_Net_Subnet2[x+4,y,2,1,mask,3], Edge_Net_Subnet2[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,3], ~Edge_Net_Subnet2[x+1,y,2,1,mask,3]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,3], Edge_Net_Subnet2[x-2,y,2,1,mask,3], Edge_Net_Subnet2[x-3,y,2,1,mask,3], Edge_Net_Subnet2[x-4,y,2,1,mask,3], Edge_Net_Subnet2[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,3], And(Edge_Net_Subnet2[x-1,y,2,1,mask,3], Edge_Net_Subnet2[x-2,y,2,1,mask,3], Edge_Net_Subnet2[x-3,y,2,1,mask,3], Edge_Net_Subnet2[x-4,y,2,1,mask,3], Edge_Net_Subnet2[x-5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(6,6+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,3], And(Edge_Net_Subnet2[x+1,y,2,1,mask,3], Edge_Net_Subnet2[x+2,y,2,1,mask,3], Edge_Net_Subnet2[x+3,y,2,1,mask,3], Edge_Net_Subnet2[x+4,y,2,1,mask,3], Edge_Net_Subnet2[x+5,y,2,1,mask,3], ))for mask in range(1,2+1)])for x in range(20-1,6)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,3], ~Edge_Net_Subnet2[x,y-1,2,0,mask,3]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,3], Edge_Net_Subnet2[x,y+2,2,0,mask,3], Edge_Net_Subnet2[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,3], ~Edge_Net_Subnet2[x,y+1,2,0,mask,3]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,3], Edge_Net_Subnet2[x,y-2,2,0,mask,3], Edge_Net_Subnet2[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,3], And(Edge_Net_Subnet2[x,y+1,2,0,mask,3], Edge_Net_Subnet2[x,y+2,2,0,mask,3], Edge_Net_Subnet2[x,y+3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,3], And(Edge_Net_Subnet2[x,y-1,2,0,mask,3], Edge_Net_Subnet2[x,y-2,2,0,mask,3], Edge_Net_Subnet2[x,y-3,2,0,mask,3], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,3], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,3], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(6,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,3], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,3], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,3], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(6,20+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,3], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(6,20+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet3_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,3], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,3], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet3_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,3], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(6,20+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,3], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(6,20+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,3], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,3], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,3], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,3], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(6,20+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,3], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,3], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(6,20+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,3], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,3], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,3], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,3], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,20+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet3_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,3], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,20+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,3], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(6,20+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet3_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,3], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,20+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,3], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(6,20+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet3_DR = And(Net2_Subnet3_DR_Trend, Net2_Subnet3_DR_GIL_HorMinWidth,Net2_Subnet3_DR_GIL_HorMinSpacing,Net2_Subnet3_DR_GIL_VerMinSpacing,Net2_Subnet3_DR_AIL2_VerMinWidth,Net2_Subnet3_DR_AIL2_VerMinSpacing,Net2_Subnet3_DR_VerAIL2_HorMinSpacing,Net2_Subnet3_DR_MINT1AB_HorMinWidth,Net2_Subnet3_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet3_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet3_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet3_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet3_DR_M1AB_MinWidth,Net2_Subnet3_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet3_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet3_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet3_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet3_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet3_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet3_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet3_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet3_DR_V0_HorMinSpacing,Net2_Subnet3_DR_V1_HorMinSpacing,Net2_Subnet3_DR_V0_VerMinSpacing,Net2_Subnet3_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet3_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[10,1,0,0, 10,2,0,0, 10,3,0,0, 10,4,0,0, 10,5,0,0, 10,6,0,0, 10,7,0,0, 10,8,0,0, 10,9,0,0, 10,10,0,0, 10,11,0,0, 10,12,0,0, 10,13,0,0, 10,14,0,0, ],14,6,0,1,20,35,3,3),
	RConstraints.R1(Edge_Net_Subnet2,[16,0,0,0, 16,1,0,0, 16,2,0,0, 16,3,0,0, 16,4,0,0, 16,5,0,0, 16,6,0,0, 16,7,0,0, 16,8,0,0, 16,9,0,0, 16,10,0,0, 16,11,0,0, 16,12,0,0, 16,13,0,0, 16,14,0,0, 16,15,0,0, 16,16,0,0, 16,17,0,0, 16,18,0,0, 16,19,0,0, 16,20,0,0, 16,21,0,0, 16,22,0,0, 16,23,0,0, 16,24,0,0, 16,25,0,0, 16,26,0,0, 16,27,0,0, 16,28,0,0, 16,29,0,0, 16,30,0,0, 16,31,0,0, 16,32,0,0, 16,33,0,0, 16,34,0,0, 16,35,0,0, ],36,6,0,1,20,35,3,3),
	).to_cnf()
Net2_Subnet3_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[10,1,0, 10,2,0, 10,3,0, 10,4,0, 10,5,0, 10,6,0, 10,7,0, 10,8,0, 10,9,0, 10,10,0, 10,11,0, 10,12,0, 10,13,0, 10,14,0, 10,15,0, 16,0,0, 16,1,0, 16,2,0, 16,3,0, 16,4,0, 16,5,0, 16,6,0, 16,7,0, 16,8,0, 16,9,0, 16,10,0, 16,11,0, 16,12,0, 16,13,0, 16,14,0, 16,15,0, 16,16,0, 16,17,0, 16,18,0, 16,19,0, 16,20,0, 16,21,0, 16,22,0, 16,23,0, 16,24,0, 16,25,0, 16,26,0, 16,27,0, 16,28,0, 16,29,0, 16,30,0, 16,31,0, 16,32,0, 16,33,0, 16,34,0, 16,35,0, ],51,6,0,0,20,35,3,3,1),
	)
Net2_Subnet3_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(6,20+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,2+1)])for x in range(6,20+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet3_R = And(Net2_Subnet3_R1,Net2_Subnet3_R2,Net2_Subnet3_R3,)
Net2_Subnet3_Formula = And(Net2_Subnet3_C,Net2_Subnet3_DR,Net2_Subnet3_R)
# Net = 2 Subnet = 5 | Left -> Right [12,24] Top -> Bottom [0,35]
# Range R1(16,16,0,35)
# Range R2(20,20,0,35)
### Disable edges outside window
Edge_Net_Subnet2[0:12,0:35+1,0:3+1,0:2+1,0:2+1,5]=exprzeros(15552)
Edge_Net_Subnet2[24:41+1,0:35+1,0:3+1,0:2+1,0:2+1,5]=exprzeros(23328)

### Consistency Constraints
Net2_Subnet5_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(12,24+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet5_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,5]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(12,24+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet5_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,5],Xor(Edge_Net_Subnet2[x,y,2,trend,1,5],Edge_Net_Subnet2[x,y,2,trend,2,5])),And(~Edge_Net_Subnet2[x,y,2,trend,0,5],~Edge_Net_Subnet2[x,y,2,trend,1,5],~Edge_Net_Subnet2[x,y,2,trend,2,5]))for x in range(12,24+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet5_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,5],Xor(Edge_Net_Subnet2[x,y,3,1,1,5],Edge_Net_Subnet2[x,y,3,1,2,5])),And(~Edge_Net_Subnet2[x,y,3,1,0,5],~Edge_Net_Subnet2[x,y,3,1,1,5],~Edge_Net_Subnet2[x,y,3,1,2,5]))for x in range(12,24+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet5_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,5],Xor(Edge_Net_Subnet2[x,y,1,trend,0,5],Edge_Net_Subnet2[x,y,1,trend,1,5])),And(~Edge_Net_Subnet2[x,y,1,trend,2,5],~Edge_Net_Subnet2[x,y,1,trend,0,5],~Edge_Net_Subnet2[x,y,1,trend,1,5]))for x in range(12,24+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet5_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,5], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,5)]))for trend in range(0,1+1)])for x in range(12,24+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,5], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(5+1,10)]))for trend in range(0,1+1)])for x in range(12,24+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,5], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,5)]))for trend in range(0,1+1)])for x in range(12,24+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,5], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(5+1,10)]))for trend in range(0,1+1)])for x in range(12,24+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet5_C = And(Net2_Subnet5_C1, Net2_Subnet5_C2,Net2_Subnet5_C3_ME1_Mask,Net2_Subnet5_C4_MINT1_Mask,Net2_Subnet5_C5_AIL2GIL_Mask,Net2_Subnet5_C6,)
### Design Rules
Net2_Subnet5_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(12,24+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet5_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,5], ~Edge_Net_Subnet2[x-1,y,1,1,1,5]), And(Edge_Net_Subnet2[x+1,y,1,1,1,5], Edge_Net_Subnet2[x+2,y,1,1,1,5], Edge_Net_Subnet2[x+3,y,1,1,1,5], ))for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,5], ~Edge_Net_Subnet2[x+1,y,1,1,1,5]), And(Edge_Net_Subnet2[x-1,y,1,1,1,5], Edge_Net_Subnet2[x-2,y,1,1,1,5], Edge_Net_Subnet2[x-3,y,1,1,1,5], ))for x in range(12,24+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,5], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,5], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(12,24+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,5], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(12,24+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,5], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(12,24+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5]), And(Edge_Net_Subnet2[x,y+1,1,0,0,5], Edge_Net_Subnet2[x,y+2,1,0,0,5], Edge_Net_Subnet2[x,y+3,1,0,0,5], ))for x in range(12,24+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5]), And(Edge_Net_Subnet2[x,y-1,1,0,0,5], Edge_Net_Subnet2[x,y-2,1,0,0,5], Edge_Net_Subnet2[x,y-3,1,0,0,5], ))for x in range(12,24+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge_Net_Subnet2[x,y-1,1,0,0,5]), And(Edge_Net_Subnet2[x,y+1,1,0,0,5], Edge_Net_Subnet2[x,y+2,1,0,0,5], Edge_Net_Subnet2[x,y+3,1,0,0,5], ))for x in range(12,24+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge_Net_Subnet2[x,y+1,1,0,0,5]), And(Edge_Net_Subnet2[x,y-1,1,0,0,5], Edge_Net_Subnet2[x,y-2,1,0,0,5], Edge_Net_Subnet2[x,y-3,1,0,0,5], ))for x in range(12,24+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet5_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(12,24+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(12,24+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(12,24+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(12,24+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(12,24+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,5], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(12,24+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet5_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,5], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,5], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(12,24+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,5], ~Edge_Net_Subnet2[x-1,y,3,1,mask,5]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,5], Edge_Net_Subnet2[x+2,y,3,1,mask,5], Edge_Net_Subnet2[x+3,y,3,1,mask,5], Edge_Net_Subnet2[x+4,y,3,1,mask,5], Edge_Net_Subnet2[x+5,y,3,1,mask,5], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,5], ~Edge_Net_Subnet2[x+1,y,3,1,mask,5]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,5], Edge_Net_Subnet2[x-2,y,3,1,mask,5], Edge_Net_Subnet2[x-3,y,3,1,mask,5], Edge_Net_Subnet2[x-4,y,3,1,mask,5], Edge_Net_Subnet2[x-5,y,3,1,mask,5], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,5], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,5], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,5], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,5], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,5], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(12,24+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,5], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(12,24+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,5], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,5], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(12,24+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,5], ~Edge_Net_Subnet2[x-1,y,2,1,mask,5]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,5], Edge_Net_Subnet2[x+2,y,2,1,mask,5], Edge_Net_Subnet2[x+3,y,2,1,mask,5], Edge_Net_Subnet2[x+4,y,2,1,mask,5], Edge_Net_Subnet2[x+5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,5], ~Edge_Net_Subnet2[x+1,y,2,1,mask,5]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,5], Edge_Net_Subnet2[x-2,y,2,1,mask,5], Edge_Net_Subnet2[x-3,y,2,1,mask,5], Edge_Net_Subnet2[x-4,y,2,1,mask,5], Edge_Net_Subnet2[x-5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,5], And(Edge_Net_Subnet2[x-1,y,2,1,mask,5], Edge_Net_Subnet2[x-2,y,2,1,mask,5], Edge_Net_Subnet2[x-3,y,2,1,mask,5], Edge_Net_Subnet2[x-4,y,2,1,mask,5], Edge_Net_Subnet2[x-5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(12,12+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,5], And(Edge_Net_Subnet2[x+1,y,2,1,mask,5], Edge_Net_Subnet2[x+2,y,2,1,mask,5], Edge_Net_Subnet2[x+3,y,2,1,mask,5], Edge_Net_Subnet2[x+4,y,2,1,mask,5], Edge_Net_Subnet2[x+5,y,2,1,mask,5], ))for mask in range(1,2+1)])for x in range(24-1,12)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,5], ~Edge_Net_Subnet2[x,y-1,2,0,mask,5]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,5], Edge_Net_Subnet2[x,y+2,2,0,mask,5], Edge_Net_Subnet2[x,y+3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,5], ~Edge_Net_Subnet2[x,y+1,2,0,mask,5]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,5], Edge_Net_Subnet2[x,y-2,2,0,mask,5], Edge_Net_Subnet2[x,y-3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,5], And(Edge_Net_Subnet2[x,y+1,2,0,mask,5], Edge_Net_Subnet2[x,y+2,2,0,mask,5], Edge_Net_Subnet2[x,y+3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,5], And(Edge_Net_Subnet2[x,y-1,2,0,mask,5], Edge_Net_Subnet2[x,y-2,2,0,mask,5], Edge_Net_Subnet2[x,y-3,2,0,mask,5], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,5], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,5], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(12,24+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,5], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,5], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,5], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(12,24+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,5], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(12,24+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet5_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,5], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,5], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet5_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,5], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(12,24+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,5], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(12,24+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,5], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,5], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,5], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,5], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(12,24+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,5], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,5], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(12,24+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,5], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,5], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,24+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,5], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,24+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,5], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,24+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet5_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,5], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,24+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,5], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(12,24+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet5_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,5], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,24+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,5], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(12,24+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet5_DR = And(Net2_Subnet5_DR_Trend, Net2_Subnet5_DR_GIL_HorMinWidth,Net2_Subnet5_DR_GIL_HorMinSpacing,Net2_Subnet5_DR_GIL_VerMinSpacing,Net2_Subnet5_DR_AIL2_VerMinWidth,Net2_Subnet5_DR_AIL2_VerMinSpacing,Net2_Subnet5_DR_VerAIL2_HorMinSpacing,Net2_Subnet5_DR_MINT1AB_HorMinWidth,Net2_Subnet5_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet5_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet5_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet5_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet5_DR_M1AB_MinWidth,Net2_Subnet5_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet5_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet5_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet5_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet5_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet5_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet5_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet5_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet5_DR_V0_HorMinSpacing,Net2_Subnet5_DR_V1_HorMinSpacing,Net2_Subnet5_DR_V0_VerMinSpacing,Net2_Subnet5_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet5_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[16,0,0,0, 16,1,0,0, 16,2,0,0, 16,3,0,0, 16,4,0,0, 16,5,0,0, 16,6,0,0, 16,7,0,0, 16,8,0,0, 16,9,0,0, 16,10,0,0, 16,11,0,0, 16,12,0,0, 16,13,0,0, 16,14,0,0, 16,15,0,0, 16,16,0,0, 16,17,0,0, 16,18,0,0, 16,19,0,0, 16,20,0,0, 16,21,0,0, 16,22,0,0, 16,23,0,0, 16,24,0,0, 16,25,0,0, 16,26,0,0, 16,27,0,0, 16,28,0,0, 16,29,0,0, 16,30,0,0, 16,31,0,0, 16,32,0,0, 16,33,0,0, 16,34,0,0, 16,35,0,0, ],36,12,0,1,24,35,3,5),
	RConstraints.R1(Edge_Net_Subnet2,[20,0,0,0, 20,1,0,0, 20,2,0,0, 20,3,0,0, 20,4,0,0, 20,5,0,0, 20,6,0,0, 20,7,0,0, 20,8,0,0, 20,9,0,0, 20,10,0,0, 20,11,0,0, 20,12,0,0, 20,13,0,0, 20,14,0,0, 20,15,0,0, 20,16,0,0, 20,17,0,0, 20,18,0,0, 20,19,0,0, 20,20,0,0, 20,21,0,0, 20,22,0,0, 20,23,0,0, 20,24,0,0, 20,25,0,0, 20,26,0,0, 20,27,0,0, 20,28,0,0, 20,29,0,0, 20,30,0,0, 20,31,0,0, 20,32,0,0, 20,33,0,0, 20,34,0,0, 20,35,0,0, ],36,12,0,1,24,35,3,5),
	).to_cnf()
Net2_Subnet5_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[16,0,0, 16,1,0, 16,2,0, 16,3,0, 16,4,0, 16,5,0, 16,6,0, 16,7,0, 16,8,0, 16,9,0, 16,10,0, 16,11,0, 16,12,0, 16,13,0, 16,14,0, 16,15,0, 16,16,0, 16,17,0, 16,18,0, 16,19,0, 16,20,0, 16,21,0, 16,22,0, 16,23,0, 16,24,0, 16,25,0, 16,26,0, 16,27,0, 16,28,0, 16,29,0, 16,30,0, 16,31,0, 16,32,0, 16,33,0, 16,34,0, 16,35,0, 20,0,0, 20,1,0, 20,2,0, 20,3,0, 20,4,0, 20,5,0, 20,6,0, 20,7,0, 20,8,0, 20,9,0, 20,10,0, 20,11,0, 20,12,0, 20,13,0, 20,14,0, 20,15,0, 20,16,0, 20,17,0, 20,18,0, 20,19,0, 20,20,0, 20,21,0, 20,22,0, 20,23,0, 20,24,0, 20,25,0, 20,26,0, 20,27,0, 20,28,0, 20,29,0, 20,30,0, 20,31,0, 20,32,0, 20,33,0, 20,34,0, 20,35,0, ],72,12,0,0,24,35,3,5,1),
	)
Net2_Subnet5_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(12,24+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,2+1)])for x in range(12,24+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet5_R = And(Net2_Subnet5_R1,Net2_Subnet5_R2,Net2_Subnet5_R3,)
Net2_Subnet5_Formula = And(Net2_Subnet5_C,Net2_Subnet5_DR,Net2_Subnet5_R)
# Net = 2 Subnet = 7 | Left -> Right [16,28] Top -> Bottom [0,35]
# Range R1(20,20,0,35)
# Range R2(24,24,0,35)
### Disable edges outside window
Edge_Net_Subnet2[0:16,0:35+1,0:3+1,0:2+1,0:2+1,7]=exprzeros(20736)
Edge_Net_Subnet2[28:41+1,0:35+1,0:3+1,0:2+1,0:2+1,7]=exprzeros(18144)

### Consistency Constraints
Net2_Subnet7_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet7_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,7]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet7_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,7],Xor(Edge_Net_Subnet2[x,y,2,trend,1,7],Edge_Net_Subnet2[x,y,2,trend,2,7])),And(~Edge_Net_Subnet2[x,y,2,trend,0,7],~Edge_Net_Subnet2[x,y,2,trend,1,7],~Edge_Net_Subnet2[x,y,2,trend,2,7]))for x in range(16,28+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet7_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,7],Xor(Edge_Net_Subnet2[x,y,3,1,1,7],Edge_Net_Subnet2[x,y,3,1,2,7])),And(~Edge_Net_Subnet2[x,y,3,1,0,7],~Edge_Net_Subnet2[x,y,3,1,1,7],~Edge_Net_Subnet2[x,y,3,1,2,7]))for x in range(16,28+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet7_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,7],Xor(Edge_Net_Subnet2[x,y,1,trend,0,7],Edge_Net_Subnet2[x,y,1,trend,1,7])),And(~Edge_Net_Subnet2[x,y,1,trend,2,7],~Edge_Net_Subnet2[x,y,1,trend,0,7],~Edge_Net_Subnet2[x,y,1,trend,1,7]))for x in range(16,28+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet7_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,7], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,7)]))for trend in range(0,1+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,7], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(7+1,10)]))for trend in range(0,1+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,7], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,7)]))for trend in range(0,1+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,7], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(7+1,10)]))for trend in range(0,1+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet7_C = And(Net2_Subnet7_C1, Net2_Subnet7_C2,Net2_Subnet7_C3_ME1_Mask,Net2_Subnet7_C4_MINT1_Mask,Net2_Subnet7_C5_AIL2GIL_Mask,Net2_Subnet7_C6,)
### Design Rules
Net2_Subnet7_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(16,28+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet7_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,7], ~Edge_Net_Subnet2[x-1,y,1,1,1,7]), And(Edge_Net_Subnet2[x+1,y,1,1,1,7], Edge_Net_Subnet2[x+2,y,1,1,1,7], Edge_Net_Subnet2[x+3,y,1,1,1,7], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,7], ~Edge_Net_Subnet2[x+1,y,1,1,1,7]), And(Edge_Net_Subnet2[x-1,y,1,1,1,7], Edge_Net_Subnet2[x-2,y,1,1,1,7], Edge_Net_Subnet2[x-3,y,1,1,1,7], ))for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet7_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,7], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,7], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet7_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,7], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(16,28+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,7], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(16,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet7_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7]), And(Edge_Net_Subnet2[x,y+1,1,0,0,7], Edge_Net_Subnet2[x,y+2,1,0,0,7], Edge_Net_Subnet2[x,y+3,1,0,0,7], ))for x in range(16,28+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7]), And(Edge_Net_Subnet2[x,y-1,1,0,0,7], Edge_Net_Subnet2[x,y-2,1,0,0,7], Edge_Net_Subnet2[x,y-3,1,0,0,7], ))for x in range(16,28+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge_Net_Subnet2[x,y-1,1,0,0,7]), And(Edge_Net_Subnet2[x,y+1,1,0,0,7], Edge_Net_Subnet2[x,y+2,1,0,0,7], Edge_Net_Subnet2[x,y+3,1,0,0,7], ))for x in range(16,28+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge_Net_Subnet2[x,y+1,1,0,0,7]), And(Edge_Net_Subnet2[x,y-1,1,0,0,7], Edge_Net_Subnet2[x,y-2,1,0,0,7], Edge_Net_Subnet2[x,y-3,1,0,0,7], ))for x in range(16,28+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet7_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(16,28+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(16,28+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(16,28+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(16,28+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(16,28+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,7], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(16,28+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet7_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,7], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,7], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet7_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,7], ~Edge_Net_Subnet2[x-1,y,3,1,mask,7]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,7], Edge_Net_Subnet2[x+2,y,3,1,mask,7], Edge_Net_Subnet2[x+3,y,3,1,mask,7], Edge_Net_Subnet2[x+4,y,3,1,mask,7], Edge_Net_Subnet2[x+5,y,3,1,mask,7], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,7], ~Edge_Net_Subnet2[x+1,y,3,1,mask,7]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,7], Edge_Net_Subnet2[x-2,y,3,1,mask,7], Edge_Net_Subnet2[x-3,y,3,1,mask,7], Edge_Net_Subnet2[x-4,y,3,1,mask,7], Edge_Net_Subnet2[x-5,y,3,1,mask,7], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet7_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,7], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,7], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet7_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,7], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,7], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet7_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,7], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(16,28+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,7], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(16,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet7_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,7], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,7], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet7_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,7], ~Edge_Net_Subnet2[x-1,y,2,1,mask,7]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,7], Edge_Net_Subnet2[x+2,y,2,1,mask,7], Edge_Net_Subnet2[x+3,y,2,1,mask,7], Edge_Net_Subnet2[x+4,y,2,1,mask,7], Edge_Net_Subnet2[x+5,y,2,1,mask,7], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,7], ~Edge_Net_Subnet2[x+1,y,2,1,mask,7]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,7], Edge_Net_Subnet2[x-2,y,2,1,mask,7], Edge_Net_Subnet2[x-3,y,2,1,mask,7], Edge_Net_Subnet2[x-4,y,2,1,mask,7], Edge_Net_Subnet2[x-5,y,2,1,mask,7], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,7], And(Edge_Net_Subnet2[x-1,y,2,1,mask,7], Edge_Net_Subnet2[x-2,y,2,1,mask,7], Edge_Net_Subnet2[x-3,y,2,1,mask,7], Edge_Net_Subnet2[x-4,y,2,1,mask,7], Edge_Net_Subnet2[x-5,y,2,1,mask,7], ))for mask in range(1,2+1)])for x in range(16,16+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,7], And(Edge_Net_Subnet2[x+1,y,2,1,mask,7], Edge_Net_Subnet2[x+2,y,2,1,mask,7], Edge_Net_Subnet2[x+3,y,2,1,mask,7], Edge_Net_Subnet2[x+4,y,2,1,mask,7], Edge_Net_Subnet2[x+5,y,2,1,mask,7], ))for mask in range(1,2+1)])for x in range(28-1,16)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,7], ~Edge_Net_Subnet2[x,y-1,2,0,mask,7]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,7], Edge_Net_Subnet2[x,y+2,2,0,mask,7], Edge_Net_Subnet2[x,y+3,2,0,mask,7], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,7], ~Edge_Net_Subnet2[x,y+1,2,0,mask,7]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,7], Edge_Net_Subnet2[x,y-2,2,0,mask,7], Edge_Net_Subnet2[x,y-3,2,0,mask,7], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,7], And(Edge_Net_Subnet2[x,y+1,2,0,mask,7], Edge_Net_Subnet2[x,y+2,2,0,mask,7], Edge_Net_Subnet2[x,y+3,2,0,mask,7], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,7], And(Edge_Net_Subnet2[x,y-1,2,0,mask,7], Edge_Net_Subnet2[x,y-2,2,0,mask,7], Edge_Net_Subnet2[x,y-3,2,0,mask,7], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet7_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,7], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,7], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet7_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,7], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,7], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet7_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,7], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(16,28+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,7], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(16,28+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet7_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,7], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,7], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet7_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,7], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(16,28+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,7], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(16,28+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet7_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,7], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,7], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet7_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,7], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,7], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(16,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet7_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,7], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,7], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet7_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,7], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,7], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet7_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,7], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,7], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet7_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,7], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,7], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet7_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,7], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,7], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(16,28+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet7_DR = And(Net2_Subnet7_DR_Trend, Net2_Subnet7_DR_GIL_HorMinWidth,Net2_Subnet7_DR_GIL_HorMinSpacing,Net2_Subnet7_DR_GIL_VerMinSpacing,Net2_Subnet7_DR_AIL2_VerMinWidth,Net2_Subnet7_DR_AIL2_VerMinSpacing,Net2_Subnet7_DR_VerAIL2_HorMinSpacing,Net2_Subnet7_DR_MINT1AB_HorMinWidth,Net2_Subnet7_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet7_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet7_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet7_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet7_DR_M1AB_MinWidth,Net2_Subnet7_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet7_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet7_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet7_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet7_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet7_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet7_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet7_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet7_DR_V0_HorMinSpacing,Net2_Subnet7_DR_V1_HorMinSpacing,Net2_Subnet7_DR_V0_VerMinSpacing,Net2_Subnet7_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet7_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[20,0,0,0, 20,1,0,0, 20,2,0,0, 20,3,0,0, 20,4,0,0, 20,5,0,0, 20,6,0,0, 20,7,0,0, 20,8,0,0, 20,9,0,0, 20,10,0,0, 20,11,0,0, 20,12,0,0, 20,13,0,0, 20,14,0,0, 20,15,0,0, 20,16,0,0, 20,17,0,0, 20,18,0,0, 20,19,0,0, 20,20,0,0, 20,21,0,0, 20,22,0,0, 20,23,0,0, 20,24,0,0, 20,25,0,0, 20,26,0,0, 20,27,0,0, 20,28,0,0, 20,29,0,0, 20,30,0,0, 20,31,0,0, 20,32,0,0, 20,33,0,0, 20,34,0,0, 20,35,0,0, ],36,16,0,1,28,35,3,7),
	RConstraints.R1(Edge_Net_Subnet2,[24,0,0,0, 24,1,0,0, 24,2,0,0, 24,3,0,0, 24,4,0,0, 24,5,0,0, 24,6,0,0, 24,7,0,0, 24,8,0,0, 24,9,0,0, 24,10,0,0, 24,11,0,0, 24,12,0,0, 24,13,0,0, 24,14,0,0, 24,15,0,0, 24,16,0,0, 24,17,0,0, 24,18,0,0, 24,19,0,0, 24,20,0,0, 24,21,0,0, 24,22,0,0, 24,23,0,0, 24,24,0,0, 24,25,0,0, 24,26,0,0, 24,27,0,0, 24,28,0,0, 24,29,0,0, 24,30,0,0, 24,31,0,0, 24,32,0,0, 24,33,0,0, 24,34,0,0, 24,35,0,0, ],36,16,0,1,28,35,3,7),
	).to_cnf()
Net2_Subnet7_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[20,0,0, 20,1,0, 20,2,0, 20,3,0, 20,4,0, 20,5,0, 20,6,0, 20,7,0, 20,8,0, 20,9,0, 20,10,0, 20,11,0, 20,12,0, 20,13,0, 20,14,0, 20,15,0, 20,16,0, 20,17,0, 20,18,0, 20,19,0, 20,20,0, 20,21,0, 20,22,0, 20,23,0, 20,24,0, 20,25,0, 20,26,0, 20,27,0, 20,28,0, 20,29,0, 20,30,0, 20,31,0, 20,32,0, 20,33,0, 20,34,0, 20,35,0, 24,0,0, 24,1,0, 24,2,0, 24,3,0, 24,4,0, 24,5,0, 24,6,0, 24,7,0, 24,8,0, 24,9,0, 24,10,0, 24,11,0, 24,12,0, 24,13,0, 24,14,0, 24,15,0, 24,16,0, 24,17,0, 24,18,0, 24,19,0, 24,20,0, 24,21,0, 24,22,0, 24,23,0, 24,24,0, 24,25,0, 24,26,0, 24,27,0, 24,28,0, 24,29,0, 24,30,0, 24,31,0, 24,32,0, 24,33,0, 24,34,0, 24,35,0, ],72,16,0,0,28,35,3,7,1),
	)
Net2_Subnet7_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,2+1)])for x in range(16,28+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet7_R = And(Net2_Subnet7_R1,Net2_Subnet7_R2,Net2_Subnet7_R3,)
Net2_Subnet7_Formula = And(Net2_Subnet7_C,Net2_Subnet7_DR,Net2_Subnet7_R)
# Net = 2 Subnet = 8 | Left -> Right [20,32] Top -> Bottom [0,35]
# Range R1(24,24,0,35)
# Range R2(28,28,0,35)
### Disable edges outside window
Edge_Net_Subnet2[0:20,0:35+1,0:3+1,0:2+1,0:2+1,8]=exprzeros(25920)
Edge_Net_Subnet2[32:41+1,0:35+1,0:3+1,0:2+1,0:2+1,8]=exprzeros(12960)

### Consistency Constraints
Net2_Subnet8_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,1]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(20,32+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet8_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet2[x,y,z,trend,mask,8]), Edge_Net[x,y,z,trend,mask,1])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(20,32+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net2_Subnet8_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,2,trend,0,8],Xor(Edge_Net_Subnet2[x,y,2,trend,1,8],Edge_Net_Subnet2[x,y,2,trend,2,8])),And(~Edge_Net_Subnet2[x,y,2,trend,0,8],~Edge_Net_Subnet2[x,y,2,trend,1,8],~Edge_Net_Subnet2[x,y,2,trend,2,8]))for x in range(20,32+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet8_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,3,1,0,8],Xor(Edge_Net_Subnet2[x,y,3,1,1,8],Edge_Net_Subnet2[x,y,3,1,2,8])),And(~Edge_Net_Subnet2[x,y,3,1,0,8],~Edge_Net_Subnet2[x,y,3,1,1,8],~Edge_Net_Subnet2[x,y,3,1,2,8]))for x in range(20,32+1)])for y in range(0,35+1)]).to_cnf()
Net2_Subnet8_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet2[x,y,1,trend,2,8],Xor(Edge_Net_Subnet2[x,y,1,trend,0,8],Edge_Net_Subnet2[x,y,1,trend,1,8])),And(~Edge_Net_Subnet2[x,y,1,trend,2,8],~Edge_Net_Subnet2[x,y,1,trend,0,8],~Edge_Net_Subnet2[x,y,1,trend,1,8]))for x in range(20,32+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net2_Subnet8_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,8], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(0,8)]))for trend in range(0,1+1)])for x in range(20,32+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,1,8], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,2,s2])for s2 in range(8+1,10)]))for trend in range(0,1+1)])for x in range(20,32+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,8], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(0,8)]))for trend in range(0,1+1)])for x in range(20,32+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,z,trend,2,8], And(*[And(~Edge_Net_Subnet2[x,y,z,trend,1,s2])for s2 in range(8+1,10)]))for trend in range(0,1+1)])for x in range(20,32+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net2_Subnet8_C = And(Net2_Subnet8_C1, Net2_Subnet8_C2,Net2_Subnet8_C3_ME1_Mask,Net2_Subnet8_C4_MINT1_Mask,Net2_Subnet8_C5_AIL2GIL_Mask,Net2_Subnet8_C6,)
### Design Rules
Net2_Subnet8_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(20,32+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net2_Subnet8_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,8], ~Edge_Net_Subnet2[x-1,y,1,1,1,8]), And(Edge_Net_Subnet2[x+1,y,1,1,1,8], Edge_Net_Subnet2[x+2,y,1,1,1,8], Edge_Net_Subnet2[x+3,y,1,1,1,8], ))for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,1,1,1,8], ~Edge_Net_Subnet2[x+1,y,1,1,1,8]), And(Edge_Net_Subnet2[x-1,y,1,1,1,8], Edge_Net_Subnet2[x-2,y,1,1,1,8], Edge_Net_Subnet2[x-3,y,1,1,1,8], ))for x in range(20,32+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet8_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,8], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,1,1,8], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(20,32+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet8_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,8], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(20,32+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,1,1,8], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(20,32+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet8_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8]), And(Edge_Net_Subnet2[x,y+1,1,0,0,8], Edge_Net_Subnet2[x,y+2,1,0,0,8], Edge_Net_Subnet2[x,y+3,1,0,0,8], ))for x in range(20,32+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8]), And(Edge_Net_Subnet2[x,y-1,1,0,0,8], Edge_Net_Subnet2[x,y-2,1,0,0,8], Edge_Net_Subnet2[x,y-3,1,0,0,8], ))for x in range(20,32+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge_Net_Subnet2[x,y-1,1,0,0,8]), And(Edge_Net_Subnet2[x,y+1,1,0,0,8], Edge_Net_Subnet2[x,y+2,1,0,0,8], Edge_Net_Subnet2[x,y+3,1,0,0,8], ))for x in range(20,32+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge_Net_Subnet2[x,y+1,1,0,0,8]), And(Edge_Net_Subnet2[x,y-1,1,0,0,8], Edge_Net_Subnet2[x,y-2,1,0,0,8], Edge_Net_Subnet2[x,y-3,1,0,0,8], ))for x in range(20,32+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net2_Subnet8_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(20,32+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(20,32+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(20,32+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(20,32+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(20,32+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,1,0,0,8], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(20,32+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net2_Subnet8_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,8], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,0,0,8], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(20,32+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet8_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,8], ~Edge_Net_Subnet2[x-1,y,3,1,mask,8]), And(Edge_Net_Subnet2[x+1,y,3,1,mask,8], Edge_Net_Subnet2[x+2,y,3,1,mask,8], Edge_Net_Subnet2[x+3,y,3,1,mask,8], Edge_Net_Subnet2[x+4,y,3,1,mask,8], Edge_Net_Subnet2[x+5,y,3,1,mask,8], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,3,1,mask,8], ~Edge_Net_Subnet2[x+1,y,3,1,mask,8]), And(Edge_Net_Subnet2[x-1,y,3,1,mask,8], Edge_Net_Subnet2[x-2,y,3,1,mask,8], Edge_Net_Subnet2[x-3,y,3,1,mask,8], Edge_Net_Subnet2[x-4,y,3,1,mask,8], Edge_Net_Subnet2[x-5,y,3,1,mask,8], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet8_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,8], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,mask,8], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet8_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,8], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,mask,8], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet8_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,8], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(20,32+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,3,1,1,8], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(20,32+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet8_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,8], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,3,1,1,8], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(20,32+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet8_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,8], ~Edge_Net_Subnet2[x-1,y,2,1,mask,8]), And(Edge_Net_Subnet2[x+1,y,2,1,mask,8], Edge_Net_Subnet2[x+2,y,2,1,mask,8], Edge_Net_Subnet2[x+3,y,2,1,mask,8], Edge_Net_Subnet2[x+4,y,2,1,mask,8], Edge_Net_Subnet2[x+5,y,2,1,mask,8], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet2[x,y,2,1,mask,8], ~Edge_Net_Subnet2[x+1,y,2,1,mask,8]), And(Edge_Net_Subnet2[x-1,y,2,1,mask,8], Edge_Net_Subnet2[x-2,y,2,1,mask,8], Edge_Net_Subnet2[x-3,y,2,1,mask,8], Edge_Net_Subnet2[x-4,y,2,1,mask,8], Edge_Net_Subnet2[x-5,y,2,1,mask,8], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,8], And(Edge_Net_Subnet2[x-1,y,2,1,mask,8], Edge_Net_Subnet2[x-2,y,2,1,mask,8], Edge_Net_Subnet2[x-3,y,2,1,mask,8], Edge_Net_Subnet2[x-4,y,2,1,mask,8], Edge_Net_Subnet2[x-5,y,2,1,mask,8], ))for mask in range(1,2+1)])for x in range(20,20+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,8], And(Edge_Net_Subnet2[x+1,y,2,1,mask,8], Edge_Net_Subnet2[x+2,y,2,1,mask,8], Edge_Net_Subnet2[x+3,y,2,1,mask,8], Edge_Net_Subnet2[x+4,y,2,1,mask,8], Edge_Net_Subnet2[x+5,y,2,1,mask,8], ))for mask in range(1,2+1)])for x in range(32-1,20)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,8], ~Edge_Net_Subnet2[x,y-1,2,0,mask,8]), And(Edge_Net_Subnet2[x,y+1,2,0,mask,8], Edge_Net_Subnet2[x,y+2,2,0,mask,8], Edge_Net_Subnet2[x,y+3,2,0,mask,8], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,8], ~Edge_Net_Subnet2[x,y+1,2,0,mask,8]), And(Edge_Net_Subnet2[x,y-1,2,0,mask,8], Edge_Net_Subnet2[x,y-2,2,0,mask,8], Edge_Net_Subnet2[x,y-3,2,0,mask,8], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,8], And(Edge_Net_Subnet2[x,y+1,2,0,mask,8], Edge_Net_Subnet2[x,y+2,2,0,mask,8], Edge_Net_Subnet2[x,y+3,2,0,mask,8], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet2[x,y,2,0,mask,8], And(Edge_Net_Subnet2[x,y-1,2,0,mask,8], Edge_Net_Subnet2[x,y-2,2,0,mask,8], Edge_Net_Subnet2[x,y-3,2,0,mask,8], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(35,35+1)]),
	).to_cnf()
Net2_Subnet8_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,8], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,1,8], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(20,32+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet8_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,8], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,1,mask,8], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet8_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,8], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(20,32+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,1,8], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(20,32+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net2_Subnet8_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,8], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet2[x,y,2,0,mask,8], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net2_Subnet8_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,8], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(20,32+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,1,8], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(20,32+1)])for y in range(3,35+1)]),
	).to_cnf()
Net2_Subnet8_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,8], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,1,mask,8], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(4,35+1)]),
	).to_cnf()
Net2_Subnet8_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,8], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,1,8], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(20,32+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet8_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,8], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,0,mask,8], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(20,32+1)])for y in range(0,35+1)]),
	).to_cnf()
Net2_Subnet8_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,8], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,1,2,mask,8], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,32+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet8_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,8], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,32+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet2[x,y,2,2,mask,8], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,32+1)])for y in range(0,35+1)])
	).to_cnf()
Net2_Subnet8_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,8], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,32+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,1,2,mask,8], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(20,32+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet8_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,8], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,32+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet2[x,y,2,2,mask,8], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(20,32+1)])for y in range(2,35+1)]),
	).to_cnf()
Net2_Subnet8_DR = And(Net2_Subnet8_DR_Trend, Net2_Subnet8_DR_GIL_HorMinWidth,Net2_Subnet8_DR_GIL_HorMinSpacing,Net2_Subnet8_DR_GIL_VerMinSpacing,Net2_Subnet8_DR_AIL2_VerMinWidth,Net2_Subnet8_DR_AIL2_VerMinSpacing,Net2_Subnet8_DR_VerAIL2_HorMinSpacing,Net2_Subnet8_DR_MINT1AB_HorMinWidth,Net2_Subnet8_DR_MINT1_SameMask_VerMinSpacing,Net2_Subnet8_DR_MINT1_SameMask_HorMinSpacing,Net2_Subnet8_DR_MINT1_DiffMask_VerMinSpacing,Net2_Subnet8_DR_MINT1_DiffMask_HorMinSpacing,Net2_Subnet8_DR_M1AB_MinWidth,Net2_Subnet8_DR_HorM1_DiffMask_HorMinSpacing,Net2_Subnet8_DR_HorM1_SameMask_HorMinSpacing,Net2_Subnet8_DR_VerM1_DiffMask_VerMinSpacing,Net2_Subnet8_DR_VerM1_SameMask_VerMinSpacing,Net2_Subnet8_DR_HorM1_DiffMask_VerMinSpacing,Net2_Subnet8_DR_HorM1_SameMask_VerMinSpacing,Net2_Subnet8_DR_VerM1_DiffMask_HorMinSpacing,Net2_Subnet8_DR_VerM1_SameMask_HorMinSpacing,Net2_Subnet8_DR_V0_HorMinSpacing,Net2_Subnet8_DR_V1_HorMinSpacing,Net2_Subnet8_DR_V0_VerMinSpacing,Net2_Subnet8_DR_V1_VerMinSpacing,)
### Routability Constraints
Net2_Subnet8_R1 = And(
	RConstraints.R1(Edge_Net_Subnet2,[24,0,0,0, 24,1,0,0, 24,2,0,0, 24,3,0,0, 24,4,0,0, 24,5,0,0, 24,6,0,0, 24,7,0,0, 24,8,0,0, 24,9,0,0, 24,10,0,0, 24,11,0,0, 24,12,0,0, 24,13,0,0, 24,14,0,0, 24,15,0,0, 24,16,0,0, 24,17,0,0, 24,18,0,0, 24,19,0,0, 24,20,0,0, 24,21,0,0, 24,22,0,0, 24,23,0,0, 24,24,0,0, 24,25,0,0, 24,26,0,0, 24,27,0,0, 24,28,0,0, 24,29,0,0, 24,30,0,0, 24,31,0,0, 24,32,0,0, 24,33,0,0, 24,34,0,0, 24,35,0,0, ],36,20,0,1,32,35,3,8),
	RConstraints.R1(Edge_Net_Subnet2,[28,0,0,0, 28,1,0,0, 28,2,0,0, 28,3,0,0, 28,4,0,0, 28,5,0,0, 28,6,0,0, 28,7,0,0, 28,8,0,0, 28,9,0,0, 28,10,0,0, 28,11,0,0, 28,12,0,0, 28,13,0,0, 28,14,0,0, 28,15,0,0, 28,16,0,0, 28,17,0,0, 28,18,0,0, 28,19,0,0, 28,20,0,0, 28,21,0,0, 28,22,0,0, 28,23,0,0, 28,24,0,0, 28,25,0,0, 28,26,0,0, 28,27,0,0, 28,28,0,0, 28,29,0,0, 28,30,0,0, 28,31,0,0, 28,32,0,0, 28,33,0,0, 28,34,0,0, 28,35,0,0, ],36,20,0,1,32,35,3,8),
	).to_cnf()
Net2_Subnet8_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet2,Edge,Edge_Net,[24,0,0, 24,1,0, 24,2,0, 24,3,0, 24,4,0, 24,5,0, 24,6,0, 24,7,0, 24,8,0, 24,9,0, 24,10,0, 24,11,0, 24,12,0, 24,13,0, 24,14,0, 24,15,0, 24,16,0, 24,17,0, 24,18,0, 24,19,0, 24,20,0, 24,21,0, 24,22,0, 24,23,0, 24,24,0, 24,25,0, 24,26,0, 24,27,0, 24,28,0, 24,29,0, 24,30,0, 24,31,0, 24,32,0, 24,33,0, 24,34,0, 24,35,0, 28,0,0, 28,1,0, 28,2,0, 28,3,0, 28,4,0, 28,5,0, 28,6,0, 28,7,0, 28,8,0, 28,9,0, 28,10,0, 28,11,0, 28,12,0, 28,13,0, 28,14,0, 28,15,0, 28,16,0, 28,17,0, 28,18,0, 28,19,0, 28,20,0, 28,21,0, 28,22,0, 28,23,0, 28,24,0, 28,25,0, 28,26,0, 28,27,0, 28,28,0, 28,29,0, 28,30,0, 28,31,0, 28,32,0, 28,33,0, 28,34,0, 28,35,0, ],72,20,0,0,32,35,3,8,1),
	)
Net2_Subnet8_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,0+1)])for x in range(20,32+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,1],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(2,2+1)])for x in range(20,32+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)])	).to_cnf()
Net2_Subnet8_R = And(Net2_Subnet8_R1,Net2_Subnet8_R2,Net2_Subnet8_R3,)
Net2_Subnet8_Formula = And(Net2_Subnet8_C,Net2_Subnet8_DR,Net2_Subnet8_R)
# Net = 3 Subnet = 0 | Left -> Right [14,22] Top -> Bottom [0,35]
# Range R1(18,18,1,14)
# Range R2(18,18,20,33)
### Disable edges outside window
Edge_Net_Subnet3[0:14,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(18144)
Edge_Net_Subnet3[22:41+1,0:35+1,0:3+1,0:2+1,0:2+1,0]=exprzeros(25920)

### Consistency Constraints
Net3_Subnet0_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(14,22+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet0_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,0]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(14,22+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet0_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,0],Xor(Edge_Net_Subnet3[x,y,2,trend,1,0],Edge_Net_Subnet3[x,y,2,trend,2,0])),And(~Edge_Net_Subnet3[x,y,2,trend,0,0],~Edge_Net_Subnet3[x,y,2,trend,1,0],~Edge_Net_Subnet3[x,y,2,trend,2,0]))for x in range(14,22+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet0_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,0],Xor(Edge_Net_Subnet3[x,y,3,1,1,0],Edge_Net_Subnet3[x,y,3,1,2,0])),And(~Edge_Net_Subnet3[x,y,3,1,0,0],~Edge_Net_Subnet3[x,y,3,1,1,0],~Edge_Net_Subnet3[x,y,3,1,2,0]))for x in range(14,22+1)])for y in range(0,35+1)]).to_cnf()
Net3_Subnet0_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,0],Xor(Edge_Net_Subnet3[x,y,1,trend,0,0],Edge_Net_Subnet3[x,y,1,trend,1,0])),And(~Edge_Net_Subnet3[x,y,1,trend,2,0],~Edge_Net_Subnet3[x,y,1,trend,0,0],~Edge_Net_Subnet3[x,y,1,trend,1,0]))for x in range(14,22+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet0_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,0], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0+1,3)]))for trend in range(0,1+1)])for x in range(14,22+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,0], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0+1,3)]))for trend in range(0,1+1)])for x in range(14,22+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet0_C = And(Net3_Subnet0_C1, Net3_Subnet0_C2,Net3_Subnet0_C3_ME1_Mask,Net3_Subnet0_C4_MINT1_Mask,Net3_Subnet0_C5_AIL2GIL_Mask,Net3_Subnet0_C6,)
### Design Rules
Net3_Subnet0_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(14,22+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet0_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge_Net_Subnet3[x-1,y,1,1,1,0]), And(Edge_Net_Subnet3[x+1,y,1,1,1,0], Edge_Net_Subnet3[x+2,y,1,1,1,0], Edge_Net_Subnet3[x+3,y,1,1,1,0], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge_Net_Subnet3[x+1,y,1,1,1,0]), And(Edge_Net_Subnet3[x-1,y,1,1,1,0], Edge_Net_Subnet3[x-2,y,1,1,1,0], Edge_Net_Subnet3[x-3,y,1,1,1,0], ))for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,0], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,0], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(14,22+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,0], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(14,22+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0]), And(Edge_Net_Subnet3[x,y+1,1,0,0,0], Edge_Net_Subnet3[x,y+2,1,0,0,0], Edge_Net_Subnet3[x,y+3,1,0,0,0], ))for x in range(14,22+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0]), And(Edge_Net_Subnet3[x,y-1,1,0,0,0], Edge_Net_Subnet3[x,y-2,1,0,0,0], Edge_Net_Subnet3[x,y-3,1,0,0,0], ))for x in range(14,22+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge_Net_Subnet3[x,y-1,1,0,0,0]), And(Edge_Net_Subnet3[x,y+1,1,0,0,0], Edge_Net_Subnet3[x,y+2,1,0,0,0], Edge_Net_Subnet3[x,y+3,1,0,0,0], ))for x in range(14,22+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge_Net_Subnet3[x,y+1,1,0,0,0]), And(Edge_Net_Subnet3[x,y-1,1,0,0,0], Edge_Net_Subnet3[x,y-2,1,0,0,0], Edge_Net_Subnet3[x,y-3,1,0,0,0], ))for x in range(14,22+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net3_Subnet0_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(14,22+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(14,22+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(14,22+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(14,22+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(14,22+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,0], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(14,22+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net3_Subnet0_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,0], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,0], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge_Net_Subnet3[x-1,y,3,1,mask,0]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,0], Edge_Net_Subnet3[x+2,y,3,1,mask,0], Edge_Net_Subnet3[x+3,y,3,1,mask,0], Edge_Net_Subnet3[x+4,y,3,1,mask,0], Edge_Net_Subnet3[x+5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge_Net_Subnet3[x+1,y,3,1,mask,0]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,0], Edge_Net_Subnet3[x-2,y,3,1,mask,0], Edge_Net_Subnet3[x-3,y,3,1,mask,0], Edge_Net_Subnet3[x-4,y,3,1,mask,0], Edge_Net_Subnet3[x-5,y,3,1,mask,0], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,0], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,0], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,0], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,0], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(14,22+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,0], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(14,22+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,0], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,0], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge_Net_Subnet3[x-1,y,2,1,mask,0]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,0], Edge_Net_Subnet3[x+2,y,2,1,mask,0], Edge_Net_Subnet3[x+3,y,2,1,mask,0], Edge_Net_Subnet3[x+4,y,2,1,mask,0], Edge_Net_Subnet3[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge_Net_Subnet3[x+1,y,2,1,mask,0]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,0], Edge_Net_Subnet3[x-2,y,2,1,mask,0], Edge_Net_Subnet3[x-3,y,2,1,mask,0], Edge_Net_Subnet3[x-4,y,2,1,mask,0], Edge_Net_Subnet3[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(Edge_Net_Subnet3[x-1,y,2,1,mask,0], Edge_Net_Subnet3[x-2,y,2,1,mask,0], Edge_Net_Subnet3[x-3,y,2,1,mask,0], Edge_Net_Subnet3[x-4,y,2,1,mask,0], Edge_Net_Subnet3[x-5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(14,14+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(Edge_Net_Subnet3[x+1,y,2,1,mask,0], Edge_Net_Subnet3[x+2,y,2,1,mask,0], Edge_Net_Subnet3[x+3,y,2,1,mask,0], Edge_Net_Subnet3[x+4,y,2,1,mask,0], Edge_Net_Subnet3[x+5,y,2,1,mask,0], ))for mask in range(1,2+1)])for x in range(22-1,14)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge_Net_Subnet3[x,y-1,2,0,mask,0]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,0], Edge_Net_Subnet3[x,y+2,2,0,mask,0], Edge_Net_Subnet3[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge_Net_Subnet3[x,y+1,2,0,mask,0]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,0], Edge_Net_Subnet3[x,y-2,2,0,mask,0], Edge_Net_Subnet3[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,0], And(Edge_Net_Subnet3[x,y+1,2,0,mask,0], Edge_Net_Subnet3[x,y+2,2,0,mask,0], Edge_Net_Subnet3[x,y+3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,0], And(Edge_Net_Subnet3[x,y-1,2,0,mask,0], Edge_Net_Subnet3[x,y-2,2,0,mask,0], Edge_Net_Subnet3[x,y-3,2,0,mask,0], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,0], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,0], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,0], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,0], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(14,22+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,0], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(14,22+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net3_Subnet0_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,0], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net3_Subnet0_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,0], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(14,22+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,0], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(14,22+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,0], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(4,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,0], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,0], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(14,22+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,0], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,0], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet0_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,0], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet0_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,0], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,22+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet0_DR = And(Net3_Subnet0_DR_Trend, Net3_Subnet0_DR_GIL_HorMinWidth,Net3_Subnet0_DR_GIL_HorMinSpacing,Net3_Subnet0_DR_GIL_VerMinSpacing,Net3_Subnet0_DR_AIL2_VerMinWidth,Net3_Subnet0_DR_AIL2_VerMinSpacing,Net3_Subnet0_DR_VerAIL2_HorMinSpacing,Net3_Subnet0_DR_MINT1AB_HorMinWidth,Net3_Subnet0_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet0_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet0_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet0_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet0_DR_M1AB_MinWidth,Net3_Subnet0_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet0_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet0_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet0_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet0_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet0_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet0_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet0_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet0_DR_V0_HorMinSpacing,Net3_Subnet0_DR_V1_HorMinSpacing,Net3_Subnet0_DR_V0_VerMinSpacing,Net3_Subnet0_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet0_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[18,1,0,0, 18,2,0,0, 18,3,0,0, 18,4,0,0, 18,5,0,0, 18,6,0,0, 18,7,0,0, 18,8,0,0, 18,9,0,0, 18,10,0,0, 18,11,0,0, 18,12,0,0, 18,13,0,0, 18,14,0,0, ],14,14,0,1,22,35,3,0),
	RConstraints.R1(Edge_Net_Subnet3,[18,20,0,0, 18,21,0,0, 18,22,0,0, 18,23,0,0, 18,24,0,0, 18,25,0,0, 18,26,0,0, 18,27,0,0, 18,28,0,0, 18,29,0,0, 18,30,0,0, 18,31,0,0, 18,32,0,0, 18,33,0,0, ],14,14,0,1,22,35,3,0),
	).to_cnf()
Net3_Subnet0_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[18,1,0, 18,2,0, 18,3,0, 18,4,0, 18,5,0, 18,6,0, 18,7,0, 18,8,0, 18,9,0, 18,10,0, 18,11,0, 18,12,0, 18,13,0, 18,14,0, 18,15,0, 18,20,0, 18,21,0, 18,22,0, 18,23,0, 18,24,0, 18,25,0, 18,26,0, 18,27,0, 18,28,0, 18,29,0, 18,30,0, 18,31,0, 18,32,0, 18,33,0, 18,34,0, ],30,14,0,0,22,35,3,0,2),
	)
Net3_Subnet0_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(14,22+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	).to_cnf()
Net3_Subnet0_R = And(Net3_Subnet0_R1,Net3_Subnet0_R2,Net3_Subnet0_R3,)
Net3_Subnet0_Formula = And(Net3_Subnet0_C,Net3_Subnet0_DR,Net3_Subnet0_R)
# Net = 3 Subnet = 1 | Left -> Right [14,30] Top -> Bottom [0,18]
# Range R1(18,18,1,14)
# Range R2(26,26,1,14)
### Disable edges outside window
Edge_Net_Subnet3[0:14,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(18144)
Edge_Net_Subnet3[14:30,18:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(10368)
Edge_Net_Subnet3[30:41+1,0:35+1,0:3+1,0:2+1,0:2+1,1]=exprzeros(15552)

### Consistency Constraints
Net3_Subnet1_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(14,30+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet1_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,1]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(14,30+1)])for y in range(0,18+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet1_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,1],Xor(Edge_Net_Subnet3[x,y,2,trend,1,1],Edge_Net_Subnet3[x,y,2,trend,2,1])),And(~Edge_Net_Subnet3[x,y,2,trend,0,1],~Edge_Net_Subnet3[x,y,2,trend,1,1],~Edge_Net_Subnet3[x,y,2,trend,2,1]))for x in range(14,30+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet1_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,1],Xor(Edge_Net_Subnet3[x,y,3,1,1,1],Edge_Net_Subnet3[x,y,3,1,2,1])),And(~Edge_Net_Subnet3[x,y,3,1,0,1],~Edge_Net_Subnet3[x,y,3,1,1,1],~Edge_Net_Subnet3[x,y,3,1,2,1]))for x in range(14,30+1)])for y in range(0,18+1)]).to_cnf()
Net3_Subnet1_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,1],Xor(Edge_Net_Subnet3[x,y,1,trend,0,1],Edge_Net_Subnet3[x,y,1,trend,1,1])),And(~Edge_Net_Subnet3[x,y,1,trend,2,1],~Edge_Net_Subnet3[x,y,1,trend,0,1],~Edge_Net_Subnet3[x,y,1,trend,1,1]))for x in range(14,30+1)])for y in range(0,18+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet1_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(14,30+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,1], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(14,30+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0,1)]))for trend in range(0,1+1)])for x in range(14,30+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,1], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(1+1,3)]))for trend in range(0,1+1)])for x in range(14,30+1)])for y in range(0,18+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet1_C = And(Net3_Subnet1_C1, Net3_Subnet1_C2,Net3_Subnet1_C3_ME1_Mask,Net3_Subnet1_C4_MINT1_Mask,Net3_Subnet1_C5_AIL2GIL_Mask,Net3_Subnet1_C6,)
### Design Rules
Net3_Subnet1_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(14,30+1)])for y in range(0,18+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet1_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,1], ~Edge_Net_Subnet3[x-1,y,1,1,1,1]), And(Edge_Net_Subnet3[x+1,y,1,1,1,1], Edge_Net_Subnet3[x+2,y,1,1,1,1], Edge_Net_Subnet3[x+3,y,1,1,1,1], ))for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,1], ~Edge_Net_Subnet3[x+1,y,1,1,1,1]), And(Edge_Net_Subnet3[x-1,y,1,1,1,1], Edge_Net_Subnet3[x-2,y,1,1,1,1], Edge_Net_Subnet3[x-3,y,1,1,1,1], ))for x in range(14,30+1)])for y in range(0,18+1)])
	).to_cnf()
Net3_Subnet1_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,1], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,1], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(14,30+1)])for y in range(0,18+1)])
	).to_cnf()
Net3_Subnet1_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,1], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,1], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(14,30+1)])for y in range(3,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1]), And(Edge_Net_Subnet3[x,y+1,1,0,0,1], Edge_Net_Subnet3[x,y+2,1,0,0,1], Edge_Net_Subnet3[x,y+3,1,0,0,1], ))for x in range(14,30+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1], ~Edge_Net_Subnet3[x,y-1,1,0,0,1]), And(Edge_Net_Subnet3[x,y+1,1,0,0,1], Edge_Net_Subnet3[x,y+2,1,0,0,1], Edge_Net_Subnet3[x,y+3,1,0,0,1], ))for x in range(14,30+1)])for y in range(0+1,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1], ~Edge_Net_Subnet3[x,y+1,1,0,0,1]), And(Edge_Net_Subnet3[x,y-1,1,0,0,1], Edge_Net_Subnet3[x,y-2,1,0,0,1], Edge_Net_Subnet3[x,y-3,1,0,0,1], ))for x in range(14,30+1)])for y in range(0+3,18+1)])
	).to_cnf()
Net3_Subnet1_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(14,30+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(14,30+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(14,30+1)])for y in range(0+3,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,1], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(14,30+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net3_Subnet1_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,1], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,1], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(14,30+1)])for y in range(0,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,1], ~Edge_Net_Subnet3[x-1,y,3,1,mask,1]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,1], Edge_Net_Subnet3[x+2,y,3,1,mask,1], Edge_Net_Subnet3[x+3,y,3,1,mask,1], Edge_Net_Subnet3[x+4,y,3,1,mask,1], Edge_Net_Subnet3[x+5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,1], ~Edge_Net_Subnet3[x+1,y,3,1,mask,1]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,1], Edge_Net_Subnet3[x-2,y,3,1,mask,1], Edge_Net_Subnet3[x-3,y,3,1,mask,1], Edge_Net_Subnet3[x-4,y,3,1,mask,1], Edge_Net_Subnet3[x-5,y,3,1,mask,1], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,1], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,1], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(3,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,1], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,1], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)])
	).to_cnf()
Net3_Subnet1_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,1], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,1], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(14,30+1)])for y in range(2,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,1], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,1], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(14,30+1)])for y in range(0,18+1)])
	).to_cnf()
Net3_Subnet1_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,1], ~Edge_Net_Subnet3[x-1,y,2,1,mask,1]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,1], Edge_Net_Subnet3[x+2,y,2,1,mask,1], Edge_Net_Subnet3[x+3,y,2,1,mask,1], Edge_Net_Subnet3[x+4,y,2,1,mask,1], Edge_Net_Subnet3[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,1], ~Edge_Net_Subnet3[x+1,y,2,1,mask,1]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,1], Edge_Net_Subnet3[x-2,y,2,1,mask,1], Edge_Net_Subnet3[x-3,y,2,1,mask,1], Edge_Net_Subnet3[x-4,y,2,1,mask,1], Edge_Net_Subnet3[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,1], And(Edge_Net_Subnet3[x-1,y,2,1,mask,1], Edge_Net_Subnet3[x-2,y,2,1,mask,1], Edge_Net_Subnet3[x-3,y,2,1,mask,1], Edge_Net_Subnet3[x-4,y,2,1,mask,1], Edge_Net_Subnet3[x-5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(14,14+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,1], And(Edge_Net_Subnet3[x+1,y,2,1,mask,1], Edge_Net_Subnet3[x+2,y,2,1,mask,1], Edge_Net_Subnet3[x+3,y,2,1,mask,1], Edge_Net_Subnet3[x+4,y,2,1,mask,1], Edge_Net_Subnet3[x+5,y,2,1,mask,1], ))for mask in range(1,2+1)])for x in range(30-1,14)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,1], ~Edge_Net_Subnet3[x,y-1,2,0,mask,1]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,1], Edge_Net_Subnet3[x,y+2,2,0,mask,1], Edge_Net_Subnet3[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0+1,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,1], ~Edge_Net_Subnet3[x,y+1,2,0,mask,1]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,1], Edge_Net_Subnet3[x,y-2,2,0,mask,1], Edge_Net_Subnet3[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0+3,18+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,1], And(Edge_Net_Subnet3[x,y+1,2,0,mask,1], Edge_Net_Subnet3[x,y+2,2,0,mask,1], Edge_Net_Subnet3[x,y+3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,1], And(Edge_Net_Subnet3[x,y-1,2,0,mask,1], Edge_Net_Subnet3[x,y-2,2,0,mask,1], Edge_Net_Subnet3[x,y-3,2,0,mask,1], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(18,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,1], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,1], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(14,30+1)])for y in range(0,18+1)])
	).to_cnf()
Net3_Subnet1_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,1], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,1], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)])
	).to_cnf()
Net3_Subnet1_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,1], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(14,30+1)])for y in range(2,18+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,1], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(14,30+1)])for y in range(0,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,1], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(4,18+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,1], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,1], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,1], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(14,30+1)])for y in range(3,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,1], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,1], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(4,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,1], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,1], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(14,30+1)])for y in range(0,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,1], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,1], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,1], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,1], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,30+1)])for y in range(0,18+1)])
	).to_cnf()
Net3_Subnet1_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,1], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,1], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,30+1)])for y in range(0,18+1)])
	).to_cnf()
Net3_Subnet1_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,1], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,1], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(14,30+1)])for y in range(2,18+1)]),
	).to_cnf()
Net3_Subnet1_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,1], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,30+1)])for y in range(0,18+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,1], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(14,30+1)])for y in range(2,18+1)]),
	).to_cnf()
Net3_Subnet1_DR = And(Net3_Subnet1_DR_Trend, Net3_Subnet1_DR_GIL_HorMinWidth,Net3_Subnet1_DR_GIL_HorMinSpacing,Net3_Subnet1_DR_GIL_VerMinSpacing,Net3_Subnet1_DR_AIL2_VerMinWidth,Net3_Subnet1_DR_AIL2_VerMinSpacing,Net3_Subnet1_DR_VerAIL2_HorMinSpacing,Net3_Subnet1_DR_MINT1AB_HorMinWidth,Net3_Subnet1_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet1_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet1_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet1_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet1_DR_M1AB_MinWidth,Net3_Subnet1_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet1_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet1_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet1_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet1_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet1_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet1_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet1_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet1_DR_V0_HorMinSpacing,Net3_Subnet1_DR_V1_HorMinSpacing,Net3_Subnet1_DR_V0_VerMinSpacing,Net3_Subnet1_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet1_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[18,1,0,0, 18,2,0,0, 18,3,0,0, 18,4,0,0, 18,5,0,0, 18,6,0,0, 18,7,0,0, 18,8,0,0, 18,9,0,0, 18,10,0,0, 18,11,0,0, 18,12,0,0, 18,13,0,0, 18,14,0,0, ],14,14,0,1,30,18,3,1),
	RConstraints.R1(Edge_Net_Subnet3,[26,1,0,0, 26,2,0,0, 26,3,0,0, 26,4,0,0, 26,5,0,0, 26,6,0,0, 26,7,0,0, 26,8,0,0, 26,9,0,0, 26,10,0,0, 26,11,0,0, 26,12,0,0, 26,13,0,0, 26,14,0,0, ],14,14,0,1,30,18,3,1),
	).to_cnf()
Net3_Subnet1_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[18,1,0, 18,2,0, 18,3,0, 18,4,0, 18,5,0, 18,6,0, 18,7,0, 18,8,0, 18,9,0, 18,10,0, 18,11,0, 18,12,0, 18,13,0, 18,14,0, 18,15,0, 26,1,0, 26,2,0, 26,3,0, 26,4,0, 26,5,0, 26,6,0, 26,7,0, 26,8,0, 26,9,0, 26,10,0, 26,11,0, 26,12,0, 26,13,0, 26,14,0, 26,15,0, ],30,14,0,0,30,18,3,1,2),
	)
Net3_Subnet1_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(14,30+1)])for y in range(0,18+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	).to_cnf()
Net3_Subnet1_R = And(Net3_Subnet1_R1,Net3_Subnet1_R2,Net3_Subnet1_R3,)
Net3_Subnet1_Formula = And(Net3_Subnet1_C,Net3_Subnet1_DR,Net3_Subnet1_R)
# Net = 3 Subnet = 2 | Left -> Right [22,30] Top -> Bottom [0,35]
# Range R1(26,26,1,14)
# Range R2(26,26,22,33)
### Disable edges outside window
Edge_Net_Subnet3[0:22,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(28512)
Edge_Net_Subnet3[30:41+1,0:35+1,0:3+1,0:2+1,0:2+1,2]=exprzeros(15552)

### Consistency Constraints
Net3_Subnet2_C1 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net[x,y,z,trend,mask,2]), Edge[x,y,z,trend,mask])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(22,30+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet2_C2 = And(*[And(*[And(*[And(*[And(*[Implies( Or(Edge_Net_Subnet3[x,y,z,trend,mask,2]), Edge_Net[x,y,z,trend,mask,2])for mask in range(0,2+1)])for trend in range(0,2+1)])for x in range(22,30+1)])for y in range(0,35+1)])for z in range(0,3+1)]).to_cnf()
Net3_Subnet2_C3_ME1_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,2,trend,0,2],Xor(Edge_Net_Subnet3[x,y,2,trend,1,2],Edge_Net_Subnet3[x,y,2,trend,2,2])),And(~Edge_Net_Subnet3[x,y,2,trend,0,2],~Edge_Net_Subnet3[x,y,2,trend,1,2],~Edge_Net_Subnet3[x,y,2,trend,2,2]))for x in range(22,30+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet2_C4_MINT1_Mask = And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,3,1,0,2],Xor(Edge_Net_Subnet3[x,y,3,1,1,2],Edge_Net_Subnet3[x,y,3,1,2,2])),And(~Edge_Net_Subnet3[x,y,3,1,0,2],~Edge_Net_Subnet3[x,y,3,1,1,2],~Edge_Net_Subnet3[x,y,3,1,2,2]))for x in range(22,30+1)])for y in range(0,35+1)]).to_cnf()
Net3_Subnet2_C5_AIL2GIL_Mask = And(*[And(*[And(*[Or(And(Edge_Net_Subnet3[x,y,1,trend,2,2],Xor(Edge_Net_Subnet3[x,y,1,trend,0,2],Edge_Net_Subnet3[x,y,1,trend,1,2])),And(~Edge_Net_Subnet3[x,y,1,trend,2,2],~Edge_Net_Subnet3[x,y,1,trend,0,2],~Edge_Net_Subnet3[x,y,1,trend,1,2]))for x in range(22,30+1)])for y in range(0,35+1)])for trend in range(0,1+1)]).to_cnf()
Net3_Subnet2_C6 = And(
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,1,2], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,2,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(22,30+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
And(*[And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,z,trend,2,2], And(*[And(~Edge_Net_Subnet3[x,y,z,trend,1,s2])for s2 in range(0,2)]))for trend in range(0,1+1)])for x in range(22,30+1)])for y in range(0,35+1)])for z in range(2,3+1)]),
).to_cnf()
Net3_Subnet2_C = And(Net3_Subnet2_C1, Net3_Subnet2_C2,Net3_Subnet2_C3_ME1_Mask,Net3_Subnet2_C4_MINT1_Mask,Net3_Subnet2_C5_AIL2GIL_Mask,Net3_Subnet2_C6,)
### Design Rules
Net3_Subnet2_DR_Trend = And(
	And(*[And(*[Not(Edge[x,y,1,0,1])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[Not(Edge[x,y,1,1,0])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Not(Edge[x,y,3,0,mask])for x in range(22,30+1)])for y in range(0,35+1)])for mask in range(0,2+1)])
	).to_cnf()
Net3_Subnet2_DR_GIL_HorMinWidth = And(
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,2], ~Edge_Net_Subnet3[x-1,y,1,1,1,2]), And(Edge_Net_Subnet3[x+1,y,1,1,1,2], Edge_Net_Subnet3[x+2,y,1,1,1,2], Edge_Net_Subnet3[x+3,y,1,1,1,2], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,1,1,1,2], ~Edge_Net_Subnet3[x+1,y,1,1,1,2]), And(Edge_Net_Subnet3[x-1,y,1,1,1,2], Edge_Net_Subnet3[x-2,y,1,1,1,2], Edge_Net_Subnet3[x-3,y,1,1,1,2], ))for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_GIL_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,2], ~Edge[x-1,y,1,1,1]), And(~Edge[x-1,y,1,1,1], ~Edge[x-2,y,1,1,1], ~Edge[x-3,y,1,1,1], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,1,1,2], ~Edge[x+1,y,1,1,1]), And(~Edge[x+1,y,1,1,1], ~Edge[x+2,y,1,1,1], ~Edge[x+3,y,1,1,1], ))for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_GIL_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,2], And(~Edge[x,y+1,1,1,1], ~Edge[x,y+2,1,1,1], ~Edge[x,y+3,1,1,1], ))for x in range(22,30+1)])for y in range(0,32+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,1,1,2], And(~Edge[x,y-1,1,1,1], ~Edge[x,y-2,1,1,1], ~Edge[x,y-3,1,1,1], ))for x in range(22,30+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_AIL2_VerMinWidth = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2]), And(Edge_Net_Subnet3[x,y+1,1,0,0,2], Edge_Net_Subnet3[x,y+2,1,0,0,2], Edge_Net_Subnet3[x,y+3,1,0,0,2], ))for x in range(22,30+1)])for y in range(0,0+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2]), And(Edge_Net_Subnet3[x,y-1,1,0,0,2], Edge_Net_Subnet3[x,y-2,1,0,0,2], Edge_Net_Subnet3[x,y-3,1,0,0,2], ))for x in range(22,30+1)])for y in range(35,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge_Net_Subnet3[x,y-1,1,0,0,2]), And(Edge_Net_Subnet3[x,y+1,1,0,0,2], Edge_Net_Subnet3[x,y+2,1,0,0,2], Edge_Net_Subnet3[x,y+3,1,0,0,2], ))for x in range(22,30+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge_Net_Subnet3[x,y+1,1,0,0,2]), And(Edge_Net_Subnet3[x,y-1,1,0,0,2], Edge_Net_Subnet3[x,y-2,1,0,0,2], Edge_Net_Subnet3[x,y-3,1,0,0,2], ))for x in range(22,30+1)])for y in range(0+3,35-1+1)])
	).to_cnf()
Net3_Subnet2_DR_AIL2_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ))for x in range(22,30+1)])for y in range(1,1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-2,1,0,0], ~Edge[x,y-1,1,0,0], ))for x in range(22,30+1)])for y in range(2,2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ))for x in range(22,30+1)])for y in range(35-1,35-1+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+2,1,0,0], ~Edge[x,y+1,1,0,0], ))for x in range(22,30+1)])for y in range(35-2,35-2+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y-1,1,0,0]), And(~Edge[x,y-1,1,0,0], ~Edge[x,y-2,1,0,0], ~Edge[x,y-3,1,0,0], ))for x in range(22,30+1)])for y in range(0+3,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,1,0,0,2], ~Edge[x,y+1,1,0,0]), And(~Edge[x,y+1,1,0,0], ~Edge[x,y+2,1,0,0], ~Edge[x,y+3,1,0,0], ))for x in range(22,30+1)])for y in range(0,35-3+1)])
	).to_cnf()
Net3_Subnet2_DR_VerAIL2_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,2], And(~Edge[x+1,y,1,0,0], ~Edge[x+2,y,1,0,0], ~Edge[x+3,y,1,0,0], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,0,0,2], And(~Edge[x-1,y,1,0,0], ~Edge[x-2,y,1,0,0], ~Edge[x-3,y,1,0,0], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_MINT1AB_HorMinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,2], ~Edge_Net_Subnet3[x-1,y,3,1,mask,2]), And(Edge_Net_Subnet3[x+1,y,3,1,mask,2], Edge_Net_Subnet3[x+2,y,3,1,mask,2], Edge_Net_Subnet3[x+3,y,3,1,mask,2], Edge_Net_Subnet3[x+4,y,3,1,mask,2], Edge_Net_Subnet3[x+5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,3,1,mask,2], ~Edge_Net_Subnet3[x+1,y,3,1,mask,2]), And(Edge_Net_Subnet3[x-1,y,3,1,mask,2], Edge_Net_Subnet3[x-2,y,3,1,mask,2], Edge_Net_Subnet3[x-3,y,3,1,mask,2], Edge_Net_Subnet3[x-4,y,3,1,mask,2], Edge_Net_Subnet3[x-5,y,3,1,mask,2], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_MINT1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,2], And(~Edge[x,y+1,3,1,mask], ~Edge[x,y+2,3,1,mask], ~Edge[x,y+3,3,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,32+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,mask,2], And(~Edge[x,y-1,3,1,mask], ~Edge[x,y-2,3,1,mask], ~Edge[x,y-3,3,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_MINT1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,2], ~Edge[x-1,y,3,1,mask]), And(~Edge[x-1,y,3,1,mask], ~Edge[x-2,y,3,1,mask], ~Edge[x-3,y,3,1,mask], ~Edge[x-4,y,3,1,mask], ~Edge[x-5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,mask,2], ~Edge[x+1,y,3,1,mask]), And(~Edge[x+1,y,3,1,mask], ~Edge[x+2,y,3,1,mask], ~Edge[x+3,y,3,1,mask], ~Edge[x+4,y,3,1,mask], ~Edge[x+5,y,3,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_MINT1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,2], And(~Edge[x,y+1,3,1,2], ~Edge[x,y+2,3,1,2], ))for x in range(22,30+1)])for y in range(0,33+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,3,1,1,2], And(~Edge[x,y-1,3,1,2], ~Edge[x,y-2,3,1,2], ))for x in range(22,30+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_MINT1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,2], ~Edge[x-1,y,3,1,1]), And(~Edge[x-1,y,3,1,2], ~Edge[x-2,y,3,1,2], ~Edge[x-3,y,3,1,2], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,3,1,1,2], ~Edge[x+1,y,3,1,1]), And(~Edge[x+1,y,3,1,2], ~Edge[x+2,y,3,1,2], ~Edge[x+3,y,3,1,2], ))for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_M1AB_MinWidth = And(
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,2], ~Edge_Net_Subnet3[x-1,y,2,1,mask,2]), And(Edge_Net_Subnet3[x+1,y,2,1,mask,2], Edge_Net_Subnet3[x+2,y,2,1,mask,2], Edge_Net_Subnet3[x+3,y,2,1,mask,2], Edge_Net_Subnet3[x+4,y,2,1,mask,2], Edge_Net_Subnet3[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(And(Edge_Net_Subnet3[x,y,2,1,mask,2], ~Edge_Net_Subnet3[x+1,y,2,1,mask,2]), And(Edge_Net_Subnet3[x-1,y,2,1,mask,2], Edge_Net_Subnet3[x-2,y,2,1,mask,2], Edge_Net_Subnet3[x-3,y,2,1,mask,2], Edge_Net_Subnet3[x-4,y,2,1,mask,2], Edge_Net_Subnet3[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,2], And(Edge_Net_Subnet3[x-1,y,2,1,mask,2], Edge_Net_Subnet3[x-2,y,2,1,mask,2], Edge_Net_Subnet3[x-3,y,2,1,mask,2], Edge_Net_Subnet3[x-4,y,2,1,mask,2], Edge_Net_Subnet3[x-5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(22,22+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,2], And(Edge_Net_Subnet3[x+1,y,2,1,mask,2], Edge_Net_Subnet3[x+2,y,2,1,mask,2], Edge_Net_Subnet3[x+3,y,2,1,mask,2], Edge_Net_Subnet3[x+4,y,2,1,mask,2], Edge_Net_Subnet3[x+5,y,2,1,mask,2], ))for mask in range(1,2+1)])for x in range(30-1,22)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,2], ~Edge_Net_Subnet3[x,y-1,2,0,mask,2]), And(Edge_Net_Subnet3[x,y+1,2,0,mask,2], Edge_Net_Subnet3[x,y+2,2,0,mask,2], Edge_Net_Subnet3[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0+1,35-4+1+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,2], ~Edge_Net_Subnet3[x,y+1,2,0,mask,2]), And(Edge_Net_Subnet3[x,y-1,2,0,mask,2], Edge_Net_Subnet3[x,y-2,2,0,mask,2], Edge_Net_Subnet3[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0+3,35-1+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,2], And(Edge_Net_Subnet3[x,y+1,2,0,mask,2], Edge_Net_Subnet3[x,y+2,2,0,mask,2], Edge_Net_Subnet3[x,y+3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,0+1)]),
	And(*[And(*[And(*[ Implies( Edge_Net_Subnet3[x,y,2,0,mask,2], And(Edge_Net_Subnet3[x,y-1,2,0,mask,2], Edge_Net_Subnet3[x,y-2,2,0,mask,2], Edge_Net_Subnet3[x,y-3,2,0,mask,2], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(35,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_HorM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,2], ~Edge[x-1,y,2,1,1]), And(~Edge[x-1,y,2,1,2], ~Edge[x-2,y,2,1,2], ~Edge[x-3,y,2,1,2], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,1,2], ~Edge[x+1,y,2,1,1]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ))for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_HorM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,2], ~Edge[x-1,y,2,1,mask]), And(~Edge[x-1,y,2,1,mask], ~Edge[x-2,y,2,1,mask], ~Edge[x-3,y,2,1,mask], ~Edge[x-4,y,2,1,mask], ~Edge[x-5,y,2,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,1,mask,2], ~Edge[x+1,y,2,1,mask]), And(~Edge[x+1,y,2,1,2], ~Edge[x+2,y,2,1,2], ~Edge[x+3,y,2,1,2], ~Edge[x+4,y,2,1,2], ~Edge[x+5,y,2,1,2], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_VerM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,2], ~Edge[x,y-1,2,0,1]), And(~Edge[x,y-1,2,0,2], ~Edge[x,y-2,2,0,2], ))for x in range(22,30+1)])for y in range(2,35+1)]),
	And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,1,2], ~Edge[x,y+1,2,0,1]), And(~Edge[x,y+1,2,0,2], ~Edge[x,y+2,2,0,2], ))for x in range(22,30+1)])for y in range(0,35-2+1)]),
	).to_cnf()
Net3_Subnet2_DR_VerM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,2], ~Edge[x,y-1,2,0,mask]), And(~Edge[x,y-1,2,0,mask], ~Edge[x,y-2,2,0,mask], ~Edge[x,y-3,2,0,mask], ~Edge[x,y-4,2,0,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(4,35+1)]),
	And(*[And(*[And(*[ Implies( And(Edge_Net_Subnet3[x,y,2,0,mask,2], ~Edge[x,y+1,2,0,mask]), And(~Edge[x,y+1,2,0,mask], ~Edge[x,y+2,2,0,mask], ~Edge[x,y+3,2,0,mask], ~Edge[x,y+4,2,0,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35-4+1)]),
	).to_cnf()
Net3_Subnet2_DR_HorM1_DiffMask_VerMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,2], And(~Edge[x,y+1,2,1,2], ~Edge[x,y+2,2,1,2], ~Edge[x,y+3,2,1,2], ))for x in range(22,30+1)])for y in range(0,35-3+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,1,2], And(~Edge[x,y-1,2,1,2], ~Edge[x,y-2,2,1,2], ~Edge[x,y-3,2,1,2], ))for x in range(22,30+1)])for y in range(3,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_HorM1_SameMask_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,2], And(~Edge[x,y+1,2,1,mask], ~Edge[x,y+2,2,1,mask], ~Edge[x,y+3,2,1,mask], ~Edge[x,y+4,2,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35-4+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,1,mask,2], And(~Edge[x,y-1,2,1,mask], ~Edge[x,y-2,2,1,mask], ~Edge[x,y-3,2,1,mask], ~Edge[x,y-4,2,1,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(4,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_VerM1_DiffMask_HorMinSpacing = And(
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,2], And(~Edge[x+1,y,2,0,2], ~Edge[x+2,y,2,0,2], ~Edge[x+3,y,2,0,2], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,1,2], And(~Edge[x-1,y,2,0,2], ~Edge[x-2,y,2,0,2], ~Edge[x-3,y,2,0,2], ))for x in range(22,30+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_VerM1_SameMask_HorMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,2], And(~Edge[x+1,y,2,0,mask], ~Edge[x+2,y,2,0,mask], ~Edge[x+3,y,2,0,mask], ~Edge[x+4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,0,mask,2], And(~Edge[x-1,y,2,0,mask], ~Edge[x-2,y,2,0,mask], ~Edge[x-3,y,2,0,mask], ~Edge[x-4,y,2,0,mask], ))for mask in range(1,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_V0_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,2], And(~Edge[x-1,y,1,2,mask], ~Edge[x-2,y,1,2,mask], ~Edge[x-3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,1,2,mask,2], And(~Edge[x+1,y,1,2,mask], ~Edge[x+2,y,1,2,mask], ~Edge[x+3,y,1,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_V1_HorMinSpacing = And(
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,2], And(~Edge[x-1,y,2,2,mask], ~Edge[x-2,y,2,2,mask], ~Edge[x-3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(0,35+1)]),
	And(*[And(*[And(*[ Implies(Edge_Net_Subnet3[x,y,2,2,mask,2], And(~Edge[x+1,y,2,2,mask], ~Edge[x+2,y,2,2,mask], ~Edge[x+3,y,2,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(0,35+1)])
	).to_cnf()
Net3_Subnet2_DR_V0_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,2], And(~Edge[x,y+1,1,2,mask], ~Edge[x,y+2,1,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,1,2,mask,2], And(~Edge[x,y-1,1,2,mask], ~Edge[x,y-2,1,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet2_DR_V1_VerMinSpacing = And(
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,2], And(~Edge[x,y+1,2,2,mask], ~Edge[x,y+2,2,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(0,33+1)]),
	And(*[And(*[And(*[Implies(Edge_Net_Subnet3[x,y,2,2,mask,2], And(~Edge[x,y-1,2,2,mask], ~Edge[x,y-2,2,2,mask], ))for mask in range(2,2+1)])for x in range(22,30+1)])for y in range(2,35+1)]),
	).to_cnf()
Net3_Subnet2_DR = And(Net3_Subnet2_DR_Trend, Net3_Subnet2_DR_GIL_HorMinWidth,Net3_Subnet2_DR_GIL_HorMinSpacing,Net3_Subnet2_DR_GIL_VerMinSpacing,Net3_Subnet2_DR_AIL2_VerMinWidth,Net3_Subnet2_DR_AIL2_VerMinSpacing,Net3_Subnet2_DR_VerAIL2_HorMinSpacing,Net3_Subnet2_DR_MINT1AB_HorMinWidth,Net3_Subnet2_DR_MINT1_SameMask_VerMinSpacing,Net3_Subnet2_DR_MINT1_SameMask_HorMinSpacing,Net3_Subnet2_DR_MINT1_DiffMask_VerMinSpacing,Net3_Subnet2_DR_MINT1_DiffMask_HorMinSpacing,Net3_Subnet2_DR_M1AB_MinWidth,Net3_Subnet2_DR_HorM1_DiffMask_HorMinSpacing,Net3_Subnet2_DR_HorM1_SameMask_HorMinSpacing,Net3_Subnet2_DR_VerM1_DiffMask_VerMinSpacing,Net3_Subnet2_DR_VerM1_SameMask_VerMinSpacing,Net3_Subnet2_DR_HorM1_DiffMask_VerMinSpacing,Net3_Subnet2_DR_HorM1_SameMask_VerMinSpacing,Net3_Subnet2_DR_VerM1_DiffMask_HorMinSpacing,Net3_Subnet2_DR_VerM1_SameMask_HorMinSpacing,Net3_Subnet2_DR_V0_HorMinSpacing,Net3_Subnet2_DR_V1_HorMinSpacing,Net3_Subnet2_DR_V0_VerMinSpacing,Net3_Subnet2_DR_V1_VerMinSpacing,)
### Routability Constraints
Net3_Subnet2_R1 = And(
	RConstraints.R1(Edge_Net_Subnet3,[26,1,0,0, 26,2,0,0, 26,3,0,0, 26,4,0,0, 26,5,0,0, 26,6,0,0, 26,7,0,0, 26,8,0,0, 26,9,0,0, 26,10,0,0, 26,11,0,0, 26,12,0,0, 26,13,0,0, 26,14,0,0, ],14,22,0,1,30,35,3,2),
	RConstraints.R1(Edge_Net_Subnet3,[26,22,0,0, 26,23,0,0, 26,24,0,0, 26,25,0,0, 26,26,0,0, 26,27,0,0, 26,28,0,0, 26,29,0,0, 26,30,0,0, 26,31,0,0, 26,32,0,0, 26,33,0,0, ],12,22,0,1,30,35,3,2),
	).to_cnf()
Net3_Subnet2_R2 = And(
	RConstraints.R2_R4_V3(Edge_Net_Subnet3,Edge,Edge_Net,[26,1,0, 26,2,0, 26,3,0, 26,4,0, 26,5,0, 26,6,0, 26,7,0, 26,8,0, 26,9,0, 26,10,0, 26,11,0, 26,12,0, 26,13,0, 26,14,0, 26,15,0, 26,22,0, 26,23,0, 26,24,0, 26,25,0, 26,26,0, 26,27,0, 26,28,0, 26,29,0, 26,30,0, 26,31,0, 26,32,0, 26,33,0, 26,34,0, ],28,22,0,0,30,35,3,2,2),
	)
Net3_Subnet2_R3 = And(
	And(*[And(*[And(*[And(*[And(*[And(*[Implies(Edge_Net[x,y,z,trend,mask,2],~Edge_Net[x,y,z,trend,mask,net2])for net2 in range(0,1+1)])for x in range(22,30+1)])for y in range(0,35+1)])for z in range(1,3+1)])for trend in range(0,2+1)])for mask in range(0,2+1)]),
	).to_cnf()
Net3_Subnet2_R = And(Net3_Subnet2_R1,Net3_Subnet2_R2,Net3_Subnet2_R3,)
Net3_Subnet2_Formula = And(Net3_Subnet2_C,Net3_Subnet2_DR,Net3_Subnet2_R)
FORMULA = And(Net1_Subnet1_Formula, Net2_Subnet0_Formula, Net2_Subnet1_Formula, Net2_Subnet2_Formula, Net2_Subnet3_Formula, Net2_Subnet5_Formula, Net2_Subnet7_Formula, Net2_Subnet8_Formula, Net3_Subnet0_Formula, Net3_Subnet1_Formula, Net3_Subnet2_Formula, )
endTime = time.time()
print('Total Time = ', endTime-startTime)
setOut.clauseDistribution(FORMULA)
setOut.setUpLayoutViaFromResult(FORMULA.satisfy_one(),outLayout,subnetRec,3)
print('#edge = 15785')