import os
import re
from PIL import Image

location = input('What is the folder\'s path for the wallpapers you wish to rename? ')

for folder_path, folders, wallpapers in os.walk(location):
    print(f'\nWorking in: {folder_path}\n')
    for wallpaper in wallpapers:
        ignore = r'[0-9][0-9][0-9]x[0-9][0-9][0-9]'
        ignore_these = re.search(ignore, wallpaper)
        if ignore_these != None:
            print(f'Resolution already listed for: {wallpaper}.')
        elif wallpaper.endswith(('.jpg', '.jpeg', '.png')):
            with Image.open(f'{folder_path}/{wallpaper}') as im:
                w, h = im.size
            new_name = f'{os.path.splitext(wallpaper)[0]}_{w}x{h}{os.path.splitext(wallpaper)[1]}'
            os.rename(f'{folder_path}/{wallpaper}', f'{folder_path}/{new_name}')
            print(f'{wallpaper} renamed to: {new_name}')
        else:
            print(f'Skipped: {wallpaper}')

print('\nDone renaming wallpapers!')

input('Press any key to exit. ')
