import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class NewsScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Specifični selektori za "mytrendyphone.rs"
            post_link_element = soup.select_one('#aboutUs .HeaderText.twelve.columns.external_page_wrapper .about_us a')
            if post_link_element:
                relative_url = post_link_element['href']
                full_url = urljoin(self.url, relative_url)  
                
                # Prikupljanje sadržaja sa linka
                post_response = requests.get(full_url)
                post_soup = BeautifulSoup(post_response.content, 'html.parser')
                post_content_elements = post_soup.select('#egneside_wrapper p')
                
                if post_content_elements:
                    content = ' '.join([element.get_text(strip=True) for element in post_content_elements])
                    return content
            
            # Generičko skrapovanje sadržaja za druge URL-ove
            paragraphs = soup.find_all('p')
            if paragraphs:
                content = ' '.join([p.get_text(strip=True) for p in paragraphs])
                return content
            
            # Ako nijedan selektor nije pronađen
            return "Nije pronađen sadržaj na zadatoj stranici."
        
        else:
            print(f"Greška: HTTP status kod {response.status_code}")
            return f"Neuspešan zahtev. Status kod: {response.status_code}"
