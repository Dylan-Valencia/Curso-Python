"""
Declarar variables
"""
Barriles_vino_tinto=50
litros_vino_tinto=2
Barriles_vino_blanco=130
litros_vino_blanco=47
Barriles_vino_rosado=180
litros_vino_rosado=73
srt_vino_tinto="Almacen Juan"
srt_vino_blanco="Almacen Pepe"
srt_vino_rosado="Almacen Dylan"
"""
Calcular el total de barriles y aplicar la plantilla: "Tenemos un total de {número de barriles} barriles" 
"""
Total_numero_de_barriles=Barriles_vino_blanco+ Barriles_vino_tinto + Barriles_vino_rosado
texto="tenemos un total de {} barriles.".format(Total_numero_de_barriles) 
"""
Calcular los litros de vino y aplicar la plantilla: "El {nombre_almacen} tiene {cantidad_litros} litros"
"""
Total_litros_vino_tinto=Barriles_vino_tinto*litros_vino_tinto
Total_litros_vino_blanco=Barriles_vino_blanco*litros_vino_blanco
Total_litros_vino_rosado=Barriles_vino_rosado*litros_vino_rosado
texto_tinto="El {srt_vino_tinto} tiene {}.".format(Total_litros_vino_tinto)
texto_blanco="El {srt_vino_blanco} tiene {}.".format(Total_litros_vino_blanco)
texto_rosado="El {srt_vino_rosado} tiene {}.".format(Total_litros_vino_rosado)
"""
Calcular e imprimir la comparación de litros entre los diferentes almacenes
"""
es_verdad=total_litros_vino_tinto<Total_litros_vino_blanco
es_verdad=total_litros_vino_blanco<Total_litros_vino_rosado
es_verdad=total_litros_vino_rosado<Total_litros_vino_tinto
