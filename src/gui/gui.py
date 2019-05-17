try:
    # http://www.tkdocs.com/tutorial/install.html
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
import tkMessageBox
# ttk available at:
# https://pypi.python.org/pypi/pyttk
from ttk import *
import tkFileDialog as fd
from tkFileDialog import askopenfilename


def create_IE_log_tab(notebook, temp, scale_factor):
    # Creates the log tab in the GUI
    # Sets up frame
    t1 = Frame(notebook, name='ie_log')
    t1.grid()

    Label(t1).grid(row=0)

    # Preparing drop-down menu variables
    variable1 = StringVar(t1)
    variable2 = StringVar(t1)
    variable3 = StringVar(t1)
    variable4 = StringVar(t1)

    Label(t1, text="Ground state/State 1, unlabeled: ").grid(row=2, columnspan=2)
    Button(t1, text="Browse", command=lambda: browse_button_2(
        variable1, t1, 2)).grid(row=2, column=2)

    Label(t1, text="Ground state/State 1, labeled: ").grid(row=4, columnspan=2)
    Button(t1, text="Browse", command=lambda: browse_button_2(
        variable2, t1, 4)).grid(row=4, column=2)

    Label(t1, text="Transition state/State 2, unlabeled: ").grid(row=6, columnspan=2)
    Button(t1, text="Browse", command=lambda: browse_button_2(
        variable3, t1, 6)).grid(row=6, column=2)

    Label(t1, text="Transition state/State 2, labeled: ").grid(row=8, columnspan=2)
    Button(t1, text="Browse", command=lambda: browse_button_2(
        variable4, t1, 8)).grid(row=8, column=2)

    Label(t1).grid(row=10)
    Label(t1).grid(row=11)

    Label(t1, text="Bigeleisen-Mayer Method:",
          font="bold").grid(row=19, columnspan=4)
    Label(t1, text="KIE/EIE:").grid(row=20)
    KIE_BM = Entry(t1, width=10)
    KIE_BM.grid(row=20, column=1)
    KIE_BM.insert(0, "")

    Label(t1, text="KIE/EIE with tunneling:").grid(row=21)
    KIEtun_BM = Entry(t1, width=10)
    KIEtun_BM.grid(row=21, column=1)
    KIEtun_BM.insert(0, "")

    Label(t1).grid(row=22)

    Label(t1, text="Rigid-Rotor Method:", font="bold").grid(row=23,
                                                            columnspan=4)
    Label(t1, text="KIE/EIE:").grid(row=24)
    KIE_RR = Entry(t1, width=10)
    KIE_RR.grid(row=24, column=1)
    KIE_RR.insert(0, "")

    Label(t1, text="KIE/EIE with tunneling:").grid(row=25)
    KIEtun_RR = Entry(t1, width=10)
    KIEtun_RR.grid(row=25, column=1)
    KIEtun_RR.insert(0, "")

    Label(t1).grid(row=26)

    Button(t1, text="Calculate Isotope Effect", command=lambda: calculate_IE_LOG_GUI(variable1.get(), variable2.get(),
                                                                                     variable3.get(), variable4.get(), temp.get(), scale_factor.get(),
                                                                                     KIE_BM, KIEtun_BM, KIE_RR, KIEtun_RR)).grid(row=12, columnspan=4)

    Label(t1).grid(row=13)

    return t1


