<%*  
const folderChoice = await tp.system.prompt("Please enter a relative path to folder e.g. 'logs/2021/'"); 
const files = app.vault.getMarkdownFiles(); 
const filesInFolder = new Array(); 
files.forEach((file) => {
	if(file.path.includes(folderChoice))		
		{filesInFolder.push(file)}; 
}) 
// If you want to select file
// const userFileChoice = (await tp.system.suggester(((item) => //item), filesInFolder, 1))

const filesList  = new Array(); 
filesInFolder.forEach((file) => {
	console.log(file.basename)
	//filesList.push("\n - ["+encodeURIComponent(file.basename.split(".")[3].trim())+"]("+file.path+")")
	filesList.push("\n - ["+file.basename+"]("+encodeURIComponent(file.name.trim())+")")
}
);
_%>

<%* tR += filesList.sort().join('') %>
