Welcome to my in depth study of Flask!  
Massive thanks to Corey Schafer on Youtube for his incredibly clear and in-depth tutorials!  
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH  

MVC:  
<img src="https://www.tutorialspoint.com/mvc_framework/images/model_view_controller.jpg">  
Model:  
The Model component corresponds to all the data-related logic that the user works with.  
This can represent either the data that is being transferred between the View and Controller components or any other business logic-related data.  
  
View:  
The View component is used for all the UI logic of the application.  

Controller:  
Controllers act as an interface between Model and View components to process all the business logic and incoming requests, manipulate data using the Model component and interact with the Views to render the final output.  

Flask is a Micro Framework  

Creating a blog web page using Flask  


```python
from flask import
Flask
render_template
url_for
request

```
  
```python
app = Flask(__name__)
# app - instance of Flask class
# __name__ = special variable in python - the name of the module
```
route decorator - what we type into our browser to go to different pages  

```python
if __name__ == "__main__":  # running the script with python directly
    app.run(debug=true)  # updates page without having to stop and reload
```
