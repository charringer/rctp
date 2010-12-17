"""
File   perm.py
 
Description
    An object oriented permutation library which currently
    uses a list to store the images of each point. The length
    of the list is generally the largest point moved plus one
    to include the 0 point (Python convention first index is zero).
 
 
Author
    Ernesto P. Adorio, Ph.D.
    University of the Philippines
    Extension Program in Pampanga
    Clark Field
 
    e-mail:
      ernesto.adorio@gmail.com
      eadorio@yahoo.com
 
Acknowledgments
    Python and GAP software developers
    Some of the names of the interface  functions
    are adopted from GAP.
 
 
Funding
    This work is not funded by any external agencies.
 
Todos
    1.  Parity or sign of a permutation
    2.  i^p, the image of i under p.  (overload int class)?
 
Revisions
    0.1      april.23.2005
             Starting permutation index is now controlled by base
             which can be either 0 or 1.  However, it is better
             that we adopt 1 as the base always to be compatible
             with other computer algebra systems.
 
             Able to accept transpositions as input. Default
             operation is from left to right.
 
    0.1      april.22.2005
             Changed to disjoint cycles as input notation.
             More user friendly than image list.
               (0,1)(2,3) in disjoint cycle notation
               is now inputted as perm([0,1],[2,3]).
 
    0.1      april.21.2005
             Uses internal list representation for
             elements, 0 based, image list for input.
 
             Example:
 
               (0, 1)(2,3) in disjoint cycle notation
               is inputted as perm([1,0,3,2]).
               This has been changed april.22.2005
 
References, alternatives
    Kirby Urner permutation routines use dictionary
    based representation.
 
Copyright 2005 Ernesto P. Adorio
License. GNU Affero GPL license.
Please see the file COPYING also in the download section.
 
 
Citation: "http://www.adorio-research.org:8003/downloads/perm.py").
 
"""
import sequence as seq
from   mathutils import *
 
 
RIGHT_TO_LEFT_EVAL_ORDER = 0
LEFT_TO_RIGHT_EVAL_ORDER = 1
 
