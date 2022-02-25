# CHALLENGE

|  Region | City Name |  Languaje | Time  |
|---|---|---|---|
|  Africa | Angola  |  AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724 | 0.23 ms  |
|   |   |   |   |
|   |   |   |   |

Desarrolle una aplicacion en python que genere la tabla anterior teniendo las siguientes consideraciones:

- De https://restcountries.com/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
- En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
- La tabla debe ser creada en un DataFrame con la libreria PANDAS
- Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
- Guarde el resultado en sqlite.
- Genere un Json de la tabla creada y guardelo como data.json
- La prueba debe ser entregada en un repositorio git.

# SOLUCIÓN

Se creo una clase llamada ***Lang*** la cual contiene:

- Attributos:
  - df: usado para almacenar el dataframe de lenguajes
- Métodos:
  - __init__: Inicaliza un dataframe vacio con las columnas Region, Country, Language, Time.
  - ***create_df***: Crear un dataframe con Pandas apartir de restcountries.com.
  - **store_data_frame**: Almancena un dataframe en la base de datos.
  - create_json_file: Crea un archivo JSON apartir de un dataframe.
  - print_data_frame: Imprime en consola el tiempo minimo, maximo, promedio y total que se tardo en procesar todas las filas de la tabla
- Manejo de errores:
  Para el manejo de errores se implementaron las excepciones en cada uno de los métodos de la clase
  
# Diagrama de flujo

![alt text](https://github.com/victrsanchez/tangelolatam-challenge/blob/master/diagrama_de_flujo.png)
