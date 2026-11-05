## Task 2 - Web app

What is responsible for hosting and delivering content for web applications?

Answer: `web server`

Which tool is used to access and interact with web applications?

Answer: `web browser`

Which component acts as a protective layer…?

Answer: `web application firewall`

## Task 3 - Uniform Resource Locator

Q5) Which protocol provides encrypted communication to ensure secure data transmission between a web browser and a web server?  
Answers : `HTTPS`

Q6) What term describes the practice of registering domain names that are misspelt variations of popular websites to exploit user errors and potentially engage in fraudulent activities?  
Answers : `Typosquatting`

Q7) What part of a URL is used to pass additional information, such as search terms or form inputs, to the web server?  
Answers : `Query String`

## Task 4 - HTTP Messages

Q8) Which HTTP message is returned by the web server after processing a client’s request?  
Answers : `HTTP response`

Q9) What follows the headers in an HTTP message?  
Answers : `Empty Line`

## Task 5 - HTTP Request: Request Line and Methods

Q11) Which HTTP protocol version became widely adopted and remains the most commonly used version for web communication, known for introducing features like persistent connections and chunked transfer encoding?  
Answers : `HTTP/1.1`

Q12) Which HTTP request method describes the communication options for the target resource, allowing clients to determine which HTTP methods are supported by the web server?  
Answers : `OPTIONS`

Q13) In an HTTP request, which component specifies the specific resource or endpoint on the web server that the client is requesting, typically appearing after the domain name in the URL?  
Answers : `URL Path`

## Task 6 - HTTP Request: Headers and Body

Q14) Which HTTP request header specifies the domain name of the web server to which the request is being sent?  
Answers : `Host`

Q15) What is the default content type for form submissions in an HTTP request where the data is encoded as key=value pairs in a query string format?  
Answers : `application/x-www-form-urlencoded`

Q16) Which part of an HTTP request contains additional information like host, user agent, and content type, guiding how the web server should process the request?  
Answers : `Request Headers`

## Task 7 - HTTP Response: Status Line and Status Codes

Q17) What part of an HTTP response provides the HTTP version, status code, and a brief explanation of the response's outcome?

Answers : `Status Line`

Q18) Which category of HTTP response codes indicates that the web server encountered an internal issue or is unable to fulfil the client's request?

Answers : `Server Error Responses`

Q19) Which HTTP status code indicates that the requested resource could not be found on the web server?  
Answers : `404`

## Task 8 - HTTP Response: Headers and Body

Q20) Which HTTP response header can reveal information about the web server’s software and version, potentially exposing it to security risks if not removed?  
Answers : `Server`

Q21) Which flag should be added to cookies in the Set-Cookie HTTP response header to ensure they are only transmitted over HTTPS, protecting them from being exposed during unencrypted transmissions?  
Answers : `Secure`

Q22) Which flag should be added to cookies in the Set-Cookie HTTP response header to prevent them from being accessed via JavaScript, thereby enhancing security against XSS attacks?  
Answers : `HttpOnly`

## Task 9 - Security Headers

Q23) In a Content Security Policy (CSP) configuration, which property can be set to define where scripts can be loaded from?  
Answers : `script-src`

Q24) When configuring the Strict-Transport-Security (HSTS) header to ensure that all subdomains of a site also use HTTPS, which directive should be included to apply the security policy to both the main domain and its subdomains?  
Answers : `includeSubDomains`

Q25) Which HTTP header directive is used to prevent browsers from interpreting files as a different MIME type than what is specified by the server, thereby mitigating content type sniffing attacks?  
Answers : `nosniff`

## Task 10 - Practical Task: Making HTTP Requests

Q25) Make a **GET** request to `/api/users`. What is the flag?

Answers : `THM{YOU_HAVE_JUST_FOUND_THE_USER_LIST}`

Q25) Make a **POST** request to `/api/user/2` and update the **country** of Bob from **UK** to **US**. What is the flag?

Answers : `THM{YOU_HAVE_MODIFIED_THE_USER_DATA}`

Q25) Make a **DELETE** request to `/api/user/1` to delete the user. What is the flag?

Answers : `THM{YOU_HAVE_JUST_DELETED_A_USER}`
