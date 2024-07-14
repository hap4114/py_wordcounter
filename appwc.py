#making word count with gui and for gui using flask
from flask import Flask, render_template, request

#creating an instance of flask application
app = Flask(__name__)

# Define a route to handle the form
@app.route('/', methods=['GET', 'POST'])

#main logic for word count
def word_count():
    if request.method == 'POST':
        
        # Get the input string from the form
        s = request.form['input_string']
        
        # Split the string into words
        tot_wc = s.split()
        
        # Calculate the number of words
        word_count = len(tot_wc)
        
        # Render the template with the word count
        return render_template('result.html', word_count=word_count)
    
    # Render the form template for GET requests
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
