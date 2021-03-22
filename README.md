# Bing Wallpapaer for Mac
A simple Python script capable of batch-downloading and setting UHD version of Bing image of the day as wallpaper on macOS.

## Usage
You can modify the Configurations section to set your own image directory and country code. Wallpapers will be saved to **/Users/USERNAME/Pictures/BingWallpaper** by default and will be immediately removed after setting wallpaper.

Download today's Bing picture of the day and set it as wallpaper:

```
python bing.py
```

Use `-d` or `--download` argument to download and save the last 8 pictures without changing the current wallpaper. You might use this option if you want to change wallpapers automatically by adding the wallpaper directory in **System Preferences**.

```
python bing.py -d
```

Use `-h` or `--help` to display help message.

## License
Licensed under the MIT License.

## Credits
- [declangao/Bing-Wallpaper-for-Mac](https://github.com/declangao/Bing-Wallpaper-for-Mac)
