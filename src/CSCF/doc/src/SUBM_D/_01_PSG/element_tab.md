class Tab(Element)
      Tab(title, layout, title_color=None, background_color=None, font=None, pad=None, p=None, disabled=False, border_width=None, key=None, k=None, tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, element_justification='left', image_source=None, image_subsample=None, metadata=None)
 
Tab Element is another "Container" element that holds a layout and displays a tab with text. Used with TabGroup only
Tabs are never placed directly into a layout.  They are always "Contained" in a TabGroup layout
 
    

Method resolution order:
    Tab
    Element
    builtins.object

Methods defined here:

AddRow = add_row(self, *args)

Layout = layout(self, rows)

Select = select(self)

Update = update(self, title=None, disabled=None, visible=None)

__init__(self, title, layout, title_color=None, background_color=None, font=None, pad=None, p=None, disabled=False, border_width=None, key=None, k=None, tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, element_justification='left', image_source=None, image_subsample=None, metadata=None)
    :param title:                 text to show on the tab
    :type title:                  (str)
    :param layout:                The element layout that will be shown in the tab
    :type layout:                 List[List[Element]]
    :param title_color:           color of the tab text (note not currently working on tkinter)
    :type title_color:            (str)
    :param background_color:      color of background of the entire layout
    :type background_color:       (str)
    :param font:                  NOT USED in the tkinter port
    :type font:                   (str or (str, int[, str]) or None)
    :param pad:                   Amount of padding to put around element in pixels (left/right, top/bottom) or ((left, right), (top, bottom)) or an int. If an int, then it's converted into a tuple (int, int)
    :type pad:                    (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param p:                     Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                      (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param disabled:              If True button will be created disabled
    :type disabled:               (bool)
    :param border_width:          NOT USED in tkinter port
    :type border_width:           (int)
    :param key:                   Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
    :type key:                    str | int | tuple | object
    :param k:                     Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                      str | int | tuple | object
    :param tooltip:               text, that will appear when mouse hovers over the element
    :type tooltip:                (str)
    :param right_click_menu:      A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu:       List[List[ List[str] | str ]]
    :param expand_x:              If True the element will automatically expand in the X direction to fill available space
    :type expand_x:               (bool)
    :param expand_y:              If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:               (bool)
    :param visible:               set visibility state of the element
    :type visible:                (bool)
    :param element_justification: All elements inside the Tab will have this justification 'left', 'right', 'center' are valid values
    :type element_justification:  (str)
    :param image_source:          A filename or a base64 bytes of an image to place on the Tab
    :type image_source:            str | bytes | None
    :param image_subsample:       amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
    :type image_subsample:        (int)
    :param metadata:              User metadata that can be set to ANYTHING
    :type metadata:               (Any)

add_row(self, *args)
    Not recommended use call.  Used to add rows of Elements to the Frame Element.
     
    :param *args: The list of elements for this row
    :type *args:  List[Element]

layout(self, rows)
    Not user callable.  Use layout parameter instead. Creates the layout using the supplied rows of Elements
     
    :param rows: List[List[Element]] The list of rows
    :type rows:  List[List[Element]]
    :return:     (Tab) used for chaining
    :rtype:

select(self)
    Create a tkinter event that mimics user clicking on a tab. Must have called window.Finalize / Read first!

update(self, title=None, disabled=None, visible=None)
    Changes some of the settings for the Tab Element. Must call `Window.Read` or `Window.Finalize` prior
     
    Changes will not be visible in your window until you call window.read or window.refresh.
     
    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.
     
    :param title:    tab title
    :type title:     (str)
    :param disabled: disable or enable state of the element
    :type disabled:  (bool)
    :param visible:  control visibility of element
    :type visible:   (bool)
