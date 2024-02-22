from customtkinter import *
from tkinter.ttk import *
from PIL import Image
from random import choice
import pandas


def data(top_players=False):
    file = pandas.read_csv("data.csv")
    file = file.groupby("players", as_index=False).sum()
    if top_players:
        file = file.sort_values("score", ascending=False)
        data_players = []
        n = 0
        for value in file.values:
            if n < 10:
                player = value[0]
                score = value[1]
                data_players.append([player, score])
                n += 1
        return data_players
    else:
        data_players = []
        n = 0
        for value in file.values:
            player = value[0]
            score = value[1]
            data_players.append([player, score])
        return data_players


class GUI:
    def __init__(self):
        self.players = []
        set_default_color_theme(r"C:\Users\New Person\Desktop\Python\Python Projects\tic tac toe\theme\doomed.json")

        self.app = CTk()
        self.app.title("Tic Tac Toe")
        self.app.iconbitmap("img/icon.ico")
        self.app.geometry("500x600")

        self.frame = CTkFrame(self.app, height=600, width=500)
        self.frame.pack(expand=True)

        self.back_icon = CTkButton(self.frame, image=CTkImage(Image.open("img/back.ico"), size=(18, 30)), text="",
                                   width=30, border_width=0, fg_color="#300000", hover_color="#400000")

        self.exit_icon = CTkButton(self.frame, image=CTkImage(Image.open("img/exit.ico"), size=(30, 30)), text="",
                                   width=30, border_width=0, fg_color="#300000", hover_color="#400000",
                                   command=lambda: self.show_dialog("Are you sure do you want to exit ?", 2,
                                                                    ["Yes", "No"], [self.exit_game, self.close_dialog]))
        self.exit_icon.place(x=440, y=20)

        self.powered_label = CTkLabel(self.frame, text="Powered by Cesar Leon")
        self.powered_label.place(x=20, y=550)

        self.home_page()
        # self.mode_game(page=1, user="Cesara")
        self.degrade(0)

    def degrade(self, n: int):
        style = Style()
        if n == 0:
            self.app.configure(fg_color="#300000")
            self.frame.configure(fg_color="#300000")

            self.back_icon.configure(fg_color="#300000", hover_color="#300000")
            self.exit_icon.configure(fg_color="#300000", hover_color="#300000")

            style.configure('TLabelframe', background="#300000")
            style.configure('TLabelframe.Label', background="#300000")

            self.app.after(5000, self.degrade, n + 1)

        elif n == 1:
            self.app.configure(fg_color="#600000")
            self.frame.configure(fg_color="#600000")

            self.back_icon.configure(fg_color="#600000", hover_color="#600000")
            self.exit_icon.configure(fg_color="#600000", hover_color="#600000")
            style.configure('TLabelframe', background="#600000")
            style.configure('TLabelframe.Label', background="#600000")

            self.app.after(150, self.degrade, n + 1)
        elif n == 2:
            self.app.configure(fg_color="#400000")
            self.frame.configure(fg_color="#400000")

            self.back_icon.configure(fg_color="#400000", hover_color="#400000")
            self.exit_icon.configure(fg_color="#400000", hover_color="#400000")
            style.configure('TLabelframe', background="#400000")
            style.configure('TLabelframe.Label', background="#400000")

            self.app.after(5000, self.degrade, n + 1)
        elif n == 3:
            self.app.configure(fg_color="#700000")
            self.frame.configure(fg_color="#700000")

            self.back_icon.configure(fg_color="#700000", hover_color="#700000")
            self.exit_icon.configure(fg_color="#700000", hover_color="#700000")
            style.configure('TLabelframe', background="#700000")
            style.configure('TLabelframe.Label', background="#700000")

            self.app.after(150, self.degrade, 0)

    def home_page(self, objects: list = None):
        if objects is not None:
            for widget in objects:
                widget.place_forget()

        title = CTkLabel(self.frame, text='Tic Tac Toe', font=CTkFont(size=64))
        title.place(x=100, y=150)

        start_button = CTkButton(self.frame, text="Start Game", width=200, height=40,
                                 command=lambda: self.start_game([start_button, title]))
        start_button.place(x=160, y=300)

    def start_game(self, objects: list = None):
        if objects is not None:
            for widget in objects:
                widget.place_forget()

        title = CTkLabel(self.frame, text='Tic Tac Toe', font=CTkFont(size=64))
        title.place(x=100, y=150)

        self.back_icon.configure(command=lambda: self.home_page([new_game, select_player, self.back_icon]))
        self.back_icon.place(x=20, y=20)

        new_game = CTkButton(self.frame, text="New Player", width=200, height=40,
                             command=lambda: self.insert_player([new_game, select_player, title]))
        new_game.place(x=160, y=300)

        select_player = CTkButton(self.frame, text="Select Player", width=200, height=40,
                                  command=lambda: self.select_player([new_game, select_player, title]))
        select_player.place(x=160, y=360)

    def insert_player(self, objects: list = None):
        if objects is not None:
            for widget in objects:
                widget.place_forget()

        self.back_icon.configure(command=lambda: self.start_game([title, username_entry, send_username]))

        title = CTkLabel(self.frame, text="Input Your Username", font=CTkFont(size=36))
        title.place(x=80, y=150)

        username_entry = CTkEntry(self.frame, placeholder_text="Your Username", width=200, height=40, justify="center")
        username_entry.place(x=140, y=300)

        send_username = CTkButton(self.frame, text="➡", height=40, width=40)
        send_username.place(x=350, y=300)

        send_username.configure(
            command=lambda: self.mode_game(page=0, user=username_entry.get().capitalize(),
                                           objects=[title, username_entry, send_username]))

    def select_player(self, objects: list = None, second_player=False):
        if objects is not None:
            for widget in objects:
                widget.place_forget()

        self.back_icon.configure(command=lambda: self.start_game([title, tree_frame, select_button]))

        title = CTkLabel(self.frame, text="Select Player", font=CTkFont(size=48))
        title.place(x=100, y=50)

        tree_frame = CTkFrame(self.frame)
        tree_frame.place(x=60, y=150)

        scrollbar = CTkScrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")

        style = Style()
        style.theme_use("clam")
        style.configure("Treeview", font=("Kdam Thmor Pro", 13, "bold"), foreground="#FFFFFF", rowheight=25,
                        fieldbackground="#800000")
        style.configure("Treeview.Heading", font=("Kdam Thmor Pro", 15, 'bold'), foreground="#FFFFFF",
                        background="#000000", borderwidth=0, fieldbackground="yellow")
        style.map('Treeview', background=[("selected", '#300000')])
        style.map('Treeview.Heading',
                  background=[('!active', '#300000'), ('pressed', '#700000'), ('active', '#500000')])

        data_players = data()
        cols = ("Players", "Score")
        treeview = Treeview(tree_frame, show="headings", columns=cols, height=10, yscrollcommand=scrollbar.set, )
        treeview.column("Players", width=250)
        treeview.column("Score", width=120)
        treeview.tag_configure('odd', background='#900000')
        treeview.tag_configure('even', background='#800000')
        treeview.delete(*treeview.get_children())

        n = 0
        for player in data_players:
            if n % 2 == 0:
                tag = "odd"
            else:
                tag = "even"
            treeview.insert('', END, values=[player[0], player[1]], tags=tag)
            n += 1

        for column in treeview["columns"]:
            treeview.column(column, anchor=CENTER)
            treeview.heading(column, text=column)

        treeview.focus(treeview.get_children()[0])
        treeview.selection_set(treeview.get_children()[0])

        treeview.pack()

        scrollbar.configure(command=treeview.yview)

        select_button = CTkButton(self.frame, text="Select", width=300, height=40)
        select_button.place(x=100, y=470)
        if not second_player:
            select_button.configure(command=lambda: self.mode_game(page=1, user=treeview,
                                                                   objects=[title, tree_frame, select_button]))
        else:
            select_button.configure(command=lambda: self.mode_game(page=1, user=treeview,
                                                                   objects=[title, tree_frame, select_button],
                                                                   is_selected=True))

    def mode_game(self, page: int, user: Treeview or str, objects: list = None, is_selected=False):
        file = pandas.read_csv("data.csv")
        if objects is not None:
            for widget in objects:
                widget.place_forget()

        if type(user) is Treeview:
            item = user.focus()
            values = user.item(item)["values"]
            if is_selected:
                if values[0] == self.players[0]:
                    self.select_player(second_player=True)
                    self.show_dialog("That player has been selected", 1, ["Try Again"],
                                     [self.close_dialog], geometry="250x100")
                    return
            try:
                score = values[1]
            except IndexError:
                self.select_player()
                self.show_dialog("Select a player", 1, ["Try Again"],
                                 [self.close_dialog], geometry="200x100")
                return
            else:
                user = values[0]
        elif len(user) < 3 or len(user) > 10:
            self.insert_player()
            self.show_dialog("You username must have\n between 3 and 10 characters", 1, ["Try Again"],
                             [self.close_dialog], geometry="280x120")
            return
        elif file[file["players"] == user].values.any():
            self.insert_player()
            self.show_dialog("That username already exists", 1, ["Try Again"],
                             [self.close_dialog], geometry="220x100")
            return

        if page == 0:
            self.back_icon.configure(command=lambda: self.insert_player([title, pc, multiplayer, info_icon]))
            file.loc[len(file)] = {"players": user, "score": 0}
            file.to_csv("data.csv", mode="w", header=True, index=False)
        else:
            self.back_icon.configure(command=lambda: self.select_player([title, pc, multiplayer, info_icon]))

        if not is_selected:
            title = CTkLabel(self.frame, text=f'{user}!\nChoose Your Enemy', font=CTkFont(size=36), justify="center")
            title.place(x=80, y=120)

            self.players.append(user)

            pc = CTkButton(self.frame, text="PC", width=200, height=40,
                           command=lambda: self.screen_game(players=[self.players[0], "Pc"],
                                                            objects=[title, pc, multiplayer, self.back_icon, info_icon,
                                                                     self.exit_icon]))
            pc.place(x=150, y=300)

            info_icon = CTkButton(self.frame, image=CTkImage(Image.open("img/info.ico"), size=(20, 20)), text="",
                                  width=40, height=40, border_width=1,
                                  command=lambda: self.show_dialog(
                                      "The battle against PC\n don't add points in leaderboard", 1,
                                      ["Ok"], [self.close_dialog], geometry="250x120"), )
            info_icon.place(x=310, y=300)

            multiplayer = CTkButton(self.frame, text="Multiplayer", width=200, height=40,
                                    command=lambda: self.select_player(
                                        [title, pc, multiplayer, self.back_icon, info_icon, self.exit_icon],
                                        second_player=True))
            multiplayer.place(x=150, y=360)
        else:
            self.players.append(user)
            self.screen_game(players=[self.players[0], self.players[1]], objects=objects)

    def screen_game(self, players: list, objects: list = None):
        if objects is not None:
            for widget in objects:
                widget.place_forget()

        set_appearance_mode("light")
        first_player = CTkLabel(self.frame, text=players[0], font=CTkFont(family="Protest Riot", size=48))
        first_player.place(x=50, y=140)
        versus = CTkLabel(self.frame, text="Vs", font=CTkFont(family="Protest Riot", size=48))
        versus.place(x=230, y=265)
        second_player = CTkLabel(self.frame, text=players[1], font=CTkFont(family="Protest Riot", size=48))
        second_player.place(x=250, y=370)
        self.app.after(3000, lambda: self.play_game(players=players, objects=[first_player, versus, second_player]))

    def play_game(self, players: list, objects: list = None):
        if objects is not None:
            for widget in objects:
                widget.place_forget()

        structure = [
            {
                "a": "-",
                "b": "-",
                "c": "-",
            },
            {
                "a": "-",
                "b": "-",
                "c": "-",
            },
            {
                "a": "-",
                "b": "-",
                "c": "-",
            }
        ]

        board = CTkLabel(self.frame, image=CTkImage(Image.open("img/board.png"), size=(408, 400)), text="")
        board.place(x=40, y=100)

        n = 0
        marks = ["O", "X"]
        columns = ["a", "b", "c"]
        rows = [0, 1, 2]

        def put_shape(position: list, round: int):
            nonlocal structure, n, marks
            if round % 2 == 0:
                image_shape = CTkLabel(self.frame,
                                       image=CTkImage(Image.open(f"img/shapes/square/dashed/sky.png"), size=(90, 90)),
                                       text="")
                number_player = players[1]
            else:
                image_shape = CTkLabel(self.frame,
                                       image=CTkImage(Image.open(f"img/shapes/triangle/outline/green.png"), size=(90, 90)),
                                       text="")
                number_player = players[0]

            if structure[position[0]][position[1]] == "-":
                if position[0] == 0:
                    if position[1] == "a":
                        image_shape.place(x=70, y=125)
                    elif position[1] == "b":
                        image_shape.place(x=200, y=125)
                    elif position[1] == "c":
                        image_shape.place(x=330, y=125)
                elif position[0] == 1:
                    if position[1] == "a":
                        image_shape.place(x=70, y=255)
                    elif position[1] == "b":
                        image_shape.place(x=200, y=255)
                    elif position[1] == "c":
                        image_shape.place(x=330, y=255)
                elif position[0] == 2:
                    if position[1] == "a":
                        image_shape.place(x=70, y=380)
                    elif position[1] == "b":
                        image_shape.place(x=200, y=380)
                    elif position[1] == "c":
                        image_shape.place(x=330, y=380)
                structure[position[0]][position[1]] = marks[players.index(number_player)]
                finish_game = check_game(players, structure, marks)
                if finish_game[0]:
                    if finish_game[1]:
                        self.retry_game("Draw", players, [self.frame.winfo_children()])
                    else:
                        self.retry_game(f"The winner is {players[finish_game[2]]}", players,
                                        [self.frame.winfo_children()])
                else:
                    if players[1] == "Pc" and n % 2 != 0:
                        row = choice([0, 1, 2])
                        column = choice(["a", "b", "c"])
                        n += 1
                        put_shape([row, column], n)
            else:
                if players[1] == "Pc" and n % 2 == 0:
                    row = choice([0, 1, 2])
                    column = choice(["a", "b", "c"])
                    put_shape([row, column], n)
                else:
                    n += 1
                    board.bind("<Button-1>", callback)

        def callback(event):
            nonlocal n
            n += 1
            column_1 = 10 <= event.x <= 140
            column_2 = 145 <= event.x <= 260
            column_3 = 270 <= event.x <= 400

            row_1 = 10 <= event.y <= 135
            row_2 = 140 <= event.y <= 255
            row_3 = 260 <= event.y <= 390

            if row_1:
                if column_1:
                    put_shape([0, "a"], round=n)
                elif column_2:
                    put_shape([0, "b"], round=n)
                elif column_3:
                    put_shape([0, "c"], round=n)
            elif row_2:
                if column_1:
                    put_shape([1, "a"], round=n)
                elif column_2:
                    put_shape([1, "b"], round=n)
                elif column_3:
                    put_shape([1, "c"], round=n)
            elif row_3:
                if column_1:
                    put_shape([2, "a"], round=n)
                elif column_2:
                    put_shape([2, "b"], round=n)
                elif column_3:
                    put_shape([2, "c"], round=n)

        board.bind("<Button-1>", callback)

        def check_game(players: list, structure, marks):
            players_structure = [
                {
                    "rows": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                    "columns": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                    "diagonal": [[0, 0, 0], [0, 0, 0]]
                },
                {
                    "rows": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                    "columns": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                    "diagonal": [[0, 0, 0], [0, 0, 0]]
                }
            ]

            board = 0

            for player in players:
                number_player = players.index(player)
                number_row = 0
                for row in structure:
                    number_position = 0
                    for position in row:
                        # Check Player
                        if row[position] == marks[number_player]:
                            # Check Rows
                            players_structure[number_player]["rows"][number_row][number_position] += 1
                            # Check Columns
                            players_structure[number_player]["columns"][number_position][number_row] += 1
                            # Check Diagonal
                            if number_row == 0:
                                if number_position == 0:
                                    players_structure[number_player]["diagonal"][number_row][number_position] += 1
                                elif number_position == 2:
                                    players_structure[number_player]["diagonal"][number_row + 1][
                                        number_position - 2] += 1
                            elif number_row == 1 and number_position == 1:
                                players_structure[number_player]["diagonal"][number_row - 1][number_position] += 1
                                players_structure[number_player]["diagonal"][number_row][number_position] += 1
                            elif number_row == 2:
                                if number_position == 2:
                                    players_structure[number_player]["diagonal"][number_row - 2][number_position] += 1
                                elif number_position == 0:
                                    players_structure[number_player]["diagonal"][number_row - 1][number_position] += 1
                            board += 1
                        number_position += 1
                    number_row += 1

                    for player_row in players_structure[number_player]["rows"]:
                        if sum(player_row) == 3:
                            return [True, False, number_player]
                    for player_columns in players_structure[number_player]["columns"]:
                        if sum(player_columns) == 3:
                            return [True, False, number_player]
                    for player_diagonal in players_structure[number_player]["diagonal"]:
                        if sum(player_diagonal) == 3:
                            return [True, False, number_player]
                    if board == 9:
                        return [True, True, 0]

            return [False, False, 0]

    def retry_game(self, result, players, objects: list = None):
        if objects is not None:
            for widget in objects:
                for w in widget:
                    w.place_forget()

        title = CTkLabel(self.frame, text=result, font=CTkFont(size=36))
        title.place(x=40, y=120)

        retry_button = CTkButton(self.frame, text="Try Again", width=200, height=40,
                                 command=lambda: self.play_game(players, [retry_button, exit_button, title]))
        retry_button.place(x=40, y=300)

        exit_button = CTkButton(self.frame, text="Finish Game", width=200, height=40, command=self.exit_game)
        exit_button.place(x=250, y=300)

    def show_dialog(self, text: str, number_of_button: int, text_in_button: list, command_in_button: list,
                    geometry: str = "250x150"):

        self.dialog = CTkToplevel(self.app)

        self.dialog.iconbitmap("img/icon.ico")
        self.dialog.title("Tic Tac Toe")
        self.dialog.geometry(geometry)
        self.dialog.grab_set()

        text = CTkLabel(self.dialog, text=text)
        text.pack(pady=20)

        first_button = CTkButton(self.dialog, text=text_in_button[0], command=command_in_button[0])
        first_button.pack(pady=(0, 10))

        if number_of_button > 1:
            second_button = CTkButton(self.dialog, text=text_in_button[1], command=command_in_button[1])
            second_button.pack()

    def close_dialog(self):
        self.dialog.destroy()

    def exit_game(self):
        self.app.destroy()

    def run(self):
        self.app.mainloop()