class perm:
    """
    Provides basic methods for permutations.
    """
    EVAL_ORDER = LEFT_TO_RIGHT_EVAL_ORDER  # Should only be changed at the start of use.
                   #   0   -  right to left
                   #   1   -  left to right
    PERM_BASE = 1 # default.
 
    def __init__(self, *kargs):
        """
        Initializes perm object. Expects either a
        varying number of integers representing a single
        cycle or a list/tuple of disjoint cycles or transpositions.
 
        Cycle elements are processed using the current evaluation order.
 
        perm.perm()                         identity permutation, [()]
        perm.perm(1,2,3,4)                  cycle [(1,2,3,4)]
        perm.perm([1,2,3,4])                cycle [(1,2,3,4)]
        perm.perm([1,2], [1,3], [1,4])      transposition, cycle [(1,2,3,4)]
        perm.perm([1,4], [1,3], [1,2])      transposition, cycle [(1,4,3,2)]
        perm.perm([1,2],[3,4])              cycle   [(1,2),(3,4)]
        perm.perm(1,2,3,1)                  invalid, will return identity [()]
        """
        # No input cycle, not even a number
        if len(kargs) == 0:
            # Default action is to return an identity permutation
            self.size = 0
            self.p    = []
            self.base = perm.PERM_BASE
            return
 
        # array of arrays ?
        newkargs = []
        if len(kargs) == 1 and type(kargs[0]) in [list, tuple]:
            for p in kargs[0]:
                newkargs.append(p)
        else:
            # Remove any empty list element
            for y in kargs:
                if (type(y) == list or type(y) == tuple):
                    if len(y) > 0:
                       newkargs.append(y)
                else:
                    newkargs.append(y)
 
        if len(newkargs) == 0 or seq.MinElt(newkargs) < self.PERM_BASE:
            self.size = 0
            self.p    = []
            return
 
        # Largest element determines storage size.
        self.size = max(seq.MaxElt(newkargs), 0) + 1
        self.p    = [i for i in range(self.size)]
 
        # print "Initial size = ", self.size
        # print "self.p       = ", self.p
 
        # All numbers (a single cycle actually) ?
        if seq.IsAllIntegers(newkargs):
            prev = start = newkargs[0]
            for x in newkargs[1:]:
                self.p[prev] = x
                prev = x
            self.p[prev] = start
 
        # All sequences ?
        elif seq.IsAllSequences(newkargs):
            # Convert all cycles to all points image
            plist = []
            for y in newkargs:
                if len(y) == 0:
                    continue
                a = [i for i in range(self.size)]
                k = y[0]
                start = k
                for i in range(1,len(y)):
                    m    = y[i]
                    a[k] = m
                    k    = m
                a[k] = start
                plist.append(a)
 
            if perm.EVAL_ORDER == 0:
                for i in range(perm.PERM_BASE, self.size):
                    imap = i
                    for j in range(len(plist)):
                        imap = plist[j][imap]
                    self.p[i] = imap
            else:
                for i in range(perm.PERM_BASE, self.size):
                    imap = i
                    for j in range(len(plist)):
                        imap = plist[j][imap]
                    self.p[i] = imap
        else:
            print("__init__() error: undefined type, returning identity.")
            self.size = 0
            self.p    = []
 
        if not self.IsPermutation():
            print("__init__() error: invalid permutation.")
            self.size = 0
            self.p    = []
        return
 
    def Pack(self):
        """
        Internal command. Decreases size of internal representation.
        Find the first point not moved starting from the right.
        I don't know if this is really useful in working with small groups.
        """
        size = self.size
        for i in range(size-1, perm.PERM_BASE, -1):
            if self[i] == i:
                size = size -1
            else:
                break
        if size != self.size:
            self.p = self[0:max(size, 1+ perm.PERM_BASE)]
            self.size = size
 
    def FromImage(self, imagearray):
        """
        imagearray - image of points
 
        Returns a permutation from an image array.
 
        Ex.  To imput 1 -> 2, 2->3, 3->1,4->4 as a permutation, one can call
             perm.FromImage([2,3,1,4])
        """
        length = len(imagearray)
        if length == 0:
            return self.Identity()
 
        minelt = min(imagearray)
        r      = perm()
 
        if perm.PERM_BASE != minelt:
            print("perm.FromImage() error: not a valid image array!")
            return r
 
        if minelt == 1:
            r.p    = [0] * (length + 1)
            for i in range(0, length):
                r.p[i+1] = imagearray[i]
            r.size = length+1
        else:
            r.p    = [0] * length
            for i in range(0, length):
                r.p[i] = imagearray[i]
            r.size = length
        return r
 
 
    def ToImage(self):
        """
        Returns the internal image array data.
 
        >>> x = perm.perm([1,2,3])
        >>> x.ToImage()
        [2, 3, 1]
        >>>
        """
        return self.p[perm.PERM_BASE:]
 
    def Identity(self, size = 0):
        """
        Returns identity element permutation of specified size.
        """
        result = perm()
        if size <= 0:
            return result
        result.size = size + perm.PERM_BASE
        result.p = [i for i in range(result.size)]
        return result
 
    def IsIdentity(self):
        """
        Returns True if permutation is an identity.
        """
        for i in range(self.size):
            if self.p[i] != i:
                return False
        return True
 
    def Inverse(self):
        """
        Returns inverse of permutation p.
        """
        q = [0] * self.size
        for i in range(self.size):
            q[self[i]] = i
        return perm.FromImage(self, q[1:])
 
    def __mul__(self, other):
        """
        Multiplication of two permutations
        Needs to be rewritten.
        """
        if type(other) != type(self):
            return self.Image(other)
 
        size   = max(self.size, other.size)
        result = self.Identity(size)
        # print("size   = ", size)
        # print("result = ", result)
        r = result.p
 
        if perm.EVAL_ORDER == 0:  # right to left
            for i in range(size):
                r[i] = self[other[i]]
        else:
            for i in range(size): # default left to right
                r[i] = other[self[i]]
        return result
 
    def __rxor__(self, other):
        """
        Allows operation of the form i ^p for the image
        of i under p.
        """
        if type(other) == int:
            return self[other]
        if seq.IsSequence(other):
            return [self[i] for i in other]
 
        print("__rxor__() error: undefined type.")
        return None
 
    def __div__(self, other):
        """
        Returns self * other^-1
        """
        return self * other.Inverse()
 
    def __eq__(self, other):
        """
        Tests for equality
        """
        # Test the trailing longer permutation
        if self.size > other.size:
            for i in range(other.size, self.size):
                if self[i] != i:
                    return False
 
        elif self.size < other.size:
            for i in range(self.size, other.size):
                if other[i] != i:
                    return False
 
        # Test for equality
        for i in range(min(self.size, other.size)):
            if self[i] != other[i]:
                return False
 
        return True
 
    def __ne__(self, other):
        """
        other - the other permutation to be compared.
 
        Returns true if self != other
        """
        return not (self == other)
 
    def __repr__(self):
        """
        External printing representation.
        """
        return "perm(" + str(self.Cycles()) + ")"
 
    def __getitem__(self, i):
        """
        i  - position
 
        Returns the image of i under permutation.
        """
        # print("@@@ size = ", self.size, ",self.size = ", i)
        if i >= perm.PERM_BASE and i < self.size:
            return self.p[i]
        else:
            return i
 
    def Copy(self):
        """
        Returns an object copy of self.
        """
        return self.FromImage(self.p[1:])
 
    def Order(self):
        """
        Returns the order of the element.
        It is computed as the lcm of the lengths of the
        cycles.
        """
        cycles  = self.Cycles()
        acycles = [ len(cyc) for cyc in cycles if len(cyc) > 1 ]
        return lcm(acycles)
 
 
    def Conjugate(self, q):
        """
        Returns conjugate q^-1 self q.
 
        See __xor__() method.
        """
        return q.Inverse() * self * q
 
    def __xor__(self, q):
        """       type    return value
        p ^ q     ---------------------------------------
                  perm    conjugate of p by q,  (q p q^-1)
                  int     integer power p^ n
        """
        if type(q) == type(self.Identity()):
            return self.Conjugate(q)
        elif type(q) == type(1):
            return self.IntPow(q)
 
        print("Error: unimplemented xor argument type.")
        return self.Identity()
 
    def IntPow(self, n):
        """
        n       integer power of permutation.
 
        """
        t = self.Identity()
        if type(n) != type(1):
            print("perm.IntPow() error: expected an integer.")
            return t
 
        if n == 0:
            return t
 
        # p ^ n = p ^ r  where r = n mod Order(p)
        p     = self.Copy()
        order = self.Order()
        m     = abs(n)
        r     = m % order
        if r == 0:
            return t
 
        if r == 1:
            return p
 
        if n < 0:
            r = order - r
 
        # Fast powering algorithm using squaring algorithm.
        while r > 0:
            if r & 1:     # odd ??
                t = t * p
            r = r >> 1
            p = p * p
        return t
 
    def Image(self, pt):
        """
        Returns the image of a point(s) under self.
        """
        if seq.IsSequence(pt):
            image = pt[:]
            for i in range(len(pt)):
                image[i] = self[pt[i]]
            return image
        return self[pt]
 
    def IsPermutation(self):
        """
        Returns True if self is 1-1.
        """
        # Test for 1-1
        flags = [False] * self.size
        for i in range(self.size):
            flags[self[i]] = True
 
        for i in range(self.size):
            if not flags[i]:
                return False
        return True
 
    def IsEvenPermutation(self):
        """
        Returns True if self is an even permutation.
        """
        if self.Sign() == 1: return True
        return False
 
    def IsOddPermutation(self):
        """
        Returns False if self is an odd permutation.
        """
        if self.Sign() == 1: return False
        return True
 
    def Sign(self):
        """
        Returns the  sign of permutation p. If the
        number of equivalent transpositions is even, the
        sign is one, otherwise it is -1.
 
        Example:
           perm.perm().Sign()       1
           perm.perm(2,3).Sign()   -1
           perm.perm(1,2).Sign()   -1
           perm.perm(1,2,3).Sign()  1
           perm.perm(1,3,2).Sign()  1
           perm.perm(1,3).Sign()   -1
        """
 
        # If the total counts of even cycles is even, return 1
        # otherwise return -1.
        cycs = self.CycleCounts()
        tot  = 0
        for i in range(2, self.size, 2):
            tot = tot + cycs[i]
        if tot % 2 == 0:
            return 1
        return -1
 
 
    def NrInversions(self):
        """
        Returns the number of inversions in a permutation.
 
        Example. The permutation perm([2,3], [4,1]) has the corresponding
        image array [4,3,2,1]. The number of inversions is
 
         Pt  pts < Pts Count
        --------------------
          4:  3,2,1   3
          3:  2,1     2
          2:  1       1
        --------------------
              Total   6
        """
        count = 0
        for i in range(1, self.size-1):
            x = self[i]
            for j in range(i+1, self.size):
                if x > self[j]:
                    count = count + 1
        return count
 
    def Cycles(self):
        """
        Returns internal permutation representation in
        disjoint cycles notation.
 
        WARNING: This is subject to eternal looping if
                 an invalid permutation was accepted.
        """
        cycles = []
        flags  = [False] * self.size
 
        for i in range(perm.PERM_BASE, self.size):
            if not flags[i]:
                flags[i] = True
                cycle    = []
                start    = i
                j        = i
                cycle.append(j)
                while self[j] != start:
                    flags[self[j]] = True
                    cycle.append(self[j])
                    j = self[j]
                if len(cycle) > 1:
                    cycles.append(tuple(cycle))
        if len(cycles) == 0:
            return [()]
        return cycles
 
    def CycleCounts(self):
        """
        Returns counts of cycles in permutation.
        The first element counts[0] is always 0.
 
        Example.
        >>> perm([1,2], [3,4,5]).CycleCounts()
        [0, 0, 1, 1, 0, 0]
        """
        counts  = [0] * (self.size)
        visited = [False] * (self.size)
 
        for i in range(1, self.size):
            if not visited[i]:
                cyclelen = 1
                j = i
                visited[j] = True
                while self[j] != i:
                    cyclelen   = cyclelen + 1
                    j          = self.p[j]
                    visited[j] = True
                counts[cyclelen] = counts[cyclelen] + 1
        return counts
 
    def LargestMovedPoint(self):
        """
        Returns largest integer moved by permutation.
        Example.
           perm([1,2],[3,4]).LargestMovedPoint() wil return 4.
        """
        for i in range(self.size-1,perm.PERM_BASE-1, -1):
            if self[i] != i:
                return i
        return -1
 
    def SmallestMovedPoint(self):
        """
        Returns smallest integer moved by p.
        Example.
           perm([1,2],[3,4]).SmallesMovedPoint() wil return 1.
        """
        for i in range(perm.PERM_BASE, self.size):
            if self[i] != i:
                return i
        return -1
 
    def NrMovedPoints(self):
        """
        Returns number of moved points.
        Example.
           perm([5,3],[1,2]).NrMovedPoints() will return 4.
        """
        count = 0
        for i in range(perm.PERM_BASE, self.size):
            if self[i] != i:
                count = count + 1
        return count
 
    def MovedPoints(self):
        """
        Returns list of moved points p.
        """
        points = []
        for i in range(perm.PERM_BASE, self.size):
            if self[i] != i:
                points.append(i)
        return points
 
    def NrFixedPoints(self, degree):
        """
        degree - number of points
 
        Returns number of fixed points. The degree is not stored
        in the internal representation of a permutation.
        """
        return len(self.Fix(degree))
 
 
    def Fix(self, degree):
        """
        degree - number of points
 
        Returns list of fixed points p. The degree is specified as
        this information is not stored internally.
        """
        points = []
        for i in range(perm.PERM_BASE, degree + 1):
            if self[i] == i:
                # print("fixed i = ", i, "self.size = ", self.size)
                points.append(i)
        return points
 
 
