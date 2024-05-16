import requests
import time
def main():

    url = 'http://www.kamtape.com/index.php?&session=gAJ9cQEoVQxlcnJvcl9maWVsZHNxAmNfX2J1aWx0aW5fXwpzZXQKcQNdhVJxBFUGZXJyb3JzcQVdcQZVIFNpZ251cHMgY2xvc2VkLCBjaGVjayBiYWNrIGxhdGVycQdhVQhtZXNzYWdlc3EIXXEJdS4='
    offline = 'Sorry, something went wrong. Check back later!'
    offline2 = "Signups closed, check back later"
    response = requests.get(url)
    time.sleep(10)
    # Get the HTML content from the response
    html_content = response.text

    # Check if the target message is present in the HTML source
    if offline in html_content:
        print(f"[>] Website Down.")
    if offline2 in html_content:
        print(f"[>] Registration Down.")
    else:
        print(f"[!] KAMTAPE ONLINE?")
        #print(html_content)


while True:
    main()