
""" Handle api calls """

from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# pylint: disable=invalid-name
@app.route('/calculate', methods=['POST'])
def calculate():
	"""Print 'Hello, world!' as the response body."""
	result = {
					'total': 0,
					'message': 'Execute with sucess.'
	}
	try:
		data = request.json
		A = list(map(int, data['array']))
		K = int(data['K'])
		L = int(data['L'])
		result['total'] = get_max_apples(A, K, L)
	except KeyError:
		abort(400, 'Parameters not send')
	except:
		result['message'] = 'Faile to execute'
	return jsonify(result)

def get_max_apples(A, K, L):
	""" Get max apples from array """
	len_a = len(A)
	if K + L > len_a:
		return -1
	max_k = 0
	for i in range(0, len_a - L - K + 1):
		a = max_array(A[i:K+i], K)
		b = max_array(A[K+i:], L)
		k = a + b
		max_k = max(max_k, k)
	return max_k

def max_array(a, k):
	""" Get max sum from a subarray fo size k """
	ksum = 0
	for i in range(0, k):
		ksum += a[i]
	max_ksum = ksum
	for i in range(k, len(a)):
		add_index = i
		sub_index = i - k
		ksum = ksum + a[add_index] - a[sub_index]
		max_ksum = max(max_ksum, ksum)
	return max_ksum


if __name__ == '__main__':
	app.run()
