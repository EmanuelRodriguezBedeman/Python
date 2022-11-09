# Project-CRUD

### Aplicacion de escritorio creada con Python y Tkinter para crear y modificar bases de datos con sqlite3. 
Como considero que la aplicacion es bastante intuitiva de entender para hispanohablantes, voy a dejar un tutorial de como operar la aplicacion en inglés. 

### Desktop app created with Python and Tkinter to create and modify a data base with sqlite3. 
Since I considerate that this app it's very easy to understand for people who speaks Spanish, I'll leave a tutorial of how to use it in english below:

![image](https://user-images.githubusercontent.com/93904438/143804868-963a9e20-b795-479f-85ac-e92e7f0de93e.png)

>ID
>
>Name = Nombre
>
>Lastname = Apellido
>
>Address = Domicilio

>Crear = Create
>
>Leer = Read
>
>Actualizar = Update
>
>Borrar = Delete
>
>Limpiar campos = Clean fields

> Ayuda = Help

## ¿How to use the aplication? (Tutorial)

### Create and connect to a sqlite3 database

First, click down the menu "BBDD" and select "Crear y/o conectar", 

![image](https://user-images.githubusercontent.com/93904438/143804895-aeb83dab-0b1b-4ed1-8aa7-1eadb2249fee.png)

It will pop-up a entry window asking the name of the database.

For this example, I'll call it "users"

![image](https://user-images.githubusercontent.com/93904438/143804924-0ce97a8a-8902-47d3-905a-f33812ccc471.png)

Once you click "Ok", it shows an information message window with the name of the dabase that was created. In this case it's called "users.sqlite3"

![image](https://user-images.githubusercontent.com/93904438/143779400-e8525b0e-c7ee-42a9-b186-5fed3262dd7a.png)

If you accidentally clicked "Cancel" or didn't enter a name in the entry window and selected "Ok", it creates a default database called "Usuarios.sqlite3" 

> _(Usuarios = users)_

![image](https://user-images.githubusercontent.com/93904438/143779862-6ef2a5b5-a3c8-4a91-874a-091b9692a490.png)

If we check the directory where this aplication (**_.exe_**) is, we will find the databases:

- "_users.sqlite3_" -> This is the one that we created.
- "_Usuarios.sqlite3_" -> This is the databases that's created by default.

![image](https://user-images.githubusercontent.com/93904438/143780218-c67aefd9-8a0a-46d8-bf8e-e56338c72cf8.png)
![image](https://user-images.githubusercontent.com/93904438/143779948-94697409-f332-4557-8fd8-f75a584776f2.png)

> "_You don't need to create and THEN connect to the database, the aplication automatically connects to the database once created._"

Suppose now that we already have a **_.sqlite3_** database created (with a table named: _"DATOS_USUARIOS"_ and with the same fields as shown in the application) and we want to connect to it.

> (_**TO DO:** Add a function to let the user write the table name to create it in the database_).

Simply when the entry window shows up, write the name of the database on it but remember to leave the database in the same folder as the aplication.

> (_**TO DO:** Add code to select the database using file explorer_).

For example, I'll select the database that we created ("_users.sqlite3_").

> Notice that you don't need to write the extension, just the name of the file.

![image](https://user-images.githubusercontent.com/93904438/143780775-f8c64e00-17fb-4e72-a643-23bc549e3ce6.png)

After clicking "Ok" it will show an information window saying that the conection to the database was sucesful.

![image](https://user-images.githubusercontent.com/93904438/143781067-47122777-f345-4052-8708-01ad24db1f55.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## CRUD

I assume that you know what CRUD means and what it does, but in case you don't remember I'll create a **VERY little** tutorial here.

After making a query (consult) to the database, you can do one of the follows: 

-**C**reate: Creates data into the database.

-**R**ead: Reads data from the database.

-**U**pdate: Updates the data inside the database.

-**D**elete: Deletes (erases...) data from the database.

> CRUD it's the acronym of all this.

### CREATE

Let's start **creating** some data inside our "_users.sqlite3_" database.

![image](https://user-images.githubusercontent.com/93904438/143804503-19fb9906-14eb-4697-a798-d5c78813e58c.png)

Just fill the fields (you don't need to fill the field "ID" because it's created automatically) and then click the button **"Crear"** our go to the menu **"CRUD"** and select **"Create"**.

If the creation was successful it will show this information window:

![image](https://user-images.githubusercontent.com/93904438/143804706-9573a860-8999-49c9-b085-8762237099d9.png)

If not, this error window will show up, asking us to try it again (usually this error shows up if you forgot to connect to the database):

![image](https://user-images.githubusercontent.com/93904438/143804670-6a6f47fb-6e07-47d4-853b-2eff5fa144f7.png)

### READ

Before explaining how read works in the application, press the button **""Limpar Campos"**" or in the menu **"Limpiar -> "Limpiar Campos"**" to **clean the fields** so we can follow the example.

Now that we have our user created, we want to see his data in the application, for that we need either his **ID** or **Name (Nombre)** or **Lastname (Apellido)** or **Address (Domicilio)**

>**NOTE**: You can't ask to read a user data based on a password. It is forbidden in the application and there is no way to do it. For obvious reasons...

For example, let's do it with his ID (which is UNIQUE and automatically generated for every user):

![image](https://user-images.githubusercontent.com/93904438/143806109-cd234ba3-5ff1-4541-a678-6be541259df0.png)

Click the button **"Leer"** or **"Read"** inside the menu **"CRUD"**.

A information window pops-up saying that the loading was succesful:

![image](https://user-images.githubusercontent.com/93904438/143805953-b2ce82cd-4b19-47cf-9a15-bdce709a8cb1.png)

And the fields are completed based on the ID that we wroted:

![image](https://user-images.githubusercontent.com/93904438/143806230-553d071e-7619-45df-9775-31b2f106064b.png)

In case you try to recover data based on elements that doesn't exist (for example, the user _"Pedro"_) the same information window shows up but the fields are not completed.

### UPDATE

Suppose now that we made a mistake and our user _"Steve"_ last name actually was _"Rogers"_. 

To fix that we can use Update (Actualizar). 

**First**, recover the data from _"Steve"_ to show it on the app with Read (Leer).

![image](https://user-images.githubusercontent.com/93904438/143806771-9f6abc73-be60-4481-8aa5-df4b4ce38f8c.png)

Then make the modifications you want to do. (On this case, change the last name).

![image](https://user-images.githubusercontent.com/93904438/143806810-f0c52133-bc24-40e1-837c-26d06b25b138.png)

Click the button **"Actualizar"** (Update) or from the Menu **"CRUD"** click **"Update"**.

This information window will show up, saying that the update was successful:

![image](https://user-images.githubusercontent.com/93904438/143806889-cdea5b93-108a-4265-9248-470f63058407.png)

Now, if we clean the fields and recover Steve's data, we can see that his last name was updated:

![image](https://user-images.githubusercontent.com/93904438/143806956-def751ce-c535-4308-9da5-6e12c7d20ef7.png) ![image](https://user-images.githubusercontent.com/93904438/143806965-f20346bf-daa9-466a-ba00-51a71334d499.png)

It gives an error if you accidently deleted or forgot to write the user ID (not recommended) 

### DELETE

For example, now we are going to remove the user _"Steve"_ from the database using the button **"Borrar"** (Delete).

In this case we can only do this by using his ID, the application that I created **DOESN'T DELETE the user based on a different field**, just as a safety protocol that I implemented (there could be many users with the same fields but not with the same ID).

As we did before, recover the data from _"Steve"_ using his ID (id = 1). This is a **good practice** to see all fields we are going to delete. 

![image](https://user-images.githubusercontent.com/93904438/143808114-d379227c-2473-48f0-99b3-8426875f3c53.png) ![image](https://user-images.githubusercontent.com/93904438/143808123-64127199-dc21-4f9b-b1b8-d140e76fedec.png)

If you click in the button _"Borrar"_ (Delete) or in the menu _"CRUD"_ -> _"Delete"_ this window will show up asking us if we are sure that we want to delete this data. 

![image](https://user-images.githubusercontent.com/93904438/143808944-85a39481-4b8a-4bac-80c8-4d74bfb3a236.png)

> This is important because once is deleted, usually there is no way to recover the data. But in this application, if you followed the good practice that I recommended before, you can simply click _"Create"_ to create the user again but this time it will have a different ID because this one is auto generated and incremented. This ID will be + 1 than the ID of the last user introduced to the database.

If you click _"Yes"_ it will delete the user **FOREVER**. If you click _"No"_ it will not delete the user.

If you were following the example, this window shows up saying that the delete process was successful:

![image](https://user-images.githubusercontent.com/93904438/143809165-8eedd8fa-5716-4f88-b41e-d7b41d547458.png)

This is the error window saying that there was an error while trying to delete the user. 

> (again, maybe you didn't connected to the database or you forgot to fill the ID field and that's why this window shows up).

![image](https://user-images.githubusercontent.com/93904438/143809055-b853e7d9-3519-4cc2-8df9-d3cd1086072c.png)

Now, if you try to recover the user _"Steve"_ data, the fields will be not completed.

![image](https://user-images.githubusercontent.com/93904438/143883350-5e53e638-cdcc-47cd-afaa-ccf8b853cf39.png) ![image](https://user-images.githubusercontent.com/93904438/143883407-26ca7317-0bb4-4c89-9eab-d51419886410.png) ![image](https://user-images.githubusercontent.com/93904438/143883440-50d22015-f85a-4196-9e78-854dcd44bcbc.png)

## Menu -> Ayuda (Help).

In this menu you will find three options:

### Licencia (License)

This one pop-ups an information window which says that the license is free and in the public domain.

![image](https://user-images.githubusercontent.com/93904438/143809893-33643903-37ae-4b27-975d-86a76e196747.png)

### Acerca... (About...)

It pop-upos an information window about this application saying that was mean as a project created by me (Emanuel Rodriguez Bedeman) and the current version (1.0 BETA).

![image](https://user-images.githubusercontent.com/93904438/143810024-73958896-6779-4aa3-994f-0b9675dcb414.png)

### Instrucciones (Instructions)

It shows up an information window with the instructions (in spanish) of the application, they are a very short explanation of the tutorial that I did here.

![image](https://user-images.githubusercontent.com/93904438/143810015-d18849f9-6e03-4724-a8bb-e021fd66ef7c.png).

## End of the tutorial.

Hope you liked this project and enjoyed playing with it as much as I did, I'll try to keep it udpated with new modifications and Bug fixes. 

Don't hesitate to suggest a modification!

> (_next update: posting the code and the .exe_)
