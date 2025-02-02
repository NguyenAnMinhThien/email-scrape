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
    msgs = get_emails(search('FROM', "upwork.com", con))

    # Uncomment this to see what actually comes as data
    # print(msgs)


    # Finding the required content from our msgs
    # User can make custom changes in this part to
    # fetch the required content he / she needs

    # printing them by the order they are displayed in your gmail
    for msg in msgs[::-1]:
        for sent in msg:
            if type(sent) is tuple:

                # encoding set as utf-8, our data is nested inside multiple layer.
                data = str(sent[1], 'utf-8')
                # for str_line in data:
                #     if "via Upwork" in str_line:
                #         print(str_line)
                #         break


                # Handling errors related to unicodenecode
                try:
                    indexstart = data.find("ltr")
                    data2 = data[indexstart + 5: len(data)]
                    indexend = data2.find("</div>")

                    # printing the required content which we need
                    # to extract from our email i.e our body
                    if "you have unread messages" in data2[0:indexend].lower():
                        print(data2[0: indexend])
                    # if "via upwork" in data2[0:indexend].lower():
                        subprocess.run("python phone_calls.py", shell = True)
                        # play_sound.play_sound("note.mp3")

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

# this is done to make SSL connection with GMAIL
while(1):
    try:
        con = imaplib.IMAP4_SSL(imap_url)
        # logging the user in
        con.login(user, password)
        # calling function to check for email under this label
        con.select('Inbox')
        loop_find_mail(con)
        time.sleep(60)
    # msgs = get_emails(search('FROM', 'hello@info.crunchyroll.com', con))
    except imaplib.IMAP4.abort as e:
        print("Re-initialize IMAP connection")
        continue
    finally:
        con.logout()

#     when send the code to virtual server, just use 60 seconds, not only 10 seconds, it will cause the script can not excute in continue - !
