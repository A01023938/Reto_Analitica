# Semana Tec TC1002S.2
***Integrantes***
- Mateo Gonzalez Cosio - A01023938
- Jose Salgado - A01023661
- Carolina Ortega - A01025254
- Rodrigo Aviles - A01023707

En este reto implementamos el algoritmo de clustering k-means en Python. Mediante un repositorio compartido en GitHub pudimos trabajar de forma remota.  
El código se implementa con el data de iris que se descargó de internet.

# Funcionamiento del código

Nuestro código empieza con una función de distancia en la cual se reciben dos listas y la función regresa el valor de la distancia euclidiana entre ellas. Al empezar a programar esta parte , primero optamos por que las listas fueran puestas por el usuario pero el problema fue que había casos en los que el programa copiaba listas y las sustituía en otro lugar. Optamos por quitar estos inputs y mejor usar datos directos.

    return d_squared**(1/2)

Usamos una función get_clusters que utiliza los puntos como una lista de (x,y) y el centro que queremos obtener será una lista de k listas (x,y).  Cada punto se compara con todos los centros y se guarda la distancia entre ellos. Se utiliza un for para que a la lista vacía se le agregue la información de los puntos donde están los centros. Los puntos seleccionados serán los que están más cerca de los centros.

    clusters[pos].append(punto)
    
La función center recibe la lista de k listas denominada como cluster. Con esta función queremos obtener los puntos donde estarán los nuevos centros , después de calcular el promedio se agrega a la nueva lista.

    cluster_f.append(avg.tolist())
    
Al implementar k_means se llegó a implementar de manera manual con random y con iris.
La función k_means con random genera todos los puntos , los centros y los clusters de manera aleatoria de puntos que estén en las coordenadas que se quieran generar. El usuario selecciona el número de coordenadas a generar , las veces que desea reajustar los centros (iteraciones) y el número de centros que quiere obtener.





Los centros son puntos representativos ya que reciben la información de la lista de los puntos , luego esos puntos los reemplazamos con el promedio de ellos mismos para así tomarlos como los nuevos centros.

El valor de k lo tomamos como el número de clusters que obtuvimos, k se implementa en el algoritmo de k-means para poder completar la función.

El valor de los centros no tiene una repercusión importante en el funcionamiento de las variables y funciones ya que si es más alto o más bajo lo único que hace el centro es tomar esos valores y para definir nuevos puntos y centros sin importar su signo.

¿Qué distancia tienen los centros entre sí? ¿Hay alguno que este muy cercano a otros?


¿Qué pasaría con los centros si tuviéramos muchos outliers en el análisis de cajas y bigotes?


¿Qué puedes decir de los datos basándose en los centros?


## Gráficas 
Se grafican los puntos y los centros para una mejor visualización de los datos.

