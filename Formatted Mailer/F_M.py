import Mail as M
import Preformat as pf
import user, os

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
            text = input("enter text for mail body: ")
            return default_text+ "\n" + text
        self.mail.set_body_html(default_text, self.html_data, self.html_data_re)


    def add_recipient(self, auto = False):
        if auto == True:
            recipient_mail = input("enter recipient's mail to add : ")
            return recipient_mail
        
        recipient_mail = input("enter recipient's mail to add : ")
        self.mail.add_recipient(recipient_mail)
    
    def add_recipients(self,r_l):
        for email in r_l:
            self.mail.add_recipient(email)
        
        print("all email are set in recipient list")

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
    user_obj = m_user.add_user(u_name, u_role)
    if user_obj:
        print(f"{u_name}, you are in system")

        while True:
            print("""
                1) start mailing process
                2) Change pass Key
                0) Log out
                """)
            option = int(input("enter option number: "))

            # if (option >= 0 and option <= 1 ):
            if option == 1:
                return True
            elif option == 2:
                user_obj.change_pKey()
            elif option == 0:
                return False

    else:
        print("You must have to login to start process!")


    

if __name__ == "__main__":
    while True:
        if login():
            html_fmat, html_replacement= pf.main()
            m = Mail_setup(html_fmat, html_replacement)

            while 1:
                print('''
                    1) add recipient
                    2) add recipient list
                    3) attach image
                    4) attach pdf
                    5) send mail
                    0) cancel process
                    ''')
                option = int(input("enter option number: "))
                if option == 0:
                    break

                if option == 1 :
                    m.add_recipient()
                elif option == 2:

                    reci_list = user.reci
                    email_list_type = reci_list.keys()

                    pf.display(email_list_type)

                    mail_option = int(input("enter mail option number: "))
                    if (mail_option>=1 and mail_option<=len(email_list_type)):
                        m.add_recipients(reci_list[email_list_type[option - 1]])
                    else:
                        print("option number not found!")
                elif option == 3:

                    print()
                    for img in os.listdir("img"):
                        print(img)
                    print()

                    img_name = ["img/"+input("enter image file name: ")]
                    m.mail.attach_image(img_name)

                elif option == 4:

                    print()
                    for pdf in os.listdir("pdf"):
                        print(pdf)
                    print()

                    pdf_name = ["img/"+input("enter pdf file name: ")]
                    m.mail.attach_pdf(pdf_name)

                elif option == 5:
                    m.final_send()
                else:
                    print("option number not found!")
            
            break
        else:
            print("You have loged out! \n")

            yes_no = input("Do you want to login again (yes) or (no)")

            if yes_no != "yes":
                break

    print("Thank you...")




    

    