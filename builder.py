
# coding: utf-8

# In[1]:

import markdown
from jsmin import jsmin
import ast
import re
import os
from csscompressor import compress


# In[2]:

# read markdown article
with open('article.md', encoding='utf-8') as text:
    parts = text.read().split('---')
    header = parts[0]
    main = parts[1]


# In[3]:

# article base
art = {}
for row in header.split('\n'):
    if len(row) > 0:
        if row.split('| ')[1].startswith('['):
            art[row.split('| ')[0]] =  ast.literal_eval(row.split('| ')[1])
        else:
            art[row.split('| ')[0]] =  row.split('| ')[1]


# In[4]:

#names of authors
tmp = ', '.join(art['authors'])
art['authors'] = ' a '.join(tmp.rsplit(', ', 1))


# In[5]:

# format external JS links
tmp = ''
for lib in art['libraries']:
    tmp += '<script src="{0}"></script>\n'.format(lib)
art['libraries'] = tmp


# In[6]:

# format external CSS links 
tmp = ''
for styl in art['styles']:
    tmp += '<link rel="stylesheet" type="text/css" href="{0}">\n'.format(styl)
art['styles'] = tmp


# In[7]:

# article content
art['content'] = markdown.markdown(main)


# In[8]:

#read snowfall template
with open('./templates/snowfall.html', encoding='utf-8') as t:
    template = t.read()


# In[9]:

# fill template
for variable in re.findall(r"\{(\w+)\}", template):
    template = template.replace('{' + variable + '}', str(art[variable]))


# In[10]:

# pack JSscripts
temp = ''
for script in os.listdir('./js/'):
    with open('./js/' + script, encoding='utf-8') as js_file:
        jmin = jsmin(js_file.read())
        temp += jmin

template = template + '<script>' + temp + '</script>\n' 


# In[11]:

# pack styles
temp = ''
for script in os.listdir('./styles/'):
    with open('./styles/' + script, encoding='utf-8') as css_file:
        csmin = compress(css_file.read())
        temp += csmin

template = '<style>' + temp + '</style>\n' + template


# In[12]:

#write template
with open('./article.html', 'w', encoding='utf-8') as f:
    f.write(template)

