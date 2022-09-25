import requests
from bs4 import BeautifulSoup

class Amazon:
    url = "https://www.amazon.com.tr/s?k=Android+Telefon&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=LSQVIX9B44OB&sprefix=android+telefon%2Caps%2C201&ref=nb_sb_noss_1"
    def __init__(self):
        self.productList = []
    def get_documents(self):
        while True:
            response = requests.get(self.url)
            code = response.status_code
            if code == 200:
                doc = BeautifulSoup(response.text,"html.parser")
                soup = doc.find_all("div",class_="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20")
                for s in soup:
                    name = s.h2.text
                    price = s.find(class_="a-price-whole").text
                    base = {
                        "Name":name,
                        "Price":price
                    }
                    self.productList.append(base)
                break
            elif code == 503:
                continue
            else:
                break
    def print_to_file(self):
        import json
        self.get_documents()
        with open("Amazon-Beatiful.json","w",encoding="Utf-8",newline="") as file:
            json.dump(self.productList,file,ensure_ascii=False,indent=1) 

p1 = Amazon()
p1.print_to_file()
