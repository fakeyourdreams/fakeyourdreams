from typing import Optional, List, Tuple
import gradio

import fakeyourdreams.globals
from fakeyourdreams import wording
from fakeyourdreams.uis.typing import File
from fakeyourdreams.common_helper import get_first
from fakeyourdreams.filesystem import has_audio, has_image, filter_audio_paths, filter_image_paths
from fakeyourdreams.uis.core import register_ui_component

SOURCE_FILE : Optional[gradio.File] = None
SOURCE_AUDIO : Optional[gradio.Audio] = None
SOURCE_IMAGE : Optional[gradio.Image] = None


def render() -> None:
	global SOURCE_FILE
	global SOURCE_AUDIO
	global SOURCE_IMAGE

	has_source_audio = has_audio(fakeyourdreams.globals.source_paths)
	has_source_image = has_image(fakeyourdreams.globals.source_paths)
	SOURCE_FILE = gradio.File(
		file_count = 'multiple',
		file_types =
		[
			'.mp3',
			'.wav',
			'.png',
			'.jpg',
			'.webp'
		],
		label = wording.get('uis.source_file'),
		value = fakeyourdreams.globals.source_paths if has_source_audio or has_source_image else None
	)
	source_file_names = [ source_file_value['name'] for source_file_value in SOURCE_FILE.value ] if SOURCE_FILE.value else None
	source_audio_path = get_first(filter_audio_paths(source_file_names))
	source_image_path = get_first(filter_image_paths(source_file_names))
	SOURCE_AUDIO = gradio.Audio(
		value = source_audio_path if has_source_audio else None,
		visible = has_source_audio,
		show_label = False
	)
	SOURCE_IMAGE = gradio.Image(
		value = source_image_path if has_source_image else None,
		visible = has_source_image,
		show_label = False
	)
	register_ui_component('source_audio', SOURCE_AUDIO)
	register_ui_component('source_image', SOURCE_IMAGE)


def listen() -> None:
	SOURCE_FILE.change(update, inputs = SOURCE_FILE, outputs = [ SOURCE_AUDIO, SOURCE_IMAGE ])


def update(files : List[File]) -> Tuple[gradio.Audio, gradio.Image]:
	file_names = [ file.name for file in files ] if files else None
	has_source_audio = has_audio(file_names)
	has_source_image = has_image(file_names)
	if has_source_audio or has_source_image:
		source_audio_path = get_first(filter_audio_paths(file_names))
		source_image_path = get_first(filter_image_paths(file_names))
		fakeyourdreams.globals.source_paths = file_names
		return gradio.Audio(value = source_audio_path, visible = has_source_audio), gradio.Image(value = source_image_path, visible = has_source_image)
	fakeyourdreams.globals.source_paths = None
	return gradio.Audio(value = None, visible = False), gradio.Image(value = None, visible = False)
