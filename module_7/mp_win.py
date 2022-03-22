import multiprocessing as mp


def funct_to_paral(param):
    return param*2


def main():
    print(f' Num cpus: {mp.cpu_count()}')
    numbers = [1, 2, 3, 4]
    pool = mp.Pool(2)
    results = pool.map(funct_to_paral, numbers)
    print(results)


if __name__ == "__main__":
    main()
