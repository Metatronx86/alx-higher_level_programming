0x14. JavaScript - Web scraping

Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/node
A README.md file, at the root of the folder of the project, is mandatory
Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
All your files must be executable
The length of your files will be tested using wc
You are not allowed to use var
More Info
Install Node 14
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
Install semi-standard
Documentation

$ sudo npm install semistandard --global
Install request module and use it
Documentation

$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
Notes: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

Tasks
0. Readme

# File Reader Script

This is a simple Node.js script that reads and prints the content of a file. It adheres to the provided guidelines and is designed to be easy to use.

## Prerequisites

Before you can use this script, you need to have Node.js installed on your system. You can download and install it from the official website: [Node.js](https://nodejs.org/)

## Installation

A. Clone this repository or download the `read_file.js` script.

B. Make the script executable:

## Usage

To use the script, run it from the command line with the following syntax:


Replace `<file_path>` with the path to the file you want to read.

### Example

```bash
./read_file.js /path/to/your/file.txt


1. Write me
mandatory
Write a script that writes a string to a file.

The first argument is the file path
The second argument is the string to write
The content of the file must be written in utf-8
If an error occurred during while writing, print the error object


# File Writer Script

This is a simple Node.js script that writes a string to a file. It allows you to specify the file path and the content to be written to the file via command-line arguments.

## Prerequisites

Before using this script, ensure you have Node.js installed on your system. You can download and install Node.js from the official website: [Node.js](https://nodejs.org/)

## Usage

To use the script, follow these steps:

A. Save the script to a file (e.g., `write_file.js`).

B. Make the script executable by running the following command in your terminal:
   ```bash
   chmod +x write_file.js



3. Star wars movie title
mandatory
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

The first argument is the movie ID
You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
You must use the module request
# Star Wars Movie Title Finder

This Node.js script allows you to find and print the title of a Star Wars movie based on the episode number you provide. It uses the 'request' module to make an HTTP request to the Star Wars API ('swapi-api.hbtn.io') to retrieve movie information.

## Prerequisites

Before using this script, ensure you have Node.js installed on your system. You can download and install Node.js from the official website: [Node.js](https://nodejs.org/)

## Usage

To use the script, follow these steps:

A. Save the script to a file (e.g., `star_wars_movie.js`).

B. Make the script executable by running the following command in your terminal:
   ```bash
   chmod +x star_wars_movie.js



4. Star wars Wedge Antilles
mandatory
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request


# Star Wars Movie Character Counter

This Node.js script counts the number of movies featuring the character Wedge Antilles in the Star Wars universe using data from the Star Wars API.

## Usage

A. Run the script with a URL to the Star Wars API as a command-line argument.

B. The script will fetch the data and display the count of movies with Wedge Antilles.

## Example

```bash
./script.js https://swapi-api.hbtn.io/api/people/

5. Write a script that gets the contents of a webpage and stores it in a file.

The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module request


# Webpage Content Downloader

## Description

This Node.js script allows you to download the contents of a webpage and save it to a file. It's a convenient tool for archiving web content for offline use or analysis.

## Usage

A. Make sure you have Node.js installed on your system.

B. Run the script with the following command:

   ```bash
   ./webpage-downloader.js [URL] [OutputFile]
6. How many completed?
mandatory
Write a script that computes the number of tasks completed by user id.

The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
You must use the module request

# Task Completion Counter

## Description

This Node.js script computes and displays the number of tasks completed by each user ID from a provided JSON data source. It's a handy tool for analyzing task completion statistics.

## Usage

A. Ensure you have Node.js installed on your system.

B. Run the script with the following command:

   ```bash
   ./task-completion-counter.js [JSONDataURL]

