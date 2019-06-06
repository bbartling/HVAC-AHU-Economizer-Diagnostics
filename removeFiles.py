import os



for filename in os.listdir('.'):
    if not filename.endswith('.py'):
        if os.path.isfile(filename):
            os.remove(filename)



