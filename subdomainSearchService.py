import requests  # Import the requests library for making HTTP requests.
import time  # Import the time module for time-related functions.
from tabulate import tabulate  # Import the tabulate function for creating tables.
def check_subdomain(subdomain):
    # Construct the URL using the provided subdomain.
    url = f"https://{subdomain}.perplexity.ai"
    try:
        # Send an HTTP GET request to the constructed URL with a timeout of 5 seconds.
        response = requests.get(url, timeout=5)
        # Check if the response status code is 200 (indicating a successful request).
        status = "Up" if response.status_code == 200 else "Down"
    except requests.RequestException:
        # If an exception occurs during the request (e.g., network error), set status to "Down".
        status = "Down"
    # Return the subdomain and its status.
    return subdomain, status
def print_table(subdomain_statuses):
    # Define the headers for the table.
    headers = ["Subdomain", "Status"]
    # Use the tabulate function to print the table with the provided data.
    print(tabulate(subdomain_statuses, headers=headers, tablefmt="grid"))
def main():
    # Define a list of subdomains to be checked.
    subdomains = [
        "www",
        "blog",
        "labs",
        "m"
        
    ]
    while True:
        # Call the check_subdomain function for each subdomain and store the results in subdomain_statuses list.
        subdomain_statuses = [check_subdomain(subdomain) for subdomain in subdomains]
        # Print the table containing subdomain statuses.
        print_table(subdomain_statuses)
        # Wait for 60 seconds before checking again (to avoid excessive requests).
        time.sleep(60)
if __name__ == "__main__":
    # Call the main function when the script is executed directly.
    main()
