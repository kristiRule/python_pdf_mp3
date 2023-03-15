# PDF to MP3 Converter
This Python program converts the text from a PDF file to an MP3 audio file. 

The program uses the PyPDF2 library to extract text from the PDF file, and the pyttsx3 library to convert the text to speech and save it as an MP3 file. The ffmpeg library is also required for generating the MP3 file.

## Setup
* Ensure that Python is installed. You can check by running python3 --version.
* Create a virtual environment by running python3 -m venv .venv and activate it with source .venv/bin/activate.
* Install the required libraries by running python3 -m pip install pyttsx3 PyPDF2 and sudo apt-get install espeak ffmpeg.
* Replace the filename wellarchitected-framework.pdf in the code with the name of your PDF file.

## Usage
* Run the program with python3 main.py.
* The program will extract the text from the PDF file and convert it to speech.
* The output will be saved as an MP3 file in the current directory, with each page saved as a separate file.

## Notes
* You can adjust the page range to be converted by modifying the line for page_num in range(11, 19):. In this example, pages 12-19 are converted.
* You can adjust the voice, rate, volume, and output file name by modifying the relevant lines in the code.
* If you encounter any errors, try running the program in debug mode by adding import pdb; pdb.set_trace() to the code, and running python3 -m pdb main.py.

## Test Case Setup
To test the program, you can use the sample PDF file included in the repository (wellarchitected-framework.pdf). Simply follow the setup and usage instructions above, and the program should extract the text from the PDF file and save it as an MP3 file in the current directory.

## Credits
This program was largely inspired by TiffInTech and has been adapted to python modules and functions available in 2023.
