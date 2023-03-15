#to setup the python environment
#first ensure python is installed run this python3 --version

#next - get the virtual environment running
#python3 -m venv .venv
#source .venv/bin/activate

#this next module is text to conversion speach library
#python3 -m pip install pyttsx3 
#sudo apt-get install espeak

#this next module performs major pdf tasks 
#python3 -m pip install PyPDF2

#this next piece is required to generate the mp3 file
#sudo apt-get update
#sudo apt-get install ffmpeg

import pyttsx3,PyPDF2

#insert name of your pdf 
pdfreader = PyPDF2.PdfReader(open('wellarchitected-framework.pdf', 'rb'))
#pyttsx3.init(driverName='espeak', executable='/usr/bin/ffmpeg')
speaker = pyttsx3.init()

#for page_num in range(len(pdfreader.pages)):

# Set the range from 12-19 (0-based index)
for page_num in range(11, 19):   
    page = pdfreader.pages[page_num]
    text = page.extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

#set speaker properties
    speaker.setProperty('voice', 'english')
    speaker.setProperty('rate', 100)
    speaker.setProperty('volume', 0.7)
    speaker.setProperty('fpath', '/usr/bin/ffmpeg')
    #speaker.save_to_file(clean_text, 'aws-waf.mp3')


# Name MP3 file whatever you would like
    speaker.save_to_file(clean_text, f'aws-waf-page{page_num+1}.mp3')
    speaker.runAndWait()

speaker.stop()
