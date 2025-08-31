import torch
print(torch.__version__)
print(torch.version.cuda)
print(torch.backends.cudnn.version())
print(torch.cuda.is_available())

amount = 100
tax = 0.06
total = amount + amount * tax
print(total)

hello = "hello"
name = input("Enter your name: ")
print(hello + " " + name)

