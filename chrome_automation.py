from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time

chatbot = ChatBot("badarpur boom")
trainer = ListTrainer(chatbot)
trainer.train([
    "hi",
    "hi kya haal h",
    "me thik hu",
    "thanx"
    "your name",
    "my name is Rohit AI bot"
])


def ch(x):
    # request = input("you:")
    responce = chatbot.get_response(x)
    # print(responce)
    return responce


# C:\Users\badarpurboom\AppData\Local\Google\Chrome\User Data\Default
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:/Users/badarpurboom/AppData/Local/Google/Chrome/User Data/Default')
path = r"C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path, chrome_options=option)
driver.get("https://web.whatsapp.com/")
time.sleep(15)
while True:
    try:
        # process to find all user name
        user_list = driver.find_elements_by_class_name("_2aBzC")
        k = []

        for i in range(len(user_list)):
            try:
                value = user_list[i].find_element_by_class_name("_38M1B").text
                unread = (int(value))
                if unread > 0:
                    a = user_list[i].find_element_by_class_name("_35k-1._1adfa._3-8er").text
                    k.append(a)
                else:
                    pass

            except:
                pass

                # process to open unread message and give reply to all user in list in "K=[]"
            for i in range(len(k)):
                user = driver.find_element_by_xpath('//span[@title="{}"]'.format(k[i]))
                user.click()
                user_msg = driver.find_elements_by_class_name("_3-8er.selectable-text.copyable-text")
                x = user_msg[-1].text
                msg_box = driver.find_element_by_class_name('_2A8P4')
                msg_box.click()
                # time.sleep(10)
                msg_box.send_keys(str(ch(x)), Keys.RETURN)
                k = None
                user = driver.find_element_by_xpath('//span[@title="{}"]'.format("Papa Jio"))
                user.click()
    except:
        pass
        print("No new massage")
# --------------------------------------------------
