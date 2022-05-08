if (__name__ == "__main__"):
    import json

    RUTA= "C:/Users/adri_/OneDrive/Documentos/Adimra/adimra_programacion/semana_11/url.json"

    def recuperarConfigJson(direccion):
        archivo = open(direccion, "r") # r = read = modo solo lectura
        config = json.load(archivo)
        archivo.close()
        return config

    def piloto_1():
        CONFIG = recuperarConfigJson(RUTA)
        print("- Piloto 1")
        print(CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["givenName"],CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["familyName"] )
        print("Victorias:", CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["wins"])
        print("Puntos:", CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["points"])

    def piloto_2():
        CONFIG = recuperarConfigJson(RUTA)
        print("- Piloto 2")
        print(CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][1]["Driver"]["givenName"],CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][1]["Driver"]["familyName"] )
        print("Victorias:", CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][1]["wins"])
        print("Puntos:", CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][1]["points"])    

    def piloto_3():
        CONFIG = recuperarConfigJson(RUTA)
        print("- Piloto 3")
        print(CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][2]["Driver"]["givenName"],CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][2]["Driver"]["familyName"] )
        print("Victorias:", CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][2]["wins"])
        print("Puntos:", CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][2]["points"])

    piloto_1()
    piloto_2()
    piloto_3()







