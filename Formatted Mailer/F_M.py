import Mail as M
import Preformat as pf
import user

class Mail_setup:
    def __init__(self,html_file_content, replacement):
        self.html_data = html_file_content
        self.html_data_re = replacement

        self.mail = M.Mailer()
        self.mail.set_subject(self.setting_subject(True))
        self.mail.set_body_html(self.setting_body_html(True),self.html_data, self.html_data_re)
        self.mail.add_recipient(self.add_recipient(True))
        

    def setting_subject(self, auto = False):
        default_text = "This is test mail sending using python"
        if auto == True:
            subject = input("enter mail subject : ")
            return subject
        self.mail.set_subject(default_text)
    
    def setting_body_html(self, auto = False):
        default_text = 'This is a test mail, please do not reply to it!'
        if auto == True:
            text = input("enter mail body text : ")
            return default_text+ " " + text
        self.mail.set_body_html(default_text, self.html_data, self.html_data_re)


    def add_recipient(self, auto = False):
        if auto == True:
            recipient_mail = input("enter recipient's mail to add : ")
            return recipient_mail
        
        recipient_mail = input("enter recipient's mail to add : ")
        self.mail.add_recipient(recipient_mail)

    def final_send(self):
        if self.mail.set_from_to():
            self.mail.send_mail()
        else:
            print("problem in sending")



def login():
    all_roles = ["admin","view"]
    u_name = input("Enter username : ")
    u_role = input("Enter your role (admin) or (view) : ")

    while not u_role in all_roles:
        u_role = input("Enter your role from this only (admin) or (view) : ")
    
    m_user = user.Userhandler()
    if m_user.add_user(u_name, u_role):
        print(f"{u_name}, you are in system")


def main():
    login()

if __name__ == "__main__":
    # main()
    html_fmat, html_replacement= pf.main()
    m = Mail_setup(html_fmat, html_replacement)
    m.final_send()


    

    