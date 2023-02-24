import os
import logging

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)

if __name__ == "__main__":
    logging.error('{"key1":"val1"}')
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
