#!/usr/bin/python

# Onyx uses Python 2.7.13 available at:
# https://www.python.org/downloads/release/python-2713/
import numpy as np
# numpy is available at:
# https://pypi.python.org/pypi/numpy/1.12.1
import math as mt
import sys as sys
import os
import subprocess as sub
from operator import itemgetter
import csv
import datetime
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
#from ttk import *
import itertools as itertools
import tkFileDialog as fd
from tkFileDialog import askopenfilename
# argparse available at:
# https://pypi.python.org/pypi/argparse
import argparse

# ==================================================================
#                               GUI
# ==================================================================

def create_IE_log_tab(notebook, temp, scale_factor):
    # Creates the log tab in the GUI
    # Sets up frame
    t1 = Frame(notebook, name='ie_log')
    t1.grid()

    Blank1 = Label(t1).grid(row=0)

    #Preparing drop-down menu variables
    variable1 = StringVar(t1)
    variable1.set("")
    variable2 = StringVar(t1)
    variable2.set("")
    variable3 = StringVar(t1)
    variable3.set("")
    variable4 = StringVar(t1)
    variable4.set("")

    std_select1 = Label(t1, text="Ground state/State 1, unlabeled: ")
    std_select1.grid(row=2, columnspan=2)
    row_id_1 = 2
    std_but1 = Button(t1, text="Browse", command= lambda: \
            browse_button_2(variable1, t1, row_id_1))
    std_but1.grid(row=2, column=2)

    std_select2 = Label(t1, text="Ground state/State 1, labeled: ")
    std_select2.grid(row=4, columnspan=2)
    row_id_2 = 4
    std_but2 = Button(t1, text="Browse", command= lambda: \
            browse_button_2(variable2, t1, row_id_2))
    std_but2.grid(row=4, column=2)

    std_select3 = Label(t1, text="Transition state/State 2, unlabeled: ")
    std_select3.grid(row=6, columnspan=2)
    row_id_3 = 6
    std_but3 = Button(t1, text="Browse", command= lambda: \
            browse_button_2(variable3, t1, row_id_3))
    std_but3.grid(row=6, column=2)

    std_select4 = Label(t1, text="Transition state/State 2, labeled: ")
    std_select4.grid(row=8, columnspan=2)
    row_id_4 = 8
    std_but4 = Button(t1, text="Browse", command= lambda: \
            browse_button_2(variable4, t1, row_id_4))
    std_but4.grid(row=8, column=2)

    Blank5 = Label(t1).grid(row=10)
    Blank6 = Label(t1).grid(row=11)

    Label(t1, text = "Bigeleisen-Mayer Method:", font="bold").grid(row=19,\
            columnspan=4)
    Label(t1, text = "KIE/EIE:").grid(row=20)
    KIE_BM = Entry(t1, width = 10)
    KIE_BM.grid(row=20, column=1)
    KIE_BM.insert(0, "")

    Label(t1, text = "KIE/EIE with tunneling:").grid(row=21)
    KIEtun_BM = Entry(t1, width = 10)
    KIEtun_BM.grid(row=21, column=1)
    KIEtun_BM.insert(0, "")

    Blank7 = Label(t1).grid(row=22)

    Label(t1, text = "Rigid-Rotor Method:", font="bold").grid(row=23, \
            columnspan=4)
    Label(t1, text = "KIE/EIE:").grid(row=24)
    KIE_RR= Entry(t1, width = 10)
    KIE_RR.grid(row=24, column=1)
    KIE_RR.insert(0, "")

    Label(t1, text = "KIE/EIE with tunneling:").grid(row=25)
    KIEtun_RR = Entry(t1, width = 10)
    KIEtun_RR.grid(row=25, column=1)
    KIEtun_RR.insert(0, "")

    Blank8 = Label(t1).grid(row=26)

    calc_but = Button(t1, text ="Calculate Isotope Effect", command= lambda: \
            calculate_IE_LOG_GUI(variable1.get(), variable2.get(),\
            variable3.get(), variable4.get(), temp.get(), scale_factor.get(),\
            KIE_BM, KIEtun_BM, KIE_RR, KIEtun_RR))
    calc_but.grid(row=12, columnspan=4)

    Blank9 = Label(t1).grid(row=13)

    return t1

def create_IE_fchk_tab(notebook, temp, scale_factor):
    # Creates the fchk tab in the GUI
    # Sets up frame
    t2 = Frame(notebook, name='ie_fchk')
    t2.grid()

    Blank1 = Label(t2).grid(row=0)

    #Preparing file name variables
    variable1 = StringVar(t2)
    variable1.set("")
    variable2 = StringVar(t2)
    variable2.set("")

    std_select1 = Label(t2, text="Ground state/State 1: ")
    std_select1.grid(row=2, columnspan=2)
    row_id_1 = 2
    std_but1 = Button(t2, text="Browse", command= lambda: \
            browse_button_3(variable1, t2, row_id_1))
    std_but1.grid(row=2, column=2)

    std_select2 = Label(t2, text="Transition state/State 2: ")
    std_select2.grid(row=4, columnspan=2)
    row_id_2 = 4
    std_but2 = Button(t2, text="Browse", command= lambda: \
            browse_button_3(variable2, t2, row_id_2))
    std_but2.grid(row=4, column=2)

    Blank2 = Label(t2).grid(row=5)

    Label(t2, text = "Atom symbol (H, C, etc.):").grid(row=6)
    atom_sym = Entry(t2, width = 10)
    atom_sym.grid(row=6, column=1)
    atom_sym.insert(0, "")

    Blank3 = Label(t2).grid(row=7)

    Label(t2, text = "GS/State 1 atom #:").grid(row=8)
    GS_atom_num = Entry(t2, width = 10)
    GS_atom_num.grid(row=8, column=1)
    GS_atom_num.insert(0, "")

    Blank4 = Label(t2).grid(row=9)

    Label(t2, text = "TS/State 2 atom #:").grid(row=10)
    TS_atom_num = Entry(t2, width = 10)
    TS_atom_num.grid(row=10, column=1)
    TS_atom_num.insert(0, "")

    Blank5 = Label(t2).grid(row=11)

    Label(t2, text = "Isotope mass (i.e. 2 for deuterium):").grid(row=12)
    iso_mass = Entry(t2, width = 10)
    iso_mass.grid(row=12, column=1)
    iso_mass.insert(0, "")

    Blank6 = Label(t2).grid(row=13)

    Label(t2, text = "Pressure (atm):").grid(row=14)
    pressure = Entry(t2, width = 10)
    pressure.grid(row=14, column=1)
    pressure.insert(0, "1.0")

    Blank5 = Label(t2).grid(row=15)

    Label(t2, text = "Write hyperchem files?").grid(row=16)
    hyperchem = Entry(t2, width = 10)
    hyperchem.grid(row=16, column=1)
    hyperchem.insert(0, "No")

    Blank6 = Label(t2).grid(row=17)

    Label(t2, text = "Project out gradient direction?").grid(row=18)
    grad_dir = Entry(t2, width = 10)
    grad_dir.grid(row=18, column=1)
    grad_dir.insert(0, "No")

    Blank7 = Label(t2).grid(row=19)
    Blank8 = Label(t2).grid(row=20)

    Label(t2, text = "Bigeleisen-Mayer Method:", font="bold").grid(row=23, \
            columnspan=4)
    Label(t2, text = "KIE/EIE:").grid(row=24)
    KIE_BM = Entry(t2, width = 10)
    KIE_BM.grid(row=24, column=1)
    KIE_BM.insert(0, "")

    Label(t2, text = "KIE/EIE with tunneling:").grid(row=25)
    KIEtun_BM = Entry(t2, width = 10)
    KIEtun_BM.grid(row=25, column=1)
    KIEtun_BM.insert(0, "")

    Blank9 = Label(t2).grid(row=26)

    Label(t2, text = "Rigid-Rotor Method:", font="bold").grid(row=27, \
            columnspan=4)
    Label(t2, text = "KIE/EIE:").grid(row=28)
    KIE_RR= Entry(t2, width = 10)
    KIE_RR.grid(row=28, column=1)
    KIE_RR.insert(0, "")

    Label(t2, text = "KIE/EIE with tunneling:").grid(row=29)
    KIEtun_RR = Entry(t2, width = 10)
    KIEtun_RR.grid(row=29, column=1)
    KIEtun_RR.insert(0, "")

    Blank10 = Label(t2).grid(row=30)

    calc_but = Button(t2, text ="Calculate Isotope Effect", command= lambda: \
            calculate_IE_FCHK_GUI(variable1.get(), variable2.get(), \
            temp.get(), scale_factor.get(), pressure.get(), hyperchem.get(), \
            grad_dir.get(), atom_sym.get(), GS_atom_num.get(), \
            TS_atom_num.get(), iso_mass.get(), KIE_BM, KIEtun_BM, \
            KIE_RR, KIEtun_RR))
    calc_but.grid(row=21, columnspan=4)

    Blank10 = Label(t2).grid(row=22)

    return t2

def create_NMR_tab(notebook, temp):
    # Creates the NMR tab in the GUI
    # Sets up frame
    t3 = Frame(notebook, name="nmr")
    t3.grid()

    Blank1 = Label(t3).grid(row=0)

    heading = Label(t3, text=\
            "Choose directory containing NMR and thermal correction files.")
    heading.grid(row=1, columnspan=4)

    Blank2 = Label(t3).grid(row=2)

    # Directory choosing for NMR & thermal correction files
    la_nums = Label(t3, text="Select directory:")
    la_nums.grid(row=3)

    dirname = StringVar()
    dirname.set("")

    row_id_1 = 3
    dir_but = Button(t3, text="Browse", command= lambda: \
            browse_button_1(dirname, t3, row_id_1))
    dir_but.grid(row=3, column=1)

    TMS_fname = StringVar()
    TMS_fname.set("")

    std_select = Label(t3, text="Select standard: ")
    std_select.grid(row=5)

    row_id_2 = 5
    std_but = Button(t3, text="Browse", command= lambda: \
            browse_button_2(TMS_fname, t3, row_id_2))
    std_but.grid(row=5, column=1)

    nums_lbl = Label(t3, text="Select atom numbers: ")
    nums_lbl.grid(row=7)

    nums_ntry = Entry(t3, width=10)
    nums_ntry.grid(row=7, column=1)

    calc_but = Button(t3, text="Calculate NMR Shifts", command= lambda: \
            calc_shift_difference(dirname, TMS_fname, nums_ntry, temp.get()))
    calc_but.grid(row=8, columnspan=4, pady=20)

    return t3

def browse_button_1(dirname, t3, row_id):
    # Gets directory name and displays what was chosen to user
    dirname.set(fd.askdirectory())
    label_row = row_id + 1
    show_dir = Label(t3, text="Selected: " + dirname.get(), wraplength=400, \
            justify=LEFT)
    show_dir.grid(row=label_row, columnspan=4)

