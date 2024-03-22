
formats_data = {
    "Promotional":{"email":".com","company name":"empty"}
    ,"Product Launch":{"email":".com"}
    ,"Newsletter":{"email":".com"}
    ,"Welcome":{"email":".com"}
    ,"Abandoned Cart":{"email":".com"}
    ,"Event Invitations":{"email":".com"}
    ,"Survey and Feedback":{"email":".com"}
    ,"Transactional":{"email":".com"}
    ,"Announcement":{"email":".com"}
    ,"Educational":{"email":".com"}
    ,"Birthday":{"email":".com","first-name":"name", "last-name":"cast","birthdate":"dd-mm-yyyy","age":0}
    ,"Re-engagement":{"email":".com"}
    ,"Cross-Sell and Up-Sell":{"email":".com"}
    ,"Holiday or Seasonal":{"email":".com"}
}

formats = list(formats_data.keys())

def get_format(format_name):
    try:
        with open(f"Templates\{format_name}.html") as f:
            return f.read()
    except Exception as e:
        print(e)

def show_format():
    i =1
    for k in formats:
        print(f"{i}) {k}")
        i += 1

    print()
    format_selected = int(input("Please chosse a predefine format: ")) - 1
    while not (format_selected >= 0 and format_selected < len(formats)):
        print("You entered a non found number!")
        format_selected = int(input("Please chosse a predefine format: ")) - 1
    fmat = formats[format_selected]
    return fmat, formats_data[fmat] 

def main():
    return show_format()

def copy_html():
    f1 = open(f"Templates\sample.html")
    t = f1.read()
    # print(t)

    for i in formats:
        with open(f"Templates\{i}.html","w") as f3:
            # print("Promotional to ",i)
            e = t.replace("New Product Launch",i)
            f3.write(e)

    f1.close()

if __name__ == "__main__":
    main()
    # copy_html()
    
    