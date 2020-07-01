import os
import json


# print(type(meta_data))


class tester:
    def __init__(self, path):
        self.path = path

    def build_report(self, problem_id):

        for files in os.walk(os.getcwd()):
            # print(files[2])
            if(files[2].count('report.html') != 0):
                os.remove('report.html')
            break

        with open('report.html', 'w') as report:
            report.write("<h3>"+"testing "+problem_id+".....</h3>\n")
            report.write("<div style=""display:flex;"" >")
            report.write(
                "<div  style=""padding:10px;font-size:15px; >\n<p>Your otput: </p> \n<pre"" > \n"+open("your_output_temp.txt", 'r').read()+" </pre> \n</div>")
            report.write(
                "<div  style=""padding:10px;font-size:15px; >\n<p>Expected otput: </p> \n<pre"" > \n"+open("outputs/" + problem_id + ".txt", 'r').read()+" </pre> \n</div>")
            report.write("</div>")

    def tester(self, problem_id):
        print("testing "+problem_id+".....\n")
        meta_data = open('meta_data.json', 'r')
        meta_data = json.load(meta_data)
        n_tests = meta_data[problem_id]
        k = 1
        found = True
        for files in os.walk(self.path):
            # print(files[2])
            if(files[2].count(problem_id+'.cpp') == 0):
                found = False
            break
        # print(" found?  " + str(found))

        if found:
            os.system("g++ \""+self.path+"\\"+problem_id +
                      ".cpp\" -o "+problem_id+".exe")

            while k <= n_tests:
                print("test case #" + str(k) + ": ")
                os.system("echo test case #" + str(k) +
                          ": >>  your_output_temp.txt")
                in_file = problem_id+"_in_"+str(k)+".txt | "
                (os.system("cat inputs/"+in_file +
                           problem_id+".exe >> your_output_temp.txt"))
                # print(test_result)
                k = k+1
                print()
            self.build_report(problem_id)
        else:
            print(" *.cpp not found")


if __name__ == "__main__":
    with open('source_location.txt', 'r') as src_:
        path = src_.read()
    user_input = ''
    tester_ = tester(path)
    os.chdir("runtime")
    while True:
        user_input = input("input : ")
        if user_input == 'exit':
            break
        try:
            if(os.listdir().count('your_output_temp.txt')) != 0:
                os.remove('your_output_temp.txt')
            tester_.tester(user_input)
        finally:
            continue
