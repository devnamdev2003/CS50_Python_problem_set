while True:
    value = input("Fraction: ")
    list1 = value.split("/")
    try:
        list1[0] = int(list1[0])
        list1[1] = int(list1[1])
        try:
            ans = 100*(list1[0]/list1[1])
            ans=round(ans)
            ans = int(ans)
            if ans > 100:
                pass
            elif ans <=1:
                print("E")
                break
            elif ans<98 and ans>0:
                ans=str(ans)
                print(ans+"%")
                break
            else:
                  print("F")
                  break
        except ZeroDivisionError:
            pass
    except ValueError:
        pass
