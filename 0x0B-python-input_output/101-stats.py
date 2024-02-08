#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    """
    Print the metrics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing counts of status codes.
    """
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{:d}: {:d}".format(code, status_codes[code]))

def parse_line(line, total_size, status_codes):
    """
    Parse each line of input.

    Args:
        line (str): The input line.
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing counts of status codes.
    """
    try:
        data = line.split()
        total_size += int(data[-1])
        code = int(data[-2])
        if code in status_codes:
            status_codes[code] += 1
    except ValueError:
        pass
    return total_size, status_codes

def main():
    """
    Main function to read input, compute metrics, and print results.
    """
    try:
        total_size = 0
        status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
        count = 0

        for line in sys.stdin:
            total_size, status_codes = parse_line(line.strip(), total_size, status_codes)
            count += 1

            if count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()

