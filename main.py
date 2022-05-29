# start basic webdriver 
from pydoc import cli
from selenium import webdriver
from json import load, dumps
from time import sleep
import requests
from selenium_youtube import Youtube



driver = webdriver.Firefox()

    
with open("data.json", "r") as f:
    data = load(f)


with open("cookies-twitch.json", "r", encoding="UTF-8") as f:
	cookie_dict = load(f)
driver.get(cookie_dict["url"])
for cookie in cookie_dict["cookies"]:
	if cookie["sameSite"] == "unspecified":
		cookie["sameSite"] = "Lax"
	elif cookie["sameSite"] == "no_restriction":
		cookie["sameSite"] = "None"
	else:
		cookie["sameSite"] = "Strict"
	driver.add_cookie(cookie)
driver.get_cookies()

with open("cookies-yt.json", "r", encoding="UTF-8") as f:
	cookie_dict = load(f)
driver.get(cookie_dict["url"])
for cookie in cookie_dict["cookies"]:
	if cookie["sameSite"] == "unspecified":
		cookie["sameSite"] = "Lax"
	elif cookie["sameSite"] == "no_restriction":
		cookie["sameSite"] = "None"
	else:
		cookie["sameSite"] = "Strict"
	driver.add_cookie(cookie)
driver.get_cookies()

driver.get("https://www.twitch.tv/directory/following/channels")
sleep(3)
tower = driver.find_element_by_class_name("tw-tower")
sleep(3)
links = tower.find_elements_by_tag_name("a")
for link in links:
    channel_name = link.get_attribute("text")
    try:
            data[channel_name]
    except KeyError: #Clip not in there
        data[channel_name] = []
    link_text = link.get_attribute("href") + "/clips?filter=clips&range=24hr"
    driver.get(link_text)
    sleep(3)
    channel_content = driver.find_element_by_class_name("channel-info-content")
    clips = channel_content.find_elements_by_css_selector("[data-a-target='preview-card-image-link']")[:10]
    for clip in clips[:1]:
        clip_link = clip.get_attribute("href")
        image = clip.find_element_by_tag_name("img")
        link = image.get_attribute("src").split("-preview")[0] + ".mp4"
        clip_name = image.get_attribute("alt")
        print(link)
        if clip_link in data[channel_name]:
            continue # in this case we have the clip so we move to next clip
        data[channel_name].append(clip_link)
        #download the mp4 file from link
        with open(clip_name + ".mp4", "w+") as f:
            pass # making sure the file exists
        with open(clip_name + ".mp4", "wb") as f:
            print("Downloading " + clip_name + ".mp4")
            f.write(requests.get(link).content)
        
        youtube = Youtube(
            browser=driver# or firefox
            )
        upload_result = youtube.upload(f'{clip_name}.mp4', f'{channel_name} - {clip_name}', f'Twitch Link = {clip_link}', ['Twitch Clip', 'Twitch', 'Clip', channel_name])
    
