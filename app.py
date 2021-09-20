import mouse, keyboard, sys, time
from colorama import init, Fore

#FUNCIONES
def autoClick(secs=1):
    mouse.click("left")
    time.sleep(secs)

def getIntInput():
    value = input(Fore.LIGHTGREEN_EX + "admin@localhost" + Fore.LIGHTWHITE_EX + ":" + Fore.LIGHTBLUE_EX + "/home$" + Fore.LIGHTWHITE_EX + " ")
    try:
        number = float(value)
        if number <= 0:
            raise Exception(Fore.LIGHTRED_EX + "Ingresa solo numeros positivos\n")
        return number
    except ValueError:
        print(Fore.LIGHTRED_EX + """Asegurate de escribir solo el numero de segundos, algunos ejemplos:
            5 -     Establece un intervalo de 5 segundos
            2.0 -   Establece un intervalo de 2 segundos
            0.25 -  Establece un intervalo de 25 milisegundos""")
        return getIntInput()
    except Exception as e:
        print(e)
        return getIntInput()

def main():
    print("""
    Ingrese el intervalo de segundos entre cada click (por default es 1 segundo)
    Protip: Para especificar milisegundos, puede poner decimales""")
    seconds = getIntInput()

    print(Fore.LIGHTYELLOW_EX + "Inicializando el autoclicker")
    time.sleep(3)

    print(Fore.LIGHTWHITE_EX + "Presiona Shift + z para empezar a clickear")
    while True:
        if keyboard.is_pressed("shift+z"): #Presionar shift + z para empezar el autoclicker
            print(Fore.LIGHTGREEN_EX + "Iniciando autoclicker, presiona Shift + x para finalizar")
            seguir = True
            while seguir:
                autoClick(seconds)
                if keyboard.is_pressed("shift+x"):
                    print(Fore.LIGHTRED_EX + "Finalizando autoclicker")
                    seguir = False



#Flujo de la aplicacion
init(autoreset=True) #Reinicia el color de los string en el CMD de windows al default
print(Fore.GREEN + """
    _         _             _ _      _             
   / \  _   _| |_ ___   ___| (_) ___| | _____ _ __ 
  / _ \| | | | __/ _ \ / __| | |/ __| |/ / _ \ '__|
 / ___ \ |_| | || (_) | (__| | | (__|   <  __/ |   
/_/   \_\__,_|\__\___/ \___|_|_|\___|_|\_\___|_|

                    Version: 1.0
            Desarrollado por: Edgar Oviedo
        Github: https://github.com/EdgarOviedo
""")

main()