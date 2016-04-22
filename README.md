# VkMusicImporter
Add your local songs to VK by searching for ID3 tags in music.

**What do you need for this to work:**

import vk_api #self-explanatory
import os #used for reading your music library
import pyantigate #used for deciphering Captcha that will pop-up every 10 tracks or so
from mutagen.id3 import ID3 #used for reading ID3 info

## Usage

To use this app you will have to enter following information:
1. Your vk.com login and password
2. Your antigate.com key
3. Your antigate.com maximum bid for 1 solved captcha
4. Path to the dirrectory that stores your .mp3 files


If you have any questions feel free to message me at vk.com/zrn01

