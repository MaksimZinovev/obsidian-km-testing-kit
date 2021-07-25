<%*   // Template updates frontmatter value in "aliases" with current file name, example: 
// if current filename is "021-07-17.exploratory.login.20min"
// in frontmatter, value in "aliases" will be updated with  ["$2021-07-17.exploratory.login.20min"]
const {update} = this.app.plugins.plugins["metaedit"].api;
alias = `["$${tp.file.title}"]`
await update('aliases', alias, tp.file.path(true))
new Notice(`Updated aliases: ${alias}`, 3000);
_%>