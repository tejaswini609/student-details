from flask import Flask, render_template, request, redirect, url_for, request
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)
fi = open("students.csv", "w")
fi.write("ID, Name, GENDER, DOB, City, State, Email, Qualification, Stream\n")
fi.close()


def search(id):
    read = open('students.csv', 'r')
    for i in read:
        l = i.split(',')
        print(l)
        if len(l) == 9:

            if l[0].strip().lower() == id.strip().lower():
                send_data = {
                    "status": 1,
                    "ID": l[0].strip(),
                    "NAME": l[1].strip(),
                    "GENDER": l[2].strip(),
                    "DOB": l[3].strip(),
                    "CITY": l[4].strip(),
                    "STATE": l[5].strip(),
                    "EMAIL": l[6].strip(),
                    "QUALIFICATION": l[7].strip(),
                    "STREAM": l[8].strip()
                }
                read.close()
                return send_data
    return {"status": 0}


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "POST":

        # print(request.form)
        x = request.form
        data = {
            "ID": x["ID"],
            "NAME": x["NAME"],
            "GENDER": x["GENDER"],
            "DOB": x["DOB"],
            "CITY": x["CITY"],
            "STATE": x["STATE"],
            "EMAIL": x["EMAIL"],
            "QUALIFICATION": x["QUALIFICATION"],
            "STREAM": x["STREAM"]
        }
        verify = search(data["ID"])
        if verify["status"] == 0:
            out = open('students.csv', 'a')

            out.write("{}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(data["ID"],
                                                                    data["NAME"],
                                                                    data["GENDER"],
                                                                    data["DOB"],
                                                                    data["CITY"],
                                                                    data["STATE"],
                                                                    data["EMAIL"],
                                                                    data["QUALIFICATION"],
                                                                    data["STREAM"])
                      )

            out.close()

        return "success"

    if request.method == "GET":

        if len(request.args) == 1:
            send_data = search(request.args["ID"])
            return send_data

        else:
            read = open('students.csv', 'r')
            send1 = {}
            j = 0
            for i in read:

                l = i.split(',')
                print(l)
                if len(l) == 9:
                    if j == 0:
                        j += 1
                        continue
                    send1[j] = {"ID": l[0].strip(),
                                "NAME": l[1].strip(),
                                "GENDER": l[2].strip(),
                                "DOB": l[3].strip(),
                                "CITY": l[4].strip(),
                                "STATE": l[5].strip(),
                                "EMAIL": l[6].strip(),
                                "QUALIFICATION": l[7].strip(),
                                "STREAM": l[8].strip()
                                }
                    j += 1
            read.close()

            return send1

        read.close()
        return {"status": 0}


if __name__ == '__main__':

    app.run(debug=True)
