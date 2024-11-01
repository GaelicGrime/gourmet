class Graph(Element)
      Graph(canvas_size, graph_bottom_left, graph_top_right, background_color=None, pad=None, p=None, change_submits=False, drag_submits=False, enable_events=False, motion_events=False, key=None, k=None, tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, float_values=False, border_width=0, metadata=None)
 
Creates an area for you to draw on.  The MAGICAL property this Element has is that you interact
with the element using your own coordinate system.  This is an important point!!  YOU define where the location
is for (0,0).  Want (0,0) to be in the middle of the graph like a math 4-quadrant graph?  No problem!  Set your
lower left corner to be (-100,-100) and your upper right to be (100,100) and you've got yourself a graph with
(0,0) at the center.
One of THE coolest of the Elements.
You can also use float values. To do so, be sure and set the float_values parameter.
Mouse click and drag events are possible and return the (x,y) coordinates of the mouse
Drawing primitives return an "id" that is referenced when you want to operation on that item (e.g. to erase it)
 
    

Method resolution order:
    Graph
    Element
    builtins.object

Methods defined here:

BringFigureToFront = bring_figure_to_front(self, figure)

ButtonPressCallBack = button_press_call_back(self, event)

ButtonReleaseCallBack = button_release_call_back(self, event)

DeleteFigure = delete_figure(self, id)

DrawArc = draw_arc(self, top_left, bottom_right, extent, start_angle, style=None, arc_color='black', line_width=1, fill_color=None)

DrawCircle = draw_circle(self, center_location, radius, fill_color=None, line_color='black', line_width=1)

DrawImage = draw_image(self, filename=None, data=None, location=(None, None))

DrawLine = draw_line(self, point_from, point_to, color='black', width=1)

DrawLines = draw_lines(self, points, color='black', width=1)

DrawOval = draw_oval(self, top_left, bottom_right, fill_color=None, line_color=None, line_width=1)

DrawPoint = draw_point(self, point, size=2, color='black')

DrawPolygon = draw_polygon(self, points, fill_color=None, line_color=None, line_width=None)

DrawRectangle = draw_rectangle(self, top_left, bottom_right, fill_color=None, line_color=None, line_width=None)

DrawText = draw_text(self, text, location, color='black', font=None, angle=0, text_location='center')

Erase = erase(self)

GetBoundingBox = get_bounding_box(self, figure)

GetFiguresAtLocation = get_figures_at_location(self, location)

MotionCallBack = motion_call_back(self, event)

Move = move(self, x_direction, y_direction)

MoveFigure = move_figure(self, figure, x_direction, y_direction)

RelocateFigure = relocate_figure(self, figure, x, y)

SendFigureToBack = send_figure_to_back(self, figure)

Update = update(self, background_color=None, visible=None)

