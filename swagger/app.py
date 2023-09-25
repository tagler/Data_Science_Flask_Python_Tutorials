from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def index():
    """Example GET endpoint
    ---
    responses:
      200:
        description: OK
        examples:
          "Index Page"
    """
    return "Index Page"

@app.route('/display/<name>', methods=['GET'])
def example_get_with_param(name):
    """Example GET endpoint with param
    ---
    parameters:
      - name: name
        in: path
        type: string
        required: true
        default: name
    responses:
      200:
        description: OK
        examples:
          "Hello {name}!"
    """
    return f"Hello {name}!"

@app.route('/json', methods=['POST'])
def example_post():
    """Example POST endpoint
    ---
    parameters:
      - in: body
        name: body
        schema:
          required:
            - first_name
            - last_name
          properties:
            first_name:
              type: string
            last_name:
              type: string
    responses:
      200:
        description: OK
        examples:
          "Hello {first_name} {last_name}!"
    """
    content = request.json
    first_name = content['first_name']
    last_name = content['last_name']
    return f"Hello {first_name} {last_name}!"

# run python file directly (use app.run() below) or call flask on the command line
# swagger ui is at http://localhost:5000/apidocs/
app.run(debug=True)
