import logging

L = logging.getLogger(__name__)

def depth(d):
	if isinstance(d, dict):
		return 1 + (max(map(depth, d.values())) if d else 0)
	return 0


def validate_append(to_append: dict):
	if depth(to_append) >= 2:
		for key in to_append.keys():
			if "image" in to_append[key].keys():
				return True
			else:
				raise ValueError("Image not specified")
	else:
		raise ValueError("Incorrect input")
