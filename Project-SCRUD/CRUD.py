# -------------------------------------IMPORTS NEED--------------------------------------

import sqlite3
from os import system
from sqlite3.dbapi2 import OperationalError
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

system('cls') # To clean the terminal / console. 

# -------------------------------------ROOT, FRAME--------------------------------------

root = Tk() # asignation of Tk(), to use it as root.
root.geometry("250x310") # Set the the geometry of the GUI (width, height)
root.title("BBDD - CRUD") # Set the Title of the GUI
root.resizable(width=0, height=0) # Set if the GUI to not allow resizability (False = 0; True = 1)

superior_frame = Frame(root) # Creates the first frame, were the fields will be
superior_frame.pack() # packs the frame

# ---------------------------------------VARIABLES--------------------------------------
# Here will be the variables that will be use.

user_id = StringVar() # userd id variable
user_name = StringVar() # user name variable
user_last_name = StringVar() # user last name variable
user_address = StringVar() # user address variable
user_password = StringVar() # user password variable

# ---------------------------------------FUNCTIONS--------------------------------------
# ------------------------------CREATE-OR-CONNECT-TO-BBDD-------------------------------

# This function will create or connect to the database the user types in the dialog

def Connect_create():

# Inside the try is the code that tries to run
    try:
        
        global bbdd_name # makes the variable bbdd_name global (bbdd = database)

        bbdd_name = simpledialog.askstring("Ingresar datos", "Nombre BBDD:", parent=superior_frame) # opens a dialog asking the user the name of the database

        # this conditional is True if the name introduced by the user isn't an empty space or didn't write anything.
        if bbdd_name != "" and bbdd_name is not None:

            bbdd_name.strip() # .strip() to remove the white spaces at the beginning and the endof the string

            bbdd_name = bbdd_name + ".sqlite3" # to add the extesion to the DDBB introduced, so the user doesn't need to enter it.

            print("BBDD: ", bbdd_name) # Prints in the console the name of the DDBB created with it's extension.

        # If the user didn't fill the dialog or filled it and clicked "cancel" this conditional captures that and creates a default database name.
        else:
            bbdd_name = "Usuarios.sqlite3" # name of the default database
            print("La BBDD se llamara: 'Usuarios.sqlite3'") # prints in the console the name of the default database

        connection = sqlite3.connect(bbdd_name) # starts the connection or creates the database (if it didn't exist) with name inside bbdd_name
        cursor = connection.cursor() # We start the cursor while the conection is on

        # Creates the table "USER_DATA" with the all variables as strings and a maximum of 50 characters
        cursor.execute('''
        CREATE TABLE USER_DATA(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_NAME VARCHAR(50) UNIQUE, 
        USER_LAST_NAME VARCHAR (50), 
        ADDRESS VARCHAR(50), 
        PASSWORD VARCHAR(50), 
        COMMENTS VARCHAR(50))
        ''')

        connection.close() # close the connection because we already did the modification in the database

# Captured the error "OperationError" so the program continues.
    except OperationalError:
        messagebox.showinfo("BBDD","La connection a la base de datos '{}' fue exitosa.".format(bbdd_name)) # Pop-ups a info window saying that the DDBB was connected and it's name

    else:
        messagebox.showinfo("BBDD","La Base de Datos '{}' fue creada con éxito".format(bbdd_name)) # Pop-ups a info window saying that the DDBB was created and it's name

# -----------------------------------------EXIT------------------------------------------
# Function to close the application

def Exit():
    valor = messagebox.askquestion("Salir","¿Seguro que quieres salir?") # Pop-ups a window asking if the user wants to exit

    # if the answer to the question from before is yes, this conditional triggers:
    if valor == "yes":
        root.destroy() # destroys the program to close it.

# -------------------------------------CLEAN-FIELDS--------------------------------------
# This function cleans all the fields from the program by setting all the variables to an empty string. 

def Clean_fields():
    user_id.set("") 
    user_name.set("")
    user_last_name.set("")
    user_address.set("")
    user_password.set("")
    comment_text.delete(0.0, END)

# -------------------------------------------CRUD------------------------------------------
# Here will be the functions that does the CRUD (Create, Read, Update, Delete)

# ------------------------------------------CREATE-----------------------------------------
# Creates the data (an user) with the information inside fields into the database

