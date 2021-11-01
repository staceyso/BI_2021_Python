This is an updated research on virtual environments (https://github.com/krglkvrmn/Virtual_environment_research).
The article is available at doi:10.1111/1000-7. Plase, cite it.

The script was tested on:
OS Version: Ubuntu 20.04.3 LTS,
Python version: Python 3.9.5

Python 3.9 is required. You can check if you have it:
```
python 3.9 --version
```
Or install it (if needed):
```
sudo apt-get install python 3.9
```
Git is required as well (to download data from this remote repository):
```
sudo apt install git
```
Install pip:
```
sudo apt install python3-pip
```
Install venv (virtual environment):
```
sudo apt-get install python3.9-venv
```
Clone this repository:
```
git clone https://github.com/staceyso/BI_2021_Python.git
```
And open:
```
cd BI_2021_Python/
```
Then switch to this branch:
```
git checkout homework_4
```
Create your virtual environment:
```
python3.9 -m venv pain
```
And activate it:
```
source pain/bin/activate
```
Install required packages into the virtual environment:
```
pip install -r requirements.txt
```
And run pain.py file with Python 3.9:
```
python3.9 pain.py
```
After you finish, you can exit the file
And deactivate virtual environment:
```
deactivate
```

