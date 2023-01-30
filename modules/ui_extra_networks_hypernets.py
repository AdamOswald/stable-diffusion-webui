import json
import os

from modules import shared, ui_extra_networks


class ExtraNetworksPageHypernetworks(ui_extra_networks.ExtraNetworksPage):
    def __init__(self):
        super().__init__('Hypernetworks')

    def refresh(self):
        shared.reload_hypernetworks()

    def list_items(self):
        for name, path in shared.hypernetworks.items():
            path, ext = os.path.splitext(path)
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
                "search_term": self.search_terms_from_path(path),
                "prompt": f'{json.dumps(f"<hypernet:{name}:")} + opts.extra_networks_default_multiplier + '
                + json.dumps(">"),
                "local_preview": f"{path}.png",
            }

    def allowed_directories_for_previews(self):
        return [shared.cmd_opts.hypernetwork_dir]

