import max_profit as mp
import prime_number as pn

if __name__ == '__main__':
    pn.is_prime_number(1)
    pn.is_prime_number(13)
    pn.is_prime_number(24)

    prices = (15, 10, 6, 9, 10, 4)
    print(mp.max_bf(prices))