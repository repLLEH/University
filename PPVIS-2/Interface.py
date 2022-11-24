import tkinter as tk
from tkinter import ttk
from tkinter.constants import *

from Controller import DiaryController

MAIN_COLOR = "white"
SECOND_COLOR = "gray30"
THIRD_COLOR = "gray80"
BG_COLOR = "#A3A4E5"


class ManagingElements:

    def __init__(self):
        self.controller = DiaryController()
        self.window = tk.Tk()
        self.window.title("TasksDiary")
        self.window.geometry("280x500")
        self.window.resizable(width=False, height=False)
        self.screens_and_names = {
            "ScreenMain": ScreenMain(name="Ежедневник",
                                     managing_elements=self, master=self.window),
            "ScreenTaskListDisplay": ScreenTaskListDisplay(name="Список записей",
                                                           managing_elements=self, master=self.window),
            "ScreenEnteringNewTask": ScreenEnteringNewTask(name="Новая запись",
                                                           managing_elements=self, master=self.window),
            "ScreenEditingTask": ScreenEditingTask(name="ScreenEditingTask",
                                                   managing_elements=self, master=self.window),
        }
        self.updateAndActivate("ScreenMain")

    def updateAndActivate(self, screen_name):
        for name in self.screens_and_names:
            self.screens_and_names[name].place(relx=0, rely=0, relwidth=0, relheight=0)
        self.screens_and_names[screen_name].update()
        self.screens_and_names[screen_name].place(relx=0, rely=0, relwidth=1, relheight=1)


class DisplayScreen(tk.Frame):
    def __init__(self, name: str, managing_elements: ManagingElements, **kwargs):
        super().__init__(**kwargs)
        self._name = name
        self._managing_elements = managing_elements
        _window_name_label = tk.Label(self, text=f"{self._name}", bg=BG_COLOR, font=("Arial", 12), fg=SECOND_COLOR)
        _window_name_label.place(relwidth=1, relheight=0.1, anchor="nw")

    def update(self):
        pass
        # try:
        #    self._managing_elements.updateAndActivate(self._name)
        # except Exception as ex:
        #    print(ex)


