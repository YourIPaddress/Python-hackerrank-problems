"""
ABC is a triangle right-angled at B, a bisector from B cuts AC equally at M, Find angle BMC for any input of AB and BC.

"""

import math

AB = int(input())
BC = int(input())

soln = str(round(math.degrees(math.atan(AB/BC))))
print(soln+"\xb0")