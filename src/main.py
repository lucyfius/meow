#!/usr/bin/env python3
import sys
from interpreter.interpreter import MeowInterpreter

def main():
    interpreter = MeowInterpreter()
    
    if len(sys.argv) > 1:
        # Run file mode
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as f:
                code = f.read()
            interpreter.run(code)
        except FileNotFoundError:
            print(f"😿 *sad meow* Cannot find file '{filename}'")
        except Exception as e:
            print(f"😾 *angry meow* Error: {str(e)}")
    else:
        # Interactive mode
        print("😺 Welcome to Meow REPL! Type HISSSS to exit.")
        while True:
            try:
                code = input("😸 > ")
                if code.strip().lower() == "hissss":
                    break
                interpreter.run(code)
            except KeyboardInterrupt:
                print("\n😺 Caught keyboard interrupt. Type HISSSS to exit.")
            except Exception as e:
                print(f"😾 *angry meow* Error: {str(e)}")

if __name__ == "__main__":
    main() 