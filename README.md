# UHD Bing Wallpapaer for Mac
A simple Python script capable of batch-downloading and setting UHD version of Bing image of the day as wallpaper on macOS.

## Usage
If you only want to set the latest Bing image of the day as your wallpaper, simply download the automation from [Releases](https://github.com/fluffyfoxxo/Bing-Wallpaper-for-Mac/releases) and run! You can make it run automatically [when you log in](https://support.apple.com/guide/mac-help/open-items-automatically-when-you-log-in-mh15189/mac) or [on schedule](https://www.computerworld.com/article/3322125/how-to-automate-your-mac-with-calendar.html).

You can modify the Configurations section to set your own image directory and country code. Wallpapers will be saved to **/Users/USERNAME/Pictures** by default and will be immediately removed after setting wallpaper.

Use `-d` or `--download` argument to download and save the last 8 pictures without changing the current wallpaper. You might use this option if you want to change wallpapers automatically by adding the wallpaper directory in **System Preferences**.

```
python bing.py -d
```

Use `-h` or `--help` to display help message.
\

## License
Licensed under the MIT License.

## Credits
- [declangao/Bing-Wallpaper-for-Mac](https://github.com/declangao/Bing-Wallpaper-for-Mac)
