# renshuu dashboard

This project utilizes renshuu.org's API to get user's Japanese vocab, kanji, sentences, and grammar reviews for the given day. It also compiles studied terms from the Japanese Language Proficiency Test, or JLPT, to display overall Japanese progress on a visually pleasing graph. The program is bundled into an executable file and can also be run from the command line, so developers and non-developers alike can both make use of renshuu dashboard!

## Project features

- Designed to resemble renshuu.org 
- GUI to display daily goals and overall JLPT Progress
- Button to toggle between two views
- Easily configure and update API key through settings button
- Refresh button to instantly update the count of reviews, new terms, and completed terms
- Additional information button to instruct users of how to make the most of renshuu dashboard
- Features Renshuu.org Kaochan for a personalized touch
- Quick links to access the GitHub page and renshuu.org
- Bundled into a single executable file so program can run without touching the command line


## Project images

Upon starting up renshuu dashboard for the first time, the following view will be visible. By pressing the grey gear in the upper right corner, the settings window will open and prompt you for your API key.

![loadapikey](https://github.com/user-attachments/assets/f398919c-ee03-420a-a671-d08c63b561d6)


After entering your API key, a .txt file will be generated in the directory for your user that renshuu dashboard can update and store. Re-running the program will read from this file and allow a similar view to the following to appear. From the API call, your renshuu Kaochan will populate on the frame, today's terms will be counted on the frame, and you'll unlock the toggle feature in the lower right corner to view your progress graph.


<p align="center">
  <img src="https://github.com/user-attachments/assets/ba537e2e-68c9-4ff6-a0d5-c4e97266f8d8" width="45%" />
  <img src="https://github.com/user-attachments/assets/8a887fa5-32e9-4053-93a2-96e063e38a20" width="45%" /> 
</p>



## To Run

### To run from the executable file:
Download RenshuuDashboard.exe. Create an account at https://www.renshuu.org/, navigate to resources/tools/renshuuAPI and copy the read only API key. Bootup RenshuuDashboard.exe and click on the grey gear in the top right corner. Paste your API key in the box and press update. Close and restart the program to see your daily goals and overall Japanese learning progress!

### To run from the command line:
Clone this repository and install all dependencies. Create a renshuu account as described above. Run the command python frame.py in the cloned directory. Click on the settings icon in the upper right corner, paste the API key and click update. Close the program and re-run the command python frame.py to get your stats.

### To re-create the executable file:
Make sure pyinstaller is installed and while in the current directory run the following command for windows (for Mac OS replace the semicolons with colons): 

pyinstaller --onefile --noconsole --add-data "myKao.png;." --add-data "ButtonReload.png;." --add-data "questionMarkButton.png;." --add-data "settings.png;." --icon frame.ico frame.py

Your executable file will populate in a sub-directory of your working directory called "dist".
