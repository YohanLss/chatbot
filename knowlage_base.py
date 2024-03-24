from bs4 import BeautifulSoup
import requests

#permet de stocker les données importants
def create_knowledge_base(soup):
    knowledge_base = {}
    for header in soup.find_all(['h1', 'h2', 'h3']):
        key = header.text.strip()
        value = [p.text.strip() for p in header.find_next_siblings('p')]
        knowledge_base[key] = value
    return knowledge_base


def scrape_website(url):
    # Faites une requête GET à l'URL spécifiée
    response = requests.get(url)

    # Vérifiez si la requête a réussi
    if response.status_code == 200:
        # Utilisez BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Exemple d'extraction de titres
        titles = soup.find_all('h1')  # Trouver tous les éléments <h1>
        for title in titles:
            print("Titre:", title.text.strip())

        # Exemple d'extraction de paragraphes
        paragraphs = soup.find_all('p')  # Trouver tous les éléments <p>
        for paragraph in paragraphs:
            print("Paragraphe:", paragraph.text.strip())

        # Exemple d'extraction de liens
        links = soup.find_all('a')  # Trouver tous les éléments <a>
        for link in links:
            print("Lien:", link.get('href'))

        # Exemple d'extraction d'images
        images = soup.find_all('img')  # Trouver tous les éléments <img>
        for image in images:
            print("Image:", image['src'])

        # Appeler la fonction create_knowledge_base avec l'objet soup comme argument
        knowledge_base = create_knowledge_base(soup)

        # Maintenant, vous pouvez utiliser la base de connaissances créée
        # Par exemple, imprimez les clés et les valeurs
        for key, value in knowledge_base.items():
            print(f"Clé : {key}")
            print(f"Valeur : {value}")

        

    else:
        print("La requête a échoué:", response.status_code)



# Appeler la fonction scrape_website avec l'URL
url = 'https://liveyourz.art/'
soup=scrape_website(url)


# Maintenant, vous pouvez utiliser l'objet soup retourné par scrape_website
# Appeler la fonction create_knowledge_base avec cet objet soup comme argument
knowledge_base = create_knowledge_base(soup)

# Maintenant, vous pouvez utiliser la base de connaissances créée
# Par exemple, imprimez les clés et les valeurs
for key, value in knowledge_base.items():
    print(f"Clé : {key}")
    print(f"Valeur : {value}")