class VerticalScrolledFrame(ttk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    * This frame only allows vertical scrolling.
    """

    def __init__(self, parent, **kw):
        ttk.Frame.__init__(self, parent, **kw)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        v_scrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        v_scrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0, yscrollcommand=v_scrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        v_scrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = ttk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW)

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            _ = event
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            _ = event
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)


class ScreenWithTable(DisplayScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._table_tasks_frame = tk.Frame(self)
        if self._name == "Ежедневник":
            self._table_tasks_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.75)
        elif self._name == "ScreenTaskListDisplay":
            self._table_tasks_frame.place(relx=0, rely=0.25, relwidth=1, relheight=0.6)
        self.update()

    def update(self):
        super(ScreenWithTable, self).update()
        # print("updating")
        # for name in self._table_tasks_frame:
        #    self._table_tasks_frame[name].place(relx=0, rely=0, relwidth=0, relheight=0)

        table = VerticalScrolledFrame(self._table_tasks_frame)
        table.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        columns_frame = tk.Frame(self._table_tasks_frame)
        title = tk.Label(columns_frame, text=f"Записи", width=100, anchor="center", bg=THIRD_COLOR)

        title.pack(side=LEFT, padx=1, pady=1, ipady=10)
        # category.pack(side=LEFT, padx=1, pady=1, ipady=10)
        # date.pack(side=LEFT, padx=1, pady=1, ipady=10)
        # overdue.pack(side=LEFT, padx=1, pady=1, ipady=10)
        columns_frame.place(relx=0.01, rely=0, relwidth=1, relheight=0.1)

        formatted_tasks = []
        all_tasks = self._managing_elements.controller.showNoteList(1,date='19.10.2022')
        # for task in all_tasks:
        #     task_frame = tk.Frame(table.interior)
        #     # title = tk.Label(task_frame, text=f"{task['name']}", width=8, anchor="center", bg=BG_COLOR)
        #     title = tk.Button(task_frame, text=f"{task['name']}", width=8, anchor="center",
        #                       bg=BG_COLOR, border=0, command=self._openScreenEditingTask)
        #     category = tk.Label(task_frame, text=f"{task['category']}", width=8, anchor="center", bg=BG_COLOR)
        #     date = tk.Label(task_frame, text=f"{task['date']}", width=8, anchor="center", bg=BG_COLOR)
        #     # overdue = tk.Label(task_frame, text=f"{task['overdue']}", width=8, anchor="center", bg=BG_COLOR)
        #     img = tk.PhotoImage(file=f"img/{task['overdue']}.png")
        #     overdue = tk.Button(task_frame, image=img, bg=BG_COLOR, border=0, width=60, height=50)
        #     overdue.image = img
        #
        #     title.pack(side=LEFT, padx=1, pady=1, ipady=15)
        #     category.pack(side=LEFT, padx=1, pady=1, ipady=16)
        #     date.pack(side=LEFT, padx=1, pady=1, ipady=8)
        #     overdue.pack(side=LEFT, padx=1, pady=1, ipady=0)
        #
        #     formatted_tasks.append(task_frame)
        #     formatted_tasks[-1].pack()

    def _openScreenEditingTask(self):  # , task_index_in_output_table: int):
        self._managing_elements.updateAndActivate("ScreenEditingTask")


class ScreenMain(ScreenWithTable):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        buttons_frame = tk.Frame(master=self, bg=BG_COLOR)
        self.button_open_screen_entering_new_task = tk.Button(buttons_frame, text="[+]", bg=MAIN_COLOR,
                                                              fg=BG_COLOR, font=("Arial", 10), border=0,
                                                              command=self._openScreenEnteringNewTask)
        self.button_open_screen_task_list_display = tk.Button(buttons_frame, text="Список записей", bg=MAIN_COLOR,
                                                              fg=BG_COLOR, font=("Arial", 10), border=0,
                                                              command=self._openScreenTaskListDisplay)
        self.button_open_screen_entering_new_task.place(rely=0.1, relx=0.05, relwidth=0.4, relheight=0.8, anchor="nw")
        self.button_open_screen_task_list_display.place(rely=0.1, relx=0.55, relwidth=0.4, relheight=0.8, anchor="nw")
        buttons_frame.place(rely=0.85, relwidth=1, relheight=0.15, anchor="nw")

    def _openScreenEnteringNewTask(self):
        self._managing_elements.updateAndActivate("ScreenEnteringNewTask")
        # self._managing_elements.updateAndActivate("ScreenEditingTask")

    def _openScreenTaskListDisplay(self):
        self._managing_elements.updateAndActivate("ScreenTaskListDisplay")

    def update(self):
        super(ScreenMain, self).update()


class ScreenTaskListDisplay(ScreenWithTable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buttons frame
        buttons_frame = tk.Frame(master=self, bg=BG_COLOR)
        self.button_open_screen_main = tk.Button(buttons_frame, text="Профиль", bg=MAIN_COLOR,
                                                 fg=BG_COLOR, font=("Arial", 10), border=0,
                                                 command=self._openScreenMain)
        self.button_open_screen_main.place(rely=0.1, relx=0.05, relwidth=0.9, relheight=0.8, anchor="nw")
        buttons_frame.place(rely=0.85, relwidth=1, relheight=0.15, anchor="nw")
        # search frame
        search_frame = tk.Frame(master=self, bg=BG_COLOR)

        self.input_text_for_search = tk.Entry(search_frame, highlightthickness=1, border=0,
                                              fg=SECOND_COLOR, font=("Arial", 10))
        self.input_text_for_search.config(highlightbackground=THIRD_COLOR, highlightcolor=THIRD_COLOR)

        self.button_search_task = tk.Button(search_frame, text="Найти", bg=MAIN_COLOR,
                                            fg=BG_COLOR, font=("Arial", 10), border=0,
                                            command=None)

        self.input_text_for_search.place(rely=0, relx=0.05, relwidth=0.9, relheight=0.4, anchor="nw")
        self.button_search_task.place(rely=0.5, relx=0.05, relwidth=0.9, relheight=0.45, anchor="nw")
        search_frame.place(rely=0.1, relwidth=1, relheight=0.15, anchor="nw")

    def _openScreenMain(self):
        self._managing_elements.updateAndActivate("ScreenMain")

    def _searchTask(self):
        pass


class ScreenEnteringNewTask(DisplayScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buttons frame
        buttons_frame = tk.Frame(master=self, bg=BG_COLOR)

        self.button_open_screen_main = tk.Button(buttons_frame, text="Назад", bg=MAIN_COLOR,
                                                 fg=BG_COLOR, font=("Arial", 10), border=0,
                                                 command=self._openScreenMain)
        self.button_save_new_task = tk.Button(buttons_frame, text="Добавить", bg=MAIN_COLOR,
                                              fg=BG_COLOR, font=("Arial", 10), border=0,
                                              command=self._saveNewTask)
        self.button_open_screen_main.place(rely=0.1, relx=0.05, relwidth=0.4, relheight=0.8, anchor="nw")
        self.button_save_new_task.place(rely=0.1, relx=0.55, relwidth=0.4, relheight=0.8, anchor="nw")

        buttons_frame.place(rely=0.85, relwidth=1, relheight=0.15, anchor="nw")
        # entering new task frame
        self.search_frame = tk.Frame(master=self, bg=BG_COLOR)

        text_1 = tk.Label(self.search_frame, text="Как прошел ваш день", bg=BG_COLOR,
                          fg=MAIN_COLOR, font=("Arial", 10), anchor="w")
        bg_1 = tk.Label(self.search_frame, text="", bg=MAIN_COLOR)
        self.input_1 = tk.Entry(self.search_frame, border=0, fg=MAIN_COLOR, font=("Arial", 10))
        text_1.place(rely=0.0, relx=0.05, relwidth=0.9, relheight=0.05, anchor="nw")
        bg_1.place(rely=0.063, relx=0.05, relwidth=0.9, relheight=0.1, anchor="nw")
        self.input_1.place(rely=0.06, relx=0.05, relwidth=0.9, relheight=0.1, anchor="nw")



        self.search_frame.place(rely=0.1, relwidth=1, relheight=0.75, anchor="nw")

    def _openScreenMain(self):
        self._managing_elements.updateAndActivate("ScreenMain")

    def _saveNewTask(self):
        self._managing_elements.controller.taskCreation()
        self._managing_elements.updateAndActivate("ScreenMain")


class ScreenEditingTask(ScreenEnteringNewTask):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.button_save_new_task.command = self._changeTask
        # editing/deleting task
        var1 = tk.BooleanVar()
        var2 = tk.BooleanVar()
        var1.set(0)
        var2.set(0)
        checkbox_text_1 = tk.Label(self.search_frame, text="Delete task", bg=BG_COLOR,
                                   fg=SECOND_COLOR, font=("Arial", 11), anchor="nw")
        self.checkbox_1 = tk.Checkbutton(self.search_frame, bg=BG_COLOR, anchor="nw", variable=var1,
                                         onvalue=1, offvalue=0)
        checkbox_text_1.place(rely=0.8, relx=0.15, relwidth=0.85, relheight=0.1, anchor="nw")
        self.checkbox_1.place(rely=0.8, relx=0.05, relwidth=0.1, relheight=0.1, anchor="nw")
        checkbox_text_2 = tk.Label(self.search_frame, text="Task finished", bg=BG_COLOR,
                                   fg=SECOND_COLOR, font=("Arial", 11), anchor="nw")
        self.checkbox_2 = tk.Checkbutton(self.search_frame, bg=BG_COLOR, border=2, anchor="nw", variable=var2,
                                         onvalue=1, offvalue=0)
        checkbox_text_2.place(rely=0.88, relx=0.15, relwidth=0.85, relheight=0.1, anchor="nw")
        self.checkbox_2.place(rely=0.88, relx=0.05, relwidth=0.1, relheight=0.1, anchor="nw")
        self.search_frame.place(rely=0.1, relwidth=1, relheight=0.75, anchor="nw")

    def _openScreenMain(self):
        self._managing_elements.updateAndActivate("ScreenMain")

    def _changeTask(self):
        self._managing_elements.controller.noteChoice(1)
main_window=ManagingElements()
main_window.window.mainloop()