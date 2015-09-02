import sys
import os

sys.path.insert(0, os.getcwd())

from tictac.server.tictacserver import TicTacServer

def run():
    port = 7777
    delay = 0.1
    serverInstance = TicTacServer(port)
    serverInstance.run(delay)

if __name__ == '__main__':
    run()

