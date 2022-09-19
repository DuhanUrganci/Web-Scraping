
import requests
import json
from bs4 import BeautifulSoup

url = "https://onedio.com/?ysclid=l88xvk0h7y382589410"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
topics = soup.find_all("div",class_="o-linkbox relative article-card-wrapper",limit=20)
while True:
    choice = int(input("Print to File - 1\nPrint On Screen - 2 \nExit - 3\nAnswer : "))
    if choice == 3:
        break
    else:
        if choice == 1:
            try:
                def record_file():
                    with open("onedio.json","w",encoding="utf-8") as file:
                        base = []
                        for pro in topics:
                            headers = pro.find(class_="sm:font-bold text-primary-100 text-xl leading-22").text.strip()
                            newsLink = "https://onedio.com/"+pro.find(class_="sm:font-bold text-primary-100 text-xl leading-22").a["href"]
                            newResponse = requests.get(newsLink)
                            newsSoup = BeautifulSoup(newResponse.text,"html.parser")
                            author = newsSoup.find("span",class_="text-link-primary text-sm sm:font-bold").text
                            subject = newsSoup.find("span",class_="text-sm text-primary-300").text
                            newsDesc= newsSoup.find("p").text
                            base.append({
                                "Title":headers,
                                "News Author":author,
                                "News Subject":subject,
                                "News Content":newsDesc,
                                "News Link":newsLink
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
                    with open("onedio.json",encoding="utf-8") as file:
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
