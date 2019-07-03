# Hello World Website
The WebApp cum Website is under development. <br>
Link for the development server: 
<Br>
http://hello-world15.herokuapp.com/

**Note: For the contributors-**
You are free to make changes in this repository. Just be under some code of conduct while contributing and please follow the rules as mentioned
<br>
The Website is made with the help of Django Framework. So the contributor having knowledge of HTML, CSS, Javascript, Python can contribute to this repository.
<bR>
  <h3>Setting up the WebApp</h3>
  1.) Clone the projectc onto your local machine.<Br>
  <Br>2.) Unzip the folder and open it in some IDE or some code-editor like - PyCharm, VS-Code, Atom, etc.<br>
  <br>3.) Set up a virtual environment fot it.<Br>
  Open the terminal in the current folder and write the given command.

```
virtualenc <foldername> <path>
```
*For Example:*
```
virtualenc venv .
```
It will create a virtual environment with a folder name - *venv* in the current directory<br>
<br>4.) Now activate the virtual environment by writing the following command: <br>
*FOR WINDOWS*<Br>
```
cd venv/scripts
```
then 
```
activate .
```
<Br>
  
*FOR MACBOOK and LINUX*
<br>
```
source venv/scripts/activate
```
This will activate the virtual environment. You can assure it by seeing *(venv)* in front of the C:/path
<Br>5.) Change the path to the main folder (where the manage.py and requirements.txt files are present)<br>
  You can change it by - change directory (cd) command.
```
cd <path name>
```
<Br>
##For previous directory
```
cd ../
```  
## For current directory
<br>
<br>6.) Install all the requirements in the requirements.txt file by using pip
```
pip install -r requirements.txt
```
<br>7.) After installing you can verify whether all the requirements have been installed or not by using:
```
pip freeze
```
<br>8.)After the installation process have been finished, you can run the development server by:<br>
*FOR WINDOWS*
```
python manage.py runserver <port>
```
For Example: 
```
python manage.py runserver 8000
```
It will start the development server on port 8000, that's -> 127.0.0.1:8000 or localhost:8000
<Br>
*SAME FOR MACBAOOK and LINUX*
<Br>
```
python3 manage.py runserver <port>
```
<br>9.)Now you can go through the App and make changes and contribute to the Open Source
  
## Code of Conduct
Please be specific in writing code. Before writing it, please understand how the previous code is regulated.

### In HTML File:
After writing the code for a particular division, please leave 2 lines after each block. Also, be sure to comment it before and after writing it. So, that if any other contributor wants some changes, then he/she can do it easily.

### In CSS File:
After defining css for a class, id, attribute, or the element tag itself, then:<br>
-- Leave one line after defining the CSS for the the parent and its children block element in the HTML file.<br>
-- Leave two lines after defining the CSS for the another parent element
