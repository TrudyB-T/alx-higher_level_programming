#!/usr/bin/python3
for fig1 in range(0, 10):
    for fig2 in range(fig1 + 1, 10):
        if fig1 == 8 and fig2 == 9:
            print(f"{fig1}{fig2}")
        else:
            print("{}{}".format(fig1, fig2), end=", ")
