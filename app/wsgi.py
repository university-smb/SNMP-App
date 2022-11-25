
from app import *
from flask import Flask


app = Flask(__name__)


# lancement de serveur WEB
if __name__ == '__main__':

    #Run web server for APP
    app.run('192.168.56.201')