from flask import Flask, Blueprint, render_template, request, redirect
import pandas as pd
import os
import regex as re

app = Flask(__name__)

csv_filename = 'email_list.csv'
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), csv_filename)

try:
    email_list = pd.read_csv(csv_path)
    email_list.iloc[:, 0] = email_list.iloc[:, 0].apply(lambda x: x.strip())
except FileNotFoundError:
    print(f"File {csv_path} not found. Make sure it exists and is in the correct directory.")
    email_list = pd.DataFrame(columns=['emails'])

email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'

def load_from_csv():
    collected_csv_filename = 'collected_emails.csv'
    collected_csv_path = os.path.join(os.path.expanduser("~"), 'mysite', collected_csv_filename)
    if os.path.exists(collected_csv_path):
        return pd.read_csv(collected_csv_path)
    else:
        return pd.DataFrame(columns=['emails'])

def save_to_csv(df):
    collected_csv_filename = 'collected_emails.csv'
    collected_csv_path = os.path.join(os.path.expanduser("~"), 'mysite', collected_csv_filename)
    df.to_csv(collected_csv_path, index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    collected_emails = load_from_csv()
    email = request.form['email']
    email = email.lower()

    if email in collected_emails['emails'].str.lower().values:
        return redirect('/duplicate')
    if not re.match(email_pattern, email):  # check if email follows the correct pattern
        return redirect('/invalid')
    if email not in email_list.iloc[:, 0].values:  # verify if email is in original email list
        return redirect('/ineligible')

    new_row = pd.DataFrame({'emails': [email]})
    collected_emails = pd.concat([collected_emails, new_row], ignore_index=True)
    collected_emails = collected_emails.sample(frac=1).reset_index(drop=True)
    save_to_csv(collected_emails)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/ineligible')
def ineligible():
    return render_template('ineligible.html')

@app.route('/invalid')
def invalid():
    return render_template('invalid.html')

@app.route('/duplicate')
def duplicate():
    return render_template('duplicate.html')

if __name__ == '__main__':
    app.run(debug=True)