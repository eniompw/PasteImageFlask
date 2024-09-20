# Image Paste and Upload

This project provides a simple web application that allows users to paste an image from their clipboard and upload it to the server.

## Features

- **Paste Anywhere**: Users can paste an image anywhere on the page.
- **Image Preview**: The pasted image is immediately displayed for preview.
- **Easy Upload**: A single click uploads the pasted image to the server.
- **Feedback**: Clear messages inform users about the upload status.

## How It Works

### Frontend (`templates/upload.html`)

1. **HTML Structure**:
   - A form with a hidden input for image data.
   - A div acting as a paste area.
   - An upload button.
   - A message div for feedback.

2. **JavaScript Functionality**:
   - Listens for paste events across the entire document.
   - When an image is pasted:
     - Displays the image in the paste area.
     - Stores the image data in the hidden input.
   - Handles form submission:
     - Prevents default form submission.
     - Sends image data to the server using fetch API.
     - Displays server response or error messages.

### Backend (`app.py`)

1. **Flask Setup**:
   - Creates a Flask application.
   - Defines a route for both GET and POST requests.

2. **Image Handling**:
   - On POST request:
     - Receives image data from the form.
     - Decodes the base64 image data.
     - Generates a unique filename.
     - Saves the image in the 'uploads' directory.
   - On GET request:
     - Renders the HTML template.

3. **Error Handling**:
   - Checks for missing image data.
   - Catches and logs any exceptions during image processing.

## How to Use

1. Run the Flask application.
2. Open the webpage in a browser.
3. Copy an image to your clipboard.
4. Paste anywhere on the page.
5. Click the "Upload Image" button.
6. The image will be saved on the server, and you'll see a confirmation message.

## Setup

1. Ensure you have Python and Flask installed.
2. Run `python app.py` to start the server.
3. Access the application through your web browser at `http://localhost:5000`.

This simple application demonstrates basic image handling, client-side JavaScript, and server-side Python using Flask.
