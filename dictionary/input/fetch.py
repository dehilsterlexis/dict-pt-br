import re
import requests
 
with open("urls.txt", encoding="utf-16") as file:
    count = 1750
    for url in file:
        url = url.strip()
        if (len(url) > 5):
            print(url)
            count = count + 1
            if count < 10:
                zeros = "00"
            elif count < 100:
                zeros = "0"
            else:
                zeros = ""
            fname = "verbs/file" + zeros + str(count) + ".txt"
            print(fname)
            html = requests.get(url)
            content = html.text
            f = open(fname, "w", encoding="utf-8")
            f.write(content)
            f.close()