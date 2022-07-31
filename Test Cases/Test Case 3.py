#Test Case 3

def temperature_converter(celcius_temp):    # this program takes input of temp in Celcius
                                            #and converts to Farenheit 


    farenheit_temp = (celcius_temp * (9/5)) - 32 # + has been changed to - to make incorrect code

    return farenheit_temp

    
if temperature_converter(40) == 104 and temperature_converter(50) == 122:
    print("Test Successful")

else:
    print("Test Failed")
        
    
  
