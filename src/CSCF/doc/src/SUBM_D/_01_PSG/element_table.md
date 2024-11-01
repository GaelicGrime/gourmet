class Table(Element)
      Table(values, headings=None, visible_column_map=None, col_widths=None, def_col_width=10, auto_size_columns=True, max_col_width=20, select_mode=None, display_row_numbers=False, num_rows=None, row_height=None, font=None, justification='right', text_color=None, background_color=None, alternating_row_color=None, selected_row_colors=(None, None), header_text_color=None, header_background_color=None, header_font=None, header_border_width=None, header_relief=None, row_colors=None, vertical_scroll_only=True, hide_vertical_scroll=False, border_width=None, sbar_trough_color=None, sbar_background_color=None, sbar_arrow_color=None, sbar_width=None, sbar_arrow_width=None, sbar_frame_color=None, sbar_relief=None, size=(None, None), s=(None, None), change_submits=False, enable_events=False, enable_click_events=False, right_click_selects=False, bind_return_key=False, pad=None, p=None, key=None, k=None, tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, metadata=None)
 
# ---------------------------------------------------------------------- #
#                           Table                                        #
# ---------------------------------------------------------------------- #
 
    

Method resolution order:
    Table
    Element
    builtins.object

Methods defined here:

Get = get(self)

Update = update(self, values=None, num_rows=None, visible=None, select_rows=None, alternating_row_color=None, row_colors=None)

__init__(self, values, headings=None, visible_column_map=None, col_widths=None, def_col_width=10, auto_size_columns=True, max_col_width=20, select_mode=None, display_row_numbers=False, num_rows=None, row_height=None, font=None, justification='right', text_color=None, background_color=None, alternating_row_color=None, selected_row_colors=(None, None), header_text_color=None, header_background_color=None, header_font=None, header_border_width=None, header_relief=None, row_colors=None, vertical_scroll_only=True, hide_vertical_scroll=False, border_width=None, sbar_trough_color=None, sbar_background_color=None, sbar_arrow_color=None, sbar_width=None, sbar_arrow_width=None, sbar_frame_color=None, sbar_relief=None, size=(None, None), s=(None, None), change_submits=False, enable_events=False, enable_click_events=False, right_click_selects=False, bind_return_key=False, pad=None, p=None, key=None, k=None, tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, metadata=None)
    :param values:                  Your table data represented as a 2-dimensions table... a list of rows, with each row representing a row in your table.
    :type values:                   List[List[str | int | float]]
    :param headings:                The headings to show on the top line
    :type headings:                 List[str]
    :param visible_column_map:      One entry for each column. False indicates the column is not shown
    :type visible_column_map:       List[bool]
    :param col_widths:              Number of characters that each column will occupy
    :type col_widths:               List[int]
    :param def_col_width:           Default column width in characters
    :type def_col_width:            (int)
    :param auto_size_columns:       if True columns will be sized automatically
    :type auto_size_columns:        (bool)
    :param max_col_width:           Maximum width for all columns in characters
    :type max_col_width:            (int)
    :param select_mode:             Select Mode. Valid values start with "TABLE_SELECT_MODE_".  Valid values are: TABLE_SELECT_MODE_NONE TABLE_SELECT_MODE_BROWSE TABLE_SELECT_MODE_EXTENDED
    :type select_mode:              (enum)
    :param display_row_numbers:     if True, the first column of the table will be the row #
    :type display_row_numbers:      (bool)
    :param num_rows:                The number of rows of the table to display at a time
    :type num_rows:                 (int)
    :param row_height:              height of a single row in pixels
    :type row_height:               (int)
    :param font:                    specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:                     (str or (str, int[, str]) or None)
    :param justification:           'left', 'right', 'center' are valid choices
    :type justification:            (str)
    :param text_color:              color of the text
    :type text_color:               (str)
    :param background_color:        color of background
    :type background_color:         (str)
    :param alternating_row_color:   if set then every other row will have this color in the background.
    :type alternating_row_color:    (str)
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
    :param row_colors:              list of tuples of (row, background color) OR (row, foreground color, background color). Sets the colors of listed rows to the color(s) provided (note the optional foreground color)
    :type row_colors:               List[Tuple[int, str] | Tuple[Int, str, str]]
    :param vertical_scroll_only:    if True only the vertical scrollbar will be visible
    :type vertical_scroll_only:     (bool)
    :param hide_vertical_scroll:    if True vertical scrollbar will be hidden
    :type hide_vertical_scroll:     (bool)
    :param border_width:            Border width/depth in pixels
    :type border_width:             (int)
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
    :param size:                    DO NOT USE! Use num_rows instead
    :type size:                     (int, int)
    :param change_submits:          DO NOT USE. Only listed for backwards compat - Use enable_events instead
    :type change_submits:           (bool)
    :param enable_events:           Turns on the element specific events. Table events happen when row is clicked
    :type enable_events:            (bool)
    :param enable_click_events:     Turns on the element click events that will give you (row, col) click data when the table is clicked
    :type enable_click_events:      (bool)
    :param right_click_selects:     If True, then right clicking a row will select that row if multiple rows are not currently selected
    :type right_click_selects:      (bool)
    :param bind_return_key:         if True, pressing return key will cause event coming from Table, ALSO a left button double click will generate an event if this parameter is True
    :type bind_return_key:          (bool)
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
    :type right_click_menu:         List[List[ List[str] | str ]]
    :param expand_x:                If True the element will automatically expand in the X direction to fill available space
    :type expand_x:                 (bool)
    :param expand_y:                If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:                 (bool)
    :param visible:                 set visibility state of the element
    :type visible:                  (bool)
    :param metadata:                User metadata that can be set to ANYTHING
    :type metadata:                 (Any)

get(self)
    Dummy function for tkinter port.  In the Qt port you can read back the values in the table in case they were
    edited.  Don't know yet how to enable editing of a Tree in tkinter so just returning the values provided by
    user when Table was created or Updated.
     
    :return: the current table values (for now what was originally provided up updated)
    :rtype:  List[List[Any]]

get_last_clicked_position(self)
    Returns a tuple with the row and column of the cell that was last clicked.
    Headers will have a row == -1 and the Row Number Column (if present) will have a column == -1
    :return: The (row,col) position of the last cell clicked in the table
    :rtype:  (int | None, int | None)

update(self, values=None, num_rows=None, visible=None, select_rows=None, alternating_row_color=None, row_colors=None)
    Changes some of the settings for the Table Element. Must call `Window.Read` or `Window.Finalize` prior
     
    Changes will not be visible in your window until you call window.read or window.refresh.
     
    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.
     
    :param values:                A new 2-dimensional table to show
    :type values:                 List[List[str | int | float]]
    :param num_rows:              How many rows to display at a time
    :type num_rows:               (int)
    :param visible:               if True then will be visible
    :type visible:                (bool)
    :param select_rows:           List of rows to select as if user did
    :type select_rows:            List[int]
    :param alternating_row_color: the color to make every other row
    :type alternating_row_color:  (str)
    :param row_colors:            list of tuples of (row, background color) OR (row, foreground color, background color). Changes the colors of listed rows to the color(s) provided (note the optional foreground color)
    :type row_colors:             List[Tuple[int, str] | Tuple[Int, str, str]]
