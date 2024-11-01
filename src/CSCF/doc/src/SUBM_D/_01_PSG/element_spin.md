Get = get\(self\)

Update = update\(self, value=None, values=None, disabled=None, readonly=None, visible=None\)

\_\_init\_\_\(self, values, initial_value=None, disabled=False, change_submits=False, enable_events=False, readonly=False, size=\(None, None\), s=\(None, None\), auto_size_text=None, font=None, background_color=None, text_color=None, key=None, k=None, pad=None, p=None, tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, metadata=None\)
    :param values:           List of valid values
    :type values:            Tuple\[Any] or List\[Any]
    :param initial_value:    Initial item to show in window. Choose from list of values supplied
    :type initial_value:     \(Any\)
    :param disabled:         set disable state
    :type disabled:          \(bool\)
    :param change_submits:   DO NOT USE. Only listed for backwards compat - Use enable_events instead
    :type change_submits:    \(bool\)
    :param enable_events:    Turns on the element specific events. Spin events happen when an item changes
    :type enable_events:     \(bool\)
    :param readonly:         Turns on the element specific events. Spin events happen when an item changes
    :type readonly:          \(bool\)
    :param size:             \(w, h\) w=characters-wide, h=rows-high. If an int instead of a tuple is supplied, then height is auto-set to 1
    :type size:              \(int, int\)  | \(None, None\) | int
    :param s:                Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
    :type s:                 \(int, int\)  | \(None, None\) | int
    :param auto_size_text:   if True will size the element to match the length of the text
    :type auto_size_text:    \(bool\)
    :param font:             specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:              \(str or \(str, int\[, str]\) or None\)
    :param background_color: color of background
    :type background_color:  \(str\)
    :param text_color:       color of the text
    :type text_color:        \(str\)
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
    :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu:  List\[List\[ List\[str] | str ]]
    :param expand_x:         If True the element will automatically expand in the X direction to fill available space
    :type expand_x:          \(bool\)
    :param expand_y:         If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:          \(bool\)
    :param visible:          set visibility state of the element
    :type visible:           \(bool\)
    :param metadata:         User metadata that can be set to ANYTHING
    :type metadata:          \(Any\)

get\(self\)
    Return the current chosen value showing in spinbox.
    This value will be the same as what was provided as list of choices.  If list items are ints, then the
    item returned will be an int \(not a string\)

    :return: The currently visible entry
    :rtype:  \(Any\)

update\(self, value=None, values=None, disabled=None, readonly=None, visible=None\)
    Changes some of the settings for the Spin Element. Must call `Window.Read` or `Window.Finalize` prior
    Note that the state can be in 3 states only.... enabled, disabled, readonly even
    though more combinations are available. The easy way to remember is that if you
    change the readonly parameter then you are enabling the element.

    Changes will not be visible in your window until you call window.read or window.refresh.

    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.

    :param value:    set the current value from list of choices
    :type value:     \(Any\)
    :param values:   set available choices
    :type values:    List\[Any]
    :param disabled: disable. Note disabled and readonly cannot be mixed. It must be one OR the other
    :type disabled:  \(bool\)
    :param readonly: make element readonly.  Note disabled and readonly cannot be mixed. It must be one OR the other
    :type readonly:  \(bool\)
    :param visible:  control visibility of element
    :type visible:   \(bool\)
