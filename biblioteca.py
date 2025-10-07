import csv
def carica_da_file(file_path):
    """Carica i libri dal file"""
    file_biblio = open(file_path, 'r', encoding = 'utf-8')
    lettore = csv.reader(file_biblio, delimiter = ',')
    numero_sezioni = int(next(lettore[0]))
    biblioteca = {}
    for i in range(1, numero_sezioni+1):
        biblioteca[i] = []
    for riga in lettore:
        biblioteca[int(riga[-1])].append(riga[:-1])
    file_biblio.close()
    return biblioteca



def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    try:
        if titolo in biblioteca:
            print('Il libro è già presente nella biblioteca')
        else:
            file_biblio = open(file_path, 'a', newline = '', encoding = 'utf-8')
            writer = csv.writer(file_biblio)
            riga_agg = [titolo, autore, anno, pagine]
            writer.writerow(riga_agg)
            biblioteca[sezione].append(riga_agg)
            file_biblio.close()
            return True
    except FileNotFoundError:
        return None



def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    for sezione in biblioteca:
        lista_libri = biblioteca[sezione]
        for libro in lista_libri:
            if libro[0] == titolo:
                return f"{libro[0]}, {libro[1]}, {libro[2]}, {libro[3]}, {sezione}"
    return None

def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    lista_libri = []
    for j in range(len(biblioteca[sezione])):
        titolo = biblioteca[sezione][j][0]
        lista_libri.append(titolo)
        lista_libri.sort()
        return lista_libri


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

