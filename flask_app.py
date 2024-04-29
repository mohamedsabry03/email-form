from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__, template_folder='templates')

emails_df = pd.DataFrame(columns=['emails'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    global emails_df
    email = request.form['email']
    if not email.endswith('@uchicago.edu'):
        return redirect('/failure')
    else:
        emails_df = emails_df.append({'emails': email}, ignore_index=True)
        if emails_df['emails'].str.lower().duplicated().any():
            return redirect('/duplicate')
        else:
            emails_df = emails_df.sample(frac=1).reset_index(drop=True)
            save_to_csv()
            return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/failure')
def failure():
    return render_template('failure.html')

@app.route('/duplicate')
def duplicate():
    return render_template('duplicate.html')

def save_to_csv():
    global emails_df
    csv_filename = 'emails.csv'
    csv_path = os.path.join(os.path.expanduser("~"), 'mysite', csv_filename)
    emails_df.to_csv(csv_path, index=False)

if __name__ == '__main__':
    app.run(debug=True)