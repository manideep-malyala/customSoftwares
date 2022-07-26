dayCheck= int(input("Check Cheyavalasina Vaaramunu Enter Cheyamdi : "))
plus_count_val = int(input("Initial Value 5088 Ku Amtha Kalapalo Enter Cheyamdi : " ))
month_count = int(input("Month Count Ni Add Cheyamdi : "))
day_model_english =  { 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
day_to_check = day_model_english[dayCheck]
initial_fix_val = 5088

step_one_val = initial_fix_val + plus_count_val
print("\n\n-----------STEP ONE---------\n\n")
print("DAY TO TO CHECKED: {} ".format(day_to_check))
print("INITIAL VALUE : {}".format(initial_fix_val))
print("VALUE TO BE ADDED TO {} IS : {}\n".format(initial_fix_val, plus_count_val))
print("{} +  {} = {} ".format(initial_fix_val,plus_count_val,step_one_val))
print("\nAnswer --> {}".format(step_one_val))
print("\n-----------------------------\n")

step_two_val = step_one_val * 12

step_two_ans = step_two_val + month_count
print("\n\n\n-----------STEP TWO---------\n\n")
print("{} + {} = {}".format(step_two_val,month_count, step_two_ans))
print("\nAnswer --> {} ".format(step_two_ans))
print("\n---------------------------\n")

print("\n\n\n-----------STEP THREE-----------\n\n")
stv = step_two_ans*183
print("{} * 183 = {} ".format(step_two_ans, stv))
print("\nAnswer --> {}".format(stv))
print("\n\n-----------------------------------\n\n")

print("\n\n\n-----------STEP FOUR---------\n\n")
into_5954 = 5954
qt_5954_stv = stv//into_5954
rem_5954_stv = stv%5954
print("{} {} {} {} {}".format(into_5954,")",stv, "(", qt_5954_stv))
print("          {}".format(into_5954*qt_5954_stv))
print("             -------\n              {} \n             -------".format(rem_5954_stv))
print("\nAnswer --> {}".format(qt_5954_stv))
print("\n\n---------------------------------\n\n")

print("\n\n\n-----------STEP FIVE-----------\n\n")
v = step_two_ans + qt_5954_stv
print("{} + {} = {}".format(step_two_ans,qt_5954_stv,v))
print("\nAnsewer --> {}".format(v))

print("\n\n\n-----------STEP SIX-----------\n\n")
x = v * 30
print("{} * 30 = {}".format(v,x))
print("\nAnswer --> {}".format(x))
print("\n\n---------------------------------\n\n")


print("\n\n\n-----------STEP SEVEN-----------\n\n")
y = x * 144
print("{} * 144 = {}".format(x,y))
print("\nAnswer --> {}".format(y))
print("\n\n---------------------------------\n\n")



print("\n\n\n-----------STEP EIGHT---------\n\n")
into_9203 = 9203
qt_9203_stv = y//into_9203
rem_9203_stv = y%9203
print("{} {} {} {} {}".format(into_9203,")",y, "(", qt_9203_stv))
print("          {}".format(into_9203*qt_9203_stv))
print("             -------\n              {} \n             -------".format(rem_9203_stv))
print("\nAnswer --> {}".format(qt_9203_stv))
print("\n\n---------------------------------\n\n")


print("\n\n\n-----------STEP NINE-----------\n\n")
z = x - qt_9203_stv
print("{} - {} = {}".format(x,qt_9203_stv,z))
print("\nAnswer --> {}".format(z))
print("\n\n---------------------------------\n\n")


print("\n\n\n-----------STEP TEN---------\n\n")
into_7 = 7
qt_7_stv = z//into_7
rem_7_stv = z%7
print("{} {} {} {} {}".format(into_7,")",z, "(", qt_7_stv))
print("     {}".format(into_7*qt_7_stv))
print("       -------\n          {} \n       -------".format(rem_7_stv))
print("\nAnswer --> {}".format(rem_7_stv))
print("\n\n---------------------------------\n\n")

day_tel = {1:"Friday", 2:"Saturday", 3:"Sunday", 4:"Monday", 5:"Tuesday", 6:"Wednesday", 7:"Thursday"}
for key in day_tel:
  if day_tel[key] == day_to_check:
    temp = key
    break

if rem_7_stv == 0:
  rem_7_stv =7
print("Value of {} --> {}".format(day_to_check, temp))

if temp == rem_7_stv:
  print("MATCH SUCCESSFUL")
  print("ADJUSTMENT IS --> 0")
  flag=-1
  diff =0
else:
  print("MATCH UNSUCCESSFULL, NEED ADJUSTMENT ")

  if temp > rem_7_stv:
    diff = temp - rem_7_stv
    diff_str = "+"+str(diff)
    flag =1
  else:
    diff = (rem_7_stv - temp) * -1
    diff_str = "-"+str(diff)
    flag =0

  print("ADJUSTMENT IS --> {}".format(diff_str))

print("\n\n\n-----------STEP ELEVEN---------\n\n")
val = z + diff
if flag==1:
  print("{} + {} = {}".format(z,abs(diff),val))
elif flag==0:
  print("{} - {} = {}".format(z,abs(diff),val))
else:
	pass

into_16 = 16
qt_16_stv = val//into_16
rem_16_stv = val%16
print("\n{} {} {} {} {}".format(into_16,")",val, "(", qt_16_stv))
print("       {}".format(into_16*qt_16_stv))
print("         -------\n           {} \n         -------".format(rem_16_stv))
print("\nKALANITYA --> {}".format(rem_16_stv))
print("\n\n---------------------------------\n\n")


print("\n\n\n-----------STEP TWELVE---------\n\n")
into_36 = 36
qt_36_stv = val//into_36
rem_36_stv = val%36
print("{} {} {} {} {}".format(into_36,")",val, "(", qt_36_stv))
print("     {}".format(into_36*qt_36_stv))
print("       -------\n          {} \n       -------".format(rem_36_stv))
print("\nDIVASAM --> {}".format(rem_36_stv))
print("\n\n---------------------------------\n\n")

print("\n\n\n-----------STEP THIRTEEN---------\n\n")
into_9 = 9
qt_9_stv = val//into_9
rem_9_stv = val%9
print("{} {} {} {} {}".format(into_9,")",val, "(", qt_9_stv))
print("     {}".format(into_9*qt_9_stv))
print("       -------\n          {} \n       -------".format(rem_9_stv))
print("\nVASARAM --> {}".format(rem_9_stv))
print("\n\n---------------------------------\n\n")

print("\n\n\n-----------STEP FOURTEEN---------\n\n")
into_5 = 5
qt_5_stv = val//into_5
rem_5_stv = val%5
print("{} {} {} {} {}".format(into_5,")",val, "(", qt_5_stv))
print("     {}".format(into_5*qt_5_stv))
print("       -------\n          {} \n       -------".format(rem_5_stv))
print("\nGHATIKA --> {}".format(rem_5_stv))
print("\n\n---------------------------------\n\n")