from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__, template_folder='templates')

# Initialize an empty DataFrame to store emails
emails_df = pd.DataFrame(columns=['emails']) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    global emails_df
    email = request.form['email']

    if "@" in email: 
        emails_df = emails_df.append({'emails': email}, ignore_index=True)
        return render_template('success.html')
    else:
        return render_template('failure.html')

@app.route('/export_csv')
def export_csv():
    emails_df.to_csv('emails.csv', index=False)
    return "CSV file exported!" 

if __name__ == '__main__':
    app.run(debug=True) 
