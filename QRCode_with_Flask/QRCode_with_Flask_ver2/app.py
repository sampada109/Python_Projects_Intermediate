from flask import Flask, render_template, request, send_from_directory
import qrcode
from PIL import Image
import qrcode.constants

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/generated_qrcode', methods=['POST'])
def generate():
    data = request.form['data']
    name = request.form['name']
    fill_color = request.form['fill_color']
    back_color = request.form['back_color']
    version = request.form['version']
    box_size = request.form['box_size']
    border_size = request.form['border_size']

    qr = qrcode.QRCode(version=version,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=box_size, border=border_size)
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(f'static/generated-QR/{name}.png')

    return render_template('generate.html', filename = f'generated-QR/{name}.png')



@app.route('/download/<path:filename>')
def download_qr(filename):
    return send_from_directory('static',filename, as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)