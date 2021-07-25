<%* // Template that creates session note
fname_lower_safe = 	tp.file.title.toLowerCase().replace(/(\b(\w{1,2})\b(\s|$|))/g,'').trim().split(' ').join('-');
	session =  await tp.system.suggester(
	["exploratory", "documentation", "review bug fixes", "regression", "end-to-end", "not defined"], 	   
	["exploratory", "documentation", "review-bug-fixes", "regression", "end-to-end","not defined"]
	); 
module =  await tp.system.suggester(["authentication", "repository", "workflows", "integrations", "compliance", "administration","not defined"], ["authentication", "repository", "workflows", "integrations", "compliance", "administration",""]); 
	async function renameFile(tp, session) {
		fname_lower_safe = tp.file.title.toLowerCase().replace(/(\b(\w{1,2})\b(\s|$|))/g,'').trim().split(' ').join('-');
		fname =  tp.date.now("YYYY-MM-DD") + "." + session + "." + fname_lower_safe + ".undefined";
		return fname;
		}
	file_name = await  renameFile(tp, session);  
	new_file_path =  "/sessions/" + fname;
	await tp.file.move(new_file_path); 	
	clip = await tp.system.clipboard();
	if (typeof clip === 'string') {
		if (clip.length < 280) { console.log("ok"); } else {clip = ""}
		} else {clip = ""}
	tR += "---";
	%>
aliases: ["<%*tR += "$" +fname_lower_safe %>"]
tags: [<%*tR += session%>, session]
created: <%tp.date.now("YYYY-MM-DD")%>
type: session
session: <%* tR += session %>
module: <%* tR += module %>
features: [<%*  tR += fname_lower_safe %>]
start: <%tp.date.now("HH-mm")%>
duration: 25
streaks_25min: 
charter: "<%* tR += clip; %>"
<%*  tR += "---"%>

#  Session: <%tp.date.now("YYYY-MM-DD")%> <%*tR += session%> 
<%* tR += "- Charter: " + clip; %>
- Context
- Set Up 
- Related links
- Risks, Test Ideas, Heuristics
- Questions
- Session Notes
	- Issues
	- Coverage outline

---
created: <% tp.date.now("YYYY-MM-DD") %>