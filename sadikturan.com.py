import requests
from bs4 import BeautifulSoup
import csv


url= "https://sadikturan.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

listOfCours = soup.find_all(class_="card kurs")



while True:
    choice = int(input("Print to File - 1\nPrint On Screen - 2 \nExit - 3\nAnswer : "))
    if choice == 3:
        break
    else:
        if choice == 1:
            try:
                def record_file():
                    with open("kurs.csv","w",encoding="utf-8",newline="") as file:
                        csv_writer = csv.writer(file)
                        liste = []
                        for course in listOfCours:
                            courseTitle=course.h2.text
                            courseDescription = course.span.text
                            coursePicture = course.img.get("src")
                            UdemyLink = course.a.get("href")
                            siteLink = course.find_all("a")[1]["href"]
                            liste.append([courseTitle,courseDescription,coursePicture,UdemyLink,siteLink])
                        csv_writer.writerow(["Course Name","Course Description","Course Picture","Udemy Connection","Course site link"])
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
                    with open("kurs.csv",encoding="utf-8") as file:
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