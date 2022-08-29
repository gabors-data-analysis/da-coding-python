# Set up environment
## Get Python

1. Install latest version of Python from the [official website](https://www.python.org/downloads/). **We used [version 3.8](https://www.python.org/downloads/release/python-3811/)**

2. We suggest to use [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/) to edit and run Python code. You can install it via `pip` by running `pip3 install jupyter` in your terminal/PowerShell. 


## How to run case studies and coding class in Python

1. **Install `Pipenv`**

    We use [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/index.html) for Python dependency management. First, install it via `pip` by running the following code in your terminal/PowerShell:

    ```
    pip3 install pipenv
    ```

2. **Create virtual environment and install required packages**

    Go to the `da-coding-python` folder to create a virtual environment and install packages by running the following code in your terminal/PowerShell:

    ```
    pipenv sync
    ```

    This installs the required Python version and packages stored in the `Pipfile.lock`.



3. **Run Jupyter Notebook**

    To start a Jupyter Notebook in this virtual environment, go to the `da-coding-python` folder and run the following code in your terminal/PowerShell:

    ```
    pipenv run jupyter notebook
    ```

    The jupyter environment should be opened on your default browser. You are good to go!

**NOTE:** For Windows users, the above code chunks might result in an error, because the `pipenv` terminal shortcut sometimes does not install properly. In this case, run ```python3 -m pipenv sync``` and ```python3 -m pipenv run jupyter notebook```.


## VS Code: An IDE For Python Scripts

While the course is using Jupyter nootebooks, Python codes in production environments are run from script files ending with a `.py` extension. Jupyter offers a simple text editor to write script files but most developers use some special software application, a so-called 'integrated development environment', or IDE, to write these scripts. 

From the many possible alternative IDEs we recommend Visual Studio Code, or VS Code, a free Microsoft tool for these developments. It is a light-weight code editor with miriad of possible extensions which enable VS Code to support basicly *any* kind of programming languages. Beyond particular language supports VS Code also has solutions for things like version control, container management or cloud access. VS Code works equally well on Windows, MAC or Linux. 

VS Code can be downloaded from [here](https://code.visualstudio.com/) and tutorials can be accessed through the [documentation](https://code.visualstudio.com/docs).

We recommend using the [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension for Python projects but other options can equally be fine. The course does not cover the deployment of production-ready Python solutions, so VS Code is just an optional component of your toolkit for using Python later. 



## Appendix: A Primer On Virtual Environments

A virtual environment is an isolated workspace for a particular project. In effect it is a directory structure which contains Python executable files and other files which tell Python the packages and their version numbers to use in that project. We set up this environment to make sure that all readers get exactly the same results when running the code snippets on the book's exercises. 

If you want ot take a deep dive into Python's virtual environment read [this](https://realpython.com/python-virtual-environments-a-primer/) detailed discussion of the topic. Beyond the dosumentation we refer above you can also get some more technical information about `pipenv` [here](https://pipenv-searchable.readthedocs.io/). 

Nevertheless, you don't need to be an expert on virtualenvs in order to be able to follow the course material. 
