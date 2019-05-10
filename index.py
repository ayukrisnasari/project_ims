import os
from flask import Flask
from flask import render_template
from pymongo import MongoClient

app = Flask(__name__)


@app.route("/")
def main():
    db_name = "heroku_16n6pr33"
    db_host = "ds155086.mlab.com"
    db_port = 55086
    db_user = "heroku_16n6pr33"
    db_pass = "lel3si28f9nbcuhs1en5ht67gv"

    client = MongoClient(db_host, db_port)

    db = client[db_name]
    db.authenticate(db_user, db_pass)

    collection = db.mahasiswa
    cursor = collection.find({})

    res = ""

    for mahasiswa in cursor:
        res += mahasiswa["nama"]
        res += "\n"
        res += mahasiswa["nim"]
        res += "\n"
        res += mahasiswa["semester"]
        res += "\n"

        if mahasiswa["jenis_kelamin"] == "L":
            res += "Laki-laki"
        else:
            res += "Perempuan"

        res += "\n\n"

    return render_template("index.html", data=res)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
