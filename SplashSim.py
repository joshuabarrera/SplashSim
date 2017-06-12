from flask import *
import flask
from random import *
app = Flask(__name__)


@app.route('/')
def hello():
	if randint(0,10) >2:
		try:
			return render_template("/index.html")

		except Exception as e:
			return str(e)
	else:
			resp = flask.make_response(render_template('yeezy.html'))
			resp.set_cookie('gceeqs', "exp=1485210572~acl=%2f*~hmac=98a845d461218eb8e1f863140caad25e34e3d2ee5a68eb8d9f5eb7f29ac3e049")
			   
			return resp

if __name__ == '__main__':
    app.run()