def browse_button_2(TMS_fname, t3, row_id):
    # Gets file name (log files) and displays what was chosen to user
    file_opt = options = {}
    options['filetypes'] = [('Log files', '.log'), ('Out files', '.out'), ('All files', '.*')]

    TMS_fname.set(askopenfilename(**file_opt))
    label_row = row_id + 1
    show_fname = Label(t3, text="Selected: " + TMS_fname.get(), \
            wraplength=500, justify=LEFT)
    show_fname.grid(row=label_row, columnspan=4)

def browse_button_3(TMS_fname, t3, row_id):
    # Gets file name (fchk files) and displays what was chosen to user
    file_opt = options = {}
    options['filetypes'] = [('Formatted checkpoint files', '.fchk'), \
            ('All files', '.*')]
            #options['filetypes'] = [('All files', '.*')]

    TMS_fname.set(askopenfilename(**file_opt))
    label_row = row_id + 1
    show_fname = Label(t3, text="Selected: " + TMS_fname.get(), \
            wraplength=500, justify=LEFT)
    show_fname.grid(row=label_row, columnspan=4)

def create_top_frame(mainframe):
    # Set up top panel (stuff not changing via tabs)
    topf = Frame(mainframe)

    # copy-pasted Alex's code of GUI setup
    Blank = Label(topf).grid(row=0)

    Label(topf, text = "Temperature (K):").grid(row=1)
    temp = Entry(topf, width = 10)
    temp.grid(row=1, column=1)
    temp.insert(0, "298.15")

    Blank2 = Label(topf).grid(row=5)

    # Scaling factor entry
    Label(topf, text = "Scaling factor:").grid(row=8)
    scale_factor = Entry(topf, width = 10)
    scale_factor.grid(row=8, column=1)
    scale_factor.insert(0, "1.0")

    Blank3 = Label(topf).grid(row=9)

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

    #Force to top
    root.lift()

    # mainloop
    root.mainloop()

# ==================================================================
#                       Freqchk Control
# ==================================================================

def run_freqchk(GS_chkpt_file, TS_chkpt_file, hyperchem_files, temp, \
        pressure, scale_factor, gradient_direction, isotope_changes, \
        number_atoms_GS, number_atoms_TS, count):
    """
        Input: Checkpoint file name and typical answers to 'freqchk'\
                prompts with the exception of changing the isotopes
        Output: 4 output files from 4 separate freqchk calculations
        Master control for setting up and running freqchk calculations
    """
    print "\n-- Running freqchk for calculation", count, "--"
    y = 0
    heading = ["GS_file", "TS_File", "Temperature", "Pressure", \
            "Scale_factor", "Chem_symbol", "GS_number", "TS_number", \
            "Labeled_isotope", "KIE", "KIE_tunneling"]
    x=0
    if len(GS_chkpt_file) > x:
        x = len(GS_chkpt_file)
    if len(TS_chkpt_file) > x:
        x = len(TS_chkpt_file)
        y += 1
    chem_sym = []
    gs_num = []
    ts_num = []
    isotope_mass = []
    output = []
    i = 0
    while i < len(isotope_changes):
        chem_sym.append(isotope_changes[i])
        gs_num.append(isotope_changes[i+1])
        ts_num.append(isotope_changes[i+2])
        isotope_mass.append(isotope_changes[i+3])
        i += 4

    # run freqchk for TS without a marker
    run_freqchk_TS_no_marker(TS_chkpt_file, hyperchem_files, temp, pressure,\
            scale_factor, gradient_direction)
    # run freqchk for TS with a marker
    run_freqchk_TS_marker(TS_chkpt_file, hyperchem_files, temp, pressure,\
            scale_factor, gradient_direction, ts_num, isotope_mass, \
            number_atoms_TS)
    # run freqchk for GS without a marker
    run_freqchk_GS_no_marker(GS_chkpt_file, hyperchem_files, temp, pressure,\
            scale_factor, gradient_direction)
    # run freqchk for GS with a marker
    run_freqchk_GS_marker(GS_chkpt_file, hyperchem_files, temp, pressure,\
            scale_factor, gradient_direction, gs_num, isotope_mass, \
            number_atoms_GS)

def run_freqchk_TS_no_marker(chkpt_file, hyperchem, temp, pressure, \
        scale_factor, gradient):
    """
        Input: Checkpoint file name and typical answers to 'freqchk' prompts \
                with the exception of changing the isotopes
        Output: file with freqchk output
        Running 'freqchk' using text file created below
    """
    iso_masses = "Yes" #forces freqchk to use natural isotopes

    #Turning a list into strings
    hyperchem = ''.join(hyperchem)
    temp = ''.join(temp)
    pressure = ''.join(pressure)
    scale_factor = ''.join(scale_factor)
    gradient = ''.join(gradient)

    # Write to a temporary text file that will act as the input to 'freqchk'
    TEMP_FREQCHK_FILE = open("temp_freqchk_file1.txt","w")
    TEMP_FREQCHK_FILE.write(chkpt_file + "\n" + hyperchem + "\n" + temp \
            + "\n" + pressure + "\n" + scale_factor + "\n" + iso_masses \
            + "\n" + gradient)
    TEMP_FREQCHK_FILE.close()

    #Run freqchk with temporary text file as input
    os.system("freqchk " + "< temp_freqchk_file1.txt" "> \
            freq_TS_no_marker.txt")

    #Remove temporary text file
    os.system("rm temp_freqchk_file1.txt")

def run_freqchk_GS_no_marker(chkpt_file, hyperchem, temp, pressure, \
        scale_factor, gradient):
    """
        Input: Checkpoint file name and typical answers to 'freqchk' prompts \
                with the exception of changing the isotopes
        Output: file with freqchk output
        Running 'freqchk' using text file created below
    """
    iso_masses = "Yes" #forces freqchk to use natural isotopes

    # Turning a list into strings
    hyperchem = ''.join(hyperchem)
    temp = ''.join(temp)
    pressure = ''.join(pressure)
    scale_factor = ''.join(scale_factor)
    gradient = ''.join(gradient)

    # Write to a temporary text file that will act as the input to 'freqchk'
    TEMP_FREQCHK_FILE = open("temp_freqchk_file2.txt","w")
    TEMP_FREQCHK_FILE.write(chkpt_file + "\n" + hyperchem + "\n" + temp \
            + "\n" + pressure + "\n" + scale_factor + "\n" + iso_masses \
            + "\n" + gradient)
    TEMP_FREQCHK_FILE.close()

    #Run freqchk with temporary text file as input
    os.system("freqchk " + "< temp_freqchk_file2.txt" "> \
            freq_GS_no_marker.txt")

    #Remove temporary text file
    os.system("rm temp_freqchk_file2.txt")

def run_freqchk_TS_marker(chkpt_file, hyperchem, temp, pressure, \
        scale_factor, gradient, atom_num, iso_mass, num_atoms):
    """
        Input: Checkpoint file name and the typical answers to 'freqchk' \
                prompts with the exception of changing the isotopes
        Output: file with freqchk output
        Creating the input for main body of code
    """
    iso_masses = "No" #forces freqchk to use changes to isotopes

    # Build the input for the changes to isotopes
    #Blanks entered for atoms that are not changing
    iso_input = []
    count = 1
    while count / (num_atoms+1) != 1:
        if count in atom_num:
            i = atom_num.index(count)
            count += 1
            iso_input.append(str(iso_mass[i]))
        else:
            count += 1
            iso_input.append("")
    iso_input = [iso_input[x:x+num_atoms] for x in xrange(0, len(iso_input), \
            num_atoms)] #'Chunks' the list into a list the length of num_atoms

    #Turning a list into strings
    for each_iso_input in iso_input:
        hyperchem = ''.join(hyperchem)
        temp = ''.join(temp)
        pressure = ''.join(pressure)
        scale_factor = ''.join(scale_factor)
        iso_masses = ''.join(iso_masses)
        gradient = ''.join(gradient)

        #Write to a temporary txt file that will act as the input to 'freqchk'
        TEMP_FREQCHK_FILE = open("temp_freqchk_file3.txt","w")
        TEMP_FREQCHK_FILE.write(chkpt_file + "\n" + hyperchem + "\n" + temp \
                + "\n" + pressure + "\n" + scale_factor + "\n" + iso_masses \
                + "\n" + "\n".join(each_iso_input) + "\n" + gradient)
        TEMP_FREQCHK_FILE.close()

        #Run freqchk with temporary text file as input
        os.system("freqchk " + "< temp_freqchk_file3.txt" "> \
                freq_TS_marker.txt")

        #Remove temporary text file
        os.system("rm temp_freqchk_file3.txt")

def run_freqchk_GS_marker(chkpt_file, hyperchem, temp, pressure, \
        scale_factor, gradient, atom_num, iso_mass, num_atoms):
    """
        Input: Checkpoint file name and the typical answers to 'freqchk' \
                prompts with the exception of changing the isotopes
        Output: file with freqchk output
        Creating the input for main body of code
    """
    iso_masses = "No" #forces freqchk to use changes to isotopes

    # Build the input for the changes to isotopes
    #Blanks entered for atoms that are not changing
    iso_input = []
    count = 1
    while count / (num_atoms+1) != 1:
        if count in atom_num:
            i = atom_num.index(count)
            count += 1
            iso_input.append(str(iso_mass[i]))
        else:
            count += 1
            iso_input.append("")
    iso_input = [iso_input[x:x+num_atoms] for x in xrange(0, len(iso_input), \
            num_atoms)] #'Chunks' the list into a list the length of num_atoms

    #Turning a list into strings
    for each_iso_input in iso_input:
        hyperchem = ''.join(hyperchem)
        temp = ''.join(temp)
        pressure = ''.join(pressure)
        scale_factor = ''.join(scale_factor)
        iso_masses = ''.join(iso_masses)
        gradient = ''.join(gradient)

        #Write to a temporary txt file that will act as the input to 'freqchk'
        TEMP_FREQCHK_FILE = open("temp_freqchk_file4.txt","w")
        TEMP_FREQCHK_FILE.write(chkpt_file + "\n" + hyperchem + "\n" + temp \
                + "\n" + pressure + "\n" + scale_factor + "\n" + iso_masses \
                + "\n" + "\n".join(each_iso_input) + "\n" + gradient)
        TEMP_FREQCHK_FILE.close()

        #Run freqchk with temporary text file as input
        os.system("freqchk " + "< temp_freqchk_file4.txt" "> \
                freq_GS_marker.txt")

        #Remove temporary text file
        os.system("rm temp_freqchk_file4.txt")

# ==================================================================
#           Calculate IE using Bigeleisen-Mayer Method
# ==================================================================

