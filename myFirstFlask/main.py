from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def Jay_Ganesh():
    return 'Jay Ganesh...!'

@app.route('/simple')
def simple():
    return 'Simple Jay Ganesh!'

@app.route('/json')
def json():
    return jsonify(text='Simple Jay Ganesh!',
                   message='You have run API successfully!'), 201

@app.route('/not-found')
def not_found():
    return jsonify(error='This is route was not found'), 404

if __name__ == '__main__':
    app.run()