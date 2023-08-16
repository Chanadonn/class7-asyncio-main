#Ans
# * Serving Flask app '2-multiple_xkcd_comic_flask'
# * Debug mode: on
#WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# * Running on http://127.0.0.1:5555
#Press CTRL+C to quit
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 517-999-963
#127.0.0.1 - - [16/Aug/2023 13:59:54] "GET /comic HTTP/1.1" 200 -
import time
from random import randint
import requests as requests
from flask import Flask, render_template

app = Flask(__name__)

def get_xkcd_image():
    comicid = randint(0, 1000)
    response = requests.get(f'http://xkcd.com/{comicid}/info.0.json')
    return response.json() ['img']

def get_multiple_images(number):
    return [get_xkcd_image() for _ in range(number)]

@app.get('/comic')
def hello():
    start = time.perf_counter()
    urls = get_multiple_images(10)
    end = time.perf_counter()
    return render_template('index.html', end=end, start=start, urls=urls)

if __name__=='__main__':
    app.run(debug=True, port=5555)