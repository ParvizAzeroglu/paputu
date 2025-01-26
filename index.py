from framework.paputu import Paputu 

def home_handler(_): 
    _.serve_static_page("templates/index.html")

Paputu.get("/", home_handler)

Paputu.run()

# Read the README.md file to learn about the Paputu framework in 5 minutes!





