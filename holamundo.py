import os
def main():
    print("Hola Mundo")
    name = os.getenv("USERNAME")
    print("Hola, {name} es tu nombre de GitHub")