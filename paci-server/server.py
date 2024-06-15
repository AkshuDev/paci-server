from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

# Endpoint to receive and save a module file
@app.route('/upload_module', methods=['POST'])
def upload_module():
    # Check if the POST request has the file part
    if 'module' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    module_file = request.files['module']

    if module_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file to a specific directory
    upload_folder = 'uploaded_modules'
    os.makedirs(upload_folder, exist_ok=True)
    module_path = os.path.join(upload_folder, module_file.filename)
    module_file.save(module_path)

    return jsonify({'message': 'File uploaded successfully', 'file_path': module_path}), 200

# Endpoint to retrieve a module file
@app.route('/download_module/<filename>', methods=['GET'])
def download_module(filename):
    module_path = os.path.join('uploaded_modules', filename)
    if os.path.isfile(module_path):
        return send_file(module_path, as_attachment=True)
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/upload_addon', methods=['POST'])
def upload_addon():
    # Check if the POST request has the file part
    if 'addon' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    addon_file = request.files['addon']

    if addon_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file to a specific directory
    upload_folder = 'uploaded_addons'
    os.makedirs(upload_folder, exist_ok=True)
    addon_path = os.path.join(upload_folder, addon_file.filename)
    addon_file.save(addon_path)

    return jsonify({'message': 'File uploaded successfully', 'file_path': addon_path}), 200

# Endpoint to retrieve a addon file
@app.route('/download_addon/<filename>', methods=['GET'])
def download_addon(filename):
    addon_path = os.path.join('uploaded_addons', filename)
    if os.path.isfile(addon_path):
        return send_file(addon_path, as_attachment=True)
    else:
        return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
