# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from dotenv import load_dotenv
# import os
# from selenium.common.exceptions import StaleElementReferenceException

from ollama import chat
from ollama import ChatResponse

# load_dotenv()
# alltext = []


# class Driver:
#     def __init__(self):
#         self.driver = webdriver.Chrome()

#     def quit(self):
#         self.driver.quit()

#     def login(self):
#         email = os.getenv("EMAIL")
#         password = os.getenv("PASSWORD")

#         self.driver.get("https://linkedin.com/login")
#         self.driver.implicitly_wait(5)

#         email_input = self.driver.find_element(By.NAME, "session_key")  # email
#         email_input.send_keys(email)

#         password_input = self.driver.find_element(
#             By.NAME, "session_password"
#         )  # password
#         password_input.send_keys(password)

#         password_input.send_keys(Keys.ENTER)

#     def find_posts(self):
#         self.driver.implicitly_wait(20)
#         # time.sleep(10)
#         try:
#             more = self.driver.find_elements(
#                 By.CSS_SELECTOR,
#                 "button._6b402a49._0ce95c7a.e38d9b8a._8acf69a4.a95bd0b8._0f812200._89be78b6._45f9f5d1.e93e1661.a549b566._2aa54fbc._32dfa89d._8ed067c3.b44fbc2b._06074ef7",
#             )
#             for m in more:
#                 self.driver.execute_script(
#                     "window.scrollBy(0, document.body.scrollHeight);"
#                 )
#                 self.driver.implicitly_wait(1)
#                 m.click()
#             posts = self.driver.find_elements(By.CSS_SELECTOR, "div._0b16c76c")

#             for i in range(len(posts)):
#                 p = self.get_fresh_element(i)
#                 if not p:
#                     continue

#                 try:

#                     text = p.text  # AFTER scroll (fresh element)
#                     if "… more" in text:
#                         print("\033[91mWARNING: Bot did not click more button\033[00m")

#                     # for t in alltext:
#                     #    if t == text:
#                     #       print("\033[33mDeleted: " + text + "\033[0m")
#                     #       detected = True
#                     #       break
#                     if text in alltext:
#                         print("\033[33m Not added: " + text + "\033[0m")
#                     else:
#                         print("\033[32mAdded: " + text + "\033[0m")
#                         alltext.append(text)

#                     # with(open(cache_file, "a", encoding="utf-8")) as f:
#                     #    f.write(text + "\n")

#                 except StaleElementReferenceException:
#                     continue

#         # self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
#         # self.driver.implicitly_wait(2)
#         except Exception as e:
#             print(e)

#     def get_fresh_element(self, index):
#         for _ in range(5):
#             try:
#                 return self.driver.find_elements(By.CSS_SELECTOR, "div._0b16c76c")[
#                     index
#                 ]
#             except StaleElementReferenceException:
#                 time.sleep(0.2)
#         return None

#     def send_text(self, alltext):
#         cache_file = "cache.txt"
#         with open(cache_file, "w", encoding="utf-8") as f:
#             for t in alltext:
#                 f.write(t + "\n")

# # class AIClassifier:
# #     def __init__(self):
# #         self.driver = 

# new_driver = Driver()
# new_driver.login()
# new_driver.find_posts()
# new_driver.send_text(alltext)
with open("cache.txt", "r", encoding="utf-8") as f:
  response: ChatResponse = chat(model='gemma3:27b', messages=[
    {
      'role': 'user',
      # 'content': 'How many posts are there, and how many posts are AI generated? Text starts now. \n' + f.read() + "\n Text ends now.",
      'content': f.read() + "\n Text ends now. What percent of posts are AI generated?",
    },
  ])
  print(response['message']['content'].replace("#", "").replace("*", ""))

# problem: qwen3:4b doesnt answer my questions
# problem, gemma3:27b doesnt answer my questions