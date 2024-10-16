"""Stub file for mods development in Assetto Corsa"""
#NOTE: Anywhere Type Any is listed- Thats just because I havent figured out the return type yet.
#NOTE: I am making assumtions based on examples. THis may not be 100% Accurate to each functions use
#NOTE: I have only documented the functions I have found code examples for or enough conversation context on forms/etc to tell me what it does
from typing import Any, Callable

__all__ = ["getDriverName", "getCarState"] 

def testcall():
    print("test")

def getCarState(car_identifier, info_identifier, optional_identifier=None):
    """
    Gets the current state of the car
    
    :param car_id: intentifier: int
    :param info_identifier: Any appropriate type
    :param optional_identifier: Any: The optional identifier can be omitted, it is used for special infos where they
                                require a specific tyre, as described in the following section.
    :returns the info_identifier type of information associated to car car_id: intentifier.
    """
    pass

#---------------------------------------------------------
#------------ General Info -------------------------------
#---------------------------------------------------------

def getDriverName(car_id: int):
    """
    Retrieves the name of the driver associated with a specified car.

    Parameters:
        car_id: int - The unique identifier of the car whose driver name is being retrieved.

    Returns:
        str - The name of the driver on success, -1 otherwise
    """


def getTrackName(car_id: int) -> str:
    """
    Retrieves the name of the track associated with a specified car.

    Parameters:
        car_id: int - The unique identifier of the car whose track name is being retrieved.

    Returns:
        str - The name of the track on success, -1 otherwise
    """


def getTrackConfiguration(car_id: int) -> str:
    """
    Retrieves the configuration of the track associated with a specified car.

    Parameters:
        car_id: int - The unique identifier of the car whose track configuration is being retrieved.

    Returns:
        str - The configuration details of the track on success, -1 otherwise
    """


def getCarName(car_id: int) -> str:
    """
    Retrieves the name of the car associated with a specified car ID.

    Parameters:
        car_id: int - The unique identifier of the car whose name is being retrieved.

    Returns:
        str - The name of the car on success, -1 otherwise
    """



def getLastSplits(car_id: int) -> list:
    """
    Retrieves the last split times for a specified car.

    Parameters:
        car_id: int - The unique identifier of the car whose last split times are being retrieved.

    Returns:
        list - A list of split times (e.g., [int, ...]) representing the car's most recent split times on success. Rreturns -1 Otherwise
    """


def isCarInPitlane(car_id: int) -> int:
    """
    Checks if the specified car is currently in the pitlane.

    Parameters:
        car_id: int - The unique identifier of the car being checked.

    Returns:
        int - 1 if the car is in the pitlane, 0 otherwise.
    """


def isCarInPitline(car_id: int) -> int:
    """
    Checks if the specified car is currently in the pitline.

    Parameters:
        car_id: int - The unique identifier of the car being checked.

    Returns:
        int - 1 if the car is in the pitline, 0 otherwise.
    """


def isCarInPit(car_id: int) -> int:
    """
    Checks if the specified car is currently in the pit area (pitline or pitlane).

    Parameters:
        car_id: int - The unique identifier of the car being checked.

    Returns:
        int - 1 if the car is in the pit area, 0 otherwise.
    """


def isConnected(car_id: int) -> int:
    """
    Checks if the specified car is currently connected.

    Parameters:
        car_id: int - The unique identifier of the car being checked.

    Returns:
        int - 1 if the car is connected, 0 otherwise.
    """


def getCarBallast(car_id: int) -> int:
    """
    Retrieves the ballast weight of a specified car.

    Parameters:
        car_id: int - The unique identifier of the car whose ballast is being retrieved.

    Returns:
        int - The ballast weight of the car.
    """



def getCarMinHeight(car_id: int) -> int:
    """
    Retrieves the minimum height (ground clearance) of a specified car.

    Parameters:
        car_id: int - The unique identifier of the car whose minimum height is being retrieved.

    Returns:
        int - The minimum height (ground clearance) of the car.
    """


