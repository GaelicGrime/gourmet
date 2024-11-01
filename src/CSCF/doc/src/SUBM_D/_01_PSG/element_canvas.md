class Canvas(Element)
      Canvas(canvas=None, background_color=None, size=(None, None), s=(None, None), pad=None, p=None, key=None, k=None, tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, border_width=0, metadata=None)
 
# ---------------------------------------------------------------------- #
#                           Canvas                                       #
# ---------------------------------------------------------------------- #
 
    

Method resolution order:
    Canvas
    Element
    builtins.object

Methods defined here:

__init__(self, canvas=None, background_color=None, size=(None, None), s=(None, None), pad=None, p=None, key=None, k=None, tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, border_width=0, metadata=None)
    :param canvas:           Your own tk.Canvas if you already created it. Leave blank to create a Canvas
    :type canvas:            (tk.Canvas)
    :param background_color: color of background
    :type background_color:  (str)
    :param size:             (width in char, height in rows) size in pixels to make canvas
    :type size:              (int,int) | (None, None)
    :param s:                Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
    :type s:                 (int, int)  | (None, None) | int
    :param pad:              Amount of padding to put around element in pixels (left/right, top/bottom) or ((left, right), (top, bottom)) or an int. If an int, then it's converted into a tuple (int, int)
    :type pad:               (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param p:                Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                 (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param key:              Used with window.find_element and with return values to uniquely identify this element
    :type key:               str | int | tuple | object
    :param k:                Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                 str | int | tuple | object
    :param tooltip:          text, that will appear when mouse hovers over the element
    :type tooltip:           (str)
    :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu:  List[List[ List[str] | str ]]
    :param expand_x:         If True the element will automatically expand in the X direction to fill available space
    :type expand_x:          (bool)
    :param expand_y:         If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:          (bool)
    :param visible:          set visibility state of the element
    :type visible:           (bool)
    :param border_width:     width of border around element in pixels. Not normally used with Canvas element
    :type border_width:      (int)
    :param metadata:         User metadata that can be set to ANYTHING
    :type metadata:          (Any)

update(self, background_color=None, visible=None)
    :param background_color: color of background
    :type background_color:  (str)
    :param visible:          set visibility state of the element
    :type visible:           (bool)
