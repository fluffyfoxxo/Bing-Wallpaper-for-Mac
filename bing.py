#!/usr/bin/env python

import urllib.request, json, sys, time
from os.path import join, expanduser


SCRIPT = """/usr/bin/osascript<<END
tell application "System Events"
    tell every desktop
        set picture to "%s"
    end tell
end tell
END"""


def get_wallpaper_path():
    dir = join(expanduser("~"), 'Pictures')
    file_path = join(dir, "Bing Wallpaper.jpg")
    return file_path


def download_image(url):
    file_path = get_wallpaper_path()
    urllib.request.urlretrieve(url, file_path)
    set_wallpaper(file_path)


def set_wallpaper(file_path):
    import subprocess
    subprocess.Popen(SCRIPT%file_path, shell=True)
    subprocess.Popen("killall Dock", shell=True)
    #time.sleep(1); from os import remove; remove(file_path)


def main():
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
    response = urllib.request.urlopen(url)
    json_data = json.load(response)
    images = json_data['images']
    print(images)
    url = 'http://www.bing.com' + images[0]['url']
    urluhd = url.replace("1920x1080", "UHD")
    download_image(urluhd)


if __name__ == '__main__':
    main()
