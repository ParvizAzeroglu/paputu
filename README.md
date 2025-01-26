# PAPUTU

[Installation](#installation) - [Guide](#guide) - [Known Issues](#known-issues)  - [License](LICENSE)


<p align="center">
  <br>
  <img src="doc/paputu.jpg"/>
  <br>
  <span>Learn and use in 3 minutes!</span>
  <br>
</p>
Paputu is a Python backend framework designed for simple use cases. It is easy to use and learn (around 3 minutes).
Paputu doesn't use any external modules, it only relies on Python's built-in modules. So, you don't need to use pip.
## Installation


To get started with Paputu, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/paputu.git
   ```
2. Navigate into the project directory:
   ```bash
   cd paputu
   ```
3. Run the Project (Framework)
    ```bash
    python index.py
    ```
Now you're all set up to start using Paputu!
Paputu doesn't use any external modules, it only relies on Python's built-in modules. So, you don't need to use pip.

## Guide


Currently, you can only work with the `index.py` file. Follow these steps to get started with the Paputu framework:

### 1. Import Paputu Framework
First, import the Paputu framework from `framework/paputu.py`:

```python
from framework.paputu import Paputu
```

### 2. Create a Route
Next, define a route using the following code:

```python
Paputu.get("/", home_handler)
 ```
Here, `home_handler` is a callback function that will handle requests to the specified route `(/)`.

### 3. Create a Callback Function
Define the callback function to serve the desired content:

```python 
def home_handler(_): 
    _.serve_static_page("templates/index.html")
```
The `serve_static_page` method takes two parameters:

- **1st parameter**: The file path (**required**).
- **2nd parameter**: The status code (**optional**, defaults to `200`).

### 4. Run the Server
Finally, start the server using:

```python
Paputu.run()
```
That's it! Your server will now be running and ready to handle requests.
***

### Additional
If you want to customize the 404 page, edit the file located at `framework/404.html`.

## Known Issues

- External CSS, JavaScript, and other assets cannot be used. You can only work with plain HTML.
- The POST method is not supported.
