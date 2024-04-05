formats_data = {
    "Product Launch": {"product name": "toy"}
    , "Welcome": {"company name": None}
    , "Event Invitations": {"Event type": "birthdat party"}
    , "Announcement": {"institude name": None, "message": None}
    , "Holiday": {"location": "location"}
}


def get_format(format_name):
    try:
        with open(f"Templates\{format_name}.html") as f:
            return f.read()
    except Exception as e:
        print(e)


def display(data_):
    i = 1
    for k in data_:
        print(f"{i}) {k}")
        i += 1
    print()


def show_format(formats):
    display(formats)

    print("Enter option number only ->")
    format_selected = int(input("Choose a predefine format: ")) - 1

    while not (0 <= format_selected < len(formats)):
        print("You entered a non found number!")
        format_selected = int(input("Choose a predefine format: ")) - 1

    fmat = formats[format_selected]
    return fmat, formats_data[fmat]


def main():
    return show_format(list(formats_data.keys()))


if __name__ == "__main__":
    main()
