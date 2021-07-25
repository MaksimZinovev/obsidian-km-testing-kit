<%* // Template that renames file by inserting values from metadata (features, duration) into filename. 
var fname, fname_updated;
fname = fname_updated = tp.file.title;
//update filename if feature in frontmatter does not match  feature in filename
if (tp.frontmatter.features != null) {
	feature_fm  = tp.frontmatter.features[0];
	console.log("1st feature in frontmatter: " + feature_fm);
	} else new Notice("No value for 'features' key in frontmatter", 3000); 
if (tp.file.title.split(".").length > 2) {
	feature_fname = tp.file.title.split(".")[2];
	console.log("feature in filename: " + feature_fname);
	if (feature_fm != feature_fname) {
		console.log("frontmatter: " + feature_fm);
		fname_updated = tp.file.title.replace(feature_fname, feature_fm);
		new Notice("Updated feature in file name : " + fname_updated, 3000)
		}
	} else console.log("could not find feature in filename: " + tp.file.title);
//update filename if duration in frontmatter does not match duration in filename
if (tp.frontmatter.duration != null) {
	duration_fm  = tp.frontmatter.duration +"min"; 
	console.log("duration in frontmatter: " + duration_fm);
	} else new Notice("No value for 'duration' key in frontmatter", 3000); 
if (tp.file.title.split(".").length > 3) {
	duration_fname = tp.file.title.split(".")[3];
	console.log("duration in filename: " + duration_fname);
	if (duration_fm != duration_fname && tp.frontmatter.duration != null) {
		fname_updated = fname_updated.replace(duration_fname, duration_fm);
		new Notice("Updated duration in file name : " + fname_updated, 3000);
		} 
	} else console.log("could not find duration in filename: " + tp.file.title)
//rename file name if there were changes
if (fname != fname_updated){
	console.log("updated file name: " + fname_updated);
	await tp.file.rename(fname_updated);
	} else new Notice("No changes in file name : " + fname_updated, 3000);
_%>