from flask import Flask, render_template, request

app = Flask(__name__)

# ------------------ HOME PAGE ------------------
@app.route('/')
def home():
    return render_template('index.html')

# ------------------ PROFILE PAGE ------------------
@app.route('/profile')
def profile():
    return render_template('profile.html')

# ------------------ WORKS PAGE ------------------
@app.route('/works')
def works():
    return render_template('works.html')

# ------------------ CONTACT PAGE ------------------
@app.route('/contact')
def contact():
    return render_template('contact.html')

# ------------------ TOUPPERCASE TOOL ------------------
@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

# ------------------ AREA OF CIRCLE ------------------
@app.route('/circle', methods=['GET', 'POST'])
def circle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            result = 3.1416 * radius ** 2
        except ValueError:
            result = "Invalid input"
    return render_template('circle.html', result=result)

# ------------------ AREA OF TRIANGLE ------------------
@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            result = 0.5 * base * height
        except ValueError:
            result = "Invalid input"
    return render_template('triangle.html', result=result)

# ------------------ RUN ------------------
if __name__ == "__main__":
    app.run(debug=True)
