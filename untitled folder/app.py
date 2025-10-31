from flask import Flask, render_template, request, jsonify
from transpiler import AssamesePythonTranspiler
import os

app = Flask(__name__)
transpiler = AssamesePythonTranspiler()

# Example programs
EXAMPLES = {
    "hello_world": {
        "title": "Hello World",
        "code": """প্ৰিণ্ট("নমস্কাৰ পৃথিৱী!")
প্ৰিণ্ট("অসমীয়া ভাষাত প্ৰগ্ৰামিং!")"""
    },
    "calculator": {
        "title": "Simple Calculator",
        "code": """x = ১০
y = ৫
প্ৰিণ্ট("যোগফল:", x + y)
প্ৰিণ্ট("বিয়োগফল:", x - y)
প্ৰিণ্ট("গুণফল:", x * y)
প্ৰিণ্ট("ভাগফল:", x / y)"""
    },
    "loop": {
        "title": "Loop Example",
        "code": """প্ৰতিটোৰ বাবে i ভিতৰত পৰিসৰ(১, ৬):
    প্ৰিণ্ট("সংখ্যা:", i)"""
    },
    "conditional": {
        "title": "If-Else Condition",
        "code": """সংখ্যা = ১৫

যদি সংখ্যা > ১০:
    প্ৰিণ্ট("সংখ্যাটো ১০ তকৈ ডাঙৰ")
নহলে:
    প্ৰিণ্ট("সংখ্যাটো ১০ বা তাতকৈ সৰু")"""
    }
}

@app.route('/')
def index():
    return render_template('index.html', examples=EXAMPLES)

@app.route('/transpile', methods=['POST'])
def transpile():
    data = request.json
    assamese_code = data.get('code', '')
    
    if not assamese_code.strip():
        return jsonify({
            'success': False,
            'error': 'কোড খালী হ\'ব নোৱাৰে (Code cannot be empty)'
        })
    
    result = transpiler.run(assamese_code)
    
    return jsonify({
        'success': result['success'],
        'python_code': result['python_code'],
        'output': result['output'],
        'error': result['error']
    })

@app.route('/examples/<example_name>')
def get_example(example_name):
    if example_name in EXAMPLES:
        return jsonify({
            'success': True,
            'code': EXAMPLES[example_name]['code']
        })
    return jsonify({
        'success': False,
        'error': 'Example not found'
    })

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)