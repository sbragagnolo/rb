import sys, getopt
import redbubble
import json

"""
    CommandHandler object is in charge of defining a adaption in between that command line code and the library.
    As error handler it defines a a method that only prints the error and exits.

    Since the initialization of the object is eager, There are two possible points of error:
        creation (__init__)
        application of the command (do_apply)

"""
class CommandHandler(object):
    """docstring for CommandHandler ."""
    def __init__(self,  products_file, cart_file):
        super(CommandHandler, self).__init__()
        try:
            self.environment = self.create_environment(products_file)
            self.cart = self.create_cart(cart_file)
        except Exception as inst:
            self.handleError(inst)

    def create_environment(self, products_file):
        instantiator = redbubble.ProductInstantiator()
        with open(products_file) as data:
            products = [ instantiator.instantiate(p) for p in json.load(data)]
        return redbubble.Environment(products)
    def create_cart(self, cart_file):
        cart = redbubble.Cart(self.environment)
        instantiator = redbubble.ItemInstantiator()
        with open(cart_file) as data:
            items = [ cart.add_item(instantiator.instantiate(p)) for p in json.load(data)]
        return cart

    def do_apply (self):
        try:
            print (self.cart.price())
        except Exception as inst:
            self.handleError(inst)

    def handleError(self, error):
        print (error)
        printHelpAndExit()

def printHelpAndExit():
    print('Usage: %s -p products-file -c cart-file' % sys.argv[0])
    sys.exit(1)

def main():
    # Store input and output file names
    pfile=''
    cfile=''

    # Read command line args
    myopts, args = getopt.getopt(sys.argv[1:],"p:c:")

    ###############################
    # o == option
    # a == argument passed to the o
    ###############################
    for o, a in myopts:
        if o == '-p':
            pfile = a
        elif o == '-c':
            cfile = a
        else:
            printHelpAndExit()

    if(pfile == ''):
        print ('Products file is mandatory')
        printHelpAndExit()

    if(cfile == ''):
        print ('Cart file is mandatory')
        printHelpAndExit()

    (CommandHandler(pfile, cfile)).do_apply()


if __name__ == '__main__':
    main()
