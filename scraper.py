import smtplib, smtpd
import codecs
import requests
import bs4
originalF = open("MLHs2016.dat","r")
originalE = originalF.read().split('\n')
originalF.close()
out = open("MLHs2016.dat","w+")
addition = []
def main():
    page = requests.get('http://mlh.io/seasons/s2016/events')
    soup = bs4.BeautifulSoup(page.text,'lxml')
    #print(data)
    mydivs = soup.findAll("div", { "class" : "event-wrapper" })
    
    events = []
    for i in mydivs:
        events.append(str(i.h3)[4:-5])
    for i in events:
        if i not in originalE:
            addition.append(i)
    for j in addition:
        USERNAME = '699deffaf305f568a69dc5c794debe11'
        PASSWORD = '7fe3167570809e035104d56a3aadea31'
        SENDER = 'diana.chang.twn@gmail.com'
        receiver = 'diana.chang.twn@gmail.com'
        message = "\r\n".join([
        "From: %s" % SENDER,
        "To: %s" % receiver,
        "Subject: ALERT: New Hackathon added to MLH Spring 2016 Season",
        "", j  ])
        try:
          server = smtplib.SMTP('in-v3.mailjet.com:587')
          server.starttls()
          server.login(USERNAME,PASSWORD)
          server.sendmail(SENDER, receiver, message)
          server.quit()
          print ("Successfully sent email to %s", receiver)
        except smtplib.SMTPException:
          print ("Error: unable to send email to %s", receiver)
        
    for i in events:
        out.write(i+"\n")
    out.close()
main()
