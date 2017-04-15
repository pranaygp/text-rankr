import markdown
from flask import Flask, request, jsonify
from summa import summarizer
app = Flask(__name__)

@app.route('/summarize', methods=['GET'])
def summarize():
	ret = dict()
	args = request.args.to_dict()

	try:
		old_text = args['text']
		new_text = summarizer.summarize(old_text)
		ret['old_text'] = old_text
		ret['new_text'] = new_text
		ret['status'] = True
		ret['error'] = None
	except Exception as e:
		ret['old_text'] = None
		ret['new_text'] = None
		ret['status'] = False
		ret['error'] = str(e)

	return jsonify(ret)

@app.route('/', methods=['GET'])
def index():
	ret = dict()
	ret['endpoints'] = ['/summarize']
	ret['status'] = True
	return jsonify(ret)

if __name__=='__main__':
	app.run(debug=True)
