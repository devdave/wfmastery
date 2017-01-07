# pylint: disable-msg=C0103,C0301,C0111,E1101,C0321
#kindly fuck off, I know

import data_v1 as d1
import operator as OP

item_element = """
            <label class="individual" id="lab_check_{id}" data-id="{id}" data-state="False">{name}</label>
            <input class="individual_input" name="lab_check_{id}" type="checkbox" data-mtype="{mtype}" data-stype="{stype}" data-id="{id}" value=0>
"""

item_line = """<span class="subgroup_box">
                    <label class="subgroup">{name}</label>
                    <span class="sgroup_box">{body}</span>
               </span><br/>
"""

main_group = """
    <fieldset class="menu_tab" id="mtype_{mtype_name}" data-active="{is_on}">
        <legend>{mtype_name}</legend>
        <span class="type_box">{body}</span>
    </fieldset>
"""
menu_item = """
            <li class="menu-option" id="menutab_{name}" data-active="{is_on}" data-dest="mtype_{name}">{name}</li>
"""

html_body = """
<!doctype html>
<html>
    <head>
        <title>MR hell</title>
        <link rel="stylesheet" type="text/css" href="./style.css">
        <script src="./script.js"></script>
    </head>
    <body>
        <ul class="menu">
            {menu_names}
        </ul>
        <p>MR hell checklist</p>
        {body}
    </body>
</html>
"""


def main():


    group_html = ""

    sorted_main_types = "Primary,Secondary,Melee,Dojo,Sentinel,Archwing".split(",")
    active_type = "Primary"

    for group_key in sorted_main_types:
        temp = d1.indexed[group_key]
        buffer = ""

        for stype in sorted(temp.keys()):
            sub_buffer = ""
            ordered = sorted(temp[stype], key=lambda x: x["name"])

            for thing in ordered:
                item_html = item_element.format(**thing)
                sub_buffer += item_html + "\n"
            buffer += item_line.format(name=stype, body=sub_buffer) + "\n"

        group_html += main_group.format(mtype_name=group_key, body=buffer, is_on=group_key == active_type)
        # print(group_html)

    menu_list = "\n".join([menu_item.format(name=x, is_on=sorted_main_types[0] == x) for x in sorted_main_types])


    with open("checklist.html", "w") as my_file:
        my_file.write(html_body.format(body=group_html, menu_names=menu_list))



if __name__ == '__main__': main()
