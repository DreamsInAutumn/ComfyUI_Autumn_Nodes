	Latent Switch
		Adds a selector node with two latent inputs and one output

   	Flux Transfer Nodes
    		Adds a from and To nodes with:
      			Model, Clip, Conditioning and VAE

  		The previous basic pipe nodes have required Positive and Negative conditioning, while flux only requires Positive.

    	Installation
		Add to the Custom nodes folder, restart

		example folder structure:
			custom_nodes/
			└── flux_transfer_node/
    				├── __init__.py
    				└── flux_node.py
