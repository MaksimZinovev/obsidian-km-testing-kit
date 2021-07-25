<%*  // Template that uses current values in  frontmatter "features" to search files in "features/" folder and generate markdown links if  filename contains the name of the feature.
// get all md files from features folder
const folderFeatures = "features/";
const files = app.vault.getMarkdownFiles();
const filesInFolder = new Array();
files.forEach((file) => {
  if (file.path.includes(folderFeatures)) {
    filesInFolder.push(file);
  };
});
// get the list of features from frontmatter
const features = tp.frontmatter.features;
const linksFeatureNotes = new Array();
if (features != null) {
  if (typeof features === "string") {
    features = [features];
  } else {
    console.log("Frontmatter: " + features);
  };
  features.forEach((feature) => {
    filesInFolder.forEach((file) => {
      if (file.basename.includes(feature)) {
        linksFeatureNotes.push(`- [${file.basename}](../${file.path})`);
      };
    });
  });
  if (linksFeatureNotes.length == 0) {
  linksFeatureNotes.push("- Feature notes not found for the following features: " + `${features}`);
  };
} else {
  linksFeatureNotes.push("- No features specified in frontmatter!");
};
console.log(linksFeatureNotes);
_%>
<%* tR += linksFeatureNotes.join("\n"); _%>