
def main():
    print("consommation en kw/h :")
    kw = float(input())
    print("prix du kw/h en euros :")
    prix = float(input())
    print("1h : ", kw * prix, " euros")
    print("24h : ", kw * prix * 24, " euros")
    print("30jours : ", kw * prix * 24 * 30, " euros")
    print("par ans : ", kw * prix * 24 * 365, " euros")

main()


