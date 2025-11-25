#COMO USAR PANDAS PARA CREAR FILTROS

#1. importarlo
import pandas as pd

#2. traer los datos
from data.simulador import generar_ventas

#3. convertir los datos en un DATAFRAME
dataFrame=pd.DataFrame(generar_ventas())

#4. aplciar los filtros (5)
print(dataFrame)

#yo como administrador de la tienda quiero obtener las ventas de enero
#yo como administrador de la tienda quiero ver ventas con mas de tres productos 
#yo como administrador de la tienda quiero ver ventas por valores de mas de 900.000 pesos
#yo como administrador de la tienda quiero ver las ventas de la camisetas Polo
#yo como administrador de la tienda quiero ver las ventas de los productos menos vendidos.

