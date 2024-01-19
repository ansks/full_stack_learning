# Try, Except and Finally 

try:
    # f = open('test.txt', 'w')
    f = open('test.txt', 'r')
    f.write("New line Added.")

except IOError:
    print("Check if file is available")

else:
    print('File read successfully and data written.')
    f.close()

finally:
    print('This will always appear')
    
print('testing block execution.')