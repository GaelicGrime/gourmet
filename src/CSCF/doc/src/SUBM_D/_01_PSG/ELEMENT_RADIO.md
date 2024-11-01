Get = get\(self\)

ResetGroup = reset_group\(self\)

Update = update\(self, value=None, text=None, background_color=None, text_color=None, circle_color=None, disabled=None, visible=None\)

\_\_init\_\_\(self, text, group_id, default=False, disabled=False, size=\(None, None\), s=\(None, None\), auto_size_text=None, background_color=None, text_color=None, circle_color=None, font=None, key=None, k=None, pad=None, p=None, tooltip=None, change_submits=False, enable_events=False, right_click_menu=None, expand_x=False, expand_y=False, visible=True, metadata=None\)
    :param text:             Text to display next to button
    :type text:              \(str\)
    :param group_id:         Groups together multiple Radio Buttons. Any type works
    :type group_id:          \(Any\)
    :param default:          Set to True for the one element of the group you want initially selected
    :type default:           \(bool\)
    :param disabled:         set disable state
    :type disabled:          \(bool\)
    :param size:             \(w, h\) w=characters-wide, h=rows-high. If an int instead of a tuple is supplied, then height is auto-set to 1
    :type size:              \(int, int\)  | \(None, None\) | int
    :param s:                Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
    :type s:                 \(int, int\)  | \(None, None\) | int
    :param auto_size_text:   if True will size the element to match the length of the text
    :type auto_size_text:    \(bool\)
    :param background_color: color of background
    :type background_color:  \(str\)
    :param text_color:       color of the text
    :type text_color:        \(str\)
    :param circle_color:     color of background of the circle that has the dot selection indicator in it
    :type circle_color:      \(str\)
    :param font:             specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:              \(str or \(str, int\[, str\]\) or None\)
    :param key:              Used with window.find_element and with return values to uniquely identify this element
    :type key:               str | int | tuple | object
    :param k:                Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                 str | int | tuple | object
    :param pad:              Amount of padding to put around element in pixels \(left/right, top/bottom\) or \(\(left, right\), \(top, bottom\)\) or an int. If an int, then it's converted into a tuple \(int, int\)
    :type pad:               \(int, int\) or \(\(int, int\),\(int,int\)\) or \(int,\(int,int\)\) or  \(\(int, int\),int\) | int
    :param p:                Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                 \(int, int\) or \(\(int, int\),\(int,int\)\) or \(int,\(int,int\)\) or  \(\(int, int\),int\) | int
    :param tooltip:          text, that will appear when mouse hovers over the element
    :type tooltip:           \(str\)
    :param change_submits:   DO NOT USE. Only listed for backwards compat - Use enable_events instead
    :type change_submits:    \(bool\)
    :param enable_events:    Turns on the element specific events. Radio Button events happen when an item is selected
    :type enable_events:     \(bool\)
    :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu:  List\[List\[ List\[str\] | str \]\]
    :param expand_x:         If True the element will automatically expand in the X direction to fill available space
    :type expand_x:          \(bool\)
    :param expand_y:         If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:          \(bool\)
    :param visible:          set visibility state of the element
    :type visible:           \(bool\)
    :param metadata:         User metadata that can be set to ANYTHING
    :type metadata:          \(Any\)

get\(self\)
    A snapshot of the value of Radio Button -> \(bool\)

    :return: True if this radio button is selected
    :rtype:  \(bool\)

reset_group\(self\)
    Sets all Radio Buttons in the group to not selected

update\(self, value=None, text=None, background_color=None, text_color=None, circle_color=None, disabled=None, visible=None\)
    Changes some of the settings for the Radio Button Element. Must call `Window.read` or `Window.finalize` prior

    Changes will not be visible in your window until you call window.read or window.refresh.

    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.

    :param value:            if True change to selected and set others in group to unselected
    :type value:             \(bool\)
    :param text:             Text to display next to radio button
    :type text:              \(str\)
    :param background_color: color of background
    :type background_color:  \(str\)
    :param text_color:       color of the text. Note this also changes the color of the selection dot
    :type text_color:        \(str\)
    :param circle_color:     color of background of the circle that has the dot selection indicator in it
    :type circle_color:      \(str\)
    :param disabled:         disable or enable state of the element
    :type disabled:          \(bool\)
    :param visible:          control visibility of element
    :type visible:           \(bool\)
