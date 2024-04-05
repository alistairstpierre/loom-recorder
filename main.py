from selenium import webdriver
import time
import logging
logging.basicConfig(level=logging.DEBUG)
import asyncio
import simpleobsws
from simpleobsws import Request
import csv
import os
import pygame
import math
import numpy
from datetime import datetime

# A tuple of video file extensions to look for
file_names = []
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.mp3')
start = 0  # Start of the range (in radians)
end = 2 * math.pi  # End of the range (in radians)
num_points = 1000  # How many points to generate
# Generate x values
x_values = numpy.linspace(start, end, num_points)

# Generate sine values
sin_values = numpy.sin(x_values)
# Get the current date and time
now = datetime.now()
# Format the date as "DD/MM"
date_string = now.strftime("%d/%m")

def remove_newlines(input_string):
    # Replace all occurrences of \n in the string with nothing (i.e., remove them)
    output_string = input_string.replace("\n", "")
    return output_string

async def read_data():
    with open('data.csv', newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader object
        csvreader = csv.DictReader(csvfile)

        # Loop through the rows in the CSV file
        for row in csvreader:
            # Print the website from the "Website" column
            website = row['Website']
            file_name = remove_newlines(row['Full Name']) + ".mp4"
            await main(website, file_name)

async def main(website, file_name):
    browser = webdriver.Firefox()

    url = 'ws://192.168.1.38:4455'
    password = 'pSxSBIABtXtZoBdX'

    parameters = simpleobsws.IdentificationParameters()

    ws = simpleobsws.WebSocketClient(url=url, password=password, identification_parameters=parameters)

    try:
        browser.get(website)

        await ws.connect()
        await ws.wait_until_identified()

        request = Request('StartRecord')
        response = await ws.call(request)

        if response.ok():
            print("Request succeeded! Response data:", response.responseData)
        else:
            print("Request failed. Response data:", response.responseData)

        sound.play() 

        time.sleep(1)
        for x, sin_val in zip(x_values, sin_values):
            print(sin_val)
            browser.execute_script("window.scrollTo(0, {});".format(sin_val*1000))

        # Keep the program running until the sound plays completely
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)

        request = Request('StopRecord')
        response = await ws.call(request)

        if response.ok():
            print("Request succeeded! Response data:", response.responseData)
        else:
            print("Request failed. Response data:", response.responseData)

    except Exception as e:
        print("Error:", str(e))
    finally:
        await ws.disconnect()
        browser.quit()
        rename_last_modified_file('output', file_name)

def rename_last_modified_file(folder_path, new_name):
    # Get the list of files in the folder
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]
    # Filter out directories, leaving only files
    files = [f for f in files if os.path.isfile(f)]
    # Find the most recently modified file
    last_modified_file = max(files, key=os.path.getmtime, default=None)
    if last_modified_file:
        # Create the full path for the new name
        new_file_path = os.path.join(folder_path, new_name)
        # Rename the file
        os.rename(last_modified_file, new_file_path)
        print(f"Renamed '{last_modified_file}' to '{new_file_path}'")
    else:
        print("No files found in the folder.")

asyncio.run(read_data())










