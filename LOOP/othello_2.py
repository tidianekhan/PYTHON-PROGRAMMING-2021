time_1 = int(input("Enter the time the black player thought: "))
time_2 = int(input("Enter the time the white player thought: "))




if time_1 > time_2:
    millis = int(time_1)
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (millis / (1000 * 60 * 60)) % 24
    "%02d:%02d:%02d" % (hours, minutes, seconds)
    print("The time the human player has spent thinking is:  %02d:%02d:%02d" % (hours, minutes, seconds))

if time_2 > time_1:
    millis = int(time_2)
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (millis / (1000 * 60 * 60)) % 24
    "%02d:%02d:%02d" % (hours, minutes, seconds)
    print("The time the human player has spent thinking is:  %02d:%02d:%02d" % (hours, minutes, seconds))




