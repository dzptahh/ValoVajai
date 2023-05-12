import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import ttk
import matplotlib.pyplot
from matplotlib.figure import Figure
from tkinter.scrolledtext import ScrolledText
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Canvas, PhotoImage
from PIL import ImageTk, Image
import networkx as nx

matplotlib.use('TkAgg')


class File:
    """For open files text"""

    def __init__(self):
        self.lines_2 = []
        with open('info.txt', 'r') as f:
            self.lines_2 = f.readlines()


class PageUI(tk.Tk):
    def __init__(self, valo: File):
        super().__init__()
        self.players = pd.read_csv("players.csv", encoding='latin-1')
        print(self.players)
        self.valo = valo
        self.title('ValoVajai')
        self.login_page()
        self.resizable(True, True)

    def login_page(self):
        self.geometry("1000x650")
        self.clear_frame()

        # create login frame
        login_frame = tk.Frame(self, bd=0, highlightthickness=0, background="white", width=50)
        login_frame.grid(row=0, column=0, sticky="nsew", padx=80, pady=30)

        # create sign-in details
        text = tk.Label(login_frame, text="Sign in", font=('Futura', 36), fg='#3A405A')
        text.pack(pady=5)

        # create register system
        username = tk.StringVar()
        password = tk.StringVar()

        # set username label and username entry
        username_label = tk.Label(login_frame, text="USERNAME", fg='#1F2933', padx=10, font="Futura", width=35)
        username_label.pack(pady=5)
        self.entry_username = tk.Entry(login_frame, textvariable=username, fg='#1F2933')
        self.entry_username.pack(pady=5, padx=10)

        # set password label and password entry
        password_label = tk.Label(login_frame, text="PASSWORD", fg='#1F2933', padx=10, font="Futura")
        password_label.pack(pady=5)
        self.entry_password = tk.Entry(login_frame, textvariable=password, fg='#1F2933', show='*')
        self.entry_password.pack(pady=5, padx=10)

        # set up the register button
        register_button = tk.Button(login_frame, width=10, height=1, text='Register', fg='#EA5455', state=tk.DISABLED,
                                    command=self.handler)

        # set up the trace on the username and password fields
        username.trace("w", lambda *args: self.toggle_button(register_button, username, password))
        password.trace("w", lambda *args: self.toggle_button(register_button, username, password))

        # pack the register button
        register_button.pack(pady=7)

        # set quit button
        self.quit = tk.Button(login_frame, text="log out", fg='#EA5455', command=self.destroy)
        self.quit.pack(expand=False)

        # create image frame
        img_frame = tk.Frame(self, bd=0, highlightthickness=0, background="#c5f25b")
        img_frame.grid(row=0, column=1, sticky="nsew")

        # set image
        self.img = Image.open("Valorant-Gekko-Art.png")
        self.img = self.img.resize((800, 750))
        self.img = ImageTk.PhotoImage(self.img)

        # create canvas and display image
        canvas = tk.Canvas(img_frame, width=self.img.width(), height=self.img.height(), highlightthickness=0,
                           background="#c5f25b")
        canvas.create_image(0, 0, anchor="nw", image=self.img)
        canvas.grid(row=0, column=0, sticky="nsew", padx=5, pady=1)

        # configure grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        login_frame.grid_columnconfigure(0, weight=1)

        # set up the validation function
        def validate_input(new_value):
            return " " not in new_value

        # set up the validation command for the username and password entries
        validate_cmd = self.register(validate_input)
        self.entry_username.configure(validate="key", validatecommand=(validate_cmd, "%P"))
        self.entry_password.configure(validate="key", validatecommand=(validate_cmd, "%P"))

    @staticmethod
    def toggle_button(button, username, password):
        if username.get() != "" or password.get() != "":
            button.configure(state="normal")
        else:
            button.configure(state="disabled")

    def handler(self):
        # check if the username and password fields are not empty
        if self.entry_username.get() != "" and self.entry_password.get() != "":
            # if both fields are not empty, go to the information page
            self.info_page()

        else:
            # if one or both fields are empty, display an error message
            error_frame = tk.Frame(self, bg='white')
            error_frame.grid(row=4, column=1, sticky="nsew")

            fail = tk.Label(error_frame, text='Registration failed. Please enter all information.', fg='red')
            fail.grid(row=0, column=0)

            # after 2 seconds, destroy the error message
            self.after(2000, fail.destroy)
            self.after(2000, error_frame.destroy)

    def info_page(self):
        """Display the page with International League Playoffs about Valorant"""
        self.geometry("1000x1000")  # Set the size of the window
        self.clear_frame()  # Remove any widgets from previous pages

        # Set up two frames to use as backgrounds for the heading and text
        heading_frame = tk.Frame(bd=0, highlightthickness=0, background="#F9F9F9")
        heading_frame.place(x=0, y=0, relwidth=1.0, relheight=.5, anchor="nw")
        text_frame = tk.Frame(bd=0, highlightthickness=0, background="#F9F9F9")
        text_frame.place(x=0, rely=.5, relwidth=1.0, relheight=.5, anchor="nw")

        # Create a heading label and pack it into the heading frame
        heading_label = tk.Label(self, text='THE ROAD TO CHAMPIONS 2023!', font=('Friz Quadrata Bold', 36, 'bold'),
                                 foreground='#EA5455', background='#F9F9F9')
        heading_label.pack(padx=12, pady=12, fill=tk.BOTH)

        # Create a ScrolledText widget and insert the text into it
        text_widget = ScrolledText(self, width=10, height=20, font=('Open Sans Regular', 16), foreground='#1F2933')
        text_widget.pack(padx=12, pady=7, fill=tk.BOTH, side='top', expand=True)

        # Configure a tag for bold text
        text_widget.tag_configure("bold", font=("Open Sans Regular", 16, "bold"))

        # Insert the text with formatting
        text = "International League Playoffs\nMay 19 - 28\n\nThe three International Leagues will commence their " \
               "respective playoffs in late May. Pacific League playoffs will begin first on May 19th, and EMEA and " \
               "Americas Playoffs will begin on May 23rd. Results here will be critically important, as the top three " \
               "teams from each league will qualify for both Masters Tokyo and Champions Los Angeles. The exception " \
               "is EMEA, who as a result of fielding 4 teams at Masters Tokyo will qualify the teams that finish " \
               "within the top 3.\n\nMasters Tokyo\nJune 11 - 25\n\nMasters Tokyo will feature the top three " \
               "representatives from each league as well as two teams from China. As a result of FNATIC’s win at " \
               "LOCK//IN, EMEA earned an extra slot at the tournament and will be sending a fourth team. The team " \
               "that emerges victorious will be declared the Masters Tokyo Champion and earn their region a fifth " \
               "slot at Champions.\n\nChallengers Ascension\nJune 28 - July 16\n\nImmediately after the conclusion of " \
               "Masters, fans can look forward to the start of Challengers Ascension. More than twenty Challengers " \
               "Leagues have been underway across the world in 2023, narrowing down hundreds of teams to the very " \
               "best. Each of the three Ascension tournaments will promote one team each into the international " \
               "leagues for 2023. We’ll be sharing detailed information about the Ascension tournaments in the coming " \
               "weeks.\n\nChampions CN Qualifiers\nJuly 3 - 16\n\nTwelve teams from China will compete through the " \
               "Champions CN Qualifiers to determine the region’s strongest contenders. The top three teams to emerge " \
               "from the tournament will earn their shot at Champions.\n\nLast Chance Qualifier\nJuly 15 - 23\n\nThe " \
               "Last Chance Qualifier is the final opportunity for teams in the international leagues to claim a spot " \
               "at Champions. Each of the ILs will qualify a fourth team through the LCQs, except for the region who " \
               "won Masters who will qualify two teams.\n\nChampions Los Angeles\nAugust 6 - 26\n\nAll roads lead to " \
               "Champions - the biggest event of the 2023 VALORANT Champions Tour. The tournament will feature 16 " \
               "teams who will converge in Los Angeles to fight for the Champions title. We have a lot in store for " \
               "Champions with more details coming soon."
        text_widget.insert(tk.END, text)
        text_widget.tag_add("bold", "1.0", "2.end")  # Apply bold formatting to the specific line
        text_widget.tag_add("bold", "6.0", "7.end")
        text_widget.tag_add("bold", "11.0", "12.end")
        text_widget.tag_add("bold", "16.0", "18.end")
        text_widget.tag_add("bold", "21.0", "23.end")
        text_widget.tag_add("bold", "26.0", "28.end")
        text_widget.tag_configure("center", justify="center")
        text_widget.tag_add("center", "1.0", "end")  # Apply center formatting to the entire text

        # Disable the text widget so the user can't edit it
        text_widget['state'] = 'disable'

        # Create a button to navigate to the next page
        next_button = tk.Button(self, width=45, text='Next Page', fg='#EA5455', command=self.info_page2)
        next_button.pack(side='bottom', pady=7)

        # Create and Place the log-out button
        logout_button = tk.Button(self, width=10, text='logout', fg='#EA5455', command=self.login_page)
        logout_button.place(relx=1, x=-10, y=60, anchor='ne')

        # Create the quit button
        quit_button = tk.Button(self, text='Quit', command=self.destroy, foreground="#EA5455")
        # Place the quit button above the logout button
        quit_button.place(relx=1, x=-10, y=10, anchor='ne')

    def info_page2(self):
        """Displays a page with information about Valorant include Roadmap image of VCT.

        The page includes a heading, a button to navigate to the next page, a button to navigate to the previous
        page, and a label widget that displays the information about road mpa and slot.

        """
        self.clear_frame()
        self.geometry("1000x1000")

        # create a heading
        head = tk.Label(self, text='ROADMAP', font=('Friz Quadrata Bold', 36, 'bold'), foreground='#EA5455')
        head.pack()
        subtitle = tk.Label(self,
                            text='THE ROAD TO CHAMPIONS 2023!\nFind out the details of the major VALORANT Esports '
                                 'events taking place this summer.',
                            font=('Open Sans Regular', 18), background="white")
        subtitle.pack(pady=1)
        # create a button to navigate to the next page
        button = tk.Button(self, width=45, text='Next Page', fg='#EA5455', command=self.graph_page)
        button.pack(side='bottom', pady=7)

        # create a button to navigate to the previous page
        button2 = tk.Button(self, width=45, text='Previous Page', fg='#EA5455', command=self.info_page)
        button2.pack(side='bottom', pady=7, expand=False)

        # create a canvas to hold the frame with the images and labels
        canvas = tk.Canvas(self, background="#140202", bd=0, highlightthickness=0)
        canvas.pack(side='top', pady=7, padx=12, fill=tk.BOTH, expand=True)

        # create a frame to contain the label and image widgets
        frame = tk.Frame(canvas, background="#140202", bd=0, highlightthickness=0)
        canvas.create_window((0, 0), window=frame, anchor='nw')

        # create an image widget
        self.roadmap_image = tk.PhotoImage(file='roadmap.png')
        self.roadmap_image = self.roadmap_image.subsample(2)  # scale the image by a factor of 2
        image_label = tk.Label(frame, image=self.roadmap_image, background="#140202", width=self.roadmap_image.width(),
                               height=self.roadmap_image.height())
        image_label.pack(side='top', padx=7, pady=7)

        # create a label to display info.txt
        info_label = tk.Label(frame, text='\n'.join(self.valo.lines_2), font=('Open Sans Regular', 16),
                              background="#140202",
                              foreground='#ffffff')
        info_label.config(text='\n'.join(self.valo.lines_2))

        info_label.pack(side='top', padx=7, pady=7)

        # create a second image widget
        self.roadmap_image_2 = tk.PhotoImage(file='second_roadmap.png')
        self.roadmap_image_2 = self.roadmap_image_2.subsample(2)  # scale the image by a factor of 2
        image_label_2 = tk.Label(frame, image=self.roadmap_image_2, background="#140202",
                                 width=self.roadmap_image_2.width(), height=self.roadmap_image_2.height())
        image_label_2.pack(side='top', padx=7, pady=7)

        # add a scrollbar to the canvas
        scrollbar = tk.Scrollbar(self, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')

        canvas.config(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox('all')))

        # move the scrollbar to the right side of the canvas
        canvas.pack(side='left', pady=7, padx=12, fill=tk.BOTH, expand=True)
        scrollbar.pack(side='right', fill='y')

        # Create and Place the log-out button
        logout_button = tk.Button(self, width=10, text='logout', fg='#EA5455', command=self.login_page)
        logout_button.place(relx=1, x=-10, y=30, anchor='ne')

        # Create the quit button
        quit_button = tk.Button(self, text='Quit', command=self.destroy, foreground="#EA5455")
        # Place the quit button above the logout button
        quit_button.place(relx=1, x=-10, y=5, anchor='ne')

    def graph_page(self):
        """Page for plotting"""
        self.geometry("1000x1000")
        self.clear_frame()

        #  Create the quit button
        quit_button = tk.Button(self, text='Quit', command=self.destroy, foreground="#EA5455")
        quit_button.pack(side='top', anchor='ne', padx=10, pady=5)

        # Create a button to go to the network graph page
        button1 = tk.Button(self, width=45, text='Network Page', fg='#EA5455', command=self.network_graph_page)
        button1.pack(side='bottom', pady=7)

        # set previous button
        button2 = tk.Button(self, width=45, text='Previous Page', fg='#EA5455', command=self.info_page2)
        button2.pack(side='bottom', pady=7, expand=False)

        # call the function to create and plot the graph
        self.for_plot_graph()

        # display the graph image using the pic() method
        self.pic(self)

    def for_plot_graph(self):
        # Create a label frame for the "select topic" filter
        self.frame_filter = ttk.LabelFrame(self, text="Select Topic")
        self.frame_filter.pack(fill='both', side='top')

        # Add a label to the filter frame
        label1 = ttk.Label(self.frame_filter, text="Topic")
        label1.pack(fill='both', side='top')

        # Create a combobox for the filter, and load options from the data
        self.cbb = tk.StringVar()
        self.cbb1 = ttk.Combobox(self, width=18)
        self.cbb1['state'] = 'readonly'
        self.cbb1.pack(fill='both', side='top', expand=False)
        self.cbb1.bind('<<ComboboxSelected>>', self.update)
        self.load_data()

        # Create a Matplotlib plot for the Valo e-sport data
        self.fig_valo = Figure()
        self.axis_valo = self.fig_valo.add_subplot()
        self.fig_canvas1 = FigureCanvasTkAgg(self.fig_valo, master=self)
        self.fig_canvas1.get_tk_widget().pack(fill='both')

    def plot_valovajai(self):
        # Clear the plot and update it with data based on the current filter selection
        self.axis_valo.clear()
        self.fig_valo.subplots_adjust(bottom=0.50)
        blinder = self.players
        sett = blinder.set_index("Player")
        gett = sett[self.cbb1.get()]
        gett.plot.bar(ax=self.axis_valo)
        self.axis_valo.set(xlabel='Name', title="The pro player's name in game")
        plt.xticks(rotation=90)
        self.fig_canvas1.draw()

    def load_data(self):
        # Load the column names of the Valo e-sport data into the combobox for filtering
        select_ = self.players.columns[2:]
        lst = list(select_)
        self.cbb1['values'] = lst

    def update(self, valo):
        # Update the plot when a new filter selection is made
        self.plot_valovajai()

    def pic(self, pics):
        # Add a picture to the GUI canvas
        self.canvas = Canvas(pics, width=840, height=400)
        self.canvas.pack(side='bottom', expand=True)
        self.image = PhotoImage(file='vct_champ.png')
        # Use the create_image method to display the loaded image
        self.canvas.create_image(320, 170, image=self.image)

    def network_graph_page(self):
        # Create graph object
        self.geometry("600x600")
        self.clear_frame()

        # Create head title
        head = tk.Label(self, text='Network Visualization', font=('Friz Quadrata Bold', 36, 'bold'),
                        foreground='#EA5455')
        head.pack()

        # Create the quit button
        quit_button = tk.Button(self, text='Quit', command=self.destroy, foreground="#EA5455")
        quit_button.pack(side='top', anchor='ne', padx=10, pady=5)

        # set previous button
        button2 = tk.Button(self, width=45, text='Previous Page', fg='#EA5455', command=self.graph_page)
        button2.pack(side='bottom', pady=7, expand=False)

        # Define nodes
        nodes = ['zombs', 'ShahZaM', 'dapr', 'SicK', 'cNed', 'starxo', 'Kiles', 'nAts', 'Chronicle', 'd3ffo', 'Sheydos',
                 'BONECOLD', 'Redgar', 'zeek', 'TenZ', 'ScreaM', 'soulcas', 'L1NK', 'mixwell', 'crashies']

        # Create graph object
        G = nx.Graph()

        # Add nodes to the graph
        G.add_nodes_from(nodes)

        # Generate all possible combinations of edges between nodes
        edges = [(node1, node2) for node1 in nodes for node2 in nodes if node1 < node2]

        # Add edges to the graph
        G.add_edges_from(edges)

        # Set node positions for layout
        pos = nx.spring_layout(G, k=1)

        # Draw the graph
        fig, ax = plt.subplots()
        nx.draw_networkx_nodes(G, pos, node_color="#c5f25b", node_size=500)
        nx.draw_networkx_edges(G, pos, edge_color="#d7d7d5", width=1)
        nx.draw_networkx_labels(G, pos, dict(zip(nodes, nodes)), font_size=12)

        # Add a title and labels
        plt.title("Network Graph")
        plt.xlabel("Node")
        plt.ylabel("")

        # Hide the axis
        ax.axis('off')

        # Embed the plot into a tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.get_tk_widget().config(highlightthickness=1, highlightbackground="#7c37e8")

    def clear_frame(self):
        # Remove all widgets from the current frame to prepare for the next page
        for widget in self.winfo_children():
            widget.destroy()

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    player = File()
    ui = PageUI(player)
    ui.run()
