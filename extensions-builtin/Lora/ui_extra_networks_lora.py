import json
import os
import lora

from modules import shared, ui_extra_networks


class ExtraNetworksPageLora(ui_extra_networks.ExtraNetworksPage):
    def __init__(self):
        super().__init__('Lora')

    def refresh(self):
        lora.list_available_loras()

    def list_items(self):
        for name, lora_on_disk in lora.available_loras.items():
            path, ext = os.path.splitext(lora_on_disk.filename)
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
                "name": name,
                "filename": path,
                "preview": preview,
                "search_term": self.search_terms_from_path(lora_on_disk.filename),
                "prompt": f'{json.dumps(f"<lora:{name}:")} + opts.extra_networks_default_multiplier + '
                + json.dumps(">"),
                "local_preview": f"{path}.png",
            }

    def allowed_directories_for_previews(self):
        return [shared.cmd_opts.lora_dir]

