class Star_Cinema:
    __hall_list = [] # private attribute

    @staticmethod
    def entry_hall(hall):
        Star_Cinema.__hall_list.append(hall)

    @staticmethod
    def get_hall_list():
        return Star_Cinema.__hall_list # private attribute access korar jonno

class Hall:
    def __init__(self, rows, cols, hall_num):
        self.rows = rows
        self.cols = cols
        self.hall_num = hall_num
        self.seats = {} # key holo show id ar value holo boser jaiga
        self.show_list = []

    def entry_show(self, id, movie_name, time):
        new_show = (id, movie_name, time)
        self.show_list.append(new_show)
        self.seats[id] = [[0 for i in range(self.rows)] for j in range(self.cols)]

    def book_seat(self, show_id, seat_list):
        
        for row,col in seat_list:
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if self.seats[show_id][row][col] == 0:
                    self.seats[show_id][row][col] = 1
                    print(f"seat booked ({row}, {col}) for show id {show_id}")
                else:
                    print(f"seat at row {row} col {col} is already booked")   
            else:
                print("that row and col is not valid")
       
    def view_show_list(self):
        for show in self.show_list:
             print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
    def view_available_seats(self, show_id):
        if show_id in self.seats:
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.seats[show_id][row][col] == 0:
                        print(f"seat ({row}, {col})")
                    else:
                        print("Booked seat")
        else:
            print("Show id is not found")

hall1 = Hall(5,5,1)
Star_Cinema.entry_hall(hall1)
hall1.entry_show(111, 'jawan', '11:00 AM')
hall1.entry_show(222, 'rawan', '1:00 AM')

while True:
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")

    print("OPTION :")
    Choice = int(input("ENTER OPTION :"))

    if Choice == 1:
        hall1.view_show_list()
    elif Choice == 2:
        id = int(input("SHOW ID : "))
        hall1.view_available_seats(id)
    elif Choice == 3:
        id = int(input("SHOW ID : "))
        if id in hall1.seats:
            ticket = int(input("NUMBER OF TICKET : "))
            show_list = []
            for i in range(ticket):
                row = int(input("ENTER SEAT ROW :"))
                col = int(input("ENTER SEAT COL :"))
                show_list.append((row,col))
            hall1.book_seat(id, show_list)
        
        else:
            print("Show is not avilable")

    elif Choice == 4:
        print("Exiting the show.")
        break
    else:
        print("Invalid option")
