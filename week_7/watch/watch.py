import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    youtube_url = re.search('src="(http|https):\/\/w*\.?youtube\.com\/embed/[A-Za-z0-9]+"', s)
    if youtube_url != None:
        youtube_url_truncated = "https://youtu.be/" + re.search("embed/[A-Za-z0-9]+", youtube_url.group()).group().split("/")[1]
        return youtube_url_truncated
    else:
        return youtube_url


if __name__ == "__main__":
    main()