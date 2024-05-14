from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__, template_folder='templates')


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
    emails_df = load_from_csv()
    email = request.form['email']
    if not email.endswith('@uchicago.edu'):
        return redirect('/failure')

    new_email = email.lower()
    if new_email in emails_df['emails'].str.lower().values:
        return redirect('/duplicate')

    emails_df = emails_df.append({'emails': email}, ignore_index=True)
    emails_df = emails_df.sample(frac=1).reset_index(drop=True)
    save_to_csv(emails_df)  # Pass emails_df as an argument
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

if __name__ == '__main__':
    app.run(debug=True)
