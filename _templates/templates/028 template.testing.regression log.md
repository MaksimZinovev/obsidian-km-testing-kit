<%* // Template that creates regression log note for current month (error will be raised if file already exist) _%>
---
aliases: [ "%<%tp.date.now("YYYY-MM")%>.regression" ]
tags: [regression, log]
created: <%tp.date.now("YYYY-MM-DD")%>
---

<%* 
async function renameFile(tp) {
	fname =  tp.date.now("YYYY-MM") + ".regression";
	return fname;
	}
file_name = await  renameFile(tp);  
new_file_path =  "/logs/" + tp.date.now("YYYY") +"/"+ file_name;  
await tp.file.move(new_file_path); _%>

## <%tp.date.now("YYYY-MM")%>.regression

- Goals: 
	- weeks: 4
	- working days: 8
	- If no e2e testing
		- 4 core testing sessions, 20-40 min per day
		- 3 non-core testing sessions, 20-40 min per day
		- 1 day off
- Core testing sessions
- Non-Core testing sessions
- End-to-end testing sessions
	

<br> <br>
___
created: <% tp.date.now("YYYY-MM-DD")%>


