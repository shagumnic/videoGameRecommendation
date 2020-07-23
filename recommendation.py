import pandas as pd
import numpy as np
from tkinter import messagebox
from tkinter import *

indices = pd.read_csv('recommend_indices.csv')

cosine_sim = np.load('recommend_cosine.npy')


def recommendation():
    global indices
    global cosine_sim
    try:
        name = list_box.get(list_box.curselection())
    except TclError:
        messagebox.showwarning('Error', 'You haven\'t picked a game yet')
    else:
        recommendation_games = []

        idx = indices[indices.name == name].index[0]

        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)

        top_10_indices = list(score_series.iloc[1:11].index)

        for i in top_10_indices :
            # recommendation_games.append(list(data_df.name)[i])
            recommendation_games.append(list(indices.name)[i])
        print(recommendation_games)
        scrollbar_result = Scrollbar(Output_frame, orient="vertical")
        result_list_box = Listbox(Output_frame, width=200, yscrollcommand=scrollbar_result.set)
        for game in recommendation_games:
            result_list_box.insert(END, game)

        result_list_box.grid(row=0, column=0)


root = Tk()
root.title('Video Game Recommendation')
root.maxsize(1280, 1024)


Intro_Frame = Frame(root, width=1280, height=30, bg='yellow')
Intro_Frame.grid(row=0, column=0, padx=10, pady=5)

Input_frame = Frame(root, width=1280, height=250, bg='grey')
Input_frame.grid(row=1, column=0, padx=10, pady=5)

Outro_frame = Frame(root, width=1280, height=30, bg='white')
Outro_frame.grid(row=2, column=0, padx=10, pady=5)

Output_frame = Frame(root, width=1280, height=250, bg='white')
Output_frame.grid(row=3, column=0, padx=10, pady=5)

scrollbar = Scrollbar(Input_frame, orient="vertical")

Label(Intro_Frame,
      text='Game that you want to find games similar to: ', bg='grey').grid(row=0, column=0,
                                                                            padx=5, pady=5)
Button(Intro_Frame, text='Recommend', command=recommendation,
       bg='green').grid(row=0, column=1, padx=5, pady=5)
list_box = Listbox(Input_frame, width=200, yscrollcommand=scrollbar.set)

for index, row in indices.iterrows():
    list_box.insert(END, row['name'])

list_box.grid(row=0, column=0)

Label(Outro_frame, text='Top 10 games that are similar: ', bg='grey').grid(row=0, column=0,
                                                                           padx=5, pady=5)
root.mainloop()
