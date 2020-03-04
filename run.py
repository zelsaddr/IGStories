import requests,json, random, re, time
from threading import Thread
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
uname = input("Input ur Username: ")

def reff():
    global user_agent_rotator
    while True:
        headers = {
            'User-Agent': str(user_agent_rotator.get_random_user_agent()),
        }
        response = requests.get('http://167.86.120.199/~salimsea/?param=igstory&keyword={}'.format(uname), headers=headers)
        if response.status_code == 200 and "View sent" in response.text:
            print(re.search('"msg":"(.*?)"', response.text).group(1))
        else:
            print("Failed to send")

for _ in range(int(20)):
    Thread(target=reff).start()