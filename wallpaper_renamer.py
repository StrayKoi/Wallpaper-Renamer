import os
import re
from PIL import Image


def title():
    os.system('cls')
    print('WALLPAPER RENAMER')

ignored = []
skipped = []

title()
location = input('\nWhat is the folder\'s path for the wallpapers you wish to rename?\n> ')

title()
print(f'\nI will rename ALL wallpapers found in:\n{location}\tand subfolders')
input('\nPress (ENTER KEY) to continue now.\n> ')

title()
for folder_path, folders, wallpapers in os.walk(location):
    print(f'\nWORKING IN: {folder_path}\n')
    if len(os.listdir(path=folder_path)) == 0:
        print('There were no wallpapers found in this folder.')
    else:
        print('These are the new file names:')
        for wallpaper in wallpapers:
            # Ignore any file names that already have 3-4 digits before and after an 'x'
            ignore = r'\d{3,4}x\d{3,4}'
            ignore_these = re.search(ignore, wallpaper)
            if ignore_these != None:
                ignored.append(wallpaper)
            elif wallpaper.endswith(('.jpg', '.jpeg', '.png')):
                with Image.open(f'{folder_path}/{wallpaper}') as im:
                    w, h = im.size
                new_name = f'{os.path.splitext(wallpaper)[0]}_{w}x{h}{os.path.splitext(wallpaper)[1]}'
                # os.rename(f'{folder_path}/{wallpaper}', f'{folder_path}/{new_name}')
                print(new_name)
            else:
                skipped.append(wallpaper)

        # List all ignored files as a group:
        if len(ignored) > 0:
            print(f'\nResolution already listed for:')
            for ignore in ignored:
                print(ignore)
            ignored.clear()
        else:
            pass

        # List all skipped files as a group:
        if len(skipped) > 0:
            print('\nThese are the files I\'ve skipped:')
            for skip in skipped:
                print(skip)
            skipped.clear()
        else:
            pass

print('\nDone renaming wallpapers!')
input('Press (ENTER KEY) to exit.')
