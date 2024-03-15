from flask import Flask, request
from views import main

app = Flask(__name__)


@app.route('/ping')
def ping():
    response = {'status': 'success', 'message': 'pong'}
    return response, 200

@app.route('/last_played')
def etl_sp():
    date = request.args.get('date')
    user_name = request.args.get('user')
    data = main.main(date,user_name)
    response = {'status': 'success', 'data': data}
    return response, 200
    

if __name__ == '__main__':
    app.run(debug=False, host= "0.0.0.0", port= "8080")
    