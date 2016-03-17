# -*- coding: utf-8 -*-
# @Author: Maxwell Amante
# @Date:   2016-03-16 01:00:36
# @Last Modified by:   max amante
# @Last Modified time: 2016-03-16 23:14:02

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
