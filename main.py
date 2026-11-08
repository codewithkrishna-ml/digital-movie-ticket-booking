#PROJECT-Digital Movie Ticket Booking
class Movie:
    def __init__(self, title,genre,price):
        self.title = title
        self.genre = genre
        self.price = price

class Showtime:
    def __init__(self,movie,time,rows=3,cols=4):
        self.movie = movie
        self.time = time
        self.seating_grid = []
        for r in range(rows):
            row_list = []
            for c in range(cols):
                row_list.append("0")
            self.seating_grid.append(row_list)

    def display_seats(self):
        print(f"\n---------Seating Arrangement for {self.movie.title} ({self.time})--------")
        for r in range(len(self.seating_grid)):
            print(f"Row {r}:" , end="")
            for c in range(len(self.seating_grid[r])):
                print(f"[{self.seating_grid[r][c]}] " , end="")
            print()

    def reserve_seat(self,row_index,col_index):
        if row_index < 0 or row_index >= len(self.seating_grid) or col_index < 0 or col_index >= len(self.seating_grid[0]):
            print("Invailed seat coordinates!")
            return False
        
        if self.seating_grid[row_index][col_index] == "X":
            print("Sorry this seat is already booked!")
            return False
        else:
            self.seating_grid[row_index][col_index] = "X"
            return True

class BookingEngine:
    def __init__(self):
        self.shows = []

    def add_show(self,showtime_object):
        self.shows.append(showtime_object)

    def list_available_shows(self):
        if not self.shows:
            print("No active screening running today")
            return False
        
        for index in range(len(self.shows)):
            current_show = self.shows[index]
            print(f"[{index}] Title: {current_show.movie.title} | Time: {current_show.time} | Price: {current_show.movie.price}")
        return True

    def book_ticket(self,show_index,row,col):
        if show_index < 0 or show_index >= len(self.shows):
            print("Invailed movie selection index choice!")
            return False

        selected_show = self.shows[show_index]

        booking_success = selected_show.reserve_seat(row,col)
        if booking_success:
            print("\n===============================================")
            print("               TICKET CONFIRMED                  ")
            print("=================================================")
            print(f"Title: {selected_show.movie.title}| Time: {selected_show.time} | Row: {row}| seat: {col}|Price: {selected_show.movie.price}")
            print("======================================================")
            return True
        else:
            return False

if __name__ == "__main__":
    engine = BookingEngine()

    m1 = Movie("Inception" , "Sci-Fi" , 12)
    m2 = Movie("The Dark knight" , "Action" , 15)

    s1 = Showtime(m1 , "03:00 PM")
    s2 = Showtime(m2 , "07:30 PM")

    engine.add_show(s1)
    engine.add_show(s2)

    while True:
        print("\n-------- DIGITAL MOVIE TICKET BOOKING ---------")
        print("1.View Movie Schedules \n2.check seat layout \n3.Book Ticket  \n4.Exit")
        user_choice = input("Select an option (1-4):")
        if user_choice == "1":
            engine.list_available_shows()
        elif user_choice == "2":
            if engine.list_available_shows():
                try:
                    show_idx = int(input("Enter movie show index to view seating map:"))
                    if 0 <= show_idx < len(engine.shows):
                        engine.shows[show_idx].display_seats()
                    else:
                        print("Invailed show selection!")
                except ValueError:
                    print("Please enter numeric integers only")
               
        elif user_choice == "3":
            if engine.list_available_shows():
                try:
                    show_idx = int(input("Enter movie show index:"))
                    row_num = int(input("Enter Row number:"))
                    col_num = int(input("Enter seat number:"))
                    engine.book_ticket(show_idx , row_num , col_num)
                except ValueError:
                    print("Please enter vailed numeric integer choice only")

        elif user_choice == "4":
            print("Exiting system runtime program tracker...GoodBye!")
            break
        else:
            print("Invailed choice! Please select an option 1 and 4")
