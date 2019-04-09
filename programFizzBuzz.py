#program to print the numbers 1 to 100

for num in range(1,101):
        #print(num)


        if num%3==0 and num%5==0:
            print("FizzBuzz")

        elif num % 3 == 0:
            print ("Fizz")

        elif num % 5==0:
            print("Buzz")

        else:
            print(num)

        

    






