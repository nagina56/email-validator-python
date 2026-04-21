# email=input("Enter your Email: ")
# k,j,d=0,0,0
# if len(email) >= 6:
#     if email [0] .isalpha():
#         if("@" in email) and (email.count("@")==1):
#             if(email [-4]==".") ^ (email [-3]=="."):
#                for i in email:
#                    if i==i.isspace():
#                        k=1
#                    elif i.isalpha():
#                        if i==i.upper():
#                            j=1
#                    elif i.isdigit():
#                       continue
#                    elif i=="_" or i=="." or i=="@":
#                       continue
#                    else:
#                        d=1
#                if k==1 or j==1 or d==1:
#                   print("Wrong Email 5")
#                else:
#                    print("Right Email")
                             
#             else:
#                 print("Wrong Email 4")
#         else:
#             print("Wrong Email 3")
        
#     else:
#         print("Wrong Email 2")
# else:
# #     print("Wrong Email 1")


# email = input("Enter your Email: ")

# if len(email) < 6:
#     print("Wrong Email: Too short")

# elif not email[0].isalpha():
#     print("Wrong Email: Must start with a letter")

# elif email.count("@") != 1:
#     print("Wrong Email: Must contain exactly one @")

# else:
#     at_index = email.index("@")
#     dot_index = email.rfind(".")

#     # @ ke baad dot hona chahiye
#     if at_index > dot_index:
#         print("Wrong Email: . must come after @")

#     # dot end ke bohat qareeb na ho
#     elif dot_index >= len(email) - 2:
#         print("Wrong Email: Invalid domain")

#     else:
#         valid = True

#         for i in email:
#             if i.isspace():
#                 valid = False
#             elif not (i.isalnum() or i in ["@", ".", "_"]):
#                 valid = False

#         if valid:
#             print("Right Email ✅")
#         else:
#             print("Wrong Email: Invalid characters")

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9] + [@]\w+[.]\w {2,3}$"
user_email=input('Enter your Email : ')

if re.search(email_condition,user_email):
    print(" Right Email ")

else:
    print( " Wrong Email " )