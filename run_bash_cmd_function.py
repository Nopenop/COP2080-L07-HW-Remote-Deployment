import os 

def run_bash_cmd(some_choice):
    print('-' * 80, '\n')
    print('You entered #', some_choice)
    if (some_choice == 1):
        print('The available memory is ')
        os.system('free -tmh')
    elif (some_choice == 2):
        print('The current network connections include: ')
        os.system('netstat -an | grep -i Estab | cut -d \':\' -f 2,3 | gawk \'{print $2}\' | grep [0-9] | uniq')
    elif (some_choice == 3):
        print('Available file space is: ')
        os.system('df -h | grep \'Filesystem\|root\'')
    