def calc_IE_Bigeleisen(GS_unlabeled, GS_labeled, TS_unlabeled, TS_labeled, \
        temp, scale_factor, count):
    """
        Input: 4 log files/output file from freqchk, temperature, \
                scaling factor, and the calculation number
        Output: Isotope effect using the Bigeleisen-Mayer equation
        Isotope effect = SYM x MMI x EXC x ZPE
    """
    temp = float(temp)

    #get frequencies from .txt file
    print "-- Parsing data for BM calculation", count, "--"
    frequency_TS_natural = get_data_Bigeleisen(TS_unlabeled)
    frequency_TS_isotope = get_data_Bigeleisen(TS_labeled)
    frequency_GS_natural = get_data_Bigeleisen(GS_unlabeled)
    frequency_GS_isotope = get_data_Bigeleisen(GS_labeled)

    # scale frequencies by scaling factor
    scaled_freq_TS_natural = scale_freq(frequency_TS_natural, scale_factor)
    scaled_freq_TS_isotope = scale_freq(frequency_TS_isotope, scale_factor)
    scaled_freq_GS_natural = scale_freq(frequency_GS_natural, scale_factor)
    scaled_freq_GS_isotope = scale_freq(frequency_GS_isotope, scale_factor)

    #get molecular mass
    mol_mass_TS_natural = float(get_mol_mass(TS_unlabeled))
    mol_mass_TS_isotope = float(get_mol_mass(TS_labeled))
    mol_mass_GS_natural = float(get_mol_mass(GS_unlabeled))
    mol_mass_GS_isotope = float(get_mol_mass(GS_labeled))

    #get rotational symmetry number
    rot_sym_TS_natural = float(get_rot_sym(TS_unlabeled))
    rot_sym_TS_isotope = float(get_rot_sym(TS_labeled))
    rot_sym_GS_natural = float(get_rot_sym(GS_unlabeled))
    rot_sym_GS_isotope = float(get_rot_sym(GS_labeled))

    print "-- Manipulating data to get IE for BM calculation", count, "--"
    #create array with u values
    u_TS_natural = np.array(calc_u(scaled_freq_TS_natural, temp))
    u_TS_isotope = np.array(calc_u(scaled_freq_TS_isotope, temp))
    u_GS_natural = np.array(calc_u(scaled_freq_GS_natural, temp))
    u_GS_isotope = np.array(calc_u(scaled_freq_GS_isotope, temp))
    if u_TS_natural[0] < 0:
        u_neg_TS_natural= u_TS_natural[0] # negative u value
        u_TS_natural = u_TS_natural[1:] # all positive u values
        u_neg_TS_isotope = u_TS_isotope[0] # negative u value
        u_TS_isotope = u_TS_isotope[1:] # all positive u values
    else:
        u_neg_TS_natural = []
        u_neg_TS_isotope = []

    # calculate SYM value
    SYM = calc_SYM(rot_sym_TS_natural, rot_sym_TS_isotope, \
            rot_sym_GS_natural, rot_sym_GS_isotope)

    # calculate MMI value using frequencies
    mass_dep = calc_mass_dep(mol_mass_TS_natural, mol_mass_TS_isotope, \
            mol_mass_GS_natural, mol_mass_GS_isotope)
    VP = calc_VP(scaled_freq_TS_natural, scaled_freq_TS_isotope, \
            scaled_freq_GS_natural, scaled_freq_GS_isotope)
    MMI = mass_dep * VP

    # calculate ZPE value
    sum_u_GS_natural = sum(u_GS_natural)
    sum_u_TS_natural = sum(u_TS_natural)
    sum_u_GS_isotope = sum(u_GS_isotope)
    sum_u_TS_isotope = sum(u_TS_isotope)
    ZPE = calc_ZPE_BM(sum_u_GS_natural, sum_u_TS_natural, sum_u_GS_isotope, \
            sum_u_TS_isotope)

    # calculate EXC value
    prod_GS_unlabaeled = calc_exc_terms(u_GS_natural)
    prod_TS_unlabaeled = calc_exc_terms(u_TS_natural)
    prod_GS_labaeled = calc_exc_terms(u_GS_isotope)
    prod_TS_labaeled = calc_exc_terms(u_TS_isotope)
    EXC = calc_EXC(prod_GS_unlabaeled, prod_TS_unlabaeled, prod_GS_labaeled, \
            prod_TS_labaeled)

    # calculate Bell tunneling corrections
    if u_neg_TS_natural:
        qt_TS_natural = calc_qt(u_neg_TS_natural)
        qt_TS_isotope = calc_qt(u_neg_TS_isotope)
    else:
        qt_TS_natural = calc_qt(u_TS_natural[0])
        qt_TS_isotope = calc_qt(u_TS_isotope[0])

    # calculate KIE
    isotope_effect = SYM * MMI * ZPE * EXC
    isotope_effect_tunneling = isotope_effect * qt_TS_natural / qt_TS_isotope

    print "-- Isotope effect successfully calculated for BM calculation", \
            count, "--", '\n'

    isotope_effect = round(isotope_effect, 4)
    isotope_effect_tunneling = round(isotope_effect_tunneling, 4)
    SYM = round(SYM, 4)
    MMI = round(MMI, 4)
    ZPE = round(ZPE, 4)
    EXC = round(EXC, 4)

    return isotope_effect, isotope_effect_tunneling, SYM, MMI, ZPE, EXC

def get_data_Bigeleisen(log_file_name):
    """
        Input: Log file or txt output file from freqchk
        Output: A list of all frequencies
    """
    frequency = []
    with open(log_file_name, 'r+') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if "Frequencies" in line:
                # ['Frequencies', '--', '#', '#', '#']
                frequency.extend(line.split())
                # ['--', '#', '#', '#']
                frequency.remove('Frequencies')
                # ['#', '#', '#']
                frequency.remove('--')
    return frequency

def scale_freq(frequencies, scale_factor):
    """
        Input: Frequencies and scaling factor
        Output: Scaled frequencies
    """
    scale_factor = float(scale_factor)
    scaled_frequencies = []
    for each_freq in frequencies:
        each_freq = float(each_freq)
        math = each_freq * scale_factor
        scaled_frequencies.append(math)
    return scaled_frequencies

def get_mol_mass(filename):
    """
        Input: Log file or txt output file from freqchk
        Output: Molecular mass for the given file
    """
    mol_mass_line = []
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if "Molecular mass: " in line:
                mol_mass_line.extend(line.split())
                mol_mass = mol_mass_line[2].split(".")
                mol_mass = mol_mass[0]
    return mol_mass

def get_rot_sym(filename):
    """
        Input: Log file or txt output file from freqchk
        Output: Rotational symmetry number
        Typically '1'
    """
    rot_sym_line = []
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if "Rotational symmetry number " in line:
                rot_sym_line.extend(line.split())
                rot_sym = rot_sym_line[3].split(".")
                rot_sym = rot_sym[0]
    return rot_sym

def calc_SYM(rot_sym_TS_natural, rot_sym_TS_isotope, rot_sym_GS_natural, \
        rot_sym_GS_isotope):
    """
        Input: Rotational symmetry numbers for all 4 structures
        Output: SYM value in the calculation of the isotope effect
        IE = SYM x MMI x EXC x ZPE
        SYM typically '1'
    """
    numerator = rot_sym_GS_natural / rot_sym_GS_isotope
    denominator = rot_sym_TS_natural / rot_sym_TS_isotope
    SYM = numerator / denominator
    return SYM

def calc_mass_dep(mol_mass_TS_natural, mol_mass_TS_isotope, \
        mol_mass_GS_natural, mol_mass_GS_isotope):
    """
        Input: Molecular mass for all 4 strucutres
        Output: Mass dependency value for the calculation of the MMI term
        IE = SYM x MMI x EXC x ZPE
        MMI = mass. dep. * VP
    """
    numerator = (mol_mass_TS_natural * mol_mass_GS_isotope)
    denominator = (mol_mass_TS_isotope * mol_mass_GS_natural)
    division = numerator / denominator
    mass_dep = (division)**(3/2)
    return mass_dep

def calc_VP(scaled_freq_TS_natural, scaled_freq_TS_isotope, \
        scaled_freq_GS_natural, scaled_freq_GS_isotope):
    """
        Input: Scaled frequencies for all 4 structures
        Output: VP values for the calculation of the MMI term
        IE = SYM x MMI x EXC x ZPE
        MMI = mass. dep. * VP
    """
    div_GS = []
    div_TS = []
    for i in range(0, len(scaled_freq_GS_natural)):
        divide_GS = scaled_freq_GS_isotope[i] / scaled_freq_GS_natural[i]
        div_GS.append(divide_GS)
    for j in range(0, len(scaled_freq_TS_natural)):
        divide_TS = scaled_freq_TS_isotope[j] / scaled_freq_TS_natural[j]
        div_TS.append(divide_TS)
    prod_GS = np.prod(div_GS)
    prod_TS = np.prod(div_TS)
    VP = prod_GS / prod_TS
    return VP

def calc_ZPE_BM(sum_u_GS_natural, sum_u_TS_natural, sum_u_GS_isotope, \
        sum_u_TS_isotope):
    """
        Input: The sum of the u values for all 4 structures
        Output: ZPE term for calculation of the isotope effect
        IE = SYM x MMI x EXC x ZPE
        Note: mt.exp(x) is equivalent to =EXP(x) in Excel. Sometimes, \
        ZPE appraches zero. The rigid-rotor method is unreliable in \
        these cases (IE = 0.0), so use the BM method.
    """
    fragment1 = sum_u_TS_natural - sum_u_GS_natural
    fragment2 = sum_u_TS_isotope - sum_u_GS_isotope
    numerator = mt.exp(-0.5*fragment1)
    denominator = mt.exp(-0.5*fragment2)
    try:
        ZPE = numerator / denominator
    except ZeroDivisionError:
        ZPE = 0
    return ZPE

def calc_exc_terms(u_values):
    """
        Input: The u values for an independent structure
        Output: EXC terms for an independent structure
        IE = SYM x MMI x EXC x ZPE
    """
    exc_terms = []
    for each_u in u_values:
        ind_term = 1/(1-mt.exp(-each_u))
        exc_terms.append(ind_term)
    prod = np.prod(exc_terms)
    return prod

def calc_EXC(prod_GS_unlabaeled, prod_TS_unlabaeled, prod_GS_labaeled, \
        prod_TS_labaeled):
    """
        Input: EXC terms for each independent structure (see calc_exc_terms)
        Output: EXC term for the calculation of the isotope effect
        IE = SYM x MMI x EXC x ZPE
    """
    numerator = prod_TS_unlabaeled / prod_GS_unlabaeled
    denominator = prod_TS_labaeled / prod_GS_labaeled
    EXC = numerator / denominator
    return EXC

