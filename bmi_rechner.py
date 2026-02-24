def berechne_bmi():
    print("--- Willkommen beim BMI-Rechner ---")
    try:
        gewicht = float(input("Gewicht in kg (z.B. 75): "))
        groesse = float(input("Groesse in Metern (z.B. 1.75): "))
        bmi = gewicht / (groesse ** 2)
        print(f"\nIhr BMI ist: {bmi:.2f}")
        if bmi < 18.5:
            print("Kategorie: Untergewicht")
        elif 18.5 <= bmi < 25:
            print("Kategorie: Normalgewicht")
        elif 25 <= bmi < 30:
            print("Kategorie: Übergewicht")
        else:
            print("Kategorie: Adipositas")
    except ValueError:
        print("Fehler: Bitte nur Zahlen eingeben.")

if __name__ == "__main__":
    berechne_bmi()