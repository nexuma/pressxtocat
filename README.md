
# Press x to Cat
Revival of "Press x to Cat" from Ginger. This app will periodically copy cat facts to your clipboard.

![alt text](https://github.com/nexuma/pressxtocat/blob/main/logo.png?raw=true)
## Usage and Features
- Use the slider to dictate how much time the fact will stay on the clipboard before being replaced by another one.
- The activate button starts copying the facts to the clipboard.
- You can limit the length of the facts to 200 characters so they fit in game chats.
- You can change the theme of the app between light, dark or system, however the app does not remember your settings yet.

## Installation
Download the right executable file for your system from [releases](https://github.com/nexuma/pressxtocat/releases) or launch the script manually.
### MacOs
Download and unzip the "pressxtocat.app.zip" and execute the pressxtocat.app that is inside. The icon on the top bar of the window is broken for now.
### Windows
Download and execute the "pressxtocat.exe".
## Notes and Bugs
- Some fact have weird characters inside, I already filter some of them but not all.
- The mac version takes a bit of time to launch.
- I did not test anything on any linux distro.
- There are around 300 facts in total. Maybe I will collect cat facts and create a bigger list later.
- The app does not remember settings for now.
- I will add other animal or subjects to choose from later.
- When using windows 10 the taskbar icon may sometimes be invisible. No idea how to fix that already tried a lot.

## Manual execution
### Run script manually on MacOS and Linux
#### Checking for Python3
You will need to have python 3 on your MacOs or Unix machine. There are problems with python versions below 3.10, if you run into any problems use python version 3.10 or above.

Maybe you already have it, check by opening the terminal and typing ```python3 --version```. If you get an output with the right version you're good. If not, download the latest 3.x version from the [official python website](https://www.python.org/downloads/).
#### Run the script
1. Download the repository and open a terminal at that location. ( Open terminal and type ```cd /PATH/TO/FOLDER``` )
2. ```python3 -m venv .env``` this creates a virtual environement for the program, to keep it from messing with anything else.
3. ```source .env/bin/activate``` this activates the environement, you should see a (.env) at the beginning of the line.
4. ```pip install -r requirements.txt``` this install the required libraries for the project.
5. ```python3 main.py``` launches the app.
6. To deactivate the environement just type ```deactivate```.
7. Do step 3. then 5. to relaunch the app.

### Run script manually on Windows 
#### Checking for Python3
You will need to have python on your PC. Maybe you already have it, check by opening the terminal and typing ```python --version```. If you get an output you're good. If not, download on the latest 3.x version from the [official python website](https://www.python.org/downloads/).
#### Run the script
1. Download the repository and open a terminal at that location. ( windows key + R -> type "cdm" press "enter" then type ```cd C:/PATH/TO/FOLDER``` inside the opened window ).
2. ```python3 -m venv .env``` this creates a virtual environement for the program, to keep it from messing with anything else.
3. ```call .env/Scripts/activate.bat``` this activates the environement, you should see a (.env) at the beginning of the line.
4. ```pip install -r requirements.txt``` this install the required libraries for the project.
5. ```python main.py``` launches the app.
6. To deactivate the environement just type ```deactivate```.
7. Do step 3. then 5. to relaunch the app.
