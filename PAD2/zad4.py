import random

class Game():
    def __init__(self,iloscGraczy):
        self.iloscGraczy = iloscGraczy

    def play(self):
        print("START GRY")
        if self.iloscGraczy == 1:
            print("WYBRANO TRYB JEDNOOSOBOWY")
        elif self.iloscGraczy == 2:
            print("WYBRANO TRYB DWU-OSOBOWY")

class Hangman(Game):
    def __init__(self,iloscGraczy):
        super().__init__(iloscGraczy)
        
def main():
    print("WITAJ W GRZE")
    print("WYBIERZ TRYB GRY")
    print("1-single")
    print("2-multi")
    mode=0
    gamemode = int(input())
    if gamemode == 1 :
        mode = 1
    if gamemode == 2 :
        mode = 2
    
    wisielec = Hangman(mode)
    print("WYBIERZ POZIOM TRUDNOŚCI")
    print("1-beginner")
    print("2-intermediate")
    print("3-advanced")
    zycia=0
    level = int(input())
    if level==1:
        zycia=8
    if level ==2:
        zycia =5
    if level == 3:
        zycia=3
    wisielec.play()
    if mode == 1 :
            print("MASZ" ,zycia, "ŻYĆ")

            lista = ["ania", "banan", "luz", "pies", "obi"]
            haslo = str(lista[random.randint(0, len(lista) - 1)])
            tablica = list(haslo)

            for i in range(len(haslo)):
                tablica[i] = "_"

            while zycia > 0:
                print("")
                print( "POZOSTAŁO CI ",zycia , "ŻYĆ")
                print("")
                print(" ".join(tablica))
                print(" ")

                print("PODAJ LITERE: ")
                litera = input()

                if litera in haslo:
                    for i in range(len(haslo)):
                        if haslo[i] == litera:
                            tablica[i] = litera
                    if "".join(map(str, tablica)) == haslo:
                        print("")
                        print("POZOSTAŁO CI ",zycia , "ŻYĆ")
                        print("")
                        print(" ".join(tablica))
                        print(" ")
                        print("WYGRAŁEŚ!")
                        break
                else:
                    zycia -= 1
    elif mode ==2:
            print("NIECH GRACZ PIERWSZY PODA HASŁO:")
            haslo = input()
            tablica = list(haslo)
            print("GRACZ 2 BĘDZIE ZGADYWAŁ I MA :", zycia, "ŻYĆ")
            for i in range(len(haslo)):
                tablica[i] = "_"

            while zycia > 0:
                print("")
                print("POZOSTAŁO CI ",zycia , "ŻYĆ")
                print("")
                print(" ".join(tablica))
                print(" ")

                print("PODAJ LITERE: ")
                litera = input()

                if litera in haslo:
                    for i in range(len(haslo)):
                        if haslo[i] == litera:
                            tablica[i] = litera
                    if "".join(map(str, tablica)) == haslo:
                        print("")
                        print("POZOSTAŁO CI ",zycia , "ŻYĆ")
                        print("")
                        print(" ".join(tablica))
                        print(" ")
                        print("WYGRAŁEŚ!")
                        break
                else:
                    zycia -= 1


if __name__ == "__main__":
    main()