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