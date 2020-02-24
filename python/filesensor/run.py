import asyncio

from filesensor import FileSensor


def create_async_tasks(path_list):				 
	# loop = asyncio.get_event_loop()
# 	tasks = []
# 	print(dir(path_list))
# 	print(help(isInstanceOf))
	for path in path_list:
		filesensor = FileSensor(path)
		tasks.append(asyncio.ensure_future(filesensor.watch()))

	loop.run_until_complete(asyncio.wait(tasks))  
	loop.close()


if __name__=='__main__':
	# Configuration Prameters

	# Provide the list of path that has to be watched
	path_list = ["C:\\Users\\Barsha\\Documents\\Rucky\\Study\\python\\filesensor\\test1", 
				 "C:\\Users\\Barsha\\Documents\\Rucky\\Study\\python\\filesensor\\test2"]

	# path_list = ["/mnt/c/Users/Barsha/Documents/Rucky/Study/python/filesensor/test1",
	# 			   "/mnt/c/Users/Barsha/Documents/Rucky/Study/python/filesensor/test2"]
	
	create_async_tasks(path_list)
