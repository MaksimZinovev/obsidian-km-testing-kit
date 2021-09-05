<%*  
// prompt to enter prefix then add alias with "prefix~"" and file name
prefix = await tp.system.prompt("Please enter prefix for an alias to add or press Esc to skip") + "~";
new_alias = "";
console.log("prefix: " + prefix + typeof(prefix));
if (prefix != "null~") {
	new_alias = prefix + tp.file.title;
	new Notice(`Added alias: ${new_alias}`, 3000);
	// await tp.file.rename(new_fname)
}

if (tp.frontmatter.aliases != null) {
	aliases_fm = tp.frontmatter.aliases;
	console.log("aliases in frontmatter: " + aliases_fm);
	if (aliases_fm instanceof Array && new_alias.length > 0) {
		aliases_fm.push(new_alias);
		const {update} = this.app.plugins.plugins["metaedit"].api;
		await update('aliases', `[${aliases_fm.map(n=>`"${n}"`).join(", ")}]`, tp.file.path(true))
		new Notice(`Updated aliases: ${aliases_fm}`, 3000);
	}
} else new Notice("No value for 'aliases_fm' key in frontmatter", 3000); 
	
_%>