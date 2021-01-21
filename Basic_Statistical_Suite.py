import statistics as s
def main():
    print("""Welcome to the Basic Statistical Suite
A program that outputs the Mean, Median, Mode, Variance and the Quantiles \n
Insert your data(each element followed by one space; use . to decimal input; Ex.: 1.1 2.2 3.3) :""")
    def stats():
        elements = input()
        numbers = list(map(float, elements.split()))
        a=s.mean(numbers)
        b=s.median(numbers)
        c=s.mode(numbers)
        d=s.variance(numbers)
        e=s.quantiles(numbers)
        print("Your Data:", elements)
        print("Mean:" , a)
        print('Median:', b)
        print('Mode:', c)
        print('Variance:', d)
        print('Quantiles:', e)
    stats()
    input('Press ENTER to exit.')
main()