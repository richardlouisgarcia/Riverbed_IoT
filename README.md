
  Riverbed_IoT
  Here are instructions on how to use the code:

  First time using Python? Setup your environment
      Validate you have Python
      python --version

      Validate you have pip
      pip --version

      Install virtualenv for create isolated Python environment and dependency manager
      pip install virtualenv
      
      Test intsall
      virtualenv --version
      
      Make a directory
      mkdir Development

      Cd to directory
      cd Development
      
      Create your virtual environment
      virtualenv my_project
      
      Start the virtual environment
      source my_project/bin/activate
      
              #When you wish to exit the virtual environment
              deactivate

              #To return to virtual environment
              workon my_project

You can now download the code and start building:
      #get code
      git clone https://github.com/Jeffhdavidson/Riverbed_IoT.git

      #cd to project folder
      cd Riverbed_IoT

      #install required dependencis
      pip install -r requirements.txt

      #to test run the following. A return code of 200 means it works!
      python test.py

      #to use the function add following to your code
      from function import upload

      #Here is the function description and usage
      returncode = upload(ID,SensorData)

      #returncode = HTTP return code; 200=OK 500=server error
      #ID = sensor identification number
  #SensorData = raw sensor data

*/
