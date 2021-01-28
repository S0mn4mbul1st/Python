import pprint
import tkinter
from contextlib import closing
import sqlite3
import requests
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import matplotlib
import tkinter as tk
import PIL.Image
from PIL import ImageTk, Image

matplotlib.use('TkAgg')
window = tkinter.Tk()
status_line = StringVar()
output_line = StringVar()
img = ''
canvas = tkinter.Canvas(window, bg=window['bg'], height=450, width=450)

def request_data():
    countries_api_res = requests.get('http://api.worldbank.org/countries?format=json&per_page=100')
    countries = countries_api_res.json()[1]
    pprint.pprint(countries[0])
    save_to_db(countries)


def save_to_db(countries):
  try:
    if np.os.path.isfile('dataset.db'):
        output_line.set('Database is exsist!')
        conn = sqlite3.connect('dataset.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS countries (id varchar(3), latitude REAL)''')
        for country in countries:
            c.execute("insert into countries values (?, ?)",
                  [country['id'], country['latitude']])
            conn.commit()
        conn.close()
  except sqlite3.Error as error:
    print("Failed to download the data", error)


def create_main_window():
    global status_line
    window.geometry('550x500')
    window.title('Scripting Languages Project')
    status_line.set('STATUS LINE')
    header = tkinter.Label(window, text='Data Analysis Application',
                           height=4)
    header.grid(row=0, columnspan=10)

    menubar = tk.Menu(window)
    window.config(menu=menubar)

    button_get_data = tkinter.Button(window,
            text='Get Data From The Internet', command=lambda :
            get_data(), width=60)
    button_get_data.grid(row=10, column=0, sticky='e')

    button_clear_db = tkinter.Button(window, text='Clear Database',
            command=lambda : clear_db(), width=60)
    button_clear_db.grid(row=20, column=0, sticky='e')

    button_aggregation = tkinter.Button(window,
            text='Displays an aggregation of the downloaded data (Finding the Avegare of latitude durations)',
            command=lambda : get_aggregation(), width=80)
    button_aggregation.grid(row=30, columnspan=2, sticky='e')

    button_chart_printer = tkinter.Button(window,
            text='Display data from the database as a chart',
            command=lambda : chart_printer(), width=60)
    button_chart_printer.grid(row=40, columnspan=2)

    button_change_theme = tkinter.Button(window, text='Change theme',
            command=lambda : change_theme(), width=60)
    button_change_theme.grid(row=50, columnspan=2)

    button_stop = tkinter.Button(window, text='Quit',
                                 command=exit_cmd, width=60)
    button_stop.grid(row=60, columnspan=4)

    status_label = tkinter.Label(window, textvariable=status_line, height=2)
    status_label.grid(row=80, columnspan=2, padx=2, pady=2)

    output_label = tkinter.Label(window, textvariable=output_line, height=2)
    output_label.grid(row=100, columnspan=2, padx=2, pady=2)

    window.mainloop()



def exit_cmd():
    answer = tk.messagebox.askyesno(
    title="Quit",
    message="Do you really want to quit?")
    if answer == True:
        exit()


def get_avg_latitude_duration():
    with closing(sqlite3.connect("dataset.db")) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('''
            SELECT AVG(countries.latitude)
            FROM countries
            ''')
            return cursor.fetchall()
        conn.commit()


def get_data():
    status_line.set('Data has been downloaded')
    data_set = request_data()


def clear_db():
    status_line.set('Database has been cleaned')
    try:
        conn = sqlite3.connect('dataset.db')
        c = conn.cursor()
        c.execute('''DELETE FROM countries;''', );
        print('We have deleted', c.rowcount, 'records from the table.')
        conn.commit()
    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")


def get_aggregation():
    status_line.set('Aggregation Printed')
    output_line.set(get_avg_latitude_duration())


def chart_printer():
        status_line.set('Chart Printed')
        make_plot()
        canvas = tkinter.Canvas(window, bg=window['bg'], height=450, width=450)
        canvas.grid()

        pil_image = Image.open("plot.png")
        tk_image = ImageTk.PhotoImage(pil_image)
        img = canvas.create_image(450, 25,
                                  anchor=tk.NE,
                                  image=tk_image)
        window.mainloop()
def make_plot():
    listA = []
    listB = []
    counter = 0

    figure = plt.figure()
    axes = figure.add_subplot(1,1,1)

    conn = sqlite3.connect('dataset.db')
    c = conn.cursor()
    c.execute('SELECT latitude FROM countries')
    result = c.fetchall()

    for data in result:
        if(isinstance(data[0], float)):
            listA.append(data[0])
            listB.append(counter)
            counter += 1
    plt.xlabel('Latitude of the country')
    plt.ylabel('Index')
    plt.title('Latitude changes of the countries by index')
    plt.tight_layout()
    plt.plot(listA, listB)
    fig = plt.gcf()
    fig.set_size_inches(4, 4)
    fig.savefig('plot.png')


def change_theme():
    status_line.set('Theme has been changed')
    if window['bg'] == 'Snow':
        window['bg'] = 'gray23'
        canvas['bg'] = window['bg']
    elif window['bg'] == 'gray23':
        window['bg'] = 'royalblue'
        canvas['bg'] = window['bg']
    else:
        window['bg'] = 'Snow'
        canvas['bg'] = window['bg']


def run():
    create_main_window()


if __name__ == '__main__':
    run()
