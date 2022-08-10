
from flask import Flask, render_template, request, jsonify, json
from flask_cors import CORS
import os
import sqlite3
from Crypto.PublicKey import RSA


conn = sqlite3.connect('data.db', check_same_thread=False) # permanent database
cursor = conn.cursor()

# Set the template and static folder to the client build
app = Flask(__name__, template_folder="client/build", static_folder="client/build/static")

app.config['SECRET_KEY'] = 'super secret key'
app.config['SITE'] = "http://0.0.0.0:5000/"
app.config['DEBUG'] = True

CORS(app)

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

@app.route('/addData', methods=['POST'])
def addData():
    key = RSA.generate(2048)
    private_key = key.export_key()
    #file_out = open("private.pem", "wb")
    #file_out.write(private_key)
    public_key = key.publickey().export_key()
    #file_out = open("public.pem", "wb")
    #file_out.write(public_key)
    strPublicKey = str(public_key)
    newStr = strPublicKey.replace("\\n", "").strip("b'-----BEGIN PUBLIC KEY-----END PUBLIC KEY")
    
    language = request.json['language']
    device = request.json['device']
    browserName = request.json['browserName']
    browserDimentions = request.json['browserDimentions']
    ipAddress = request.json['ipAddress']
    cookieStatus = request.json['cookieStatus']
    try:
        cursor.execute("insert into data values (?, ?, ?, ?, ?, ?, ?)",
                        [json.dumps(language), json.dumps(device), json.dumps(browserName), json.dumps(browserDimentions), json.dumps(ipAddress), json.dumps(cookieStatus), newStr ])
        conn.commit()
        return "Data added"
    except:
        return "Please add the correct values"

@app.route('/getData', methods=['GET'])
def getData():
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    keys = ["language", 'device', "browserName", "browserDimentions", "ipAddress", "cookieStatus", "Public key"]
    list_dict = []
    
    for row in rows:
        new_dict = dict(zip(keys, list(row)))
        
        list_dict.append(new_dict)
     
    jsonFile = json.dumps(list_dict, indent=1)   
    return jsonFile   


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
