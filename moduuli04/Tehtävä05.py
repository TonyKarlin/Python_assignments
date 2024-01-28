# Tehtävä05

failures= 0
max_failures = 5

username = ("python")
password = ("rules")

while failures < max_failures:
    what_username = (input('Enter your username: '))
    what_password = (input("Enter your password: "))

    if what_username.lower() == username.lower() and what_password == password: # Salasana tarkempi kuin käyttäjätunnus.
        print(f"Welcome, {username}!")
        break
    else:
        print("Invalid username or password.")
        failures += 1
if failures == max_failures:
    print("Access denied.")






