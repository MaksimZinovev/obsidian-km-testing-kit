<%* 
title_upper = tp.file.title.replace(/(^\w{1})|(\s{1}\w{1})/g, match => match.toUpperCase()); 
module =  await tp.system.suggester(["authentication", "repository", "workflows", "integrations", "compliance", "administration","not defined"], ["authentication", "repository", "workflows", "integrations", "compliance", "administration",""]); 
fname_lower_safe = tp.file.title.toLowerCase().replace(/(\b(\w{1,2})\b(\s|$|))/g,'').trim().split(' ').join('-');
fname = module + "." + fname_lower_safe;
await  tp.file.rename(fname);  
new_file_path =  "/features/" + fname;
await tp.file.move(new_file_path); 	
tR += "---\n";
_%>
aliases: [~<%fname%>]
tags: [feature]
created: <% tp.date.now("YYYY-MM-DD") %>
type: feature 
feature: <%fname_lower_safe%>
module: [<% module %>]
updated_tms: no
<%*  tR += "---"%>

# <%*  tR += title_upper %>

## Progress
- [ ] Add feature note: [<%*tR += fname%>](<%*tR += fname%>.md)
- [ ] Add description or user story
- [ ] Add related links
- [ ] Add acceptance criteria, expected behavior
- [ ] Test sessions:
	- [ ] yyyy-mm-dd charter
- [ ] Update [Feature List](../70_feature_list.md)
- [ ] Update and map test cases in [Test Management Software](../90_test_management.md).

## Testing Notes
- Set Up 
- User Story
	- As a (user_type) 
	- I want to (perform_something) 
	- so that (reason)
- Acceptance Criteria
- Related links
- Regression Coverage Outline
	- 
---
created: <% tp.date.now("YYYY-MM-DD") %>