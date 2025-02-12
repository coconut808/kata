import argparse

def main():
    parser = argparse.ArgumentParser(description='Description of your CLI tool')
    
    # Add arguments
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    parser.add_argument('input', type=str, help='Input file')
    parser.add_argument('-o', '--output', type=str, help='Output file', default='output.txt')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Your code logic here
    if args.verbose:
        print("Verbose mode enabled")
    
    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")

if __name__ == '__main__':
    main()
