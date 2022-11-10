
from flask import Flask, render_template, request, session, redirect, send_from_directory
import json



# import functions



app = Flask(__name__)

# secret key for session (mandatory)
app.secret_key = "session is used in this application!"



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



