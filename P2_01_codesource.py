import requests
from bs4 import BeautifulSoup
import csv
import shutil

#download image to specified file path
def image_downloader(url, file_path, file_name):
    response = requests.get(url, stream=True)
    with open(file_path + "/" + file_name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

#get absolute url of a book from the relative url
def convert_book_relative_url_to_book_absolute_url(relative_url):
    return "https://books.toscrape.com/catalogue/" + relative_url.removeprefix('../../../')

#remove last part of category so that week can add href that will direct to the next page of the url
def remove_last_part_of_url(category_url):
    return "/".join(category_url.split("/")[:-1])

#convert the a number in words to a number as a digit
def word_to_number2(nb_word):
    return {
        "Zero": 0,
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }[nb_word]

# return only the number of books available as an integer
def number_only(number_available):
        number_available = number_available.removeprefix('In stock (')
        number_available = number_available.removesuffix(' available)')
        return (number_available)

# Transform relative image url to absolute image url
def remove_suffix(image_url):
        image_url = image_url.removeprefix('../../')
        real_image_url = "https://books.toscrape.com/" + image_url
        return real_image_url
#scrap all the category links from the main site url(base url)
def scrap_site_category_links(base_url):
    response = requests.get(base_url)
    page = response.content
    soup = BeautifulSoup(page, "html.parser")
    category_links = []
    for category_link in soup.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li'):
        href = category_link.a.get('href')
        # url of the category
        url = ["https://books.toscrape.com/{}".format(href)]
        category_links.append(url)
    return category_links

#returns the name of a category to use as the title of the category CSV
def get_category_name(category_link):
    reponse = requests.get(category_link)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    category_name = soup.find("div", class_="page-header action").find("h1").text
    return category_name

#scrape all the links in a category from the category link
def scrap_book_links(category_link):

    #list where the links  of the books will be stored
    book_links = []

    while True:
        #check to see if url was successfully gotten (if ok response=200,otherwise 404)
        response = requests.get(category_link)

        #get the content of the page as html  and saves it in an object called page
        page = response.content

        #since the content of the page is in html we want to convert from html to page content we can actually work with , for this we use BeautifulSoup to parse(converting information into a format that's easier to work with) the html
        soup = BeautifulSoup(page, "html.parser")

        #in the parsed html all children of the parent article,because this is where all the oinformation we need is
        class_with_all_the_info_we_need_links_we_want = soup.find_all('article')

        #links are found in the a href ,so that is where we willl tell it to look
        #in the class with the info we need , we take each element (these elements in the list are called the stuff) that we need and add it to the list
        book_links += [convert_book_relative_url_to_book_absolute_url(the_stuff.find('a')['href']) for the_stuff in class_with_all_the_info_we_need_links_we_want]

        #check whether there exists a next button
        if a := soup.select_one(".next > a"):
            category_link = remove_last_part_of_url(category_link) + "/" + a["href"]
        else:
            break
    return book_links

def scrap_book_info(book_url):
    reponse = requests.get(book_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")

    return {
        "product_page_url": book_url,
        "upc": soup.select_one("table tr:nth-child(1) > td").text,
        "title": soup.select_one("article  div.col-sm-6.product_main > h1").text,
        "price_including_tax": soup.select_one("table tr:nth-child(4) > td").text,
        "price_excluding_tax": soup.select_one("table tr:nth-child(3) > td").text,
        "number_available": number_only(soup.select_one("#content_inner > article > table  tr:nth-child(6) > td").text),
        "product_description": soup.select_one("article > p").text,
        "category": soup.select_one("#default > div > div > ul > li:nth-child(3) > a").text,
        "review_rating": word_to_number2(soup.select_one(".star-rating")["class"][1]),
        "image_url": remove_suffix(soup.select_one("#product_gallery img")["src"]),

}

def main():
    all_books = []
    base_url = "https://books.toscrape.com/index.html"
    category_links = scrap_site_category_links(base_url)
    category_links = [''.join(ele) for ele in category_links]

    for category_link in category_links:
        book_links = scrap_book_links(category_link)

        headings = ["product_page_url", "upc", "title", "price_including_tax", "price_excluding_tax",
                    "number_available", "product_description", "category", "review_rating", "image_url"]

        with open(get_category_name(category_link) + ".csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headings)
            writer.writeheader()

            for book_link in book_links:
                book = scrap_book_info(book_link)
                writer.writerow(book)

                image_downloader(book["image_url"], "/Users/user/PycharmProjects/webscraping_run_code/Books_to_Scrape_Images", book["upc"] + ".png")

main()





