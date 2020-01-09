import secrets


def get_names():
  names = []
  i = int(input("How many people is the shadow council considering this time?"))
  for consideration in range(0, i):
    print("Please enter name number {}".format(consideration + 1))
    name = str(input())
    names.append(name)
  return names

def Kage_Summit():
  print("It's time for the shadow council of chance to again change the hokage for no apparent reason!")
  ninjas = get_names()
  print("These ninja will do just fine, let us pick from {}".format(ninjas))
  
  return print("THE NEW HOKAGE IS: {}".format(secrets.choice(ninjas)))

Kage_Summit()
