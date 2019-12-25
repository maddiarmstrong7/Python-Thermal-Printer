#!/usr/bin/python


from __future__ import print_function
import base64, json, sys, urllib, zlib
from Adafruit_Thermal import *

import urllib.request
import lxml as lh


url = "http://readpoopfiction.com/story.php?length=1"
page = urllib.request.urlopen(url)
doc = str(page.read())
index = doc.find("<p class=\"author\">")
doc = doc[index:-1]
index = doc.find("<p>")
doc = doc[index+3:-1]
end = doc.find("<p class=\"more\">")
result = doc[:end].replace("</p>", "").replace("\\t",
    "").replace("\\n","").replace("\\r", "").replace("<p>",
        "\n").replace("&nbsp;"," ").replace("&ldquo;","\"").replace("&rdquo;",
            "\"").split("<br />")

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
for x in result:
    printer.print(x)
    printer.println(' ')


printer.feed(3)

