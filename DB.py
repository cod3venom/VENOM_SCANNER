import requests as req
from collections import Counter
import re
class DB:


    def debug(data):
        data.replace('<', data)
        data.replace('>',data)
        
        print("[+]  " + data)


    def getPAGE(host):
        content = req.get(host)
        return content.text

    def HTML(self,host):
        regex = "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"

        content = self.getPAGE(host)
        links = re.findall(regex,content)

        for link in links:
            self.debug(link)




     
