
# coding: utf-8

# In[56]:


import markdown, re, os, yaml
from jsmin import jsmin
from csscompressor import compress


# In[57]:


# read markdown article
with open('article.md', encoding='utf-8') as text:
    parts = text.read().split('---')
    header = parts[0]
    main = parts[1]


# In[58]:


art = yaml.load(header)


# In[59]:


#read options
options = art['options'].split(", ")


# In[60]:


#names of authors
tmp = ', '.join(art['authors'])
art['authors'] = ' a '.join(tmp.rsplit(', ', 1))


# In[61]:


# format external JS links
tmp = ''
for lib in art['libraries']:
    tmp += '<script src="{0}"></script>\n'.format(lib)
art['libraries'] = tmp


# In[62]:


# format external CSS links 
tmp = ''
for style in art['styles']:
    tmp += '<link rel="stylesheet" type="text/css" href="{0}">\n'.format(style)
art['styles'] = tmp


# In[63]:


#<wide> pseudotag
main = main.replace("<wide>","</div><div class=\"row-main row-main--article\">")
main = main.replace("</wide>","</div><div class=\"row-main row-main--narrow\">")


# In[64]:


# article content
art['content'] = markdown.markdown(main)


# In[65]:


#read snowfall template
if "noheader" in options: template_file = './templates/snowfall_noheader.html'
else: template_file = './templates/snowfall.html'
with open(template_file, encoding='utf-8') as t:
    template = t.read()


# In[66]:


#option: wide
if "wide" in options: art['column'] = "<div class=\"row-main row-main--article\">"
else: art['column'] = "<div class=\"row-main row-main--narrow\">"


# In[67]:


# fill template
for variable in re.findall(r"\{(\w+)\}", template):
    template = template.replace('{' + variable + '}', str(art[variable]))


# In[68]:


# pack JSscripts
temp = ''
for script in os.listdir('./js/'):
    with open('./js/' + script, encoding='utf-8') as js_file:
        jmin = jsmin(js_file.read())
        temp += jmin

template = template + '<script>' + temp + '</script>\n' 


# In[69]:


# pack styles
temp = ''
for style in os.listdir('./styles/'):
    with open('./styles/' + style, encoding='utf-8') as css_file:
        csmin = compress(css_file.read())
        temp += csmin

template = '<style>' + temp + '</style>\n' + template


# In[70]:


#write template
with open('./output.html', 'w', encoding='utf-8') as f:
    f.write(template)


# In[71]:


# write wrapped content into dummy index
with open('./templates/wrapper.html', encoding='utf-8') as t:
    wrapper = t.read()
    
wrapper = wrapper.replace('{content}', template)

with open('./index.html', 'w', encoding='utf-8') as f:
    f.write(wrapper)

