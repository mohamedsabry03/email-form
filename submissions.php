<?php
// POST request to get the email from the form 
$email = $_POST['email'];
// Opening the CSV file
$file = fopen('emails.csv', 'a');
// Writing the email to the csv file 
fputcsv($file, array($email));
// Closing the file 
fclose($file);
// Back to the HTML page
header('Location: index.html');
?>