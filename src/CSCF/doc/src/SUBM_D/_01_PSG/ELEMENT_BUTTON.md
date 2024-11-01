


  - ButtonCallBack\(self\)
    - Not user callable! Called by tkinter when a button is clicked.  This is where all the fun begins!
  - ButtonPressCallBack\(self, parm\)
    - Not a user callable method. Callback called by tkinter when a "realtime" button is pressed
      - :param parm: Event info passed in by tkinter
      - :type parm:
  - ButtonReleaseCallBack\(self, parm\)
    - Not a user callable function.  Called by tkinter when a "realtime" button is released
      - :param parm: the event info from tkinter
      - :type parm:
  - Click = click\(self\)
  - GetText = get_text\(self\)
  - Update = update\(
    - self,
    - text=None,
    - button_color=\(None, None\),
    - disabled=None,
    - image_data=None,
    - image_filename=None,
    - visible=None,
    - image_subsample=None,
    - disabled_button_color=\(None, None\),
    - image_size=None\)
  - \_\_init\_\_\(
    - self, 
    - button_text='', 
    - button_type=7, 
    - target=\(None, None\), 
    - tooltip=None, 
    - file_types=\(\('ALL Files', '*.* *'\),\), 
    - initial_folder=None, 
    - default_extension='', 
    - disabled=False, 
    - change_submits=False, 
    - enable_events=False, 
    - image_filename=None, 
    - image_data=None, 
    - image_size=\(None, None\), 
    - image_subsample=None, 
    - border_width=None, 
    - size=\(None, None\), 
    - s=\(None, None\), 
    - auto_size_button=None, 
    - button_color=None, 
    - disabled_button_color=None, 
    - highlight_colors=None, 
    - mouseover_colors=\(None, None\), 
    - use_ttk_buttons=None, 
    - font=None, 
    - bind_return_key=False, 
    - focus=False, 
    - pad=None, 
    - p=None, 
    - key=None, 
    - k=None, 
    - right_click_menu=None, 
    - expand_x=False, 
    - expand_y=False, 
    - visible=True, 
    - metadata=None\)
      - :param button_text:           Text to be displayed on the button
      - :type button_text:            \(str\)
      - :param button_type:           You  should NOT be setting this directly. ONLY the shortcut functions set this
      - :type button_type:            \(int\)
      - :param target:                key or \(row,col\) target for the button. Note that -1 for column means 1 element to the left of this one. The constant ThisRow is used to indicate the current row. The Button itself is a valid target for some types of button
      - :type target:                 str | \(int, int\)
      - :param tooltip:               text, that will appear when mouse hovers over the element
      - :type tooltip:                \(str\)
      - :param file_types:            the filetypes that will be used to match files. To indicate all files: \(\("ALL Files", "*.* *"\),\).  Note - NOT SUPPORTED ON MAC
      - :type file_types:             Tuple\[\(str, str\), ...\]
      - :param initial_folder:        starting path for folders and files
      - :type initial_folder:         \(str\)
      - :param default_extension:     If no extension entered by user, add this to filename \(only used in saveas dialogs\)
      - :type default_extension:      \(str\)
      - :param disabled:              If True button will be created disabled. If BUTTON_DISABLED_MEANS_IGNORE then the button will be ignored rather than disabled using tkinter
      - :type disabled:               \(bool | str\)
      - :param change_submits:        DO NOT USE. Only listed for backwards compat - Use enable_events instead
      - :type change_submits:         \(bool\)
      - :param enable_events:         Turns on the element specific events. If this button is a target, should it generate an event when filled in
      - :type enable_events:          \(bool\)
      - :param image_filename:        image filename if there is a button image. GIFs and PNGs only.
      - :type image_filename:         \(str\)
      - :param image_data:            Raw or Base64 representation of the image to put on button. Choose either filename or data
      - :type image_data:             bytes | str
      - :param image_size:            Size of the image in pixels \(width, height\)
      - :type image_size:             \(int, int\)
      - :param image_subsample:       amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
      - :type image_subsample:        \(int\)
      - :param border_width:          width of border around button in pixels
      - :type border_width:           \(int\)
      - :param size:                  \(w, h\) w=characters-wide, h=rows-high. If an int instead of a tuple is supplied, then height is auto-set to 1
      - :type size:                   \(int | None, int | None\)  | \(None, None\) | int
      - :param s:                     Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
      - :type s:                      \(int | None, int | None\)  | \(None, None\) | int
      - :param auto_size_button:      if True the button size is sized to fit the text
      - :type auto_size_button:       \(bool\)
      - :param button_color:          Color of button. default is from theme or the window. Easy to remember which is which if you say "ON" between colors. "red" on "green". Normally a tuple, but can be a simplified-button-color-string "foreground on background". Can be a single color if want to set only the background.
      - :type button_color:           \(str, str\) | str | \(int, int\) | None
      - :param disabled_button_color: colors to use when button is disabled \(text, background\). Use None for a color if don't want to change. Only ttk buttons support both text and background colors. tk buttons only support changing text color
      - :type disabled_button_color:  \(str, str\) | str
      - :param highlight_colors:      colors to use when button has focus \(has focus, does not have focus\). None will use colors based on theme. Only used by Linux and only for non-TTK button
      - :type highlight_colors:       \(str, str\)
      - :param mouseover_colors:      Important difference between Linux & Windows! Linux - Colors when mouse moved over button.  Windows - colors when button is pressed. The default is to switch the text and background colors \(an inverse effect\)
      - :type mouseover_colors:       \(str, str\) | str
      - :param use_ttk_buttons:       True = use ttk buttons. False = do not use ttk buttons.  None \(Default\) = use ttk buttons only if on a Mac and not with button images
      - :type use_ttk_buttons:        \(bool\)
      - :param font:                  specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
      - :type font:                   \(str or \(str, int\[, str\]\) or None\)
      - :param bind_return_key:       If True the return key will cause this button to be pressed
      - :type bind_return_key:        \(bool\)
      - :param focus:                 if True, initial focus will be put on this button
      - :type focus:                  \(bool\)
      - :param pad:                   Amount of padding to put around element in pixels \(left/right, top/bottom\) or \(\(left, right\), \(top, bottom\)\) or an int. If an int, then it's converted into a tuple \(int, int\)
      - :type pad:                    \(int, int\) or \(\(int, int\),\(int,int\)\) or \(int,\(int,int\)\) or  \(\(int, int\),int\) | int
      - :param p:                     Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
      - :type p:                      \(int, int\) or \(\(int, int\),\(int,int\)\) or \(int,\(int,int\)\) or  \(\(int, int\),int\) | int
      - :param key:                   Used with window.find_element and with return values to uniquely identify this element to uniquely identify this element
      - :type key:                    str | int | tuple | object
      - :param k:                     Same as the Key. You can use either k or key. Which ever is set will be used.
      - :type k:                      str | int | tuple | object
      - :param right_click_menu:      A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
      - :type right_click_menu:       List\[List\[ List\[str\] | str \]\]
      - :param expand_x:              If True the element will automatically expand in the X direction to fill available space
      - :type expand_x:               \(bool\)
      - :param expand_y:              If True the element will automatically expand in the Y direction to fill available space
      - :type expand_y:               \(bool\)
      - :param visible:               set visibility state of the element
      - :type visible:                \(bool\)
      - :param metadata:              User metadata that can be set to ANYTHING
      - :type metadata:               \(Any\)
  - click\(self\)
    - Generates a click of the button as if the user clicked the button
    - Calls the tkinter invoke method for the button
  - get_text\(self\)
    - Returns the current text shown on a button
      - :return: The text currently displayed on the button
      - :rtype:  \(str\)
  - update\(
    - self, 
    - text=None, 
    - button_color=\(None, None\), 
    - disabled=None, 
    - image_data=None, 
    - image_filename=None, 
    - visible=None, 
    - image_subsample=None, 
    - disabled_button_color=\(None, None\), 
    - image_size=None\)
      - Changes some of the settings for the Button Element. Must call `Window.Read` or `Window.Finalize` prior
      - Changes will not be visible in your window until you call window.read or window.refresh.
        - If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper" function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there when made visible.
    - `:param text:                  sets button text
    - `:type text:                   \(str\)
    - `:param button_color:          Color of button. default is from theme or the window. Easy to remember which is which if you say "ON" between colors. "red" on "green". Normally a tuple, but can be a simplified-button-color-string "foreground on background". Can be a single color if want to set only the background.
    - `:type button_color:           \(str, str\) | str | \(int, int\) | None
    - `:param disabled:              True/False to enable/disable at the GUI level. Use BUTTON_DISABLED_MEANS_IGNORE to ignore clicks \(won't change colors\)
    - `:type disabled:               \(bool | str\)
    - `:param image_data:            Raw or Base64 representation of the image to put on button. Choose either filename or data
    - `:type image_data:             bytes | str
    - `:param image_filename:        image filename if there is a button image. GIFs and PNGs only.
    - `:type image_filename:         \(str\)
    - `:param disabled_button_color: colors to use when button is disabled \(text, background\). Use None for a color if don't want to change. Only ttk buttons support both text and background colors. tk buttons only support changing text color
    - `:type disabled_button_color:  \(str, str\)
    - `:param visible:               control visibility of element
    - `:type visible:                \(bool\)
    - `:param image_subsample:       amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
    - `:type image_subsample:        \(int\)
    - `:param image_size:            Size of the image in pixels \(width, height\)
    - `:type image_size:             \(int, int\)