def getServerName() -> str:
    """
    Retrieves the name of the server.

    Returns:
        str - The name of the server.
    """


def getServerIP() -> str:
    """
    Retrieves the IP address of the server.

    Returns:
        str - The IP address of the server.
    """


def getServerHttpPort() -> int:
    """
    Retrieves the HTTP port number used by the server.

    Returns:
        int - The HTTP port number of the server.
    """


def getServerSlotsCount() -> int:
    """
    Retrieves the maximum number of slots available on the server.

    Returns:
        int - The number of slots on the server.
    """


def getCarsCount() -> int:
    """
    Retrieves the total number of cars currently on the server.

    Returns:
        int - The count of cars on the server.
    """



def getCarLeaderboardPosition(car_id: int) -> int:
    """
    Retrieves the current leaderboard position of a specified car.

    Parameters:
        car_id: int - The unique identifier of the car whose leaderboard position is being retrieved.

    Returns:
        int - The current position of the car on the leaderboard.
    """


def getCarRealTimeLeaderboardPosition(car_id: int) -> int:
    """
    Retrieves the real-time leaderboard position of a specified car.

    Parameters:
        car_id: int - The unique identifier of the car whose leaderboard position is being retrieved.

    Returns:
        int - The real-time position of the car on the leaderboard.
    """


def getCarFFB() -> int:
    """
    Retrieves the current force feedback (FFB) value of the car.

    Returns:
        int - The force feedback value of the car.
    """


def setCarFFB(value: int):
    """
    Sets the force feedback (FFB) value for the car.

    Parameters:
        value: int - The desired force feedback value to set.
    """

#---------------------------------------------------------
#------------ Camera Management --------------------------
#---------------------------------------------------------
def setCameraMode(info_identifier: int):
    #GOing to use get camera mode to get all the modes as inputs to update this
    """
    Sets the camera mode based on the specified information identifier.

    Parameters:
        info_identifier: int - The identifier representing the desired camera mode.
    """


def getCameraMode() -> int:
    """
    Retrieves the current camera mode.

    Returns:
        int - The identifier of the current camera mode.
    """


def isCameraOnBoard(car_id: int) -> int:
    """
    Checks if the camera is currently in an on-board mode for a specified car.

    Parameters:
        car_id: int - The unique identifier of the car being checked.

    Returns:
        int - 1 if the camera is on-board the car, 0 otherwise.
    """


def setCameraCar(camera_id: int, car_id: int) -> int:
    """
    Sets the camera to focus on a specific car using the F6 camera index.

    Parameters:
        camera_id: int - The F6 camera index to be used for viewing.
        car_id: int - The unique identifier of the car to focus on.

    Returns:
        int - 1 on success, -1 otherwise.
    """


def getCameraCarCount(car_id: int) -> int:
    """
    Retrieves the count of F6 cameras available for a specified car.

    Parameters:
        car_id: int - The unique identifier of the car.

    Returns:
        int - The number of cameras associated with the car, -1 otherwise.
    """


def focusCar(car_id: int) -> int:
    """
    Switches the actor's focus to the selected car.

    Parameters:
        car_id: int - The unique identifier of the car to focus on. Use 0 for the player’s car.

    Returns:
        int - 1 on success, -1 otherwise.
    """


def getFocusedCar() -> int:
    """
    Retrieves the unique identifier of the currently focused car.

    Returns:
        int - The car ID of the currently focused car.
    """
#---------------------------------------------------------
#------------ Debug --------------------------------------
#---------------------------------------------------------

def log(log_message: str):
    """
    Logs a message for debugging or informational purposes.

    Parameters:
        log_message: str - The message to be logged.
    """


def console(console_message: str) -> int:
    """
    Outputs a message to the console for debugging or informational purposes. Sends it to the log.txt file

    Parameters:
        console_message: str - The message to be output to the console. Returns 1 on success
    """

