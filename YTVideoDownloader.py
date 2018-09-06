import pafy, os, sys

class banner:
    header = """
YT Video Downloader by Macs

Use this tool to download any video to your computer lightning fast!
Enjoy.
"""

print banner.header
url = raw_input("Please Enter Your Youtube URL: ")
print "\n[*] Fetching Video...\n"
video = pafy.new(url)

print "[!] Video Found!\n[*] Title: " + video.title + "\n\n[*] Description: " + video.description + "\n\n[*] Creator: " + video.author

qdl = raw_input("Would you like to download this video? [Y/N] ")

try:
    if str(qdl) == "Y" or "y":
        best = video.getbest()
        print "Getting Best Resolution: " + best.resolution + best.extension
        print "\n Saving to Videos/"
        os.system("mkdir Songs")
        best.download(quiet=False, filepath="Videos/")
        print "File Downloaded! To Download Another Song Run The Same Command!"
        
except KeyError:
    pass
