import os
from flask_limiter import Limiter
from flask import Flask, request, make_response
from flask_limiter.util import get_remote_address

from utils.security import DataSecurity


app = Flask(__name__)
limiter = Limiter(key_func=get_remote_address, app=app)


@app.route("/upload", methods=["POST", "PUT"])
@limiter.limit("20/minute")
def upload():
    file = request.files["file"]
    data = DataSecurity.save_file(file.stream.read())
    key = DataSecurity.encrypt_key(data[1], data[2])

    return {"file": data[0], "key": key}


@app.route("/getfile", methods=["POST"])
@limiter.limit("20/minute")
def getfile():
    file = request.get_json()
    key, iv = DataSecurity.decrypt_key(file["key"])
    data = DataSecurity.get_file(key, iv, file["file"])

    return make_response(data)


if __name__ == "__main__":
    if "files" not in os.listdir():
        os.mkdir("files")

    PORT = 8080
    HOST = "127.0.0.1"

    app.run(host=HOST, port=PORT)
