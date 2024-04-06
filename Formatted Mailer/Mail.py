import Preformat as pf

# import sever 
import smtplib

# to get login details from .env
from decouple import config

from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart

# text for that box
from email.mime.text import MIMEText

# to attach image in the box
from email.mime.image import MIMEImage

# to attach pdf in the box
from email.mime.application import MIMEApplication


class Sever:
    def __init__(self) -> None:
        self._sending_mail = config('SENDING_MAIL')
        self.__password = config('PASSWORD')

        print()
        print("*"*26)
        print("Connecting to smtp server!")

        self.ob = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        try:
            self.ob.login(self._sending_mail, self.__password)
            print("login done!")
            print("*"*26)
            print()

        except smtplib.SMTPAuthenticationError as e:
            print(f"Authentication failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


class Mailer(Sever):
    def __init__(self,loged_user):
        super().__init__()
        self.recipients_list = []
        self.from_to = False
        self.msg = MIMEMultipart()
        # self.msg = EmailMessage()

        self.loged_user = loged_user

    def set_subject(self, subject: str):
        self.msg['Subject'] = subject
        print("subject set :", subject)

    def set_from_to(self) -> bool:
        """
        this method must call after adding recipient
        """
        if self.recipients_list:
            self.from_to = True
            self.msg['From'] = self._sending_mail
            self.msg['To'] = ', '.join(self.recipients_list)
            print("mail sending from", self._sending_mail,"\n")
        else:
            print("Please add recipients!")

        return bool(self.recipients_list)

    def set_body_html(self, text: str, body_structure=None, re=None):
        # Attach text content
        self.msg.attach(MIMEText(text, 'plain'))

        if body_structure:
            if re:
                try:
                    print()
                    for k, v in re.items():
                        re[k] = input(f"enter value for {k}: ")
                        body_structure = body_structure.replace("{" + k + "}", str(re[k]))
                except Exception as e:
                    print(e, "error")
            else:
                print("format not given!")
            

            # Add the HTML body structure
            html_part = MIMEText(body_structure, _subtype='html')
            self.msg.attach(html_part)

            print()
        else:
            print("this mail not have HTML structure!")

    def attach_image(self, list_of_img):
        # Attach Image file
        for image_path in list_of_img:
            with open(image_path, 'rb') as image_file:
                try:
                    image_attachment = MIMEImage(image_file.read(), name=image_file.name)
                    self.msg.attach(image_attachment)

                    status = image_file.name + " attached..."
                    print(status)
                    Logs().log(status+"\n")


                except Exception as e:
                    print(image_file.name, "->", e)

    def attach_pdf(self, list_of_pdf):
        # Attach PDF file
        for pdf_path in list_of_pdf:
            with open(pdf_path, 'rb') as pdf_file:
                pdf_attachment = MIMEApplication(pdf_file.read(), name=pdf_file.name, _subtype="pdf")
                pdf_attachment.add_header('Content-Disposition', 'attachment', filename=pdf_file.name)
                self.msg.attach(pdf_attachment)

                status = pdf_file.name+ " attached..."
                print(status)
                Logs().log(status+"\n")

    def clear_recipient_list(self):
        print("\nrecipients_list is empty now.")
        self.recipients_list.clear()

    def set_recipients(self, reci_list: list):
        self.recipients_list = list(set(reci_list))
        print("recipients are added")

    def add_recipient(self, recipient):
        if not recipient in self.recipients_list:
            self.recipients_list.append(recipient)
            print(recipient, ": recipient is added")
        else:
            print(recipient, ": already added")

    def send_mail(self):
        if self.loged_user == "admin":
            if self.from_to:
                if (input("Enter (send) to confirm the sending process: ")).lower() == "send":
                    respond = self.ob.sendmail(self._sending_mail, self.recipients_list, self.msg.as_string())
                    # print('send mail', respond)
                    print('send mail')
                    Logs().finish_log()
                # pass
                else:
                    print("the process is canceled")
            else:
                print("please set From and To\nset using set_from_to() method")
        else:
            print("Only the admin have the access to send mails")


class Logs:

    def log(self, msg):
        with open("logs.txt", 'a') as f:
            f.write(msg)

    def finish_log(self):
        with open("logs.txt", 'a') as f:
            f.write('\n\n')


if __name__ == "__main__":
    m = Mailer("admin")
    
    m.attach_image(["img\holiday location2.jpeg"])
    m.attach_pdf(["pdf\SEM III_FCSP-1_CE_Syllabus.pdf"])

    html_fmat, html_replacement = pf.main()

    Logs().log("format selected : "+html_fmat+"\n")

    file = lambda: open(f"Templates\\{html_fmat}.html").read()
    

    m.set_subject("This is test mail sending using python")
    m.set_body_html('This is a test mail, please do not reply to it!', file(), html_replacement)
    m.add_recipient("gta5andepic@gmail.com")
    # m.add_recipient('jaldeepsinhgohil2003@gmail.com')
    # m.add_recipient('mendhaforam2010@gmail.com')
    # m.add_recipient('edcftygh@gmail.com')
    m.set_from_to()
    m.send_mail()