#---------------------------------------------------------
#------------ General App Management----------------------
#---------------------------------------------------------
def newApp(app_name: str) -> int:
    """
    Creates a new application with the specified name.

    Parameters:
        app_name: str - The name of the application to be created.

    Returns:
        int - The unique identifier of the newly created application, -1 otherwise
    """


def setTitle(control_identifier: int, title: str) -> int:
    """
    Sets the title of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element whose title is being set.
        title: str - The title text to set for the control element.

    Returns:
        int - 1 on success, -1 on failure.
    """


def setSize(control_identifier: int, width: int, height: int) -> int:
    """
    Sets the size of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        width: int - The width to set for the control element.
        height: int - The height to set for the control element.

    Returns:
        int - 1 on success, -1 on failure.
    """


def addLabel(control_identifier: int, message: str) -> int:
    """
    Adds a label with a specified message to a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        message: str - The message text for the label.

    Returns:
        int - 1 on success, -1 on failure.
    """


def setPosition(control_identifier: int, x: int, y: int) -> int:
    """
    Sets the position of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        x: int - The x-coordinate for the control's new position.
        y: int - The y-coordinate for the control's new position.

    Returns:
        int - 1 on success, -1 on failure.
    """


def setIconPosition(control_identifier: int, x: int, y: int) -> int:
    """
    Sets the position of an icon within a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        x: int - The x-coordinate for the icon's new position.
        y: int - The y-coordinate for the icon's new position.

    Returns:
        int - 1 on success, -1 on failure.
    """


def setTitlePosition(control_identifier: int, x: int, y: int) -> int:
    """
    Sets the position of the title within a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        x: int - The x-coordinate for the title's new position.
        y: int - The y-coordinate for the title's new position.

    Returns:
        int - 1 on success, -1 on failure.
    """


def getPosition(control_identifier: int):
    """
    Retrieves the current position of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.

    Returns:
        tuple - A tuple (x, y) representing the control's current position on success, 
                or -1 on failure.
    """



def setText(control_identifier: int, text: str):
    """
    Sets the text content of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element
        text: str - The text content to set for the control element.
    """


def getText(control_identifier: int) -> str:
    """
    Retrieves the current text content of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.

    Returns:
        str - The current text content of the control element.
    """



def setBackgroundOpacity(control_identifier: int, opacity_percentage: int) -> int:
    """
    Sets the background opacity of the control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        opacity_percentage: int - The desired background opacity as a percentage (0-100).

    Returns:
        int - 1 on success, -1 on failure.
    """



def drawBackground(control_identifier: int, value: int) -> int:
    """
    Draws or hides the background of a control element based on the specified value.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        value: int - A flag indicating whether to draw the background (1) or hide it (0).

    Returns:
        int - 1 on success, -1 on failure.
"""


def drawBorder(control_identifier: int, show_border: int) -> int:
    """
    Draws or hides a border around the specified control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        show_border: int - A flag to show or hide the border; use 1 to show the border (default) or 0 to hide it.

    Returns:
        int - 1 on success, -1 on failure.
    """


def setBackgroundTexture(control_identifier: int, path: str) -> int:
    """
    Sets the background texture of a control element using the specified file path.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        path: str - The file path to the texture image, starting from the Assetto Corsa root folder.

    Returns:
        int - 1 on success, -1 otherwise.
    
    Notes:
        Use this function to set a specified texture, stored in the path relative to the Assetto Corsa 
        root folder, as the background image for the control specified by <CONTROL_IDENTIFIER>.
    """



def setFontAlignment(control_identifier: int, alignment: str) -> int:
    """
    Sets the text alignment for the font of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        alignment: str - The alignment setting for the font (e.g., "left", "center", "right").

    Returns:
        int - 1 on success, -1 on failure.
    """

def setBackgroundColor(control_identifier: int, r: int, g: int, b: int) -> int:
    """
    Sets the background color of a control element using RGB values.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        r: int - The red component of the color (0-255).
        g: int - The green component of the color (0-255).
        b: int - The blue component of the color (0-255).

    Returns:
        int - 1 on success, -1 on failure.
    """


