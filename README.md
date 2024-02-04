Gif Data Organizer and Metadata Extractor from Pixabay
https://pixabay.com/
Objective
Develop a Python script or application to scrape Gifs and their metadata from Pixabay,
categorize them based on photo categories, store them in an organized file system, and create
a CSV file in each category folder containing detailed metadata of the Gifs. The project
will explore both serial and multithreaded programming approaches.
Project Description
Inputs
1. Website URL: The primary input will be the URL to Pixabay (https://pixabay.com/).
2. Category and Gif Data: Identify and utilize data about Gifs categories and their
related metadata present on the website.
Outputs
1. Folder Structure: Create a main directory with subdirectories for each Gifs category.
Each category's folder will store photographs and a CSV file.
2. Stored Photographs: Download and store Gifs in their respective category
folders.
3. CSV Files: Generate a CSV file in each category folder containing detailed information
for each photo, including the title, tags, Gif name, Gif URL, and other
relevant metadata.
4. Summary Report: A chart summarizing the number of Gifs downloaded per
category.
Phases
1. Phase 1: Serial Implementation
○ Implement web scraping, categorization, file storage, and CSV file generation
using a serial approach.
○ Document the performance in terms of execution time and resource utilization.
2. Phase 2: Multithreaded Implementation
○ Modify the script to perform the same tasks using multithreading.
○ Analyze and compare the performance with the serial approach.
