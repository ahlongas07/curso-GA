import os

def main():
    print("Hola Mundo")
    username = os.getenv("USERNAME")
    print("Hola, " + username + " es tu nombre de GitHub e!")
    print("Esta sería la otra forma: "+ os.getenv("USERNAME") + " de imprimir una variable de ambiente")

if __name__== "__main__":
    main()