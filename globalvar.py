x = "global data"  # Declared outside -> Global

def my_function():
    print("I am a " +x)  # Directly read the global variable

my_function()
