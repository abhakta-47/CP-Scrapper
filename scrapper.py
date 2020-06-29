from bs4 import BeautifulSoup
import requests


def problem_page_scrapper(url):
    raw_data = requests.get(url).text

    formatted_data = BeautifulSoup(raw_data, "html5lib")
    print(formatted_data.find('div', class_="title").text+"\n")
    inputs = formatted_data.find_all('div', class_="input")
    print("inputs :")
    for input_ in inputs:
        # /print(input_.pre)
        if (input_.pre.find_all('br')).__len__() != 0:
            for item in input_.pre.find_all('br'):
                print(item.previous_sibling)
                # print()
        else:
            print(input_.pre.text)
        print()

    print("outputs :")
    outputs = formatted_data.find_all('div', class_="output")
    for output_ in outputs:
        # /print(input_.pre)
        if (output_.pre.find_all('br')).__len__() != 0:
            for item in output_.pre.find_all('br'):
                print(item.previous_sibling)
                # print()
        else:
            print(output_.pre.text)
        print()


def contest_page_scrapper(contest_url):
    raw_data = requests.get(contest_url).text

    formatted_data = BeautifulSoup(raw_data, "html5lib")

    contest_table = formatted_data.find('table', class_="problems")
    urls = []
    for row in contest_table.find_all('tr'):
        if(row.find_all('td').__len__() != 0):
            urls.append("https://codeforces.com/"+row.td.a.get('href'))
            print("url   ", end=" ")
            print(urls[urls.__len__() - 1], end=" ")
            print("    added")
    print()
    for url in urls:
        problem_page_scrapper(url)


if __name__ == "__main__":
    contest_url = "https://codeforces.com/contest/1374"
    contest_page_scrapper(contest_url)

    # url = "https://codeforces.com/contest/1374/problem/B"
    # problem_page_scrapper(url)
