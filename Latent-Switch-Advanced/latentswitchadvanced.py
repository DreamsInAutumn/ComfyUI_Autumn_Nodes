import torch
class LatentSwitchAdvanced:
    """
    V0.6
    A switch node that allows toggling between two latent inputs
    """

    RETURN_TYPES = ("LATENT", "FLOAT")
    RETURN_NAMES = ("latent", "denoise")
    FUNCTION = "switch_latents"
    CATEGORY = "Autumn Nodes"
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "denoise_empty": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                "denoise_image": ("FLOAT", {"default": 0.72, "min": 0.0, "max": 1.0, "step": 0.01}),
                "latent_source": (["empty", "image"], {"default": "empty"}),
            },
            "optional": {
                "empty": ("LATENT", ),
                "image": ("LATENT", ),
            }
        }

    def switch_latents(self, latent_source, denoise_empty, denoise_image, empty=None, image=None):
        if latent_source == "image":
            return (image, denoise_image)
        else:
            return (empty, denoise_empty)

NODE_CLASS_MAPPINGS = {
    "LatentSwitchAdvanced": LatentSwitchAdvanced
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "LatentSwitchAdvanced": "LatentSwitchAdvanced"
}
