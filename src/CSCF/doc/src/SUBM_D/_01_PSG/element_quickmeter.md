class QuickMeter(builtins.object)
      QuickMeter(title, current_value, max_value, key, *args, orientation='v', bar_color=(None, None), button_color=(None, None), size=(20, 20), border_width=None, grab_anywhere=False, no_titlebar=False, keep_on_top=None, no_button=False)
 

 
    Methods defined here:

BuildWindow(self, *args)

ComputeProgressStats(self)

UpdateMeter(self, current_value, max_value, *args)

__init__(self, title, current_value, max_value, key, *args, orientation='v', bar_color=(None, None), button_color=(None, None), size=(20, 20), border_width=None, grab_anywhere=False, no_titlebar=False, keep_on_top=None, no_button=False)
    :param title:         text to display in element
    :type title:          (str)
    :param current_value: current value
    :type current_value:  (int)
    :param max_value:     max value of QuickMeter
    :type max_value:      (int)
    :param key:           Used with window.find_element and with return values to uniquely identify this element
    :type key:            str | int | tuple | object
    :param *args:         stuff to output
    :type *args:          (Any)
    :param orientation:   'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical' / 'v')
    :type orientation:    (str)
    :param bar_color:     color of a bar line
    :type bar_color:      (str, str)
    :param button_color:  button color (foreground, background)
    :type button_color:   (str, str) or str
    :param size:          (w,h) w=characters-wide, h=rows-high (Default value = DEFAULT_PROGRESS_BAR_SIZE)
    :type size:           (int, int)
    :param border_width:  width of border around element
    :type border_width:   (int)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere:  (bool)
    :param no_titlebar:   If True: window will be created without a titlebar
    :type no_titlebar:    (bool)
    :param keep_on_top:   If True the window will remain above all current windows
    :type keep_on_top:    (bool)
    :param no_button:     If True: window will be created without a cancel button
    :type no_button:      (bool)
