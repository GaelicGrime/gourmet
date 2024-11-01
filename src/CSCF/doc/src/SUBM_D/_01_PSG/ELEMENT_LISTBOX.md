GetIndexes = get_indexes\(self\)

GetListValues = get_list_values\(self\)

SetValue = set_value\(self, values\)

Update = update\(self, values=None, disabled=None, set_to_index=None, scroll_to_index=None, select_mode=None, visible=None\)

\_\_init\_\_\(self, values, default_values=None, select_mode=None, change_submits=False, enable_events=False, bind_return_key=False, size=\(None, None\), s=\(None, None\), disabled=False, auto_size_text=None, font=None, no_scrollbar=False, horizontal_scroll=False, background_color=None, text_color=None, highlight_background_color=None, highlight_text_color=None, key=None, k=None, pad=None, p=None, tooltip=None, expand_x=False, expand_y=False, right_click_menu=None, visible=True, metadata=None\)
    :param values:                     list of values to display. Can be any type including mixed types as long as they have \_\_str\_\_ method
    :type values:                      List\[Any\] or Tuple\[Any\]
    :param default_values:             which values should be initially selected
    :type default_values:              List\[Any\]
    :param select_mode:                Select modes are used to determine if only 1 item can be selected or multiple and how they can be selected.   Valid choices begin with "LISTBOX_SELECT_MODE_" and include: LISTBOX_SELECT_MODE_SINGLE LISTBOX_SELECT_MODE_MULTIPLE LISTBOX_SELECT_MODE_BROWSE LISTBOX_SELECT_MODE_EXTENDED
    :type select_mode:                 \[enum\]
    :param change_submits:             DO NOT USE. Only listed for backwards compat - Use enable_events instead
    :type change_submits:              \(bool\)
    :param enable_events:              Turns on the element specific events. Listbox generates events when an item is clicked
    :type enable_events:               \(bool\)
    :param bind_return_key:            If True, then the return key will cause a the Listbox to generate an event
    :type bind_return_key:             \(bool\)
    :param size:                       w=characters-wide, h=rows-high. If an int instead of a tuple is supplied, then height is auto-set to 1
    :type size:                        \(int, int\) |  \(int, None\) | int
    :param s:                          Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
    :type s:                           \(int, int\)  | \(None, None\) | int
    :param disabled:                   set disable state for element
    :type disabled:                    \(bool\)
    :param auto_size_text:             True if element should be the same size as the contents
    :type auto_size_text:              \(bool\)
    :param font:                       specifies the font family, size, etc.  Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:                        \(str or \(str, int\[, str\]\) or None\)
    :param no_scrollbar:               Controls if a scrollbar should be shown.  If True, no scrollbar will be shown
    :type no_scrollbar:                \(bool\)
    :param horizontal_scroll:          Controls if a horizontal scrollbar should be shown.  If True a horizontal scrollbar will be shown in addition to vertical
    :type horizontal_scroll:           \(bool\)
    :param background_color:           color of background
    :type background_color:            \(str\)
    :param text_color:                 color of the text
    :type text_color:                  \(str\)
    :param highlight_background_color: color of the background when an item is selected. Defaults to normal text color \(a reverse look\)
    :type highlight_background_color:  \(str\)
    :param highlight_text_color:       color of the text when an item is selected. Defaults to the normal background color \(a rerverse look\)
    :type highlight_text_color:        \(str\)
    :param key:                        Used with window.find_element and with return values to uniquely identify this element
    :type key:                         str | int | tuple | object
    :param k:                          Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                           str | int | tuple | object
    :param pad:                        Amount of padding to put around element in pixels \(left/right, top/bottom\) or \(\(left, right\), \(top, bottom\)\) or an int. If an int, then it's converted into a tuple \(int, int\)
    :type pad:                         \(int, int\) or \(\(int, int\),\(int,int\)\) or \(int,\(int,int\)\) or  \(\(int, int\),int\) | int
    :param p:                          Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                           \(int, int\) or \(\(int, int\),\(int,int\)\) or \(int,\(int,int\)\) or  \(\(int, int\),int\) | int
    :param tooltip:                    text, that will appear when mouse hovers over the element
    :type tooltip:                     \(str\)
    :param expand_x:                   If True the element will automatically expand in the X direction to fill available space
    :type expand_x:                    \(bool\)
    :param expand_y:                   If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:                    \(bool\)
    :param right_click_menu:           A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu:            List\[List\[ List\[str\] | str \]\]
    :param visible:                    set visibility state of the element
    :type visible:                     \(bool\)
    :param metadata:                   User metadata that can be set to ANYTHING
    :type metadata:                    \(Any\)

get\(self\)
    Returns the list of items currently selected in this listbox.  It should be identical
    to the value you would receive when performing a window.read\(\) call.

    :return: The list of currently selected items. The actual items are returned, not the indexes
    :rtype:  List\[Any\]

get_indexes\(self\)
    Returns the items currently selected as a list of indexes

    :return: A list of offsets into values that is currently selected
    :rtype:  List\[int\]

get_list_values\(self\)
    Returns list of Values provided by the user in the user's format

    :return: List of values. Can be any / mixed types -> \[\]
    :rtype:  List\[Any\]

set_value\(self, values\)
    Set listbox highlighted choices

    :param values: new values to choose based on previously set values
    :type values:  List\[Any\] | Tuple\[Any\]

update\(self, values=None, disabled=None, set_to_index=None, scroll_to_index=None, select_mode=None, visible=None\)
    Changes some of the settings for the Listbox Element. Must call `Window.Read` or `Window.Finalize` prior
    Changes will not be visible in your window until you call window.read or window.refresh.

    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.

    :param values:          new list of choices to be shown to user
    :type values:           List\[Any\]
    :param disabled:        disable or enable state of the element
    :type disabled:         \(bool\)
    :param set_to_index:    highlights the item\(s\) indicated. If parm is an int one entry will be set. If is a list, then each entry in list is highlighted
    :type set_to_index:     int | list | tuple
    :param scroll_to_index: scroll the listbox so that this index is the first shown
    :type scroll_to_index:  \(int\)
    :param select_mode:     changes the select mode according to tkinter's listbox widget
    :type select_mode:      \(str\)
    :param visible:         control visibility of element
    :type visible:          \(bool\)
