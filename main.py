# Importing libraries
import imaplib, email
import time
import subprocess
import dotenv
import os

dotenv.load_dotenv()
user = os.getenv("user_imap")
password = os.getenv("password")
imap_url = 'imap.gmail.com'

def loop_find_mail(con):
    # msgs = get_emails(search('FROM', "upwork.com", con)) #heree
    msgs = get_emails(search('FROM', "nguyenanminhthien@gmail.com", con))
    # msgs = get_emails(search('FROM', "namthien0503@gmail.com", con))
    for msg in msgs[::-1]:
        for sent in msg:
            if type(sent) is tuple:
                # encoding set as utf-8, our data is nested inside multiple layer.
                data = str(sent[1], 'utf-8')
                try:
                    indexstart = data.find("ltr")
                    data2 = data[indexstart + 5: len(data)]
                    indexend = data2.find("</div>")
                    # if "you have unread messages" in data2[0:indexend].lower():
                    #     print(data2[0: indexend])
                    #     subprocess.run("python phone_calls.py", shell = True)
                    #     # play_sound.play_sound("note.mp3")
                    #     return

                    print("\nemail_heree\n")
                    print(data2[0: indexend])

                # pass the unicode Encode error
                except UnicodeEncodeError as e:
                    pass
# Function to get email content part i.e its body part
# def get_body(msg):
#     if msg.is_multipart():
#         return get_body(msg.get_payload(0))
#     else:
#         return msg.get_payload(None, True)

# Function to search for a key value pair
def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

# Function to get the list of emails under this label
def get_emails(result_bytes):
    msgs = [] # all the email data are pushed inside an array
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

if __name__ == '__main__':
    # this is done to make SSL connection with GMAIL
    con = imaplib.IMAP4_SSL(imap_url)
    while(1):
        try:
            con.login(user, password)
            con.select('Inbox')
            loop_find_mail(con)
            time.sleep(20)
        # except imaplib.IMAP4.abort as e:
        except Exception as e:
            print("Re-initializing IMAP connection dueto :",e,"\n")
            con.logout()
            con = imaplib.IMAP4_SSL(imap_url)
            pass

    #     when send the code to virtual server, just use 60 seconds, not only 10 seconds, it will cause the script can not excute in continue - !
