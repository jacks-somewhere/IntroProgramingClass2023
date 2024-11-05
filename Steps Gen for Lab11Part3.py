# need 365 entries, from 1000 t0 20000
mini = 10000
maxi = 20000
def main():
    file = ('steps.txt', 'w')
    import random
    for count in range(365):
        line = int(random.randint(mini, maxi))
        print(line)
        file.write(line)
    file.close()
    print('Done')
main()
    
