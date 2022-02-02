from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [{
    'id': 1,
    'Name': u'Raju',
    'Contact': u'9924580492',
    'done': False},
    {
        'id': 2,
        'Name': u'Rahul',
        'Contact': u'9934896904',
        'done': False,
    }]

@app.route('/')

def index():
    return jsonify({
        'data': contacts,
        'message': 'Success!'
    }), 200

@app.route('/add-data', methods = ['POST'])

def add_data():
    if not request.json:
        return jsonify({
            'status': 'error', 
            'message': 'Please provide the data'
        },400)

    contact = {
        'id': contacts[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ''),
        'done': False
    }

    contacts.append(contact)
    return jsonify({
        'status': 'Success',
        'message': 'Contact added successfully!',
    },400)

@app.route('/get-data')

def get_data():
    return jsonify({
        'data': contacts
    })

app.run()