def my_functionlecture():
    print("Starting program")
    print("bonjour je vais bien")
    print("Ending program")
    fichier = open("test.txt","w+")
    fichier.read("bonjour")
    fichier.close
    return


def my_functionecriture():
    fichier = open("test.txt","w+")
    fichier.write("bonjour")
    fichier.close
    return


if __name__ == "__main__":

    print("hello world")

my_functionlecture()

my_functionecriture()
      
    

