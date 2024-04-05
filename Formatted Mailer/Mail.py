import Preformat as pf


# import sever 
import smtplib

#to get login details from .env
from decouple import config

# text for that box
from email.mime.text import MIMEText

# to attach image in the box
from email.mime.image import MIMEImage

from email.message import EmailMessage

# to attach pdf in the box
from email.mime.application import MIMEApplication

class Sever:
    def __init__(self) -> None:
        self._sending_mail = config('SENDING_MAIL')
        self.__password = config('PASSWORD')

        self.ob = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        try:
            self.ob.login(self._sending_mail, self.__password)
            print("login done!")

        except smtplib.SMTPAuthenticationError as e:
            print(f"Authentication failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        

class Mailer(Sever):
    def __init__(self):
        super().__init__()
        self.recipients_list = []
        self.from_to = False
        # self.msg = MIMEMultipart()
        self.msg = EmailMessage()

    def set_subject(self,subject:str):
        self.msg['Subject'] = subject
        print("subject set :",subject)

    def set_from_to(self) -> bool:
        """
        this method must call after adding recipient
        """
        if self.recipients_list:
            self.from_to = True
            self.msg['From'] = self._sending_mail
            self.msg['To'] = ', '.join(self.recipients_list)
            print("mail sending from",self._sending_mail)
        else:
            print("Please add recipients!")
        
        return bool(self.recipients_list)

    def set_body_html(self,text:str,body_structure=None,re=None):
         # Attach text content
        self.msg.attach(MIMEText(text, 'plain'))

        if body_structure:
            if re:
                try:
                    for k,v in re.items():
                        body_structure.replace("{"+k+"}", str(v))
                        print("{"+k+"}", str(v))
                except Exception as e:
                    print(e,"error")
            else:
                print("format not given!")

            # Add the HTML body structure
            self.msg.set_content(body_structure, subtype='html')
        else:
            print("this mail not have HTML structure!")
    
    def attach_image(self,list_of_img):
        # Attach Image file
        for image_path in list_of_img:
            with open(image_path, 'rb') as image_file:
                try:
                    image_attachment = MIMEImage(image_file.read(), name = image_file.name)
                    self.msg.attach(image_attachment)
                    print(image_file.name,"attached...")
                except Exception as e:
                    print(image_file.name,"->",e)
    
    def attach_pdf(self,list_of_pdf):
        # Attach PDF file
        for pdf_path in list_of_pdf:
            with open(pdf_path, 'rb') as pdf_file:
                pdf_attachment = MIMEApplication(pdf_file.read(), name=pdf_file.name)
                self.msg.attach(pdf_attachment)
                print(pdf_file.name," attached...")

    def set_recipients(self,reci_list:list):
        self.recipients_list = reci_list
        print("recipients are added")

    def add_recipient(self,recipient):
        self.recipients_list.append(recipient)
        print(recipient , ": recipient is added")
    
    def send_mail(self):
        if self.from_to:
            # respond = self.ob.sendmail(self._sending_mail, self.recipients_list, self.msg.as_string())
            # print('send mail', respond)
            pass
        else:
            print("please set From and To\nset using set_from_to() method")


class Logs:

    def log(self, msg):
        with open("logs.txt",'a') as f:
            f.write(msg)

    def finish_log(self):
        with open("logs.txt",'a') as f:
            f.write('\n')


if __name__ == "__main__":
    m = Mailer()

    html_fmat, html_replacement= pf.main()
    print(html_replacement)

    file = lambda : open(f"Templates\{html_fmat}.html").read()

    m.set_subject("This is test mail sending using python")
    m.set_body_html('This is a test mail, please do not reply to it!', file(), html_replacement)
    # m.add_recipient()
    # m.add_recipient('jaldeepsinhgohil2003@gmail.com')
    # m.add_recipient('mendhaforam2010@gmail.com')
    # m.add_recipient('edcftygh@gmail.com')
    m.set_from_to()
    m.send_mail()
    