import time

#Rates the user's rhythm based on the percentage difference from the target time.
def rate_rhythm(target_time, actual_time):
    difference = abs((actual_time - target_time) / target_time) * 100
    if difference <=8:
        return "Great!"
    elif difference <= 16:
        return "Okay!"
    else:
        return "Miss!"

def main():  
    while True:
        print("\nWelcome to Rhythm Tester")
        print("This program will test your rhythm - how consistent are YOU!")

        while True:
            speed_input = str(input("Enter rhythm speed (1, 2, or 3): "))
            if speed_input.isdigit() and int(speed_input) in [1, 2, 3]:
                speed = int(speed_input)
                break
            print("Invalid input. Please enter 1, 2, or 3.")

        while True:
            rounds_input = str(input("Enter number of rounds (5 to 50): "))
            if rounds_input.isdigit() and 5 <= int(rounds_input) <= 50:
                rounds = int(rounds_input)
                break
            print("Invalid input. Please enter a number between 5 and 50.")

        print("\nOkay, this test will last", rounds,"rounds and you are aiming for a", speed,"second rhythm.")
        input("Press Enter to begin!\n")

        #A lsit stores each round’s response time added to it during the loop
        response_times = []

        for i in range(1, rounds + 1):
            print('Round', i,'of', rounds, end='')
            start_time = time.time()

            input()
            end_time = time.time()

            response_time = round(end_time - start_time, 2)
            response_times.append(response_time)

            rating = rate_rhythm(speed, response_time)
            print(response_time,'s -', rating, '\n')

        #Calculate fastest,avarage & slowest response based on response time
        fastest_response = min(response_times)
        average_response = round(sum(response_times) / len(response_times), 2)
        slowest_response = max(response_times)

        print("\nTest Complete! Press Enter to see your results.")
        input()

        print("Results:")
        print(' Fastest time:', fastest_response,'s -', rate_rhythm(speed, fastest_response))
        print(' Average time:', average_response,'s -', rate_rhythm(speed, average_response))
        print(' Slowest time:', slowest_response,'s -', rate_rhythm(speed, slowest_response))

        #round by round breakdown
        print(f"\n{'Round':<6}{'Response':<10}{'Difference'}")
        print(f"{'-'*6} {'-'*9} {'-'*10}")
        for i, response_time in enumerate(response_times, start=1):
            diff = response_time - speed
            diff_str = f"{abs(diff):.2f}s {'early' if diff < 0 else 'late'}"
            print(f"{i:<6}{f'{response_time:.2f}s':<10}{diff_str}.")

        restart = str(input("\nWould you like to start again? (y/yes to restart): "))
        if restart not in ["y", "yes"]:
            print("Goodbye!")
            break

#function is executed when the Python file is run directly        
if __name__ == "__main__":
    main()






