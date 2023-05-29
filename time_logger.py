import time

class Time_logger:
	__instance = None
	__events_start_timestamps = {}
	__events_time = {}

	def __init__(self) -> None:
		'''
		Constructor to ensure that only one instance of this class can be created.
		'''
		if Time_logger.__instance != None:
			raise Exception('Singleton recreate. Just to be sure')
		else:
			Time_logger.__instance = self

	@staticmethod 
	def get_instance():
		'''
		Get the singleton instance of this class.
		'''
		if Time_logger.__instance == None:
			Time_logger()
		return Time_logger.__instance


	def start_timer_for_event(self, event_name : str) -> None:
		'''
		Start the timer for a given event.
		'''
		start = time.monotonic()
		self.__events_start_timestamps[event_name] = start


	def mark_timestamp_for_event(self, event_name : str) -> None:
		'''
		Mark the timestamp for a given event.
		'''
		end = time.monotonic()
		try:
			start = self.__events_start_timestamps[event_name]
		except KeyError:
			start = end
		duration = end - start
		self.__events_time[event_name] = duration


	def print_events(self) -> None:
		'''
		Print the recorded events and their durations.
		'''
		print('Time logger:')
		for key, value in self.__events_time.items():
			print(f'{key}: {value * 1000:.0f} ms')


