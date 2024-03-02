# 🎉 QRGeniusAPI 🎉

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
[![made-with-flask](https://img.shields.io/badge/Made%20with-Flask-yellow.svg)](https://flask.palletsprojects.com/)
[![made-with-qrcode](https://img.shields.io/badge/Made%20with-QRCode-green.svg)](https://pypi.org/project/qrcode/)
[![made-with-pillow](https://img.shields.io/badge/Made%20with-Pillow-orange.svg)](https://python-pillow.org/)

Welcome to QRGeniusAPI! This Flask-based Python API is your go-to solution for generating hilarious QR codes in a snap.

## 🚀 How it Works
Simply send your desired data through the API endpoint, and QRGeniusAPI will work its magic, transforming it into a quirky QR code masterpiece. Spice up your messages, URLs, or any other data with a touch of humor and creativity!

## 📸 Example Usage
```python
import requests

data = "Hello, world!"
response = requests.get(f"http://localhost:5000/qr?data={data}")

# Save or display the generated QR code image
with open("qrcode.png", "wb") as f:
    f.write(response.content)
```

# 🛠️ Getting Started
1. Clone this repository to your local machine.
2. Install the necessary dependencies by running `pip install -r requirements.txt`.
3. Run the Flask app by executing `python app.py`.
4. Send GET requests to `http://localhost:5000/qr` with your desired data.
5. Voila! Your hilarious QR code is ready to be shared.

## 🔧 Technologies Used
- **Python**: Backend development using Flask.
- **Flask**: Micro web framework for Python.
- **QRCode**: Library for generating QR codes.
- **Pillow**: Imaging library for Python.

## 🎨 Coded By
Coded with ❤️ by Shahjada ALif

## 🎈 Contributing
Feel free to contribute to this project by forking the repository and submitting a pull request!

## License 📄
This project is licensed under the [MIT License](LICENSE).
