class Window(builtins.object)
      Window(title, layout=None, default_element_size=None, default_button_element_size=(None, None), auto_size_text=None, auto_size_buttons=None, location=(None, None), relative_location=(None, None), size=(None, None), element_padding=None, margins=(None, None), button_color=None, font=None, progress_bar_color=(None, None), background_color=None, border_depth=None, auto_close=False, auto_close_duration=3, icon=None, force_toplevel=False, alpha_channel=None, return_keyboard_events=False, use_default_focus=True, text_justification=None, no_titlebar=False, grab_anywhere=False, grab_anywhere_using_control=True, keep_on_top=None, resizable=False, disable_close=False, disable_minimize=False, right_click_menu=None, transparent_color=None, debugger_enabled=True, right_click_menu_background_color=None, right_click_menu_text_color=None, right_click_menu_disabled_text_color=None, right_click_menu_selected_colors=(None, None), right_click_menu_font=None, right_click_menu_tearoff=False, finalize=False, element_justification='left', ttk_theme=None, use_ttk_buttons=None, modal=False, enable_close_attempted_event=False, titlebar_background_color=None, titlebar_text_color=None, titlebar_font=None, titlebar_icon=None, use_custom_titlebar=None, scaling=None, sbar_trough_color=None, sbar_background_color=None, sbar_arrow_color=None, sbar_width=None, sbar_arrow_width=None, sbar_frame_color=None, sbar_relief=None, metadata=None)
 
Represents a single Window
 
    Methods defined here:

AddRow = add_row(self, *args)

AddRows = add_rows(self, rows)

BringToFront = bring_to_front(self)

Close = close(self)

CloseNonBlocking = close(self)

CloseNonBlockingForm = close(self)

CurrentLocation = current_location(self, more_accurate=False)

Disable = disable(self)

DisableDebugger = disable_debugger(self)

Disappear = disappear(self)

Elem = find_element(self, key, silent_on_error=False)

Element = find_element(self, key, silent_on_error=False)

Enable = enable(self)

EnableDebugger = enable_debugger(self)

Fill = fill(self, values_dict)

Finalize = finalize(self)

Find = find_element(self, key, silent_on_error=False)

FindElement(self, key, silent_on_error=False)
    ** Warning ** This call will eventually be depricated. **
     
    It is suggested that you modify your code to use the recommended window[key] lookup or the PEP8 compliant window.find_element(key)
     
    For now, you'll only see a message printed and the call will continue to funcation as before.
     
    :param key:             Used with window.find_element and with return values to uniquely identify this element
    :type key:              str | int | tuple | object
    :param silent_on_error: If True do not display popup nor print warning of key errors
    :type silent_on_error:  (bool)
    :return:                Return value can be: the Element that matches the supplied key if found; an Error Element if silent_on_error is False; None if silent_on_error True;
    :rtype:                 Element | Error Element | None

FindElementWithFocus = find_element_with_focus(self)

GetScreenDimensions = get_screen_dimensions(self)

GrabAnyWhereOff = grab_any_where_off(self)

GrabAnyWhereOn = grab_any_where_on(self)

Hide = hide(self)

Layout = layout(self, rows)

LayoutAndRead(self, rows, non_blocking=False)
    Deprecated!!  Now your layout your window's rows (layout) and then separately call Read.
     
    :param rows:         The layout of the window
    :type rows:          List[List[Element]]
    :param non_blocking: if True the Read call will not block
    :type non_blocking:  (bool)

LayoutAndShow(self, rows)
    Deprecated - do not use any longer.  Layout your window and then call Read.  Or can add a Finalize call before the Read

LoadFromDisk = load_from_disk(self, filename)

Maximize = maximize(self)

Minimize = minimize(self)

Move = move(self, x, y)

Normal = normal(self)

Read = read(self, timeout=None, timeout_key='__TIMEOUT__', close=False)

Reappear = reappear(self)

Refresh = refresh(self)

SaveToDisk = save_to_disk(self, filename)

SendToBack = send_to_back(self)

SetAlpha = set_alpha(self, alpha)

SetIcon = set_icon(self, icon=None, pngbase64=None)

SetTransparentColor = set_transparent_color(self, color)

UnHide = un_hide(self)

