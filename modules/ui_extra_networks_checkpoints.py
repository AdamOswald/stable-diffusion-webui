import html
import json
import os
import urllib.parse

from modules import shared, ui_extra_networks, sd_models


class ExtraNetworksPageCheckpoints(ui_extra_networks.ExtraNetworksPage):
    def __init__(self):
        super().__init__('Checkpoints')

    def refresh(self):
        shared.refresh_checkpoints()

    def list_items(self):
        checkpoint: sd_models.CheckpointInfo
        for name, checkpoint in sd_models.checkpoints_list.items():
            path, ext = os.path.splitext(checkpoint.filename)
            previews = [f"{path}.png", f"{path}.preview.png"]

            preview = next(
                (
                    self.link_preview(file)
                    for file in previews
                    if os.path.isfile(file)
                ),
                None,
            )
            yield {
                "name": checkpoint.name_for_extra,
                "filename": path,
                "preview": preview,
                "search_term": f"{self.search_terms_from_path(checkpoint.filename)} "
                + (checkpoint.sha256 or ""),
                "onclick": f'"{html.escape(f"""return selectCheckpoint({json.dumps(name)})""")}"',
                "local_preview": f"{path}.png",
            }

    def allowed_directories_for_previews(self):
        return [v for v in [shared.cmd_opts.ckpt_dir, sd_models.model_path] if v is not None]

