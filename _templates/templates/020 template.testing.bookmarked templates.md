<%* tR ="";
		choice =  await tp.system.suggester(
		["session", "daily note", "feature", "regression log", "not defined"], 
		["session", "daily note", "feature", "regression log", " "]);
		function includeTemplate(tp, choice) {
			switch (choice) {
				case "feature": 
				return tp.file.include("[[021 template.testing.feature catalogued]]");
				case "session": 
				return tp.file.include("[[023 template.testing.create session]]");
				case "regression log": 
				return tp.file.include("[[028 template.testing.regression log]]");	
				case "daily note": 
				return tp.file.include("[[022 template.testing.daily note]]");
				case "not defined": console.log("default");
				return "not defined";
				default: console.log("default");
				return "not defined";
			}
		}
 _%>
 <%*tR+=await includeTemplate(tp, choice)%>