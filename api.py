from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data',methods=['GET'])
def receive_data():
     data = request.json()
     return jsonify({
          'data':data
     })
    # For demonstration, we'll just return the received data
     

if __name__ == '__main__':
    app.run(debug=True)
