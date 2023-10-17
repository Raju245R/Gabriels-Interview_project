- 👋 Hi, I’m @Raju245R

Steps to Run Project

Download Project and Extact it.

Step 1

Open mysql table creation queries.docx (location : Gabriels>mysql table creation queries.docx) Copy Queries and Paste it in the MYSQL Workbench Then , Execute. Now Database and Table have created with records populated.

Note

We have used longblob field for userprofile image 1.Inorder to use local images, Images Must be stored in (C:\ProgramData\MySQL\MySQL Server 8.0\Uploads) path . Because, which is MySQL Server Environmental Path. (If any doubts, you can refer the document (mysql table creation queries.docx)).

Step 2

Open VSCode and Open the Project Folder . In VSCode Open Settings.py

Add this things in this settings.py

*In Database - 'default': {'ENGINE': 'django.db.backends.mysql', 'NAME': ' ', 'USER':' ', 'PASSWORD':' ', 'HOST':'<'your localhost'> ', 'PORT':''}

In cmd Prompt *pip install pymysql #for creating model as Existing Table *pip install pybase64 #for converting binary to image type (Encoding & Decoding)

Step 3

In VSCode Terminal or cmd Prompt in project location ** py manage.py runserver
