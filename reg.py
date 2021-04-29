import shuntingre
import thompson
from argparse import ArgumentParser, RawTextHelpFormatter #import argparser
import sys #to take arguments

# a*: zero or more a's.
# a+: one or more a's. i.e. aa*


def get_arg_parser():
    argparser = ArgumentParser(formatter_class=RawTextHelpFormatter)

    argparser.add_argument('--regex', dest='regex',
                           action='append',
                           help='Regex that will be run against a text file')
    argparser.add_argument('--file', dest='file',
                           action='append',
                           help='Full path to a text file')

    return argparser

# Get the arguments that are passed in while running the script
def get_main_args(sys_argv):
    arg_parser = get_arg_parser()
    if len(sys_argv) <= 1: #If no arguments passed print help message only
        arg_parser.print_help() 
        raise SystemExit(2)
    return get_arg_parser().parse_args(sys_argv[1:]) # Return all passed arguments

def main(args):
    _args = get_main_args(args)
    if _args.regex:
        if _args.file:
            print("\nLooking for \'{0}\' regular expression matches in {1}\n".format(_args.regex[0], _args.file[0]))
            regex(_args.file[0], _args.regex[0])
        else:
            print("No file specified")
    else:
        print("No regex specified")


# Function takes the text file path, and regex, and then searches for matches of the pattern
def regex(text_file, regex_match):
    with open(text_file, 'r') as the_file:
        text = the_file.readlines()
        infix = regex_match
        postfix = shuntingre.shunt(infix)
        nfa = thompson.re_to_nfa(postfix)
        for word in text:
            word = word.strip()
            match = nfa.match(word)
            print("Match {0}: {1}".format(word, match)) # Prints found matches


if __name__ == '__main__':
    main(sys.argv)
