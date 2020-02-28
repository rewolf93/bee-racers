import tkinter as tk
from tkinter import filedialog
import config
from gamemode import *
import platform
import os
import pickle as pkl


def create_start_menu():
    root = tk.Tk()
    start = StartMenu(master=root)
    start.mainloop()


class StartMenu(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.title("Bee Racers")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets that make up the start menu"""
        self.select_game_mode_button = tk.Button(self, text="Select Game Mode", command=self.select_game_mode)
        self.select_game_mode_button.grid(row=0)
        self.select_map_button = tk.Button(self, text="Select Map", command=self.select_map)
        self.select_map_button.grid(row=1)
        self.start_button = tk.Button(self, text="Start Game!", command=self.start_game)
        self.start_button.grid(row=2)

    def select_map(self):
        #Opens a file browser to select a .tmx map file to play
        config.map_filename = filedialog.askopenfilename(initialdir=config.maps_folder,
           title="Select Map", filetypes=[("tmx map files", "*.tmx")])
        print(config.map_filename)

    def select_game_mode(self):
        config.game_mode = "Pollen Hunt"
        print("Game mode set to: " + config.game_mode)

    def start_game(self):
        #Closes the start menu and loads the game
        self.master.destroy()
        play_game(config.game_mode)

