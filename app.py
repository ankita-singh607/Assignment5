from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined responses for student questions
def get_answer(question):
  question = question.lower()

    # Simple question matching (you can extend thi
  if "programming languages" in question:
    return "Focus on languages like Python, Java, and C++."
  elif "projects" in question:
    return "Here are some of the projects - student dashboard, whether app, e-commerce site and for more refer to google.com"
  elif "subjects" in question:
    return "Your subjects are based on your semester."
  elif "grades" in question:
    return "Focus on your studies, prepare a time table and ask doubts"
  elif "circuit design" in question:
    return "Use resources like online tutorials and textbooks on circuit theory."
  elif "subjects" in question:
    return "Your subjects are based on your semester."
  elif "grades" in question:
    return "Focus on your studies, prepare a time table and ask doubts"
  elif "cad software" in question:
    return "Learn software like AutoCAD and SolidWorks."
  elif "subjects" in question:
    return "Your subjects are based on your semester."
  elif "grades" in question:
    return "Focus on your studies, prepare a time table and ask doubts"
  elif "structural analysis" in question:
    return "Review textbooks and online courses that cover structural engineering principles."
  elif "subjects" in question:
    return "Your subjects are based on your semester."
  elif "grades" in question:
    return "Focus on your studies, prepare a time table and ask doubts"
  elif "custom" in question:
    return "Your custom question will be reviewed, and you'll get a response shortly."
  else:
    return "I'm not sure, but you can ask your professor or career counselor for detailed advice."


# Home route to display the form
@app.route('/')
def home():
    return render_template('home.html')
# Route to handle form submission and show the answer
@app.route('/get_answer', methods=['POST'])
def get_answer_route():
    question = request.form['question']
    answer = get_answer(question)
    return render_template('answer.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

