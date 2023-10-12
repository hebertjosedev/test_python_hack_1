"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    resultado_1 = result.replace('o','0')
    resultado_2 = resultado_1.replace('i','1')
    resultado_3 = resultado_2.replace('a','@')
    resultado_4 = resultado_3.upper()
    resultado_final = list(resultado_4)
    return resultado_final  