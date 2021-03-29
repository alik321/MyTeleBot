# импортируем библиотеки

from bs4 import BeautifulSoup
import requests
import json


# получем доступ к элементам страницы
def get_html(url):
    responce = requests.get(url)
    return responce.text


# запись данных в json формат
def write_to_json(data):
    with open("my_json_file.json", "a") as json_file:
        file1 = json.dump(data, json_file, ensure_ascii=False, indent=2)


# функция для получения и преоброзования html кода 

def get_data_page(html):
    soup = BeautifulSoup(html, "lxml")
    app_lists = soup.find("div", class_="main catalog").find("div", class_="catalog-list")
    cars = app_lists.find_all("a", class_="catalog-list-item")

    empty_list = []

    for car in cars:
        try:
            title = car.find("span", class_="catalog-item-params").find("span",
                                                                        class_="catalog-item-caption").text.split()
        except:
            title = ''

        try:
            description = car.find("span", class_="catalog-item-descr").text
        except:
            description = ''

        try:
            photo = car.find("span", class_="catalog-item-cover").find("img").get("src")
        except:
            photo = ""

        data = {
            "title": title[0],
            "description": description.replace("\n", "").split(),
            "photo": photo
        }

        empty_list.append(data)
    write_to_json(empty_list)


# главная функция
def main():
    url_cars_kg = 'https://cars.kg/offers'
    get_data_page(get_html(url_cars_kg))


main()
