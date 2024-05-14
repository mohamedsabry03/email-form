from flask import Flask, render_template, request, redirect
import pandas as pd
import os
import regex as re

app = Flask(__name__, template_folder='templates')

email_list = pd.read_csv('email_list.csv')  # emails survey is sent to
email_list.iloc[:,0] = email_list.iloc[:,0].apply(lambda x: x.strip())  # clean email list
email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'  # to ensure response validity

def load_from_csv():
    csv_filename = 'emails.csv'
    csv_path = os.path.join(os.path.expanduser("~"), 'mysite', csv_filename)
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    else:
        return pd.DataFrame(columns=['emails'])

def save_to_csv(df):
    csv_filename = 'emails.csv'
    csv_path = os.path.join(os.path.expanduser("~"), 'mysite', csv_filename)
    df.to_csv(csv_path, index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    collected_emails = load_from_csv()
    email = request.form['email']
    email = email.lower()
    
    if email not in email_list.iloc[:,0]:  # verify if email is in original email list
        return redirect('/ineligible')
    if not bool(re.match(email_pattern, email)):  # does not follow email pattern 
        return redirect('/invalid')
    if email in collected_emails['emails'].str.lower().values:
        return redirect('/duplicate')
    
    new_row = pd.DataFrame({'emails':[email]})
    collected_emails = pd.concat([collected_emails, new_row])
    collected_emails = collected_emails.sample(frac=1).reset_index(drop=True)
    save_to_csv(collected_emails)  # Pass collected_emails as an argument
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