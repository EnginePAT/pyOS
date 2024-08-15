import os, sys, random, time, tqdm

os.system('clear')
def progressBar(count_value, total, suffix=''):
    bar_length = 100
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100.0 * count_value/float(total),1)
    bar = '#' * filled_up_Length + '.' * (bar_length - filled_up_Length)
    sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percentage, '%', suffix))
    sys.stdout.flush()
#for i in range(11):
    #time.sleep(random.random())
    #progressBar(i,10)
#print('\nComplete.')
#time.sleep(1)

os.system('clear')

running = True

print()
print(f'GNU grub - pyOS v2024.01 lts')
print('[1] {pyOS-v2024.01-lts}')
print('[2] {pyOS-Desktop-env}')
print('[3] {exit}')

while running:
    boot_menu = input("> ")

    if boot_menu == '1':
        break
    elif boot_menu == '2':
        print("option currently unavailable - please choose another")
    elif boot_menu == '3':
        exit()
    else:
        print("Invalid Option")
