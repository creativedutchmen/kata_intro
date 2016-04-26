# KATA intro
This is a boilerplate repo for the introduction to TDD using Python.

## Installation and prerequisites
Before we start, please make sure you have a working Python installation. I will be using 3.5, but the code we write should work in 2.7 just fine.

To keep things clean, open a new terminal window in this folder, and create a new virtual environment with the following command:

    virtualenv env

This creates a new virtual environment in the `env` folder, with only the packages you install during this session. To start working in this environment, run the following command:

    source env/bin/activate

Now we have a clean python installation with only the bare minimum installed (pip, most notably). Because we will be using `nosetest` for this demo, we should install it. To keep things maintainable, I've freezed the packages I've installed into the requirements.txt file, so we can easily use pip to install them.

    pip install -r requirements.txt

Finally, to test if everything is working, let's see if we can run the tests:

    nosetests --rednose
