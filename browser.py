from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

userfile = "user.txt"
openuser = open(userfile, 'r')
userlines = openuser.readlines()  
usernameFile = userlines[0]           # first line of user.txt represents username
passwordFile = userlines[1]           # second line of user.txt represents password

opengotolink = open("gotouser.txt","r")
gotouserlines = opengotolink.readlines() 
if len(gotouserlines) == 1:
    gotouserFile = gotouserlines[0]
else:
    gotouserFile = usernameFile


t = time.localtime()
year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())
current_time = time.strftime("%d.%m.%Y_time_%H_%M_%S", t)

class Browser:
    def __init__(self,link):
        self.link = link
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        Browser.runInstagram(self)

    def runInstagram(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.login(self)
        Browser.getFollowers(self)
        Browser.getFollowing(self)       
    
    def getFollowing(self):
        self.browser.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a").click()
        time.sleep(4)

        Browser.scrollDown(self)

        followinglist = self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

        for person in followinglist: 
            with open("following_"+current_time+".txt", "a+") as followingfile:
                followingfile.writelines(person.text+"\n")     
        followingfile.close()

        self.browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3)").click()
        exit()

    def getFollowers(self):
        self.browser.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(2) > a").click()
        time.sleep(4)

        Browser.scrollDown(self)

        followerslist = self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

        for person in followerslist:
            with open("followers_"+current_time+".txt", "a+") as followersfile:
                followersfile.writelines(person.text+"\n")     
        followersfile.close()

        self.browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3)").click()                     

    def scrollDown(self):
        jsScrollControlling = """
        page = document.querySelector(".isgrP");
        page.scrollTo(0,page.scrollHeight);
        var pageEnd = page.scrollHeight;
        return pageEnd;
        """

        pageEnd = self.browser.execute_script(jsScrollControlling)
        while True:
            end = pageEnd
            time.sleep(1)
            pageEnd = self.browser.execute_script(jsScrollControlling)

            if end == pageEnd:
                break

    def login(self):
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")

        username.send_keys(usernameFile)
        password.send_keys(passwordFile)
        time.sleep(1)

        loginButton = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div")
        
        loginButton.click()
        time.sleep(4)

        self.browser.get(self.link + "/" + gotouserFile)

        time.sleep(4)
