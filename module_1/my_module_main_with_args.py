from argparse import ArgumentParser

def suma(x, y):
    return x+y

def main():
    parser = ArgumentParser()
    parser.add_argument("-n1",
                        "--numero_1",  
                        required=True,
                        type=int,
                        help="primer numero")
    parser.add_argument("-n2",
                        "--numero_2",
                        required=True,
                        type=int,
                        help="segundo numero")
    args = parser.parse_args()
    print(suma(args.numero_1, args.numero_2))

if __name__ == "__main__":
    main()
