<%* 
// Rename current file by replacing whitespaces with underscores and remove 1-2 characters words
new_fname = tp.file.title.toLowerCase().replace(/(\b(\w{1,2})\b(\s|$|))|[-]+/g,'').trim().split(' ').join('_'); _%>
<%* tp.file.rename(new_fname) %>
