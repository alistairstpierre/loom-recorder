
# Cold Email For Wizards

Press play and walk away 'loom style' video recorder.

Record as many 'loom style' videos as you like. You will need:

    1. An audio recording.
    2. Your 'loom style' profile picture.
    3. A list of websites and business owners names
     (Or any unique name that you'd like to associate to the video.)


## Downloads & Installs

Download and install Python version 3.1.1 [here](https://www.python.org/downloads/release/python-3110/) no other version will work.

Download and install OBS [here](https://obsproject.com/) this will be used to record the videos.

Download and install Visual Studio Code [here](https://visualstudio.microsoft.com/) this will be used to run the code.

Download the zip file of code above. (Or use GIT if you are also a wizard.)

Download and install Firefox [here](https://www.mozilla.org/en-US/firefox/)



## CSV File Setup
    1. Create a spreadsheet with at least two columns. These columns must be called 'Website' and 'Full Name' exactly, the capital letters matter.
    2. Add your websites to the 'Website' column and associated names to the 'Full Name' column.
    3. Export this data as a csv file.
## OBS Setup
    1. Open OBS
    2. Go to the menu, click 'Tools' then 'Scripts' which will open this window.
    
![App Screenshot](https://i.imgur.com/nroyEss.png)
    
    3. Paste in or browse to /Library/Frameworks/
    4. Your Scripts window should now say "Loaded Python Version 3.11 if it doesn't I'm sorry but your journey ends here.
    5. Close out of scripts and go back to the menu, click 'Tools' then 'WebSocket Server Settings'
    6. Tick 'Enable Websocket Server' and then click Apply.
    7. Add your circular profile image to OBS in the bottom left corner to look like loom.

## Windows Studio Code Setup
    1. Open Windows Studio Code
    2. Click the Extensions Button

![Screenshot](https://i.imgur.com/S9d4wYr.png)

    3. Type in 'Python' in the searchbar and install the extension names 'Python' by Microsoft
    4. Unzip the zip file of the project you downloaded from Github.
    5. Go to the menu and click 'File' then 'Open Folder'
    6. Open the folder you just unzipped.
    7. Create two new folders called 'data' and 'output' within the project.
    7. Drag your audio file into the 'data' folder and rename the file 'audio' exactly.
    8. Drag your csv file into the 'data' folder and rename it 'data' exactly. Your project should look like the image below.
    9. In Visual Studio Code click on the 'main.py' file.

![Screenshot](https://i.imgur.com/CFkVq44.png)

    10. Scroll to where it says 'url=' and 'password='
    11. Go back to OBS and go to the menu, click 'Tools' then 'Websocket Server Settings'
    12. Click 'Show Connect Info' and use the information you see for the next steps.

![Screenshot](https://i.imgur.com/6pechLr.png)

    13. Update the url code so it looks like the following: url = 'ws://(Server IP):(Server Port)' as an example it should look something lke this: url = 'ws://198.162.1.26:4455'
    14. Update the password code so it looks like the following: password = '(Server Password)'

## Set The OBS Output To Your Output Folder And Change The Settings
    1. Open OBS
    2. Click Settings on the "Controls" panel, bottom right of the interface.
    3. Click Output
    4. Go to the recording section and change the recording path to the output folder we created in Visual Studio.
    5. Change the Recording Quality to "High Quality, Medium File Size"
    6. Change the Recording Format to "MPEG-4(.mp4)"

![Screenshot](https://i.imgur.com/rKu978Z.png)
    
## Run The Code
    1. Go to the menu and click 'Terminal' then 'New Terminal'
    2. Type 'pip install -r requirements.txt'
    2. In the terminal type 'python main.py'
