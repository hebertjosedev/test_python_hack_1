"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    numero = 1
    bandera = True
    while numero < 6:
        if bandera:
            result.insert(numero, '@')
            numero+=1
            bandera = False
        else:
            numero+=1
            bandera = True
    return result  