class Slider(Element)
      Slider(range=(None, None), default_value=None, resolution=None, tick_interval=None, orientation=None, disable_number_display=False, border_width=None, relief=None, change_submits=False, enable_events=False, disabled=False, size=(None, None), s=(None, None), font=None, background_color=None, text_color=None, trough_color=None, key=None, k=None, pad=None, p=None, expand_x=False, expand_y=False, tooltip=None, visible=True, metadata=None)
 
A slider, horizontal or vertical
 
    

Method resolution order:
    Slider
    Element
    builtins.object

Methods defined here:

Update = update(self, value=None, range=(None, None), disabled=None, visible=None)

__init__(self, range=(None, None), default_value=None, resolution=None, tick_interval=None, orientation=None, disable_number_display=False, border_width=None, relief=None, change_submits=False, enable_events=False, disabled=False, size=(None, None), s=(None, None), font=None, background_color=None, text_color=None, trough_color=None, key=None, k=None, pad=None, p=None, expand_x=False, expand_y=False, tooltip=None, visible=True, metadata=None)
    :param range:                  slider's range (min value, max value)
    :type range:                   (int, int) | Tuple[float, float]
    :param default_value:          starting value for the slider
    :type default_value:           int | float
    :param resolution:             the smallest amount the slider can be moved
    :type resolution:              int | float
    :param tick_interval:          how often a visible tick should be shown next to slider
    :type tick_interval:           int | float
    :param orientation:            'horizontal' or 'vertical' ('h' or 'v' also work)
    :type orientation:             (str)
    :param disable_number_display: if True no number will be displayed by the Slider Element
    :type disable_number_display:  (bool)
    :param border_width:           width of border around element in pixels
    :type border_width:            (int)
    :param relief:                 relief style. Use constants - RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID
    :type relief:                  str | None
    :param change_submits:         * DEPRICATED DO NOT USE. Use `enable_events` instead
    :type change_submits:          (bool)
    :param enable_events:          If True then moving the slider will generate an Event
    :type enable_events:           (bool)
    :param disabled:               set disable state for element
    :type disabled:                (bool)
    :param size:                   (l=length chars/rows, w=width pixels)
    :type size:                    (int, int)
    :param s:                      Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
    :type s:                       (int, int)  | (None, None)
    :param font:                   specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:                    (str or (str, int[, str]) or None)
    :param background_color:       color of slider's background
    :type background_color:        (str)
    :param text_color:             color of the slider's text
    :type text_color:              (str)
    :param trough_color:           color of the slider's trough
    :type trough_color:            (str)
    :param key:                    Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
    :type key:                     str | int | tuple | object
    :param k:                      Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                       str | int | tuple | object
    :param pad:                    Amount of padding to put around element in pixels (left/right, top/bottom) or ((left, right), (top, bottom)) or an int. If an int, then it's converted into a tuple (int, int)
    :type pad:                     (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param p:                      Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                       (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param expand_x:               If True the element will automatically expand in the X direction to fill available space
    :type expand_x:                (bool)
    :param expand_y:               If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:                (bool)
    :param tooltip:                text, that will appear when mouse hovers over the element
    :type tooltip:                 (str)
    :param visible:                set visibility state of the element
    :type visible:                 (bool)
    :param metadata:               User metadata that can be set to ANYTHING
    :type metadata:                (Any)

update(self, value=None, range=(None, None), disabled=None, visible=None)
    Changes some of the settings for the Slider Element. Must call `Window.Read` or `Window.Finalize` prior
     
    Changes will not be visible in your window until you call window.read or window.refresh.
     
    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.
     
    :param value:    sets current slider value
    :type value:     int | float
    :param range:    Sets a new range for slider
    :type range:     (int, int) | Tuple[float, float
    :param disabled: disable or enable state of the element
    :type disabled:  (bool)
    :param visible:  control visibility of element
    :type visible:   (bool)
