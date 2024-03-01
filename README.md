# Get the Status Page of Services via API Calls
Explain: 
1. app.py is the main program
2. app.py uses the "requests" library for accessing via API to Slack status page
3. app.py uses the "flask" library for displaying the status in a web page
4. index.html is the file where we design how our web page will look like
5. @app.route('/'): This line decorates the index() function with a route. It tells Flask that the index() function should be invoked when a request is made to the root URL ('/') of the web application.
6. def index(): This is the Python function that represents the behavior of the root URL. It returns the rendered HTML template with the Slack status information.
7. By using decorators like @app.route('/'), Flask allows developers to define routes and map them to specific functions easily and cleanly. This is a common pattern in Flask applications for defining the routing behavior.





