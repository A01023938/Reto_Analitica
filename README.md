# Semana Tec TC1002S.2
***Integrantes***
- Mateo Gonzalez Cosio - A01023938
- Jose Salgado - A01023661
- Carolina Ortega - A01025254
- Rodrigo Aviles - A01023707

En este reto implementamos el algoritmo de clustering k-means en Python. Mediante un repositorio compartido en GitHub pudimos trabajar de forma remota.  

Nuestro código empieza con una función de distancia en la cual se reciben dos listas y la función regresa el valor de la distancia euclidiana entre ellas.

'''python
def distance(list1, list2):
    return d_squared**(1/2)
'''

¿Crees que estos centros puedan ser representativos de los datos? ¿Por qué?
Los centros son puntos representativos ya que reciben la información de la lista de los puntos , luego esos puntos los reemplazamos con el promedio de ellos mismos para así tomarlos como los nuevos centros.

¿Cómo obtuviste el valor de k a usar?
El valor de k lo tomamos como el número de clusters que obtuvimos, k se implementa en el algortimo de k-means para poder completar la función.

¿Los centros serían más representativos si usaras un valor más alto? ¿Más bajo?
El valor de los centros no tiene una repercusión importante en el funcionamiento de las variables y funciones ya que si es más alto o más bajo lo único que hace el centro es tomar esos valores y para definir nuevos puntos y centros sin importar su signo.

¿Qué distancia tienen los centros entre sí? ¿Hay alguno que este muy cercano a otros?


¿Qué pasaría con los centros si tuviéramos muchos outliers en el análisis de cajas y bigotes?


¿Qué puedes decir de los datos basándose en los centros?


## Gráficas 

