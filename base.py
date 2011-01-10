"""
           1  2  3
           4  5  6
           7  8  9
 10 11 12 19 20 21 28 29 30
 13 14 15 22 23 24 31 32 33
 16 17 18 25 26 27 34 35 36
          37 38 39
          40 41 42
          43 44 45
          46 47 48
          49 50 51
          52 53 54

Description:
  base of permutations of 6 elements that is natural to humans.
  note that there are some fixed points in this model

Data:
  B ... array of 6 base permutations
  N ... number of small faces
  fixed_points ... array of fixed points
"""

from perm import perm

b0 = perm([(1+3*i,19+3*i,37+3*i,46+3*i) for i in range(3)]+[(10,12,18,16),(11,15,17,13)])
b1 = perm([(3+3*i,21+3*i,39+3*i,48+3*i) for i in range(3)]+[(30,28,34,36),(29,31,35,33)])

b2 = perm([(10+i,19+i,28+i,54-i) for i in range(3)]+[(1,7,9,3),(4,8,6,2)])
b3 = perm([(16+i,25+i,34+i,48-i) for i in range(3)]+[(43,37,39,45),(40,38,42,44)])

b4 = perm([(7+i,18-3*i,39-i,28+3*i) for i in range(3)]+[(19,25,27,21),(22,26,24,20)])
b5 = perm([(1+i,16-3*i,45-i,30+3*i) for i in range(3)]+[(52,46,48,54),(49,47,51,53)])

B = [b0,b1,b2,b3,b4,b5]

N = 9*6

fixed_points = [5,14,23,32,41,50]