def Create():

    try:
        connection = sqlite3.connect(bbdd_name) # starts the connection
        cursor = connection.cursor() # starts the cursor

        # List that contains a tuple with the data captured from the fields
        user_data = [(
            user_name.get().strip(), 
            user_last_name.get().strip(), 
            user_address.get().strip(), 
            user_password.get().strip(), 
            comment_text.get(0.0, END).strip()
            )]

        cursor.executemany("INSERT INTO USER_DATA VALUES(NULL,?,?,?,?,?)", user_data) # Grabs the list created before and dump it inside the database in their respective columns and rows

        connection.commit() # to commit the changes

        connection.close() # closes the connection

        messagebox.showinfo("Creacion de datos", "Se ha creado el registro exitosamente.") # Shows a info window saying that the creation was successful

    except:		
        messagebox.showwarning("Error creacion de datos.", "Error, Vuelva a intentarlo.") # Shows a warning info saying that the creation was failed

# ------------------------------------------READ-----------------------------------------
# Function that reads the requested data from a user, acording to the fields filled in the GUI
# It has multiple "If's" to find if one of the fields is filled with information to search for a specific user.

def Read():

    try:
        
        # Checks if the user password is not empty
        if user_password.get() != "":

            raise NameError("ERROR!","No se puede buscar según una contraseña.\nEsta prohibido en el programa.") # It raises NameError and triggers the except (see below)

        connection = sqlite3.connect(bbdd_name) # Starts connection
        cursor = connection.cursor() # Starts cursor

        # Checks if the user id field is not empty
        if user_id.get() != "":

            cursor.execute("SELECT * FROM USER_DATA WHERE ID= {}".format(user_id.get().strip())) # Recovers the data based on the provided element in the ID field

        # Checks if the user name field is not empty
        elif user_name.get() != "":

            cursor.execute("SELECT * FROM USER_DATA WHERE USER_NAME= '{}'".format(user_name.get().strip())) # Recovers the data based on the provided element in the name field

        # Checks if the last name field is not empty
        elif user_last_name.get() != "":

            cursor.execute("SELECT * FROM USER_DATA WHERE USER_LAST_NAME= '{}'".format(user_last_name.get().strip())) # Recovers the data based on the provided element in the last name field

        # Checks if the last name field is not empty
        elif user_address.get() != "":

            cursor.execute("SELECT * FROM USER_DATA WHERE ADDRESS= '{}'".format(user_address.get().strip())) # Recovers the data based on the provided element in the Address field

        # Checks if the last name field is not empty
        elif comment_text.get("0.0", "end") != "":

            cursor.execute("SELECT * FROM USER_DATA WHERE COMMENTS= '{}'".format(comment_text.get(0.0, END).strip())) # Recovers the data based on the provided element in the Comments field

        user_data_list = cursor.fetchall() # Gathers the data requested from the database (which is inside a list) and puts it inside a variable

        # Loop the user_data_list to get all the elements and put them inside the fields
        for dato in user_data_list:

            user_id.set(dato[0])
            user_name.set(dato[1])
            user_last_name.set(dato[2])
            user_address.set(dato[3])
            user_password.set(dato[4])
            comment_text.insert(1.0,dato[5])

        connection.close() # Closes the connection

        messagebox.showinfo("Lectura exitosa.", "Mostrando los datos ingresados...") # Pop-ups a info window saying that the reading was successful and are shown in the fields of the program

    # Excepts the NameError (The password error) as ErrorSearchPassword
    except NameError as ErrorSearchPassword:

        messagebox.showwarning("ERROR!","No se puede buscar según una contraseña.\nEsta prohibido.", ErrorSearchPassword) # Pop-ups a warning window saying that's not possible to search by a user password

    except:
        
        messagebox.showwarning("ERROR!","Error al Read los datos ingresados.\n Dato inválido ó inexistente.") # In case the Try failed and there wasn't any user (or data) that fits the search

# ---------------------------------------UPDATE--------------------------------------
# Function that updates the data of a user only based on the ID. If the ID field is empty, then triggers a warning window
# As a security protocol and good practice, always first Read the user data and then modify it, lastly use this function

def Update():

    try:

        # This conditional triggers if the ID field is empty
        if user_id.get() == "":
            raise NameError("ERROR!", "El campo ID esta vacío.") # Raises a NameError because the ID field is empty

        connection = sqlite3.connect(bbdd_name) # Starts the connection to the database
        cursor = connection.cursor() # Starts the cursor

        #This tuple gets the data from the fields
        columns_data = (
            user_name.get().strip(), 
            user_last_name.get().strip(), 
            user_address.get().strip(), 
            user_password.get().strip(), 
            comment_text.get(0.0, END).strip()
            )

        # Just a safety protocol, it checks that the user ID isn't empty
        if user_id.get() != "" :
            
            # Generates the modifications based on the data inside the tuple and the ID passed on the field ID
            cursor.execute("UPDATE USER_DATA SET USER_NAME=?, USER_LAST_NAME=?, ADDRESS=?, PASSWORD=?, COMMENTS=? WHERE ID= {}".format(user_id.get()), columns_data) 

        connection.commit() # Commits the changes

        connection.close() # Close the connection

        messagebox.showinfo("Actualización exitosa","Se ha actualizado la BBDD exitosamente.") # Pop-ups a info message saying that the update was successful

    # When the exception NameError raises, this triggers:
    except NameError:
        messagebox.showwarning("ERROR!","El campo ID esta vacío.") # Pop-ups a warning window saying that the ID field is empty