Update = update(self, text=None, button_color=(None, None), disabled=None, image_data=None, image_filename=None, visible=None, image_subsample=None, disabled_button_color=(None, None), image_size=None)

__init__(self, button_text='', button_type=7, target=(None, None), tooltip=None, file_types=(('ALL Files', '*.* *'),), initial_folder=None, default_extension='', disabled=False, change_submits=False, enable_events=False, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None, image_source=None, border_width=None, size=(None, None), s=(None, None), auto_size_button=None, button_color=None, disabled_button_color=None, highlight_colors=None, mouseover_colors=(None, None), use_ttk_buttons=None, font=None, bind_return_key=False, focus=False, pad=None, p=None, key=None, k=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, metadata=None)
    :param button_text:           Text to be displayed on the button
    :type button_text:            (str)
    :param button_type:           You  should NOT be setting this directly. ONLY the shortcut functions set this
    :type button_type:            (int)
    :param target:                key or (row,col) target for the button. Note that -1 for column means 1 element to the left of this one. The constant ThisRow is used to indicate the current row. The Button itself is a valid target for some types of button
    :type target:                 str | (int, int)
    :param tooltip:               text, that will appear when mouse hovers over the element
    :type tooltip:                (str)
    :param file_types:            the filetypes that will be used to match files. To indicate all files: (("ALL Files", "*.* *"),). NOT avoilable on the MAC
    :type file_types:             Tuple[(str, str), ...]
    :param initial_folder:        starting path for folders and files
    :type initial_folder:         (str)
    :param default_extension:     If no extension entered by user, add this to filename (only used in saveas dialogs)
    :type default_extension:      (str)
    :param disabled:              If True button will be created disabled. If BUTTON_DISABLED_MEANS_IGNORE then the button will be ignored rather than disabled using tkinter
    :type disabled:               (bool | str)
    :param change_submits:        DO NOT USE. Only listed for backwards compat - Use enable_events instead
    :type change_submits:         (bool)
    :param enable_events:         Turns on the element specific events. If this button is a target, should it generate an event when filled in
    :type enable_events:          (bool)
    :param image_source:          Image to place on button. Use INSTEAD of the image_filename and image_data. Unifies these into 1 easier to use parm
    :type image_source:           (str | bytes)
    :param image_filename:        image filename if there is a button image. GIFs and PNGs only.
    :type image_filename:         (str)
    :param image_data:            Raw or Base64 representation of the image to put on button. Choose either filename or data
    :type image_data:             bytes | str
    :param image_size:            Size of the image in pixels (width, height)
    :type image_size:             (int, int)
    :param image_subsample:       amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
    :type image_subsample:        (int)
    :param border_width:          width of border around button in pixels
    :type border_width:           (int)
    :param size:                  (w, h) w=characters-wide, h=rows-high. If an int instead of a tuple is supplied, then height is auto-set to 1
    :type size:                   (int | None, int | None)  | (None, None) | int
    :param s:                     Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
    :type s:                      (int | None, int | None)  | (None, None) | int
    :param auto_size_button:      if True the button size is sized to fit the text
    :type auto_size_button:       (bool)
    :param button_color:          Color of button. default is from theme or the window. Easy to remember which is which if you say "ON" between colors. "red" on "green". Normally a tuple, but can be a simplified-button-color-string "foreground on background". Can be a single color if want to set only the background.
    :type button_color:           (str, str) | str | (int, int) | None
    :param disabled_button_color: colors to use when button is disabled (text, background). Use None for a color if don't want to change. Only ttk buttons support both text and background colors. tk buttons only support changing text color
    :type disabled_button_color:  (str, str) | str
    :param highlight_colors:      colors to use when button has focus (has focus, does not have focus). None will use colors based on theme. Only used by Linux and only for non-TTK button
    :type highlight_colors:       (str, str)
    :param mouseover_colors:      Important difference between Linux & Windows! Linux - Colors when mouse moved over button.  Windows - colors when button is pressed. The default is to switch the text and background colors (an inverse effect)
    :type mouseover_colors:       (str, str) | str
    :param use_ttk_buttons:       True = use ttk buttons. False = do not use ttk buttons.  None (Default) = use ttk buttons only if on a Mac and not with button images
    :type use_ttk_buttons:        (bool)
    :param font:                  specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:                   (str or (str, int[, str]) or None)
    :param bind_return_key:       If True the return key will cause this button to be pressed
    :type bind_return_key:        (bool)
    :param focus:                 if True, initial focus will be put on this button
    :type focus:                  (bool)
    :param pad:                   Amount of padding to put around element in pixels (left/right, top/bottom) or ((left, right), (top, bottom)) or an int. If an int, then it's converted into a tuple (int, int)
    :type pad:                    (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param p:                     Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                      (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param key:                   Used with window.find_element and with return values to uniquely identify this element to uniquely identify this element
    :type key:                    str | int | tuple | object
    :param k:                     Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                      str | int | tuple | object
    :param right_click_menu:      A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu:       List[List[ List[str] | str ]]
    :param expand_x:              If True the element will automatically expand in the X direction to fill available space
    :type expand_x:               (bool)
    :param expand_y:              If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:               (bool)
    :param visible:               set visibility state of the element
    :type visible:                (bool)
    :param metadata:              User metadata that can be set to ANYTHING
    :type metadata:               (Any)

click(self)
    Generates a click of the button as if the user clicked the button
    Calls the tkinter invoke method for the button

get_text(self)
    Returns the current text shown on a button
     
    :return: The text currently displayed on the button
    :rtype:  (str)

update(self, text=None, button_color=(None, None), disabled=None, image_data=None, image_filename=None, visible=None, image_subsample=None, disabled_button_color=(None, None), image_size=None)
    Changes some of the settings for the Button Element. Must call `Window.Read` or `Window.Finalize` prior
     
    Changes will not be visible in your window until you call window.read or window.refresh.
     
    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.
     
    :param text:                  sets button text
    :type text:                   (str)
    :param button_color:          Color of button. default is from theme or the window. Easy to remember which is which if you say "ON" between colors. "red" on "green". Normally a tuple, but can be a simplified-button-color-string "foreground on background". Can be a single color if want to set only the background.
    :type button_color:           (str, str) | str | (int, int) | None
    :param disabled:              True/False to enable/disable at the GUI level. Use BUTTON_DISABLED_MEANS_IGNORE to ignore clicks (won't change colors)
    :type disabled:               (bool | str)
    :param image_data:            Raw or Base64 representation of the image to put on button. Choose either filename or data
    :type image_data:             bytes | str
    :param image_filename:        image filename if there is a button image. GIFs and PNGs only.
    :type image_filename:         (str)
    :param disabled_button_color: colors to use when button is disabled (text, background). Use None for a color if don't want to change. Only ttk buttons support both text and background colors. tk buttons only support changing text color
    :type disabled_button_color:  (str, str)
    :param visible:               control visibility of element
    :type visible:                (bool)
    :param image_subsample:       amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
    :type image_subsample:        (int)
    :param image_size:            Size of the image in pixels (width, height)
    :type image_size:             (int, int)
