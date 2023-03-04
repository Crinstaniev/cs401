import app
import waitress

waitress.serve(app.app.server, port=31510, url_scheme='http', host='0.0.0.0')