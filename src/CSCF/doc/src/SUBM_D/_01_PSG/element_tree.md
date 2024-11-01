class Tree(Element)
      Tree(data=None, headings=None, visible_column_map=None, col_widths=None, col0_width=10, col0_heading='', def_col_width=10, auto_size_columns=True, max_col_width=20, select_mode=None, show_expanded=False, change_submits=False, enable_events=False, font=None, justification='right', text_color=None, border_width=None, background_color=None, selected_row_colors=(None, None), header_text_color=None, header_background_color=None, header_font=None, header_border_width=None, header_relief=None, num_rows=None, sbar_trough_color=None, sbar_background_color=None, sbar_arrow_color=None, sbar_width=None, sbar_arrow_width=None, sbar_frame_color=None, sbar_relief=None, row_height=None, vertical_scroll_only=True, hide_vertical_scroll=False, pad=None, p=None, key=None, k=None, tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, metadata=None)
 
Tree Element - Presents data in a tree-like manner, much like a file/folder browser.  Uses the TreeData class
to hold the user's data and pass to the element for display.
 
    

Method resolution order:
    Tree
    Element
    builtins.object

Methods defined here:

Update = update(self, values=None, key=None, value=None, text=None, icon=None, visible=None)

__init__(self, data=None, headings=None, visible_column_map=None, col_widths=None, col0_width=10, col0_heading='', def_col_width=10, auto_size_columns=True, max_col_width=20, select_mode=None, show_expanded=False, change_submits=False, enable_events=False, font=None, justification='right', text_color=None, border_width=None, background_color=None, selected_row_colors=(None, None), header_text_color=None, header_background_color=None, header_font=None, header_border_width=None, header_relief=None, num_rows=None, sbar_trough_color=None, sbar_background_color=None, sbar_arrow_color=None, sbar_width=None, sbar_arrow_width=None, sbar_frame_color=None, sbar_relief=None, row_height=None, vertical_scroll_only=True, hide_vertical_scroll=False, pad=None, p=None, key=None, k=None, tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, metadata=None)
    :param data:                    The data represented using a PySimpleGUI provided TreeData class
    :type data:                     (TreeData)
    :param headings:                List of individual headings for each column
    :type headings:                 List[str]
    :param visible_column_map:      Determines if a column should be visible. If left empty, all columns will be shown
    :type visible_column_map:       List[bool]
    :param col_widths:              List of column widths so that individual column widths can be controlled
    :type col_widths:               List[int]
    :param col0_width:              Size of Column 0 which is where the row numbers will be optionally shown
    :type col0_width:               (int)
    :param col0_heading:            Text to be shown in the header for the left-most column
    :type col0_heading:             (str)
    :param def_col_width:           default column width
    :type def_col_width:            (int)
    :param auto_size_columns:       if True, the size of a column is determined  using the contents of the column
    :type auto_size_columns:        (bool)
    :param max_col_width:           the maximum size a column can be
    :type max_col_width:            (int)
    :param select_mode:             Use same values as found on Table Element.  Valid values include: TABLE_SELECT_MODE_NONE TABLE_SELECT_MODE_BROWSE TABLE_SELECT_MODE_EXTENDED
    :type select_mode:              (enum)
    :param show_expanded:           if True then the tree will be initially shown with all nodes completely expanded
    :type show_expanded:            (bool)
    :param change_submits:          DO NOT USE. Only listed for backwards compat - Use enable_events instead
    :type change_submits:           (bool)
    :param enable_events:           Turns on the element specific events. Tree events happen when row is clicked
    :type enable_events:            (bool)
    :param font:                    specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:                     (str or (str, int[, str]) or None)
    :param justification:           'left', 'right', 'center' are valid choices
    :type justification:            (str)
    :param text_color:              color of the text
    :type text_color:               (str)
    :param border_width:            Border width/depth in pixels
    :type border_width:             (int)
    :param background_color:        color of background
    :type background_color:         (str)
    :param selected_row_colors:     Sets the text color and background color for a selected row. Same format as button colors - tuple ('red', 'yellow') or string 'red on yellow'. Defaults to theme's button color
    :type selected_row_colors:      str or (str, str)
    :param header_text_color:       sets the text color for the header
    :type header_text_color:        (str)
    :param header_background_color: sets the background color for the header
    :type header_background_color:  (str)
    :param header_font:             specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type header_font:              (str or (str, int[, str]) or None)
    :param header_border_width:     Border width for the header portion
    :type header_border_width:      (int | None)
    :param header_relief:           Relief style for the header. Values are same as other elements that use relief. RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID
    :type header_relief:            (str | None)
    :param num_rows:                The number of rows of the table to display at a time
    :type num_rows:                 (int)
    :param row_height:              height of a single row in pixels
    :type row_height:               (int)
    :param vertical_scroll_only:    if True only the vertical scrollbar will be visible
    :type vertical_scroll_only:     (bool)
    :param hide_vertical_scroll:    if True vertical scrollbar will be hidden
    :type hide_vertical_scroll:     (bool)
    :param sbar_trough_color:           Scrollbar color of the trough
    :type sbar_trough_color:            (str)
    :param sbar_background_color:       Scrollbar color of the background of the arrow buttons at the ends AND the color of the "thumb" (the thing you grab and slide). Switches to arrow color when mouse is over
    :type sbar_background_color:        (str)
    :param sbar_arrow_color:            Scrollbar color of the arrow at the ends of the scrollbar (it looks like a button). Switches to background color when mouse is over
    :type sbar_arrow_color:             (str)
    :param sbar_width:                  Scrollbar width in pixels
    :type sbar_width:                   (int)
    :param sbar_arrow_width:            Scrollbar width of the arrow on the scrollbar. It will potentially impact the overall width of the scrollbar
    :type sbar_arrow_width:             (int)
    :param sbar_frame_color:            Scrollbar Color of frame around scrollbar (available only on some ttk themes)
    :type sbar_frame_color:             (str)
    :param sbar_relief:                 Scrollbar relief that will be used for the "thumb" of the scrollbar (the thing you grab that slides). Should be a constant that is defined at starting with "RELIEF_" - RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID
    :type sbar_relief:                  (str)
    :param pad:                     Amount of padding to put around element in pixels (left/right, top/bottom) or ((left, right), (top, bottom)) or an int. If an int, then it's converted into a tuple (int, int)
    :type pad:                      (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param p:                       Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                        (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param key:                     Used with window.find_element and with return values to uniquely identify this element to uniquely identify this element
    :type key:                      str | int | tuple | object
    :param k:                       Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                        str | int | tuple | object
    :param tooltip:                 text, that will appear when mouse hovers over the element
    :type tooltip:                  (str)
    :param right_click_menu:        A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu:         List[List[str] | str]]
    :param expand_x:                If True the element will automatically expand in the X direction to fill available space
    :type expand_x:                 (bool)
    :param expand_y:                If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:                 (bool)
    :param visible:                 set visibility state of the element
    :type visible:                  (bool)
    :param metadata:                User metadata that can be set to ANYTHING
    :type metadata:                 (Any)

add_treeview_data(self, node)
    Not a user function.  Recursive method that inserts tree data into the tkinter treeview widget.
     
    :param node: The node to insert.  Will insert all nodes from starting point downward, recursively
    :type node:  (TreeData)

update(self, values=None, key=None, value=None, text=None, icon=None, visible=None)
    Changes some of the settings for the Tree Element. Must call `Window.Read` or `Window.Finalize` prior
     
    Changes will not be visible in your window until you call window.read or window.refresh.
     
    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.
     
    :param values:  Representation of the tree
    :type values:   (TreeData)
    :param key:     identifies a particular item in tree to update
    :type key:      str | int | tuple | object
    :param value:   sets the node identified by key to a particular value
    :type value:    (Any)
    :param text:    sets the node identified by key to this string
    :type text:     (str)
    :param icon:    can be either a base64 icon or a filename for the icon
    :type icon:     bytes | str
    :param visible: control visibility of element
    :type visible:  (bool)
