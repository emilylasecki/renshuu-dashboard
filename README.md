# renshuu dashboard

This project utilizes renshuu.org's API to get user's Japanese vocab, kanji, sentences, and grammar reviews for the given day. It also compiles studied terms from the Japanese Language Proficiency Test, or JLPT, to display overall Japanese progress on a visually pleasing graph. 

This project is a work in progress. Currently, I'm looking into what aspects of the GUI can be improved and what features can be added to make renshuu dashboard the best it can be.

## Project features

- Designed to resemble renshuu.org 
- GUI to display daily goals and overall JLPT Progress
- Button to toggle between two views
- Easily configure and update API key through settings button
- Refresh button to instantly update the count of reviews, new terms, and completed terms
- Information button to instruct users of how to make the most of renshuu dashboard
- Features Renshuu.org Kaochan for a personalized touch
- Quick links to access the GitHub page and renshuu.org

Soon!
- Single executable file to package dependencies so program can run without needing to touch the command line


## Program images

Upon starting up renshuu dashboard for the first time, the following view will be visible. By pressing the grey gear in the upper right corner, the settings window will open and prompt you for your api key.

![loadapikey](https://github.com/user-attachments/assets/f398919c-ee03-420a-a671-d08c63b561d6)


After entering your API key and re-running the program, a similar view to the following will appear. Your renshuu Kaochan will populate on the frame, today's terms will be counted on the frame, and you'll unlock the toggle feature in the lower right corner to view your progress graph.


<p align="center">
  <img src="https://github.com/user-attachments/assets/ba537e2e-68c9-4ff6-a0d5-c4e97266f8d8" width="45%" />
  <img src="https://github.com/user-attachments/assets/8a887fa5-32e9-4053-93a2-96e063e38a20" width="45%" /> 
</p>



## To Run

To run this program in its current state, first clone this repository. Create a renshuu account at https://www.renshuu.org/. Navigate to resources/tools/renshuuAPI and copy the read/write API key. Run the command python frame.py in the cloned directory. Click on the settings icon in the upper right corner, paste the API key and click update. Close the program and re-run the command python frame.py. Running this program via an executable will be implemented soon!
