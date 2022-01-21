from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [{
    'id': 1,
    'number': 9924580492,
    'name': 'Mr. Goel',
    'done': False},
    {
        'id': 2,
        'number': 9934896904,
        'name': 'Mr. Gupta',
        'done': False,
    }]

@app.route('/')

@app.route('/add-data', methods = ['POST'])


def index():
    return jsonify({
        'data': contacts,
        'message': 'Success!'
    }), 200

def add_contact():
    if not request.json:
        return jsonify({
            'status': 'error', 
            'message': 'Please provide the data'
        }),200

    contact = {
        'id': contacts[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }

    contacts.append(contact)
    return jsonify({
        'status': 'Success',
        'message': 'Contact added successfully!'
    }), 200

app.run()