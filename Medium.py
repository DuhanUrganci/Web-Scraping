import requests
from bs4 import BeautifulSoup
import json

url = "https://medium.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find("div",class_="jv jw y").find_all("div",class_="ae cx") 
while True:
    choice = int(input("Print to File - 1\nPrint On Screen - 2 \nExit - 3\nAnswer : "))
    if choice == 3:
        break
    else:
        if choice == 1:
            try:
                def record_file():
                    with open("medium.json","w",encoding="utf-8") as file:
                        base =[]
                        for med in articles:
                            head = med.h2.text
                            author = med.h4.text
                            descript = med.find(class_="bv b ec bx ct jm jf jg jn ji jk ho").text
                            date = med.span.text
                            base.append({
                                "Head":head,
                                "Author":author,
                                "Description":descript,
                                "Date":date
                            })
                        json.dump(base,file,ensure_ascii=False,indent=1)
            except Exception as e:
                print(e)
            finally:
                record_file()
                print("File Writing is successful")
                break
        elif choice == 2 :
            try:
                def print_file():
                    with open("medium.json",encoding="utf-8") as file:
                        load = json.load(file)
                        for a in load:
                            print(a)
                            print("*"*100)
            except Exception as e:
                print(e)
            finally:
                print_file()
                print("The Reading Process Is Completed")
                break            
        else:
            print("Wrong Choice")
            break
