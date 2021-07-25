# <% 
// Rename current file title by replacing whitespaces with underscores
tp.file.title.replace(/(^\w{1})|(\s{1}\w{1})/g, match => match.toUpperCase()) %>
<%* new_fname = tp.file.title.toLowerCase().replace(/(\b(\w{1,2})\b(\s|$|))|[-]+/g,'').trim().split(' ').join('_'); %>
<%* tp.file.rename(new_fname) %>
