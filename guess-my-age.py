my_name = 'Guesser Bot'
create_year = 2022


def guess_age(rem3, rem5, rem7):
    return (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print(f'Hello, My name is {my_name} \nI was created in {create_year}!')

your_name = input('Please enter your name: ').title()

print(f'What a great name you have, {your_name}!')

print('Let me guess your age...')

while True:
    remainders = input('Please enter remainders dividing your age by 3, 5 and 7.: ').split(" ")

    if len(remainders) != 3:
        print('Please enter 3 remainders')
        continue

    rem3, rem5, rem7 = remainders
    
    if not rem3.isdigit() and not rem5.isdigit() and not rem7.isdigit():
        print('Please enter only integers')
        continue

    rem3, rem5, rem7 = int(rem3), int(rem5), int(rem7)

    if not (0 <= rem3 <= 3 and 0 <= rem5 <= 5 and 0 <= rem7 <= 7):
        print('Please enter correct remainders ranges are proper')
        continue
    else:
        your_age = guess_age(rem3, rem5, rem7)
        print(f"Your age is {your_age}, Am i right :)")
        break
