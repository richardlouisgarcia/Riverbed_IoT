# Riverbed_IoT
Here are instructions on how to use the code:


# Make a directory
mkdir ~/projects

#Cd to directory
cd ~/projects

#get code
git clone https://github.com/Jeffhdavidson/Riverbed_IoT.git

#cd to project
cd 

#install required dependencis
pip install -r requirements.txt

#to test run the following
python test.py

#to use the function add following to your code
from function import upload

#Here is the format to use function
returncode = upload(ID,SensorData)
