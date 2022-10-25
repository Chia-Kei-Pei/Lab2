def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Add code here to calculate BMI
    bmi = weight / (height * height);

    # Add code here to display calculate BMI
    print("BMI = " + str(bmi))

    # weight classification
    if bmi < 18.5:
        weight_class = "Under Weight"
    elif 18.5 <= bmi <= 25.0:
        weight_class = "Normal Weight"
    elif bmi > 25.0:
        weight_class = "Over Weight"

    print("Weight Classification = " + weight_class)

calculate_bmi(weight=57, height=1.73)
