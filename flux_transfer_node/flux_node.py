import torch
import comfy.utils
import comfy.model_management

class FluxTransferNode:
    """
    Autumn Nodes 0.2
    A custom node for ComfyUI designed to work with flux1-dev models.
    It contains two pipes:
    - FromPipe: with four inputs (model, clip, conditioning, vae) and one output
    - ToPipe: with one input and four outputs (model, clip, conditioning, vae)
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "conditioning": ("CONDITIONING",),
                "vae": ("VAE",),
            }
        }
    
    RETURN_TYPES = ("FLUX_PIPE",)
    FUNCTION = "from_pipe"
    CATEGORY = "Autumn Nodes"
    
    def from_pipe(self, model, clip, conditioning, vae):
        # Package the inputs into a single object
        flux_pipe = {
            "model": model,
            "clip": clip,
            "conditioning": conditioning,
            "vae": vae
        }
        return (flux_pipe,)


class FluxReceiveNode:
    """
    The receiving end of the FluxTransferNode.
    Takes a FLUX_PIPE input and unpacks it into the original four components.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "flux_pipe": ("FLUX_PIPE",),
            }
        }
    
    RETURN_TYPES = ("MODEL", "CLIP", "CONDITIONING", "VAE")
    FUNCTION = "to_pipe"
    CATEGORY = "Autumn Nodes"
    
    def to_pipe(self, flux_pipe):
        # Unpack the flux_pipe object
        return (
            flux_pipe["model"],
            flux_pipe["clip"],
            flux_pipe["conditioning"],
            flux_pipe["vae"]
        )


# Register the nodes
NODE_CLASS_MAPPINGS = {
    "FluxTransferFrom": FluxTransferNode,
    "FluxTransferTo": FluxReceiveNode
}

# Add descriptions
NODE_DISPLAY_NAME_MAPPINGS = {
    "FluxTransferFrom": "Flux From Pipe",
    "FluxTransferTo": "Flux To Pipe"
}
