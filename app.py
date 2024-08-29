from flask import Flask, render_template, request
import similarity

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def result():
    if request.method == 'POST':
        result = request.form['text']
        report_html = similarity.returnTable(similarity.report(str(result)))
        return render_template('report.html', report_html=report_html)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)
