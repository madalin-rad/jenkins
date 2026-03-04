import fire

def hello(name="World"):
  return "Hello %s from main branch!" % name

if __name__ == '__main__':
  fire.Fire(hello)