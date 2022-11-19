‘’’Build a python code, temperature and humidity values assume 
 (generated with random function to a variable) and write a 
Conditon to continuously detect alarm in 
 Case of high temperature’’’ 
#import the necessary package! 
Import requests 
From bs4 import BeautifulSoup 
Import random 
From time import * 
Gate=True 
#input the city name 
Def run_city(): 
  City = input(‘input the city name :’) 
  Print(city) 
 
# or you can also hard-code the value 
 
 
#Display the message! 
  Print(‘Displaying Weater report for: ‘ + city) 
 
#fetch the weater details 
  url = ‘https://www.google.co.in/search?q=weather+{}’.format(city) 
  res = requests.get(url) 
 
#display the result! 
  Print(res.text) 
 
#temprature searching 
While(gate): 
    Temperature = random.randint(1,50) 
    Humidity = random.randint(10,50) 
    If temperature>45 and humidity<50: 
        Print( “Temperature=”,temperature) 
        Print(“Humidity=”,humidity) 
         
        Print(“Alert message in Activate”) 
        Gate=False 
    Else: 
        Print(“Temperature=”,temperature) 
        Print(“Humidity=”,humidity) 
    Sleep(1); 
 
#enter temprature value 
X= int(input(“Please enter the Humidity value :”)) 
Y= int(input(“Please enter the temperature value  :”)) 
Z=print(x,y) 
Print(z) 
If x == 30: 
    Print(“Due to Temperature is Normal place”) 
If x < 45: 
        Print(“your Temperature is Normal…”) 
If x > 70: 
            Print(“your Temperature is High…”) 
If y == 30: 
    Print(“Due to Humidity report is Normal place”) 
If y < 45: 
        Print(“your Humidity is Normal”) 
If y > 55: 
            Print(“your Humidity is High”) 
 
 
 
 
 
While True: 
    Run_city() 
