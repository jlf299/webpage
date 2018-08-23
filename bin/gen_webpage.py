import json
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape


YEAR = datetime.today().year
# TODO detect if we are in the bin directory and go down one step

info = json.load(open('data/editorial-board.json', 'r'))

if not os.path.exists('output'):
    os.mkdir('output')


# beta webpage
prefix = 'beta'
if not os.path.exists(os.path.join('output', prefix)):
    os.mkdir(os.path.join('output', prefix))
env = Environment(
    loader=FileSystemLoader(os.path.join('templates', 'beta')),
    autoescape=select_autoescape(['html', 'xml'])
)

for page in ['editorial-board.html', 'contact.html']:
    with open(os.path.join('output', prefix, page), 'w') as f:
        template = env.get_template('%s' % page)
        out = template.render(**info, year=YEAR)
        f.write(out)
    
# current webpage
prefix = ''
if not os.path.exists(os.path.join('output', prefix)):
    os.mkdir(os.path.join('output', prefix))
env = Environment(
    loader=FileSystemLoader(os.path.join('templates', prefix)),
    autoescape=select_autoescape(['html', 'xml'])
)

for page in ['index.html']:
    with open(os.path.join('output', prefix, page), 'w') as f:
        template = env.get_template('%s' % page)
        out = template.render(**info, year=YEAR)
        f.write(out)
