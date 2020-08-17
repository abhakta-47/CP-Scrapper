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

**1. changing settings.json :**

- **_contest url :_** for full contest in settings.json change its value to contest url

```
 {
  "contest_url": "https://codeforces.com/contest/1374",
  "problem_url": ""
 }
```

- **_problem url :_** for particular problem in settings.json change its value to problem url
  <br> **leave contest_url empty**

```
 {
  "contest_url": "",
  "problem_url": "https://codeforces.com/contest/1374/problem/B"
 }
```

**2. source_location.txt :**
in here put full path where sourc .cpp will be collected for testing, file names should be problem code name ( eg.A.cpp, B.cpp etc) e.g.<br>
(for Linux)

```
~/projects/CompetitiveCodingMyPractices/codeforces/practice/div3 661
```

(for Windows)

```
C:\Users\ARNAB BHAKTA\Documents\cs\CP\codeforces\challanges\div2 654
```

**3. then run main.py**<br>

**4. wait for _input :_ propmt**<br>

**5. in the prompt enter problem code you want to check**<br>
let you entered A, then A.cpp will be collected from the dir specified in source_location.txt, compiled and run against test cases of problem code A.<br>

**6. result should be saved in runtime/report.html. Open with browser to see results.**
<br><br>
Most importantly<br>

## Happy coding :blush: and best of luck :+1:
