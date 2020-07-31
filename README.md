# Wallpaper Renamer
This is a simple Python script I wrote to solve a problem that would have took me ages to rename manually. Instead of manually checking their dimensions from properties and then renaming, I wrote this script to take "wallpapername.png" and turn it into "wallpapername_1920x1080.png"

## Table of Contents
- [Techonologies](#Technologies)
- [Modules Used & Why](#Modules-Used-&-Why)
- [Other Notes](#Other-Notes)

## The Problem
Basically I had a small folder full of wallpapers I've acquired over years on the internet, many of which are different resolution sizes and a couple of odd irregulars that I thought would look nice. They were not all the same resolution as I have switched between desktop and laptop a few times that I only had the wallpaper art in at least one resolution. Though it was nice looking at the thumbnails in the folder, it kind of sucked not knowing what their resolution/dimensions were at a glance.

## Technologies
- Python 3

## Modules Used & Why
### OS
os.walk and os.rename
Self-explanatory, os.walk for the Python to see where my files are and browse any folders inside the folder path I specified. os.rename to rename the actual files

### Re
The regular expression module was used check and ignore any wallpaper files that I had attempted to rename already. It would be redundant to see something like: wallpapername_1920x1080_1920x1080.png.

The script will print the wallpaper name and print that the resolution was already in the file name.

### PIL ([Pillow](https://pypi.org/project/Pillow/))
This was the only 3rd-party module that was used, the rest came built-in to Python.
I needed something that could check the file's image dimensions and Pillow did the trick with grabbing the info and passing it over to help rename the file.

## Other Notes
This script will only rename .jpg, .jpeg, and .png and will ignore other file extensions such as .txt, .bmp, .svg.

I will admit it's a very rough script as it's one of my first Python scripts. It already served its purpose but if I ever come back to this project, here are some improvements I would like to add:
- Confirmation of folder path in case user entered to wrong location on the first go.
- Grouped list of items that were ignored or skipped listed at the end instead of seeing "Resolution already listed for: {wallpaper}" repeated and cluttered throughout.
- Grouped list of items that will be renamed and a confirmation to rename everything on the list.
- At the end, ask if there are any other folders that need wallpapers to be renamed.
- Regular expression could ask user if they would like to additionaly change a list of wallpapers manually. Such as wallpapers that are just random strings of letters and numbers.
- Maybe an ability to export changes as an .csv in case a user would need to go back and compare the old name with the new name.

### Ko-fi
Ko-fi is basically a virtual tip jar where you can support creatives for about the price of a cup of coffee.

At this time, I'm not very active on Ko-fi nor do I offer any rewards. If you love my art and feel like supporting me, hit the button below to get started.

I will appreciate any amount you choose to donate. Thank you (´• ω •`) ♡ !
<script type='text/javascript' src='https://ko-fi.com/widgets/widget_2.js'></script><script type='text/javascript'>kofiwidget2.init('Support Me on Ko-fi', '#29abe0', 'I2I77G74');kofiwidget2.draw();</script><br/>
