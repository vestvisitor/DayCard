import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path
path = Path(myDir)
a=str(path.parent.absolute())

sys.path.append(a)

from flask_jwt_extended import JWTManager
from backend.app import create_app
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = create_app()
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
cors = CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run(debug=True)