# -----------------------------------------BORRAR----------------------------------------
# Function to delete a user from the database, based on the ID
# It's highly recommended to read the user data and then use this one

def Delete():

    try:
        # This conditional triggers if the ID field is empty
        if user_id.get() == "":
            raise NameError("ERROR!", "El campo ID esta vacío.") # Raises a NameError because the ID field is empty
        
        respuesta = messagebox.askquestion("Borrar registro","¿Seguro que borrar el registro?".format(user_id)) # Message window asking "yes" or "no" to delete the user

        if respuesta == "yes":

            connection = sqlite3.connect(bbdd_name) # Start the connection
            cursor = connection.cursor() # Start the cursor

            cursor.execute("DELETE FROM USER_DATA WHERE ID= {}".format(user_id.get())) # Deletes a user based on the ID

            connection.commit() # Commit the changes to the database

            connection.close() # Close the connection

    except:
        messagebox.showwarning("ERROR!","Error al tratar de borrar un registro de la BBDD.") # Same error as update, if the ID field is empty pop-ups a warning window saying that the ID is empty

    else:
        messagebox.showinfo("Borrado exitoso","Se ha borrado un registro de la BBDD, exitosamente.") # Shows a info window saying that the delete was successful


# ---------------------------------------Help-Menu--------------------------------------
# Here are the functions that are define for the buttons in the "Ayuda" Menu

# ----------------------------------------License---------------------------------------
#This function shows a info window about the license of this program

def License():
    messagebox.showinfo("Licencia","Programa perteneciente al dominio público.\nUsted es libre de usarlo.") # Shows a info window with the information about the license (it's free)

# ----------------------------------------About...--------------------------------------
# This function shows a info window about the program and it's version

def About():
    messagebox.showinfo("Acerca...","Programa realizado como proyecto por: \n-Emanuel Rodriguez Bedeman®\n\nVersión: 1.0 (BETA)") # Shows a info windows with the information about the program

# --------------------------------------Instructions-----------------------------------
# This function shows the instructions about the program (for this owns check the readme.md in: https://github.com/EmanuelRodriguezBedeman/Project-SCRUD/blob/main/README.md)

def Instructions():
    messagebox.showinfo("Instrucciones de uso",
'''Antes de operar con el programa, siempre ir a la pestaña "BBDD" y seleccionar "Create y/o conectar" para indicar con que base de datos queremos operar. 

-"Create": Agrega los datos ingresados como un registro a la BBDD.
    
-"Read": Muestra un registro según el dato introducido. Prohibido buscar por contraseña, antes de buscar otro registro limpiar el campo "Contraseña".
    
-"ACTUALIZAR": Actualiza la BBDD según la ID ingresada. ATENCIÓN: Primero Read los datos y luego actualizarlos.
    
-"BORRAR": Borra todo un registro de la BBDD según el ID. ¡CUIDADO: NO SE PUEDE DESHACER!''')

# --------------------------------------Menus-bar--------------------------------------
# Here will be all the code used to create the menu bar

menu_bar = Menu(root) # Here assigns the Menu function to the variable menu_bar, to make easier to use
root.config(menu= menu_bar) # Configures the root to use the variable we created before as the menu

menu_bbdd = Menu(menu_bar, tearoff = 0) # Creates the menu "BBDD". tearoff = 0 to eliminate the dotted line at the beginning of the cascade
menu_bbdd.add_command(label="Create y/o conectar", command= Connect_create) # Creates the command named "Create y/o conectar" asigned to the function Connect_create
menu_bbdd.add_command(label="Exit", command = Exit) # Creates the command named "Exit" asigned to the function Exit

menu_clean = Menu(menu_bar, tearoff = 0) # Creates the menu "Limpiar". tearoff = 0 to eliminate the dotted line at the beginning of the cascade
menu_clean.add_command(label="Limpiar campos", command= Clean_fields) # Creates the command named "Limpiar campos" asigned to the function Clean_fields

