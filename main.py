import scrapper
import tester_win
import json
import os

settingsjson = open('settings.json', 'r')
settings = json.load(settingsjson)
settingsjson.close()

contest_url = settings['contest_url']
problem_url = settings['problem_url']
with open('source_location.txt', 'r') as src_:
    path = src_.read()
scrapper = scrapper.scrapper()

if os.listdir().count('runtime') != 0:
    for root, dirs, files in os.walk('runtime', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
else:
    os.mkdir('runtime')
os.chdir('runtime')
os.mkdir('inputs')
os.mkdir('outputs')


if(contest_url != ''):
    scrapper.contest_page_scrapper(contest_url)
else:
    scrapper.problem_page_scrapper(problem_url)

user_input = ''
tester = tester_win.tester(path)
while True:
    user_input = input("input : ")
    if user_input == 'exit':
        break
    try:
        if(os.listdir().count('your_output_temp.txt')) != 0:
            os.remove('your_output_temp.txt')
        tester.tester(user_input)
    finally:
        continue
