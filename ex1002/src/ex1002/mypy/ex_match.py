
day = 4

match day:
    case 1:
        print("Monday")    
    case 2:
        print("Tusday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
        print("기능정리1")
        print("기능정리2")
        print("기능정리3")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# ------------------------------
day2 = 4

match day2:
    case 6: 
        print("오늘은 화요일")
    case 7:     
        print("오늘은 수요일")
    case _:
        print("일치하는 값이 없으면 case _ 출력함.")

# ------------------------------
month = 5
day3 = 4
match day3:
    case 1|2|3|4|5 if month == 4:
        print("4월")
    case 1|2|3|4|5 if month == 5:
        print("5월")
    case _:
        print("맞는값이 없음.")




