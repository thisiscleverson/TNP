from json import load, loads, dump, decoder
import os

class JsonFile:
   def __init__(self, path) -> None:
      self.path = path

   def readJsonFile(self):
      try:
         if os.stat(self.path):
            with open(self.path, 'r') as file:
               config = load(file)
               file.close()
               return config
         else:
            return None
      except FileNotFoundError:
         print("Arquivo de configuração não encontrado")
         raise

   def writeJsonFile(self, title=None, filename=None, reference=None):
      try:
         # check if the file exist. else, create file 
         if not os.stat(self.path) or os.path.getsize(self.path) == 0:
            with open(self.path, 'w') as file:
               jsonObject = {
                  "title":"",
                  "filename":"",
                  "reference":""
               }
               dump(jsonObject,file)
               file.close()

         #salve data for json file
         with open(self.path, 'r+') as file:
            valuesJson = loads(file.read())

            valuesJson['title']     = title     if title     != None else valuesJson['title']
            valuesJson['filename']  = filename  if filename  != None else valuesJson['filename']
            valuesJson['reference'] = reference if reference != None else valuesJson['reference']
            
            #write json file
            file.seek(0)
            dump(valuesJson, file)
            file.close()

      except decoder.JSONDecodeError:
         print('Arquivo de configuração inválido, verifique se o arquivo o arquivo está no formato JSON')
         raise
      except FileNotFoundError:
         print("Arquivo de configuração não encontrado")
         raise
      except KeyError:
         print("Arquivo de configuração inválido")
         raise

