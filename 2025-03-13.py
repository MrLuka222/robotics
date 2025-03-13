#today i learned how to use the elif in my code
login = input("please input your login: ")
if login == "Mark":
  print("Ah! Hello Mark, please input your password to comfirm:")
  password = input("please input your password: ")
  if password == "password":
    print("Welcome Mark!")
  elif password == "Password":
    print("hint no caps")
  else:
    print("incorrect.")
else:
  print("Unknown login. Please try again.")
