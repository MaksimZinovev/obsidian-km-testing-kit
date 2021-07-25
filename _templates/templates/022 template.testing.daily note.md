<%* // Template that creates session note _%>
---
aliases: ["&<%tp.date.now("YYYY-MM-DD")%>"]
tags: [dailynote, dn, log]
created: <% tp.date.now("YYYY-MM-DD")%>
---

# <% tp.file.title %>
<%* new_file_path =  "/logs/" + tp.date.now("YYYY") +"/"+ tp.file.title;  
await tp.file.move(new_file_path); _%>

## Context

## Plan
1. Review bug fixes.
2. Exploratory testing: 
3. Documentation: 
4. Regression testing:

## ToDo

## Summary
- Summary
	Here is a short summary for  today
- Sessions

## GitHub Tickets

___
links: 
- This month notes: [<%tp.date.now("YYYY-MM")%>.monthly](<%tp.date.now("YYYY-MM")%>.monthly.md)
- Previous daily note:  <%tp.file.include("[[027 template.testing.get previous daily note link]]")%>