def Test():
    print("TestPerm() Version 0.1.1")
 
    print("Permutations are specified in cycle notation.")
    p = perm((1,2,3,4))
    print("  A single cycle: p = perm([1,2,3,4]) = ", p)
 
    r = perm(1,2,3,4)
    print("Or you can write: r = perm(1,2,3,4) = ", r)
 
    q = perm((1,2), (3,4))
    print("      Two cycles: q = perm((1,2), (3,4)) = ", q)
    print("The cycles are NOT checked for disjointness. So transpositions")
    print("can also be inputted.")
    print()
    print("Some operations and functions available for permutation objects")
    print("       Identity permutation: p.Identity()     =", p.Identity())
    print("            A separate copy: p.Copy()         =", p.Copy())
    print("   Inverse of a permutation: p.Inverse()      =", p.Inverse().Cycles())
    print("Product of two permutations: p * q            =", (p * q).Cycles())
    print(" Conjugate of a permutation: p ^ q            =", p ^ q)
    print("     Order of a permutation: p.Order()        =", p.Order())
    print("        Set of moved points: p.MovedPoints()  =", p.MovedPoints())
    print("        Set of fixed points: p.Fix()          =", p.Fix(4))
    print("     Number of moved points: p.NrMovedPoints()=", p.NrMovedPoints())
    print("    Number of fixed points: p.NrFixedPoints(4)=", p.NrFixedPoints(4))
    print("you have to specify the index of permutation 4.")
    print("           Image of a point: p.Image(3)       =", p.Image(3))
    print("                      or as: 3^p              =", 3^p)
    print("          Image of a vector: [1,2,3,4] ^ p    =", [1,2,3,4]^p)
    print("            Image of points: p.Image([0,2,3]) =", p.Image([0,2,3]))
 
    print("               Cycle counts: p.CycleCounts()  =", p.CycleCounts())
    print("Done !")
 
if __name__ == "__main__":
    Test()
