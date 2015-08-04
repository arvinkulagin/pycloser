pycloser
========

Сlean exit for Python scripts after Ctrl-C. Inspired by `xlab’s Closer`_
for Go (Golang). # Usage

.. code:: python

    from pycloser import defer, listen, close

    # Push inform function to stack.
    @defer
    def inform():
        print('You close programm with Ctrl-C.')

    # Push goodbuy function to stack.
    @defer
    def goodbuy():
        print('Goodbuy!')

    # Listening SIGINT, SIGTERM and SIGHUP OS signals.
    # When it sended, listen() pop deferred functions from stack
    # and call its one after the other.
    listen()

    # Main programm loop
    for x in range(1, 10):
        print("{0}: {1}".format(x, input(">> ")))

    # Pop deferred functions from stack and call its, if signal was not sended.
    close()

.. _xlab’s Closer: https://github.com/xlab/closer