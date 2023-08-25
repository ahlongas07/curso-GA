import os
def main():
    print("Hola Mundo")
    username = os.getenv("USERNAME")
    print("Hola," + {username}+ "es tu nombre de GitHub")

if __name__== "__main__":
    main()