def create_IE_fchk_tab(notebook, temp, scale_factor):
    # Creates the fchk tab in the GUI
    # Sets up frame
    t2 = Frame(notebook, name='ie_fchk')
    t2.grid()

    Label(t2).grid(row=0)

    # Preparing file name variables
    variable1 = StringVar(t2)
    variable2 = StringVar(t2)

    Label(t2, text="Ground state/State 1: ").grid(row=2, columnspan=2)
    Button(t2, text="Browse", command=lambda: browse_button_3(
        variable1, t2, 2)).grid(row=2, column=2)

    Label(t2, text="Transition state/State 2: ").grid(row=4, columnspan=2)
    Button(t2, text="Browse", command=lambda: browse_button_3(
        variable2, t2, 4)).grid(row=4, column=2)

    Label(t2).grid(row=5)

    Label(t2, text="Atom symbol (H, C, etc.):").grid(row=6)
    atom_sym = Entry(t2, width=10)
    atom_sym.grid(row=6, column=1)
    atom_sym.insert(0, "")

    Label(t2).grid(row=7)

    Label(t2, text="GS/State 1 atom #:").grid(row=8)
    GS_atom_num = Entry(t2, width=10)
    GS_atom_num.grid(row=8, column=1)
    GS_atom_num.insert(0, "")

    Label(t2).grid(row=9)

    Label(t2, text="TS/State 2 atom #:").grid(row=10)
    TS_atom_num = Entry(t2, width=10)
    TS_atom_num.grid(row=10, column=1)
    TS_atom_num.insert(0, "")

    Label(t2).grid(row=11)

    Label(t2, text="Isotope mass (i.e. 2 for deuterium):").grid(row=12)
    iso_mass = Entry(t2, width=10)
    iso_mass.grid(row=12, column=1)
    iso_mass.insert(0, "")

    Label(t2).grid(row=13)

    Label(t2, text="Pressure (atm):").grid(row=14)
    pressure = Entry(t2, width=10)
    pressure.grid(row=14, column=1)
    pressure.insert(0, "1.0")

    Label(t2).grid(row=15)

    Label(t2, text="Write hyperchem files?").grid(row=16)
    hyperchem = Entry(t2, width=10)
    hyperchem.grid(row=16, column=1)
    hyperchem.insert(0, "No")

    Label(t2).grid(row=17)

    Label(t2, text="Project out gradient direction?").grid(row=18)
    grad_dir = Entry(t2, width=10)
    grad_dir.grid(row=18, column=1)
    grad_dir.insert(0, "No")

    Label(t2).grid(row=19)
    Label(t2).grid(row=20)

    Label(t2, text="Bigeleisen-Mayer Method:", font="bold").grid(row=23,
                                                                 columnspan=4)
    Label(t2, text="KIE/EIE:").grid(row=24)
    KIE_BM = Entry(t2, width=10)
    KIE_BM.grid(row=24, column=1)
    KIE_BM.insert(0, "")

    Label(t2, text="KIE/EIE with tunneling:").grid(row=25)
    KIEtun_BM = Entry(t2, width=10)
    KIEtun_BM.grid(row=25, column=1)
    KIEtun_BM.insert(0, "")

    Label(t2).grid(row=26)

    Label(t2, text="Rigid-Rotor Method:", font="bold").grid(row=27,
                                                            columnspan=4)
    Label(t2, text="KIE/EIE:").grid(row=28)
    KIE_RR = Entry(t2, width=10)
    KIE_RR.grid(row=28, column=1)
    KIE_RR.insert(0, "")

    Label(t2, text="KIE/EIE with tunneling:").grid(row=29)
    KIEtun_RR = Entry(t2, width=10)
    KIEtun_RR.grid(row=29, column=1)
    KIEtun_RR.insert(0, "")

    Label(t2).grid(row=30)

    Button(t2, text="Calculate Isotope Effect", command=lambda: calculate_IE_FCHK_GUI(variable1.get(), variable2.get(),
                                                                                      temp.get(), scale_factor.get(), pressure.get(), hyperchem.get(),
                                                                                      grad_dir.get(), atom_sym.get(), GS_atom_num.get(),
                                                                                      TS_atom_num.get(), iso_mass.get(), KIE_BM, KIEtun_BM,
                                                                                      KIE_RR, KIEtun_RR)).grid(row=21, columnspan=4)

    Label(t2).grid(row=22)

    return t2


