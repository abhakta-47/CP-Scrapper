# CP-Scrapper

Python script to scrap input output from problems of Codeforces Contest <br/>

## Requiremets :

1.  bs4
2.  requests
3.  html5lib

**command** :

```
 pip3 install bs4 requests html5lib
```

## How to Use :

- **_contest url :_** for full contest in settings.json change its value to contest url

```
 {
  "contest_url": "https://codeforces.com/contest/1374",
  "problem_url": "",
  "platform": "",
  "path": ""
 }
```

- **_problem url :_** for particular problem in settings.json change its value to problem url
  <br> **leave contest_url empty**

```
 {
  "contest_url": "",
  "problem_url": "https://codeforces.com/contest/1374/problem/B",
  "platform": "",
  "path": ""
 }
```

- **_source_location.txt :_** in here put full path where sourc .cpp will be collected for testing, file names should be problem code naem ( eg.A.cpp, B.cpp etc)