menu_CRUD = Menu(menu_bar, tearoff = 0) # Creates the menu "CRUD". tearoff = 0 to eliminate the dotted line at the beginning of the cascade 
menu_CRUD.add_command(label="Create", command = Create) # Creates the command named "Create" asigned to the function Create
menu_CRUD.add_command(label="Read", command = Read) # Creates the command named "Read" asigned to the function Read
menu_CRUD.add_command(label="Update", command = Update) # Creates the command named "Update" asigned to the function Update
menu_CRUD.add_command(label="Delete", command = Delete) # Creates the command named "Delete" asigned to the function Delete

menu_help = Menu(menu_bar, tearoff = 0) # Creates the menu "Ayuda". tearoff = 0 to eliminate the dotted line at the beginning of the cascade 
menu_help.add_command(label="Licencia", command= License) # Creates the command named "Licencia" asigned to the function License
menu_help.add_command(label="Acerca de...", command = About) # Creates the command named "Acerca de..." asigned to the function About
menu_help.add_separator() # Adds a horizontal line that separates commands inside the menu cascade of "Ayuda"
menu_help.add_command(label="Instrucciones", command = Instructions) # Creates the command "Instrucciones" asigned to the function Instructions

menu_bar.add_cascade(label="BBDD", menu=menu_bbdd) # Adds a cascade to the Menu menu_bbdd, named "BBDD"

menu_bar.add_cascade(label="Limpiar", menu=menu_clean) # Adds a cascade to the Menu menu_clean, named "Limpiar"

menu_bar.add_cascade(label="CRUD", menu=menu_CRUD) # Adds a cascade to the Menu menu_CRUD, named "CRUD"

menu_bar.add_cascade(label="Ayuda", menu=menu_help) # Adds a cascade to the Menu menu_help, named "Ayuda"

# ----------------------------------Labels and Entries----------------------------------
# Here is all the code used to create the labels and entries 

# Label and Entry for used ID
id_label = Label(superior_frame, text="ID:") # Creates the label "id_label" and inserts it in the superior_frame with the text "ID:"
id_label.grid(row=0, column=0, sticky="e", padx="2", pady="2") # Configures the position of the Label, to the row 0, column 0, sticked to the left (sticky ="e"), spaced horizontal (padx) and vertical (pady) by 2 pixels
ID_entry = Entry(superior_frame, textvariable = user_id) # Creates the Entry for the variable "user_id", and adds it to the superior_frame
ID_entry.grid(row=0, column=1, padx="5", pady="5") # Configures the position of the Entry, to the row 0, column 1, with padx and pady by 5 pixels
ID_entry.config(fg="black", justify="left") # Configures the entry, with black font color y justifies it to the left

# Label and Entry for used name
name_label = Label(superior_frame, text="Nombre:") # Creates the label "name_label" and inserts it in the superior_frame with the text "Nombre:"
name_label.grid(row=1, column=0, sticky="e", padx="2", pady="2") # Configures the position of the Label, to the row 1, column 0, sticked to the left, with padx and pady by 2 pixels
name_entry = Entry(superior_frame, textvariable = user_name) # Creates the Entry for the variable "user_name", and adds it to the superior_frame
name_entry.grid(row=1, column=1, padx="5", pady="5") # Configures the position of the Entry, to the row 1, column 1, with padx and pady by 5 pixels
name_entry.config(fg="red", justify="left") # Configures the entry, with red font color y justifies it to the left

# Label and Entry for used last name
last_name_label = Label(superior_frame, text="Apellido:") # Creates the label "last_name_label" and inserts it in the superior_frame with the text "Apellido:"
last_name_label.grid(row=2, column=0, sticky="e", padx="2", pady="2") # Configures the position of the Label, to the row 2, sticked to the left, column 0, with padx and pady by 2 pixels
last_name_entry = Entry(superior_frame, textvariable = user_last_name) # Creates the Entry for the variable "user_last_name", and adds it to the superior_frame
last_name_entry.grid(row=2, column=1, padx="5", pady="5") # Configures the position of the Entry, to the row 2, column 1, with padx and pady by 5 pixels 
last_name_entry.config(fg="black", justify="left") # Configures the entry, with black font color y justifies it to the left

