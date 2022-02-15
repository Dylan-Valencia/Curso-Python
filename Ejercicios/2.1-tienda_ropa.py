"""
Aplicar la plantilla: "{ropa} cuesta {numero} euros" a dos prendas de ropa
"""
plantilla="{ropa}:\n cuesta {valor} euros."
texto_limpio1=plantilla.format(ropa="pantalon", valor="doce")
texto_limpio2=plantilla.format(ropa="camiseta", valor="diez")
"""
Aplicar la plantilla: "Su carro de la compra tiene: <formato_aplicado1> y <formato_aplicado2>"
"""
plantilla_2="Su carro de la compra tiene {} y {}." .format(plantilla)
