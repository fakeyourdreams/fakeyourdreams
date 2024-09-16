from typing import Optional, List
import gradio

import fakeyourdreams.globals
from fakeyourdreams import wording
from fakeyourdreams.uis import choices as uis_choices

COMMON_OPTIONS_CHECKBOX_GROUP : Optional[gradio.Checkboxgroup] = None


def render() -> None:
	global COMMON_OPTIONS_CHECKBOX_GROUP

	value = []
	if fakeyourdreams.globals.keep_temp:
		value.append('keep-temp')
	if fakeyourdreams.globals.skip_audio:
		value.append('skip-audio')
	if fakeyourdreams.globals.skip_download:
		value.append('skip-download')
	COMMON_OPTIONS_CHECKBOX_GROUP = gradio.Checkboxgroup(
		label = wording.get('uis.common_options_checkbox_group'),
		choices = uis_choices.common_options,
		value = value
	)


def listen() -> None:
	COMMON_OPTIONS_CHECKBOX_GROUP.change(update, inputs = COMMON_OPTIONS_CHECKBOX_GROUP)


def update(common_options : List[str]) -> None:
	fakeyourdreams.globals.keep_temp = 'keep-temp' in common_options
	fakeyourdreams.globals.skip_audio = 'skip-audio' in common_options
	fakeyourdreams.globals.skip_download = 'skip-download' in common_options
