
import time

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():

    return 'Hello World! I am ALIVE.\n'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False) # bind to 0.0.0.0 (machine/container's IP) -- so that it can be accessed from outside
                                        # if localhost, it can only be accessed from within the machine/container
                                        # default port is 5000
