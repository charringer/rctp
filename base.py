"""
           0  1  2
           3  4  5
           6  7  8
  9 10 11 18 19 20 27 28 29
 12 13 14 21 22 23 30 31 32
 15 16 17 24 25 26 33 34 35
          36 37 38
          39 40 41
          42 43 44
          45 46 47
          48 49 50
          51 52 53

Description:
  base of permutations of 6 elements that is natural to humans.
  note that there are some fixed points in this model

Data:
  B ... array of 6 base permutations
  N ... number of small faces
  fixed_points ... array of fixed points
"""

from perm import perm

b0 = perm([(0+3*i,18+3*i,36+3*i,45+3*i) for i in range(3)]+[(9,11,17,15),(10,14,16,12)])
b1 = perm([(2+3*i,20+3*i,38+3*i,47+3*i) for i in range(3)]+[(29,27,33,35),(28,30,34,32)])

b2 = perm([(9+i,18+i,27+i,53-i) for i in range(3)]+[(0,6,8,2),(3,7,5,1)])
b3 = perm([(15+i,24+i,33+i,47-i) for i in range(3)]+[(42,36,38,44),(39,37,41,43)])

b4 = perm([(6+i,17-3*i,38-i,27+3*i) for i in range(3)]+[(18,24,26,20),(21,25,23,19)])
b5 = perm([(0+i,15-3*i,44-i,29+3*i) for i in range(3)]+[(51,45,47,53),(48,46,50,52)])

B = [b0,b1,b2,b3,b4,b5]

N = 9*6

fixed_points = [4,13,22,31,40,49]