def setVisible(control_identifier: int, state: int) -> int:
    """
    Sets the visibility state of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        state: int - The visibility state to set for the control element (1 for visible, 0 for hidden).

    Returns:
        int - 1 on success, -1 on failure.
    """


def addOnAppActivatedListener(control_identifier: int, OnAppActivatedListener: Callable) -> int:
    """
    Adds a listener that triggers when an app is activated on the task bar.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        OnAppActivatedListener: Callable - The listener function to be called when the app is activated.

    Returns:
        int - 1 on success, -1 on failure.
    """


def addOnAppDismissedListener(control_identifier: int, OnAppDismissedListener: Callable) -> int:
    """
    Adds a listener that triggers when an app is dismissed on the task bar.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        OnAppDismissedListener: Callable - The listener function to be called when the app is dismissed.

    Returns:
        int - 1 on success, -1 on failure.
    """


def addRenderCallback(control_identifier: int, onRender: Callable) -> int:
    """
    Adds a render callback to a control element. The callback is invoked after finishing rendering 
    and receives a delta time parameter.

    Parameters:
        control_identifier: int - The unique identifier of the control element to which the render callback is added.
        onRender: Callable - The callback function to be called during rendering. This function should accept one 
                            parameter: deltaT (int), representing the time elapsed since the last render call.

    Returns:
        int - 1 on success, -1 on failure.
    """


def setFontColor(control_identifier: int, r: int, g: int, b: int, a: int) -> int:
    """
    Sets the font color of a control element using RGBA values.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        r: int - The red component of the color (0-255).
        g: int - The green component of the color (0-255).
        b: int - The blue component of the color (0-255).
        a: int - The alpha (transparency) component of the color (0-255).

    Returns:
        int - 1 on success, -1 on failure.
    """


def setFontSize(control_identifier: int, size: int) -> int:
    """
    Sets the font size of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        size: int - The font size to set for the control element.

    Returns:
        int - 1 on success, -1 on failure.
    """


def initFont(_: int, fontname: str, italic: int, bold: int) -> int:
    """
    Initializes a font with specified attributes and loads it into memory. This function should be called 
    during the application's initialization. The font must be located in the "content/fonts" folder.

    Parameters:
        _: int - Unused parameter placeholder, typically passed as 0.
        fontname: str - The base name of the font to be initialized (e.g., "Arial").
        italic: int - Indicates whether the font is italic; 0 for non-italic, 1 for italic 
                    (e.g., "Arial Italic").
        bold: int - Indicates whether the font is bold; 0 for non-bold, 1 for bold 
                    (e.g., "Arial Bold" or "Arial Italic Bold" if italic is also set).

    Returns:
        int - 1 on success, -1 on failure.

    Notes:
        - The `_` parameter is always passed as 0.
        - <FONTNAME> must be the actual font name, not the filename.
        - The <ITALIC> and <BOLD> parameters control the font instance loaded. For example, 
        if italic is set, "Arial Italic" will be loaded, and if both italic and bold are set, 
        "Arial Italic Bold" will be used.
    """


def setCustomFont(control_identifier: int, fontname: str, italic: int, bold: int) -> int:
    """
    Creates or replaces the font of a control element with the specified font attributes.
    This function should only be used after calling `initFont`. The font file must be located 
    in the "content/fonts" folder.

    Parameters:
        control_identifier: int - The unique identifier of the control element that will use the custom font.
        fontname: str - The base name of the font to be set (e.g., "Arial").
        italic: int - Indicates whether the font is italic; 0 for non-italic, 1 for italic 
                    (e.g., "Arial Italic").
        bold: int - Indicates whether the font is bold; 0 for non-bold, 1 for bold 
                    (e.g., "Arial Bold" or "Arial Italic Bold" if italic is also set).

    Returns:
        int - 1 on success, -1 on failure.

    Notes:
        - Ensure that `initFont` has been called before using this function.
        - <FONTNAME> should be the real font name, not the filename.
        - The <ITALIC> and <BOLD> parameters determine the font style. For example, 
        if italic is set, "Arial Italic" will be used, and if both italic and bold are set, 
        "Arial Italic Bold" will be applied.
    """

