
# Press x to Cat
Revival of "Press x to Cat" from Ginger. This app will copy clean cat facts to your keyboard using cat-fact.herokuapp.com API. The facts may be a bit weird, not accurate or just not as good as they used to be in Ginger versions. I will try to find a better API or just to get better results. I already need to filter out a lot of none-facts and weird strings. Maybe I'll just create a database of accurate good facts myself.

![alt text](https://github.com/nexuma/pressxtocat/blob/main/logo.png?raw=true)
## Installation
Download .exe from [releases](https://github.com/nexuma/pressxtocat/releases/tag/stable) or "build" the app manually.
There is currently no executable for MacOS or Linux. You will have to make it yourself using pyinstaller or just run the script for now.


### Run script manually on MacOS and Linux
#### Checking for Python3
You will need to have python3 on your MacOs or Unix machine. 

Maybe you already have it, check by opening the terminal and typing ```python3 --version```. If you get an output you're good. If not, download the latest 3.x version from the [official python website](https://www.python.org/downloads/)
#### Run the script
1. Download the repository and open a terminal at that location. ( Open terminal and type ```cd $PATH_TO_FOLDER``` )
2. ```python3 -m venv venv``` this creates a virtual environement for the program to keep it seperated
3. ```source .env/bin/activate``` this activates the environement, you should see a (.env) at the beginning of the line
4. ```pip install -r requirements.txt``` this install the required libraries for the project
5. ```python3 main.py``` launches the app
6. To deactivate the environement just type ```deactivate```

### Run script manually on Windows 
#### Checking for Python3
You will need to have python on your PC. Maybe you already have it, check by opening the terminal and typing ```python3 --version```. If you get an output you're good. If not, download on the latest 3.x version from the [official python website](https://www.python.org/downloads/)
#### Run the script
1. Download the repository and open a terminal at that location. ( windows key + R -> type "cdm" press "enter" then type ```cd $PATH_TO_FOLDER``` inside the opened window )
2. ```python3 -m venv .env``` this creates a virtual environement for the program to keep it seperated
3. ```call ./.env/Script/activate.bat``` this activates the environement, you should see a (.env) at the beginning of the line
4. ```pip install -r requirements.txt``` this install the required libraries for the project
5. ```python3 main.py``` launches the app
6. To deactivate the environement just type ```deactivate```



