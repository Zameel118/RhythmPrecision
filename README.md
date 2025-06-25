# Rhythm Tester

A Python command-line application that tests your ability to maintain consistent timing and rhythm. Challenge yourself to press Enter at precise intervals and see how well you can keep the beat!

## Features

- **Multiple Speed Settings**: Choose from 3 different rhythm speeds (1, 2, or 3 seconds)
- **Customizable Rounds**: Test yourself with anywhere from 5 to 50 rounds
- **Real-time Feedback**: Get instant feedback on each attempt with "Great!", "Okay!", or "Miss!" ratings
- **Detailed Statistics**: View your fastest, average, and slowest response times
- **Round-by-Round Analysis**: See exactly how early or late you were on each attempt
- **Performance Rating System**: 
  - **Great!** - Within 8% of target time
  - **Okay!** - Within 8-16% of target time  
  - **Miss!** - More than 16% off target time

## How to Use

1. **Run the Program**
   ```bash
   python rhythm_precision.py
   ```

2. **Select Your Settings**
   - Choose rhythm speed (1, 2, or 3 seconds)
   - Set number of rounds (5-50)

3. **Take the Test**
   - Press Enter to start each round
   - Try to press Enter again at exactly the target interval
   - Receive instant feedback on your timing

4. **View Results**
   - See your overall performance statistics
   - Review round-by-round breakdown showing how early/late you were
   - Choose to restart or exit

## Example Output

```
Welcome to Rhythm Tester
This program will test your rhythm - how consistent are YOU!

Enter rhythm speed (1, 2, or 3): 2
Enter number of rounds (5 to 50): 10

Okay, this test will last 10 rounds and you are aiming for a 2 second rhythm.
Press Enter to begin!

Round 1 of 10
1.98s - Great! 

Round 2 of 10
2.15s - Okay! 

...

Results:
 Fastest time: 1.95s - Great!
 Average time: 2.08s - Okay!
 Slowest time: 2.34s - Miss!

Round  Response   Difference
------ --------- ----------
1      1.98s     0.02s early.
2      2.15s     0.15s late.
...
```

## Requirements

- Python 3.x
- No external libraries required (uses built-in `time` module)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/rhythm-tester.git
   ```

2. Navigate to the project directory:
   ```bash
   cd rhythm-tester
   ```

3. Run the program:
   ```bash
   python rhythm_precision.py
   ```

## How It Works

The program uses Python's `time.time()` function to measure the precise interval between when you're prompted and when you press Enter. It calculates the percentage difference from your target time and provides feedback based on your accuracy.

The rating system is designed to be challenging but fair:
- **Great!** requires timing within ±8% of the target
- **Okay!** allows for ±8-16% variance
- **Miss!** indicates timing that's more than 16% off

## Tips for Better Performance

- Find a quiet environment to minimize distractions
- Try to internalize the rhythm before starting
- Focus on consistency rather than perfect accuracy
- Use shorter rounds (5-10) when starting out
- Practice with slower speeds (3 seconds) before attempting faster rhythms

## Contributing

Feel free to fork this project and submit pull requests for improvements! Some ideas for enhancements:

- Add sound/metronome functionality
- Implement difficulty levels with tighter timing windows
- Add visual rhythm indicators
- Create a scoring system with leaderboards
- Export results to CSV files

## License

This project is open source and available under the [MIT License](LICENSE).

---

Test your rhythm, improve your timing, and see how consistent you really are! 🎵
