### Environment
#### Create an environment
Make a virtual environment. Change directory (cd) in the command line into the directory and type:

python3 -m venv [environment name] 

For example, to make the environment 'venv', use:

`
python3 -m venv venv
`

#### Activate the environment
For the example used above, in the command line, type:

`
. venv/bin/activate
`

- Note that the dot means source. And 
activate is the script and it changes the current path so the python in the venv comes first, so there is no need to type python3 or pip3 with the commands anymore, you could just type pip for example.

#### If there is a need to delete the venv
Delete the venv from the system with:
```
rm -rf venv
```


### Create a gitignore file
See herer for whst to paste into the .gitignore file:
https://github.com/github/gitignore/blob/main/Python.gitignore

Be sure the environment created is in there, in this case `venv/`.

### FastAPI


#### Install FastAPI
To install FastAPI, in the command line, run:

`pip install "fastapi[all]"`

Note that this installs it with all the optional dependencies and features. If not using [all], then Uvicorn needs to also be installed. To install Uvicorn, which will be used as the server, run:

`pip install "uvicorn[standard]"`

See the docs [here](https://fastapi.tiangolo.com/tutorial/).

### Run it
Be sure you're in the active environment. To run, use:

```
uvicorn Carsharing:app --reload
```

In the command above, `uvicorn` is the name of a Python package, which is the server that will run and handle requests for our application. We point it to our application with the next word `Carsharing` which is the name of the python module, without the .py at the end, we point it to the name of the application object in that Carsharing file, that's why we have a `:app` here, it tells uvicorn that the application object is called app. `--reload` makes sure the application is running every time we change the coade, without that we would have to restart every time we changed the code.

### Extras

#### Pydantic

#### Remove a venv
If needed, a virtual environment can be removed with:
```
rm -rf venv
```

### See the documentation

#### /docs
If you go to the endpoint /docs, you see the docs to test out the code. Go [here](http://127.0.0.1:8000/docs). You can click try it out and execute to test the code. You get the openAPI specification of the welcome document if you click `/openapi.json` in the upper left corner, which is a machine readable version of the documentation that shows our welcome operation looks like. You might use this documentation to generate client code, among other things.

#### /redoc
Another URL you can go to shows another flavor of the documentation, this endpoint is /redoc, see [here](http://127.0.0.1:8000/redoc), it contains the same information but in another format. And it has a link the API specification (specs) as well.

### Control flow
The Uvicorn server process controls the flow of our code (i.e., the code doesn't run from top to bottom like normal Python code). What the server does is wait for incoming requests, i.e., our program will do nothing until a request comes in.

When I visit a URL in my browser, e.g., [this](http://127.0.0.1:8000 ), the browser sends an HTTP GET request to the server (because I made a GET in line 8 in Carsharing.py). Now in the server log (the terminal that shows INFO: the URL the GET request with a status 200 OK), we see that the GET request was received for this path. FastAPI then looks up the operation mapped through that path, and in line 8, I've mapped the welcome function to the path `/`. So when a request comes in for `/`, FastAPI knows to call the welcome function (lines 9 to 11 in Carsharing.py), and sends the return value back to the browser which then shows the resulting message.

So, the flow of my FastAPI app is dictated by ther http requests that come in. Any operation I define will only be called if a request is made for the corresponding URL, and this can be done with the browser, or with other clients. This also mean that every time I refresh the page, a new request is made and we can see this in the log.

### Type hints
See [here](https://docs.python.org/3/library/typing.html).

### Debugging
See [here](https://fastapi.tiangolo.com/tutorial/debugging/) for debugging in FastAPI.

### Download code for videos
https://github.com/codesensei-courses/fastapi_fundamentals

### Errors
# carsharing
# carsharing
