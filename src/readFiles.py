
class ReadFile:
   def __init__(self) -> None:
      pass
      
   def getExtensionType(self, file):
      sliced = file.split('.')
      return sliced[len(sliced) - 1].lower()
   
   # function to read file [.md]
   def readFile(self, path):
      if self.getExtensionType(path).lower() == 'md':
         try:
            with open(path,'r') as file:
               text = file.read()
            return text
         except:
            raise(
               ValueError(f'Não foi possível ler o arquivo:"{path}"'))
      else:
         raise(
            ValueError('o arquivo tem que ser do tipo ".md"'))