#---------------------------------------------------------
#------------ Specific Control Management ----------------
#---------------------------------------------------------

#---------------------------------------------------------
#------------ Buttons ------------------------------------
#---------------------------------------------------------
def addButton(control_identifier: int, button_text: str) -> int:
    """
    Adds a button to a control element with the specified text.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        button_text: str - The text to display on the button.

    Returns:
        int - 1 on success, -1 on failure.
    """


def addOnClickedListener(control_identifier: int, OnClickedListener: Callable) -> int:
    """
    Adds a click listener to a control element, triggering when the button is clicked.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        OnClickedListener: Callable - The listener function to be called when the button is clicked.

    Returns:
        int - 1 on success, -1 on failure.
    """

#---------------------------------------------------------
#------------ Graphs -------------------------------------
#---------------------------------------------------------

def addGraph(control_identifier: int, value: int) -> int:
    """
    Adds a graph to a control element, initializing it with the specified value.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        value: int - The initial value to be displayed on the graph.

    Returns:
        int - 1 on success, -1 on failure.
    """


def addSerieToGraph(control_identifier: int, r: int, g: int, b: int) -> int:
    """
    Adds a new series to a graph within a control element, with a specified color using RGB values.

    Parameters:
        control_identifier: int - The unique identifier of the control element containing the graph.
        r: int - The red component of the color (0-255).
        g: int - The green component of the color (0-255).
        b: int - The blue component of the color (0-255).

    Returns:
        int - The index of the newly added series, or -1 on failure.
    """


def addValueToGraph(control_identifier: int, serie_index: int, value: int) -> int:
    """
    Adds a value to a specific series in a graph within a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element containing the graph.
        serie_index: int - The index of the series to which the value will be added.
        value: int - The value to add to the graph series.

    Returns:
        int - 1 on success, -1 on failure.
    """


def setRange(control_identifier: int, min_value: int, max_value: int, max_points: int = 0) -> int:
    """
    Sets the range of values for a control element, with an optional maximum number of points.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        min_value: int - The minimum value of the range.
        max_value: int - The maximum value of the range.
        max_points: int, optional - The maximum number of points within the range (default is 0, which implies no limit).

    Returns:
        int - 1 on success, -1 on failure.
    """

#---------------------------------------------------------
#------------ Spinners -----------------------------------
#---------------------------------------------------------

def addSpinner(control_identifier: int, text: str) -> int:
    """
    Adds a spinner (loading indicator) to a control element with the specified text.

    Parameters:
        control_identifier: int - The unique identifier of the control element to which the spinner is added.
        text: str - The text to display alongside the spinner. (The exact usage of this parameter may vary.)

    Returns:
        int - 1 on success, -1 on failure.
    """


def setValue(control_identifier: int, current_page_number: int) -> int:
    """
    Sets the current value or page number for a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        current_page_number: int - The value or page number to set for the control element.

    Returns:
        int - 1 on success, -1 on failure.
    """


def getValue(control_identifier: int) -> int:
    """
    Retrieves the current value associated with a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.

    Returns:
        int - The current value of the control element.
    """


def setStep(control_identifier: int, step_value: float) -> int:
    """
    Sets the step value for a Spinner control element, defining the increment or decrement step when the + or - button is pressed.

    Parameters:
        control_identifier: int - The unique identifier of the Spinner control element.
        step_value: float - The step increment or decrement value as a floating-point number.

    Returns:
        int - 1 on success, -1 on failure.
    
    Notes:
        - <CONTROL_IDENTIFIER> must correspond to a Spinner ID.
        - <VALUE> defines the amount added or subtracted when the Spinner's increment or decrement buttons are pressed.
    """