# Label and Entry for used address
address_label = Label(superior_frame, text="Domicilio:") # Creates the label "address_label" and inserts it in the superior_frame with the text "Domicilio:"
address_label.grid(row=3, column=0, sticky="e", padx="2", pady="2") # Configures the position of the Label, to the row 3, sticked to the left, column 0, with padx and pady by 2 pixels
address_entry = Entry(superior_frame, textvariable = user_address) # Creates the Entry for the variable "user_address", and adds it to the superior_frame
address_entry.grid(row=3, column=1, padx="5", pady="5") # Configures the position of the Entry, to the row 3, column 1, with padx and pady by 5 pixels 
address_entry.config(fg="black", justify="left") # Configures the entry, with black font color y justifies it to the left

# Label and Entry for used password
password_label = Label(superior_frame, text="Contraseña:") # Creates the label "password_label" and inserts it in the superior_frame with the text "Contraseña:"
password_label.grid(row=4, column=0, sticky="e", padx="2", pady="2") # Configures the position of the Label, to the row 4, sticked to the left, column 0, with padx and pady by 2 pixels
password_entry = Entry(superior_frame, textvariable = user_password) # Creates the Entry for the variable "user_password", and adds it to the superior_frame
password_entry.grid(row=4, column=1, padx="5", pady="5") # Configures the position of the Entry, to the row 4, column 1, with padx and pady by 5 pixels 
password_entry.config(fg="black", justify="left", show="*") # Configures the entry, with black font color y justifies it to the left

# Label and Text for used comment box
comments_label = Label(superior_frame, text="Comentarios:") # Creates the label "comments_label" and inserts it in the superior_frame with the text "Comentarios:"
comments_label.grid(row=5, column=0, sticky="e", padx="2", pady="2")  # Configures the position of the Label, to the row 5, sticked to the left, column 0, with padx and pady by 2 pixels
comment_text = Text(superior_frame, width=15, height=5) # Creates the a Textbox, adds it to the superior_frame with a width of 15 pixels, height of 5 pixels
comment_text.grid(row=5, column=1, padx="2", pady="2") # Configures the position Textbox, to the row 5, column 1 with padx and pady by 2 pixels

# --------------------------------------- SCROLLBAR --------------------------------------
# This block of code adds the scrollbar to the comments in the Textbox

scrollbar = Scrollbar(superior_frame, command=comment_text.yview) # Creates the scrollbar, adds it the superior frame, and reacts to the y axis of the comment Textbox 
scrollbar.grid(row=5, column=2, sticky="nsew") # configures the position of the Scrollbar, to the row 5, column 2 and sticked to all directions
comment_text.config(yscrollcommand= scrollbar.set) # Configures the Textbox, adding the scrollbar to it

# -----------------------------------------BUTTONS----------------------------------------
# This block of code is for the buttons of the program

inferior_frame = Frame(root) # Frame for the buttons, named "inferior_frame"
inferior_frame.pack() # Packs it

button_create = Button(inferior_frame, text="Crear", bg="light grey", command = Create) # Creates the button "Crear", with light grey background, and with the command "Create"
button_create.grid(row=0, column=0, sticky = "e", padx = 10, pady = 10) # Modifies the position of the button, to the row 0, column 0, sticked to the left, padx and pady by 10 pixels

button_read = Button(inferior_frame, text="Leer", bg="light grey", command = Read) # Creates the button "Read", with light grey background, and with the command "Read"
button_read.grid(row=0, column=1, sticky = "e", padx = 5, pady = 10) # Modifies the position of the button, to the row 0, column 1, sticked to the left, padx by 5 pixels and pady by 10 pixels

button_update = Button(inferior_frame, text="Actualizar", bg="light grey", command = Update) # Creates the button "Actualizar", with light grey background, and with the command "Update"
button_update.grid(row=0, column=2, sticky = "e", padx = 5, pady = 10) # Modifies the position of the button, to the row 0, column 2, sticked to the left, padx by 5 pixels and pady by 10 pixels

button_delete = Button(inferior_frame, text="Borrar", bg="dark red", fg="White", command = Delete) # Creates the button "Borrar", with Dark Red background, and with the command "Delete"
button_delete.grid(row=0, column=3, sticky = "e", padx = 10, pady = 10) # Modifies the position of the button, to the row 0, column 3, sticked to the left, padx and pady by 10 pixels

button_clean = Button(inferior_frame, text="Limpiar Campos", bg="light grey", width=32, command = Clean_fields) # Creates the button "Limpar campos", with background "light_grey" and with the command "Clean_fields"
button_clean.grid(row=1, column=0, padx = 10, columnspan=4) # Modifies the position of the button, to the row 1, column 0, sticked to the left, padx by 10 pixels. 
# "columnspan" defines the number of columns that the button occupies

# -----------------------------------------------------------------------------------------
root.mainloop() # To start