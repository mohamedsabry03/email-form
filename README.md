<h1 align="center">Incentivizing Anonymous Surveys</h1>
This repository presents a framework to incentivize surveys while maintaining respondents' anonymity.

# The Problem
To incentivize surveys while maintaining respondent anonymity, a proposed solution involves
separating the process of collecting contact information from survey responses in the main survey. This method
suggests including a separate survey link at the end of the main survey for participants to provide
contact details for reward distribution. By decoupling contact information from survey
responses, researchers can gather necessary details without compromising anonymity. 

We identified three issues that arise with the practical implementation of this solution. For
demonstration, we will label the second survey for collecting contact information the contact
information survey, or CI survey for short. For the purpose of this report, we assume contact
information to be emails for ease of discussion.

**1. Timestamps:**

When creating the CI survey, a problem of storing timestamps is identified. If both the main
survey and the CI survey store responses’ timestamps, then contact information can be traced
back to the responses based on timestamps. The major survey platforms like Google Forms,
SurveyMonkey and Qualtrics do not have the option to not store timestamps.

**2. Order of Responses:** 

Another threat to anonymity rises with the order of responses. As the respondent traverses from
the main survey to the CI survey, their responses will standardly be in the same row in both
survey’s datasets. That is, the nth response in the main survey corresponds to the nth response in
the CI survey. Accordingly, the order of responses in the CI survey needs to be shuffled.

**3. Verification of Contact Information:**

A survey respondent may enter multiple emails to get multiple rewards, or even send out the CI
survey to their friends. This can make the researchers send out unnecessary rewards.

# The Solution
We developed a website that serves as the CI survey in the framework discussed above to combat
these pitfalls.The purpose is to solve the pitfalls discussed above: the website does not store the timestamps, shuffles responses every time
an email is collected, and implements a verification feature to filter out ineligible emails. The
website outputs a CSV file containing the collected emails.

# Tutorial
The following are instructions on how to use the website to incentivize anonymous surveys:

1. Choose a web-hosting service and upload the files in this directory. We recommend using pyhtonanywhere.com.

2. Replace email_list.csv with your email list that represents the emails you will be sending the survey to. Make sure to place these emails in the first column of the csv file. The emails collected using the website will be verified against the first column in the email_list.csv, and eligibility for rewards is assessed by whether the email collected is in this first column.

3. Place the link to the website at the end page of your main survey to ensure that the website is only accessible after completing the survey.

4. Deploy your survey.

5. The collected emails are going to be stored in the collected_emails.csv.

6. If you are guaranteeing rewards for every survey respondent, you can directly access the collected_emails.csv once you close your main survey and distribute rewards for each email collected.

7. If you are doing a one-winner raffle, simply run the raffle.py file that will randomly select and output the winner's email. Make sure that the raffle.py and collected_emails.csv are in the same directory.

