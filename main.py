from flask import Flask, jsonify
import random
from flask_cors import CORS # Import CORS
from project_bank import projects

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://www.khojcommunity.com"}})
    # Replace this with your actual JSON data or logic to fetch data
    
@app.route('/api/projects', methods=['GET'])
def get_projects():
    # Select 9 random projects
    selected_projects = random.sample(projects, 9)
    return jsonify(selected_projects)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))