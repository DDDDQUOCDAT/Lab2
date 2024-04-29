bmi=0
weight=0
height=0
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/(height*height)
    print("bmi = " + str(bmi))
    if(bmi<18.5):
        print("Under weight")
        return -1

    if(bmi>25.0):
        print("Over Weight")
        return 1

    if(bmi>=18.5 and bmi<=25.0):
        print("normal Weight")
        return 0
    
calculate_bmi(weight=57, height=1.73)
