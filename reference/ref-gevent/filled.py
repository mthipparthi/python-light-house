from requests_html import HTMLSession


def main():
    session = HTMLSession()
    r = session.get("http://apply.dataprocessors.com.au/")

    count = 0
    for i in r.html.find("img"):
        print(i.attrs["src"])
        if i.attrs["src"] == "filledO.gif":
            count += 1
    print(count)


if __name__ == "__main__":
    main()
