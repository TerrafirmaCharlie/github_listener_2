from github import Github
import markdown2

access_token = "59926b9a55e6e2e2a5a25ba5c6fecdd72e36c8e0"
g = Github(access_token)


def font_colour_picker(colour_font_desc):
    map_dict = {"#r": "color:red;", "#g": "color:#00cc00;", "#b": "color:blue;", "#y": "color:black",
                "# ": "color:black"}
    description_stripped = colour_font_desc.strip(colour_font_desc[:2])
    font_colour = map_dict[colour_font_desc[:2]]
    new_description = f"<span style=\"{font_colour}\"> {description_stripped}</span>"
    return new_description


repo_find = g.get_repo("TerrafirmaCharlie/github_listener_2")
repo_desc = repo_find.description
commits = repo_find.get_commits()

with open("C:\\Users\\My Desktop\\Documents\\GitHub\\github_listener_2\\commits.md", 'a') as f:
    f.truncate(0)

    for commit in commits:
        author = commit.commit.committer.name
        date = commit.stats.last_modified
        summary_description = commit.commit.message
        splitting = summary_description.splitlines()
        summary = splitting[0]
        description = "".join(splitting[1:])
        if "#" in description[:2]:
            description = font_colour_picker(description)

        f.write("\n")
        f.write(f"####Author:\n {author}\n")
        f.write(f"####Date Modified:\n {date}\n")
        f.write(f"####Summary:\n {summary}\n")
        f.write(f"####Description:\n {description}\n")
        f.write("<hr>\n")

md_to_html = markdown2.markdown_path("C:\\Users\\My Desktop\\Documents\\GitHub\\github_listener_2\\commits.md")

Html_file = open("commits.html", "w")
Html_file.write(md_to_html)

# DESCRIPTION SORTING
# #r_s = red and small   #g_s = green and small  #b_s = blue and small
# #r_m = red and medium  #g_m = green and medium  #b_m = blue and medium
# #r_b = red and big     #g_b = green and big  #b_b = blue and big



