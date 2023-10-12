"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    final = 0
    inicio = 6
    while inicio > final:
          inicio-=1
          result.append(inicio)
    return result