__init__(self, canvas_size, graph_bottom_left, graph_top_right, background_color=None, pad=None, p=None, change_submits=False, drag_submits=False, enable_events=False, motion_events=False, key=None, k=None, tooltip=None, right_click_menu=None, expand_x=False, expand_y=False, visible=True, float_values=False, border_width=0, metadata=None)
    :param canvas_size:       size of the canvas area in pixels
    :type canvas_size:        (int, int)
    :param graph_bottom_left: (x,y) The bottoms left corner of your coordinate system
    :type graph_bottom_left:  (int, int)
    :param graph_top_right:   (x,y) The top right corner of  your coordinate system
    :type graph_top_right:    (int, int)
    :param background_color:  background color of the drawing area
    :type background_color:   (str)
    :param pad:               Amount of padding to put around element in pixels (left/right, top/bottom) or ((left, right), (top, bottom)) or an int. If an int, then it's converted into a tuple (int, int)
    :type pad:                (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param p:                 Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
    :type p:                  (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int) | int
    :param change_submits:    * DEPRICATED DO NOT USE. Use `enable_events` instead
    :type change_submits:     (bool)
    :param drag_submits:      if True and Events are enabled for the Graph, will report Events any time the mouse moves while button down.  When the mouse button is released, you'll get an event = graph key + '+UP' (if key is a string.. if not a string, it'll be made into a tuple)
    :type drag_submits:       (bool)
    :param enable_events:     If True then clicks on the Graph are immediately reported as an event. Use this instead of change_submits
    :type enable_events:      (bool)
    :param motion_events:     If True then if no button is down and the mouse is moved, an event is generated with key = graph key + '+MOVE' (if key is a string, it not a string then a tuple is returned)
    :type motion_events:      (bool)
    :param key:               Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
    :type key:                str | int | tuple | object
    :param k:                 Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k:                  str | int | tuple | object
    :param tooltip:           text, that will appear when mouse hovers over the element
    :type tooltip:            (str)
    :param right_click_menu:  A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu:   List[List[ List[str] | str ]]
    :param expand_x:          If True the element will automatically expand in the X direction to fill available space
    :type expand_x:           (bool)
    :param expand_y:          If True the element will automatically expand in the Y direction to fill available space
    :type expand_y:           (bool)
    :param visible:           set visibility state of the element (Default = True)
    :type visible:            (bool)
    :param float_values:      If True x,y coordinates are returned as floats, not ints
    :type float_values:       (bool)
    :param border_width:      width of border around element in pixels. Not normally used for Graph Elements
    :type border_width:       (int)
    :param metadata:          User metadata that can be set to ANYTHING
    :type metadata:           (Any)

bring_figure_to_front(self, figure)
    Changes Z-order of figures on the Graph.  Brings the indicated figure to the front of all other drawn figures
     
    :param figure: value returned by tkinter when creating the figure / drawing
    :type figure:  (int)

button_press_call_back(self, event)
    Not a user callable method.  Used to get Graph click events. Called by tkinter when button is released
     
    :param event: (event) event info from tkinter. Contains the x and y coordinates of a click
    :type event:

button_release_call_back(self, event)
    Not a user callable method.  Used to get Graph click events. Called by tkinter when button is released
     
    :param event: (event) event info from tkinter. Note not used in this method
    :type event:

change_coordinates(self, graph_bottom_left, graph_top_right)
    Changes the corrdinate system to a new one.  The same 2 points in space are used to define the coorinate
    system - the bottom left and the top right values of your graph.
     
    :param graph_bottom_left: The bottoms left corner of your coordinate system
    :type graph_bottom_left:  (int, int) (x,y)
    :param graph_top_right:   The top right corner of  your coordinate system
    :type graph_top_right:    (int, int)  (x,y)

delete_figure(self, id)
    Remove from the Graph the figure represented by id. The id is given to you anytime you call a drawing primitive
     
    :param id: the id returned to you when calling one of the drawing methods
    :type id:  (int)

draw_arc(self, top_left, bottom_right, extent, start_angle, style=None, arc_color='black', line_width=1, fill_color=None)
    Draws different types of arcs.  Uses a "bounding box" to define location
    :param top_left:     the top left point of bounding rectangle
    :type top_left:      (int, int) | Tuple[float, float]
    :param bottom_right: the bottom right point of bounding rectangle
    :type bottom_right:  (int, int) | Tuple[float, float]
    :param extent:       Andle to end drawing. Used in conjunction with start_angle
    :type extent:        (float)
    :param start_angle:  Angle to begin drawing. Used in conjunction with extent
    :type start_angle:   (float)
    :param style:        Valid choices are One of these Style strings- 'pieslice', 'chord', 'arc', 'first', 'last', 'butt', 'projecting', 'round', 'bevel', 'miter'
    :type style:         (str)
    :param arc_color:    color to draw arc with
    :type arc_color:     (str)
    :param fill_color:   color to fill the area
    :type fill_color:    (str)
    :return:             id returned from tkinter that you'll need if you want to manipulate the arc
    :rtype:              int | None