# ==================================================================
#               Calculate IE using Rigid-Rotor Method
# ==================================================================

def calc_IE_rigid_rotor_method(GS_unlabeled, GS_labeled, TS_unlabeled, \
        TS_labeled, temp, scale_factor, count):
    """
        Input: 4 log files/output file from freqchk, temperature, \
                scaling factor, and the calculation number
        Output: Isotope effect using the rigid-rotor equation (ddH,ddS)
        Isotope effect = ddH * ddS
        dd = "delta delta"
    """
    #Constants
    h = 6.6262e-34
    c = 2.9979e10
    k = 1.3807e-23
    R = 1.9872e-3
    kcal = 4184
    Rjoule = 8.314
    Rcal = 1.9872
    temp = float(temp)

    print "-- Parsing data for RR calculation", count, "--"
    #Extract frequencies from log file
    frequencies_TS_unlabeled, rot_temp_TS_unlabeled, \
            rot_sym_TS_unlabeled = get_data_RR(TS_unlabeled)
    frequencies_TS_labeled, rot_temp_TS_labeled, \
            rot_sym_TS_labeled = get_data_RR(TS_labeled)
    frequencies_GS_unlabeled, rot_temp_GS_unlabeled, \
            rot_sym_GS_unlabeled = get_data_RR(GS_unlabeled)
    frequencies_GS_labeled, rot_temp_GS_labeled, \
            rot_sym_GS_labeled = get_data_RR(GS_labeled)

    # scale frequencies by scaling factor
    scaled_freq_TS_unlabeled = scale_freq(frequencies_TS_unlabeled, \
            scale_factor)
    scaled_freq_TS_labeled = scale_freq(frequencies_TS_labeled, \
            scale_factor)
    scaled_freq_GS_unlabeled = scale_freq(frequencies_GS_unlabeled, \
            scale_factor)
    scaled_freq_GS_labeled = scale_freq(frequencies_GS_labeled, \
            scale_factor)

    #if scaled_freq_TS_unlabeled[0] < 0:
        #neg_frequency_unlabeled = scaled_freq_TS_unlabeled[0]
        #neg_frequency_labeled = scaled_freq_TS_labeled[0]
    #else:
        #neg_frequency_unlabeled = []
        #neg_frequency_labeled = []

    u_GS_unlabeled = np.array(calc_u(scaled_freq_GS_unlabeled, temp))
    u_GS_labeled = np.array(calc_u(scaled_freq_GS_labeled, temp))
    u_TS_unlabeled = np.array(calc_u(scaled_freq_TS_unlabeled, temp))
    u_TS_labeled = np.array(calc_u(scaled_freq_TS_labeled, temp))
    if u_TS_unlabeled[0] < 0:
        u_neg_TS_unlabeled = u_TS_unlabeled[0] # negative u value
        u_TS_unlabeled = u_TS_unlabeled[1:] # all positive u values
        u_neg_TS_labeled = u_TS_labeled[0] # negative u value
        u_TS_labeled = u_TS_labeled[1:] # all positive u values
    else:
        u_neg_TS_unlabeled = []
        u_neg_TS_labeled = []

    #Removing neg frequency from calculations
    if scaled_freq_TS_unlabeled[0] < 0 and scaled_freq_TS_labeled[0] < 0:
        scaled_freq_TS_unlabeled = scaled_freq_TS_unlabeled[1:]
        scaled_freq_TS_labeled = scaled_freq_TS_labeled[1:]
        KIE_or_EIE = 1
    else:
        KIE_or_EIE = 2

    print "-- Manipulating data to get IE for RR calculation", count, "--"
    #Calculate ddH(ZPE)
    ZPE_GS_unlabeled = calc_ZPE_RR(scaled_freq_GS_unlabeled, h, c, Rjoule, \
            k, kcal)
    ZPE_GS_labeled = calc_ZPE_RR(scaled_freq_GS_labeled, h, c, Rjoule, \
            k, kcal)
    ZPE_TS_unlabeled = calc_ZPE_RR(scaled_freq_TS_unlabeled, h, c, Rjoule, \
            k, kcal)
    ZPE_TS_labeled = calc_ZPE_RR(scaled_freq_TS_labeled, h, c, Rjoule, \
            k, kcal)
    GS_unlabeled_component = sum(ZPE_GS_unlabeled)
    GS_labeled_component = sum(ZPE_GS_labeled)
    TS_unlabeled_component = sum(ZPE_TS_unlabeled)
    TS_labeled_component = sum(ZPE_TS_labeled)
    ZPE = (TS_labeled_component - GS_labeled_component) - \
            (TS_unlabeled_component - GS_unlabeled_component)
    ZPE = mt.exp(ZPE/(R*temp))

    #Calculate ddH(vib)
    VIB_GS_unlabeled = calc_VIB(R, h, c, scaled_freq_GS_unlabeled, k, temp)
    VIB_GS_labeled = calc_VIB(R, h, c, scaled_freq_GS_labeled, k, temp)
    VIB_TS_unlabeled = calc_VIB(R, h, c, scaled_freq_TS_unlabeled, k, temp)
    VIB_TS_labeled = calc_VIB(R, h, c, scaled_freq_TS_labeled, k, temp)
    GS_unlabeled_VIB_component = sum(VIB_GS_unlabeled)
    GS_labeled_VIB_component = sum(VIB_GS_labeled)
    TS_unlabeled_VIB_component = sum(VIB_TS_unlabeled)
    TS_labeled_VIB_component = sum(VIB_TS_labeled)
    Hvib = (TS_labeled_VIB_component - GS_labeled_VIB_component) - \
            (TS_unlabeled_VIB_component- GS_unlabeled_VIB_component)
    Hvib = mt.exp(Hvib/(R*temp))

    #Calculate ddS(vib)
    GS_unlabeled_Svib = calc_svib_comp(u_GS_unlabeled, Rcal)
    GS_labeled_Svib = calc_svib_comp(u_GS_labeled, Rcal)
    TS_unlabeled_Svib = calc_svib_comp(u_TS_unlabeled, Rcal)
    TS_labeled_Svib = calc_svib_comp(u_TS_labeled, Rcal)
    Svib = (TS_unlabeled_Svib - GS_unlabeled_Svib) - \
            (TS_labeled_Svib - GS_labeled_Svib)
    Svib = mt.exp(Svib/Rcal)

    #Calculate ddS(rot)
    Srot_GS_unlabeled = calc_Srot(rot_temp_GS_unlabeled, \
            rot_sym_GS_unlabeled, Rcal, temp)
    Srot_GS_labeled = calc_Srot(rot_temp_GS_labeled, \
            rot_sym_GS_labeled, Rcal, temp)
    Srot_TS_unlabeled = calc_Srot(rot_temp_TS_unlabeled, \
            rot_sym_TS_unlabeled, Rcal, temp)
    Srot_TS_labeled = calc_Srot(rot_temp_TS_labeled, \
            rot_sym_TS_labeled, Rcal, temp)
    Srot = (Srot_TS_unlabeled - Srot_GS_unlabeled) - \
            (Srot_TS_labeled - Srot_GS_labeled)
    Srot = mt.exp(Srot/Rcal)

    #Calculate ddH(thermal)
    Hthermal = ZPE * Hvib
    ddS = Svib * Srot

    # calculate tunneling correction
    if u_neg_TS_unlabeled:
        qt_TS_unlabeled = calc_qt(u_neg_TS_unlabeled)
        qt_TS_labeled = calc_qt(u_neg_TS_labeled)
    else:
        qt_TS_unlabeled = calc_qt(u_TS_unlabeled[0])
        qt_TS_labeled = calc_qt(u_TS_labeled[0])

    isotope_effect = Hthermal * ddS
    isotope_effect = round(isotope_effect, 4)
    isotope_effect_tunn = isotope_effect * qt_TS_unlabeled / qt_TS_labeled
    isotope_effect_tunn = round(isotope_effect_tunn, 4)

    print "-- Isotope effect successfully calculated for RR calculation", \
            count, "--"

    Hthermal = round(Hthermal, 4)
    ddS = round(ddS, 4)

    return isotope_effect, isotope_effect_tunn, KIE_or_EIE, Hthermal, ddS

def get_data_RR(log_file_name):
    """
        Input: Log file or output file from freqchk
        Output: Frequencies, rotational temperatures, \
                and rotational symmetry numbers
    """
    frequency = []
    rot_temp = []
    rot_sym = []

    with open(log_file_name, 'r+') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if "Frequencies" in line:
                # ['Frequencies', '--', '#', '#', '#']
                frequency.extend(line.split())
                # ['--', '#', '#', '#']
                frequency.remove('Frequencies')
                # ['#', '#', '#']
                frequency.remove('--')
            if "Rotational temperatures" in line:
                rot_temp.extend(line.split())
                rot_temp.remove('Rotational')
                rot_temp.remove('temperatures')
                rot_temp.remove('(Kelvin)')
            if "Rotational symmetry number" in line:
                rot_sym.extend(line.split())
                rot_sym_num = rot_sym[3].split(".")
                rot_sym_num = float(rot_sym_num[0])

    return frequency, rot_temp, rot_sym_num

def calc_ZPE_RR(frequencies, h, c, Rjoule, k, kcal):
    """
        Input: Frequencies and several constants
        Output: H(ZPE) component of the isotope effect
        H(thermal) = H(ZPE) + H(vib)
    """
    ZPE_component = []
    for each_freq in frequencies:
        numerator = h * c * float(each_freq) * Rjoule
        denominator = k * kcal
        division = 0.5 * (numerator / denominator)
        ZPE_component.append(division)
    return ZPE_component

def calc_VIB(R, h, c, frequencies, k, temp):
    """
        Input: Frequencies, temperature, and several constants
        Output: H(vib) component of the isotope effect
        H(thermal) = H(ZPE) + H(vib)
    """
    vib_combonent = []
    for each_freq in frequencies:
        each_freq = float(each_freq)
        fragment1 = (h * c * each_freq)/k
        fragment2 = (h * c * each_freq) / k
        fragment3 = (fragment2 / temp)
        expfrag = mt.exp(fragment3) - 1
        final = R * (fragment1 / expfrag)
        vib_combonent.append(final)
    return vib_combonent

def calc_svib_comp(u_values, Rcal):
    """
        Input: u values for an individual structure and a constant
        Output: The S(vib) component for an individual structure
        S = S(vib) + S(rot)
    """
    svib_comp = []
    for each_u in u_values:
        fragment1 = each_u/(mt.exp(each_u)-1)
        fragment2 = mt.log(1-mt.exp(-each_u))
        subtract = fragment1 - fragment2
        final = Rcal * subtract
        svib_comp.append(final)
    final_svib_comp = sum(svib_comp)
    return final_svib_comp

