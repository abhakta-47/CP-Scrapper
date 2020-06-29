# CP-Scrapper
Python script to scrap input output from problems of Codeforces Contest <br/>
## Requiremets :
 1. bs4
 2. requests
 3. html5lib
 
 **command** : 
```
 pip3 install bs4 requests html5lib
```
 
 ## How to Use :
 - for full contest : in __ main__ change ***contest url*** to required url
 ```
    contest_url = " <contest url> "
    contest_page_scrapper(contest_url)
    # url = "https://codeforces.com/contest/1374/problem/B"
    #problem_page_scrapper(url)
   ```
  - for particular problem : in __ main__ change ***problem url*** to required url
  ```
    #contest_url = " <contest url> "
    # contest_page_scrapper(contest_url)
    url = " <problem url> "
    problem_page_scrapper(url)
  ```
