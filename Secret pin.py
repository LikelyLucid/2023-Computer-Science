pin = 1234
attempt = 0
while attempt != pin:
    try:
        attempt = int(input("Enter the Pin: "))
    else:
        print("bro what the heck, put in the right code")