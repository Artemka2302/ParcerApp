from flask import Flask, render_template, request, jsonify
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secret-key-here'


@app.route('/')
def index():
   
    return render_template('index.html', 
        title="Главная страница",
        user_name="Артем",
        items=['Python', 'Flask', 'Jinja']
    )


if __name__ == '__main__':
    app.run(debug=True)