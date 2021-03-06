# Knowledge Management in Testing - Obsidian Starter Kit
<p align="center">

<img title="obsidian" alt="obsidian" src="attachments/obsidian.png">

</p>

&nbsp;
&nbsp;
&nbsp;

## Table of Contents
+ [About](#about)
+ [How You Can Benefit from This Kit as a Tester](#benefit)
+ [Getting Started](#getting_started)
+ [Usage](#usage)
+ [Templates](#templates)
+ [Metadata](#metadata)
+ [Issues](#issues)

## About <a name = "about"></a>
This is an ObsidianMD starter kit (vault) for testers and QA enthusiasts. The main 2 goals are:
1. Share my templates, findings and  settings for ObsidianMD with other testers who also use that tool in their work.
2. To have a handy template in the cloud for myself. When I need to start a new testing project, I can download / clone this starter kit  from  GitHub. Without spending much time on settings and configurations  I can quickly start using it for my testing needs in less than 5 min.

The starter kit includes 
- preinstalled [Red Graphite Theme](https://github.com/seanwcom/Red-Graphite-for-Obsidian)
- preinstalled plugins
- predefined hotkeys
- [Templater ](https://silentvoid13.github.io/Templater/) scripts
- some heuristics (templates)
- some test charter examples (templates)
- sample folder structure and file name conventions

All of the above is customizable as per your needs and preferences.

##  How You Can Benefit from This Kit as a Tester <a name = "benefit"></a>
- **Session Based Test Management.** Use templates (invoked by hotkeys) to generate session report, daily report, insert metadata, links, automatically update file name and perform other actions. You can customize templates, include YAML metadata to track progress and generate reports.
- **Heuristics and charters.** Use hotkey to quickly access or view heuristic or charter examples. Modify included heuristics and charters or add your own.
- **Mind maps.** Use mind maps  inside Obsidian for exploratory testing notes (2 mind map plugins already preinstalled). Alternatively you can export markdown notes to other mind-mapping formats.
- **Outlining and tasks**. Use ordered or bulleted lists and tasks to outline your exploratory testing notes, feature notes. Track what's already covered/completed.
- **Linking**. Link your sessions, daily reports, monthly logs, feature notes and test plan.
- **Version control and sharing.** Use Git to take snapshots of your knowledge base.  You can upload your vault to GitHub for  sharing and backup.
- **Automations.** Use 20+ templates to automate tasks.
- **Full control.** All files are stored on your device.

&nbsp;
![mindmap](attachments/mindmap.jpg)

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the starter kit up and running on your local machine so you can start using it.

Main steps include
1. Clone repository or [download zip](https://github.com/MaksimZinovev/obsidian-km-testing-kit/releases) from GitHub. Unzip if you downloaded zip
2. Install [ObsidianMD ](https://obsidian.md/)on your machine (cross-platform support)
3. Launch ObsidianMD
4. On first launch when Safe mode warning appears click "Turn off Safe Mode"
5. Click "Open folder as a vault" and select the folder (obsidian-km-testing-kit)
6. Enjoy

Here is the screen you should see after step #5

![obsidian-km-testing-kit](attachments/obsidian-km-testing-kit.jpg)

## Usage <a name = "usage"></a>

Some hotkeys to get started. All commands in Obsidian can be accessed from command palette. Hotkeys can be customized by navigating to Settings (icon in the bottom left corner) > Hotkeys (below are Mac OS examples).

> Cmd + O - open quick switcher (dialog window with fuzzy search across all files in your vault)

> Cmd + W - close current note

> Cmd + click - open link in a new pane

> Cmd + E - toggle edit / preview mode

> Alt + Cmd + X -  insert Templater template

> Cmd + Shift + N - create note in a new pane 

> Cmd + L - open local graph view

> Ctr + D - delete current note (deleted notes can be found in ".trash" folder)

> Cmd + 1 - move list item up

> Cmd + 2 - move list item down

> Cmd + 4 - toggle line to bulleted or numbered list

> Cmd + Enter - toggle checklist status

> Cmd + Shift + D - duplicate line

> Alt + Cmd + M - move active note to another folder 

> Alt + Cmd + M - run MetaEdit plugin

> Alt + Cmd  + I - show developer console


![quick-switcher](attachments/quick-switcher.jpg)

## Templates <a name = "templates"></a>
All templates are split in 3 areas, located in "_templates/" folder. Feel free to correct them or add your own:
1. templates - templates to manage various types of notes, e.g. create test session note.
2. heuristics - each file contains a brief description of testing heuristic.
2. charters - each file contains a charter example.

How to create exploratory session note  for authentication module

```
Cmd + Shift + N - create new note
Alt + Cmd + X - run Templater plugin
type "020"
select "020 template.testing.bookmarked templates" using keyboard and press Enter or click on it
select "session"  - note template 
select "exploratory"  - session type, your note will have this session type in metadata
select "authentication" -  your note will have this module name in metadata
press Enter
```

You can create other types of notes using template "020 template.testing.bookmarked templates" or run any other template.


![templates](attachments/templates.jpg)

## Metadata  <a name = "metadata"></a>
Some examples describing how to work with metadata using [MetaEdit plugin](https://github.com/chhoumann/MetaEdit) and templates

1. Add or update YAML properties - press Alt + Cmd + M
2. Add Auto Properties  values selectable through a suggester - navigate to Settings > Plugin Options > MetaEdit > Auto Properties > click Settings icon. Then add properties and selectable values.



How to add  feature name to metadata of the session note created in previous example

```
Alt + Cmd + M - run MetaEdit plugin
type "f"
select "features" using keyboard and press Enter or click the option
select "untitled" using keyboard and press Enter or click the option
type feature name (no spaces, e.g. user-login)  or select "registration" using keyboard and press Enter or click the option
```

Rename filename using the name of the first feature in metadata ("features")

```
Alt + Cmd + X -  insert Templater template
type 024
select "024 template ... " using keyboard and press Enter or click the option
# session note file will be renamed 2021-07-25.exploratory.untitled.undefined ??? 2021-07-25.exploratory.login.25min
```


![metadata](attachments/metadata.jpg)

## Navigation  <a name = "navigation"></a>
Aliases (frontmatter fields at the top) can be used for quick navigation using keyboard.

This example shows how to quickly open test session note created today (2021-07-25)

```
Cmd + O - open quick switcher (dialog window with fuzzy search across all files in your vault)
type "$" - this will show all session files
select file
Cmd + Enter - open selected file in a new pane
```

The following examples  of frontmatter demonstrate naming conventions for most common types of notes. Templates  automatically create aliases starting from special characters (which makes it easier to filter them in quick switcher)

 > aliases: ["$2021-07-25.exploratory.login.25min"] - test session (023 template.testing.create session, 025 template.testing.update alias using values in file name )

 > aliases: [~authentication.login] - feature note (021 template.testing.feature catalogued)
 
> aliases: ["&2021-07-25"] - daily note, daily report (022 template.testing.daily note)

> aliases: ["#2021-07"] - monthly log (no template, see example [2021-07.monthly](logs/2021/2021-07.monthly.md))

> aliases: ["%2021-07.regression"] - monthly regression log (no template, see example [2021-07.regression](logs/2021/2021-07.regression.md))

![navigation](attachments/navigation.jpg)

![graph](attachments/graph.jpg)
## Issues <a name = "issues"></a>
Please report issues [here](https://github.com/MaksimZinovev/obsidian-km-testing-kit/issues)
