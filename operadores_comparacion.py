# comparisons

if 5 > 4:
    print("N")
    
if 4 < 5:
    print("Y")
    
if "name" == "NAME":
    print("N")
    
if 10 % 2 == 0:
    print("E")
    
if 10 % 3 == 0:
    print("T")
    
if (4 * 6) == 24:
    print("S")
    
food = input("What's the best food?: ")

if food == "rice":
    print("Yes, rice is the best.")
elif food == "apple":
    print("Apples aren't my cup of rice.")
elif food == "mondongo":
    print("It's delicius")
else:
    print("Never heard of it!")
    
# your first while loop: can you gess what it does?

limit = 100

counter = 1

while counter <= limit:
    print(counter)
    counter = counter + 1
    
names_i_like = ['Thomson', 'Thompson', 'Haddock', 'Snowy', 'Kevin', 'Cristian']

for name in names_i_like:
    print(f"I like this name: {name}")
    
for number in range(2, 13, 2):
    print(number)