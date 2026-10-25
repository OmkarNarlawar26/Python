from flask import Flask, jsonify, request

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

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age > 18:
        return jsonify(message= f"Welcome {name}!!!")
    else:
        return jsonify(message= f"Sorry {name}, you are not old enough to access this API")

@app.route('/api_variables/<string:name>/<int:age>')
def api_variables(name:str, age:int):
    if age > 21:
        return jsonify(message= f"Welcome {name}!!!")
    else:
        return jsonify(message= f"Sorry {name}, you are not old enough to access this API")



if __name__ == '__main__':
    app.run()