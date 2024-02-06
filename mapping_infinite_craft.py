def printMenu():
    print("")
    print("q -> quitter")

def main():
    fini = False
    choix = ""
    while(not fini):
        printMenu()
        choix = input()
        match choix:
            case "q":
                fini = True
            case _:
                print("entré non reconnue")
                print("")

if __name__ == "__main__":
    main()
