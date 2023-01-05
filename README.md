
# Press x to Cat
Revival of "Press x to Cat" from Ginger. This app will copy cat facts to your clipboard every 300 ms using cat-fact.herokuapp.com API. I still have not tried the instructions I wrote, there may be some errors.
## Difference with original versions
The facts may be a bit weird, not accurate, full of spelling errors or just not as good as they used to be in Ginger versions. I will try to find a better API or just to get better results. I already need to filter out a lot of none-facts and weird strings. Maybe I'll just create a database of accurate good facts myself.

![alt text](https://github.com/nexuma/pressxtocat/blob/main/logo.png?raw=true)
## Usage

- The slider will dictate how much time the fact will stay on the clipboard before being replaced by another one
- The activate button starts copying the facts to the clipboard
- The refresh button fetches other facts from the API, the program has 100 facts before filtering them (there is a lot of garbage to clear) the amount varies but generally between 40 and 60 are left. Anyway, as soon as you get tired of them just hit refresh or restart the program. (this can take up to 5 seconds depending on your connection speed)
- You can change the theme of the app between light and dark, however the app does not remember your settings yet. The default is system.

## Installation
Download ".exe" or the ".app" file from [releases](https://github.com/nexuma/pressxtocat/releases) or launch the script manually.

### Run script manually on MacOS and Linux
#### Checking for Python3
You will need to have python3 on your MacOs or Unix machine. 

Maybe you already have it, check by opening the terminal and typing ```python3 --version```. If you get an output you're good. If not, download the latest 3.x version from the [official python website](https://www.python.org/downloads/).
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
You will need to have python on your PC. Maybe you already have it, check by opening the terminal and typing ```python3 --version```. If you get an output you're good. If not, download on the latest 3.x version from the [official python website](https://www.python.org/downloads/).
#### Run the script
1. Download the repository and open a terminal at that location. ( windows key + R -> type "cdm" press "enter" then type ```cd C:/PATH/TO/FOLDER``` inside the opened window ).
2. ```python3 -m venv .env``` this creates a virtual environement for the program, to keep it from messing with anything else.
3. ```call .env/Scripts/activate.bat``` this activates the environement, you should see a (.env) at the beginning of the line.
4. ```pip install -r requirements.txt``` this install the required libraries for the project.
5. ```python main.py``` launches the app.
6. To deactivate the environement just type ```deactivate```.
7. Do step 3. then 5. to relaunch the app.


