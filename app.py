from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
   return "Hello, Render!"

@app.route('/webhook', methods=['POST'])
def webhook():
   data = request.json
   # 在这里处理接收到的数据
   print(data)
   return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
