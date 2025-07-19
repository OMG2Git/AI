from flask import Flask
from flask_cors import CORS
from routes.api_server import api_server
from routes.api_server2 import api_server2
import os

app = Flask(__name__)
CORS(app)
app.register_blueprint(api_server)
app.register_blueprint(api_server2)

if __name__ == '__main__':
    # Use environment port for production, fallback to 5000 for local
    port = int(os.environ.get('PORT', 5000))
    # Remove debug=True for production
    app.run(host='0.0.0.0', port=port, debug=False)