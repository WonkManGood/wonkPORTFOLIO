from flask import Flask, render_template
app = Flask(__name__, static_folder='assets')

def test():
    print('Hello World')

@app.route('/')
def main():
    return render_template('base.html') # 

app.run(host='0.0.0.0', port='1024', debug=False)
