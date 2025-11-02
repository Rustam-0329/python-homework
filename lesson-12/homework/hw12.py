# Lesson-12 | Homework

# Exercise 1: Threaded Prime Number Checker

# Write a Python program that checks whether a given range of numbers contains prime numbers. 
# Divide the range among multiple threads to parallelize the prime checking process. 
# Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.

import threading
import math
from typing import List

# Lock for thread-safe appending to shared results list
results_lock = threading.Lock()
primes_found: List[int] = []

def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check odd factors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_prime_range(start: int, end: int, thread_id: int) -> None:
    """
    Check numbers from start (inclusive) to end (exclusive) for primes.
    Appends primes to global primes_found list in a thread-safe way.
    """
    local_primes = []
    print(f"Thread {thread_id}: Checking range [{start}, {end})")
    
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)
    
    # Thread-safe update to shared list
    with results_lock:
        primes_found.extend(local_primes)
    print(f"Thread {thread_id}: Found {len(local_primes)} primes")

def threaded_prime_check(start: int, end: int, num_threads: int = 4) -> List[int]:
    """
    Divide [start, end) into num_threads chunks and check for primes in parallel.
    Returns sorted list of all prime numbers found.
    """
    if start >= end:
        return []
    if num_threads <= 0:
        num_threads = 1

    # Clear previous results
    global primes_found
    primes_found = []

    # Calculate chunk size
    total_numbers = end - start
    chunk_size = total_numbers // num_threads
    if total_numbers % num_threads != 0:
        chunk_size += 1

    threads = []
    current_start = start

    print(f"Starting prime check in range [{start}, {end}) using {num_threads} threads...\n")

    for i in range(num_threads):
        chunk_start = current_start
        chunk_end = min(current_start + chunk_size, end)
        
        thread = threading.Thread(
            target=check_prime_range,
            args=(chunk_start, chunk_end, i),
            daemon=True
        )
        threads.append(thread)
        thread.start()

        current_start = chunk_end
        if current_start >= end:
            break

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Sort final results
    primes_found.sort()
    print(f"\nAll threads finished. Total primes found: {len(primes_found)}")
    return primes_found

# ——————————————————————————————————————
# Example Usage & Test
# ——————————————————————————————————————
if __name__ == "__main__":
    # Test with a reasonable range
    START = 2
    END = 100
    THREADS = 6

    primes = threaded_prime_check(START, END, THREADS)

    print("\n" + "="*60)
    print(f"PRIME NUMBERS FOUND IN [{START}, {END}):")
    print("="*60)
    print(primes)
    print(f"\nTotal count: {len(primes)}")



# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text. 
# Implement a threaded solution to count the occurrence of each word in the file. 
# Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.

# threaded_word_counter.py
import threading
import os
import re
from collections import Counter
from typing import List, Dict

# Thread-safe shared dictionary for final word counts
word_count_lock = threading.Lock()
global_word_counts: Counter = Counter()

def clean_word(word: str) -> str:
    """Convert to lowercase and remove punctuation."""
    return re.sub(r'^[\W_]+|[\W_]+$', '', word.lower())

def count_words_in_chunk(chunk: str, thread_id: int) -> None:
    """
    Count words in a chunk of text.
    Updates global_word_counts in a thread-safe way.
    """
    print(f"Thread {thread_id}: Processing chunk of {len(chunk):,} characters...")

    # Split into words, clean, and count locally
    words = chunk.split()
    local_counts = Counter(clean_word(word) for word in words if word.strip())

    # Merge into global counter safely
    with word_count_lock:
        global_word_counts.update(local_counts)

    print(f"Thread {thread_id}: Found {len(local_counts)} unique words in chunk.")

def split_file_into_chunks(file_path: str, num_threads: int) -> List[str]:
    """
    Read file and split into roughly equal chunks by character count.
    """
    file_size = os.path.getsize(file_path)
    chunk_size = file_size // num_threads

    chunks = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for i in range(num_threads):
            start_pos = i * chunk_size
            f.seek(start_pos)

            # Read up to chunk boundary
            if i > 0:
                # Skip to next newline to avoid splitting words
                f.readline()

            end_pos = (i + 1) * chunk_size if i < num_threads - 1 else file_size
            remaining = end_pos - f.tell()
            chunk = f.read(remaining)

            if chunk.strip():
                chunks.append(chunk)

    return chunks

def threaded_word_count(file_path: str, num_threads: int = 4) -> Dict[str, int]:
    """
    Main function: parallel word counting using threads.
    Returns final word frequency dictionary.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    print(f"Reading file: {file_path}")
    print(f"File size: {os.path.getsize(file_path):,} bytes")
    print(f"Using {num_threads} threads for processing...\n")

    # Split file
    chunks = split_file_into_chunks(file_path, num_threads)
    print(f"Split into {len(chunks)} chunks\n")

    # Reset global counter
    global global_word_counts
    global_word_counts = Counter()

    threads = []
    for i, chunk in enumerate(chunks):
        thread = threading.Thread(
            target=count_words_in_chunk,
            args=(chunk, i),
            daemon=True
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads
    for thread in threads:
        thread.join()

    print(f"\nAll threads completed.")
    print(f"Total unique words: {len(global_word_counts):,}")

    return dict(global_word_counts)

# ——————————————————————————————————————
# Example Usage & Test
# ——————————————————————————————————————
def create_sample_file():
    """Create a large sample file for testing."""
    sample_text = (
        "The quick brown fox jumps over the lazy dog. "
        "Python is great for threading and file processing. "
        "This is a test. This is only a test. "
        "Words will be counted accurately across threads. "
    )
    large_text = (sample_text * 5000) + "\n"  # ~500 KB file

    with open("large_sample.txt", "w", encoding="utf-8") as f:
        f.write(large_text)
    print("Created sample file: large_sample.txt")

if __name__ == "__main__":
    # Create sample file if not exists
    sample_file = "large_sample.txt"
    if not os.path.exists(sample_file):
        create_sample_file()

    # Run threaded word count
    try:
        word_freq = threaded_word_count(sample_file, num_threads=4)

        # Display top 10 most common words
        print("\n" + "="*60)
        print("TOP 10 MOST FREQUENT WORDS")
        print("="*60)
        for word, count in Counter(word_freq).most_common(10):
            print(f"{word:<15} : {count:,}")

        print(f"\nFull word count saved to 'word_frequency.txt'")
        with open("word_frequency.txt", "w", encoding="utf-8") as f:
            for word, count in sorted(word_freq.items()):
                f.write(f"{word}: {count}\n")

    except Exception as e:
        print(f"Error: {e}")
