from flask import Flask, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def generate_qr_code():
    data = request.args.get('data')
    if data:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')
    else:
        return "Please provide data parameter in the query string.", 400

@app.route('/', methods=['GET'])
def main():
    return "Hey, API is working!!"

if __name__ == '__main__':
    app.run(debug=True)