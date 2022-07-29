import random
import re
import sys
from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/recommend')
def ad():
    return render_template('recommend.json')

if __name__ == '__main__':
    app.run(host='localhost',port=5002,debug=True)