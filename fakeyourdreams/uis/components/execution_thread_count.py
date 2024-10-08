from typing import Optional
import gradio

import fakeyourdreams.globals
import fakeyourdreams.choices
from fakeyourdreams import wording

EXECUTION_THREAD_COUNT_SLIDER : Optional[gradio.Slider] = None


def render() -> None:
	global EXECUTION_THREAD_COUNT_SLIDER

	EXECUTION_THREAD_COUNT_SLIDER = gradio.Slider(
		label = wording.get('uis.execution_thread_count_slider'),
		value = fakeyourdreams.globals.execution_thread_count,
		step = fakeyourdreams.choices.execution_thread_count_range[1] - fakeyourdreams.choices.execution_thread_count_range[0],
		minimum = fakeyourdreams.choices.execution_thread_count_range[0],
		maximum = fakeyourdreams.choices.execution_thread_count_range[-1]
	)


def listen() -> None:
	EXECUTION_THREAD_COUNT_SLIDER.release(update_execution_thread_count, inputs = EXECUTION_THREAD_COUNT_SLIDER)


def update_execution_thread_count(execution_thread_count : int = 1) -> None:
	fakeyourdreams.globals.execution_thread_count = execution_thread_count

