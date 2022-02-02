# strip 공백제거

def main():
    s = "  angel  "

    print(s + "님")
    print(s.strip() + "님")
    print(s.lstrip() + "님")
    print(s.rstrip() + "님")

main()