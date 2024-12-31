# scraper
This is a Python program designed to (scrape) extract and download images from Google Search Images with the Google API Key.
Steps and key points to keep in mind-
1. Download ChromeDriver for your version of Chrome in the folder where this Python Code will be kept.
   1.a. You will find your version of the driver on - https://developer.chrome.com/docs/chromedriver/downloads   
 or    https://googlechromelabs.github.io/chrome-for-testing/.
   1.b. To find which version of Chrome you are using -
https://www.whatsmyua.info/      (It will come like this - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/(version) Safari/537.36)
2. Relocate the executable file to a place in your PC whose location you know. Copy it's location.
   like- D:\Earn\chromedriver.exe
3. Paste the code in new file in IDLE, then edit in line 10 path of chromedriver with that in line2 of ReadME
4. Open Command Prompt (cmd) and execute - pip install selenium
   pip install beautifulsoup4
   pip install requests
   pip install Pillow
   (one by one)
5. Edit the number of images you want and the query in last line of the python program -
   scrape_images("query", max_images=500)

The program will run after you save it in the same desetination as the chromedriver and you will need to wait 20 seconds if the "No 'Show more images' button found" is displayed, to see if any further images are being downloaded. It should be safe to use as it uses some techniques like random delays etc., but agains use at your own risk.
Does't have virus and safe to use.
Thanks.
