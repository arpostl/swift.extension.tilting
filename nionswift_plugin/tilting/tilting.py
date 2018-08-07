# standard libraries
import gettext
import logging
import threading
import time
import numpy as np

# third party libraries
# None

# local libraries
# None

_ = gettext.gettext

class TiltingDelegate:
     
    def __init__(self, api):
        self.__api = api
        self.panel_id = "tilting-panel"
        self.panel_name = _("Tilting")
        self.panel_positions = ["left", "right"]
        self.panel_position = "right"

    def create_panel_widget(self, ui, document_controller):
        calc_row = ui.create_row_widget()
        calc_label = ui.create_label_widget(_("n.a."))
        calc_button = ui.create_push_button_widget(_("Calculate tilt"))
        def calc_button_clicked():
            dc = self.__api.application.document_controllers[0]
            grphcs = dc.target_display.selected_graphics
            # Go to else-block if nothing or a graphic of another type has been selected 
            if (not not grphcs) and ("ellipse" in grphcs[0].graphic_type):
                sz = np.array(grphcs[0].size)
                if sz[0] > sz[1]:
                    a = sz[0]
                    b = sz[1]
                else:
                    a = sz[1]
                    b = sz[0]
                # Calculating tilt of the projection of a circle
                phi = np.arccos(b/a)
                phi_deg = phi / np.pi * 180  
                # Output
                calc_label.text = '{:.2f} ° ~ '.format(phi_deg) + '{:.1f} mrad'.format(phi*1000)
                logging.info(_("Tilting calculated from ellipse graphic aspect ratio: ")
                            + calc_label.text)
            else:
                calc_label.text = _("No ellipse graphic selected")
                logging.info(_("Tilting not calculated. Selection is no ellipse graphic."))
        calc_button.on_clicked = calc_button_clicked
        calc_row.add(calc_button)
        calc_row.add_spacing(5)
        calc_row.add(calc_label)
        calc_row.add_stretch()
        
        column = ui.create_column_widget()
        column.add(calc_row)
        column.add_spacing(8)
        column.add_stretch()

        return column


class TiltingExtension(object):
    
    # required for Swift to recognize this as an extension class.
    extension_id = "nion.swift.extension.tilting"
    
    def __init__(self, api_broker):
        # grab the api object.
        api = api_broker.get_api(version='~1.0', ui_version='~1.0')
        # be sure to keep a reference or it will be closed immediately.
        self.__panel_ref = api.create_panel(TiltingDelegate(api))
  
    def close(self):
        # close will be called when the extension is unloaded. in turn, close any references so they get closed. this
        # is not strictly necessary since the references will be deleted naturally when this object is deleted.
        self.__panel_ref.close()
        self.__panel_ref = None 
        