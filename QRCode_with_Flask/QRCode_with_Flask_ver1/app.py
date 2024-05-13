from flask import Flask , render_template , request , send_file, send_from_directory
import qrcode as qr

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/generated-qrcode' , methods = ['POST'])
def generate():
    data = request.form['data']
    name = request.form['name']
    img = qr.make(data)
    img.save(f'static/generated-QR/{name}.png')
    return render_template('generate.html', filename = f'generated-QR/{name}.png')


@app.route('/download/<path:filename>')
def download_qr(filename):
    return send_from_directory('static',filename, as_attachment=True)


if __name__=='__main__':
    app.run(debug=True)