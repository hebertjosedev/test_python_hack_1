"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    resultado_nuevo = result.replace("n","N")
    return resultado_nuevo
