def createSeatMap():
    while True:
        try:
            row, col = input(
                "Input number of seat in theater (row col) : ").split(" ")
            row = int(row)
            col = int(col)
        except ValueError:
            print("Please insert 2 number only !!")
            continue
        except:
            print("Please insert number !!")
            continue
        if row <= 0 or col <= 0:
            print("!! Please insert positive number.")
        else:
            arr = []
            for i in range(row):
                arr_col = []
                for j in range(col):
                    arr_col.append(0)
                arr.append(arr_col)
            cap = len(arr) * len(arr[0])
            return arr, cap


def showSeat(seat):
    s_row = len(seat)
    s_col = len(seat[0])
    print()
    print("----- Theater layout -----")
    print()
    print("<- SCREEN ->")
    for i in range(s_row):
        for j in range(s_col):
            if seat[i][j] == 1:
                print("X", end=' ')
            else:
                print('_', end=' ')
        print()
    print()
    print("----- Theater layout -----")
    print()


def booking(seat_b, cap):
    fail = 0
    while True:
        flag = False
        success = 0
        try:
            book_seat = int(input("number to book (seat remaining : {}) : ".format(cap)))
        except ValueError:
            print("Please insert 1 number only !!")
            continue
        except:
            print("Please insert number !!")
            continue
        else:
            if book_seat <= 0:
                print("Please insert positive number !!")
                continue
            elif book_seat > cap:
                print("Not enough capacity !!")
                continue
            elif book_seat > len(seat_b) * len(seat_b[0]):
                print("Over theater size")
                continue
            else:
                flag = True
                i = 1
                while i <= book_seat:
                    try:
                        book_r, book_c = input("Location to book ({}) (row col) ? : ".format(i)).split()
                        book_r = int(book_r)
                        book_c = int(book_c)
                    except ValueError:
                        print("Please insert 2 numbers only !!")
                        continue
                    except:
                        print("Please insert positive number or zero !!")
                        continue
                    if book_r >= len(seat_b) or book_c >= len(
                            seat_b[0]) or book_c < 0 or book_r < 0:
                        print("!! Please input in range [ row 0 -> ",
                              len(seat_b) - 1, " ,colum  0 -> ",
                              len(seat_b[0]) - 1, " ]")
                        continue
                    else:
                        if seat_b[book_r][book_c] == 1:
                            print("Location is booked !!")
                            fail += 1
                            continue
                        else:
                            seat_b[book_r][book_c] = 1
                            success += 1
                            cap -= 1
                    i += 1
                return success, fail, flag, cap, seat_b


def money(seat_m):
    count_f = 0
    count_h = 0
    for i in range(len(seat_m)):
        for j in range(len(seat_m[0])):
            if i < len(seat_m) / 2 and seat_m[i][j] == 1:
                count_f += 1
            if i > len(seat_m) / 2 and seat_m[i][j] == 1:
                count_h += 1
    sum = count_f * 150 + count_h * 200
    return sum


def main(seat, cap):
    if cap == 0:
        return 'n', 0
    success, failure, ff, capp, seat = booking(seat, cap)
    if ff:
        showSeat(seat)
        print("Success =", success, ", Failure =", failure)
        print("Total money : {} $ ".format(money(seat)))
        print()
        if capp == 0:
            return 'n', 0
        re = input("Are you want to book more ? (y=yes ,n=no) : ")
        while ((re.upper() != "Y") and (re.upper() != "N")):
            re = input("Are you want to book more ? (y=yes ,n=no) : ")
    else:
        print("Fail to booking")
        re = input("Are you want to book again ? (y=yes ,n=no) : ")
        while ((re.upper() != "Y") and (re.upper() != "N")):
            re = input("Are you want to book again ? (y=yes ,n=no) : ")
    print()
    print("------------------")
    return re, capp

seat, cap = createSeatMap()
rr, cap_new = main(seat, cap)
while rr.upper() == "Y":
  rr, cap_new = main(seat, cap_new)
print("Thank you _/|\_")
