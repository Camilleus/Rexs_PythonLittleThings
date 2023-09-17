import dearpygui.dearpygui as dpg

dpg.create_context()


def save_callback():
    value = dpg.get_value("my_value")
    print(value)


with dpg.window(tag="Primary Window"):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(tag="my_value")


dpg.create_viewport(title='My Title is Unicorn', width=750, height=250)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
