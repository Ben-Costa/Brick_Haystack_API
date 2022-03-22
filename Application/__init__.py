from flask import Flask

app = Flask(__name__, static_folder="../Application/static")

from Application import routes