def addOnValueChangeListener(control_identifier: int, OnValueChangeListener: Callable) -> int:
    """
    Adds a listener that triggers when the value of a Spinner control element changes, such as when the increment 
    or decrement button is pressed.

    Parameters:
        control_identifier: int - The unique identifier of the control element to which the value change listener is added.
        OnValueChangeListener: Callable - The listener function to be called when the value changes. 
                                        This should be a function defined within the Python script.

    Returns:
        int - 1 on success, -1 on failure.

    Notes:
        - <CONTROL_IDENTIFIER> should correspond to a Spinner ID.
        - The listener function specified by <VALUE> is triggered when the Spinner's increment or decrement buttons are pressed.
    """

#---------------------------------------------------------
#------------ Progress Bar -------------------------------
#---------------------------------------------------------

def addProgressBar(control_identifier: int, value: str) -> int:
    """
    Adds a Progress Bar to a control element with the specified label or value.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        value: str - The label or value to display with the Progress Bar.

    Returns:
        int - The Progress Bar ID on success, -1 on failure.

    Notes:
        - The <VALUE> parameter should be a string that represents the label or value associated with the Progress Bar.
    """

#---------------------------------------------------------
#------------ Input Text----------------------------------
#---------------------------------------------------------

def addTextInput(control_identifier: int, input_name: str) -> int:
    """
    Adds a text input field to a specified control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element to which the text input will be added.
        input_name: str - The name or label for the text input field.

    Returns:
        int - The Text Input ID on success, -1 on failure.
    """



def setFocus(control_identifier: int, focus: int) -> int:
    """
    Sets the focus state of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element for which the focus state is being set.
        focus: int - The focus state to set for the control element (1 for focused, 0 for unfocused).

    Returns:
        int - 1 on success, -1 on failure.
    """


def addOnValidateListener(control_identifier: int, OnValidateListener: Callable) -> int:
    """
    Adds a validation listener to a control element. The listener is called when validation is required, 
    passing a data string to the listener function.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        OnValidateListener: Callable - The listener function to be called for validation. This function should accept 
                                    a single parameter: data of type str.

    Returns:
        int - 1 on success, -1 on failure.
    """


#---------------------------------------------------------
#------------ List Box------------------------------------
#---------------------------------------------------------
def addListBox(control_identifier: int, name: str) -> int:
    """
    Adds a List Box to the specified window.

    Parameters:
        control_identifier: int - The unique identifier of the window where the List Box will be added.
        name: str - The name of the List Box.

    Returns:
        int - The List Box ID on success, -1 on failure.
    """


def addItem(control_identifier: int, name: str) -> int:
    """
    Adds an item to a List Box.

    Parameters:
        control_identifier: int - The unique identifier of the List Box.
        name: str - The label for the List Box item.

    Returns:
        int - The List Box Item ID on success, -1 on failure.
    """


def removeItem(control_identifier: int, identifier: int) -> int:
    """
    Removes an item from a List Box by its identifier.

    Parameters:
        control_identifier: int - The unique identifier of the List Box.
        identifier: int - The ID of the item to be removed.

    Returns:
        int - The size of the List Box after removal on success, -1 on failure.
    """


def getItemCount(control_identifier: int) -> int:
    """
    Retrieves the number of items in a List Box.

    Parameters:
        control_identifier: int - The unique identifier of the List Box.

    Returns:
        int - The number of items in the List Box on success, -1 on failure.
    """


def setItemNumberPerPage(control_identifier: int, number: int) -> int:
    """
    Sets the number of items displayed per page in a List Box.

    Parameters:
        control_identifier: int - The unique identifier of the List Box.
        number: int - The desired number of items to display per page.

    Returns:
        int - 1 on success, -1 on failure.
    """


def highlightListBoxItem(control_identifier: int, identifier: int) -> int:
    """
    Highlights (selects) a specific item in a List Box.

    Parameters:
        control_identifier: int - The unique identifier of the List Box.
        identifier: int - The ID of the item to be highlighted.

    Returns:
        int - 1 on success, -1 on failure.
    """


