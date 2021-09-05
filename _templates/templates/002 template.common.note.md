<%* title_upper = tp.file.title.replace(/(^\w{1})|(\s{1}\w{1})/g, match => match.toUpperCase()) 
// ask user if prefix should be appended
prefix =  await tp.system.prompt("Please enter prefix for a file or press Esc to skip") + "~";
alias = tp.file.title;
console.log("prefix: " + prefix + typeof(prefix));
if (prefix != "null~") {
	alias = prefix + tp.file.title; 
	new Notice(`Added alias: ${alias}`, 3000);
};
console.log(tp.file.title);
// ask user if file should be moved to some folder 
const folders = this.app.vault.getAllLoadedFiles().filter(i => i.children);
const folder_choice = await tp.system.suggester(folders.map(folder => folder.path), folders);
if (folder_choice!= null) {
	new_file_path =  folder_choice.path +"/" + tp.file.title; 
	console.log(new_file_path);
	await tp.file.move(new_file_path); 
	new Notice(`File has been moved to: ${new_file_path}`, 3000);
} else {new Notice(`File path: /unsorted/${alias}`, 3000);}
_%>
<%*  tR += "---"%>
aliases: ["<%title_upper %>", "<%*tR += alias %>"]
tags: []
created: <% tp.date.now("YYYY-MM-DD") %>
<%*  tR += "---"%>

<br ><br >

# <% title_upper %>


Short description / Content body.

<br ><br >


