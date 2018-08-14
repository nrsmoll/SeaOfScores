

def AqolScore():
    #Q1. Household Help
    Q1 = q1.get()
    # Q1. Household Help
    if Q1 == 1:
        dvQ1 = 0
    elif Q1 == 2:
        dvQ1 = 0.073
    elif Q1 == 3:
        dvQ1 = 0.435
    elif Q1 == 4:
        dvQ1 = 0.820
    elif Q1 == 5:
        dvQ1 = 1
    else:
        dvQ1 = np.NaN

    #Q2. Getting Around Outside
    if Q2 == 1
        dvQ2 = 0
    replace
    dvQ2 = 0.033 if Q2 == 2
    replace
    dvQ2 = 0.240 if Q2 == 3
    replace
    dvQ2 = 0.471 if Q2 == 4
    replace
    dvQ2 = 0.840 if Q2 == 5
    replace
    dvQ2 = 1 if Q2 == 6

    ** *3.
    Mobility
    generate
    dvQ3 = 0 if Q3 == 1
    replace
    dvQ3 = 0.041 if Q3 == 2
    replace
    dvQ3 = 0.251 if Q3 == 3
    replace
    dvQ3 = 0.570 if Q3 == 4
    replace
    dvQ3 = 0.830 if Q3 == 5
    replace
    dvQ3 = 1 if Q3 == 6

    ** *4.
    Personal
    Care
    generate
    dvQ4 = 0 if Q4 == 1
    replace
    dvQ4 = 0.040 if Q4 == 2
    replace
    dvQ4 = 0.297 if Q4 == 3
    replace
    dvQ4 = 0.797 if Q4 == 4
    replace
    dvQ4 = 1 if Q4 == 5

    ** *Dimension
    2.
    Relationships

    ** *5.
    Intimate
    generate
    dvQ5 = 0 if Q5 == 1
    replace
    dvQ5 = 0.074 if Q5 == 2
    replace
    dvQ5 = 0.461 if Q5 == 3
    replace
    dvQ5 = 0.841 if Q5 == 4
    replace
    dvQ5 = 1 if Q5 == 5

    ** *6.
    Family
    Role
    generate
    dvQ6 = 0 if Q6 == 1
    replace
    dvQ6 = 0.193 if Q6 == 2
    replace
    dvQ6 = 0.759 if Q6 == 3
    replace
    dvQ6 = 1 if Q6 == 4

    ** *7.
    Community
    Role
    generate
    dvQ7 = 0 if Q7 == 1
    replace
    dvQ7 = 0.197 if Q7 == 2
    replace
    dvQ7 = 0.648 if Q7 == 3
    replace
    dvQ7 = 1 if Q7 == 4

    ** *Dimension
    3.
    Mental
    Health

    ** *8.
    Despair
    generate
    dvQ8 = 0 if Q8 == 1
    replace
    dvQ8 = 0.133 if Q8 == 2
    replace
    dvQ8 = 0.392 if Q8 == 3
    replace
    dvQ8 = 0.838 if Q8 == 4
    replace
    dvQ8 = 1 if Q8 == 5

    ** *9.
    Worried
    generate
    dvQ9 = 0 if Q9 == 1
    replace
    dvQ9 = 0.142 if Q9 == 2
    replace
    dvQ9 = 0.392 if Q9 == 3
    replace
    dvQ9 = 0.824 if Q9 == 4
    replace
    dvQ9 = 1 if Q9 == 5

    ** *10.
    Sad
    generate
    dvQ10 = 0 if Q10 == 1
    replace
    dvQ10 = 0.097 if Q10 == 2
    replace
    dvQ10 = 0.330 if Q10 == 3
    replace
    dvQ10 = 0.784 if Q10 == 4
    replace
    dvQ10 = 1 if Q10 == 5

    ** *11.
    Calm
    generate
    dvQ11 = 0 if Q11 == 1
    replace
    dvQ11 = 0.064 if Q11 == 2
    replace
    dvQ11 = 0.368 if Q11 == 3
    replace
    dvQ11 = 0.837 if Q11 == 4
    replace
    dvQ11 = 1 if Q11 == 5

    ** *Dimension
    4.
    Coping

    ** *12.
    Energy
    generate
    dvQ12 = 0 if Q12 == 1
    replace
    dvQ12 = 0.056 if Q12 == 2
    replace
    dvQ12 = 0.338 if Q12 == 3
    replace
    dvQ12 = 0.722 if Q12 == 4
    replace
    dvQ12 = 1 if Q12 == 5

    ** *13.
    Control
    generate
    dvQ13 = 0 if Q13 == 1
    replace
    dvQ13 = 0.055 if Q13 == 2
    replace
    dvQ13 = 0.382 if Q13 == 3
    replace
    dvQ13 = 0.774 if Q13 == 4
    replace
    dvQ13 = 1 if Q13 == 5

    ** *14.
    Coping
    generate
    dvQ14 = 0 if Q14 == 1
    replace
    dvQ14 = 0.057 if Q14 == 2
    replace
    dvQ14 = 0.423 if Q14 == 3
    replace
    dvQ14 = 0.826 if Q14 == 4
    replace
    dvQ14 = 1 if Q14 == 5

    ** *Dimension
    5.
    Pain

    ** *15.
    Serious
    pain
    generate
    dvQ15 = 0 if Q15 == 1
    replace
    dvQ15 = 0.133 if Q15 == 2
    replace
    dvQ15 = 0.642 if Q15 == 3
    replace
    dvQ15 = 1 if Q15 == 4

    ** *16.
    Pain
    generate
    dvQ16 = 0 if Q16 == 1
    replace
    dvQ16 = 0.200 if Q16 == 2
    replace
    dvQ16 = 0.758 if Q16 == 3
    replace
    dvQ16 = 1 if Q16 == 4

    ** *17.
    Pain
    interferes
    generate
    dvQ17 = 0 if Q17 == 1
    replace
    dvQ17 = 0.072 if Q17 == 2
    replace
    dvQ17 = 0.338 if Q17 == 3
    replace
    dvQ17 = 0.752 if Q17 == 4
    replace
    dvQ17 = 1 if Q17 == 5

    ** *Dimension
    6.
    Senses

    ** *18.
    Vision
    generate
    dvQ18 = 0 if Q18 == 1
    replace
    dvQ18 = 0.033 if Q18 == 2
    replace
    dvQ18 = 0.223 if Q18 == 3
    replace
    dvQ18 = 0.621 if Q18 == 4
    replace
    dvQ18 = 0.843 if Q18 == 5
    replace
    dvQ18 = 1 if Q18 == 6

    ** *19.
    Hearing
    generate
    dvQ19 = 0 if Q19 == 1
    replace
    dvQ19 = 0.024 if Q19 == 2
    replace
    dvQ19 = 0.205 if Q19 == 3
    replace
    dvQ19 = 0.586 if Q19 == 4
    replace
    dvQ19 = 0.826 if Q19 == 5
    replace
    dvQ19 = 1 if Q19 == 6

    ** *20.
    Communicate
    generate
    dvQ20 = 0 if Q20 == 1
    replace
    dvQ20 = 0.187 if Q20 == 2
    replace
    dvQ20 = 0.695 if Q20 == 3
    replace
    dvQ20 = 1 if Q20 == 4
