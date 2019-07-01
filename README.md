# HelloWorldWebsite
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
  2.) Unzip the folder and open it in some IDE or some code-editor like - PyCharm, VS-Code, Atom, etc.<br>
  3.) Set up a virtual environment fot it.<Br>
  Open the terminal in the current folder and write the given command.

```
virtualenc <foldername> <path>
```
*For Example:*
```
virtualenc venv .
```
It will create a virtual environment with a folder name - *venv* in the current directory<br>
4.) Now activate the virtual environment by writing the following command: <br>
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
5.) Change the path to the main folder (where the manage.py and requirements.txt files are present)<br>
6.) Install all the requirements in the requirements.txt file by using pip
```
pip install -r requirements.txt
```
7.) After installing you can verify whether all the requirements have been installed or not by using:
```
pip freeze
```
8.)After the installation process have been finished, you can run the development server by:<br>
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
