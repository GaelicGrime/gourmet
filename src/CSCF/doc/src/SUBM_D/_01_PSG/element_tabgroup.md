class TabGroup(Element)
      TabGroup(layout, tab_location=None, title_color=None, tab_background_color=None, selected_title_color=None, selected_background_color=None, background_color=None, focus_color=None, font=None, change_submits=False, enable_events=False, pad=None, p=None, border_width=None, tab_border_width=None, theme=None, key=None, k=None, size=(None, None), s=(None, None), tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, metadata=None)
 
TabGroup Element groups together your tabs into the group of tabs you see displayed in your window
 
    

Method resolution order:
    TabGroup
    Element
    builtins.object

Methods defined here:

AddRow = add_row(self, *args)

FindKeyFromTabName = find_key_from_tab_name(self, tab_name)

Get = get(self)

Layout = layout(self, rows)

__init__(self, layout, tab_location=None, title_color=None, tab_background_color=None, selected_title_color=None, selected_background_color=None, background_color=None, focus_color=None, font=None, change_submits=False, enable_events=False, pad=None, p=None, border_width=None, tab_border_width=None, theme=None, key=None, k=None, size=(None, None), s=(None, None), tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, metadata=None)
    :param layout:                    Layout of Tabs. Different than normal layouts. ALL Tabs should be on first row
    :type layout:                     List[List[Tab]]
    :param tab_location:              location that tabs will be displayed. Choices are left, right, top, bottom, lefttop, leftbottom, righttop, rightbottom, bottomleft, bottomright, topleft, topright
    :type tab_location:               (str)
    :param title_color:               color of text on tabs
    :type title_color:                (str)
    :param tab_background_color:      color of all tabs that are not selected
    :type tab_background_color:       (str)
    :param selected_title_color:      color of tab text when it is selected
    :type selected_title_color:       (str)
    :param selected_background_color: color of tab when it is selected
    :type selected_background_color:  (str)
    :param background_color:          color of background area that tabs are located on
    :type background_color:           (str)
    :param focus_color:               color of focus indicator on the tabs
    :type focus_color:                (str)
    :param font:                      specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:                       (str or (str, int[, str]) or None)
    :param change_submits:            * DEPRICATED DO NOT USE. Use `enable_events` instead
    :type change_submits:             (bool)
    :param enable_events:             If True then switching tabs will generate an Event
    :type enable_events:              (bool)
    :param pad:                       Amount of padding to put around element in pixels (left/right, top/bottom) or ((left, right), (top, bottom)) or an int. If an int, then it's converted into a tuple (int, int)
    :type pad:                        (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param p:                         Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                          (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param border_width:              width of border around element in pixels
    :type border_width:               (int)
    :param tab_border_width:          width of border around the tabs
    :type tab_border_width:           (int)
    :param theme:                     DEPRICATED - You can only specify themes using set options or when window is created. It's not possible to do it on an element basis
    :type theme:                      (enum)
    :param key:                       Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
    :type key:                        str | int | tuple | object
    :param k:                         Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                          str | int | tuple | object
    :param size:                      (width, height) w=pixels-wide, h=pixels-high. Either item in tuple can be None to indicate use the computed value and set only 1 direction
    :type size:                       (int|None, int|None)
    :param s:                         Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
    :type s:                          (int|None, int|None)
    :param tooltip:                   text, that will appear when mouse hovers over the element
    :type tooltip:                    (str)
    :param right_click_menu:          A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu:           List[List[ List[str] | str ]]
    :param expand_x:                  If True the element will automatically expand in the X direction to fill available space
    :type expand_x:                   (bool)
    :param expand_y:                  If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:                   (bool)
    :param visible:                   set visibility state of the element
    :type visible:                    (bool)
    :param metadata:                  User metadata that can be set to ANYTHING
    :type metadata:                   (Any)

add_row(self, *args)
    Not recommended user call.  Used to add rows of Elements to the Frame Element.
     
    :param *args:     The list of elements for this row
    :type *args:      List[Element]

add_tab(self, tab_element)
    Add a new tab to an existing TabGroup
    This call was written so that tabs can be added at runtime as your user performs operations.
    Your Window should already be created and finalized.
     
    :param tab_element: A Tab Element that has a layout in it
    :type tab_element:  Tab

find_key_from_tab_name(self, tab_name)
    Searches through the layout to find the key that matches the text on the tab. Implies names should be unique
     
    :param tab_name: name of a tab
    :type tab_name:  str
    :return:         Returns the key or None if no key found
    :rtype:          key | None

get(self)
    Returns the current value for the Tab Group, which will be the currently selected tab's KEY or the text on
    the tab if no key is defined.  Returns None if an error occurs.
    Note that this is exactly the same data that would be returned from a call to Window.Read. Are you sure you
    are using this method correctly?
     
    :return: The key of the currently selected tab or the tab's text if it has no key
    :rtype:  Any | None

layout(self, rows)
    Can use like the Window.Layout method, but it's better to use the layout parameter when creating
     
    :param rows: The rows of Elements
    :type rows:  List[List[Element]]
    :return:     Used for chaining
    :rtype:      (Frame)
