import networkx, numpy, scipy
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	ret = dict()
	ret['drawbacks'] = ["My name is Shank", "My mum gave birth to me"]
	ret['benefits'] = None
	return jsonify(ret)

if __name__=='__main__':
	app.run()
