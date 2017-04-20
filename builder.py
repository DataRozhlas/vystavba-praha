
# coding: utf-8

# In[14]:

import markdown
from jsmin import jsmin
import ast
import re
import os
from csscompressor import compress
import yaml


# In[15]:

# read markdown article
with open('article.md', encoding='utf-8') as text:
    parts = text.read().split('---')
    header = parts[0]
    main = parts[1]


# In[16]:

art = yaml.load(header)


# In[17]:

#names of authors
tmp = ', '.join(art['authors'])
art['authors'] = ' a '.join(tmp.rsplit(', ', 1))


# In[18]:

# format external JS links
tmp = ''
for lib in art['libraries']:
    tmp += '<script src="{0}"></script>\n'.format(lib)
art['libraries'] = tmp


# In[19]:

# format external CSS links 
tmp = ''
for styl in art['styles']:
    tmp += '<link rel="stylesheet" type="text/css" href="{0}">\n'.format(styl)
art['styles'] = tmp


# In[20]:

# article content
art['content'] = markdown.markdown(main)


# In[21]:

#read snowfall template
with open('./templates/snowfall.html', encoding='utf-8') as t:
    template = t.read()


# In[22]:

# fill template
for variable in re.findall(r"\{(\w+)\}", template):
    template = template.replace('{' + variable + '}', str(art[variable]))


# In[23]:

# pack JSscripts
temp = ''
for script in os.listdir('./js/'):
    with open('./js/' + script, encoding='utf-8') as js_file:
        jmin = jsmin(js_file.read())
        temp += jmin

template = template + '<script>' + temp + '</script>\n' 


# In[24]:

# pack styles
temp = ''
for script in os.listdir('./styles/'):
    with open('./styles/' + script, encoding='utf-8') as css_file:
        csmin = compress(css_file.read())
        temp += csmin

template = '<style>' + temp + '</style>\n' + template


# In[25]:

#write template
with open('./article.html', 'w', encoding='utf-8') as f:
    f.write(template)


# In[26]:

# write wrapped content into dummy index
with open('./templates/wrapper.html', encoding='utf-8') as t:
    wrapper = t.read()
    
wrapper = wrapper.replace('{content}', template)

with open('./index.html', 'w', encoding='utf-8') as f:
    f.write(wrapper)

