from flask import Flask, render_template
app = Flask(__name__, static_folder='assets')

@app.route('/')
def main():
    return render_template('base.html')

while True:
    app.run(host='0.0.0.0', port='80')
    if KeyboardInterrupt:
        break