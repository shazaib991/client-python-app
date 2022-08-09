from flask import Flask, render_template, request, jsonify
import os

# Set the template and static folder to the client build
app = Flask(__name__, template_folder="client/build", static_folder="client/build/static")

app.config['SECRET_KEY'] = 'super secret key'
app.config['SITE'] = "http://0.0.0.0:5000/"
app.config['DEBUG'] = True

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """ This is a catch all that is required for react-router """
    return render_template('index.html')

# Endpoints
@app.route('/test', methods=['GET'])
def login():
    """ An example endpoint """
    if request.method == 'GET':
        return jsonify({'languages' : languages}),200
    
@app.route('/test', methods=['POST'])
def addOne():
	language = {'name' : request.json['name']}
	languages.append(language)
	return jsonify({'languages' : languages}),201

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
