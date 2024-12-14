from flask import Flask, request, jsonify
import base64
import io
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan_image():
    data = request.get_json()
    image_data = data['image']  # Received as base64
    image = Image.open(io.BytesIO(base64.b64decode(image_data.split(',')[1])))  # Decode and open image

    # Process image, extract nutritional data, etc.
    pie_chart_data = {'Vitamins': 30, 'Carbs': 40, 'Fats': 15, 'Fibers': 10, 'Minerals': 5}  # Example data
    pros = ["Good source of vitamins", "High in fiber", "Low in fat"]
    cons = ["Contains added sugar", "High in calories"]
    conclusion = "This product is healthy in moderation."

    return jsonify({
        'pie_chart_data': pie_chart_data,
        'pros': pros,
        'cons': cons,
        'conclusion': conclusion
    })

if __name__ == '__main__':
    app.run(debug=True)
