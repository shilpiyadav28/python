#string challenge
#Replace function = replace.("old value","new value")
#convert a messy number into clean phone number
# "+49 (176) 123-4567"

phone_number = "+49 (176) 123-4567"

print(phone_number.replace('+','00').replace(" ","").replace("(","").replace(")","").replace("-",""))


#convert "968 - Maria" , ( D@t@ Engineer ) ;; 27y " to clean structure
# name : maria | role : data Engineer | age : 27

data = '"968 - Maria" , ( D@t@ Engineer ) ;; 27y '

#first do strip to remove unwanted spaces
data2 = data.strip()
print(data2)

#split the age left part and age part
left_part,age_part = data2.split(';;')
print(left_part)
print(age_part)

#cleaning age part
age_part = age_part.replace('y',"").strip()
print(age_part)

#divide left part into name part and role part
name_part,role_part = left_part.split(',')
print(name_part)
print(role_part)

print('length of name before cleaning : ', len(name_part))
print('length of role before cleaning : ', len(role_part))

#cleaning name part
name_part = name_part.replace("968 - ","").replace('"',"").lower()
print(name_part)
print('length of name after cleaning : ', len(name_part))

#cleaning role part
role_part = role_part.replace('(',"").replace(')',"")
role_part = role_part.strip().replace("@",'a').replace('D','d')
print(role_part)
print('length of role after cleaning : ', len(role_part))

#final output
print(f"name : {name_part} | role : {role_part} | age : {age_part}")

