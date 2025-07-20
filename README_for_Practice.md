🧠 Python + SRE Practice Problems
Log Analyzer
Write a function that reads a log file (sample.log) and returns a dictionary with the count of each HTTP status code (e.g., 200, 404, 500).
Use: file handling, dictionary, regex

Disk Space Checker
Given a dictionary of servers with disk usage in percentage:

python
Copy
Edit
servers = {"web1": 65, "db1": 91, "cache1": 55, "web2": 88}
Write a function to return a list of servers with usage above 85%.
Use: dictionary, list comprehension

Retry Decorator
Write a decorator @retry that retries a function 3 times if it fails with an exception, then raises the error.
Use: decorators, exception handling

IP Address Validator
Write a function to validate a list of IP addresses using regex. Return only valid IPs.
Input:

python
Copy
Edit
ips = ['192.168.1.1', '10.300.12.3', '172.16.0.256', '172.16.0.1']
Use: regex, lists

Service Uptime Parser
Given a list of strings from uptime command outputs like:

css
Copy
Edit
["10:23:45 up 12 days, 3:45, 1 user, load average: 0.12, 0.11, 0.13"]
Write a function to extract how many days each system has been up.
Use: regex, string parsing, list

SSH Port Mapper
You have a dictionary of servers and ports:

python
Copy
Edit
ports = {'web1': 22, 'web2': 22, 'db1': 2222, 'cache': 2200}
Write a function that inverts the dictionary, mapping port to a list of hostnames.
Use: dictionary, defaultdict

Error Tracker
Write a function that reads a text file and tracks the most common error keyword (e.g., "ERROR", "FAIL", "TIMEOUT"). Return a dictionary with their counts.
Use: file handling, regex, dictionary

Process Filter
From a list of process strings like:

css
Copy
Edit
["nginx 1234", "python3 2312", "java 4321", "python3 8765"]
Filter only python-related processes and return their PIDs as integers.
Use: list, regex, int conversion

Command Timer (Decorator)
Create a decorator that measures and prints the time taken to execute a function.
Use: decorators, time module

System Inventory Merger
You have two lists of dictionaries:

python
Copy
Edit
sys1 = [{"host": "web1", "ip": "192.168.1.1"}, {"host": "db1", "ip": "192.168.1.2"}]
sys2 = [{"host": "web2", "ip": "192.168.1.3"}, {"host": "db1", "location": "DC1"}]
Merge entries with the same host into a single dictionary.
Use: dictionary, list iteration, merging logic
