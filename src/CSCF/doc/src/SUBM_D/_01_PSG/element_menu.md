class Menu(Element)
      Menu(menu_definition, background_color=None, text_color=None, disabled_text_color=None, size=(None, None), s=(None, None), tearoff=False, font=None, pad=None, p=None, key=None, k=None, visible=True, metadata=None)
 
Menu Element is the Element that provides a Menu Bar that goes across the top of the window, just below titlebar.
Here is an example layout.  The "&" are shortcut keys ALT+key.
Is a List of -  "Item String" + List
Where Item String is what will be displayed on the Menubar itself.
The List that follows the item represents the items that are shown then Menu item is clicked
Notice how an "entry" in a mennu can be a list which means it branches out and shows another menu, etc. (resursive)
menu_def = [['&File', ['!&Open', '&Save::savekey', '---', '&Properties', 'E&xit']],
            ['!&Edit', ['!&Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Debugger', ['Popout', 'Launch Debugger']],
            ['&Toolbar', ['Command &1', 'Command &2', 'Command &3', 'Command &4']],
            ['&Help', '&About...'], ]
Finally, "keys" can be added to entries so make them unique.  The "Save" entry has a key associated with it. You
can see it has a "::" which signifies the beginning of a key.  The user will not see the key portion when the
menu is shown.  The key portion is returned as part of the event.
 
    

Method resolution order:
    Menu
    Element
    builtins.object

Methods defined here:

Update = update(self, menu_definition=None, visible=None)

__init__(self, menu_definition, background_color=None, text_color=None, disabled_text_color=None, size=(None, None), s=(None, None), tearoff=False, font=None, pad=None, p=None, key=None, k=None, visible=True, metadata=None)
    :param menu_definition:     The Menu definition specified using lists (docs explain the format)
    :type menu_definition:      List[List[Tuple[str, List[str]]]
    :param background_color:    color of the background
    :type background_color:     (str)
    :param text_color:          element's text color. Can be in #RRGGBB format or a color name "black"
    :type text_color:           (str)
    :param disabled_text_color: color to use for text when item is disabled. Can be in #RRGGBB format or a color name "black"
    :type disabled_text_color:  (str)
    :param size:                Not used in the tkinter port
    :type size:                 (int, int)
    :param s:                   Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
    :type s:                    (int, int)  | (None, None)
    :param tearoff:             if True, then can tear the menu off from the window ans use as a floating window. Very cool effect
    :type tearoff:              (bool)
    :param pad:                 Amount of padding to put around element in pixels (left/right, top/bottom) or ((left, right), (top, bottom)) or an int. If an int, then it's converted into a tuple (int, int)
    :type pad:                  (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param p:                   Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                    (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param font:                specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:                 (str or (str, int[, str]) or None)
    :param key:                 Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
    :type key:                  str | int | tuple | object
    :param k:                   Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                    str | int | tuple | object
    :param visible:             set visibility state of the element
    :type visible:              (bool)
    :param metadata:            User metadata that can be set to ANYTHING
    :type metadata:             (Any)

update(self, menu_definition=None, visible=None)
    Update a menubar - can change the menu definition and visibility.  The entire menu has to be specified
     
    Changes will not be visible in your window until you call window.read or window.refresh.
     
    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.
     
    :param menu_definition: The menu definition list
    :type menu_definition:  List[List[Tuple[str, List[str]]]
    :param visible:         control visibility of element
    :type visible:          (bool)
