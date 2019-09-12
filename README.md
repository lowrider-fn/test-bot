## Deploy python environment for Ubuntu
```
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install python3-venv
python3 -m venv env
```
## Activate and deactivate env
```
source env/bin/activate
deactivate
```
#### Create ``` requirements.txt ``` file in the root of the project directory

#### Create dependenses list 
```
pip freeze
```
#### install dependenses
``` 
pip install -r requirements.txt
```
