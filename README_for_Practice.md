🧠 Python Practice Problems for SRE Role:

1. Log Aggregator (Dictionary + List):
Write a Python function that takes a list of log entries (each a string in the format "[ERROR] Disk full at /dev/sda1"), and returns a dictionary where the key is the log level (INFO, WARNING, ERROR) and the value is a list of corresponding messages.

2. Service Health Checker (Regex):
Given a string containing multiple service status messages like "Service: nginx [UP], Service: mysql [DOWN], Service: redis [UP]", extract and return a list of only the service names that are DOWN using regular expressions.

3. IP Allocator (Lists + Ranges):
Write a function that receives a subnet range (like 192.168.1.0/29) and returns a list of usable IPs (excluding network and broadcast addresses). You may use the ipaddress module.

4. Decorator for Retry Logic (Decorators):
Write a decorator called @retry_on_failure that retries a function up to 3 times if it raises an exception, with a 1-second delay between retries.

5. Config Validator (Regex + Dict):
Given a list of strings representing configuration lines like "hostname=webserver1", "ip=192.168.1.10", "port=8080", validate each line using regex and return a dictionary. If the config line is malformed, skip it.

6. Disk Usage Analyzer (List + Dict):
Given a list of tuples like [('sda1', 40), ('sda2', 80), ('sda3', 90)] where the first element is the disk name and the second is usage in %, write a function that returns disks with usage above 75%.

7. Custom Iterator for Service Status:
Create a class ServiceStatusIterator that iterates over a dictionary like {'nginx': 'running', 'mysql': 'stopped'} and yields formatted strings like "nginx is running".

8. Port Availability Filter (Lists + Sets):
Write a function that takes two lists: open_ports = [22, 80, 443] and required_ports = [21, 22, 23, 80] and returns a list of ports that are required but not open.

9. Grouping Logs by Day (Datetime + Dict):
Given a list of log timestamps like "2025-07-19 10:22:33" and "2025-07-19 15:40:12", group all log entries by date and return a dictionary with date keys and list of times as values.

10. Parse and Filter Process List (Regex + Lists):
Given a multiline string simulating ps -aux output, extract all processes with memory usage > 10% using regex and return a list of dictionaries with pid, user, mem, and cmd.
