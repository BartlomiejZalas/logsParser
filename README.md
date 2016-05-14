# logsParser

### Description

Python script which parses server logs in NGINX format to python collection of objects.

### Usage

Simple usage is presented in SimlpeUsage.py. 

### Format of Log object

Script generates collection of objects of Log class where each object represents one log line.
Attributes of Log class:

- client_ip - (string) client IP address
- client_identd - (string) identity of the client 
- user_id - (string) - username determined by HTTP authentication 
- date_time - (datetime) - date and time of request
- request_type - (string) request method
- requested_resource - (string) requested resource
- response_code - (int) HTTP code of response
- content_size - (int) size of requested content
- agent - (string) - informations about client browser

### Python version

Scrip works on Python 3.4.3 or higher

### Author

Bartłomiej Zalas


