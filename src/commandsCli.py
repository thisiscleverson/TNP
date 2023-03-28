import click
import os
from getpass import getpass
from jsonFile import JsonFile
from readFiles import ReadFile
from tabnews import Client


json_file = JsonFile('config_tnp.json')
read_file = ReadFile()

#create group
@click.group()
def cli():
   ...

#commands cli
@cli.command('add')
@click.argument('filename')
def addFile(filename):
   json_file.writeJsonFile(filename=filename)


@cli.command('title')
@click.option('-t','--title',type=str, help='')
def setTitle(title):
   json_file.writeJsonFile(title=title)


@cli.command('ref')
@click.option('-l', '--link',type=str, help='')
def reference(link):
   json_file.writeJsonFile(reference=link)


@cli.command('push')
def publish():
   email    = input('Your Email: ')
   password = getpass('Your Password: ')


   try:
      client = Client(email, password, use_preview_tabnews_host=False) #create login with tabnews.com.br
      valuesJson = json_file.readJsonFile()
      text = read_file.readFile(valuesJson['filename'])

      #publish post
      post = client.publish_post(
         title=valuesJson['title'],
         content=text,
         reference=valuesJson['reference']
      )
      
      if post['status'] == 'published':
         slug = post['slug']
         print('Seu post foi publicado com sucesso!')
         print(f'https://tabnews.com.br/{slug}')
   except:
      print('Não foi possível publicar seu post!')
      raise



cli.add_command(addFile)
cli.add_command(setTitle)
cli.add_command(reference)

