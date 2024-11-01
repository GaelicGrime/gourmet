class SystemTray(builtins.object)
      SystemTray(menu=None, filename=None, data=None, data_base64=None, tooltip=None, metadata=None)
 
A "Simulated System Tray" that duplicates the API calls available to PySimpleGUIWx and PySimpleGUIQt users.
 
All of the functionality works. The icon is displayed ABOVE the system tray rather than inside of it.
 
    Methods defined here:

Close = close(self)

Hide = hide(self)

Read = read(self, timeout=None)

ShowMessage = show_message(self, title, message, filename=None, data=None, data_base64=None, messageicon=None, time=(1000, 3000))

UnHide = un_hide(self)

Update = update(self, menu=None, tooltip=None, filename=None, data=None, data_base64=None)

__init__(self, menu=None, filename=None, data=None, data_base64=None, tooltip=None, metadata=None)
    SystemTray - create an icon in the system tray
    :param menu:        Menu definition. Example - ['UNUSED', ['My', 'Simple', '---', 'Menu', 'Exit']]
    :type menu:         List[List[List[str] or str]]
    :param filename:    filename for icon
    :type filename:     (str)
    :param data:        in-ram image for icon (same as data_base64 parm)
    :type data:         (bytes)
    :param data_base64: base-64 data for icon
    :type data_base64:  (bytes)
    :param tooltip:     tooltip string
    :type tooltip:      (str)
    :param metadata:    User metadata that can be set to ANYTHING
    :type metadata:     (Any)

close(self)
    Close the system tray window

hide(self)
    Hides the icon

read(self, timeout=None)
    Reads the context menu
    :param timeout: Optional.  Any value other than None indicates a non-blocking read
    :type timeout:
    :return:
    :rtype:

show_message(self, title, message, filename=None, data=None, data_base64=None, messageicon=None, time=(1000, 3000))
    Shows a balloon above icon in system tray
    :param title:       Title shown in balloon
    :type title:        str
    :param message:     Message to be displayed
    :type message:      str
    :param filename:    Optional icon filename
    :type filename:     str
    :param data:        Optional in-ram icon
    :type data:         b''
    :param data_base64: Optional base64 icon
    :type data_base64:  b''
    :param time:        Amount of time to display message in milliseconds. If tuple, first item is fade in/out duration
    :type time:         int | (int, int)
    :return:            The event that happened during the display such as user clicked on message
    :rtype:             Any

un_hide(self)
    Restores a previously hidden icon

update(self, menu=None, tooltip=None, filename=None, data=None, data_base64=None)
    Updates the menu, tooltip or icon
    :param menu:        menu defintion
    :type menu:         ???
    :param tooltip:     string representing tooltip
    :type tooltip:      ???
    :param filename:    icon filename
    :type filename:     ???
    :param data:        icon raw image
    :type data:         ???
    :param data_base64: icon base 64 image
    :type data_base64:  ???
