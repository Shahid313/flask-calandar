from flask import Flask, url_for

app = Flask(__name__)

from application.views.CalenderView import CalenderView

CalenderView.register(app)