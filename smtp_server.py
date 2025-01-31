# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import yagmail

receiver = "nguyenanminhthien97+hehe@gmail.com"
body = "Hello there from Yagmail"
filename = "hihi.csv"

yag = yagmail.SMTP("nguyenanminhthien97@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body,
    attachments=filename,
)