"""
Installing virtual environment:
To install a virtual environment, we use the command pip install virtualenv
To do this, open the terminal on mac or Linux, cmd on windows and type the following command to install a virtual environment;

# pip install virtualenv

To check the version of your virtualenv type;

# virtualenv --version

Creating a virtual environment:
After successful installation of virtualenv, you can create a virtual environment with your desired name using the following command.

Syntax:
virtualenv virtualenvironment_name

Virtualenv MyDataAnalyticEnv
j
After successfully creating the virtual environment, for you to use it, you need to activate so you can enter into that particular isolated environment.

Activating virtual environment
Syntax on windows:

Virtualenvname\scripts\activate

Activating virtualenv called MyDataAnalyticEnv

MyDataAnalyticEnv\scripts\activate

Syntax on Linux/mac

Source Virtualenvname/bin/activate

Activating virtualenv called MyDataAnalyticEnv

Source MyDataAnalyticEnv /bin/activate

After activation, you can now install all the required libraries and modules you need to work on your project.

When done working on the project, you can deactivate the virtualenv using the following command

deactivate
"""