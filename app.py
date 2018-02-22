#!/usr/bin/python
# -*- coding: <unicode-escape> -*-
#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
	return ("********Welcome******")
if __name__ == "__main__":
	app.run()
