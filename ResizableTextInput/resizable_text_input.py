class ResizableTextInput:
    """
    V0.1
    A node that provides a resizable text input area, compatible with CLIP text encoder input.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "default_text": ("STRING", {"default": "", "multiline": True})
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "process"
    CATEGORY = "Autumn Nodes"
    
    def process(self, default_text=""):
        # Simply return the input text, making it compatible with CLIP text encoder
        return (default_text,)

# Node mapping for registration
NODE_CLASS_MAPPINGS = {
    "ResizableTextInput": ResizableTextInput
}

# Display names for UI
NODE_DISPLAY_NAME_MAPPINGS = {
    "ResizableTextInput": "Resizable Text Input"
}
