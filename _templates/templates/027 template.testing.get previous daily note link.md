<%*  // Template that finds previous  daily note and generates markdown link for that note
// get all md files from logs folder
const folderFeatures = "logs/" + tp.date.now("YYYY");
const files = app.vault.getMarkdownFiles();
const filesInFolder = new Array();
files.forEach((file) => {
  if (file.path.includes(folderFeatures)) {
    filesInFolder.push(file);
  }
});
console.log("===\n");
// check the daily note file exist in last 30 days range
const range = (start, end, length = end - start + 1) =>
Array.from({ length }, (_, i) => start + i)
i = range(1,30).find(daysAgo => filesInFolder.map(Tfile => Tfile.basename).indexOf(tp.date.now("YYYY-MM-DD", -daysAgo)) > -1);
if (i != null && i != undefined) {
	PreviousDailyNoteFile = filesInFolder.find(file => file.basename == tp.date.now("YYYY-MM-DD", -i));
	console.log("Found i: " + i.toString());
	console.log("Found day: " + tp.date.now("YYYY-MM-DD", -i));
	console.log("PreviousDailyNote: " + PreviousDailyNoteFile.name);
	tR += `[${PreviousDailyNoteFile.basename}](${PreviousDailyNoteFile.name})`
} else  { tR += "Previous daily note not found within the range of 30 days." }
_%>