VisibilityChanged = visibility_changed(self)

__call__(self, *args, **kwargs)
    Call window.read but without having to type it out.
    window() == window.read()
    window(timeout=50) == window.read(timeout=50)
     
    :return: The famous event, values that Read returns.
    :rtype:  Tuple[Any, Dict[Any, Any]]

__getitem__(self, key)
    Returns Element that matches the passed in key.
    This is "called" by writing code as thus:
    window['element key'].Update
     
    :param key: The key to find
    :type key:  str | int | tuple | object
    :rtype:     Element | Input | Combo | OptionMenu | Listbox | Radio | Checkbox | Spin | Multiline | Text | StatusBar | Output | Button | ButtonMenu | ProgressBar | Image | Canvas | Graph | Frame | VerticalSeparator | HorizontalSeparator | Tab | TabGroup | Slider | Column | Pane | Menu | Table | Tree | ErrorElement | None

__init__(self, title, layout=None, default_element_size=None, default_button_element_size=(None, None), auto_size_text=None, auto_size_buttons=None, location=(None, None), relative_location=(None, None), size=(None, None), element_padding=None, margins=(None, None), button_color=None, font=None, progress_bar_color=(None, None), background_color=None, border_depth=None, auto_close=False, auto_close_duration=3, icon=None, force_toplevel=False, alpha_channel=None, return_keyboard_events=False, use_default_focus=True, text_justification=None, no_titlebar=False, grab_anywhere=False, grab_anywhere_using_control=True, keep_on_top=None, resizable=False, disable_close=False, disable_minimize=False, right_click_menu=None, transparent_color=None, debugger_enabled=True, right_click_menu_background_color=None, right_click_menu_text_color=None, right_click_menu_disabled_text_color=None, right_click_menu_selected_colors=(None, None), right_click_menu_font=None, right_click_menu_tearoff=False, finalize=False, element_justification='left', ttk_theme=None, use_ttk_buttons=None, modal=False, enable_close_attempted_event=False, titlebar_background_color=None, titlebar_text_color=None, titlebar_font=None, titlebar_icon=None, use_custom_titlebar=None, scaling=None, sbar_trough_color=None, sbar_background_color=None, sbar_arrow_color=None, sbar_width=None, sbar_arrow_width=None, sbar_frame_color=None, sbar_relief=None, metadata=None)
    :param title:                                The title that will be displayed in the Titlebar and on the Taskbar
    :type title:                                 (str)
    :param layout:                               The layout for the window. Can also be specified in the Layout method
    :type layout:                                List[List[Element]] | Tuple[Tuple[Element]]
    :param default_element_size:                 size in characters (wide) and rows (high) for all elements in this window
    :type default_element_size:                  (int, int) - (width, height)
    :param default_button_element_size:          (width, height) size in characters (wide) and rows (high) for all Button elements in this window
    :type default_button_element_size:           (int, int)
    :param auto_size_text:                       True if Elements in Window should be sized to exactly fir the length of text
    :type auto_size_text:                        (bool)
    :param auto_size_buttons:                    True if Buttons in this Window should be sized to exactly fit the text on this.
    :type auto_size_buttons:                     (bool)
    :param relative_location:                    (x,y) location relative to the default location of the window, in pixels. Normally the window centers.  This location is relative to the location the window would be created. Note they can be negative.
    :type relative_location:                     (int, int)
    :param location:                             (x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen.
    :type location:                              (int, int)
    :param size:                                 (width, height) size in pixels for this window. Normally the window is autosized to fit contents, not set to an absolute size by the user. Try not to set this value. You risk, the contents being cut off, etc. Let the layout determine the window size instead
    :type size:                                  (int, int)
    :param element_padding:                      Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom)), or an int. If an int, then it's converted into a tuple (int, int)
    :type element_padding:                       (int, int) or ((int, int),(int,int)) or int
    :param margins:                              (left/right, top/bottom) Amount of pixels to leave inside the window's frame around the edges before your elements are shown.
    :type margins:                               (int, int)
    :param button_color:                         Default button colors for all buttons in the window
    :type button_color:                          (str, str) or str
    :param font:                                 specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:                                  (str or (str, int[, str]) or None)
    :param progress_bar_color:                   (bar color, background color) Sets the default colors for all progress bars in the window
    :type progress_bar_color:                    (str, str)
    :param background_color:                     color of background
    :type background_color:                      (str)
    :param border_depth:                         Default border depth (width) for all elements in the window
    :type border_depth:                          (int)
    :param auto_close:                           If True, the window will automatically close itself
    :type auto_close:                            (bool)
    :param auto_close_duration:                  Number of seconds to wait before closing the window
    :type auto_close_duration:                   (int)
    :param icon:                                 Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO. Most portable is to use a Base64 of a PNG file. This works universally across all OS's
    :type icon:                                  (str | bytes)
    :param force_toplevel:                       If True will cause this window to skip the normal use of a hidden master window
    :type force_toplevel:                        (bool)
    :param alpha_channel:                        Sets the opacity of the window. 0 = invisible 1 = completely visible. Values bewteen 0 & 1 will produce semi-transparent windows in SOME environments (The Raspberry Pi always has this value at 1 and cannot change.
    :type alpha_channel:                         (float)
    :param return_keyboard_events:               if True key presses on the keyboard will be returned as Events from Read calls
    :type return_keyboard_events:                (bool)
    :param use_default_focus:                    If True will use the default focus algorithm to set the focus to the "Correct" element
    :type use_default_focus:                     (bool)
    :param text_justification:                   Default text justification for all Text Elements in window
    :type text_justification:                    'left' | 'right' | 'center'
    :param no_titlebar:                          If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar
    :type no_titlebar:                           (bool)
    :param grab_anywhere:                        If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems
    :type grab_anywhere:                         (bool)
    :param grab_anywhere_using_control:          If True can use CONTROL key + left mouse mouse to click and drag to move the window. DEFAULT is TRUE. Unlike normal grab anywhere, it works on all elements.
    :type grab_anywhere_using_control:           (bool)
    :param keep_on_top:                          If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm
    :type keep_on_top:                           (bool)
    :param resizable:                            If True, allows the user to resize the window. Note the not all Elements will change size or location when resizing.
    :type resizable:                             (bool)
    :param disable_close:                        If True, the X button in the top right corner of the window will no work.  Use with caution and always give a way out toyour users
    :type disable_close:                         (bool)
    :param disable_minimize:                     if True the user won't be able to minimize window.  Good for taking over entire screen and staying that way.
    :type disable_minimize:                      (bool)
    :param right_click_menu:                     A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu:                      List[List[ List[str] | str ]]
    :param transparent_color:                    Any portion of the window that has this color will be completely transparent. You can even click through these spots to the window under this window.
    :type transparent_color:                     (str)
    :param debugger_enabled:                     If True then the internal debugger will be enabled
    :type debugger_enabled:                      (bool)
    :param right_click_menu_background_color:    Background color for right click menus
    :type right_click_menu_background_color:     (str)
    :param right_click_menu_text_color:          Text color for right click menus
    :type right_click_menu_text_color:           (str)
    :param right_click_menu_disabled_text_color: Text color for disabled right click menu items
    :type right_click_menu_disabled_text_color:  (str)
    :param right_click_menu_selected_colors:     Text AND background colors for a selected item. Can be a Tuple OR a color string. simplified-button-color-string "foreground on background". Can be a single color if want to set only the background. Normally a tuple, but can be a simplified-dual-color-string "foreground on background". Can be a single color if want to set only the background.
    :type right_click_menu_selected_colors:      (str, str) | str | Tuple
    :param right_click_menu_font:                Font for right click menus
    :type right_click_menu_font:                 (str or (str, int[, str]) or None)
    :param right_click_menu_tearoff:             If True then all right click menus can be torn off
    :type right_click_menu_tearoff:              bool
    :param finalize:                             If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code
    :type finalize:                              (bool)
    :param element_justification:                All elements in the Window itself will have this justification 'left', 'right', 'center' are valid values
    :type element_justification:                 (str)
    :param ttk_theme:                            Set the tkinter ttk "theme" of the window.  Default = DEFAULT_TTK_THEME.  Sets all ttk widgets to this theme as their default
    :type ttk_theme:                             (str)
    :param use_ttk_buttons:                      Affects all buttons in window. True = use ttk buttons. False = do not use ttk buttons.  None = use ttk buttons only if on a Mac
    :type use_ttk_buttons:                       (bool)
    :param modal:                                If True then this window will be the only window a user can interact with until it is closed
    :type modal:                                 (bool)
    :param enable_close_attempted_event:         If True then the window will not close when "X" clicked. Instead an event WINDOW_CLOSE_ATTEMPTED_EVENT if returned from window.read
    :type enable_close_attempted_event:          (bool)
    :param titlebar_background_color:            If custom titlebar indicated by use_custom_titlebar, then use this as background color
    :type titlebar_background_color:             (str | None)
    :param titlebar_text_color:                  If custom titlebar indicated by use_custom_titlebar, then use this as text color
    :type titlebar_text_color:                   (str | None)
    :param titlebar_font:                        If custom titlebar indicated by use_custom_titlebar, then use this as title font
    :type titlebar_font:                         (str or (str, int[, str]) or None)
    :param titlebar_icon:                        If custom titlebar indicated by use_custom_titlebar, then use this as the icon (file or base64 bytes)
    :type titlebar_icon:                         (bytes | str)
    :param use_custom_titlebar:                  If True, then a custom titlebar will be used instead of the normal titlebar
    :type use_custom_titlebar:                   bool
    :param scaling:                              Apply scaling to the elements in the window. Can be set on a global basis using set_options
    :type scaling:                               float
    :param sbar_trough_color:                    Scrollbar color of the trough
    :type sbar_trough_color:                     (str)
    :param sbar_background_color:                Scrollbar color of the background of the arrow buttons at the ends AND the color of the "thumb" (the thing you grab and slide). Switches to arrow color when mouse is over
    :type sbar_background_color:                 (str)
    :param sbar_arrow_color:                     Scrollbar color of the arrow at the ends of the scrollbar (it looks like a button). Switches to background color when mouse is over
    :type sbar_arrow_color:                      (str)
    :param sbar_width:                           Scrollbar width in pixels
    :type sbar_width:                            (int)
    :param sbar_arrow_width:                     Scrollbar width of the arrow on the scrollbar. It will potentially impact the overall width of the scrollbar
    :type sbar_arrow_width:                      (int)
    :param sbar_frame_color:                     Scrollbar Color of frame around scrollbar (available only on some ttk themes)
    :type sbar_frame_color:                      (str)
    :param sbar_relief:                          Scrollbar relief that will be used for the "thumb" of the scrollbar (the thing you grab that slides). Should be a constant that is defined at starting with "RELIEF_" - RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID
    :type sbar_relief:                           (str)
    :param metadata:                             User metadata that can be set to ANYTHING
    :type metadata:                              (Any)

add_row(self, *args)
    Adds a single row of elements to a window's self.Rows variables.
    Generally speaking this is NOT how users should be building Window layouts.
    Users, create a single layout (a list of lists) and pass as a parameter to Window object, or call Window.Layout(layout)
     
    :param *args: List[Elements]
    :type *args:

add_rows(self, rows)
    Loops through a list of lists of elements and adds each row, list, to the layout.
    This is NOT the best way to go about creating a window.  Sending the entire layout at one time and passing
    it as a parameter to the Window call is better.
     
    :param rows: A list of a list of elements
    :type rows:  List[List[Elements]]

bind(self, bind_string, key, propagate=True)
    Used to add tkinter events to a Window.
    The tkinter specific data is in the Window's member variable user_bind_event
    :param bind_string: The string tkinter expected in its bind function
    :type bind_string:  (str)
    :param key:         The event that will be generated when the tkinter event occurs
    :type key:          str | int | tuple | object
    :param propagate:   If True then tkinter will be told to propagate the event
    :type propagate:    (bool)

bring_to_front(self)
    Brings this window to the top of all other windows (perhaps may not be brought before a window made to "stay
    on top")

close(self)
    Closes window.  Users can safely call even if window has been destroyed.   Should always call when done with
    a window so that resources are properly freed up within your thread.

current_location(self, more_accurate=False)
    Get the current location of the window's top left corner.
    Sometimes, depending on the environment, the value returned does not include the titlebar,etc
    A new option, more_accurate, can be used to get the theoretical upper leftmost corner of the window.
    The titlebar and menubar are crated by the OS. It gets really confusing when running in a webpage (repl, trinket)
    Thus, the values can appear top be "off" due to the sometimes unpredictable way the location is calculated.
     
    :param more_accurate: If True, will use the window's geometry to get the topmost location with titlebar, menubar taken into account
    :type more_accurate:  (bool)
    :return:              The x and y location in tuple form (x,y)
    :rtype:               Tuple[(int | None), (int | None)]

current_size_accurate(self)
    Get the current location of the window based on tkinter's geometry setting
     
    :return:              The x and y size in tuple form (x,y)
    :rtype:               Tuple[(int | None), (int | None)]

ding(self, display_number=0)
    Make a "bell" sound. A capability provided by tkinter.  Your window needs to be finalized prior to calling.
    Ring a display's bell is the tkinter description of the call.
    :param display_number: Passed to tkinter's bell method as parameter "displayof".
    :type display_number:  int

disable(self)
    Disables window from taking any input from the user

disable_debugger(self)
    Disable the internal debugger. By default the debugger is ENABLED

disappear(self)
    Causes a window to "disappear" from the screen, but remain on the taskbar. It does this by turning the alpha
    channel to 0.  NOTE that on some platforms alpha is not supported. The window will remain showing on these
    platforms.  The Raspberry Pi for example does not have an alpha setting

element_list(self)
    Returns a list of all elements in the window
     
    :return: List of all elements in the window and container elements in the window
    :rtype:  List[Element]

enable(self)
    Re-enables window to take user input after having it be Disabled previously

enable_debugger(self)
    Enables the internal debugger. By default, the debugger IS enabled

extend_layout(self, container, rows)
    Adds new rows to an existing container element inside of this window
    If the container is a scrollable Column, you need to also call the contents_changed() method
     
    :param container: The container Element the layout will be placed inside of
    :type container:  Frame | Column | Tab
    :param rows:      The layout to be added
    :type rows:       (List[List[Element]])
    :return:          (Window) self so could be chained
    :rtype:           (Window)

fill(self, values_dict)
    Fill in elements that are input fields with data based on a 'values dictionary'
     
    :param values_dict: pairs
    :type values_dict:  (Dict[Any, Any]) - {Element_key : value}
    :return:            returns self so can be chained with other methods
    :rtype:             (Window)

finalize(self)
    Use this method to cause your layout to built into a real tkinter window.  In reality this method is like
    Read(timeout=0).  It doesn't block and uses your layout to create tkinter widgets to represent the elements.
    Lots of action!
     
    :return: Returns 'self' so that method "Chaining" can happen (read up about it as it's very cool!)
    :rtype:  (Window)

find_element(self, key, silent_on_error=False)
    Find element object associated with the provided key.
    THIS METHOD IS NO LONGER NEEDED to be called by the user
     
    You can perform the same operation by writing this statement:
    element = window[key]
     
    You can drop the entire "find_element" function name and use [ ] instead.
     
    However, if you wish to perform a lookup without error checking, and don't have error popups turned
    off globally, you'll need to make this call so that you can disable error checks on this call.
     
    find_element is yypically used in combination with a call to element's Update method (or any other element method!):
    window[key].update(new_value)
     
    Versus the "old way"
    window.FindElement(key).Update(new_value)
     
    This call can be abbreviated to any of these:
    find_element = FindElement == Element == Find
    With find_element being the PEP8 compliant call that should be used.
     
    Rememeber that this call will return None if no match is found which may cause your code to crash if not
    checked for.
     
    :param key:             Used with window.find_element and with return values to uniquely identify this element
    :type key:              str | int | tuple | object
    :param silent_on_error: If True do not display popup nor print warning of key errors
    :type silent_on_error:  (bool)
    :return:                Return value can be: the Element that matches the supplied key if found; an Error Element if silent_on_error is False; None if silent_on_error True;
    :rtype:                 Element | Error Element | None

find_element_with_focus(self)
    Returns the Element that currently has focus as reported by tkinter. If no element is found None is returned!
    :return: An Element if one has been found with focus or None if no element found
    :rtype:  Element | None

force_focus(self)
    Forces this window to take focus

get_screen_dimensions(self)
    Get the screen dimensions.  NOTE - you must have a window already open for this to work (blame tkinter not me)
     
    :return: Tuple containing width and height of screen in pixels
    :rtype:  Tuple[None, None] | Tuple[width, height]

grab_any_where_off(self)
    Turns off Grab Anywhere functionality AFTER a window has been created.  Don't try on a window that's not yet
    been Finalized or Read.

grab_any_where_on(self)
    Turns on Grab Anywhere functionality AFTER a window has been created.  Don't try on a window that's not yet
    been Finalized or Read.

hide(self)
    Hides the window from the screen and the task bar

is_closed(self)
    Returns True is the window is maybe closed.  Can be difficult to tell sometimes
     
    :return:    True if the window was closed or destroyed
    :rtype:     (bool)

keep_on_top_clear(self)
    Clears keep_on_top after a window has been created.  Effect is the same
    as if the window was created with this set.

keep_on_top_set(self)
    Sets keep_on_top after a window has been created.  Effect is the same
    as if the window was created with this set.  The Window is also brought
    to the front

layout(self, rows)
    Second of two preferred ways of telling a Window what its layout is. The other way is to pass the layout as
    a parameter to Window object.  The parameter method is the currently preferred method. This call to Layout
    has been removed from examples contained in documents and in the Demo Programs. Trying to remove this call
    from history and replace with sending as a parameter to Window.
     
    :param rows: Your entire layout
    :type rows:  List[List[Elements]]
    :return:     self so that you can chain method calls
    :rtype:      (Window)

load_from_disk(self, filename)
    Restore values from a previous call to SaveToDisk which saves the returned values dictionary in Pickle format
     
    :param filename: Pickle Filename to load
    :type filename:  (str)

make_modal(self)
    Makes a window into a "Modal Window"
    This means user will not be able to interact with other windows until this one is closed
     
    NOTE - Sorry Mac users - you can't have modal windows.... lobby your tkinter Mac devs

maximize(self)
    Maximize the window. This is done differently on a windows system versus a linux or mac one.  For non-Windows
    the root attribute '-fullscreen' is set to True.  For Windows the "root" state is changed to "zoomed"
    The reason for the difference is the title bar is removed in some cases when using fullscreen option

minimize(self)
    Minimize this window to the task bar

mouse_location(self)
    Return the (x,y) location of the mouse relative to the entire screen.  It's the same location that
    you would use to create a window, popup, etc.
     
    :return:    The location of the mouse pointer
    :rtype:     (int, int)

move(self, x, y)
    Move the upper left corner of this window to the x,y coordinates provided
    :param x: x coordinate in pixels
    :type x:  (int)
    :param y: y coordinate in pixels
    :type y:  (int)

move_to_center(self)
    Recenter your window after it's been moved or the size changed.
     
    This is a conveinence method. There are no tkinter calls involved, only pure PySimpleGUI API calls.

normal(self)
    Restore a window to a non-maximized state.  Does different things depending on platform.  See Maximize for more.

perform_long_operation(self, func, end_key)
    Call your function that will take a long time to execute.  When it's complete, send an event
    specified by the end_key.
     
    Starts a thread on your behalf.
     
    This is a way for you to "ease into" threading without learning the details of threading.
    Your function will run, and when it returns 2 things will happen:
    1. The value you provide for end_key will be returned to you when you call window.read()
    2. If your function returns a value, then the value returned will also be included in your windows.read call in the values dictionary
     
    IMPORTANT - This method uses THREADS... this means you CANNOT make any PySimpleGUI calls from
    the function you provide with the exception of one function, Window.write_event_value.
     
    :param func:    A lambda or a function name with no parms
    :type func:     Any
    :param end_key: The key that will be generated when the function returns
    :type end_key:  (Any)
    :return:        The id of the thread
    :rtype:         threading.Thread

read(self, timeout=None, timeout_key='__TIMEOUT__', close=False)
    THE biggest deal method in the Window class! This is how you get all of your data from your Window.
        Pass in a timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout_key
        if no other GUI events happen first.
     
    :param timeout:     Milliseconds to wait until the Read will return IF no other GUI events happen first
    :type timeout:      (int)
    :param timeout_key: The value that will be returned from the call if the timer expired
    :type timeout_key:  (Any)
    :param close:       if True the window will be closed prior to returning
    :type close:        (bool)
    :return:            (event, values)
    :rtype:             Tuple[(Any), Dict[Any, Any], List[Any], None]

reappear(self)
    Causes a window previously made to "Disappear" (using that method). Does this by restoring the alpha channel

refresh(self)
    Refreshes the window by calling tkroot.update().  Can sometimes get away with a refresh instead of a Read.
    Use this call when you want something to appear in your Window immediately (as soon as this function is called).
    If you change an element in a window, your change will not be visible until the next call to Window.read
    or a call to Window.refresh()
     
    :return: `self` so that method calls can be easily "chained"
    :rtype:  (Window)

save_to_disk(self, filename)
    Saves the values contained in each of the input areas of the form. Basically saves what would be returned from a call to Read.  It takes these results and saves them to disk using pickle.
     Note that every element in your layout that is to be saved must have a key assigned to it.
     
    :param filename: Filename to save the values to in pickled form
    :type filename:  str

save_window_screenshot_to_disk(self, filename=None)
    Saves an image of the PySimpleGUI window provided into the filename provided
     
    :param filename:        Optional filename to save screenshot to. If not included, the User Settinds are used to get the filename
    :return:                A PIL ImageGrab object that can be saved or manipulated
    :rtype:                 (PIL.ImageGrab | None)

send_to_back(self)
    Pushes this window to the bottom of the stack of windows. It is the opposite of BringToFront

set_alpha(self, alpha)
    Sets the Alpha Channel for a window.  Values are between 0 and 1 where 0 is completely transparent
     
    :param alpha: 0 to 1. 0 is completely transparent.  1 is completely visible and solid (can't see through)
    :type alpha:  (float)

set_cursor(self, cursor)
    Sets the cursor for the window.
    If you do not want any mouse pointer, then use the string "none"
     
    :param cursor: The tkinter cursor name
    :type cursor:  (str)

set_icon(self, icon=None, pngbase64=None)
    Changes the icon that is shown on the title bar and on the task bar.
    NOTE - The file type is IMPORTANT and depends on the OS!
    Can pass in:
    * filename which must be a .ICO icon file for windows, PNG file for Linux
    * bytes object
    * BASE64 encoded file held in a variable
     
    :param icon:      Filename or bytes object
    :type icon:       (str)
    :param pngbase64: Base64 encoded image
    :type pngbase64:  (bytes)

set_min_size(self, size)
    Changes the minimum size of the window. Note Window must be read or finalized first.
     
    :param size: (width, height) tuple (int, int) of the desired window size in pixels
    :type size:  (int, int)

set_title(self, title)
    Change the title of the window
     
    :param title: The string to set the title to
    :type title:  (str)

set_transparent_color(self, color)
    Set the color that will be transparent in your window. Areas with this color will be SEE THROUGH.
     
    :param color: Color string that defines the transparent color
    :type color:  (str)

start_thread = perform_long_operation(self, func, end_key)

un_hide(self)
    Used to bring back a window that was previously hidden using the Hide method

visibility_changed(self)
    When making an element in a column or someplace that has a scrollbar, then you'll want to call this function
    prior to the column's contents_changed() method.

was_closed(self)
    Returns True if the window was closed
     
    :return: True if the window is closed
    :rtype:  bool

widget_to_element(self, widget)
    Returns the element that matches a supplied tkinter widget.
    If no matching element is found, then None is returned.
     
     
    :return:    Element that uses the specified widget
    :rtype:     Element | None

write_event_value(self, key, value)
    Adds a key & value tuple to the queue that is used by threads to communicate with the window
     
    :param key:   The key that will be returned as the event when reading the window
    :type key:    Any
    :param value: The value that will be in the values dictionary
    :type value:  Any

Class methods defined here:

get_screen_size() from builtins.type
    This is a "Class Method" meaning you call it by writing: width, height = Window.get_screen_size()
    Returns the size of the "screen" as determined by tkinter.  This can vary depending on your operating system and the number of monitors installed on your system.  For Windows, the primary monitor's size is returns. On some multi-monitored Linux systems, the monitors are combined and the total size is reported as if one screen.
     
    :return: Size of the screen in pixels as determined by tkinter
    :rtype:  (int, int)
