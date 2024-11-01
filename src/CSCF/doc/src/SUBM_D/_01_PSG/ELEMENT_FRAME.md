AddRow = add_row\(self, *args\)

Layout = layout\(self, rows\)

Update = update\(self, value=None, visible=None\)

\_\_init\_\_\(self, title, layout, title_color=None, background_color=None, title_location=None, relief='groove', size=\(None, None\), s=\(None, None\), font=None, pad=None, p=None, border_width=None, key=None, k=None, tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, grab=None, visible=True, element_justification='left', vertical_alignment=None, metadata=None\)
    :param title:                 text that is displayed as the Frame's "label" or title
    :type title:                  \(str\)
    :param layout:                The layout to put inside the Frame
    :type layout:                 List\[List\[Elements\]\]
    :param title_color:           color of the title text
    :type title_color:            \(str\)
    :param background_color:      background color of the Frame
    :type background_color:       \(str\)
    :param title_location:        location to place the text title.  Choices include: TITLE_LOCATION_TOP TITLE_LOCATION_BOTTOM TITLE_LOCATION_LEFT TITLE_LOCATION_RIGHT TITLE_LOCATION_TOP_LEFT TITLE_LOCATION_TOP_RIGHT TITLE_LOCATION_BOTTOM_LEFT TITLE_LOCATION_BOTTOM_RIGHT
    :type title_location:         \(enum\)
    :param relief:                relief style. Values are same as other elements with reliefs. Choices include RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID
    :type relief:                 \(enum\)
    :param size:                  \(width, height\) Sets an initial hard-coded size for the Frame. This used to be a problem, but was fixed in 4.53.0 and works better than Columns when using the size paramter
    :type size:                   \(int, int\)
    :param s:                     Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
    :type s:                      \(int, int\)  | \(None, None\) | int
    :param font:                  specifies the  font family, size, etc. for the TITLE. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:                   \(str or \(str, int\[, str\]\) or None\)
    :param pad:                   Amount of padding to put around element in pixels \(left/right, top/bottom\) or \(\(left, right\), \(top, bottom\)\) or an int. If an int, then it's converted into a tuple \(int, int\)
    :type pad:                    \(int, int\) or \(\(int, int\),\(int,int\)\) or \(int,\(int,int\)\) or  \(\(int, int\),int\) | int
    :param p:                     Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                      \(int, int\) or \(\(int, int\),\(int,int\)\) or \(int,\(int,int\)\) or  \(\(int, int\),int\) | int
    :param border_width:          width of border around element in pixels
    :type border_width:           \(int\)
    :param key:                   Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
    :type key:                    str | int | tuple | object
    :param k:                     Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                      str | int | tuple | object
    :param tooltip:               text, that will appear when mouse hovers over the element
    :type tooltip:                \(str\)
    :param right_click_menu:      A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu:       List\[List\[ List\[str\] | str \]\]
    :param expand_x:              If True the element will automatically expand in the X direction to fill available space
    :type expand_x:               \(bool\)
    :param expand_y:              If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:               \(bool\)
    :param grab:                  If True can grab this element and move the window around. Default is False
    :type grab:                   \(bool\)
    :param visible:               set visibility state of the element
    :type visible:                \(bool\)
    :param element_justification: All elements inside the Frame will have this justification 'left', 'right', 'center' are valid values
    :type element_justification:  \(str\)
    :param vertical_alignment:    Place the Frame at the 'top', 'center', 'bottom' of the row \(can also use t,c,r\). Defaults to no setting \(tkinter decides\)
    :type vertical_alignment:     \(str\)
    :param metadata:              User metadata that can be set to ANYTHING
    :type metadata:               \(Any\)

add_row\(self, *args\)
    Not recommended user call.  Used to add rows of Elements to the Frame Element.

    :param *args: The list of elements for this row
    :type *args:  List\[Element\]

layout\(self, rows\)
    Can use like the Window.Layout method, but it's better to use the layout parameter when creating

    :param rows: The rows of Elements
    :type rows:  List\[List\[Element\]\]
    :return:     Used for chaining
    :rtype:      \(Frame\)

update\(self, value=None, visible=None\)
    Changes some of the settings for the Frame Element. Must call `Window.Read` or `Window.Finalize` prior

    Changes will not be visible in your window until you call window.read or window.refresh.

    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.

    :param value:   New text value to show on frame
    :type value:    \(Any\)
    :param visible: control visibility of element
    :type visible:  \(bool\)
