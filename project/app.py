from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')

def home():
    return render_template('index.html')

# Quiz route
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        return process_quiz_results(request.form)
    return render_template('quiz.html')

def process_quiz_results(answers):
 
    scores = {"Openness": 0, "Agreeableness": 0, "Extraversion": 0, "Overconfidence": 0}
    
    percentage =0
    for key, value in answers.items():
        if "openness" in key:
            scores["Openness"] += int(value)
        elif "agreeableness" in key:
            scores["Agreeableness"] += int(value)
        elif "extraversion" in key:
            scores["Extraversion"] += int(value)
        elif "overconfidence" in key:
            scores["Overconfidence"] += int(value)
    percentage = (answers.items/value)
    
    return render_template('results.html', scores=scores)

if __name__ == '__main__':
    app.run(debug=True)