def addOnListBoxSelectionListener(control_identifier: int, value: Callable) -> int:
    """
    Adds a selection listener to a List Box, triggering on item selection.

    Parameters:
        control_identifier: int - The unique identifier of the List Box.
        value: Callable - The callback function to be called on item selection. It should accept 
                        the item's name and ID as parameters.

    Returns:
        int - 1 on success, -1 on failure.
    """


def addOnListBoxDeselectionListener(control_identifier: int, value: Callable) -> int:
    """
    Adds a deselection listener to a List Box, triggering on item deselection.

    Parameters:
        control_identifier: int - The unique identifier of the List Box.
        value: Callable - The callback function to be called on item deselection. It should accept 
                        the item's name and ID as parameters.

    Returns:
        int - 1 on success, -1 on failure.
    """


def setAllowDeselection(control_identifier: int, allow_deselection: int) -> int:
    """
    Sets whether items in a List Box can be deselected.

    Parameters:
        control_identifier: int - The unique identifier of the List Box.
        allow_deselection: int - Set to 1 to allow deselection of items, 0 to disable.

    Returns:
        int - 1 on success, -1 on failure.
    """


def setAllowMultiSelection(control_identifier: int, allow_multi_selection: int) -> int:
    """
    Sets whether multiple items in a List Box can be selected.

    Parameters:
        control_identifier: int - The unique identifier of the List Box.
        allow_multi_selection: int - Set to 1 to allow multi-selection, 0 to disable.

    Returns:
        int - 1 on success, -1 on failure.
    """


def getSelectedItems(control_identifier: int) -> list:
    """
    Retrieves the list of selected items in a List Box.

    Parameters:
        control_identifier: int - The unique identifier of the List Box.

    Returns:
        list - A list of selected item IDs on success, -1 on failure.
    """
#---------------------------------------------------------
#------------ Check Box ----------------------------------
#---------------------------------------------------------

def addCheckBox(control_identifier: int, text_label: str) -> int:
    """
    Adds a checkbox to a form control element with the specified label text.

    Parameters:
        control_identifier: int - The unique identifier of the form control element to which the checkbox is added.
        text_label: str - The name or label of the checkbox.

    Returns:
        int - The identifier of the created checkbox on success, -1 on failure.
    """


def addOnCheckBoxChanged(control_identifier: int, OnCheckBoxChanged: Callable) -> int:
    """
    Adds a listener that triggers when the state of a checkbox control element changes, indicating selection or deselection.

    Parameters:
        control_identifier: int - The unique identifier of the checkbox control element.
        OnCheckBoxChanged: Callable - The callback function to be called on checkbox state change. It should accept
                                    the checkbox's name and its state (1 for selected, -1 otherwise).

    Returns:
        int - 1 on success, -1 on failure.
    
    Notes:
        - <CONTROL_IDENTIFIER> must correspond to a checkbox element.
        - <VALUE> should be a function defined within the Python script to handle checkbox state changes.
    """
#---------------------------------------------------------
#------------ Text Box -----------------------------------
#---------------------------------------------------------

def addTextBox(control_identifier: int, name: str) -> int:
    """
    Adds a text box to a form control element. The text box is scrollable if the content exceeds its display area.

    Parameters:
        control_identifier: int - The unique identifier of the form control element to which the text box is added.
        name: str - The name or label of the text box.

    Returns:
        int - The identifier of the created text box on success, -1 on failure.

    Notes:
        - This control is currently non-functional, so no methods for setting or modifying text are available.
    """


#---------------------------------------------------------
#------------ Graphics and Rendering----------------------
#---------------------------------------------------------
def newTexture(path: str) -> int:
    """
    Creates a new texture from the specified file path.

    Parameters:
        path: str - The file path to the texture image, starting from the Assetto Corsa installation directory.

    Returns:
        int - The texture identifier on success, -1 on failure.
    """


