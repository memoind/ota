from flask import current_app, send_from_directory, jsonify, Blueprint
import os  # Importando o módulo os

# Usando um Blueprint para organizar as rotas
bp = Blueprint('main', __name__)

@bp.route('/version', methods=['GET'])
def get_version():
    version_file = os.path.join(current_app.root_path, 'version.txt')
    with open(version_file, 'r') as file:
        version = file.read().strip()
    return jsonify({"version": version})

@bp.route('/ota', methods=['GET'])
def serve_firmware():
    firmware_file = 'firmware.bin'
    return send_from_directory(directory=current_app.root_path, path=firmware_file)