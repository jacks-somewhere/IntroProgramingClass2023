
# Lab 11 Part 3
# Average Steps Determiner

# VARIABLES
ZERO = 0
JAN = 31
FEB = 59
MAR = 90
APR = 120
MAY = 151
JUN = 181
JUL = 212
AUG = 243
SEP = 273
OCT = 304
NOV = 334
DEC = 365

#Main Function
def main():
    #Shows user opening and what the program does
    print('Average Steps Determiner')
    print('----------------------------------------------------------------')
    print('A month by month summery of the whole year of you highest number')
    print('of steps along with your monthly average will be show below.')
    print('')

    #Opens file and creates a list from it
    work_file = open('steps.txt','r')
    step = []
    for line in work_file:
        steps = (line)
        line = line.strip('\n')
        step.append(int(line))

    #Creates list for only January steps
    jan_step = steps_read(work_file, JAN, ZERO, step)
    #Calculates January highest number of steps and average
    jan_high, jan_avg = stats_calc(jan_step)
    #Shows user January stats
    print('January:')
    print(f'Highest number of steps: {jan_high:,} steps')
    print(f'Average number of steps: {jan_avg:,.0f} steps')
    print('')

    #Repeats for February
    feb_step = steps_read(work_file, FEB, JAN, step)
    feb_high, feb_avg = stats_calc(feb_step)
    print('February:')
    print(f'Highest number of steps: {feb_high:,} steps')
    print(f'Average number of steps: {feb_avg:,.0f} steps')
    print('')

    #Repeats for March
    mar_step = steps_read(work_file, MAR, FEB, step)
    mar_high, mar_avg = stats_calc(mar_step)
    print('March:')
    print(f'Highest number of steps: {mar_high:,} steps')
    print(f'Average number of steps: {mar_avg:,.0f} steps')
    print('')

    #Repeats for April
    apr_step = steps_read(work_file, APR, MAR, step)
    apr_high, apr_avg = stats_calc(apr_step)
    print('April:')
    print(f'Highest number of steps: {apr_high:,} steps')
    print(f'Average number of steps: {apr_avg:,.0f} steps')
    print('')

    #Repeats for May
    may_step = steps_read(work_file, MAY, APR, step)
    may_high, may_avg = stats_calc(may_step)
    print('May:')
    print(f'Highest number of steps: {may_high:,} steps')
    print(f'Average number of steps: {may_avg:,.0f} steps')
    print('')

    #Repeats for June
    jun_step = steps_read(work_file, JUN, MAY, step)
    jun_high, jun_avg = stats_calc(jun_step)
    print('June:')
    print(f'Highest number of steps: {jun_high:,} steps')
    print(f'Average number of steps: {jun_avg:,.0f} steps')
    print('')

    #Repeats for July
    jul_step = steps_read(work_file, JUL, JUN, step)
    jul_high, jul_avg = stats_calc(jul_step)
    print('July:')
    print(f'Highest number of steps: {jul_high:,} steps')
    print(f'Average number of steps: {jul_avg:,.0f} steps')
    print('')

    #Repeats for August
    aug_step = steps_read(work_file, AUG, JUL, step)
    aug_high, aug_avg = stats_calc(aug_step)
    print('August:')
    print(f'Highest number of steps: {aug_high:,} steps')
    print(f'Average number of steps: {aug_avg:,.0f} steps')
    print('')

    #Repeats for September
    sep_step = steps_read(work_file, SEP, AUG, step)
    sep_high, sep_avg = stats_calc(sep_step)
    print('September:')
    print(f'Highest number of steps: {sep_high:,} steps')
    print(f'Average number of steps: {sep_avg:,.0f} steps')
    print('')

    #Repeats for October
    oct_step = steps_read(work_file, OCT, SEP, step)
    oct_high, oct_avg = stats_calc(oct_step)
    print('October:')
    print(f'Highest number of steps: {oct_high:,} steps')
    print(f'Average number of steps: {oct_avg:,.0f} steps')
    print('')

    #Repeats for November
    nov_step = steps_read(work_file, NOV, OCT, step)
    nov_high, nov_avg = stats_calc(nov_step)
    print('November:')
    print(f'Highest number of steps: {nov_high:,} steps')
    print(f'Average number of steps: {nov_avg:,.0f} steps')
    print('')

    #Repeats for December
    dec_step = steps_read(work_file, DEC, NOV, step)
    dec_high, dec_avg = stats_calc(dec_step)
    print('December:')
    print(f'Highest number of steps: {dec_high:,} steps')
    print(f'Average number of steps: {dec_avg:,.0f} steps')

#Creats new list for month that it is called for
def steps_read(work_file, maximum, base, step):
    step = step[base:maximum]
    return step

#Calculates highest number of steps and average
def stats_calc(step):
    size = len(step)
    total = sum(step)
    high = max(step)
    avg = total / size
    return high, avg

#Calls Main Function
main()
