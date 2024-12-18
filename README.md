# renshuu dashboard

This project utilizes renshuu.org's API to get user's Japanese vocab, kanji, sentences, and grammar reviews for the given day. It also compiles studied terms from the Japanese Language Proficiency Test, or JLPT, to display overall Japanese progress on a visually pleasing graph. Soon, users will be able to access information about the program, settings to update the API key, and see all of their stats without touching the command line via converting the code into a single executable.

This project is currently a work in progress. Currently, I'm looking into what aspects of the GUI can be improved and what features can be added to make renshuu dashboard the best it can be.

## Program images

Upon starting up renshuu dashboard for the first time, the following view will be visible. By pressing the grey gear in the upper right corner, the settings window will open and prompt you for your api key.

![loadapikey](https://github.com/user-attachments/assets/f398919c-ee03-420a-a671-d08c63b561d6)

After entering your API key, a similar view to the following will appear. Your renshuu kaochan will populate on the frame to give the dashboard a personalized feel, today's terms will be counted on the frame, and you'll unlock the toggle feature in the lower right corner to view your progress graph.

<p align="center">
  <img src="https://github.com/user-attachments/assets/ba537e2e-68c9-4ff6-a0d5-c4e97266f8d8" width="45%" />
  <img src="https://github.com/user-attachments/assets/8a887fa5-32e9-4053-93a2-96e063e38a20" width="45%" /> 
</p>



## To Run

To run this program in its current state, first clone this repository. Create a renshuu account at https://www.renshuu.org/. Navigate to resources/tools/renshuuAPI and copy the read/write API key. Run the command python frame.py in the cloned directory. Click on the settings icon in the upper right corner, paste the API key and click update. Close the program and re-run the command python frame.py. Running this program via an executable will be implemented soon!
