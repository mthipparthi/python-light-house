# Alas we come to dark corners of Gevent.
# I've avoided mentioning monkey patching up until now to try and motivate the powerful coroutine patterns, but the time has come to discuss the dark arts of monkey-patching.
# If you noticed above we invoked the command monkey.patch_socket(). This is a purely side-effectful command to modify the standard library's socket library.


# Python's runtime allows for most objects to be modified at runtime including modules, classes, and even functions. This is generally an astoudingly bad idea since it creates an "implicit side-effect" that is most often extremely difficult to debug if problems occur, nevertheless in extreme situations where a library needs to alter the fundamental behavior of Python itself monkey patches can be used. In this case gevent is capable of patching most of the blocking system calls in the standard library including those in socket, ssl, threading and select modules to instead behave cooperatively.

# For example, the Redis python bindings normally uses regular tcp sockets to communicate with the redis-server instance. Simply by invoking gevent.monkey.patch_all() we can make the redis bindings schedule requests cooperatively and work with the rest of our gevent stack.

# This lets us integrate libraries that would not normally work with gevent without ever writing a single line of code. While monkey-patching is still evil, in this case it is a "useful evil".


import socket

print(socket.socket)

print("After monkey patch")
from gevent import monkey

monkey.patch_socket()
print(socket.socket)

import select

print(select.select)
monkey.patch_select()
print("After monkey patch")
print(select.select)
