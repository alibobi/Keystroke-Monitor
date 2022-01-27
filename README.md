# Keystroke-Monitor
Simple keystroke monitor with emailing logs functionality

# Description
This project acts as background process that "parses" the keys that a user is pressing into words. Inputs are split into words when the user clicks or uses the enter/space key. It also takes into account the use of the backspace key and will adjust words properly. The words are then written into the log file along with the time that it was written next to it. After 50 words have been written the log file will be emailed to 'keylogproject38@gmail.com' and then cleared. This script can be stopped through the use of the escape key or if it is killed.

# Development
The process taken to develop this keystroke monitor was researching libraries that have the capability of handling key and mouse input. This led to the pynput library. Researching this library led to the creating a keyboard listener that would print the keys that were pressed. Then the log file writing was implemented which initially only wrote the letters with the time it was pressed. I then implemented the parsing which consisted of me creating an array that keeps track of the characters that are pressed. Once the enter/space key was pressed, it would write the char array into the log file. In order to create a more realistic parsing, a mouse listener was implemented. This allowed for the char array to be written into the log file when the mouse was clicked. Afterwards, to allow for remote access to the log file an email functionality was implemented using the smtplib and email libraries. For future development, I would like to make this undetectable to antivirus software to further my understanding of malware.

