import requests
import csv
from bs4 import BeautifulSoup

while True:
    choice = int(input("Print to File - 1\nPrint On Screen - 2 \nExit - 3\nAnswer : "))
    if choice == 3:
        break
    else:
        if choice == 1:
            try:
                def record_file():
                    with open("movies.csv","w",encoding="utf-8",newline="") as file:
                        csv_writer = csv.writer(file)
                        headers =["Movie Rank","Movie Name","History of filmmaking","Rating Of Movie"]
                        url1 = "https://www.imdb.com/chart/toptv/"
                        response = requests.get(url1)
                        soup = BeautifulSoup(response.text,"html.parser")
                        mainİnfo= soup.find('tbody',class_='lister-list').find_all('tr')
                        liste = []
                        for mov in mainİnfo:
                            movieName = mov.a.img["alt"]
                            movieRating = mov.find("td",class_="ratingColumn imdbRating").text.strip()
                            movieRank = mov.span["data-value"]
                            movieDate = mov.find(class_="secondaryInfo").text
                            liste.append([movieRank,movieName,movieDate,movieRating])
                        csv_writer.writerow(headers)
                        csv_writer.writerows(liste)
            except Exception as e:
                print(e)
            finally:
                record_file()
                print("File Writing is successful")
                break
        elif choice == 2 :
            try:
                def print_file():
                    with open("movies.csv",encoding="utf-8") as file:
                        load = csv.reader(file)
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
