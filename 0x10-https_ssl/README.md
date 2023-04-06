In this assignment, I gained knowledge on the significance and functionality of HTTPS. I successfully set up certbot certificates and HAproxy SSL termination on my HolbertonBnB web servers.

Tasks
0. HTTPS ABC

0-https_abc: This file contains responses to the following questions:
What is HTTPS?
It is a secure version of HTTP.
Why do you need HTTPS?
To encrypt all communication between the client and the website servers, including sensitive information such as credit card and social security numbers.
1. World wide web

1-world_wide_web: This bash script provides details about subdomains on my configured servers.
Usage: ./1-world_wide_web <domain> <subdomain>
Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
If no subdomain parameter is passed, information about the subdomains www, lb-01, web-01, and web-02 is displayed in that order.
2. HAproxy SSL termination

2-haproxy_ssl_termination: This file is the HAproxy configuration that enables encrypted SSL traffic for the subdomain www. on TCP port 443.
3. No loophole in your website traffic

100-redirect_http_to_https: This file is the HAproxy configuration that automatically redirects HTTP traffic to HTTPS to prevent any security loopholes.
