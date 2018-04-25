  Here are instructions on how to use the code:

  First time using Python? Setup your environment
     
     #Validate you have Python
      python --version
      <Python 2.7 or Python 2.x.x>

      #Validate you have pip
      pip --version
      <pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 2.X)>

      #Install virtualenv for create isolated Python environment and dependency manager
      pip install virtualenv
      
      #Test intsall
      virtualenv --version
      <15.1.0>
      
      #Make a directory
      mkdir Development

      #Switch to directory
      cd Development
      
      #Create your virtual environment
      virtualenv my_project
      
      #Start the virtual environment
      source my_project/bin/activate
      
              #When you wish to exit the virtual environment
              deactivate

              #To return to virtual environment
              workon my_project

You can now download the code and start building:

      #get code
      git clone https://github.com/Jeffhdavidson/Riverbed_IoT.git

      #Switch to project folder
      cd Riverbed_IoT

      #install required dependencis
      sudo pip install -r requirements.txt

      #to test run the following. A return code of 200 means it works!
      python basic_function_test.py

      #to use the function add following to your code (look at test.py as example)
      from function import upload
      returncode = upload(username,UUID,Moisture,temp,humidity)

      #Here is the function usage example
      returncode = upload(Jdavidson, 690592e3-e919-4ec5-a948-bc7d29709f27, 33, 14, 22)

      #Variable descriptions
      returncode = HTTP return code; 200=OK 500=server error etc.
      username = your username
      UUID = sensor unique identification number
      Moisture = moisture level
      temp = temperature in Celsius
      humidity = percent humidity
      
Validate your data uploaded:

    http://40.70.0.179:8080/sensor/
