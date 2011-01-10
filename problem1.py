"""
Description:
  given the initial state of the cube turned a small number of times
  try to find a list of base permutations to solve it exactly; works! :-)
"""
from perm import perm
import base

def breath_search(a):
    queue = [([],a)]
    i = 0
    while True:
        moves, state = queue[i]
        i += 1
        if state.IsIdentity():
            return moves
        j = 0
        for b in base.B:
            queue.append((moves+[j],b*state))
            j += 1

if __name__ == '__main__':
    print(breath_search((base.b0)))
    print(breath_search((base.b0*base.b5*base.b3*base.b0).Inverse()))
    print(breath_search((base.b0*base.b5*base.b3*base.b0*base.b1).Inverse()))

# vim:expandtab:softtabstop=4:shiftwidth=4
