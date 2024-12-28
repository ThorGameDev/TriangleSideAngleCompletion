import numpy as np
import math

def fill_third_angle(A, B, C):
    if A != None and B != None and C == None:
        C = 180 - A - B
    if B != None and C != None and A == None:
        A = 180 - B - C
    if C != None and A != None and B == None:
        B = 180 - C - A
    return A, B, C

def fill_missing_side_with_sas(a, b, c, A, B, C):
    if a == None and b != None and c != None and A != None:
        a = law_of_cosines(b, c, A)
    if b == None and c != None and a != None and B != None:
        b = law_of_cosines(c, a, B)
    if c == None and a != None and b != None and C != None:
        c = law_of_cosines(a, b, C)
    return a, b, c

def fill_missing_side_with_asa(a, b, c, A, B, C):
    if a == None and b != None and A != None and B != None:
        a = law_of_sines(A, b, B)
    if b == None and c != None and B != None and C != None:
        b = law_of_sines(B, c, C)
    if c == None and a != None and C != None and A != None:
        c = law_of_sines(C, a, A)
    return a, b, c

def fill_missing_angle(a, b, c, A, B, C):
    if A == None and a != None and b != None and B != None:
        A = law_of_sines_2(a, b, B)
    if B == None and b != None and c != None and C != None:
        B = law_of_sines_2(b, c, C)
    if C == None and c != None and a != None and A != None:
        C = law_of_sines_2(c, a, A)
    if A == None and a != None and c != None and C != None:
        A = law_of_sines_2(a, c, C)
    if B == None and b != None and a != None and A != None:
        B = law_of_sines_2(b, a, A)
    if C == None and c != None and b != None and B != None:
        C = law_of_sines_2(c, b, B)
    return A, B, C

def fill_all_missing_angles(a, b, c, A, B, C):
    if A == None and a != None and b != None and c != None:
        A = law_of_cosines_2(a, b, c)
    if B == None and a != None and b != None and c != None:
        B = law_of_cosines_2(b, c, a)
    if C == None and a != None and b != None and c != None:
        C = law_of_cosines_2(c, b, a)
    return A, B, C

def law_of_cosines(b, c, A):
    print("Call law of cos")
    a = np.sqrt(b**2 + c**2 - 2*b*c* np.cos(np.deg2rad(A)))
    return a

def law_of_cosines_2(a, b, c):
    cosA = (a**2 - b**2 - c**2)/(-2*a*c)
    A = np.rad2deg(np.arccos(cosA))
    return A

def law_of_sines(A, b, B):
    print("Call law of sin")
    a=np.sin(np.deg2rad(A))*b/np.sin(np.deg2rad(B))
    return a

def law_of_sines_2(a, b, B):
    print("Call law of sin2")
    A=np.rad2deg(np.arcsin(np.sin(np.deg2rad(B))*a/b))
    return A

def solve(a, b, c, A, B, C):
    for i in range(10):
        if A != None:
            if math.isnan(A):
                A = None
        if B != None: 
            if math.isnan(B):
                B = None
        if C != None:
            if math.isnan(C):
                C = None
        a, b, c = fill_missing_side_with_sas(a, b, c, A, B, C)
        a, b, c = fill_missing_side_with_asa(a, b, c, A, B, C)
        A, B, C = fill_third_angle(A, B, C)
        A, B, C = fill_missing_angle(a, b, c, A, B, C)
        A, B, C = fill_all_missing_angles(a, b, c, A, B, C)
    print("a: " + str(a))
    print("b: " + str(b))
    print("c: " + str(c))
    print("A: " + str(A))
    print("B: " + str(B))
    print("C: " + str(C))
    return a, b, c, A, B, C

def get_input(prompt):
    val = None
    try:
        val = float(input(prompt))
        return val
    except:
        return None

a = get_input("a: ")
b = get_input("b: ")
c = get_input("c: ")
A = get_input("A: ")
B = get_input("B: ")
C = get_input("C: ")

a, b, c, A, B, C = solve(a, b, c, A, B, C)
