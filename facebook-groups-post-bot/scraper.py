import os
import json

from dotenv import load_dotenv
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from logs import logger
from time import sleep, time
from scraping_manager.automate import WebScraping

# Read env vars 
load_dotenv ()
CHROME_FOLDER = os.getenv("CHROME_FOLDER")
WAIT_MIN = int(os.getenv("WAIT_MIN","1"))
PROFILE = os.getenv("PROFILE")
PUBLISH_LABEL = os.getenv("PUBLISH_LABEL")
VISIT_LABEL = os.getenv("VISIT_LABEL")


class Scraper (WebScraping):

    def __init__(self):
        """ read data from json file and start scraper using chrome folder """
        # Files paths
        current_folder = os.path.dirname(__file__)
        self.data_path = os.path.join(current_folder, "data.json")

        # Read json data
        with open(self.data_path, encoding="UTF-8") as file:
            self.json_data = json.loads(file.read())

        # Start scraper
        super().__init__(chrome_folder=CHROME_FOLDER, start_killing=True, user_agent=True, profile=PROFILE)

        self._do_login()

    def _do_login(self):
        EMAIL = "avijoshi323@gmail.com"
        PASSWORD = "Av@12345"

        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()

        email_box = self.driver.find_element(By.ID, "email")
        email_box.clear()
        email_box.send_keys(EMAIL)

        password_box = self.driver.find_element(By.ID, "pass")
        password_box.clear()
        password_box.send_keys(PASSWORD)

        login_button = self.driver.find_element(By.NAME, "login")
        login_button.click()
        sleep(15)

    def post_in_groups (self):
        """ Publish each post in each group from data file """

        ################################ Loop each group
        # posts_done = []
        global post_text, post_attachment
        for group in self.json_data["groups"]:
            self.set_page(group)
            sleep (2)

            ################# Get random post
            for post in self.json_data["posts"]:
                post_text = post.get("content", {}).get("title", "")
                post_attachment = post.get("content", {}).get("attachment", "")
                print("Text:", post_text)
                print("Attachment:", post_attachment)
                ###################### Open text input
                elem = self.driver.find_element(By.XPATH, "//span[text()='Write something...']")
                elem.click()
                sleep(5)

                # add context on popup
                elem1 = self.driver.find_element(By.XPATH, "//div[@aria-placeholder='Write something...']")
                # Send the text first
                elem1.send_keys(post_text)
                elem1.send_keys(Keys.SPACE)

                # Add a newline to separate text and link
                elem1.send_keys(Keys.SHIFT, Keys.ENTER)
                elem1.send_keys(Keys.SHIFT, Keys.ENTER)

                # Paste the YouTube link
                elem1.click()
                elem1.send_keys(post_attachment)
                sleep(5)

                elem = self.driver.find_element(By.XPATH,"//div[@aria-label='Post']")
                sleep(5)
                elem.click()
                sleep (5)
                print("Post submitted successfully.")

    def save_groups (self, keyword):
        """ Sedarch already signed groups and save them in data file """
        
        # Set groups page
        logger.info ("Searching groups...")
        search_page = f"https://www.facebook.com/groups/search/groups/?q={keyword}&filters=eyJteV9ncm91cHM6MCI6IntcIm5hbWVcIjpcIm15X2dyb3Vwc1wiLFwiYXJnc1wiOlwiXCJ9In0%3D"
        self.set_page(search_page)
        sleep (3)
        self.refresh_selenium()
        links_num = 0
        tries_count = 0
        
        selectors = {
            "group_link": f'.x1yztbdb div[role="article"] a[aria-label="{VISIT_LABEL}"]',
        }
        
        # Scroll for show already logged groups
        while True:
            self.go_bottom()
            new_links_num = len(self.get_elems (selectors["group_link"]))
            if new_links_num == links_num:
                tries_count += 1
            else: 
                links_num = new_links_num
                    
            if tries_count == 3:
                break
            
        # Get all link of the groups
        links = self.get_attribs (selectors["group_link"], "href")
        logger.info (f"{len(links)} groups found and saved")
        
        # Save links in jdon file
        if links:
            self.json_data["groups"] = links
            with open (self.data_path, "w", encoding="UTF-8") as file:
                file.write (json.dumps(self.json_data))
                
            
        
         
