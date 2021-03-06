def area_triangle(base,height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle (7,3)

sum = area_a + area_b
print ("the sum of both areas is:  " + str(sum))


def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a+amount_b
print("This many seconds: " +str(result))


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes *60
    return hours,minutes,remaining_seconds 

hours, minutes, seconds = convert_seconds (5000)
print (hours, minutes, seconds)
