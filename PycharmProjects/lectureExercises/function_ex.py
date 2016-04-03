
def main():
    celcius = float(input("Enter celcius value:"))
    fer = cellcius_to_F(celcius)
    print("F value is:", fer)

def cellcius_to_F(C):
    F = C * 1.8 + 32.0
    return F
main()

