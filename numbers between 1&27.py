n = int(input("Enter n ( >=3 ): "))

if n >= 3:

    # -------------------------------------------------------
    # -----[first print the phrase outside the loop!]--------
    # -------------------------------------------------------

    print("numbers between 1 and 27 divisible by 3 or 5 are:")

    for numbers in range(1, n+1):
        if numbers % 3 == 0 or numbers % 5 == 0:

            print(numbers,"",end='')
else:
    print("Wrong input n must be >= 3")

# -------------------------------------------
# ------------------[DONE]-------------------
# -------------------------------------------