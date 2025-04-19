import torch

class LatentSwitch:
    """
    A switch node that allows toggling between two latent inputs
    """
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "switch": (["input1", "input2"], {"default": "input1"}),
            },
            "optional": {
                "input1": ("LATENT", ),
                "input2": ("LATENT", ),
            }
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("output",)
    FUNCTION = "switch_latents"
    CATEGORY = "latent"

    def switch_latents(self, switch, input1=None, input2=None):
        if switch == "input2":
            if input2 is None:
                raise ValueError("Input 2 selected but no latent connected to input2")
            return (input2,)
        else:
            if input1 is None:
                raise ValueError("Input 1 selected but no latent connected to input1")
            return (input1,)

NODE_CLASS_MAPPINGS = {
    "LatentSwitch": LatentSwitch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LatentSwitch": "Latent Switch"
}
