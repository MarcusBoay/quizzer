#! /usr/bin/env python3
#-------------------------------------------------------------------------------
# Quizzer
# Version 0.1.0
#-------------------------------------------------------------------------------

import sys
import yaml

def main(argv):
    yaml_file_name = argv[1]
    with open(yaml_file_name, 'r') as file:
        yaml_file = yaml.safe_load(file)
        title = yaml_file['title']
        print("="*len(title))
        print(title)
        print("="*len(title), '\n')

        for q in yaml_file['questions']:
            print("Q:", q, "")
            input() # we don't care about user input for now
            print("A:")
            print(''.join(yaml_file['questions'][q]), "\n\n")
    


if __name__ == "__main__":
    main(sys.argv)