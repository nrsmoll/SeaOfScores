


Q1list = [
        ("I can do all these tasks very quickly and efficiently without any help", 1),
        ("I can do these tasks relatively easily without help", 2),
        ("I can do these tasks only very slowly without help", 3),
        ("I cannot do most of these tasks unless I have help", 4),
        ("I can do none of these tasks by myself.", 5),
    ]
Label(win, text="Q1. How much help do you need with jobs around your place of residence (eg preparing food, cleaning, gardening)?", justify = LEFT, wraplength=500 ).grid(row=3, columnspan=2)
q1 = IntVar()
for text, value in Q1list:
    b = Radiobutton(win, text=text, variable=q1, value=value)
    b.grid(sticky='W', rowspan=5, columnspan=2)


Q2list = [
        ("getting around is enjoyable and easy", 1),
        ("I have no difficulty getting around outside my place of residence", 2),
        ("I have a little difficulty", 3),
        ("I have moderate difficulty", 4),
        ("I have a lot of difficulty", 5),
        ("I cannot get around unless somebody is there to help me.", 6)
    ]
Label(win, text="Q2. How easy or difficult is it for you to get around by yourself outside your place of residence (eg to go shopping, visiting)?", justify = LEFT, wraplength=500 ).grid(rowspan=2, columnspan=2)
q2 = IntVar()
for text, value in Q2list:
    b = Radiobutton(win, text=text, variable=q2, value=value)
    b.grid(sticky='W', rowspan=6, columnspan=2)