from flask import Flask
from flask import request
import os

from boundary import boundary

app = Flask(__name__)

@app.route("/")
def home_dir():
  if request.method == 'GET':
    return boundary()

  else:
    return "Method not supported"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)