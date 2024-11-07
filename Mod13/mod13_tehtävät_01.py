from operator import truediv

from flask import Flask, Response
import json


app = Flask(__name__)

@app.route('/')
@app.route('/alkuluku/<int:num>')


def alkuluku(num):
    try:
        alkuluku = True
        if num <1:
            alkuluku = False

        for i in range(2, num):
            if num % i == 0:
                alkuluku = False

        tilakoodi = 200
        if not alkuluku:
            vastaus = {
                "num" : num,
                "alkuluku" : alkuluku
            }
        else:
            vastaus = {
                "num" : num,
                "alkuluku" : alkuluku
            }

        jsonvastaus = json.dumps(vastaus)
        return vastaus


    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)