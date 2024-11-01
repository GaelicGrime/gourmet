
 
BM = class ButtonMenu(Element)
      BM(button_text, menu_def, tooltip=None, disabled=False, image_source=None, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None, border_width=None, size=(None, None), s=(None, None), auto_size_button=None, button_color=None, text_color=None, background_color=None, disabled_text_color=None, font=None, item_font=None, pad=None, p=None, expand_x=False, expand_y=False, key=None, k=None, tearoff=False, visible=True, metadata=None)
 
The Button Menu Element.  Creates a button that when clicked will show a menu similar to right click menu
 
    

Method resolution order:
    ButtonMenu
    Element
    builtins.object

Methods defined here:

Click = click(self)

Update = update(self, menu_definition=None, visible=None, image_source=None, image_size=(None, None), image_subsample=None, button_text=None)

__init__(self, button_text, menu_def, tooltip=None, disabled=False, image_source=None, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None, border_width=None, size=(None, None), s=(None, None), auto_size_button=None, button_color=None, text_color=None, background_color=None, disabled_text_color=None, font=None, item_font=None, pad=None, p=None, expand_x=False, expand_y=False, key=None, k=None, tearoff=False, visible=True, metadata=None)
    :param button_text:         Text to be displayed on the button
    :type button_text:          (str)
    :param menu_def:            A list of lists of Menu items to show when this element is clicked. See docs for format as they are the same for all menu types
    :type menu_def:             List[List[str]]
    :param tooltip:             text, that will appear when mouse hovers over the element
    :type tooltip:              (str)
    :param disabled:            If True button will be created disabled
    :type disabled:             (bool)
    :param image_source:        Image to place on button. Use INSTEAD of the image_filename and image_data. Unifies these into 1 easier to use parm
    :type image_source:         (str | bytes)
    :param image_filename:      image filename if there is a button image. GIFs and PNGs only.
    :type image_filename:       (str)
    :param image_data:          Raw or Base64 representation of the image to put on button. Choose either filename or data
    :type image_data:           bytes | str
    :param image_size:          Size of the image in pixels (width, height)
    :type image_size:           (int, int)
    :param image_subsample:     amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
    :type image_subsample:      (int)
    :param border_width:        width of border around button in pixels
    :type border_width:         (int)
    :param size:                (w, h) w=characters-wide, h=rows-high. If an int instead of a tuple is supplied, then height is auto-set to 1
    :type size:                 (int, int)  | (None, None) | int
    :param s:                   Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
    :type s:                    (int, int)  | (None, None) | int
    :param auto_size_button:    if True the button size is sized to fit the text
    :type auto_size_button:     (bool)
    :param button_color:        of button. Easy to remember which is which if you say "ON" between colors. "red" on "green"
    :type button_color:         (str, str) or str
    :param background_color:    color of the background
    :type background_color:     (str)
    :param text_color:          element's text color. Can be in #RRGGBB format or a color name "black"
    :type text_color:           (str)
    :param disabled_text_color: color to use for text when item is disabled. Can be in #RRGGBB format or a color name "black"
    :type disabled_text_color:  (str)
    :param font:                specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:                 (str or (str, int[, str]) or None)
    :param item_font:           specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike, for the menu items
    :type item_font:            (str or (str, int[, str]) or None)
    :param pad:                 Amount of padding to put around element in pixels (left/right, top/bottom) or ((left, right), (top, bottom)) or an int. If an int, then it's converted into a tuple (int, int)
    :type pad:                  (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param p:                   Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                    (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param expand_x:            If True the element will automatically expand in the X direction to fill available space
    :type expand_x:             (bool)
    :param expand_y:            If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:             (bool)
    :param key:                 Used with window.find_element and with return values to uniquely identify this element to uniquely identify this element
    :type key:                  str | int | tuple | object
    :param k:                   Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                    str | int | tuple | object
    :param tearoff:             Determines if menus should allow them to be torn off
    :type tearoff:              (bool)
    :param visible:             set visibility state of the element
    :type visible:              (bool)
    :param metadata:            User metadata that can be set to ANYTHING
    :type metadata:             (Any)

click(self)
    Generates a click of the button as if the user clicked the button
    Calls the tkinter invoke method for the button

update(self, menu_definition=None, visible=None, image_source=None, image_size=(None, None), image_subsample=None, button_text=None)
    Changes some of the settings for the ButtonMenu Element. Must call `Window.Read` or `Window.Finalize` prior
     
    Changes will not be visible in your window until you call window.read or window.refresh.
     
    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.
     
    :param menu_definition: (New menu definition (in menu definition format)
    :type menu_definition:  List[List]
    :param visible:         control visibility of element
    :type visible:          (bool)
    :param image_source:    new image if image is to be changed. Can be a filename or a base64 encoded byte-string
    :type image_source:     (str | bytes)
    :param image_size:      Size of the image in pixels (width, height)
    :type image_size:       (int, int)
    :param image_subsample: amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
    :type image_subsample:  (int)
    :param button_text:     Text to be shown on the button
    :type button_text:      (str)
