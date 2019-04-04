import socket, sys, argparse, datetime, time
import threading


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address', dest='ip',  type=str, help='Echo Server\'s IP Address')
    parser.add_argument('-p', '--port',  dest='port', type=int,  help='Port Number Opened for Connection.')
    options = parser.parse_args()
    if options.ip == 'host':
        options.ip = '127.0.0.1'
    startClient(options)

def startClient(options):
# Create a TCP/IP socket
# Connect the socket to the port where the server is listening
	server_address = (options.ip, options.port)
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		print('connecting to {} port {}'.format(*server_address))
		try:
			sock.connect(server_address)
		except:
			print('Connection error...Goodbye.')
			sys.exit()
            
# Accept Welcome Message...Confirm Connection
		print("Enter 'Exit' to Terminate.")
		while True:
			try:
				data = sock.recv(512).decode('utf8')
				print(data)
				data = ""
			except OSError:
				print ('[{}] Socket Closed'.format(datetime.datetime.now()))
# Take Client Input
			clientInput = input('Enter Message: \n')
			message = str(clientInput)
            
			if message == 'Exit':
				message = 'Exit'
				sock.sendall(message.encode('utf8'))
				print('[{}] Terminating Connection to: {} '.format(datetime.datetime.now(),*server_address))
				sock.close()
				sys.exit()
			else:
				sock.sendall(message.encode('utf8'))
				
			
            
if __name__ == '__main__':
        main()