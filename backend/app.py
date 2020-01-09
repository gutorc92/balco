
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
	"""Print 'Hello, world!' as the response body."""
	data = request.json
	A = list(map(int, data['array']))
	K = int(data['K'])
	L = int(data['L'])
	result = {
		'total': get_max_apples(A, K, L)
	}
	return jsonify(result)

def get_max_apples(A, K, L):
	if K + L > len(A):
		return -1
	max_value = max(K, L)
	max_k = 0
	for i in range(0, len(A) - L - K):
		a = max_array(A[i:K+i], K)
		b = max_array(A[K+i:], L)
		k = a + b
		max_k = max(max_k, k)
	return max_k

def max_array(a, k):
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