def calc_Srot(rot_temp, rot_sym, Rcal, temp):
    """
        Input: Rotational temperatures, rotational symmetry numbers, \
                temperature, and a constant
        Output: The S(rot) component for an individual structure
        S = S(vib) + S(rot)
    """
    fragment1 = mt.sqrt(mt.pi)/rot_sym
    fragment2 = (temp**1.5)/(mt.sqrt(float(rot_temp[0]) * \
            float(rot_temp[1]) * float(rot_temp[2])))
    mult = fragment1 * fragment2
    log = mt.log(mult) + 1.5
    Srot = Rcal * log
    return Srot

# ==================================================================
#                       Shared IE functions
# ==================================================================

def calc_u(frequency, temp):
    """
    Input: array with frequencies (see get_data module)
    Output: values of u
    u = h*(frequency) / kT
    """
    temp = float(temp) #Makes integer
    h = 6.6262E-34
    c = 2.9979e10
    k = 1.3807E-23

    hKT = h*c/(k*temp)

    u = []
    for each_freq in frequency:
        u = [float(x) * hKT for x in frequency]
    return u

def calc_qt(u):
    """
        Input: u array
        Output: Bell tunneling correction
    """
    qt = u/2 #(u/2)/sin(u/2) where u is the negative u value
    sine_qt = u/2
    sine_qt = mt.sin(sine_qt)
    qt = qt/sine_qt
    return qt

def print_results_FREQ(master_output, KIE_or_EIE):
    """
        Input: List with all necessary information
        Output: Printing results to the screen
    """
    index = 0
    count = []
    GS_file = []
    TS_file = []
    temp = []
    scale_factor = []
    IE_BM = []
    IE_tunneling_BM = []
    IE_RR = []
    IE_tunneling_RR = []
    isotope_changes = []
    SYM = []
    MMI = []
    EXC = []
    ZPE = []
    ddH = []
    ddS = []
    for i in range(0,len(master_output)/16):
        count.append(str(master_output[index]))
        index += 1
        GS_file.append(str(master_output[index]))
        index += 1
        TS_file.append(str(master_output[index]))
        index += 1
        temp.append(float(master_output[index]))
        index += 1
        scale_factor.append(float(master_output[index]))
        index += 1
        IE_BM.append(str(master_output[index]))
        index += 1
        IE_tunneling_BM.append(str(master_output[index]))
        index += 1
        IE_RR.append(str(master_output[index]))
        index += 1
        IE_tunneling_RR.append(str(master_output[index]))
        index += 1
        isotope_changes.append(master_output[index])
        index += 1
        SYM.append(float(master_output[index]))
        index += 1
        MMI.append(float(master_output[index]))
        index += 1
        EXC.append(float(master_output[index]))
        index += 1
        ZPE.append(float(master_output[index]))
        index += 1
        ddH.append(float(master_output[index]))
        index += 1
        ddS.append(float(master_output[index]))
        index += 1

    print "\nRESULTS:"
    if KIE_or_EIE == 1:
        abbreviation = "KIE"
    elif KIE_or_EIE == 2:
        abbreviation = "EIE"
    step = 0
    for i in range(0,len(GS_file)):
        k = 0
        GS_num_list = []
        TS_num_list = []
        while k < len(isotope_changes[step]):
            GS_num_list.append(isotope_changes[step][k])
            GS_num_list.append(str(isotope_changes[step][k+1]))

            TS_num_list.append(isotope_changes[step][k])
            TS_num_list.append(str(isotope_changes[step][k+2]))
            k += 4
        GS_num_iter = iter(GS_num_list)
        GS_num = [c+next(GS_num_iter, '') for c in GS_num_iter]
        TS_num_iter = iter(TS_num_list)
        TS_num = [c+next(TS_num_iter, '') for c in TS_num_iter]
        spacer = "=========================================================="
        print spacer + " Calculation " + count[step] + " " + spacer
        print '\n\t', "Temperature:", '\t\t', "{T:.2f}".format(T=temp[step])
        print '\t', "Scale factor:", '\t\t', "{S:.2f}".\
                format(S=scale_factor[step])
        if KIE_or_EIE == 1:
            print '\t', "GS_file:", '\t\t', GS_file[step]
            print '\t', "TS_file:", '\t\t', TS_file[step]
            print '\t', "GS_atom_number(s):", '\t', ", ".join(GS_num)
            print '\t', "TS_atom_number(s):", '\t', ", ".join(TS_num)
        elif KIE_or_EIE == 2:
            print '\t', "File1:", '\t\t\t', GS_file[step]
            print '\t', "File2:", '\t\t\t', TS_file[step]
            print '\t', "File1_atom_number(s):", '\t', ", ".join(GS_num)
            print '\t', "File2_atom_number(s):", '\t', ", ".join(TS_num)

        print "\n\nBM (" + abbreviation + ") = SYM x MMI x EXC x ZPE"
        print "SYM", '\t\t', "MMI", '\t\t', "EXC", '\t\t', "ZPE", '\t\t', \
                abbreviation, '\t\t', abbreviation+"_tunneling"
        print "------------------------------------------------------------" +\
                "---------------------------------"
        print SYM[step], '\t\t', MMI[step], '\t\t', EXC[step], '\t\t', \
                ZPE[step], '\t\t', bcolors.GREEN + IE_BM[step] + bcolors.ENDC,\
                '\t\t', bcolors.PURPLE + IE_tunneling_BM[step] + bcolors.ENDC
        print "------------------------------------------------------------" +\
                "---------------------------------\n"
        print "RR (" + abbreviation + ") = ddH x ddS"
        print "ddH", '\t\t', "ddS", '\t\t', abbreviation, '\t\t', \
                abbreviation+"_tunneling"
        print "-------------------------------------------------------------"
        print ddH[step], '\t\t', ddS[step], '\t\t', bcolors.GREEN + \
                IE_RR[step] + bcolors.ENDC, '\t\t', bcolors.PURPLE + \
                IE_tunneling_RR[step] + bcolors.ENDC
        print "-------------------------------------------------------------"
        print "\n"
        step += 1

def print_results_LOG(master_output, KIE_or_EIE):
    """
        Input: List with all necessary information
        Output: Printing results to the screen
    """
    index = 0
    count = []
    GS_file_unlabeled = []
    GS_file_labeled = []
    TS_file_unlabeled = []
    TS_file_labeled = []
    temp = []
    scale_factor = []
    IE_BM = []
    IE_tunneling_BM = []
    IE_RR = []
    IE_tunneling_RR = []
    SYM = []
    MMI = []
    EXC = []
    ZPE = []
    ddH = []
    ddS = []
    for i in range(0,len(master_output)/17):
        count.append(str(master_output[index]))
        index += 1
        GS_file_unlabeled.append(str(master_output[index]))
        index += 1
        GS_file_labeled.append(str(master_output[index]))
        index += 1
        TS_file_unlabeled.append(str(master_output[index]))
        index += 1
        TS_file_labeled.append(str(master_output[index]))
        index += 1
        temp.append(float(master_output[index]))
        index += 1
        scale_factor.append(float(master_output[index]))
        index += 1
        IE_BM.append(str(master_output[index]))
        index += 1
        IE_tunneling_BM.append(str(master_output[index]))
        index += 1
        IE_RR.append(str(master_output[index]))
        index += 1
        IE_tunneling_RR.append(str(master_output[index]))
        index += 1
        SYM.append(float(master_output[index]))
        index += 1
        MMI.append(float(master_output[index]))
        index += 1
        EXC.append(float(master_output[index]))
        index += 1
        ZPE.append(float(master_output[index]))
        index += 1
        ddH.append(float(master_output[index]))
        index += 1
        ddS.append(float(master_output[index]))
        index += 1

    print "\nRESULTS:"
    if KIE_or_EIE == 1:
        abbreviation = "KIE"
    elif KIE_or_EIE == 2:
        abbreviation = "EIE"
    step = 0
    for i in range(0,len(GS_file_unlabeled)):
        spacer = "=========================================================="
        print spacer + " Calculation " + count[step] + " " + spacer
        print '\n\t', "Temperature:", '\t\t', "{T:.2f}".format(T=temp[step])
        print '\t', "Scale factor:", '\t\t', "{S:.2f}".\
                format(S=scale_factor[step])
        if KIE_or_EIE == 1:
            print '\t', "GS_file_unlabeled:", '\t', GS_file_unlabeled[step]
            print '\t', "GS_file_labeled:", '\t', GS_file_labeled[step]
            print '\t', "TS_file_unlabeled:", '\t', TS_file_unlabeled[step]
            print '\t', "TS_file_labeled:", '\t', TS_file_labeled[step]
        elif KIE_or_EIE == 2:
            print '\t', "File1_unlabeled:", '\t', GS_file_unlabeled[step]
            print '\t', "File1_labeled:", '\t\t', GS_file_labeled[step]
            print '\t', "File2_unlabeled:", '\t', TS_file_unlabeled[step]
            print '\t', "File2_labeled:", '\t\t', TS_file_labeled[step]

        print "\n\nBM (" + abbreviation + ") = SYM x MMI x EXC x ZPE"
        print "SYM", '\t\t', "MMI", '\t\t', "EXC", '\t\t', "ZPE", '\t\t', \
                abbreviation, '\t\t', abbreviation+"_tunneling"
        print "------------------------------------------------------------" +\
                "---------------------------------"
        print SYM[step], '\t\t', MMI[step], '\t\t', EXC[step], '\t\t', \
                ZPE[step], '\t\t', bcolors.GREEN + IE_BM[step] + bcolors.ENDC,\
                '\t\t', bcolors.PURPLE + IE_tunneling_BM[step] + bcolors.ENDC
        print "------------------------------------------------------------" +\
                "---------------------------------\n"
        print "RR (" + abbreviation + ") = ddH x ddS"
        print "ddH", '\t\t', "ddS", '\t\t', abbreviation, '\t\t', \
                abbreviation+"_tunneling"
        print "-------------------------------------------------------------"
        print ddH[step], '\t\t', ddS[step], '\t\t', bcolors.GREEN + \
                IE_RR[step] + bcolors.ENDC, '\t\t', bcolors.PURPLE + \
                IE_tunneling_RR[step] + bcolors.ENDC
        print "-------------------------------------------------------------"
        print "\n"
        step += 1

# ==================================================================
#                       NMR Calculations
# ==================================================================

