<%* 
// Rename current file title by replacing whitespaces with underscores and insert minimum YAML fields at the top
title_upper = tp.file.title.replace(/(^\w{1})|(\s{1}\w{1})/g, match => match.toUpperCase()) _%>
<%*  tR += "---"%>
aliases: [<% title_upper %>]
tags: []
created: <% tp.date.now("YYYY-MM-DD") %>
<%*  tR += "---"%>



# <% title_upper %>


Content body.




