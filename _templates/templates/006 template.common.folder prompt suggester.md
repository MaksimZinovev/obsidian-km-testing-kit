<%* ///Snippet for folder prompt suggester
const folders = this.app.vault.getAllLoadedFiles().filter(i => i.children);

tp.system.suggester(folders.map(folder => folder.path), folders);
%>

