from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
app = Flask(__name__, static_folder='assets')
app.wsgi_app = ProxyFix(app.wsgi_app)

def test():
    print('Hello World')

@app.route('/')
def main():
    return render_template('base.html')

app.run(host='0.0.0.0', port='1024')
