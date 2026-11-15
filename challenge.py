import os
import json
import math
from datetime import datetime

def main():
    numbers = []
    print("--- Number Entry Phase ---")
    
    # 1. Input loop with your prompt
    while True:
        user_input = input('Enter a number (enter "DONE" to stop): ')
        
        # Check if they typed DONE (case-insensitive)
        if user_input.strip().upper() == "DONE":
            print("Stopping entry...\n")
            break
            
        try:
            # Try to convert the input to a float (real number)
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            # Warn the user if it's not a valid number and request re-entry
            print("Invalid input! That is not a number. Please try again.")

    if not numbers:
        print("No numbers were entered. Exiting program.")
        return

    # 2. Ensure the 'outcomes' directory exists
    os.makedirs("outcomes", exist_ok=True)
    
    # Generate a unique filename using the current timestamp (e.g., 2026-06-06_21-30-15.txt)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join("outcomes", f"{timestamp}.txt")

    # Save original numbers temporarily to test reading back immediately
    with open(file_path, "w") as f:
        json.dump(numbers, f)

    # 3. Read data back from the newly created timestamped file
    with open(file_path, "r") as f:
        loaded_numbers = json.load(f)

    # 4. Custom Sort Procedure (Bubble Sort - Descending: greatest to smallest)
    n = len(loaded_numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if loaded_numbers[j] < loaded_numbers[j + 1]:
                loaded_numbers[j], loaded_numbers[j + 1] = loaded_numbers[j + 1], loaded_numbers[j]

    # 5. Compute Arithmetic Mean (Custom loop)
    total_sum = 0
    count = 0
    for num in loaded_numbers:
        total_sum += num
        count += 1
    mean = total_sum / count

    # 6. Compute Sample Standard Deviation (Custom loop, N - 1 denominator)
    if count > 1:
        sum_squared_diff = 0
        for num in loaded_numbers:
            diff = num - mean
            sum_squared_diff += diff * diff
        variance = sum_squared_diff / (count - 1)
        sample_std_dev = math.sqrt(variance)
    else:
        sample_std_dev = 0.0  # Undefined for N=1

    # 7. Write the final formatted output back into the timestamped file
    with open(file_path, "w") as f:
        f.write(f"Original Numbers: {numbers}\n")
        f.write(f"Sorted Numbers (Greatest to Smallest): {loaded_numbers}\n")
        f.write(f"Arithmetic Mean: {mean:.4f}\n")
        f.write(f"Sample Standard Deviation: {sample_std_dev:.4f}\n")

    print(f"Data successfully processed and saved to '{file_path}'.")

    # 8. Display Results in Terminal
    print("\n" + "="*35)
    print("RESULTS:")
    print("="*35)
    print(f"Original Array: {numbers}")
    print(f"Sorted Data:    {loaded_numbers}")
    print(f"Arithmetic Mean: {mean:.4f}")
    print(f"Sample Std Dev:  {sample_std_dev:.4f}")

if __name__ == "__main__":
    main()