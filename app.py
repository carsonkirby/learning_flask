from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route to delete "Mike" function, and the associated HTML template
@app.route('/delete-mike')
def delete_mike():
    # Code to delete Mike goes here
    return render_template('mike.html')

if __name__ == '__main__':
    app.run(debug=True)