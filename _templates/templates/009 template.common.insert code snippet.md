<%*
const languages = {
    "C#": "CSharp",
    "JavaScript": "JavaScript",
	"Python": "Python"
}
lang = await tp.system.suggester(Object.keys(languages), Object.values(languages)) 
if (lang) {
%>```<% lang %>
<% tp.file.cursor(0) %>
```<%* } %>