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
