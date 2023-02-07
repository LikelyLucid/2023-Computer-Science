pin = 1234
attempt = 0
while attempt != pin:
    try:
        attempt = int(input("Enter the Pin: "))
    except:
        print("bro what the heck, put in the right code")