def get_therm_vals(log_file_name, path):
    """
        Extracts ZPVE, U, H, G, & T in kcal/mol & K from the given log file
    """
    with open(os.path.join(path, log_file_name), 'r+') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if  "Zero-point correction" in line:
                ZPVE = line.split()[2]
            if "correction to Energy" in line:
                U = line.split()[4]
            if "correction to Enthalpy" in line:
                H = line.split()[4]
            if "correction to Gibbs" in line:
                G = line.split()[6]
            if "Temperature   " in line:
                T = line.split()[1]
            # if "and zero" in line:
            #   SCF = float(line.split()[6]) - float(ZPVE)
    # therm_vals = map(float, [SCF, ZPVE, U, H, G])
    # No SCF in the Kolin files I used

    therm_vals = map(float, [ZPVE, U, H, G])

    # Converting from Hartrees/mol to kcal/mol
    c = 627.5095
    therm_vals = map(lambda x: x*c, therm_vals)
    therm_vals.append(float(T))

    return therm_vals

def get_shielding(atom_numbers, log_file_name, path):
    """
        Extracts the shielding values for the specified atoms from the given \
                log file
    """
    shielding = []
    with open(os.path.join(path, log_file_name), 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            for i in range(0,len(atom_numbers)):
                if str(atom_numbers[i]) + "  " + "H    I"in line:
                    shielding.append(line.split()[4])
    return shielding

# Files must follow naming convention "base_name_rot1_therm.log" & \
#"base_name_rot1_nmr.log"
# "base_name_rot2_therm.log, etc."
# Still working on proper differentiation of rotamers!
def parse_file_names(directory):
    """
        Returns two lists containing all the thermo files and all the nmr files 
        (respectively) in the selected directory
    """
    t_files = []
    nmr_files = []

    # Get log files from selected directory
    log_files = find_log_files(directory.get())

    # Sorts _nmr & _therm files
    for n in range(0, len(log_files)):
        if '_therm' in log_files[n]:
            t_files.append(log_files[n])
        if '_nmr' in log_files[n] and 'tms' not in log_files[n]:
            # don't add tms file to list
            nmr_files.append(log_files[n])

    return t_files, nmr_files

def calc_values(t_files, nmr_files, atom_nums, path):
    """
        Given the list of thermo & nmr files, atom numbers for which to get\
                the shielding of, and the path of the files, returns a list\
                containing lists of thermo values for each rotamer and a \
                list of shielding values for selected atoms
    """
    t_vals = []
    nmr_vals = []

    for i in t_files:
        t_vals.append(get_therm_vals(i, path))

    # Should only have one nmr file, right?
    nmr_vals = get_shielding(atom_nums, nmr_files[0], path)

    return t_vals, nmr_vals

def calc_shift_difference(directory, TMS_fname, atom_nums, temp):
    temp = float(temp)

    # Gets file names from chosen directory
    tnames, nnames = parse_file_names(directory)

    # converts entered atom numbers to ints
    atom_nums = map(int, atom_nums.get().split())

    # Gets thermo values & nmr values for files
    tvals, nvals = calc_values(tnames, nnames, atom_nums, directory.get())

    # tvals is a list where each element is a list of therm\
            #values (ZPVE, U, H, G, & T in kcal/mol & K)
    # corresponding to the different rotamers

    # nvals is a list of shielding values for chosen atom nums

    # Gets TMS value (chose 12 randomly, all Hs have same shielding value)
    TMS = float(get_shielding([12], TMS_fname.get(), directory.get())[0])

    # Convert shielding values (str --> float)
    nvals = map(float, nvals)

    # Subtract TMS val to get shift
    for n in range(0, len(nvals)):
        nvals[n] = abs(nvals[n] - TMS)

    # Extract Gs from each rotamer
    Gs = []
    for i in tvals:
        for j in range(0,len(i)):
            if j == 3:
                Gs.append(i[j])

    # Calculate delta Gs, Nj, N, & populations
    delGs = calc_delGs(Gs)

    # Calculate pops for each temperature interval
    #min_temp = float(min_temp)
    #max_temp = float(max_temp)
    #step_size = float(step_size)

    #step = ((max_temp - min_temp) / step_size) + 1
    #interval = np.linspace(min_temp, max_temp, num=step)


    #for x in interval:
    Njs, N = calc_Njs_N(delGs, temp)
    pops = calc_pops(Njs, N)
    Hr, Hs = Hr_Hs_calc(pops, nvals)
    print str(temp) + " K"
    print "Hr: " + str(Hr) + " ppm"
    print "Hs: " + str(Hs) + " ppm"
    print "Hr - Hs: " + str(Hr - Hs) + " ppm"

def calc_delGs(Gs):
    delGs = []
    for x in Gs:
        delGs.append(x - Gs[0])
    return delGs

def calc_Njs_N(delGs, T):
    Njs = [1] # Nj_d20 is 1, start with it inside the list
    for x in delGs[1:]:
        Njs.append(mt.exp(-x/T/0.0019872))
    N = sum(Njs)
    return Njs, N

def calc_pops(Njs, N):
    pops = []
    for x in Njs:
        pops.append(x/N)
    return pops

def Hr_Hs_calc(pops, shifts):
    # Need to calculate:
    # pop_20 * shift_21 + pop_22 * shift_20 + pop_21 * shift_22
    # pop_20 * shift_22 + pop_22 * shift_21 + pop_21 * shift 20

    # Making shifts into cycle for easier iteration for calculation
    shif_c = itertools.cycle(shifts)
    next(shif_c)

    # Flipping the position of these for calculation
    pops[1], pops[2] = pops[2], pops[1]

    r_vals = []
    s_vals = []
    for n in pops:
        r_vals.append(n * next(shif_c))
        s_vals.append(n * next(shif_c))

    return sum(r_vals), sum(s_vals)

# ==================================================================
#                           Main Control
# ==================================================================

class bcolors:
    """
        Allows the IE values to be printed in color
    """
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    ENDC = '\033[0m'

def no_input_FCHK():
    """
        Input: None. Def called only if txt file is not given in command line
        Output: Text file for user to fill out
        Populates a text file that the user then fills out to enter with \
                the code
    """
    filename = datetime.datetime.now().strftime("%m%d%Y-%H%M%S")
    filename = "ONYX-INPUT-FCHKMOD-", filename, ".txt"
    filename = ''.join(filename)

    #Input population for checkpoint files
    ERROR_OUT = open(filename,"w")
    ERROR_OUT.write("======================Onyx Input File======================\n\n" +\
            "Please fill out your entry in the space BELOW each query.\n" +\
            "If multiple entries are desired for a query, each must be typed in a new line.\n" +\
            "[Words in brackets] =  standard response to query.\n\n" +\
            "=====================USER ENTRY BELOW======================\n\n")
    ERROR_OUT.write("Ground state (or state 1) formatted checkpoint file(s):" + "\n\n")
    ERROR_OUT.write("Transition state (or state 2) formatted checkpoint file(s):" + "\n\n")
    ERROR_OUT.write("Write hyperchem files? [No]:" + "\n\n")
    ERROR_OUT.write("Temperature(s) in Kelvin:" + "\n\n")
    ERROR_OUT.write("Pressure (only one) in atmospheres:" + "\n\n")
    ERROR_OUT.write("Scaling factor for vibrational frequencies (only one) [1.0]:" + "\n\n")
    ERROR_OUT.write("Project out gradient direction [No]:" + "\n\n")
    ERROR_OUT.write("Atom symbol - ground state atom number - transition state atom number - isotope" + "\n")
    ERROR_OUT.write("Put at least one space between each input. DO NOT use any other character to signify spaces!" + "\n\n")
    ERROR_OUT.close()

def no_input_LOG():
    """
        Input: None. Def called only if option is called in command line
        Output: Text file for user to fill out
    """
    filename = datetime.datetime.now().strftime("%m%d%Y-%H%M%S")
    filename = "ONYX-INPUT-LOGMOD-", filename, ".txt"
    filename = ''.join(filename)

    ERROR_OUT = open(filename,"w")
    ERROR_OUT.write("======================Onyx Input File======================\n\n" +\
            "Please fill out your entry in the space BELOW each query.\n" +\
            "If multiple entries are desired for a query, each must be typed in a new line.\n" +\
            "[Words in brackets] =  standard response to query.\n\n" +\
            "=====================USER ENTRY BELOW======================\n\n")
    ERROR_OUT.write("Unlabeled transition state (or state 2) file(s):" +"\n\n")
    ERROR_OUT.write("Labeled transition state (or state 2) file(s):" + "\n\n")
    ERROR_OUT.write("Unlabeled ground state (or state 1) file(s):" + "\n\n")
    ERROR_OUT.write("Labeled ground state (or state 1) file(s):" + "\n\n")
    ERROR_OUT.write("Temperature(s) in Kelvin:" + "\n\n")
    ERROR_OUT.write("Scaling factor for vibrational frequencies (only one) [1.0]:" + "\n\n")
    ERROR_OUT.close()

def parse_txt_fchk(text_file):
    """f
        Input: Text file (see def no_input for format)
        Output: Each input for the four separate freqchks
        Preparing temperary text files that will be fed into the \
                'freqchk' command
    """
    IN_TEXT = open(text_file)
    all_lines = IN_TEXT.readlines()

    lines = []
    queue1 = "Ground state (Or State 1)"
    queue2 = "Transition state (Or State 2)"
    queue3 = "Write hyperchem files?"
    queue4 = "Temperature"
    queue5 = "Pressure"
    queue6 = "Scaling factor"
    queue7 = "gradient direction"
    queue8 = "Atom symbol - ground state atom number"
    queue9 = "Put at least one space between each input."
    for i in range(0, len(all_lines)):
        if queue1.lower() in all_lines[i].lower():
            Q1 = i
        if queue2.lower() in all_lines[i].lower():
            Q2 = i
        if queue3.lower() in all_lines[i].lower():
            Q3 = i
        if queue4.lower() in all_lines[i].lower():
            Q4 = i
        if queue5.lower() in all_lines[i].lower():
            Q5 = i
        if queue6.lower() in all_lines[i].lower():
            Q6 = i
        if queue7.lower() in all_lines[i].lower():
            Q7 = i
        if queue8.lower() in all_lines[i].lower():
            Q8 = i
        if queue9.lower() in all_lines[i].lower():
            Q9 = i

    GS_chkpt_file = []
    TS_chkpt_file = []
    hyperchem_files = []
    temp = []
    pressure = []
    scale_factor = []
    iso_masses = []
    gradient_direction = []
    isotope_changes = []
    #Pulls data from text file and enters them into respective list
    for j in range(0, len(all_lines)):
        if all_lines[j].isspace():
            continue
        if j > Q1 and j < Q2:
            GS_chkpt_file.append(all_lines[j])
            GS_chkpt_file = map(lambda s: s.strip(), GS_chkpt_file)
        if j > Q2 and j < Q3:
            TS_chkpt_file.append(all_lines[j])
            TS_chkpt_file = map(lambda s: s.strip(), TS_chkpt_file)
        if j > Q3 and j < Q4:
            hyperchem_files.append(all_lines[j])
            hyperchem_files = map(lambda s: s.strip(), hyperchem_files)
        if j > Q4 and j < Q5:
            temp.append(all_lines[j])
            temp = map(lambda s: s.strip(), temp)
        if j > Q5 and j < Q6:
            pressure.append(all_lines[j])
            pressure = map(lambda s: s.strip(), pressure)
        if j > Q6 and j < Q7:
            scale_factor.append(all_lines[j])
            scale_factor = map(lambda s: s.strip(), scale_factor)
        if j > Q7 and j < Q8 and j != Q8:
            gradient_direction.append(all_lines[j])
            gradient_direction = map(lambda s: s.strip(), gradient_direction)
        if j > Q9:
            all_lines[j] = all_lines[j].split()
            isotope_changes.append(all_lines[j])

    #Combines all lists of lists into a single list
    merge = list(itertools.chain.from_iterable(isotope_changes))
    #'Chunks' the list into lists of 4 (atom symbol, GS atom num, \
            #TS atom num, isotope mass) - makes list of lists
    isotope_changes = [isotope_changes[x:x+4] for x in xrange(0, \
            len(isotope_changes), 4)]
    #Make an iterator that returns elements from the first iterable until \
            #it is exhausted, then proceeds to the next iterable, \
            #until all of the iterables are exhausted
    isotope_changes = list(itertools.chain(*isotope_changes))
    #Sorts the lists (within the bigger list) based on the GS atom num
    isotope_changes = sorted(isotope_changes, key=itemgetter(1))
    #Calls 'try_int' module to turn any values into integers possible
    isotope_changes = [[try_int(x) for x in lst] for lst in isotope_changes]

    #Find the number of atoms in the GS checkpoint file
    for j in GS_chkpt_file:
        IN_FILE_GS = open(GS_chkpt_file[0])
        number_atoms_GS = []
        for line in IN_FILE_GS:
            if "Number of atoms" in line:
                number_atoms_GS.append(line.split())
                #Joins all characters in the line together to form \
                        #"NumberofatomsI#" where # is the number of atoms
                number_atoms_GS = ''.join(number_atoms_GS[0])
                #First 14 characters are "NumberofatomsI" \
                        #(leaves just the number of atoms)
                number_atoms_GS = ''.join(number_atoms_GS[14:])
                #Makes the number an integer rather than a string
                number_atoms_GS = int(number_atoms_GS)

    #Find the number of atoms in the TS checkpoint file
    i = 0
    for j in TS_chkpt_file:
        IN_FILE_TS = open(TS_chkpt_file[0])
        number_atoms_TS = []
        for line in IN_FILE_TS:
            if "Number of atoms" in line:
                number_atoms_TS.append(line.split())
                #Joins all characters in the line together to form \
                        #"NumberofatomsI#" where # is the number of atoms
                number_atoms_TS = ''.join(number_atoms_TS[0])
                #First 14 characters are "NumberofatomsI" \
                        #(leaves just the number of atoms)
                number_atoms_TS = ''.join(number_atoms_TS[14:])
                #Makes the number an integer rather than a string
                number_atoms_TS = int(number_atoms_TS)

    IN_TEXT.close()
    IN_FILE_GS.close()
    IN_FILE_TS.close()
    return GS_chkpt_file, TS_chkpt_file, hyperchem_files, temp, pressure, \
            scale_factor, gradient_direction, isotope_changes, \
            number_atoms_GS, number_atoms_TS

def parse_txt_log(text_file):
    """
        Input: Text file (see def no_input for format)
        Output: Each input for the four separate freqchks
        Preparing temperary text files that will be fed into the \
                'freqchk' command
    """
    IN_TEXT = open(text_file)
    all_lines = IN_TEXT.readlines()
    
    queue1 = "Unlabeled transition state"
    queue2 = "Labeled transition state"
    queue3 = "Unlabeled ground state"
    queue4 = "Labeled ground state"
    queue5 = "Temperature"
    queue6 = "Scaling factor"

    lines = []
    for i in range(0, len(all_lines)):
        if queue1.lower() in all_lines[i].lower():
            Q1 = i
        if queue2.lower() in all_lines[i].lower():
            Q2 = i
        if queue3.lower() in all_lines[i].lower():
            Q3 = i
        if queue4.lower() in all_lines[i].lower():
            Q4 = i
        if queue5.lower() in all_lines[i].lower():
            Q5 = i
        if queue6.lower() in all_lines[i].lower():
            Q6 = i

    TS_unlabeled = []
    TS_labeled = []
    GS_unlabeled = []
    GS_labeled = []
    scale_factor = []
    temp = []

    #Pulls data from text file and enters them into respective list
    for j in range(0, len(all_lines)):
        if all_lines[j].isspace():
            continue
        if j > Q1 and j < Q2:
            TS_unlabeled.append(all_lines[j])
            TS_unlabeled = map(lambda s: s.strip(), TS_unlabeled)
        if j > Q2 and j < Q3:
            TS_labeled.append(all_lines[j])
            TS_labeled = map(lambda s: s.strip(), TS_labeled)
        if j > Q3 and j < Q4:
            GS_unlabeled.append(all_lines[j])
            GS_unlabeled = map(lambda s: s.strip(), GS_unlabeled)
        if j > Q4 and j < Q5:
            GS_labeled.append(all_lines[j])
            GS_labeled = map(lambda s: s.strip(), GS_labeled)
        if j > Q5 and j < Q6:
            temp.append(all_lines[j])
            temp = map(lambda s: s.strip(), temp)
        if j > Q6:
            all_lines[j] = all_lines[j].split()
            scale_factor.append(all_lines[j])
    IN_TEXT.close()
    return TS_unlabeled, TS_labeled, GS_unlabeled, GS_labeled, \
            temp, scale_factor

def try_int(x):
    """
        Input: list with strings
        Output: list with integers and strings
        If the index can be converted to an integer, it will be. \
                Otherwise it will stay a string
    """
    try:
        return int(x)
    except ValueError:
        return x

def calculate_IE_LOG_GUI(GS_unlabeled, GS_labeled, TS_unlabeled, \
        TS_labeled, temp, scale_factor, BM_output, BMtun_output, \
        RR_output, RRtun_output):
    """
        Called if using the GUI. Skips several of the steps in the full \
                IE calculation
    """
    if GS_unlabeled == '' or GS_labeled == '' or TS_unlabeled == '' \
            or TS_labeled == '':
        print "Please select four files before proceeding."
        return

    try:
        if float(temp) < 0 or float(scale_factor) < 0:
            print "Cannot have negative values for temperature and/or \
                    scaling factor!"
            return
    except ValueError:
        print "Temperature and/or scaling factor should be a number."
        return

    print "\n-------- Initializing Onyx Program --------\n"
    print "HERE BITCH"

    count = 1
    master_output = []

    IE_BM, IE_tunneling_BM, SYM, MMI, ZPE, EXC = \
            calc_IE_Bigeleisen(GS_unlabeled, GS_labeled, TS_unlabeled, \
            TS_labeled, temp, scale_factor, count)
    IE_RR, IE_tunneling_RR, KIE_or_EIE, Hthermal, ddS = \
            calc_IE_rigid_rotor_method(GS_unlabeled, GS_labeled, \
            TS_unlabeled, TS_labeled, temp, scale_factor, count)

    #Split file names so that doesn't show entire path
    GS_unlabeled = GS_unlabeled.split("/")
    GS_unlabeled = GS_unlabeled[-1]
    GS_labeled = GS_labeled.split("/")
    GS_labeled = GS_labeled[-1]
    TS_unlabeled = TS_unlabeled.split("/")
    TS_unlabeled = TS_unlabeled[-1]
    TS_labeled = TS_labeled.split("/")
    TS_labeled = TS_labeled[-1]

    IE_BM_temp = str(IE_BM)
    IE_tunneling_BM_temp = str(IE_tunneling_BM)
    IE_RR_temp = str(IE_RR)
    IE_tunneling_RR_temp = str(IE_tunneling_RR)

    print "\nRESULTS:"
    if KIE_or_EIE == 1:
        abbreviation = "KIE"
    elif KIE_or_EIE == 2:
        abbreviation = "EIE"

    print "\n\nBM (" + abbreviation + ") = SYM x MMI x EXC x ZPE"
    print "SYM", '\t\t', "MMI", '\t\t', "EXC", '\t\t', "ZPE", '\t\t', \
            abbreviation, '\t\t', abbreviation+"_tunneling"
    print "------------------------------------------------------------" +\
            "---------------------------------"
    print SYM, '\t\t', MMI, '\t\t', EXC, '\t\t', \
            ZPE, '\t\t', bcolors.GREEN + IE_BM_temp + bcolors.ENDC,\
            '\t\t', bcolors.PURPLE + IE_tunneling_BM_temp + bcolors.ENDC
    print "------------------------------------------------------------" +\
            "---------------------------------\n"
    print "RR (" + abbreviation + ") = ddH x ddS"
    print "ddH", '\t\t', "ddS", '\t\t', abbreviation, '\t\t', \
            abbreviation+"_tunneling"
    print "-------------------------------------------------------------"
    print Hthermal, '\t\t', ddS, '\t\t', bcolors.GREEN + \
            IE_RR_temp + bcolors.ENDC, '\t\t', bcolors.PURPLE + \
            IE_tunneling_RR_temp + bcolors.ENDC
    print "-------------------------------------------------------------"
    print "\n"

    IE_BM = "{IB:.4f}".format(IB=IE_BM)
    BM_output.insert(0, IE_BM)

    IE_tunneling_BM = "{ITB:.4f}".format(ITB=IE_tunneling_BM)
    BMtun_output.insert(0, IE_tunneling_BM)

    IE_RR = "{IR:.4f}".format(IR=IE_RR)
    RR_output.insert(0, IE_RR)

    IE_tunneling_RR = "{ITR:.4f}".format(ITR=IE_tunneling_RR)
    RRtun_output.insert(0, IE_tunneling_RR)

def calculate_IE_FCHK_GUI(GS, TS, temp, scale_factor, pressure, hyperchem, \
        grad_dir, atom_sym, GS_atom_num, TS_atom_num, isotope_mass, \
        BM_output, BMtun_output, RR_output, RRtun_output):
    """
        Called if using the GUI. Skips several of the steps in the full \
                IE calculation
    """
    if GS == '' or TS == '':
        print "Please select two files before proceeding."
        return

    try:
        if float(temp) < 0 or float(scale_factor) < 0 or float(pressure) < 0:
            print "Cannot have negative values for temperature, \
                    scaling factor and/or pressure!"
            return
    except ValueError:
        print "Temperature, scaling factor and/or scaling factor should be \
                numbers."
        return

    print "\n-------- Initializing Onyx Program --------\n"

    count = 1
    master_output = []

    #Find how many atoms in each file
    with open(GS, 'r+') as f:
        number_atoms_GS = []
        for line in f:
            if "Number of atoms" in line:
                number_atoms_GS.append(line.split())
                #Joins all characters in the line together to form \
                        #"NumberofatomsI#" where # is the number of atoms
                number_atoms_GS = ''.join(number_atoms_GS[0])
                #First 14 characters are "NumberofatomsI" \
                        #(leaves just the number of atoms)
                number_atoms_GS = ''.join(number_atoms_GS[14:])
                #Makes the number an integer rather than a string
                number_atoms_GS = int(number_atoms_GS)
    with open(TS, 'r+') as j:
        number_atoms_TS = []
        for line in j:
            if "Number of atoms" in line:
                number_atoms_TS.append(line.split())
                #Joins all characters in the line together to form \
                        #"NumberofatomsI#" where # is the number of atoms
                number_atoms_TS = ''.join(number_atoms_TS[0])
                #First 14 characters are "NumberofatomsI" \
                        #(leaves just the number of atoms)
                number_atoms_TS = ''.join(number_atoms_TS[14:])
                #Makes the number an integer rather than a string
                number_atoms_TS = int(number_atoms_TS)

    isotope_changes = []
    isotope_changes.append(atom_sym)
    isotope_changes.append(int(GS_atom_num))
    isotope_changes.append(int(TS_atom_num))
    isotope_changes.append(int(isotope_mass))

    run_freqchk(GS, TS, hyperchem, temp, pressure, scale_factor, \
            grad_dir, isotope_changes, number_atoms_GS, number_atoms_TS, count)
    IE_BM, IE_tunneling_BM, SYM, MMI, ZPE, EXC = \
            calc_IE_Bigeleisen("freq_GS_no_marker.txt", "freq_GS_marker.txt", \
            "freq_TS_no_marker.txt", "freq_TS_marker.txt", temp, \
            scale_factor, count)
    IE_RR, IE_tunneling_RR, KIE_or_EIE, Hthermal, ddS = \
            calc_IE_rigid_rotor_method("freq_GS_no_marker.txt", \
            "freq_GS_marker.txt", "freq_TS_no_marker.txt", \
            "freq_TS_marker.txt", temp, scale_factor, count)
    os.system("rm freq_GS_no_marker.txt freq_GS_marker.txt \
            freq_TS_no_marker.txt freq_TS_marker.txt")

    #Split file names so that doesn't show entire path
    GS = GS.split("/")
    GS = GS[-1]
    TS = TS.split("/")
    TS = TS[-1]

    IE_BM_temp = str(IE_BM)
    IE_tunneling_BM_temp = str(IE_tunneling_BM)
    IE_RR_temp = str(IE_RR)
    IE_tunneling_RR_temp = str(IE_tunneling_RR)

    print "\nRESULTS:"
    if KIE_or_EIE == 1:
        abbreviation = "KIE"
    elif KIE_or_EIE == 2:
        abbreviation = "EIE"


    print "\n\nBM (" + abbreviation + ") = SYM x MMI x EXC x ZPE"
    print "SYM", '\t\t', "MMI", '\t\t', "EXC", '\t\t', "ZPE", '\t\t', \
            abbreviation, '\t\t', abbreviation+"_tunneling"
    print "------------------------------------------------------------" +\
            "---------------------------------"
    print SYM, '\t\t', MMI, '\t\t', EXC, '\t\t', \
            ZPE, '\t\t', bcolors.GREEN + IE_BM_temp + bcolors.ENDC,\
            '\t\t', bcolors.PURPLE + IE_tunneling_BM_temp + bcolors.ENDC
    print "------------------------------------------------------------" +\
            "---------------------------------\n"
    print "RR (" + abbreviation + ") = ddH x ddS"
    print "ddH", '\t\t', "ddS", '\t\t', abbreviation, '\t\t', \
            abbreviation+"_tunneling"
    print "-------------------------------------------------------------"
    print Hthermal, '\t\t', ddS, '\t\t', bcolors.GREEN + \
            IE_RR_temp + bcolors.ENDC, '\t\t', bcolors.PURPLE + \
            IE_tunneling_RR_temp + bcolors.ENDC
    print "-------------------------------------------------------------"
    print "\n"

    IE_BM = "{IB:.4f}".format(IB=IE_BM)
    BM_output.insert(0, IE_BM)

    IE_tunneling_BM = "{ITB:.4f}".format(ITB=IE_tunneling_BM)
    BMtun_output.insert(0, IE_tunneling_BM)

    IE_RR = "{IR:.4f}".format(IR=IE_RR)
    RR_output.insert(0, IE_RR)

    IE_tunneling_RR = "{ITR:.4f}".format(ITR=IE_tunneling_RR)
    RRtun_output.insert(0, IE_tunneling_RR)

def main(freqinput, loginput, fchktxtname, logtxtname):
    if len(sys.argv) > 1:
        if freqinput:
            print "Please fill out the text file that was just populated " +\
                    "in the current directory."
            no_input_FCHK()
            sys.exit()
        if loginput:
            print "Please fill out the text file that was just populated " +\
                    "in the current directory."
            no_input_LOG()
            sys.exit()
        if fchktxtname:
            master_output = []
            count = 0
            print "\n-------- Initializing Onyx Program --------\n"
            GS_chkpt_file, TS_chkpt_file, hyperchem_files, temp, pressure, \
                    scale_factor, gradient_direction, isotope_changes, \
                    number_atoms_GS, number_atoms_TS = \
                    parse_txt_fchk(fchktxtname)
            for each_GS_file in GS_chkpt_file:
                for each_TS_file in TS_chkpt_file:
                    for each_temp in temp:
                        for each_pressure in pressure:
                            for each_label in isotope_changes:
                                for each_scale in scale_factor:
                                    count += 1
                                    run_freqchk(each_GS_file, each_TS_file, \
                                            hyperchem_files, each_temp, \
                                            each_pressure, each_scale, \
                                            gradient_direction, each_label, \
                                            number_atoms_GS, \
                                            number_atoms_TS, count)
                                    IE_BM, IE_tunneling_BM, SYM, MMI, ZPE, \
                                            EXC = calc_IE_Bigeleisen(\
                                            "freq_GS_no_marker.txt", \
                                            "freq_GS_marker.txt", \
                                            "freq_TS_no_marker.txt", \
                                            "freq_TS_marker.txt", \
                                            each_temp, each_scale, count)
                                    IE_RR, IE_tunneling_RR, KIE_or_EIE, \
                                            Hthermal, ddS = \
                                            calc_IE_rigid_rotor_method(\
                                            "freq_GS_no_marker.txt", \
                                            "freq_GS_marker.txt", \
                                            "freq_TS_no_marker.txt", \
                                            "freq_TS_marker.txt", each_temp, \
                                            each_scale, count)
                                    master_output.append(count)
                                    master_output.append(each_GS_file)
                                    master_output.append(each_TS_file)
                                    master_output.append(each_temp)
                                    master_output.append(each_scale)
                                    master_output.append(IE_BM)
                                    master_output.append(IE_tunneling_BM)
                                    master_output.append(IE_RR)
                                    master_output.append(IE_tunneling_RR)
                                    master_output.append(each_label)
                                    master_output.append(SYM)
                                    master_output.append(MMI)
                                    master_output.append(EXC)
                                    master_output.append(ZPE)
                                    master_output.append(Hthermal)
                                    master_output.append(ddS)
                                    os.system("rm freq_GS_no_marker.txt \
                                            freq_GS_marker.txt \
                                            freq_TS_no_marker.txt \
                                            freq_TS_marker.txt")
            print_results_FREQ(master_output, KIE_or_EIE)
        if logtxtname:
            master_output = []
            count = 0
            print "\n-------- Initializing Onyx Program --------\n"
            TS_unlabeled, TS_labeled, GS_unlabeled, GS_labeled, temp, \
                    scale_factor = parse_txt_log(logtxtname)
            scale_factor = scale_factor[0]
            for each_TS_unlabeled in TS_unlabeled:
                for each_TS_labeled in TS_labeled:
                    for each_GS_unlabeled in GS_unlabeled:
                        for each_GS_labeled in GS_labeled:
                            for each_temp in temp:
                                for each_scale in scale_factor:
                                    count += 1
                                    IE_BM, IE_tunneling_BM, SYM, MMI, ZPE, \
                                            EXC = calc_IE_Bigeleisen(\
                                            each_GS_unlabeled, \
                                            each_GS_labeled, \
                                            each_TS_unlabeled, \
                                            each_TS_labeled, \
                                            each_temp, each_scale, count)
                                    IE_RR, IE_tunneling_RR, KIE_or_EIE, \
                                            Htermal, ddS = \
                                            calc_IE_rigid_rotor_method(\
                                            each_GS_unlabeled, \
                                            each_GS_labeled, \
                                            each_TS_unlabeled, \
                                            each_TS_labeled, each_temp, \
                                            each_scale, count)
                                    master_output.append(count)
                                    master_output.append(each_GS_unlabeled)
                                    master_output.append(each_GS_labeled)
                                    master_output.append(each_TS_unlabeled)
                                    master_output.append(each_TS_labeled)
                                    master_output.append(each_temp)
                                    master_output.append(each_scale)
                                    master_output.append(IE_BM)
                                    master_output.append(IE_tunneling_BM)
                                    master_output.append(IE_RR)
                                    master_output.append(IE_tunneling_RR)
                                    master_output.append(SYM)
                                    master_output.append(MMI)
                                    master_output.append(EXC)
                                    master_output.append(ZPE)
                                    master_output.append(Htermal)
                                    master_output.append(ddS)
            print_results_LOG(master_output, KIE_or_EIE)
    else:
        GUI()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A program to " +\
            "automatically compute isotope effects. To use the Graphical " +\
            "User Interface (GUI), simply type " +\
            "'python Onyx.py'.")
    parser.add_argument('-fp', '--freqchkprint', help=\
            'print input file for freqchk functionality. ' +\
            'Fill out txt file with necessary information', action='count')
    parser.add_argument('-lp', '--logprint', help='print input file for ' +\
            'G09 log file functionality. Fill out txt file with necessary ' +\
            'information', action='count')
    parser.add_argument('-fi', '--freqchkinput', dest="fchktxtname", help=\
            'Calculate IE utilizing freqchk functionality. Pass in filled ' +\
            'out text input file (generated by -fi option)')
    parser.add_argument('-li', '--loginput', dest="logtxtname", help=\
            'Calculate IE utilizing log file functionality. Pass in filled ' +\
            'out text input file (generated by -li option)')

    args = parser.parse_args()

    main(args.freqchkprint, args.logprint, args.fchktxtname, args.logtxtname)