def create_NMR_tab(notebook, temp):
    # Creates the NMR tab in the GUI
    # Sets up frame
    t3 = Frame(notebook, name="nmr")
    t3.grid()

    Label(t3).grid(row=0)

    Label(t3, text="Choose directory containing NMR and thermal correction files.").grid(
        row=1, columnspan=4)

    Label(t3).grid(row=2)

    # Directory choosing for NMR & thermal correction files
    Label(t3, text="Select directory:").grid(row=3)

    dirname = StringVar()

    Button(t3, text="Browse", command=lambda: browse_button_1(
        dirname, t3, 3)).grid(row=3, column=1)

    TMS_fname = StringVar()

    Label(t3, text="Select standard: ").grid(row=5)

    Button(t3, text="Browse", command=lambda: browse_button_2(
        TMS_fname, t3, 5)).grid(row=5, column=1)

    Label(t3, text="Select atom numbers: ").grid(row=7)

    nums_ntry = Entry(t3, width=10)
    nums_ntry.grid(row=7, column=1)

    Button(t3, text="Calculate NMR Shifts", command=lambda: calc_shift_difference(
        dirname, TMS_fname, nums_ntry, temp.get())).grid(row=8, columnspan=4, pady=20)

    return t3


def browse_button_1(dirname, t3, row_id):
    # Gets directory name and displays what was chosen to user
    dirname.set(fd.askdirectory())
    label_row = row_id + 1
    show_dir = Label(t3, text="Selected: " + dirname.get(), wraplength=400,
                     justify=LEFT)
    show_dir.grid(row=label_row, columnspan=4)


def browse_button_2(TMS_fname, t3, row_id):
    # Gets file name (log files) and displays what was chosen to user
    file_opt = options = {}
    options['filetypes'] = [('Log files', '.log'),
                            ('Out files', '.out'), ('All files', '.*')]

    TMS_fname.set(askopenfilename(**file_opt))
    label_row = row_id + 1
    show_fname = Label(t3, text="Selected: " + TMS_fname.get(),
                       wraplength=500, justify=LEFT)
    show_fname.grid(row=label_row, columnspan=4)


def browse_button_3(TMS_fname, t3, row_id):
    # Gets file name (fchk files) and displays what was chosen to user
    file_opt = options = {}
    options['filetypes'] = [('Formatted checkpoint files', '.fchk'),
                            ('All files', '.*')]
    #options['filetypes'] = [('All files', '.*')]

    TMS_fname.set(askopenfilename(**file_opt))
    label_row = row_id + 1
    show_fname = Label(t3, text="Selected: " + TMS_fname.get(),
                       wraplength=500, justify=LEFT)
    show_fname.grid(row=label_row, columnspan=4)


def create_top_frame(mainframe):
    # Set up top panel (stuff not changing via tabs)
    topf = Frame(mainframe)

    Label(topf).grid(row=0)

    Label(topf, text="Temperature (K):").grid(row=1)
    temp = Entry(topf, width=10)
    temp.grid(row=1, column=1)
    temp.insert(0, "298.15")

    Label(topf).grid(row=5)

    # Scaling factor entry
    Label(topf, text="Scaling factor:").grid(row=8)
    scale_factor = Entry(topf, width=10)
    scale_factor.grid(row=8, column=1)
    scale_factor.insert(0, "1.0")

    Label(topf).grid(row=9)

    return topf, temp, scale_factor


def create_bottom_frame(mainframe, temp, scale_factor):
    # Setup bottom panel (Notebook, tab changing)
    botf = Frame(mainframe)

    # Notebook widget allows for tabbed functionality
    nb = Notebook(botf, name="nb")
    nb.grid()

    # Creating 3 tabs via respective methods & adding them to notebook
    t1 = create_IE_log_tab(nb, temp, scale_factor)
    nb.add(t1, text="IE_log_files")

    t2 = create_IE_fchk_tab(nb, temp, scale_factor)
    nb.add(t2, text="IE_fchk_files")

    t3 = create_NMR_tab(nb, temp)
    nb.add(t3, text="NMR")

    return botf


def GUI():
    # Setup main window & set title
    root = Tk()
    root.title("Onyx")

    # Create main frame, holding everything
    mf = Frame(root, name="mainframe")
    mf.grid()

    # Create top frame
    top_frame, temp, scale_factor = create_top_frame(mf)
    top_frame.grid()

    # Create bottom frame
    bottom_frame = create_bottom_frame(mf, temp, scale_factor)
    bottom_frame.grid()

    # Force to top
    root.lift()

    # mainloop
    root.mainloop()
