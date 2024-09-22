from flask import Flask, request, render_template
import base64, os
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if not (image_data := request.form.get('image')):
            return "No image data received", 400
        
        try:
            filename = f"image_{datetime.now():%Y%m%d_%H%M%S}.png"
            with open(os.path.join('uploads', filename), 'wb') as f:
                f.write(base64.b64decode(image_data.split(',')[1]))
            return f"Image saved successfully as {filename}"
        except Exception as e:
            app.logger.error(f"Error uploading image: {e}")
            return "An error occurred while uploading the image", 500
    
    return render_template('upload.html')

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
