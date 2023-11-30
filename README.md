# networkserverassignment
this repository for the submission of networkserver assignment code

Submitting the Python file : subdomainSearchService.py

A website can have many subdomains and different services are running on them.
Write a Python script to check the status of the subdomains which are up or down.
The script should automatically check the status every minute and should update it in tabular format on the screen. 

Each scan delivers a list of subdomains that is given for validated.
It will check periodically whether subdomain is Up or Down.

I have chosen new alternative to ChatGTP , https://www.perplexity.ai/
Obtained its minimum Subdomain list : www,blog,labs
one more invalid subdomain - "m" , if its have mobile version.

After each scan, publish the result using python tabular form , using "tabular" library.
For making requests from domain, imported "requests" library in python script.

Import the requests library for making HTTP requests.
Import the time module for time-related functions.
Import the tabulate function for creating tables.
Construct the URL using the provided subdomain.
Send an HTTP GET request to the constructed URL with a timeout of 5 seconds.
Check if the response status code is 200 (indicating a successful request).
If an exception occurs during the request (e.g., network error), set status to "Down".
Return the subdomain and its status.
Define the headers for the table.
Use the tabulate function to print the table with the provided data.
Define a list of subdomains to be checked.
Call the check_subdomain function for each subdomain and store the results in subdomain_statuses list.
Print the table containing subdomain statuses.
Wait for 60 seconds before checking again (to avoid excessive requests).
Call the main function when the script is executed directly.


