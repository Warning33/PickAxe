import webbrowser
import urllib.parse
import requests
from bs4 import BeautifulSoup




print('''                             
 _____ _     _   _____         
|  _  |_|___| |_|  _  |_ _ ___                    
|   __| |  _| '_|     |_'_| -_|
|__|  |_|___|_,_|__|__|_,_|___| v.1             
     The Internet Digger 

    +----------------+
    |    By ZKRIM    |
    |      2K23      |
    +----------------+

''')

def search_on_browser(search_term):
    # Encodage du terme de recherche pour les URL
    encoded_search_term = urllib.parse.quote(search_term)

    # URL de recherche sur Google (vous pouvez modifier l'URL pour utiliser un autre moteur de recherche)
    search_url = f"https://www.google.com/search?q={encoded_search_term}"

    # Ouvrir le navigateur avec l'URL de recherche
    webbrowser.open(search_url)

def get_number_of_results(search_term):
    encoded_search_term = urllib.parse.quote(search_term)
    search_url = f"https://www.google.com/search?q={encoded_search_term}"
    response = requests.get(search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        result_stats = soup.find("div", {"id": "result-stats"})
        if result_stats:
            num_results = result_stats.get_text()
            return num_results
    return "Nombre de résultats non disponible."

def sous_menu_fonction_1():
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    search_term = f'intext:"{prenom} {nom}"'
    num_results = get_number_of_results(search_term)
    print(f"Nombre de résultats trouvés sur Google : {num_results}")
    search_on_browser(search_term)

def sous_menu_fonction_2():
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    search_term = f'inurl:"{prenom} {nom}"'
    num_results = get_number_of_results(search_term)
    print(f"Nombre de résultats trouvés sur Google : {num_results}")
    search_on_browser(search_term)

def sous_menu_fonction_3():
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    search_term = f'{prenom} {nom} site:youtube.com | site:instagram.com | site:twitter.com | site:linkedin.com | site:tiktok.com | site:facebook.com'
    num_results = get_number_of_results(search_term)
    print(f"Nombre de résultats trouvés sur Google : {num_results}")
    search_on_browser(search_term)

def sous_menu_fonction_4():
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    search_term = f'intext:"{prenom} {nom}" filetype:pdf'
    num_results = get_number_of_results(search_term)
    print(f"Nombre de résultats trouvés sur Google : {num_results}")
    search_on_browser(search_term)

def afficher_sous_menu_fonction_1():
    while True:
        print("\n----------> IDENTITY TRACKING MENU <----------\n")
        print("-> 1. Text Searching")
        print("-> 2. Title Searching")
        print("-> 3. Social Networks Searching")
        print("-> 4. Document Searching")
        print("-> 5. Main Menu\n")

        choix_sous_menu_fonction_1 = input("Choose An Option (1-5) : ")

        if choix_sous_menu_fonction_1 == "1":
            sous_menu_fonction_1()
        elif choix_sous_menu_fonction_1 == "2":
            sous_menu_fonction_2()
        elif choix_sous_menu_fonction_1 == "3":
            sous_menu_fonction_3()
        elif choix_sous_menu_fonction_1 == "4":
            sous_menu_fonction_4()
        elif choix_sous_menu_fonction_1 == "5":
            break
        else:
            print("Invalid Choice. Please Enter A Valid Number (1-5).")

def fonction_1():
    while True:
        print("\n----------> MENU <----------:")
        print("-> 1. Identity Tracking")
        print("-> 2. Username Tracking")
        print("-> 3. Quit\n")

        choix_fonction_1 = input("Choose An Option (1-3) : ")

        if choix_fonction_1 == "1":
            afficher_sous_menu_fonction_1()
        elif choix_fonction_1 == "2":
            fonction_2()
        elif choix_fonction_1 == "3":
            break
        else:
            print("Invalid Choice. Please Enter A Valid Number (1-3).")

def fonction_2():
    username = input("Username : ")
    search_term = f'{username} site:youtube.com | site:instagram.com | site:twitter.com | site:tiktok.com | site:facebook.com'
    num_results = get_number_of_results(search_term)
    print(f"Nombre de résultats trouvés sur Google : {num_results}")
    search_on_browser(search_term)

if __name__ == "__main__":
    fonction_1()
