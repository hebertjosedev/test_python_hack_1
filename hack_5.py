"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    resultado_primero = result.replace("o","0")
    resultado_segundo = resultado_primero.replace("i","1")
    resultado_ultimo = resultado_segundo.replace("a","@")
    return resultado_ultimo 