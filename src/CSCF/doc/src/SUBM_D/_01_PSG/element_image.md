class Image(Element)
      Image(source=None, filename=None, data=None, background_color=None, size=(None, None), s=(None, None), pad=None, p=None, key=None, k=None, tooltip=None, subsample=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, enable_events=False, metadata=None)
 
Image Element - show an image in the window. Should be a GIF or a PNG only
 
    

Method resolution order:
    Image
    Element
    builtins.object

Methods defined here:

Update = update(self, source=None, filename=None, data=None, size=(None, None), subsample=None, visible=None)

UpdateAnimation = update_animation(self, source, time_between_frames=0)

__init__(self, source=None, filename=None, data=None, background_color=None, size=(None, None), s=(None, None), pad=None, p=None, key=None, k=None, tooltip=None, subsample=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, enable_events=False, metadata=None)
    :param source:           A filename or a base64 bytes. Will automatically detect the type and fill in filename or data for you.
    :type source:            str | bytes | None
    :param filename:         image filename if there is a button image. GIFs and PNGs only.
    :type filename:          str | None
    :param data:             Raw or Base64 representation of the image to put on button. Choose either filename or data
    :type data:              bytes | str | None
    :param background_color: color of background
    :type background_color:
    :param size:             (width, height) size of image in pixels
    :type size:              (int, int)
    :param s:                Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
    :type s:                 (int, int)  | (None, None) | int
    :param pad:              Amount of padding to put around element in pixels (left/right, top/bottom) or ((left, right), (top, bottom)) or an int. If an int, then it's converted into a tuple (int, int)
    :type pad:               (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param p:                Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                 (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param key:              Used with window.find_element and with return values to uniquely identify this element to uniquely identify this element
    :type key:               str | int | tuple | object
    :param k:                Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                 str | int | tuple | object
    :param tooltip:          text, that will appear when mouse hovers over the element
    :type tooltip:           (str)
    :param subsample:        amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
    :type subsample:         (int)
    :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu:  List[List[ List[str] | str ]]
    :param expand_x:         If True the element will automatically expand in the X direction to fill available space
    :type expand_x:          (bool)
    :param expand_y:         If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:          (bool)
    :param visible:          set visibility state of the element
    :type visible:           (bool)
    :param enable_events:    Turns on the element specific events. For an Image element, the event is "image clicked"
    :type enable_events:     (bool)
    :param metadata:         User metadata that can be set to ANYTHING
    :type metadata:          (Any)

update(self, source=None, filename=None, data=None, size=(None, None), subsample=None, visible=None)
    Changes some of the settings for the Image Element. Must call `Window.Read` or `Window.Finalize` prior.
    To clear an image that's been displayed, call with NONE of the options set.  A blank update call will
    delete the previously shown image.
     
    Changes will not be visible in your window until you call window.read or window.refresh.
     
    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.
     
    :param source:   A filename or a base64 bytes. Will automatically detect the type and fill in filename or data for you.
    :type source:    str | bytes | None
    :param filename: filename to the new image to display.
    :type filename:  (str)
    :param data:     Base64 encoded string OR a tk.PhotoImage object
    :type data:      str | tkPhotoImage
    :param size:     (width, height) size of image in pixels
    :type size:      Tuple[int,int]
    :param subsample:  amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
    :type subsample:   (int)
    :param visible:  control visibility of element
    :type visible:   (bool)

update_animation(self, source, time_between_frames=0)
    Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next frame and will automatically advance to the next frame at the right time.
    NOTE - does NOT perform a sleep call to delay
    :param source:              Filename or Base64 encoded string containing Animated GIF
    :type source:               str | bytes | None
    :param time_between_frames: Number of milliseconds to wait between showing frames
    :type time_between_frames:  (int)

update_animation_no_buffering(self, source, time_between_frames=0)
    Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next frame and will automatically advance to the next frame at the right time.
    NOTE - does NOT perform a sleep call to delay
     
    :param source:              Filename or Base64 encoded string containing Animated GIF
    :type source:               str | bytes
    :param time_between_frames: Number of milliseconds to wait between showing frames
    :type time_between_frames:  (int)
