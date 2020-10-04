def c_to_f(c_temp):
  farenheit=(9/5)*c_temp + 32
  return farenheit

def f_to_c(f_temp):
  celsius=5*(f_temp-32)/9
  return celsius

temp=int(input("Enter the tempertature:"))
temp_type=str(input("Enter the temperature type in which you want to convert,type celsius or farenheit:"))

if temp_type=='celsius':
  celsius=f_to_c(temp)
  print("The temperaturte in celsius is:",round(celsius,2))

elif temp_type=='farenheit':
  farenheit=c_to_f(temp)
  print("The temperaturte in farenheit is:",round(farenheit,2))

else:
  print("The conversion is beyond my abilities")
