def createSeatMap():
    while True:
        print("----------")
        print("Welcome to theater seat booking system ^-^")
        print("Please input theater size ")
        row, col = check_err(1, "Please insert one positive numbers. !!", "b","", [])
        if row < 0 or col < 0: continue
        return [[0 for i in range(row)] for j in range(col)], row * col

def showSeat(seat):
    book = list(map(lambda x: list(map(lambda y: 'X' if y == 1 else '_', x)), seat))
    print()
    print("----- Theater layout -----")
    print()
    print("<- SCREEN ->")
    [print(*x) for x in book]
    print()
    print("----- Theater layout -----")
    print()

def booking(seat_b, cap):
    width = len(seat_b[0]) - 1
    length = len(seat_b) - 1
    fail = 0
    while True:
        success = 0
        incap = "number to book (seat remaining : {}) : ".format(cap)
        book_seat = check_err(1, "Please insert one positive number only. !!","a", incap, [])
        if book_seat < 0: continue
        if book_seat > cap:
            print("Not enough capacity or !!")
            continue
        else:
            i = 1
            while i <= book_seat:
                caption = "Location to book ({}) (row col) ? : ".format(i)
                error_cap = "Please input numbers in range ( Width 0 -> {} ) ( Length  0 -> {} ). !!".format(length, width)
                book_r, book_c = check_err(0, error_cap, "c", caption, seat_b)
                if book_r < 0 or book_c < 0:
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
            return success, fail, cap, seat_b

def money(seat_m):
    return sum(map(sum, seat_m[:len(seat_m) // 2])) * 150 + sum(map(sum, seat_m[len(seat_m) // 2:])) * 200

def main(seat, cap):
    success, failure, capp, seat = booking(seat, cap)
    showSeat(seat)
    print("-- Status --")
    print("Success =", success, ", Failure =", failure)
    print("Total money : {} $ ".format(money(seat)))
    print()
    if capp == 0: return '', 0
    while True:
        re = input("Are you want to book more ? (y=yes ,n=no) : ")
        if ((re.upper() == "Y") or (re.upper() == "N")): break
        else: print("Please insert y or n . !!")
    print()
    print("------------------")
    return re, capp

def check_err(limit, caption, mode, in_cap, arr):
    try:
        if mode == "a":
          a = input_mode1(mode, in_cap, limit)
        else:
          a,b = input_mode2(mode, limit, arr)
    except ValueError:
        print(caption)
        if mode == "a": return -1
        else: return -1, -1
    else:
        if mode == "a": return a
        else: return a, b

def input_mode1(mode,in_cap,limit):
  if mode == "a":
      a = int(input(in_cap))
      if a < limit: raise (ValueError)
  return a
  
def input_mode2(mode,limit,arr):
  if mode == "b":
      a = int(input("Width : "))
      b = int(input("Length : "))
      if a < limit or b < limit: raise (ValueError)
  else:
      a = int(
        input("position number of row (0 to {}) : ".format(len(arr) -1)))
      b = int(input("position number of column (0 to {}) : ".format(
                    len(arr[0]) - 1)))
      if a < limit or a >= len(arr) or b < limit or b >= len(arr[0]): raise (ValueError)
  return a,b

def core():
    seat, cap_new = createSeatMap()
    while True:
        rr, cap_new = main(seat, cap_new)
        if rr.lower() == "n": break
    print("Thank you _/|\_")

core()
