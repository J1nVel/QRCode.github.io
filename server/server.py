# -*- coding: utf-8 -*-
"""
Created on 2023/5/9  11:57

@author: v_wweijin
"""
import os
import sys
import traceback

from flask import Flask, jsonify, request
from PIL import Image
from pyzbar import pyzbar
from werkzeug.utils import secure_filename

app = Flask(__name__)
# app.config["JSON_AS_ASCII"] = False
upload_path = '../file_cache'
app.config["UPLOAD_FOLDER"] = upload_path


@app.route('/api/qrcodescan', methods=["POST"])
def qrcode_scan():
    """
    支持多个二维码识别
    """
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    images = request.files.getlist('image')
    result = dict()
    try:
        for image in images:
            if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], image.filename)):
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            result[image.filename] = list()
            img = Image.open(image.stream)
            barcodes = pyzbar.decode(img)
            if not barcodes:
                result[os.path.basename(image)].append('No QRcode detected')
                continue
            else:
                for barcode in barcodes:
                    barcodedata = barcode.data.decode("utf-8")
                    result[image.filename].append(barcodedata)
        return jsonify(result)
    except Exception:
        return traceback.format_exc()


if __name__ == '__main__':
    app.run(host='localhost', debug=True)