def glBegin(primitive_identifier: int) -> int:
    """
    Begins rendering of a specified primitive type.

    Parameters:
        primitive_identifier: int - The identifier for the primitive type:
            0 : Lines
            1 : Line Strip
            2 : Triangles
            3 : Quads

    Returns:
        int - 1 on success, -1 on failure.
    """


def glEnd() -> int:
    """
    Ends the rendering sequence for the current primitive.

    Returns:
        int - 1 on success.
    """


def glVertex2f(x: float, y: float) -> int:
    """
    Specifies a vertex in 2D space for rendering in OpenGL.

    Parameters:
        x: float - The x-coordinate of the vertex.
        y: float - The y-coordinate of the vertex.

    Returns:
        int - 1 on success, -1 on failure.
    """


def glColor3f(r: float, g: float, b: float) -> int:
    """
    Sets the current rendering color using RGB values scaled from 0 to 1.

    Parameters:
        r: float - The red component of the color (0.0 - 1.0).
        g: float - The green component of the color (0.0 - 1.0).
        b: float - The blue component of the color (0.0 - 1.0).

    Returns:
        int - 1 on success, -1 on failure.
    """


def glColor4f(r: float, g: float, b: float, a: float) -> int:
    """
    Sets the current rendering color using RGBA values scaled from 0 to 1.

    Parameters:
        r: float - The red component of the color (0.0 - 1.0).
        g: float - The green component of the color (0.0 - 1.0).
        b: float - The blue component of the color (0.0 - 1.0).
        a: float - The alpha component for transparency (0.0 - 1.0).

    Returns:
        int - 1 on success, -1 on failure.
    """


def glQuad(x: float, y: float, width: float, height: float) -> int:
    """
    Draws a quadrilateral (quad) at the specified position with the given dimensions.

    Parameters:
        x: float - The x-coordinate of the bottom-left corner of the quad.
        y: float - The y-coordinate of the bottom-left corner of the quad.
        width: float - The width of the quad.
        height: float - The height of the quad.

    Returns:
        int - 1 on success, -1 on failure.
    """


def glQuadTextured(x: float, y: float, width: float, height: float, texture_id: int) -> int:
    """
    Draws a textured quadrilateral (quad) at the specified position with the given dimensions.

    Parameters:
        x: float - The x-coordinate of the bottom-left corner of the quad.
        y: float - The y-coordinate of the bottom-left corner of the quad.
        width: float - The width of the quad.
        height: float - The height of the quad.
        texture_id: int - The identifier of the previously loaded texture.

    Returns:
        int - 1 on success, -1 on failure.
    """



def isAcLive(): ...


def restart(): ...


def getCarSkin(car_id: int): ...


def getDriverNationCode(car_id: int): ...


def getCurrentSplits(car_id: int): ...


def getTrackLength(car_id: int): ...


def getWindSpeed(): ...


def getWindDirection(): ...


def isAIControlled(): ...


def getCarEngineBrakeCount(): ...


def getCarPowerControllerCount(): ...


def freeCameraSetClearColor(r: int, g: int, b: int, alpha): ...


def freeCameraMoveForward(value: int): ...


def freeCameraMoveRight(value: int): ...


def freeCameraMoveUpWorld(value: int): ...


def freeCameraRotatePitch(value: int): ...


def freeCameraRotateHeading(value: int): ...


def freeCameraRotateRoll(value: int): ...


def sendChatMessage(string_msg: str):
    """
    Sends a chat message with the specified content.

    Parameters:
        string_msg: str - The content of the chat message to be sent.
    """


def addOnChatMessageListener(control_identifier: int, onChatMessage: Callable):
    """
    Adds a chat message listener to a control element. The listener is called when a chat message is received, 
    passing the message content and author to the listener function.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        onChatMessage: Callable - The listener function to be called when a chat message is received. This function should 
                            accept two parameters: message (str) and author (str).
    """


def getCarRestrictor(car_id: int): ...


def getCarTyreCompound(car_id: int): ...


def getSize(control_identifier: int): ...


def setFont(): ...


def shutdown(): ...
