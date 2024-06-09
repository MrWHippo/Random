from flask import Flask , render_template, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def home():
    return redirect('https://www.audi.co.uk/uk/web/en/used-car-search/details.sc_detail.R0JSMDA0MjgyMzI1Mzc0=.html')





if __name__ == '__main__':
    app.run(host='192.168.1.144', port=5000, debug=True, threaded=False)