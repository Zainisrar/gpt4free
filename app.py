
from flask import Flask, jsonify,render_template,request
import gpt4free
from gpt4free import Provider
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat_start', methods=['POST'])
def chat_start():
    query = request.form.get('question')
    response = gpt4free.Completion.create(Provider.You, query)
    # print("Response:", response)
    return jsonify(response=response)

if __name__ == "__main__":
    app.run(debug=True)
