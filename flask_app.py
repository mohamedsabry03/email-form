from flask import Flask, render_template, request, redirect
import pandas as pd
import os
import regex as re

app = Flask(__name__, template_folder='templates')

email_list = pd.read_csv('email_list.csv')  # emails survey is sent to
email_list.iloc[:,0] = email_list.iloc[:,0].apply(lambda x: x.strip())  # clean email list
collected_emails = pd.DataFrame(columns=['emails'])  # emails collected to distribute incentives
email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'  # to ensure response validity

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    global collected_emails
    email = request.form['email']
    if email not in email_list.iloc[:,0]:  # verify if email is in original email list
        return redirect('/ineligible')
    elif not bool(re.match(email_pattern, email)):  # does not follow email pattern 
        return redirect('/invalid')
    else:
        new_row = pd.DataFrame({'emails':[email]})
        collected_emails = pd.concat([collected_emails, new_row])  # add new row to collected emails
        if collected_emails['emails'].str.lower().duplicated().any():  # check if duplicate
            return redirect('/duplicate')
        else:
            collected_emails = collected_emails.sample(frac=1).reset_index(drop=True)  # shuffle collected emails
            save_to_csv()
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

def save_to_csv():
    global collected_emails
    csv_filename = 'collected_emails.csv'
    csv_path = os.path.join(os.path.expanduser("~"), 'mysite', csv_filename)
    collected_emails.to_csv(csv_path, index=False)

if __name__ == '__main__':
    app.run(debug=True)