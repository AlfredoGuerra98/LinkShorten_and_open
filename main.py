import pyshorteners
import webbrowser

oglink = input("\nEnter your original link : ")

short = pyshorteners.Shortener()
x = short.tinyurl.short(oglink)

print("\nShorted link is : "+x)

webbrowser.open_new(x)
