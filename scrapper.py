from bs4 import BeautifulSoup
import requests
import json
import os

folder_addr = "/mnt/c/Users/ARNAB BHAKTA/Documents/cs/cp/codeforces/challanges/"


class scrapper:
    # def __init__(self):
    contest_meta_data = {}

    def problem_page_scrapper(self, url):
        raw_data = requests.get(url).text
        formatted_data = BeautifulSoup(raw_data, "html5lib")
        problem_code = url.split('/')
        problem_code = problem_code[problem_code.__len__()-1]
        print(formatted_data.find('div', class_="title").text +
              " parsing started ...."+"\n")
        # infile = open(folder_addr + formatted_data.find('table',
        #                                                 class_='rtable').th.a.text.split('#')[1].split(' ')[0]+'/' + url.split('/', 7)[7]+"_in.txt", 'w')

        inputs = formatted_data.find_all('div', class_="input")
        # print("inputs :")
        self.contest_meta_data[problem_code] = inputs.__len__()
        k = 1
        for input_ in inputs:
            infile = open("inputs/"+problem_code + "_in_"+str(k)+".txt", 'w')
            if (input_.pre.find_all('br')).__len__() != 0:
                for item in input_.pre.find_all('br'):
                    infile.write(item.previous_sibling+"\n")
                    # print(item.previous_sibling)
                    # print()
            else:
                infile.write(input_.pre.text)
                # print(input_.pre.text)
            # print()
            infile.close()
            k = k+1
        # print("outputs :")
        k = 1
        outputs = formatted_data.find_all('div', class_="output")
        infile = open("outputs/"+problem_code + ".txt", 'w')
        for output_ in outputs:
            infile.write("test case #" + str(k)+":\n")
            if (output_.pre.find_all('br')).__len__() != 0:
                for item in output_.pre.find_all('br'):
                    infile.write(item.previous_sibling+"\n")
                    # print(item.previous_sibling)
                    # print()
            else:
                infile.write(output_.pre.text)
                # print(output_.pre.text)
            # print()
            k = k+1
        infile.close()
        print(problem_code + " parsing done \n ..........\n")

    def contest_page_scrapper(self, contest_url):
        print("parsing contest page :")
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
        # contest_meta_data = {}
        print("cotest page parsing done \n ..........\n")
        for url in urls:
            self.problem_page_scrapper(url)
        meta_data = open('meta_data.json', 'w')
        json.dump(self.contest_meta_data, meta_data)
        meta_data.close()


# if __name__ == "__main__":
#     dir_name = input("Enter dir name : ")
#     os.chdir(r"C:\Users\ARNAB BHAKTA\Documents\cs\CP\codeforces\challanges")
#     os.mkdir(dir_name)
#     os.chdir(dir_name)
#     os.mkdir('inputs')
#     os.mkdir('outputs')
#     print("Current changed to " + os.getcwd())

#     contest_meta_data = {}

#     contest_url = "https://codeforces.com/contest/1374"
#     contest_page_scrapper(contest_url)

#     # url = "https://codeforces.com/contest/1374/problem/E1"
#     # problem_page_scrapper(url)

#     print(contest_meta_data)
#     meta_data = open('meta_data.json', 'w')
#     json.dump(contest_meta_data, meta_data)
#     meta_data.close()
