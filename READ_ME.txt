To incentivize surveys while maintaining respondent anonymity, a proposed solution involves separating the process of collecting contact information from survey responses. This method suggests including a separate link which leads respondents to the contact information survey at the end of the main survey, for participants to provide contact details for reward distribution. By decoupling contact information from survey responses, researchers can gather necessary details without compromising anonymity.

The following are instructions on how to use the website to incentivize anonymous surveys:

1. Choose a web-hosting service and upload the files in this directory. We recommend using pyhtonanywhere.com.

2. Replace email_list.csv with your email list that represents the emails you will be sending the survey to. Make sure to place these emails in the first column of the csv file. The emails collected using the website will be verified against the first column in the email_list.csv, and eligibility for rewards is assessed by whether the email collected is in this first column.

3. Place the link to the website at the end page of your main survey to ensure that the website is only accessible after completing the survey.

4. Deploy your survey.

5. The collected emails are going to be stored in the collected_emails.csv.

6. If you are guaranteeing rewards for every survey respondent, you can directly access the collected_emails.csv once you close your main survey and distribute rewards for each email collected.

7. If you are doing a one-winner raffle, simply run the raffle.py file that will randomly select and output the winner's email. Make sure that the raffle.py and collected_emails.csv are in the same directory.

