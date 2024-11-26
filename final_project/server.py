from flask import Flask, request, jsonify, render_template
from emotion_detection import emotion_detector  # Import your function

app = Flask(__name__)

# Route for rendering the HTML template
@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    if request.method == 'POST':
        input_data = request.get_json()
        statement = input_data.get("statement", "")
    elif request.method == 'GET':
        statement = request.args.get("textToAnalyze", "")

    # Process the statement using emotion_detector
    response = emotion_detector(statement)

    # Check for blank or invalid input
    if response["dominant_emotion"] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    formatted_response = {
        "anger": response["anger"],
        "disgust": response["disgust"],
        "fear": response["fear"],
        "joy": response["joy"],
        "sadness": response["sadness"],
        "dominant_emotion": response["dominant_emotion"],
    }

    display_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return jsonify({"formatted_response": formatted_response, "display": display_response})

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
