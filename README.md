## What is this about?
- A basic data entry web page made with the Django framework available in the Python programming language.
- This was made during the CodeRun-2024 competition.
- The data entry application had to be created within the context of an ongoing investigation where participants (witnesses, suspects, detectives and victims) would be added to a database.

![[images/actors-page.png]]
![[images/Sherloc-Holmes.png]]

## Installaiton

#### Step 1:

Using the `git clone` command inside your operating system's CLI you can copy this repository to your local machine in a directory/folder of your choice:

```bash
git clone https://github.com/DanNicolaeBoca/basic-data-entry-django.git
```

#### Step 2:

You need to make sure to create and activate a virtual enviroment that has `pip` and `django` installed:

###### Option 1 (Using `conda`, needs to be installed beforehand): 
```bash
conda create -n testDjango
conda activate testDjango
conda install pip
pip install django
```

You can replace "testDjango" with the name of your choice. Also make sure that `(<name_you_chose>)` is present in your CLI prompt before intsalling packages.

###### Option 2 (Using `python3 - m venv`):
Run the following commands in the cloned repository or somewhere you have access to (maybe a folder/directory where your virtual enviroments are stored):
```bash
python3 -m venv testDjango
```

Now for the next two chose the appropiate one:

- On Linux/MacOS (for bash/zsh shells):
```bash
source testDjango/bin/activate
```
- On Windows:
```bash
source testDjango/bin/Activate.ps1
```

Finally install `django`: 
```bash
pip install django
```

#### Step 3:
- Run the server by typing this command in the cloned repository:
```bash
python3 manage.py runserver
```
- Leave this running and go to the following link in your browser [http://localhost:8000/actors/](http://localhost:8000/actors/)
- Now everything should be ready to go! ;)