draw_circle(self, center_location, radius, fill_color=None, line_color='black', line_width=1)
    Draws a circle, cenetered at the location provided.  Can set the fill and outline colors
    :param center_location: Center location using USER'S coordinate system
    :type center_location:  (int, int) | Tuple[float, float]
    :param radius:          Radius in user's coordinate values.
    :type radius:           int | float
    :param fill_color:      color of the point to draw
    :type fill_color:       (str)
    :param line_color:      color of the outer line that goes around the circle (sorry, can't set thickness)
    :type line_color:       (str)
    :param line_width:      width of the line around the circle, the outline, in pixels
    :type line_width:       (int)
    :return:                id returned from tkinter that you'll need if you want to manipulate the circle
    :rtype:                 int | None

draw_image(self, filename=None, data=None, location=(None, None))
    Places an image onto your canvas.  It's a really important method for this element as it enables so much
     
    :param filename: if image is in a file, path and filename for the image. (GIF and PNG only!)
    :type filename:  (str)
    :param data:     if image is in Base64 format or raw? format then use instead of filename
    :type data:      str | bytes
    :param location: the (x,y) location to place image's top left corner
    :type location:  (int, int) | Tuple[float, float]
    :return:         id returned from tkinter that you'll need if you want to manipulate the image
    :rtype:          int | None

draw_line(self, point_from, point_to, color='black', width=1)
    Draws a line from one point to another point using USER'S coordinates. Can set the color and width of line
    :param point_from: Starting point for line
    :type point_from:  (int, int) | Tuple[float, float]
    :param point_to:   Ending point for line
    :type point_to:    (int, int) | Tuple[float, float]
    :param color:      Color of the line
    :type color:       (str)
    :param width:      width of line in pixels
    :type width:       (int)
    :return:           id returned from tktiner or None if user closed the window. id is used when you
    :rtype:            int | None

draw_lines(self, points, color='black', width=1)
    Draw a series of lines given list of points
     
    :param points: list of points that define the polygon
    :type points:  List[(int, int) | Tuple[float, float]]
    :param color:  Color of the line
    :type color:   (str)
    :param width:  width of line in pixels
    :type width:   (int)
    :return:       id returned from tktiner or None if user closed the window. id is used when you
    :rtype:        int | None

draw_oval(self, top_left, bottom_right, fill_color=None, line_color=None, line_width=1)
    Draws an oval based on coordinates in user coordinate system. Provide the location of a "bounding rectangle"
    :param top_left:     the top left point of bounding rectangle
    :type top_left:      (int, int) | Tuple[float, float]
    :param bottom_right: the bottom right point of bounding rectangle
    :type bottom_right:  (int, int) | Tuple[float, float]
    :param fill_color:   color of the interrior
    :type fill_color:    (str)
    :param line_color:   color of outline of oval
    :type line_color:    (str)
    :param line_width:   width of the line around the oval, the outline, in pixels
    :type line_width:    (int)
    :return:             id returned from tkinter that you'll need if you want to manipulate the oval
    :rtype:              int | None

draw_point(self, point, size=2, color='black')
    Draws a "dot" at the point you specify using the USER'S coordinate system
    :param point: Center location using USER'S coordinate system
    :type point:  (int, int) | Tuple[float, float]
    :param size:  Radius? (Or is it the diameter?) in user's coordinate values.
    :type size:   int | float
    :param color: color of the point to draw
    :type color:  (str)
    :return:      id returned from tkinter that you'll need if you want to manipulate the point
    :rtype:       int | None

draw_polygon(self, points, fill_color=None, line_color=None, line_width=None)
    Draw a polygon given list of points
     
    :param points:     list of points that define the polygon
    :type points:      List[(int, int) | Tuple[float, float]]
    :param fill_color: color of the interior
    :type fill_color:  (str)
    :param line_color: color of outline
    :type line_color:  (str)
    :param line_width: width of the line in pixels
    :type line_width:  (int)
    :return:           id returned from tkinter that you'll need if you want to manipulate the rectangle
    :rtype:            int | None

draw_rectangle(self, top_left, bottom_right, fill_color=None, line_color=None, line_width=None)
    Draw a rectangle given 2 points. Can control the line and fill colors
     
    :param top_left:     the top left point of rectangle
    :type top_left:      (int, int) | Tuple[float, float]
    :param bottom_right: the bottom right point of rectangle
    :type bottom_right:  (int, int) | Tuple[float, float]
    :param fill_color:   color of the interior
    :type fill_color:    (str)
    :param line_color:   color of outline
    :type line_color:    (str)
    :param line_width:   width of the line in pixels
    :type line_width:    (int)
    :return:             int | None id returned from tkinter that you'll need if you want to manipulate the rectangle
    :rtype:              int | None

draw_text(self, text, location, color='black', font=None, angle=0, text_location='center')
    Draw some text on your graph.  This is how you label graph number lines for example
     
    :param text:          text to display
    :type text:           (Any)
    :param location:      location to place first letter
    :type location:       (int, int) | Tuple[float, float]
    :param color:         text color
    :type color:          (str)
    :param font:          specifies the  font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike
    :type font:           (str or (str, int[, str]) or None)
    :param angle:         Angle 0 to 360 to draw the text.  Zero represents horizontal text
    :type angle:          (float)
    :param text_location: "anchor" location for the text. Values start with TEXT_LOCATION_
    :type text_location:  (enum)
    :return:              id returned from tkinter that you'll need if you want to manipulate the text
    :rtype:               int | None

erase(self)
    Erase the Graph - Removes all figures previously "drawn" using the Graph methods (e.g. DrawText)

get_bounding_box(self, figure)
    Given a figure, returns the upper left and lower right bounding box coordinates
     
    :param figure: a previously drawing figure
    :type figure:  object
    :return:       upper left x, upper left y, lower right x, lower right y
    :rtype:        Tuple[int, int, int, int] | Tuple[float, float, float, float]

get_figures_at_location(self, location)
    Returns a list of figures located at a particular x,y location within the Graph
     
    :param location: point to check
    :type location:  (int, int) | Tuple[float, float]
    :return:         a list of previously drawn "Figures" (returned from the drawing primitives)
    :rtype:          List[int]

motion_call_back(self, event)
    Not a user callable method.  Used to get Graph mouse motion events. Called by tkinter when mouse moved
     
    :param event: (event) event info from tkinter. Contains the x and y coordinates of a mouse
    :type event:

move(self, x_direction, y_direction)
    Moves the entire drawing area (the canvas) by some delta from the current position.  Units are indicated in your coordinate system indicated number of ticks in your coordinate system
     
    :param x_direction: how far to move in the "X" direction in your coordinates
    :type x_direction:  int | float
    :param y_direction: how far to move in the "Y" direction in your coordinates
    :type y_direction:  int | float

move_figure(self, figure, x_direction, y_direction)
    Moves a previously drawn figure using a "delta" from current position
     
    :param figure:      Previously obtained figure-id. These are returned from all Draw methods
    :type figure:       (id)
    :param x_direction: delta to apply to position in the X direction
    :type x_direction:  int | float
    :param y_direction: delta to apply to position in the Y direction
    :type y_direction:  int | float

relocate_figure(self, figure, x, y)
    Move a previously made figure to an arbitrary (x,y) location. This differs from the Move methods because it
    uses absolute coordinates versus relative for Move
     
    :param figure: Previously obtained figure-id. These are returned from all Draw methods
    :type figure:  (id)
    :param x:      location on X axis (in user coords) to move the upper left corner of the figure
    :type x:       int | float
    :param y:      location on Y axis (in user coords) to move the upper left corner of the figure
    :type y:       int | float

send_figure_to_back(self, figure)
    Changes Z-order of figures on the Graph.  Sends the indicated figure to the back of all other drawn figures
     
    :param figure: value returned by tkinter when creating the figure / drawing
    :type figure:  (int)

update(self, background_color=None, visible=None)
    Changes some of the settings for the Graph Element. Must call `Window.Read` or `Window.Finalize` prior
     
    Changes will not be visible in your window until you call window.read or window.refresh.
     
    If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper"
    function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there
    when made visible.
     
    :param background_color: color of background
    :type background_color:  ???
    :param visible:          control visibility of element
    :type visible:           (bool)
