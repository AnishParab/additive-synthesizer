import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

SAMPLE_RATE = 44100


def make_time_array(duration: float, sample_rate: int = SAMPLE_RATE) -> np.ndarray:
    """
    Returns an array of time values from 0 to duration (seconds).
    """
    return np.linspace(0, duration, int(sample_rate * duration), endpoint=False)


def sine_oscillator(
    freq: float,
    amplitude: float,
    duration: float,
    phase: float = 0.0,
    sample_rate: int = SAMPLE_RATE,
) -> np.ndarray:

    t = make_time_array(duration, sample_rate)

    return amplitude * np.sin(2 * np.pi * freq * t + phase)
