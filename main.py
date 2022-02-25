import pandas as pd
import hashlib
import time
import sqlite3
import requests


class Lang:

    df = None

    def __init__(self):
        print("Creación de la clase");
        

    def create_df(self):
        """
        Este método tiene como objetivo crear un dataframe con la librería de pandas.

        1.- Inicalizar un dataframe vacio con las columnas Region, Country, Language, Time
        1.- Consultar restcountries.com.
        2.- Convertir la respuesta a JSON
        3.- Recorrer cada uno de los registros obtenidos de restcountries.com
        4.- Por cada uno de los registros, inicializar el time para calcular el tiempo de procesamiento de cada renglon.
        5.- Por cada uno de los registros, Inicializar lang en vacío para los paises que no tengan idiomas
        6.- Si el pais que se esta procesando tiene idiomas, primero se contactenan estos separados por comillas y despues se convierten a SHA1
        7.- Se calcula el tiempo que tardo en procesar el renglon y se inserta este renglon en el dataframe, 

        Toda esta información se almance en el atributo df de la clase
        """
        try:
            self.df = pd.DataFrame(columns=['Region','Country','Language','Time'])
            languages_by_contry_response = requests.get("https://restcountries.com/v3.1/all")
            languages_by_contry_json = languages_by_contry_response.json()

            for item in languages_by_contry_json:
                start_time = time.time()
                lang = "";
                if( 'languages' in item ):
                    lang = ", ".join(item['languages'].values())
                    lang = hashlib.sha1(lang.encode()).hexdigest()

                self.df = self.df.append({'Region': item['region'], 'Country': item['name']['official'], 'Language': lang,'Time': time.time() - start_time }, ignore_index=True)
        except:
            print("Error: While creating dataframe")

    def store_data_frame(self):
        """
        Este método tiene como objetivo almacenar un dataframe en una base de datos

        1.- Crear una conexión a la base datos
        2.- Usando el atributo df de la clase, se llama al metodo to_sql pasando como parametros el nombre de la tabla, 
            la conexión a la bd y como tercer parametro append para agregar los nuevos registros a la tabla y no borrar los existentes
        3.- Cerrar conexión
        """
        try:
            connection  = sqlite3.connect("tangelolatam.sql")
            self.df.to_sql('langs',con = connection,if_exists = 'append')
            connection.close()
        except:
            print("Error: While storing data base")

    def create_json_file(self):
        """
        En este método se crea un archivo json con la data del dataframe

        1.- Se llama el método to_json del dataframe pasando como parametro la dirección donde se guardara el archivo generado

        """
        try:
            self.df.to_json(r'.\data.json')
        except:
            print("Error: While creating json file")


    def print_data_frame(self):
        """
        Este metodo es encardo de imprimir el dataframe en consola.

        1.- se imprimen los primeros 5 datos del dataframe
        2.- Se imprime el tiempo minimo, maximo, promedio y total que se tardo en procesar todas las filas de la tabla

        """
        try:
            print("*********************************************************")
            print(self.df.head())
            print("*********************************************************")
            print(self.df.agg({ "Time": ["min", "max","mean","sum"] }))
            print("*********************************************************")
        except:
            print("Error: While printing data")


lang = Lang()

lang.create_df();
lang.create_json_file();
lang.store_data_frame();
lang.print_data_frame();