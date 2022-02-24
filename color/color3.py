#!/usr/bin/env python3
"""Alta3 Research || Author RZFeeser@alta3.com
Learning how to use functions"""

## Installs the crayons package.
## python3 -m pip install crayons
## import statements ALWAYS go up top
import crayons


def main():
    """run time code. Always indent under function"""

    # print 'red string' in red
    print(crayons.red('red string'))

    # Red White and Blue text
    #print('{} white {}'.format(crayons.red('red'), crayons.blue('blue'))) # format string (old ver of str templating)
    print(f"{crayons.red('red')} white {crayons.blue('blue')}")  # f-string (newest version of str templating)

    crayons.disable() # disables the crayons package

    # this line should NOT have color as crayons is disabled
    print(f"{crayons.red('red')} white {crayons.blue('blue')}")  # f-string (newest version of string templating)

    crayons.DISABLE_COLOR = False # enable the crayons package

    # This line will print in color because color is enabled
    print(f"{crayons.red('red')} white {crayons.blue('blue')}")  # f-string (newest version of string templating)

    # print 'Mandar Ghanekar' in yellow
    print(crayons.yellow('Mandar Ghanekar', bold=True))
    
    # print 'Mandar Ghanekar' in magenta
    print(crayons.magenta('Mandar Ghanekar', bold=True))

# this condition is only true if our script is run directly
# it is NOT true if our code is imported into another script
if __name__ == "__main__":
    main()

