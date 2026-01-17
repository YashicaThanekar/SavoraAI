from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'SavoraAI Test Server Running',
        'status': 'healthy'
    })

@app.route('/generate', methods=['POST'])
def test_generate():
    try:
        data = request.json
        print(f"Received data: {data}")
        
        # Return a mock response for testing
        return jsonify({
            'success': True,
            'recipe': {
                'title': 'Test Chicken Rice Bowl',
                'description': 'A simple test recipe',
                'prepTime': '15 mins',
                'cookTime': '30 mins',
                'totalTime': '45 mins',
                'difficulty': 'Easy',
                'servings': '2-3 people',
                'cuisine': 'Asian',
                'ingredients': [
                    '2 cups rice',
                    '1 lb chicken breast',
                    '1 onion, diced'
                ],
                'instructions': [
                    'Cook rice according to package directions',
                    'Season and cook chicken',
                    'Combine and serve'
                ]
            }
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("🚀 Starting Test Server...")
    app.run(host='0.0.0.0', port=5000, debug=True)