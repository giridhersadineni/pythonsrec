import pyqrcode
url=pyqrcode.create("https://www.github.com/giridhersadineni/pythonsrec")
url.svg('uca-url.svg',scale=8)
print(url.terminal(quiet_zone=1))