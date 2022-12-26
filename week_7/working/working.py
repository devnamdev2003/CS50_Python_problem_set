import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if "to" in s:
        try:
            start = re.search("(((0?[1-9]|1[0-2]):([0-5]\d))|(0?[1-9]|1[0-2]))\s(AM|PM)", s).group()
            end = re.search("(((0?[1-9]|1[0-2]):([0-5]\d))|(0?[1-9]|1[0-2]))\s(AM|PM)", s.replace(start, "")).group()

            times_converted = []
            for i in [start, end]:
                if ":" in i:
                    if "PM" in i:
                        if i[:-6] == "12":
                            times_converted.append(f"{int(0) + 12:02}" + ":" + i[:-3].split(':')[1])
                        else:
                            times_converted.append(f"{int(i[:-3].split(':')[0]) + 12:02}" + ":" + i[:-3].split(':')[1])
                    else:
                        if i[:-6] == "12":
                            times_converted.append(f"{int(0):02}" + ":" + i[:-3].split(':')[1])
                        else:
                            times_converted.append(f"{int(i[:-3].split(':')[0]):02}" + ":" + i[:-3].split(':')[1])
                else:
                    if "PM" in i:
                        if i[:-3] == "12":
                            times_converted.append(f"{int(0) + 12:02}" + ":00")
                        else:
                            times_converted.append(f"{int(i[:-3]) + 12:02}" + ":00")
                    else:
                        if i[:-3] == "12":
                            times_converted.append(f"{int(0):02}" + ":00")
                        else:
                            times_converted.append(f"{int(i[:-3]):02}" + ":00")
            return f"{times_converted[0]} to {times_converted[1]}"
        except:
            raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()