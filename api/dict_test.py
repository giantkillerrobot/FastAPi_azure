# Testing some work on dictionaries



dict_config =   [
  {
    "id": "book",
    "header": {
      "text": "&nbsp;",
      "autoheight": True,
      "css": "multiline"
    },
    "css": "webix_el_button",
    "width": 75,
    "template": "<a href='javascript:act_upon_function(#id#)' >Act Upon</a>"
  },
    {
    "map": "#comments#",
    "id": "comments",
    "header": {
      "text": "Comments",
      "autoheight": True,
      "css": "multiline"
    },
    "cssFormat": "",
    "sort": "string",
    "width": 200,
    "hidden": 0
  }

]


print(dict_config)