class TwoFloatValueSelector:
    """
    Autumn Nodes Fload Selector 0.1
    A ComfyUI node that allows selection between two float values (between 0 and 1)
    and outputs the selected value.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value_1": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.01}),
                "value_2": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.01}),
                "selection": (["value_1", "value_2"], {"default": "value_1"}),
            }
        }
    
    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "select_value"
    CATEGORY = "Autumn Nodes"
    
    def select_value(self, value_1, value_2, selection):
        if selection == "value_1":
            return (value_1,)
        else:  # selection == "value_2"
            return (value_2,)

# Register the node
NODE_CLASS_MAPPINGS = {
    "TwoFloatValueSelector": TwoFloatValueSelector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TwoFloatValueSelector": "Two Float Value Selector"
}
