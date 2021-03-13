# instagram-follower-following-scraper

Creates a list of followers and following with the current time.  

## Usage

### WebDrive Manager

Chrome WebDrive Manager and Selenium must be installed to run the application. If they are installed, you can just run the main.py.

-[ChromeDriver-WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

-[Selenium](https://selenium-python.readthedocs.io/installation.html)

In the directory(assumed "myff") of program:

### Installation

```
myff>python -m env env
myff>python cd venv
myff\venv>cd Scripts
myff\venv\Scripts>activate
myff\venv\Scripts>cd..
myff\venv>cd ..
myff>pip install selenium

```

### Determining the Target Account
If it is required to access followers of another account instead of the followers of the account you are logged in, change the content of "gotouser.txt". 

Otherwise, there must not have content in this "gotouser.txt" file. Program will create the list of followers/following of the account which is in "user.txt".

"user.txt" file must include username in the first line and the password in the second line.

#### gotouser.txt

```
[target account username]    
```

#### user.txt
```
[username]
[password]
```

### Commands to Run

```
myff>python main.py

```

### Instance of Created Files

![alt text](https://i.imgur.com/Xw1SXpi.png)
